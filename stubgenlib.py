from __future__ import absolute_import, annotations, division, print_function

import contextlib
import io
import itertools
import re
import tokenize
from collections import defaultdict
from typing import Any
from typing_extensions import Literal

from mypy.stubdoc import infer_sig_from_docstring, _TYPE_RE, _ARG_NAME_RE, is_valid_type
from mypy.stubgenc import (
    ArgSig,
    FunctionContext,
    FunctionSig,
    SignatureGenerator,
    DocstringSignatureGenerator as CDocstringSignatureGenerator,
)
from mypy.fastparse import parse_type_comment


class Notifier:
    """
    Class to display and filter warnings
    """

    def __init__(self) -> None:
        self._seen_msgs = defaultdict(int)
        self._seen_keys = defaultdict(int)
        self._modules: list[str] | None = None

    def set_modules(self, modules: list[str]) -> None:
        self._modules = modules

    def warn(self, key: str, module: str, msg: str) -> None:
        if (key, module, msg) not in self._seen_msgs:
            if self._modules is None or module in self._modules:
                print(f"({module}) {key}: {msg}")
        self._seen_msgs[(key, module, msg)] += 1
        self._seen_keys[key] += 1

    def print_summary(self) -> None:
        print()
        print("Warning Summary:")
        for key in sorted(self._seen_keys):
            count = self._seen_keys[key]
            print(f"  {key}: {count}")


class BaseSigFixer:
    """
    Mixin base class that handles the boilerplate of cleaning up a signature
    from an external source, such as documentation
    """

    def __init__(
        self, default_sig_handling: Literal["ignore", "merge"] = "merge"
    ) -> None:
        """
        default_sig_handling
            How to use the default signature.
            "ignore": only use the sigs from this generator. don't use the default sig.
            "merge": merge the sigs from this generator into the default.
        """
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
        self, type_name: str, ctx: FunctionContext, is_result: bool
    ) -> str:
        """Override this to implement logic to fix a type"""
        return type_name

    def cleanup_sig_types(self, sig: FunctionSig, ctx: FunctionContext) -> FunctionSig:
        args = []
        return_type = None
        invalid = []
        for arg in sig.args:
            type_name = None
            if arg.type:
                type_name = self.cleanup_type(arg.type, ctx, is_result=False)
                if not self.is_valid(type_name):
                    invalid.append(
                        "Invalid arg {} (orig: {} converted: {})".format(
                            repr(arg.name), repr(arg.type), repr(type_name)
                        )
                    )
                    type_name = None
            args.append(ArgSig(arg.name, type_name, arg.default))
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
        converted = FunctionSig(sig.name, args, return_type)

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
        sigs = super().get_function_sig(default_sig, ctx)
        if sigs:
            for i, sig in enumerate(sigs):
                sig = self.cleanup_sig_types(sig, ctx)
                if self.default_sig_handling == "ignore":
                    merged_sig = sig
                elif default_sig.is_identity() or (
                    default_sig.has_catchall_args()
                    and default_sig.ret_type == sig.ret_type
                ):
                    merged_sig = sig
                else:
                    merged_sig = default_sig.merge(sig)
                sigs[i] = merged_sig
        return sigs


