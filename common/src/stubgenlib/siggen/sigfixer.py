from __future__ import absolute_import, annotations, division, print_function

import re

from mypy.fastparse import parse_type_comment
from mypy.stubgenc import (
    ArgSig,
    FunctionContext,
    FunctionSig,
    SignatureGenerator,
)
from typing_extensions import Literal

from stubgenlib.utils import merge_signatures


class SignatureFixer(SignatureGenerator):
    """
    Signature generator that handles the boilerplate of cleaning up a signature
    from an external source, such as documentation.

    This class should be subclassed to implement cleanup_type(), then paired
    with a concrete SignatureGenerator class (the fixer should come first).
    It will call super().get_function_sig() then apply the fixes defined by
    cleanup_type() to all types in the signatures.
    """

    def __init__(
        self,
        sig_gen: SignatureGenerator,
        default_sig_handling: Literal["ignore", "merge"] = "merge",
    ) -> None:
        """
        sig_gen: signature generator to call to get signatures to fix.
        default_sig_handling
            How to use the default signature.
            "ignore": only use the sigs from this generator. don't use the default sig.
            "merge": merge the sigs from this generator into the default.
        """
        self.sig_gen = sig_gen
        self.default_sig_handling = default_sig_handling

    @staticmethod
    def is_valid(type_name: str) -> bool:
        try:
            parse_type_comment(type_name, 0, 0, None)
        except Exception:
            return False
        else:
            return True

    def cleanup_type(
        self,
        type_name: str,
        ctx: FunctionContext,
        is_result: bool,
        default_value: str | None = None,
    ) -> str:
        """Override this to implement logic to fix a type"""
        return type_name

    def cleanup_sigs_types(
        self,
        sigs: list[FunctionSig],
        ctx: FunctionContext,
    ) -> list[FunctionSig]:
        """Call cleanup_type on the types of all sigs"""
        return [self.cleanup_sig_types(sig, ctx) for sig in sigs]

    def cleanup_sig_types(
        self, sig: FunctionSig, ctx: FunctionContext, docstring: str | None = None
    ) -> FunctionSig:
        """Call cleanup_type on the types of the sig (args and return type)"""
        args = []
        return_type = None
        invalid = []
        for arg in sig.args:
            type_name = None
            if arg.type:
                type_name = self.cleanup_type(
                    arg.type, ctx, is_result=False, default_value=arg.default_value
                )
                if not self.is_valid(type_name):
                    invalid.append(
                        "Invalid arg {} (orig: {} converted: {})".format(
                            repr(arg.name), repr(arg.type), repr(type_name)
                        )
                    )
                    type_name = None
            args.append(
                ArgSig(
                    arg.name,
                    type_name,
                    default=arg.default,
                    default_value=arg.default_value,
                )
            )
        if sig.ret_type:
            return_type = self.cleanup_type(sig.ret_type, ctx, is_result=True)
            if not self.is_valid(return_type):
                invalid.append(
                    "Invalid ret (orig: {} converted: {})".format(
                        repr(sig.ret_type), repr(return_type)
                    )
                )
                return_type = None

        # FIXME: only copy if something has changed?
        converted = sig._replace(args=args, ret_type=return_type)
        if docstring:
            converted = converted._replace(docstring=docstring)

        if invalid:
            print(f"Invalid type after cleanup: {ctx.fullname}")
            print("  orig: {}".format(sig.format_sig()))
            print("  new:  {}".format(converted.format_sig()))
            for item in invalid:
                print("  {}".format(item))

        return converted

    def get_function_sig(
        self, default_sig: FunctionSig, ctx: FunctionContext
    ) -> list[FunctionSig] | None:
        """Gets the signatures from sig_gen, then cleans up the types"""
        sigs = self.sig_gen.get_function_sig(default_sig, ctx)
        if sigs:
            for i, sig in enumerate(sigs):
                sig = self.cleanup_sig_types(sig, ctx)
                if self.default_sig_handling == "ignore":
                    merged_sig = sig
                elif default_sig.is_catchall_signature() or (
                    default_sig.has_catchall_args()
                    and default_sig.ret_type == sig.ret_type
                ):
                    merged_sig = sig
                else:
                    merged_sig = merge_signatures(default_sig, sig)
                sigs[i] = merged_sig
        return sigs


