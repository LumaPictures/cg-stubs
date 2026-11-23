import argparse
import enum
import pathlib
from . import images as images, known_dirs as known_dirs
from .images import _RenderStats
from houtypes import JSONValue
from hutil.PySide import QtCore, QtGui
from typing import NoReturn

from typing import TypeVar
from collections.abc import Mapping
from typing import TypeVar
_D = TypeVar('_D', bound=Mapping[str, object])
class PreviewMode(enum.Enum):
    overlay = enum.auto()
    sidebar = enum.auto()

class Verbosity(enum.IntEnum):
    quiet = 0
    normal = 1
    verbose = 2

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
def _maybeLoadFile(source: pathlib.Path | _D) -> _D: ...
def makeOverlay(template_data: pathlib.Path | dict[str, JSONValue], data: pathlib.Path | _RenderStats, width: int, scale: float = 1.0, rotation: float = 0.0) -> QtGui.QPixmap: ...
def writePreview(input_file: pathlib.Path, output_file: pathlib.Path, overlay: QtGui.QPixmap, resize: str | None, preview_mode: PreviewMode, alignment: QtCore.Qt.AlignmentFlag, margin: int, edge: QtCore.Qt.Edge | None, bg_color: QtGui.QColor, aov: int | str = 0, color_space: str = ..., preserve_transparency: bool = False, verbosity: Verbosity = ...) -> None: ...
def getResize(data: _RenderStats, resize: int | str | None, force_resize: bool) -> tuple[int, str | None]: ...
def generate(image_path: pathlib.Path, preview_mode: str | PreviewMode, output_path: str | pathlib.Path | None = None, *, overlay_file: str | pathlib.Path | None = None, resize: int | str | None = ..., force_resize: bool = False, stats_width: int | str = ..., template_file: str | pathlib.Path | None = None, alignment: str | QtCore.Qt.AlignmentFlag = ..., edge: str | QtCore.Qt.Edge | None = None, bg_color: str | QtGui.QColor = ..., margin: int = ..., aov: int | str = 0, preview_format: str = ..., color_space: str = ..., preserve_transparency: bool = False, scale: float = 1.0, rotation: float = 0.0, verbosity: Verbosity = ...) -> None: ...
def makeArgParser() -> argparse.ArgumentParser: ...
def run() -> None: ...
def runMain() -> NoReturn: ...
