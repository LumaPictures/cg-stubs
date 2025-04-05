from __future__ import absolute_import, annotations, division, print_function

import contextlib
import io
import re
import tokenize

from mypy.stubdoc import _ARG_NAME_RE, is_valid_type
from mypy.stubgenc import (
    ArgSig,
    FunctionContext,
    FunctionSig,
    SignatureGenerator,
)
from typing_extensions import Final

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
        self.ret_type = "typing.Any"
        self.defaults: str | bool = False
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


class BoostDocstringSignatureGenerator(SignatureGenerator):
    """
    Parses boost-python style signatures
    """

    def get_function_sig(
        self, default_sig: FunctionSig, ctx: FunctionContext
    ) -> list[FunctionSig] | None:
        if ctx.docstring:
            return infer_sig_from_boost_docstring(ctx.docstring, ctx.name)
        return None

    @classmethod
    def is_default_boost_arg(cls, arg_name: str) -> bool:
        return bool(re.match("^arg[0-9]+$", arg_name))


# def boost_parser() -> None:
#     from lark import Lark
#
#     parser = Lark(
#         r"""
#         identifier : (CNAME ".")* CNAME
#
#         type_list : type ("," type)*
#
#         generic_type : identifier "[" type_list "]"
#
#         ?base_type : ["unsigned" " "+] identifier | pointer_type | reference_type | const_type
#
#         ?type : base_type | generic_type
#
#         signature : identifier "(" [type_list] ")" ["const"]
#
#         %import common.CNAME
#         %import common.WS
#         %ignore WS
#         """,
#         start='signature',
#     )
#
#     text = "Mari::ExportItem::setUvIndexList(QList<int> const&, int, char const*)"
#     print(parser.parse(text).pretty())
