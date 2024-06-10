# mypy: disable-error-code="misc, override, no-redef"

from _typeshed import Incomplete
from pxr.Ts.TsTest_Grapher import TsTest_Grapher as TsTest_Grapher

class TsTest_Comparator:
    def __init__(self, title, widthPx: int = ..., heightPx: int = ...) -> None: ...
    def AddSpline(self, name, splineData, samples, baked: Incomplete | None = ...): ...
    def Display(self): ...
    def GetMaxDiff(self): ...
    @classmethod
    def Init(cls): ...
    def Write(self, filePath): ...
    def _Compare(self): ...
    def _FindDiffs(self): ...