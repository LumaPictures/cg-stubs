from __future__ import absolute_import, annotations, division, print_function

import mypy.stubgen
import mypy.stubgenc
from mypy.stubgenc import DocstringSignatureGenerator, SignatureGenerator

from stubgenlib.siggen import (
    AdvancedSigMatcher,
    AdvancedSignatureGenerator,
)
from stubgenlib.utils import add_positional_only_args


class OIIOSignatureGenerator(AdvancedSignatureGenerator):
    sig_matcher = AdvancedSigMatcher(
        signature_overrides={
            # signatures for these special methods include many inaccurate overloads
            "*.__ne__": "(self, other: object) -> bool",
            "*.__eq__": "(self, other: object) -> bool",
        },
        arg_type_overrides={
            ("*", "*", "Buffer"): "numpy.ndarray",
            ("*", "*", "*.TypeDesc"): "Union[TypeDesc, BASETYPE, str]",
            ("*.ImageOutput.open", "specs", "list[ImageSpec]"): "Iterable[ImageSpec]",
        },
        result_type_overrides={
            ("*.ImageOutput.create", "object"): "ImageOutput | None",
            ("*.ImageOutput.open", "object"): "ImageOutput | None",
            ("*.ImageInput.create", "object"): "ImageInput | None",
            ("*.ImageInput.open", "object"): "ImageInput | None",
            ("*.ImageInput.read_native_deep_*", "object"): "DeepData | None",
            # this must come after the prev rule because it overlaps
            ("*.ImageInput.read_*", "object"): "numpy.ndarray | None",
            ("*", "Buffer"): "numpy.ndarray",
            ("*.get_pixels", "object"): "numpy.ndarray | None",
            ("*.TextureSystem.imagespec", "object"): "ImageSpec | None",
            ("*.getattribute", "object"): "Any",
            ("*.ImageSpec.get", "object"): "Any",
            ("*.ImageBufAlgo.histogram", "object"): "tuple[int, ...]",
            ("*.ImageBufAlgo.isConstantColor", "object"): "tuple[float, ...] | None",
        },
        property_type_overrides={
            # FIXME: this isn't working
            ("*.ParamValue.value", "object"): "Any",
        },
    )

    def process_sig(
        self, ctx: mypy.stubgen.FunctionContext, sig: mypy.stubgen.FunctionSig
    ) -> mypy.stubgen.FunctionSig:
        return add_positional_only_args(ctx, super().process_sig(ctx, sig))


class InspectionStubGenerator(mypy.stubgenc.InspectionStubGenerator):
    def get_sig_generators(self) -> list[SignatureGenerator]:
        return [
            OIIOSignatureGenerator(
                fallback_sig_gen=DocstringSignatureGenerator(),
            )
        ]

    def set_defined_names(self, defined_names: set[str]) -> None:
        super().set_defined_names(defined_names)
        for typ in ["Any", "Iterable"]:
            self.add_name(f"typing.{typ}", require=False)


mypy.stubgen.InspectionStubGenerator = InspectionStubGenerator  # type: ignore[attr-defined,misc]
mypy.stubgenc.InspectionStubGenerator = InspectionStubGenerator  # type: ignore[misc]

if __name__ == "__main__":
    mypy.stubgen.main()
