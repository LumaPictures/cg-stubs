from __future__ import absolute_import, annotations, division, print_function

import re
from typing import Any

import mypy.stubgen
import mypy.stubgenc
from mypy.stubgenc import SignatureGenerator

from stubgenlib import (
    DocstringTypeFixer,
    FixableCDocstringSigGen,
)


class OcioDocstringSignatureGenerator(DocstringTypeFixer, FixableCDocstringSigGen):
    pass


class InspectionStubGenerator(mypy.stubgenc.InspectionStubGenerator):
    def get_sig_generators(self) -> list[SignatureGenerator]:
        return [OcioDocstringSignatureGenerator(default_sig_handling="merge")]

    def set_defined_names(self, defined_names: set[str]) -> None:
        super().set_defined_names(defined_names)
        for typ in ["Iterable", "Iterator", "Callable"]:
            self.add_name(f"typing.{typ}", require=False)

    def get_members(self, obj: object) -> list[tuple[str, Any]]:
        return [
            (name, obj)
            for name, obj in super().get_members(obj)
            if not (name == "__hash__" and obj is None)
        ]

    def get_base_types(self, obj: type) -> list[str]:
        bases = super().get_base_types(obj)
        if obj.__name__ == "Exception":
            return ["__builtins__.Exception"]
        else:
            return bases


mypy.stubgen.InspectionStubGenerator = InspectionStubGenerator  # type: ignore[attr-defined,misc]
mypy.stubgenc.InspectionStubGenerator = InspectionStubGenerator  # type: ignore[misc]

if __name__ == "__main__":
    mypy.stubgen.main()
