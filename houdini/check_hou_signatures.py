"""Check the signatures in the hou stub against the ones hython really has.

    rez env houdini-22 -- hython check_hou_signatures.py [--class REGEX] [--stub PATH] </dev/null

SWIG generates most of `hou.py` with explicit python signatures, so they can be compared with
the stub's without calling anything.  This reports:

- renamed: a parameter the stub names differently, so passing it by keyword fails.
- parameters: parameters the stub has that the runtime doesn't, or the other way round.  For a
  function that takes `**kwargs` (houpythonportion's options), the stub's first parameters must
  be the runtime's explicit ones.
- required: parameters required in one and optional in the other.
- positional-only: functions SWIG wraps as `(self, *args)` (C++ overloads), and C builtins
  (`hou.getenv`), which take no keywords, but whose stub parameters aren't positional-only.
  A builtin without a text signature is called with an unknown keyword to find out, which
  CPython or the builtin's argument parsing rejects before it does anything.
- order: for those functions, positional parameters the stub orders differently from the C++
  declaration in the HDK's HOM headers, which is the order SWIG passes them in.
- types: parameter types the C++ type SWIG records for them can't take, `None` the stub allows
  for a C++ reference, `None` it rejects for a C++ pointer with a NULL default, and enums
  (`EnumValue[enum]`) that aren't the one a C++ default value belongs to (`HOM_nodeTypeFilter::
  NoFilter`; from the HOM headers).
- keywords: for functions SWIG wraps as `(*args, **kwargs)`, which check their keywords by name,
  the stub's keywords they reject and those they accept that the stub lacks.  They are found by
  calling the wrapper with each name and an unknown keyword, which fails in SWIG's argument
  parsing, before anything reaches C++.  If the names found don't account for every argument
  the wrapper takes, every identifier in `_hou.so` is tried.

Overloaded stub functions (`@overload`) are skipped, except for the positional-only check.
Exits with status 1 if anything is reported.
"""

from __future__ import annotations

import argparse
import ast
import collections
import inspect
import pathlib
import re
import subprocess
import sys
import types
from typing import Any, NamedTuple

import hou

STUB = pathlib.Path(__file__).parent / "stubs" / "hou-stubs" / "__init__.pyi"


def runtime_class(name: str) -> Any:
    if hasattr(hou, name):
        return getattr(hou, name)
    # Classes of hou's submodules are stubbed as `_<module>_<class>`, e.g. `_ik_Joint`.
    module, _, cls = name[1:].partition("_")
    return getattr(getattr(hou, module, None), cls, None)


def stub_params(func: ast.FunctionDef, is_method: bool) -> tuple[list[ast.arg], int]:
    """The positional parameters of a stub function, without self, and how many are optional."""
    params = func.args.posonlyargs + func.args.args
    if is_method and params and params[0].arg in ("self", "cls"):
        params = params[1:]
    return params, len(func.args.defaults)


def rejects_keywords(func: Any) -> bool:
    """Whether a C builtin without a text signature takes no keyword arguments."""
    try:
        func(__no_such_keyword__=None)
    except TypeError as e:
        return "takes no keyword arguments" in str(e)
    return False


def runtime_params(func: Any, is_method: bool) -> list[inspect.Parameter] | None:
    try:
        params = list(inspect.signature(func).parameters.values())
    except (TypeError, ValueError):
        if isinstance(func, types.BuiltinFunctionType) and rejects_keywords(func):
            return [inspect.Parameter("args", inspect.Parameter.VAR_POSITIONAL)]
        return None
    if is_method and params and params[0].name == "self":
        params = params[1:]
    return params


