from collections.abc import Sequence

from autorigs.ui.uiParamNum import UiParamNum

class UiParamFloat(UiParamNum):
    defaults: Sequence[float]

    def __init__(
        self,
        label: str | None,
        num_components: int,
        defaults: Sequence[float] = ...,
        soft_range: tuple[float, float] = ...,
        parmnames: Sequence[str] | None = ...,
    ) -> None: ...
    def setToDefaults(self) -> None: ...
    def getRange(self) -> tuple[float, float]: ...
    def eval(self) -> list[float]: ...
    def isAlmostEqual(self, nodevalue: float, slidervalue: float) -> bool: ...
