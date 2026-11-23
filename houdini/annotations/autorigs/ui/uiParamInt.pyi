from collections.abc import Sequence

from autorigs.ui.uiParamNum import UiParamNum

class UiParamInt(UiParamNum):
    SLIDER_RANGE_DEFAULT_MIN: int
    SLIDER_RANGE_DEFAULT_MAX: int

    slidermin: float
    slidermax: float
    defaults: Sequence[float]
    min: float
    max: float

    def __init__(
        self,
        label: str | None,
        num_components: int,
        defaults: Sequence[float] = ...,
        soft_range: tuple[float, float] = ...,
        parmnames: Sequence[str] | None = ...,
    ) -> None: ...
    def setRange(self, min: float, max: float, bypass_strict: bool = ...) -> None: ...
    def getRange(self) -> tuple[float, float]: ...
    def eval(self) -> list[int]: ...
    def setValues(self, values: Sequence[float]) -> None: ...