class DocstringTypeFixer(SignatureFixer):
    """
    fixes human-defined types in docstrings
    """

    PYPATH = re.compile(r"((?:[a-zA-Z_][a-zA-Z0-9_]*)(?:[.][a-zA-Z_][a-zA-Z0-9_]*)*)")
    EPY_REG = re.compile(r"([LC]\{([^}]+)\})")
    LIST_OF_REG = re.compile(r"\b(list|Sequence|Iterable|Iterator) of (.*)")
    TUPLE_OF_REG = re.compile(r"\btuple of ([a-zA-Z0-9_.,() ]*)")
    SET_OF_REG = re.compile(r"\bset of ([a-zA-Z0-9_.]*)")
    DICT_OF_REG = re.compile(r"\bdict of ([a-zA-Z0-9_.]*) (?:of|to) ([a-zA-Z0-9_.]*)")
    NUMERIC_TUPLE_REG = re.compile(r"\b(int|float)\[(\d+)\]")

    REPLACEMENTS = [
        ("number", "float"),
        ("List", "list"),
        ("Dict", "dict"),
        ("Type", "type"),
        ("module", "types.ModuleType"),
        ("traceback", "types.TracebackType"),
        ("function", "typing.Callable"),
        ("callable", "typing.Callable"),
        ("hashable", "typing.Hashable"),
        ("iterable", "typing.Iterable"),
        ("class", "type"),
        ("sequence", "typing.Sequence"),
        ("generator", "typing.Iterator"),
        ("buffer", "typing_extensions.Buffer"),
        ("long", "int"),
        ("strings?", "str"),
        ("Str", "str"),
        ("int_", "int"),
        ("none", "None"),
    ]

    def get_replacements(self, is_result: bool) -> list[tuple[str, str]]:
        repl = self.REPLACEMENTS
        if is_result:
            return repl + [("object", "Any")]
        return repl

    def get_full_name(self, obj_name: str) -> str:
        return obj_name

    def cleanup_type(
        self,
        type_name: str,
        ctx: FunctionContext,
        is_result: bool,
        default_value: str | None = None,
    ) -> str:
        type_name = type_name.replace("`", "")
        type_name = type_name.replace("\n", " ")
        type_name = type_name.replace("<", "[")
        type_name = type_name.replace(">", "]")
        type_name = type_name.rstrip(".")
        type_name = self.EPY_REG.sub(lambda m: m.group(2), type_name).strip()

        type_name = re.sub(r"\bNoneType\b", "None", type_name)

        # special case
        optional = False
        if type_name.endswith(", or None"):
            optional = True
            type_name = type_name[: len(", or None")]

        for find, replace in self.get_replacements(is_result):
            type_name = re.sub(r"\b{}\b".format(find), replace, type_name)

        type_name = type_name.replace(" or ", " | ")

        type_name = type_name.replace(
            "object convertible to a float", "typing.SupportsFloat"
        )

        def list_sub(m) -> str:
            return "{}[{}]".format(m.group(1), m.group(2))

        type_name = self.LIST_OF_REG.sub(list_sub, type_name, count=1)

        def tuple_sub(m) -> str:
            members = [s.strip() for s in m.group(1).replace(" and ", " , ").split(",")]
            if len(members) == 1:
                members.append("...")
            return "tuple[{}]".format(", ".join(members))

        type_name = self.TUPLE_OF_REG.sub(tuple_sub, type_name, count=1)

        def set_sub(m) -> str:
            return "set[{}]".format(m.group(1))

        type_name = self.SET_OF_REG.sub(set_sub, type_name, count=1)

        def dict_sub(m) -> str:
            return "dict[{}, {}]".format(m.group(1), m.group(2))

        type_name = self.DICT_OF_REG.sub(dict_sub, type_name, count=1)

        def numeric_tuple_sub(m) -> str:
            count = int(m.group(2))
            return "tuple[{}]".format(", ".join([m.group(1)] * count))

        type_name = self.NUMERIC_TUPLE_REG.sub(numeric_tuple_sub, type_name, count=1)

        if optional:
            type_name = "typing.Optional[{}]".format(type_name)

        parts = []
        for part in self.PYPATH.split(type_name):
            if part and part[0].isalpha():
                parts.append(self.get_full_name(part))
            else:
                parts.append(part)
        return "".join(parts)
