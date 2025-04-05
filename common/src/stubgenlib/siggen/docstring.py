from __future__ import absolute_import, annotations, division, print_function

from mypy.stubgenc import (
    ArgSig,
    FunctionContext,
    FunctionSig,
    SignatureGenerator,
)


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

        if ctx.docstring:
            parsed = docstring_parser.parse(self.prepare_docstring(ctx.docstring))
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
                            default=bool(param.is_optional),
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
