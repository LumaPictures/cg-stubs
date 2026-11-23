from _csv import Writer
from collections.abc import Mapping, Sequence
from io import TextIOWrapper

class PlotType:
    @classmethod
    def menu(cls) -> list[str]: ...

class BufferedPlotter:
    axes: Mapping[str, str]
    data: dict[str, list[float]]
    buffer: int
    file_format: str
    ext: str
    def __init__(self, axes: Mapping[str, str] = ..., file_format: str = ..., ext: str = ...) -> None: ...
    def appendRow(self, **kwargs: float) -> None: ...
    def updateRow(self, **kwargs: float) -> None: ...
    def flush(self, **kwargs: object) -> None: ...

class MatPlotLibPlotter(BufferedPlotter):
    title: str
    x_label: str
    x_range: Sequence[float] | None
    y_label: str
    y_range: Sequence[float] | None
    def __init__(
        self,
        axes: Mapping[str, str] = ...,
        file_format: str = ...,
        title: str = ...,
        x_label: str = ...,
        x_range: Sequence[float] | None = ...,
        y_label: str = ...,
        y_range: Sequence[float] | None = ...,
    ) -> None: ...

class CSVPlotter(BufferedPlotter):
    csv_file: TextIOWrapper | None
    csv_writer: Writer | None
    write_header: bool
    def __init__(self, axes: Mapping[str, str] = ..., file_format: str = ..., write_header: bool = ...) -> None: ...
    def __del__(self) -> None: ...