def check_function(
    qualname: str, overloads: list[ast.FunctionDef], func: Any, is_method: bool
) -> list[tuple[str, str]]:
    params = runtime_params(func, is_method)
    if params is None:
        return []
    kinds = {p.kind for p in params}
    if kinds == {inspect.Parameter.VAR_POSITIONAL}:
        return [
            ("positional-only", f"{qualname}({ast.unparse(f.args)})")
            for f in overloads
            if stub_params(f, is_method)[0] and not f.args.posonlyargs
        ]
    if len(overloads) > 1 or inspect.Parameter.VAR_POSITIONAL in kinds:
        return []
    stub, num_optional = stub_params(overloads[0], is_method)
    names = [p.arg for p in stub]
    runtime = [
        p
        for p in params
        if p.kind not in (inspect.Parameter.KEYWORD_ONLY, inspect.Parameter.VAR_KEYWORD)
    ]
    runtime_names = [p.name for p in runtime]
    if inspect.Parameter.VAR_KEYWORD in kinds:
        # houpythonportion's `(self, data, **opts)`: the stub spells the options out after the
        # runtime's own parameters, which must come first.
        names = names[: len(runtime_names)]
        num_optional = max(0, num_optional - (len(stub) - len(names)))
    if names != runtime_names:
        if len(names) == len(runtime_names):
            return [("renamed", f"{qualname}: stub {names}, runtime {runtime_names}")]
        return [("parameters", f"{qualname}: stub {names}, runtime {runtime_names}")]
    stub_required = names[: len(names) - num_optional]
    runtime_required = [p.name for p in runtime if p.default is inspect.Parameter.empty]
    if stub_required != runtime_required:
        return [
            (
                "required",
                f"{qualname}: stub {stub_required}, runtime {runtime_required}",
            )
        ]
    return []


def is_forwarder(func: Any) -> bool:
    """Whether a hou function is one hou.py makes to call houpythonportion's function of that
    name (`expandString = __createTopLevelFunc("expandString")`)."""
    return getattr(func, "__qualname__", "") == "__createTopLevelFunc.<locals>.new_func"


class _Signature:
    """A callable with a given signature, for check_function."""

    def __init__(self, signature: inspect.Signature) -> None:
        self.__signature__ = signature

    def __call__(self, *args: object, **kwargs: object) -> None: ...


def check_forwarder(node: ast.FunctionDef, func: Any) -> list[tuple[str, str]]:
    """Check a forwarder against the houpythonportion function it calls."""
    import houpythonportion

    target = getattr(houpythonportion, node.name, None)
    if target is None:
        # Calling it raises AttributeError: the stub should say it never returns.
        if node.returns is None or ast.unparse(node.returns) != "NoReturn":
            return [
                ("parameters", f"{node.name}: houpythonportion has no such function")
            ]
        return []
    # houpythonportion's functions are `@wraps(hou.<name>)`, whose __wrapped__ is the forwarder.
    signature = inspect.signature(target, follow_wrapped=False)
    return check_function(node.name, [node], _Signature(signature), False)


# What check_keywords found for each function: (required in order, optional, argument count).
RUNTIME_KEYWORDS: dict[str, tuple[list[str], list[str], int | None]] = {}

# Passed with every probe, so that SWIG's argument parsing always fails before anything reaches
# C++: with a missing required argument if there is one, otherwise with this unknown keyword.
BOGUS = "zz_not_a_parameter"
HOU_SO = pathlib.Path(hou.__file__).with_name("_hou.so")


