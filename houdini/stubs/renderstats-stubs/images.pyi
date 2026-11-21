# Houdini stubs generated from Houdini 22.0.466

import dataclasses
import enum
import pathlib
from collections.abc import Iterator
from houtypes import JSONValue
from typing import Collection, Sequence
from typing_extensions import Required, TypedDict

class _AovBuffer(TypedDict, total=False, extra_items=JSONValue):  # type: ignore[call-arg]
    name: Required[str]
    cryptomatte: bool

_AovMetadata = TypedDict('_AovMetadata', {'husk:render_stats': '_RenderStats'}, total=False, extra_items=JSONValue)  # type: ignore[misc]

class _ImageAov(TypedDict, total=False, extra_items=JSONValue):  # type: ignore[call-arg]
    name: str
    channels: list[str]
    resolution: list[int]
    color_space: str
    metadata: _AovMetadata

class _RenderStats(TypedDict, total=False, extra_items=JSONValue):  # type: ignore[call-arg]
    filename: str
    aovs: list[_ImageAov]
    resolution: list[int]
    aov_buffers: list[_AovBuffer] | dict[str, _AovBuffer]
    md: _AovMetadata
    husk: _RenderStats | None

DEFAULT_FORMAT: str
DEFAULT_COLOR_MAP: str
DEFAULT_THUMBNAIL_SIZE: int
DEFAULT_COLOR_SPACE: str
DEFAULT_HEAT_SCALE: str
DEFAULT_HEATMAPS: tuple[str, str, str]
DEFAULT_C1: str
DEFAULT_C2: str

class UnknownAov(Exception): ...

class Level(enum.Enum):
    none = enum.auto()
    diagnostic = enum.auto()
    default = enum.auto()
    all = enum.auto()

class Kind(enum.Enum):
    normal = enum.auto()
    heatmap = enum.auto()
    scale = enum.auto()

class Verbosity(enum.IntEnum):
    quiet = 0
    normal = 1
    verbose = 2

@dataclasses.dataclass
class Thumbnail:
    path: pathlib.Path
    aov_index: int
    aov_name: str
    format: str = ...
    kind: Kind = ...
    def dataUrl(self) -> str: ...

def image_metadata(image_path: pathlib.Path) -> _RenderStats: ...
def normalize_stats(data: _RenderStats) -> _RenderStats: ...
def find_aov(data: _RenderStats, aov: int | str) -> _ImageAov: ...
def resolution_from_metadata(data: _RenderStats, aov: int | str = 0) -> Sequence[int]: ...
def aov_datas(data: _RenderStats) -> Iterator[_ImageAov]: ...
def crypto_data_names(data: _RenderStats) -> set[str] | tuple[()]: ...
def filtered_aov_names(data: _RenderStats, level: Level, include_aovs: Collection[str], exclude_aovs: Collection[str]) -> list[str]: ...
def oiiotool_checks(size: int, c1: str = ..., c2: str = ...) -> str: ...
def generate_preview_image(input_file: pathlib.Path, output_file: pathlib.Path, resize: str | None, aov: int | str = 0, color_space: str = ..., over_checkerboard: bool = False, check_size: int = 8, c1: str = ..., c2: str = ...) -> None: ...
def generate_aov_thumbnails(image_path: pathlib.Path, dir_path: pathlib.Path, data: _RenderStats | None = None, size: int = ..., level: Level = ..., include_aovs: Collection[str] = ..., exclude_aovs: Collection[str] = ..., heatmap_aovs: Collection[str | int] = ..., colormap: str = 'magma', format: str = ..., heatmap_scale: str | float = ..., create_color_scale: bool = True, color_space: str = ..., check_size: int = 8, c1: str = ..., c2: str = ..., ignore_errors: bool = True, verbosity: int = ...) -> list[Thumbnail]: ...