class DocstringTypeFixer:
    """
    Mixin class that fixes human-defined types in docstrings
    """

    PYPATH = re.compile(r"((?:[a-zA-Z_][a-zA-Z0-9_]*)(?:[.][a-zA-Z_][a-zA-Z0-9_]*)*)")
    EPY_REG = re.compile(r"([LC]\{([^}]+)\})")
    LIST_OF_REG = re.compile(r"\b(list|Sequence|Iterable|Iterator) of (.*)")
    TUPLE_OF_REG = re.compile(r"\btuple of ([a-zA-Z0-9_.,() ]*)")
    SET_OF_REG = re.compile(r"\bset of ([a-zA-Z0-9_.]*)")
    NUMERIC_TUPLE_REG = re.compile(r"\b(int|float)\[(\d+)\]")

    REPLACEMENTS = [
        ('number', 'float'),
        ('List', 'list'),
        ('Dict', 'dict'),
        ('Type', 'type'),
        ('module', 'types.ModuleType'),
        ('traceback', 'types.TracebackType'),
        ('function', 'typing.Callable'),
        ('callable', 'typing.Callable'),
        ('hashable', 'typing.Hashable'),
        ('iterable', 'typing.Iterable'),
        ('class', 'type'),
        ('sequence', 'typing.Sequence'),
        ('generator', 'typing.Iterator'),
        ('buffer', 'typing_extensions.Buffer'),
        ('long', 'int'),
        ('strings?', 'str'),
        ('Str', 'str'),
        ('int_', 'int'),
        ('none', 'None'),
    ]

    def get_replacements(self, is_result: bool) -> list[tuple[str, str]]:
        repl = self.REPLACEMENTS
        if is_result:
            return repl + [('object', 'Any')]
        return repl

    def get_full_name(self, obj_name: str) -> str:
        return obj_name

    def cleanup_type(
        self, type_name: str, ctx: FunctionContext, is_result: bool
    ) -> str:
        type_name = type_name.replace('`', '')
        type_name = type_name.replace('\n', ' ')
        type_name = type_name.replace('<', '[')
        type_name = type_name.replace('>', ']')
        type_name = type_name.rstrip('.')
        type_name = self.EPY_REG.sub(lambda m: m.group(2), type_name).strip()

        type_name = re.sub(r'\bNoneType\b', 'None', type_name)

        # special case
        optional = False
        if type_name.endswith(', or None'):
            optional = True
            type_name = type_name[: len(', or None')]

        for find, replace in self.get_replacements(is_result):
            type_name = re.sub(r'\b{}\b'.format(find), replace, type_name)

        type_name = type_name.replace(' or ', ' | ')

        type_name = type_name.replace(
            'object convertible to a float', 'typing.SupportsFloat'
        )

        def list_sub(m) -> str:
            return "{}[{}]".format(m.group(1), m.group(2))

        type_name = self.LIST_OF_REG.sub(list_sub, type_name, count=1)

        def tuple_sub(m) -> str:
            members = [s.strip() for s in m.group(1).replace(" and ", " , ").split(",")]
            if len(members) == 1:
                members.append('...')
            return "tuple[{}]".format(", ".join(members))

        type_name = self.TUPLE_OF_REG.sub(tuple_sub, type_name, count=1)

        def set_sub(m) -> str:
            return "set[{}]".format(m.group(1))

        type_name = self.SET_OF_REG.sub(set_sub, type_name, count=1)

        def numeric_tuple_sub(m) -> str:
            count = int(m.group(2))
            return "tuple[{}]".format(', '.join([m.group(1)] * count))

        type_name = self.NUMERIC_TUPLE_REG.sub(numeric_tuple_sub, type_name, count=1)

        if optional:
            type_name = 'typing.Optional[{}]'.format(type_name)

        parts = []
        for part in self.PYPATH.split(type_name):
            if part and part[0].isalpha():
                parts.append(self.get_full_name(part))
            else:
                parts.append(part)
        return "".join(parts)


class DocstringSignatureGenerator(SignatureGenerator):
    """
    Generate signatures from docstrings.

    Unlike the built-in parser which targets signatures created by C++ binding
    generators, this works with standard docstring formats such as numpy,
    google, and epydoc (which Katana uses).
    """

    def prepare_docstring(self, docstr: str) -> str:
        return docstr

    def get_function_sig(
        self, default_sig: FunctionSig, ctx: FunctionContext
    ) -> list[FunctionSig] | None:
        import docstring_parser

        if ctx.docstr:
            parsed = docstring_parser.parse(self.prepare_docstring(ctx.docstr))
            args = []
            return_type = None
            if parsed.params:
                for param in parsed.params:
                    # param.default can be unreliable. in the case of google-style docs
                    # the default is parsed from human description, whereas is_optional is
                    # taken from a more concrete convention: `arg_name(list of in, optional)`
                    args.append(
                        ArgSig(
                            param.arg_name,
                            param.type_name,
                            default=param.is_optional,
                        )
                    )
            if parsed.returns:
                if parsed.returns.type_name:
                    return_type = parsed.returns.type_name
                elif parsed.returns.description and ":" in parsed.returns.description:
                    # the parser fails to extract the type when it encounters
                    # "list of {blah}" in google doctrings, so try a last ditch
                    # effort to grab the type
                    return_type = parsed.returns.description.split(":", 1)[0]
                else:
                    return_type = None

            sig = FunctionSig(ctx.name, args, return_type)
            return [sig]
        return None


class FixableDocstringSigGen(BaseSigFixer, DocstringSignatureGenerator):
    pass


class FixableCDocstringSigGen(BaseSigFixer, CDocstringSignatureGenerator):
    pass


class BoostDocstringSignatureGenerator(SignatureGenerator):
    """
    Parses boost-python style signatures
    """

    def get_function_sig(
        self, default_sig: FunctionSig, ctx: FunctionContext
    ) -> list[FunctionSig] | None:
        if ctx.docstr:
            return infer_sig_from_boost_docstring(ctx.docstr, ctx.name)
        return None


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
        return CFunctionStub(sig.name, sig.format_sig(suffix=""), is_abstract)

    @classmethod
    def _from_sigs(cls, sigs: list[FunctionSig], is_abstract=False) -> CFunctionStub:
        return CFunctionStub(
            sigs[0].name,
            '\n'.join(sig.format_sig(suffix="") for sig in sigs),
            is_abstract,
        )

    def __get__(self) -> None:
        """
        This exists to make this object look like a method descriptor and thus
        return true for CStubGenerator.ismethod()
        """
        pass


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
            if sig.args and sig.args[0].name == 'self':
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
    results = [sig for sig in sigs if sig not in redundant]
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