class SwigLibrary:
    """Reads the keyword names that _hou.so's SWIG wrappers accept, from their machine code.

    Each wrapper builds its `kwnames` array on the stack from the addresses of string
    constants, so the names are the identifier strings it loads: directly with `lea`, or, where
    the compiler vectorized the stores, from a constant pool of pointers that the dynamic linker
    relocates (`vmovq`/`vmovdqa` of an `xmm`/`ymm` register).
    """

    def __init__(self, path: pathlib.Path) -> None:
        import struct

        self.path = path
        self.data = path.read_bytes()
        shoff = struct.unpack_from("<Q", self.data, 0x28)[0]
        shentsize, shnum = struct.unpack_from("<HH", self.data, 0x3A)
        # (address, size, file offset) of each section that occupies space in the file
        self.sections = [
            (addr, size, offset)
            for _, kind, _, addr, offset, size, *_ in (
                struct.unpack_from("<IIQQQQIIQQ", self.data, shoff + i * shentsize)
                for i in range(shnum)
            )
            if addr and kind != 8  # SHT_NOBITS
        ]
        # The addresses the dynamic linker writes into pointer slots (R_X86_64_RELATIVE relocations).
        self.relocations: dict[int, int] = {}
        for _, kind, _, _, offset, size, *_ in (
            struct.unpack_from("<IIQQQQIIQQ", self.data, shoff + i * shentsize)
            for i in range(shnum)
        ):
            if kind == 4:  # SHT_RELA
                for position in range(offset, offset + size, 24):
                    slot, info, addend = struct.unpack_from("<QQq", self.data, position)
                    if info & 0xFFFFFFFF == 8:
                        self.relocations[slot] = addend
        symbols = subprocess.run(
            ["nm", "-S", "--defined-only", str(path)], capture_output=True, text=True
        ).stdout
        self.wrappers = {
            name.removeprefix("_wrap_"): (int(addr, 16), int(size, 16))
            for addr, size, _, name in (
                line.split() for line in symbols.splitlines() if " _wrap_" in line
            )
        }

    def string_at(self, address: int) -> str | None:
        for start, size, offset in self.sections:
            if start <= address < start + size:
                position = offset + address - start
                return self.data[position : self.data.index(b"\0", position)].decode(
                    errors="replace"
                )
        return None

    def keywords(self, wrapper: str) -> set[str] | None:
        if wrapper not in self.wrappers:
            return None
        start, size = self.wrappers[wrapper]
        code = subprocess.run(
            [
                "objdump",
                "-d",
                "--no-show-raw-insn",
                f"--start-address={start}",
                f"--stop-address={start + size}",
                str(self.path),
            ],
            capture_output=True,
            text=True,
        ).stdout
        pointers = []
        for instruction, register, address in re.findall(
            r"\t(\w+)\s+[-0-9a-fx]*\(%rip\),%(\w+)\s+# ([0-9a-f]+)", code
        ):
            address = int(address, 16)
            if instruction == "lea":
                pointers.append(address)
            elif register.startswith(("xmm", "ymm")):
                width = (
                    32
                    if register.startswith("ymm")
                    else 8
                    if instruction.endswith("q")
                    else 16
                )
                pointers += [
                    self.relocations[a]
                    for a in range(address, address + width, 8)
                    if a in self.relocations
                ]
        names = set()
        for pointer in pointers:
            text = self.string_at(pointer)
            if text and re.fullmatch(r"[a-z][A-Za-z0-9_]*", text):
                names.add(text)
        return names


_swig_library: list[SwigLibrary] = []


def swig_library() -> SwigLibrary:
    if not _swig_library:
        _swig_library.append(SwigLibrary(HOU_SO))
    return _swig_library[0]


def parse_error(call: Any, args: tuple[Any, ...], kwargs: dict[str, Any]) -> str:
    try:
        call(*args, **kwargs)
    except BaseException as exc:  # noqa: BLE001 - only the message matters
        return str(exc)
    return ""


def runtime_keywords(
    call: Any, self_args: tuple[Any, ...], hints: tuple[set[str], ...]
) -> tuple[list[str], set[str], int | None]:
    """The required keywords of a `(*args, **kwargs)` SWIG wrapper, in order, its optional ones,
    and how many arguments it takes."""
    required: list[str] = []
    while True:
        missing = re.search(
            r"missing required argument '(\w+)'",
            parse_error(call, self_args, {**dict.fromkeys(required), BOGUS: None}),
        )
        if not missing:
            break
        required.append(missing.group(1))
    count = re.search(
        r"(\w+)\(\) takes at most (\d+)",
        parse_error(call, (*self_args, *[None] * 99), {}),
    )
    if not count:
        return required, set(), None
    loaded = swig_library().keywords(count.group(1)) or set()
    total = int(count.group(2))

    def probe(name: str) -> bool | None:
        """Whether the wrapper accepts a keyword, or None if the probe can't tell."""
        error = parse_error(
            call, self_args, {**dict.fromkeys(required), name: None, BOGUS: None}
        )
        if f"'{BOGUS}'" in error:
            return True
        # With every slot filled, the argument count is checked before the names.
        return None if "takes at most" in error else False

    results = {name: probe(name) for name in sorted(loaded - {"self", *required})}
    optional = {name for name, ok in results.items() if ok}
    # The wrapper loads other strings too (default values such as 'xyz'), so names the probe
    # can't settle only fill the slots left: all of them if they fit, otherwise those the stub
    # uses, then those the docs mention.
    slots = total - len(self_args) - len(required) - len(optional)
    unsure = [name for name, ok in results.items() if ok is None]
    for tier in (unsure, *hints):
        chosen = [name for name in unsure if name in tier and name not in optional]
        if chosen and len(chosen) <= slots:
            optional.update(chosen)
            slots -= len(chosen)
    return required, optional, total


HOM_HEADERS = pathlib.Path(hou.__file__).parents[2] / "toolkit" / "include" / "HOM"


