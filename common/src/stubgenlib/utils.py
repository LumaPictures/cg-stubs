from __future__ import absolute_import, annotations, division, print_function

import itertools
from dataclasses import dataclass, field

from mypy.stubgenc import (
    ArgSig,
    FunctionContext,
    FunctionSig,
)


@dataclass
class ArgGroups:
    pos_only: list[ArgSig] = field(default_factory=list)
    pos_or_kw: list[ArgSig] = field(default_factory=list)
    star_args: ArgSig | None = None
    kw_only: list[ArgSig] = field(default_factory=list)
    star_kwargs: ArgSig | None = None

    def all_args(self) -> list[ArgSig]:
        args = []
        if self.pos_only:
            args += self.pos_only + [ArgSig("/", None)]
        args += self.pos_or_kw
        if self.star_args:
            args += [self.star_args]
        args += self.kw_only
        if self.star_kwargs:
            args += [self.star_kwargs]
        return args


def insert_typevars(import_lines: str, typevars: list[str]) -> str:
    imports = import_lines.split("\n")
    if "import typing" not in imports:
        imports.append("import typing")
    return "\n".join(imports + typevars)


def merge_args_by_name(
    dest: list[ArgSig],
    other: list[ArgSig],
    force: bool = False,
    add_extra: bool = False,
) -> list[ArgSig]:
    args: list[ArgSig] = []
    other_args = {arg.name: arg for arg in other}
    for arg in dest:
        other_arg = other_args.pop(arg.name, None)
        if other_arg is not None:
            if (arg.type is None or force) and other_arg.type is not None:
                arg = ArgSig(
                    arg.name,
                    other_arg.type,
                    default=arg.default,
                    default_value=arg.default_value,
                )
        args.append(arg)
    if add_extra:
        args.extend(other_args.values())
    return args


def merge_signatures(
    dest: FunctionSig, other: FunctionSig, force: bool = False
) -> FunctionSig:
    """Merge the `other` signature into `dest`, returning a new signature.

    The other signature can have fewer arguments: args will be matched by position
    for special methods and name otherwise.

    If force is True, types from other signature will override dest one even if
    dest has non-None types.
    """
    if dest.is_special_method() and len(other.args) == len(dest.args):
        args: list[ArgSig] = []
        # ignore argument names for special methods
        for arg, other_arg in zip(dest.args, other.args):
            if (arg.type is None or force) and other_arg.type is not None:
                arg = ArgSig(
                    arg.name,
                    other_arg.type,
                    default=arg.default,
                    default_value=arg.default_value,
                )
            args.append(arg)
    else:
        # TODO: strict mode that ignores donor sig if arg length doesn't match?
        args = merge_args_by_name(dest.args, other.args)

    ret_type = dest.ret_type
    if (ret_type is None or force) and other.ret_type:
        ret_type = other.ret_type

    new_sig = FunctionSig(name=dest.name, args=args, ret_type=ret_type)
    other_docstring = getattr(other, "docstring", None)
    dest_docstring = getattr(dest, "docstring", None)
    if other_docstring is not None or dest_docstring is not None:
        new_sig.docstring = dest_docstring or other_docstring
    return new_sig


def is_star_arg(arg_name):
    return arg_name == "*" or (
        len(arg_name) >= 2 and arg_name[0] == "*" and arg_name[1] != "*"
    )


def get_arg_groups(sig: FunctionSig) -> ArgGroups:
    """
    def foo(pos_or_kw, **kwargs)
    def foo(pos_only, /, pos_or_kw, **kwargs)
    def foo(pos_only, /, pos_or_kw, *, kw_only, **kwargs)
    def foo(pos_or_kw, *, kw_only, **kwargs)
    """

    groups = ArgGroups()

    current = groups.pos_or_kw

    for arg in sig.args:
        if arg.name == "/":
            groups.pos_only = groups.pos_or_kw
            current = groups.pos_or_kw = []
        elif is_star_arg(arg.name):
            groups.star_args = arg
            current = groups.kw_only
        elif arg.name.startswith("**"):
            groups.star_kwargs = arg
            current = None
        else:
            current.append(arg)
    return groups


def merge_signature_kwargs(
    dest: FunctionSig,
    other: FunctionSig,
    force: bool = False,
    replace_kwargs=False,
) -> FunctionSig:
    """Replace **kwargs with keyword-only arguments.

    This is only safe if dest has **kwargs and source has keyword only args (i.e. a *-arg exists)

    Args:
        replace_kwargs: if True, remove **kwargs argumenet if any keyword replacements are made
    """
    dest_groups = get_arg_groups(dest)

    if dest_groups.star_kwargs is not None:
        # FIXME: handle name conflicts with other arg groups
        source_groups = get_arg_groups(other)
        dest_groups.kw_only = merge_args_by_name(
            dest_groups.kw_only, source_groups.kw_only, force=force, add_extra=True
        )
        if replace_kwargs:
            dest_groups.star_kwargs = None
        if source_groups.kw_only and dest_groups.star_args is None:
            dest_groups.star_args = ArgSig("*")

    ret_type = dest.ret_type
    if (ret_type is None or force) and other.ret_type:
        ret_type = other.ret_type

    new_sig = FunctionSig(
        name=dest.name, args=dest_groups.all_args(), ret_type=ret_type
    )
    other_docstring = getattr(other, "docstring", None)
    dest_docstring = getattr(dest, "docstring", None)
    if other_docstring is not None or dest_docstring is not None:
        new_sig.docstring = dest_docstring or other_docstring
    return new_sig


