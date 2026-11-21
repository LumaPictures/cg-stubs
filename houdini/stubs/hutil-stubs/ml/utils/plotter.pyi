# Houdini stubs generated from Houdini 22.0.466

import enum
from _csv import Writer
from collections.abc import Mapping, Sequence
from hutil.ml.utils.menu import indexed_menu as indexed_menu
from io import TextIOWrapper

class PlotType(enum.Enum):
    """
    Enumeration of supported activation types.
    """
    Disabled = 0
    CSV = 1
    Image = 2
    @classmethod
    def menu(cls) -> list[str]:
        """
        Returns a parm menu entry list that matches the values
        specified in this enum
        """

class BufferedPlotter:
    """
    Base class for plotters that buffer their data and be flushed at a
    fixed rate. Axes can be configured by passing an `axes` dictionary
    that contains a mapping from the axis name to a human-readable axis
    label
    """
    axes: Mapping[str, str]
    data: dict[str, list[float]]
    buffer: int
    file_format: str
    ext: str
    def __init__(self, axes: Mapping[str, str] = ..., file_format: str = '', ext: str = 'txt') -> None:
        """
        Constructs a new plotter with the specified axes layout and file
        format string
        """
    def appendRow(self, **kwargs: float) -> None:
        """
        Appends a row to the plot. Values for specifc axes can be specified
        using keyword arguments that map the axis name to its value in the
        row
        """
    def updateRow(self, **kwargs: float) -> None:
        """
        Updates value(s) in the current row. Valus are specified using
        keyword arguments that map the axis name to the value in the row.

        appendRow must be called before updateRow to insert rows for each
        data axis.
        """
    def flush(self, **kwargs: object) -> None:
        """
        Flushes the current buffer contents to the output file
        """

class MatPlotLibPlotter(BufferedPlotter):
    """
    Plots data to an image file using matplotlib
    """
    title: str
    x_label: str
    x_range: Sequence[float] | None
    y_label: str
    y_range: Sequence[float] | None
    def __init__(self, axes: Mapping[str, str] = ..., file_format: str = '', title: str = '', x_label: str = '', x_range: Sequence[float] | None = None, y_label: str = '', y_range: Sequence[float] | None = None) -> None: ...

class CSVPlotter(BufferedPlotter):
    """
    Plots data to a text file with comma-separate rows and one row
    per data point
    """
    csv_file: TextIOWrapper | None
    csv_writer: Writer | None
    write_header: bool
    def __init__(self, axes: Mapping[str, str] = ..., file_format: str = '', write_header: bool = False) -> None: ...
    def __del__(self) -> None: ...