def split_top_level(text: str) -> list[str]:
    """Split C++ parameters at the commas outside brackets."""
    parts, depth, current = [], 0, ""
    for char in text:
        if char in "<([{":
            depth += 1
        elif char in ">)]}":
            depth -= 1
        if char == "," and depth == 0:
            parts.append(current)
            current = ""
        else:
            current += char
    return [part.strip() for part in [*parts, current] if part.strip()]


class CppParam(NamedTuple):
    name: str
    type: str  # e.g. "HOM_EnumValue *", "const char *", "double"
    default: str | None


def header_signatures(qualname: str) -> list[list[CppParam]]:
    """The parameters of each C++ declaration of a HOM method, from the HDK headers.

    SWIG passes positional arguments in this order, and takes the same names as keywords.
    """
    cls, _, name = qualname.rpartition(".")
    if name == "__init__":
        name = f"HOM_{cls}"
    header = HOM_HEADERS / (f"HOM_{cls.lstrip('_')}.h" if cls else "HOM_Module.h")
    if not header.exists():
        return []
    text = re.sub(
        r"//[^\n]*|/\*.*?\*/", "", header.read_text(errors="replace"), flags=re.S
    )
    signatures = []
    for match in re.finditer(rf"\b{re.escape(name)}\s*\(", text):
        depth, end = 1, match.end()
        while depth and end < len(text):
            depth += {"(": 1, ")": -1}.get(text[end], 0)
            end += 1
        params = []
        for param in split_top_level(text[match.end() : end - 1]):
            declaration, _, default = param.partition("=")
            identifier = re.search(r"(\w+)\s*(?:\[\s*\])?$", declaration.strip())
            if identifier and identifier.group(1) not in ("void", "const"):
                cpp_type = declaration.strip()[: identifier.start()].strip()
                params.append(
                    CppParam(identifier.group(1), cpp_type, default.strip() or None)
                )
        signatures.append(params)
    return signatures


def check_keywords(
    qualname: str,
    overloads: list[ast.FunctionDef],
    call: Any,
    self_args: tuple[Any, ...],
    constructor: bool = False,
) -> list[tuple[str, str]]:
    """Compare the stub's keywords for a `(*args, **kwargs)` SWIG wrapper with those it accepts."""
    if constructor and "No constructor defined" in parse_error(call, (), {}):
        return []
    has_self = bool(self_args) or constructor
    stub_names: list[str] = []
    for func in overloads:
        params = stub_params(func, has_self)[0] + func.args.kwonlyargs
        stub_names += [p.arg for p in params if p.arg not in stub_names]
    doc = getattr(call, "__doc__", None) or ""
    snake = {re.sub(r"(?<=[a-z])(?=[A-Z])", "_", name).lower() for name in stub_names}
    hints = ({*stub_names, *snake}, set(re.findall(r"\b[a-z_][a-z0-9_]*\b", doc)))
    required, optional, total = runtime_keywords(call, self_args, hints)
    RUNTIME_KEYWORDS[qualname] = (required, sorted(optional), total)
    runtime = set(required) | optional
    found = []
    rejected = [name for name in stub_names if name not in runtime]
    missing = [
        name for name in [*required, *sorted(optional)] if name not in stub_names
    ]
    if rejected or missing:
        found.append(
            (
                "keywords",
                f"{qualname}: stub has {rejected}, runtime has {missing} instead",
            )
        )
    if len(overloads) == 1 and not rejected:
        func = overloads[0]
        params, num_optional = stub_params(func, has_self)
        stub_required = [p.arg for p in params[: len(params) - num_optional]]
        if stub_required != required:
            found.append(
                ("required", f"{qualname}: stub {stub_required}, runtime {required}")
            )
    if not rejected and len(overloads) == 1:
        order = [p.arg for p in stub_params(overloads[0], has_self)[0]]
        declared = [
            [p.name for p in params]
            for params in header_signatures(qualname)
            if {p.name for p in params} == runtime
        ]
        if (
            declared
            and [n for n in declared[0] if n in order]
            != order[: len([n for n in declared[0] if n in order])]
        ):
            found.append(("order", f"{qualname}: stub {order}, C++ {declared[0]}"))
    if total is None:
        found.append(("keywords", f"{qualname}: could not find its SWIG wrapper"))
    elif len(runtime) + len(self_args) != total:
        found.append(
            (
                "keywords",
                f"{qualname}: takes {total} arguments, found the keywords {sorted(runtime)}",
            )
        )
    return found