def boost_parser() -> None:
    from lark import Lark

    parser = Lark(
        r"""
        identifier : (CNAME ".")* CNAME

        type_list : type ("," type)*

        generic_type : identifier "[" type_list "]"

        ?base_type : ["unsigned" " "+] identifier | pointer_type | reference_type | const_type

        ?type : base_type | generic_type
        
        signature : identifier "(" [type_list] ")" ["const"]

        %import common.CNAME
        %import common.WS
        %ignore WS
        """,
        start='signature',
    )

    text = "Mari::ExportItem::setUvIndexList(QList<int> const&, int, char const*)"
    print(parser.parse(text).pretty())


# this is adapted from mypy.stubdoc

# States of the docstring parser.
STATE_INIT: Final = 1
STATE_FUNCTION_NAME: Final = 2
STATE_ARGUMENT_LIST: Final = 3
STATE_ARGUMENT_TYPE: Final = 4
STATE_ARGUMENT_DEFAULT: Final = 5
STATE_RETURN_VALUE: Final = 6
STATE_OPEN_BRACKET: Final = 7  # For generic types.


class BoostDocStringParser:
    """Parse function signatures in documentation."""

    def __init__(self, function_name: str, verbose: bool = False) -> None:
        # Only search for signatures of function with this name.
        self.function_name = function_name
        self.state = [STATE_INIT]
        self.accumulator = ""
        self.arg_type: str | None = None
        self.arg_name = ""
        self.arg_default: str | None = None
        self.ret_type = "tying.Any"
        self.defaults = False
        self.found = False
        self.args: list[ArgSig] = []
        # Valid signatures found so far.
        self.signatures: list[FunctionSig] = []
        self.verbose = verbose

    def debug(self, *msg) -> None:
        if self.verbose:
            print(*msg)

    def pop_state(self, reason) -> None:
        prev = self.state.pop()
        self.debug("pop state {} {} -> {}".format(reason, prev, self.state[-1]))

    def add_token(self, token: tokenize.TokenInfo) -> None:
        """Process next token from the token stream."""
        if (
            token.type == tokenize.NAME
            and token.string == self.function_name
            and self.state[-1] == STATE_INIT
        ):
            self.debug()
            self.debug("STATE_FUNCTION_NAME")
            self.state.append(STATE_FUNCTION_NAME)

        elif (
            token.type == tokenize.OP
            and token.string == "("
            and self.state[-1] == STATE_FUNCTION_NAME
        ):
            self.pop_state("START ARGS")
            self.accumulator = ""
            self.found = True
            self.debug("STATE_ARGUMENT_LIST")
            self.state.append(STATE_ARGUMENT_LIST)

        elif self.state[-1] == STATE_FUNCTION_NAME:
            # Reset state, function name not followed by '('.
            self.pop_state("RESET")

        elif (
            token.type == tokenize.OP
            and token.string == "("
            and self.state[-1] == STATE_ARGUMENT_LIST
        ):
            self.debug("STATE_ARGUMENT_TYPE")
            self.state.append(STATE_ARGUMENT_TYPE)

        elif (
            token.type == tokenize.OP
            and token.string == "["
            and self.state[-1] in (STATE_ARGUMENT_LIST, STATE_ARGUMENT_DEFAULT)
        ):
            self.debug("setting defaults")
            if self.defaults is False:
                self.defaults = "next"

        elif (
            token.type == tokenize.OP
            and token.string == "]"
            and self.state[-1] == STATE_ARGUMENT_LIST
        ):
            pass

        elif (
            token.type == tokenize.OP
            and token.string == ")"
            and self.state[-1] == STATE_ARGUMENT_TYPE
        ):
            self.arg_type = self.accumulator
            self.debug("accumulate type", repr(self.arg_type))
            self.accumulator = ""
            self.pop_state("END ARG TYPE")

        elif (
            token.type == tokenize.OP
            and token.string in ("[", "(", "{")
            and self.state[-1] != STATE_INIT
        ):
            self.accumulator += token.string
            self.debug("STATE_OPEN_BRACKET", token.string)
            self.state.append(STATE_OPEN_BRACKET)

        elif (
            token.type == tokenize.OP
            and token.string in ("]", ")", "}")
            and self.state[-1] == STATE_OPEN_BRACKET
        ):
            self.accumulator += token.string
            self.pop_state(f"END OPEN BRACKET {token.string}")

        elif (
            token.type == tokenize.OP
            and token.string == "="
            and self.state[-1] in (STATE_ARGUMENT_LIST, STATE_ARGUMENT_TYPE)
        ):
            if self.state[-1] == STATE_ARGUMENT_TYPE:
                self.arg_type = self.accumulator
                self.debug("STATE_ARGUMENT_DEFAULT. type", self.arg_type)
                self.pop_state("END ARG TYPE")
            else:
                self.arg_name = self.accumulator
                self.debug("STATE_ARGUMENT_DEFAULT. name", self.arg_name)
            self.accumulator = ""

            self.state.append(STATE_ARGUMENT_DEFAULT)

        elif (
            token.type == tokenize.OP
            and token.string in (",", ")")
            and self.state[-1] in (STATE_ARGUMENT_LIST, STATE_ARGUMENT_DEFAULT)
        ):
            if self.state[-1] == STATE_ARGUMENT_DEFAULT:
                self.arg_default = self.accumulator
                self.debug("accumulate default", repr(self.arg_default))
                self.pop_state("END ARG DEFAULT")
            elif self.state[-1] == STATE_ARGUMENT_LIST:
                self.arg_name = self.accumulator
                self.debug("accumulate arg_name", repr(self.arg_name))
                if not (
                    token.string == ")" and self.accumulator.strip() == ""
                ) and not _ARG_NAME_RE.match(self.arg_name):
                    # Invalid argument name.
                    self.debug("reset. invalid arg name", repr(self.arg_name))
                    self.reset()
                    return

            if token.string == ")":
                self.pop_state("END PAREN")

            # arg_name is empty when there are no args. e.g. func()
            if self.arg_name:
                default = True if self.defaults is True else bool(self.arg_default)
                if self.arg_type and not is_valid_type(self.arg_type):
                    arg_type = None
                else:
                    arg_type = self.arg_type

                self.args.append(
                    ArgSig(
                        name=self.arg_name,
                        type=arg_type,
                        default=default,
                    )
                )
                if self.defaults == "next":
                    self.defaults = True
            self.arg_name = ""
            self.arg_type = None
            self.arg_default = None
            self.accumulator = ""

        elif (
            token.type == tokenize.OP
            and token.string == "->"
            and self.state[-1] == STATE_INIT
        ):
            self.debug("STATE_RETURN_VALUE", repr(self.accumulator))
            self.accumulator = ""
            self.state.append(STATE_RETURN_VALUE)

        # ENDMAKER is necessary for python 3.4 and 3.5.
        elif (
            token.type in (tokenize.NEWLINE, tokenize.ENDMARKER)
            or token.type == tokenize.OP
            and token.string == ":"
        ) and self.state[-1] in (
            STATE_INIT,
            STATE_RETURN_VALUE,
        ):
            if self.state[-1] == STATE_RETURN_VALUE:
                if not is_valid_type(self.accumulator):
                    self.debug("reset: invalid return", repr(self.accumulator))
                    self.reset()
                    return
                self.ret_type = self.accumulator
                self.accumulator = ""
                self.pop_state("END RETURN")

            if self.found:
                self.signatures.append(
                    FunctionSig(
                        name=self.function_name, args=self.args, ret_type=self.ret_type
                    )
                )
                self.found = False
            self.args = []
            self.ret_type = "typing.Any"
            self.defaults = False
            # Leave state as INIT.
        else:
            self.debug("catchall", self.state[-1], repr(token.string))
            self.accumulator += token.string

    def reset(self) -> None:
        self.state = [STATE_INIT]
        self.args = []
        self.found = False
        self.accumulator = ""

    def get_signatures(self) -> list[FunctionSig]:
        """Return sorted copy of the list of signatures found so far."""

        def has_arg(name: str, signature: FunctionSig) -> bool:
            return any(x.name == name for x in signature.args)

        def args_kwargs(signature: FunctionSig) -> bool:
            return has_arg("*args", signature) and has_arg("**kwargs", signature)

        # Move functions with (*args, **kwargs) in their signature to last place.
        return list(sorted(self.signatures, key=lambda x: 1 if args_kwargs(x) else 0))


def infer_sig_from_boost_docstring(
    docstr: str | None, name: str
) -> list[FunctionSig] | None:
    if not docstr:
        return None

    state = BoostDocStringParser(name)
    # Return all found signatures, even if there is a parse error after some are found.
    with contextlib.suppress(tokenize.TokenError):
        try:
            tokens = tokenize.tokenize(io.BytesIO(docstr.encode("utf-8")).readline)
            for token in tokens:
                state.add_token(token)
        except IndentationError:
            return None
    sigs = state.get_signatures()
    return sigs

    # def is_unique_args(sig: FunctionSig) -> bool:
    #     """return true if function argument names are unique"""
    #     return len(sig.args) == len({arg.name for arg in sig.args})

    # # Return only signatures that have unique argument names. Mypy fails on non-unique arg names.
    # return [sig for sig in sigs if is_unique_args(sig)]
