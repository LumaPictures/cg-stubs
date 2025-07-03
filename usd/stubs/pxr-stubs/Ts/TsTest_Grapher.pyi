from _typeshed import Incomplete

class TsTest_Grapher:
    class Spline:
        data: Incomplete
        name: Incomplete
        baked: Incomplete
        samples: Incomplete
        def __init__(self, name, data, samples, baked) -> None: ...
    class Diff:
        time: Incomplete
        value: Incomplete
        def __init__(self, time, value) -> None: ...
    class _StyleTable:
        class _Region:
            start: Incomplete
            openStart: Incomplete
            isDim: Incomplete
            def __init__(self, start, openStart, isDim) -> None: ...
        _regions: Incomplete
        def __init__(self, data, forKnots) -> None: ...
        def IsDim(self, time): ...
    class _KeyframeData:
        splineData: Incomplete
        def __init__(self, splineData) -> None: ...
        def Draw(self, ax, color) -> None: ...
    @classmethod
    def Init(cls): ...
    _title: Incomplete
    _widthPx: Incomplete
    _heightPx: Incomplete
    _includeScales: Incomplete
    _splines: Incomplete
    _diffs: Incomplete
    _figure: Incomplete
    def __init__(self, title, widthPx: int = 1000, heightPx: int = 750, includeScales: bool = True) -> None: ...
    def AddSpline(self, name, splineData, samples, baked: Incomplete | None = None) -> None: ...
    def AddDiffData(self, diffs) -> None: ...
    def Display(self) -> None: ...
    def Write(self, filePath) -> None: ...
    @staticmethod
    def _DimColor(colorStr):
        """Transform a matplotlib color string to reduced opacity."""
    def _ConfigureAxes(self, axes) -> None:
        """
        Set whole-axes properties.
        """
    def _MakeGraph(self) -> None:
        """
        Set up self._figure, a matplotlib Figure.
        """
    def _ClearGraph(self) -> None: ...