def is_no_constructor_stub(func: ast.FunctionDef) -> bool:
    """Whether a stub `__init__` is the form that rejects every call (see stubgen_houdini.py)."""
    args = func.args
    return (
        [a.arg for a in args.posonlyargs + args.args] == ["self"]
        and args.vararg is None
        and args.kwarg is None
        and [
            (a.arg, ast.unparse(a.annotation) if a.annotation else None)
            for a in args.kwonlyargs
        ]
        == [("no_constructor", "Never")]
        and args.kw_defaults == [None]
    )


def takes_only_cpp_types(cls: Any) -> bool:
    """Whether every parameter of a SWIG constructor is a C++ type python has no class for."""
    params = runtime_params(cls.__dict__.get("__init__"), True)
    if not params:
        return False
    annotations = [p.annotation for p in params if isinstance(p.annotation, str)]
    return len(annotations) == len(params) and all(
        not hasattr(hou, re.sub(r"\W", "", a)) and re.search(r"\bUT_\w+", a)
        for a in annotations
    )


def check_constructor(
    qualname: str, overloads: list[ast.FunctionDef], cls: Any
) -> list[tuple[str, str]]:
    """Check that the stub rejects constructing exactly the classes SWIG gives no constructor.

    hou's submodules (`hou.anim`, ...) are instances of such classes.
    """
    runtime = cls if isinstance(cls, type) else type(cls)
    stubbed = any(is_no_constructor_stub(func) for func in overloads)
    # SWIG's constructors without a C++ one take (*args, **kwargs); don't construct the others.
    if not stubbed and not takes_keywords(runtime.__dict__.get("__init__")):
        return []
    rejected = "No constructor defined" in parse_error(
        runtime, (), {}
    ) or takes_only_cpp_types(runtime)
    if rejected and not stubbed:
        return [
            (
                "constructor",
                f"{qualname}: SWIG defines no constructor, but the stub's can be called",
            )
        ]
    if stubbed and not rejected:
        return [
            (
                "constructor",
                f"{qualname}: the stub rejects every call, but SWIG defines a constructor",
            )
        ]
    return []


def takes_keywords(func: Any) -> bool:
    params = runtime_params(func, False)
    return params is not None and {p.kind for p in params} >= {
        inspect.Parameter.VAR_POSITIONAL,
        inspect.Parameter.VAR_KEYWORD,
    }


# What a stub type may be for each C++ parameter type SWIG records in hou.py's signatures.
SCALARS = {
    "bool": {
        "bool",
        "int",
    },  # SWIG converts any object by truthiness, but documents bool
    "int": {"int", "bool"},
    "int64": {"int", "bool"},
    "long": {"int"},
    "ptrdiff_t": {"int"},
    "double": {"float", "int"},
    "float": {"float", "int"},
    "char const *": {"str"},
    "std::string const &": {"str"},
    "std::string": {"str"},
    "str": {"str"},
    "HOM_BinaryString": {"bytes", "str"},
    "EnumValue": {"EnumValue"},
}
TYPED_ENUM_VALUE = re.compile(r"\bEnumValue\[(?:hou\.)?(\w+)\]")
SWIG_TUPLES = {
    "_DoubleTuple": "float",
    "_FloatTuple": "float",
    "_IntTuple": "int",
    "_Int64Tuple": "int",
    "_StringTuple": "str",
    "_EnumTuple": "EnumValue",
}
SEQUENCES = {"Sequence", "Iterable", "list", "tuple", "Tuple", "Collection"}
# HOM's typemaps also take a sequence of floats for these.
FROM_SEQUENCE = {
    "Vector2",
    "Vector3",
    "Vector4",
    "Matrix2",
    "Matrix3",
    "Matrix4",
    "Quaternion",
    "Color",
}
NUMERIC = {"float": {"float", "int"}, "int": {"int", "bool"}}


def union_members(annotation: str) -> list[str]:
    members, depth, current = [], 0, ""
    for char in annotation:
        depth += {"[": 1, "]": -1}.get(char, 0)
        if char == "|" and depth == 0:
            members.append(current.strip())
            current = ""
        else:
            current += char
    result = []
    for member in (m.strip("'\" ") for m in [*members, current] if m.strip()):
        optional = re.fullmatch(r"(?:typing\.)?Optional\[(.*)\]", member)
        result += [*union_members(optional.group(1)), "None"] if optional else [member]
    return result


