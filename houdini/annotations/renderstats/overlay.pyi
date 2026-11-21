import argparse
import pathlib
from collections.abc import Mapping
from typing import NoReturn, TypeVar

from houtypes import JSONValue
from PySide6 import QtCore, QtGui

from .images import _RenderStats

_D = TypeVar("_D", bound=Mapping[str, object])

DEFAULT_MARGIN: int
DEFAULT_ALIGNMENT: str
DEFAULT_EDGE: str
DEFAULT_BG_COLOR: str
DEFAULT_PREVIEW_MODE: PreviewMode
DEFAULT_PREVIEW_RESIZE: None
DEFAULT_SIDEBAR_WIDTH: int
DEFAULT_TEMPLATE: str

def defaultTemplateFile() -> pathlib.Path: ...
def findTemplateFile(rel_path: str) -> pathlib.Path: ...

preview_mode_names: dict[str, PreviewMode]

def oiiotoolColor(c: QtGui.QColor) -> str: ...
def makeOverlay(
    template_data: pathlib.Path | dict[str, JSONValue],
    data: pathlib.Path | _RenderStats,
    width: int,
    scale: float = ...,
    rotation: float = ...,
) -> QtGui.QPixmap: ...
def writePreview(
    input_file: pathlib.Path,
    output_file: pathlib.Path,
    overlay: QtGui.QPixmap,
    resize: str | None,
    preview_mode: PreviewMode,
    alignment: QtCore.Qt.AlignmentFlag,
    margin: int,
    edge: QtCore.Qt.Edge | None,
    bg_color: QtGui.QColor,
    aov: int | str = ...,
    color_space: str = ...,
    preserve_transparency: bool = ...,
    verbosity: Verbosity = ...,
) -> None: ...
# A template or the stats, or the JSON file to load it from.
def _maybeLoadFile(source: pathlib.Path | _D) -> _D: ...
def getResize(data: _RenderStats, resize: int | str | None, force_resize: bool) -> tuple[int, str | None]: ...
def generate(
    image_path: pathlib.Path,
    preview_mode: str | PreviewMode,
    output_path: str | pathlib.Path | None = ...,
    *,
    overlay_file: str | pathlib.Path | None = ...,
    resize: int | str | None = ...,
    force_resize: bool = ...,
    stats_width: int | str = ...,
    template_file: str | pathlib.Path | None = ...,
    alignment: str | QtCore.Qt.AlignmentFlag = ...,
    edge: str | QtCore.Qt.Edge | None = ...,
    bg_color: str | QtGui.QColor = ...,
    margin: int = ...,
    aov: int | str = ...,
    preview_format: str = ...,
    color_space: str = ...,
    preserve_transparency: bool = ...,
    scale: float = ...,
    rotation: float = ...,
    verbosity: Verbosity = ...,
) -> None: ...
def makeArgParser() -> argparse.ArgumentParser: ...
def run() -> None: ...
def runMain() -> NoReturn: ...