class CFunctionStub:
    """
    Class that mimics a C function in order to provide parseable docstrings.
    """

    def __init__(self, name: str, doc: str, is_abstract=False) -> None:
        # Use special dunder names so that this object is interpreted as desired during inspection.
        self.__name__ = name
        self.__doc__ = doc
        self.__abstractmethod__ = is_abstract

    @classmethod
    def _from_sig(cls, sig: FunctionSig, is_abstract=False) -> CFunctionStub:
        return CFunctionStub(
            sig.name, sig.format_sig().replace(": ...", ""), is_abstract
        )

    @classmethod
    def _from_sigs(cls, sigs: list[FunctionSig], is_abstract=False) -> CFunctionStub:
        return CFunctionStub(
            sigs[0].name,
            "\n".join(sig.format_sig().replace(": ...", "") for sig in sigs),
            is_abstract,
        )

    def __get__(self) -> None:
        """
        This exists to make this object look like a method descriptor and thus
        return true for InspectionStubGenerator.ismethod()
        """


# FIXME: should this include the return type?
def sig_sort_key(py_sig: FunctionSig) -> tuple[int, tuple[str, ...]]:
    return (len(py_sig.args), tuple([arg.name for arg in py_sig.args]))


def reduce_overloads(sigs: list[FunctionSig]) -> list[FunctionSig]:
    """
    Remove unsupported and redundant overloads.

    - Some overloads are a subset of other overloads and can be pruned.
    - Some methods implement both classmethod and instancemethod overloads, and mypy prevents
      mixing these and does not correctly analyze them. We have to drop one, and we've chosen
      to remove classmethods.  It is possible to implement a "universalmethod" decorator, but
      we could not use overloads to distinguish their arguments.
    """
    # remove dups (FunctionSig is not hashable, so it's a bit cumbersome)
    new_sigs = []
    classmethods = []
    instancmethods = []
    for sig in sigs:
        if sig not in new_sigs:
            if sig.args and sig.args[0].name == "self":
                instancmethods.append(sig)
            else:
                classmethods.append(sig)
            new_sigs.append(sig)
    if classmethods and instancmethods:
        new_sigs = instancmethods

    if len(new_sigs) <= 1:
        return new_sigs

    sigs = sorted(new_sigs, key=sig_sort_key, reverse=True)
    redundant = []
    for a, b in itertools.combinations(sigs, 2):
        if contains_other_overload(a, b):
            redundant.append(b)
        elif contains_other_overload(b, a):
            redundant.append(a)
    results = [sig for sig in new_sigs if sig not in redundant]
    if not results:
        print("removed too much")
        for x in sigs:
            print(x)
        raise ValueError
    # results.reverse()
    return results


def contains_other_overload(sig: FunctionSig, other: FunctionSig) -> bool:
    """
    Return whether an overload is fully covered by another overload, and thus redundant.
    """
    if other.ret_type != sig.ret_type:
        # not compatible
        return False
    num_other_args = len(other.args)
    if len(sig.args) < num_other_args:
        # other has more args, sig cannot contain other
        return False
    if sig.args[:num_other_args] == other.args and all(
        a.default for a in sig.args[num_other_args:]
    ):
        # sig contains all of other's args, and the remaining sig args all have defaults
        return True
    return False


def add_positional_only_args(ctx: FunctionContext, py_sig: FunctionSig) -> FunctionSig:
    """
    Analyze the signature and add a '/' argument if necessary to mark
    arguments which cannot be access by name.

    Before:
        def foo(arg0, arg1, this=True, that='with_default')
    After:
        def foo(arg0, arg1, /, this=True, that='with_default')

    Before:
        def foo(arg0, arg1, this=True, that)
    After:
        def foo(arg0, arg1, /, this=True, *, that)
    """
    from stubgenlib.siggen.boost import BoostDocstringSignatureGenerator

    args = []
    requires_pos_only: bool | None = None
    has_defaults: bool | None = False
    for arg_num, py_arg in enumerate(py_sig.args):
        if BoostDocstringSignatureGenerator.is_default_boost_arg(py_arg.name):
            if requires_pos_only is False:
                raise ValueError(
                    f"{ctx.fullname}: Unnamed argument appears after named one: {py_sig.format_sig()}"
                )
            requires_pos_only = True
        else:
            if requires_pos_only:
                # force arguments before this to be positional only
                args.append(ArgSig("/"))
            if not (arg_num == 0 and py_arg.name in ("self", "cls")):
                requires_pos_only = False

        if has_defaults is False and py_arg.default:
            has_defaults = True
        elif has_defaults and not py_arg.default:
            # force arguments after this to be keyword only
            args.append(ArgSig("*"))
            has_defaults = None

        args.append(py_arg)

    if requires_pos_only:
        # force arguments before this to be positional only
        args.append(ArgSig("/"))

    return py_sig._replace(args=args)


def get_mypy_ignore_directive(codes: list[str]) -> str:
    return '# mypy: disable-error-code="{}"\n\n'.format(", ".join(codes))