def member_head(member: str) -> tuple[str, str | None]:
    generic = re.fullmatch(r"([\w.]+)\[(.*)\]", member)
    if generic:
        return generic.group(1).split(".")[-1], generic.group(2)
    return member.split(".")[-1], None


def accepts(cpp_type: str, member: str) -> bool | None:
    """Whether C++ can take a value of one member of a stub's union type (None: can't tell)."""
    name, inner = member_head(member)
    if name == "_FloatSequence":
        name, inner = "Sequence", "float"
    if name in ("Any", "object") or name == "None":
        return None
    if cpp_type in SCALARS:
        return name in SCALARS[cpp_type] or (
            name == "Literal" and SCALARS[cpp_type] & {"str", "int"} != set()
        )
    if cpp_type in SWIG_TUPLES:
        element = SWIG_TUPLES[cpp_type]
        if name not in SEQUENCES:
            return element == "float" and name in FROM_SEQUENCE
        if inner is None:
            return True
        first = member_head(union_members(split_top_level(inner)[0])[0])[0]
        return first in NUMERIC.get(element, {element})
    tuple_of = re.fullmatch(r"_(\w+)Tuple", cpp_type)
    if tuple_of:
        if name not in SEQUENCES or inner is None:
            return name in SEQUENCES
        element = member_head(union_members(split_top_level(inner)[0])[0])[0]
        if tuple_of.group(1) == "Bool":
            return element in ("bool", "int")
        element_class, cpp_class = (
            getattr(hou, element, None),
            getattr(hou, tuple_of.group(1), None),
        )
        if isinstance(element_class, type) and isinstance(cpp_class, type):
            return issubclass(element_class, cpp_class)
        return None
    cpp_class = getattr(hou, cpp_type, None)
    if isinstance(cpp_class, type):
        stub_class = getattr(hou, name, None)
        if isinstance(stub_class, type):
            return issubclass(stub_class, cpp_class)
        return name in SEQUENCES and cpp_type in FROM_SEQUENCE
    return None


def swig_type(cpp_type: str) -> str:
    """A C++ parameter type from a HOM header, as SWIG names it in hou.py's signatures."""
    base = re.sub(r"\bconst\b|&", "", cpp_type).strip()
    vector = re.fullmatch(r"std::vector<\s*(.*?)\s*\*?\s*>", base)
    if vector:
        element = {
            "std::string": "String",
            "double": "Double",
            "float": "Float",
            "int": "Int",
            "int64": "Int64",
            "bool": "Bool",
        }
        inner = vector.group(1).strip()
        return f"_{element.get(inner, inner.removeprefix('HOM_'))}Tuple"
    if re.fullmatch(r"char\s*\*", base):
        return "char const *"
    if base == "std::string":
        return "std::string const &"
    return base.rstrip("* ").removeprefix("HOM_")


def check_types(
    qualname: str, func: ast.FunctionDef, runtime: Any
) -> list[tuple[str, str]]:
    """Compare a stub function's parameter types with the C++ types SWIG records for them (or,
    for a `(*args, **kwargs)` wrapper, the HOM headers declare), and with whether C++ takes None
    (a pointer with a NULL default does; a reference doesn't)."""
    try:
        cpp_types = {
            p.name: p.annotation
            for p in inspect.signature(runtime).parameters.values()
            if isinstance(p.annotation, str)
        }
    except (TypeError, ValueError):
        return []
    if not cpp_types:
        names = {a.arg for a in func.args.args + func.args.kwonlyargs} - {"self"}
        for params in header_signatures(qualname):
            if {p.name for p in params} == names:
                cpp_types = {p.name: swig_type(p.type) for p in params}
    stub = {
        a.arg: a.annotation
        for a in func.args.posonlyargs + func.args.args + func.args.kwonlyargs
        if a.annotation is not None
    }
    declared = {
        p.name: p
        for params in header_signatures(qualname)
        if {p.name for p in params} >= set(cpp_types) - {"self"}
        for p in params
    }
    found = []
    for name, cpp_type in cpp_types.items():
        if name not in stub:
            continue
        annotation = ast.unparse(stub[name])
        members = union_members(annotation)
        verdicts = [accepts(cpp_type, member) for member in members]
        if (
            verdicts
            and all(v is False for v in verdicts if v is not None)
            and any(v is False for v in verdicts)
        ):
            found.append(
                ("types", f"{qualname}({name}): stub {annotation}, C++ {cpp_type}")
            )
            continue
        cpp = declared.get(name)
        default_enum = (
            re.fullmatch(r"HOM_(\w+)::\w+", cpp.default)
            if cpp and cpp.default
            else None
        )
        enums = [e.lstrip("_") for e in TYPED_ENUM_VALUE.findall(annotation)]
        if cpp and default_enum and enums and default_enum.group(1) not in enums:
            found.append(
                (
                    "types",
                    f"{qualname}({name}): stub {annotation}, C++ default {cpp.default}",
                )
            )
        if cpp is None or cpp_type == "char const *" or "InterpreterObject" in cpp.type:
            continue
        pointer = "*" in cpp.type
        null_default = cpp.default in ("NULL", "nullptr", "0") and pointer
        if (
            "None" in members
            and not pointer
            and cpp_type not in ("InterpreterObject",)
            and accepts(cpp_type, members[0]) is not None
        ):
            found.append(
                (
                    "types",
                    f"{qualname}({name}): stub {annotation} takes None, C++ {cpp.type} doesn't",
                )
            )
        elif (
            null_default
            and "None" not in members
            and not any(m in ("Any", "object") for m in members)
        ):
            found.append(
                (
                    "types",
                    f"{qualname}({name}): stub {annotation} rejects None, C++ {cpp.type} = {cpp.default} takes it",
                )
            )
    return found


