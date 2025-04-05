from __future__ import absolute_import, annotations, division, print_function

from mypy.stubgenc import (
    FunctionContext,
    FunctionSig,
    SignatureGenerator,
)


class DefaultSigGenerator(SignatureGenerator):
    """Sig Gen that uses the signature extracted from the source code"""

    def get_function_sig(
        self, default_sig: FunctionSig, ctx: FunctionContext
    ) -> list[FunctionSig] | None:
        return [default_sig]
