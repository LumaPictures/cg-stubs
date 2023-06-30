from __future__ import absolute_import, annotations, division, print_function

import re

import mypy.stubgen
import mypy.stubgenc
from mypy.fastparse import parse_type_comment
from mypy.stubgen import main
from mypy.stubgenc import ArgSig
from mypy.stubgenc import DocstringSignatureGenerator as CDocstringSignatureGenerator
from mypy.stubgenc import FunctionContext, FunctionSig, SignatureGenerator

import mari

from stubgenlib import DocstringSignatureGenerator, DocstringTypeFixer

# the mari.so mdule patches in the Mari pure python package using __path__. Undo that
# so that mypy will just process mari.so as a single c extension.
mari.__path__ = []


class MariDocstringSignatureGenerator(DocstringSignatureGenerator, DocstringTypeFixer):
    pass


class CStubGenerator(mypy.stubgenc.CStubGenerator):
    def is_defined_in_module(self, obj: object) -> bool:
        if self.module_name == 'mari' and getattr(obj, '__module__', '').startswith(
            'mari.Mari'
        ):
            return True
        return super().is_defined_in_module(obj)

    def get_sig_generators(self) -> list[SignatureGenerator]:
        return [MariDocstringSignatureGenerator()]


mypy.stubgen.CStubGenerator = CStubGenerator
mypy.stubgenc.CStubGenerator = CStubGenerator
