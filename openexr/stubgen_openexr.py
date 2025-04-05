from __future__ import absolute_import, annotations, division, print_function

import mypy.stubgen
import mypy.stubgenc
from mypy.stubgenc import DocstringSignatureGenerator, SignatureGenerator

from stubgenlib.siggen import (
    AdvancedSigMatcher,
    AdvancedSignatureGenerator,
)

# HEADER_TYPE = "Mapping[str, float | str | Iterable[str], Iterable[int] | Iterable[float] | Iterable[tuple] | Compression | KeyCode | LineOrder | TimeCode | numbers.Rational | np.ndarray]"
HEADER_TYPE = "dict[str, Any]"


class OpenEXRSignatureGenerator(AdvancedSignatureGenerator):
    sig_matcher = AdvancedSigMatcher(
        signature_overrides={
            # signatures for these special methods include many inaccurate overloads
            "*.__ne__": "(self, other: object) -> bool",
            "*.__eq__": "(self, other: object) -> bool",
            "*.File.header": f"(self, part_index: int = ...) -> {HEADER_TYPE}",
        },
        arg_type_overrides={
            ("*", "parts", "list"): "Iterable[Part]",
            ("*", "channels", "dict"): "Mapping[str, Channel | numpy.ndarray]",
            ("*", "header", "dict"): HEADER_TYPE,
        },
        result_type_overrides={
            ("*.isOpenExrFile", "*"): "bool",
            ("*.isComplete", "*"): "bool",
            ("*.File.__enter__", "object"): "Self",
        },
        property_type_overrides={
            ("*.File.parts", "*"): "list[Part]",
            ("*.File.header", "*"): HEADER_TYPE,
        },
    )


class InspectionStubGenerator(mypy.stubgenc.InspectionStubGenerator):
    def get_sig_generators(self) -> list[SignatureGenerator]:
        return [
            OpenEXRSignatureGenerator(
                fallback_sig_gen=DocstringSignatureGenerator(),
            )
        ]

    def set_defined_names(self, defined_names: set[str]) -> None:
        super().set_defined_names(defined_names)
        for typ in ["Any", "Self", "Iterable", "Mapping"]:
            self.add_name(f"typing.{typ}", require=False)


mypy.stubgen.InspectionStubGenerator = InspectionStubGenerator  # type: ignore[attr-defined,misc]
mypy.stubgenc.InspectionStubGenerator = InspectionStubGenerator  # type: ignore[misc]

if __name__ == "__main__":
    mypy.stubgen.main()
