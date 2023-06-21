from __future__ import absolute_import, annotations, division, print_function

import re
from typing import Any

from mypy.stubdoc import infer_sig_from_docstring
from mypy.stubgenc import (
    ArgSig, FunctionContext, FunctionSig, SignatureGenerator
)
from mypy.fastparse import parse_type_comment


class BaseSigFixer:

    @staticmethod
    def is_valid(type_name: str) -> bool:
        try:
            parse_type_comment(type_name, 0, 0, None)
        except Exception:
            return False
        else:
            return True
    
    def cleanup_type(self, type_name: str, ctx: FunctionContext, is_result: bool) -> str:
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
                    invalid.append("  Invalid arg {}: {} {}".format(
                        arg.name, repr(arg.type), repr(type_name)))
                    type_name = None
            args.append(ArgSig(arg.name, type_name, arg.default))
        if sig.ret_type:
            return_type = self.cleanup_type(sig.ret_type, ctx, is_result=True)
            if not self.is_valid(return_type):
                invalid.append("  Invalid ret: {} {}".format(
                    repr(sig.ret_type), repr(return_type)))
                return_type = None

        if invalid:
            print(f"Invalid type after cleanup: {ctx.fullname}")
            print(sig.format_sig())

        # FIXME: only copy if something has changed?
        return FunctionSig(sig.name, args, return_type)


class DocstringSignatureGenerator(SignatureGenerator, BaseSigFixer):
    """
    Generate signatures from docstrings.

    Unlike the built-in parser which targets signatures created by C++ binding
    generators, this works with standard docstring formats such as numpy,
    google, and epydoc (which Katana uses).
    """

    def get_function_sig(
        self, default_sig: FunctionSig, ctx: FunctionContext
    ) -> list[FunctionSig] | None:
        import docstring_parser
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
            sig = self.cleanup_sig_types(sig, ctx)

            # if len(default_sig.args) != len(args):
            #     print("  Lengths are not the same")

            merged_sig = default_sig.merge(sig)
            # print(merged_sig.format_sig())
            return [merged_sig]
        return None


class BoostDocstringSignatureGenerator(SignatureGenerator):
    def get_function_sig(
        self, default_sig: FunctionSig, ctx: FunctionContext
    ) -> list[FunctionSig] | None:
        
        if ctx.docstr:
            # convert the boost-provided signature into a proper python signature
            docstr = ctx.docstr.replace('[', '')
            docstr = docstr.replace(']', '')
            docstr = re.sub(r"\(([^(]+)\)([a-zA-Z_][a-zA-Z0-9_]*)", lambda m: '{}: {}'.format(m.group(2), m.group(1)), docstr)
            return infer_sig_from_docstring(docstr, ctx.name)
        