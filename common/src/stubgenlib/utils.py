from __future__ import absolute_import, annotations, division, print_function

import itertools

from mypy.stubgenc import (
    ArgSig,
    FunctionContext,
    FunctionSig,
)


def insert_typevars(import_lines: str, typevars: list[str]) -> str:
    imports = import_lines.split("\n")
    if "import typing" not in imports:
        imports.append("import typing")
    return "\n".join(imports + typevars)


def merge_signatures(
    dest: FunctionSig, other: FunctionSig, force: bool = False
) -> FunctionSig:
    """Merge the `other` signature `dest`, returning a new signature.

    The other signature can have fewer arguments: args will be matched by position
    for special methods and name otherwise.

    If force is True, types from other signature will override this one even if
    this sig has non-None types.
    """
    args: list[ArgSig] = []
    if dest.is_special_method() and len(other.args) == len(dest.args):
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
        other_args = {arg.name: arg for arg in other.args}
        for arg in dest.args:
            if arg.name in other_args:
                other_arg = other_args[arg.name]
                if (arg.type is None or force) and other_arg.type is not None:
                    arg = ArgSig(
                        arg.name,
                        other_arg.type,
                        default=arg.default,
                        default_value=arg.default_value,
                    )
            args.append(arg)

    ret_type = dest.ret_type
    if (ret_type is None or force) and other.ret_type:
        ret_type = other.ret_type

    return FunctionSig(name=dest.name, args=args, ret_type=ret_type)


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
