from __future__ import absolute_import, annotations, division, print_function

from typing import Any

import docstring_parser
from mypy.stubgenc import (
    ArgSig, FunctionContext, FunctionSig, SignatureGenerator
)


class DocstringSignatureGenerator(SignatureGenerator):
    """
    Generate signatures from docstrings.

    Unlike the built-in parser which targets signatures created by C++ binding
    generators, this works with standard docstring formats such as numpy,
    google, and epydoc (which Katana uses).
    """

    def cleanup_sig(self, sig):
        return sig, []

    def get_function_sig(
        self, default_sig: FunctionSig, ctx: FunctionContext
    ) -> list[FunctionSig] | None:
        if ctx.docstr:
            parsed = docstring_parser.parse(ctx.docstr)
            args = []
            return_type = None
            if parsed.params:
                for param in parsed.params:
                    # FIXME: handle optional
                    args.append(
                        ArgSig(param.arg_name,
                               param.type_name,
                               default=param.default is not None))
            if parsed.returns and parsed.returns.type_name:
                return_type = parsed.returns.type_name
            sig = FunctionSig(ctx.name, args, return_type)
            sig, invalid = self.cleanup_sig(sig)
            if invalid:
                print(ctx.fullname)
                print(sig.format_sig())
            # if len(default_sig.args) != len(args):
            #     print("  Lengths are not the same")

            merged_sig = default_sig.merge(sig)
            # print(merged_sig.format_sig())
            return [merged_sig]
        return None