def main() -> int:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument(
        "--class",
        dest="cls",
        default=None,
        help="only check classes matching this regex",
    )
    parser.add_argument(
        "--dump",
        type=pathlib.Path,
        default=None,
        help="write the keywords found to this JSON file",
    )
    parser.add_argument(
        "--stub",
        type=pathlib.Path,
        default=STUB,
        help=f"default: {STUB.relative_to(STUB.parents[2])}",
    )
    args = parser.parse_args()

    tree = ast.parse(args.stub.read_text())
    issues: list[tuple[str, str]] = []
    for node in tree.body:
        if (
            isinstance(node, ast.FunctionDef)
            and args.cls is None
            and hasattr(hou, node.name)
        ):
            func = getattr(hou, node.name)
            if is_forwarder(func):
                issues += check_forwarder(node, func)
            elif takes_keywords(func):
                issues += check_keywords(node.name, [node], func, ())
            else:
                issues += check_function(node.name, [node], func, False)
        if not isinstance(node, ast.ClassDef) or (
            args.cls and not re.search(args.cls, node.name)
        ):
            continue
        cls = runtime_class(node.name)
        if cls is None:
            continue
        functions: dict[str, list[ast.FunctionDef]] = collections.defaultdict(list)
        for func in node.body:
            if isinstance(func, ast.FunctionDef):
                functions[func.name].append(func)
        for name, overloads in functions.items():
            qualname = f"{node.name}.{name}"
            if name == "__init__":
                issues += check_constructor(qualname, overloads, cls)
                if takes_keywords(cls.__dict__.get("__init__")):
                    issues += check_keywords(
                        qualname, overloads, cls, (), constructor=True
                    )
                continue
            runtime = cls.__dict__.get(name)
            if name.startswith("__") or runtime is None or not callable(runtime):
                continue
            is_method = not isinstance(runtime, staticmethod) and not inspect.ismodule(
                cls
            )
            if takes_keywords(runtime):
                issues += check_keywords(
                    qualname,
                    overloads,
                    getattr(cls, name),
                    (None,) if is_method else (),
                )
                if len(overloads) == 1:
                    issues += check_types(qualname, overloads[0], runtime)
            else:
                issues += check_function(qualname, overloads, runtime, is_method)
                if len(overloads) == 1:
                    issues += check_types(qualname, overloads[0], runtime)

    if args.dump:
        import json

        args.dump.write_text(json.dumps(RUNTIME_KEYWORDS, indent=1))
    by_kind: dict[str, list[str]] = collections.defaultdict(list)
    for kind, text in issues:
        by_kind[kind].append(text)
    for kind in (
        "constructor",
        "renamed",
        "parameters",
        "required",
        "positional-only",
        "keywords",
        "order",
        "types",
    ):
        print(f"== {kind}: {len(by_kind[kind])}")
        for text in by_kind[kind]:
            print(f"   {text}")
    return 1 if issues else 0


if __name__ == "__main__":
    sys.exit(main())
