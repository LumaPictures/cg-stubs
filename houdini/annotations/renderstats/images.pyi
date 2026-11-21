import pathlib
from collections.abc import Collection, Iterator, Sequence


from houtypes import JSONValue
from typing_extensions import Required, TypedDict

# Render stats: the JSON `iinfo -J` prints for an image (its AOVs, with their metadata), or
# husk's render stats from an interactive render, both as normalize_stats() leaves them.
class _AovBuffer(TypedDict, total=False, extra_items=JSONValue):  # type: ignore[call-arg]
    name: Required[str]
    cryptomatte: bool

_AovMetadata = TypedDict(  # type: ignore[call-arg]
    "_AovMetadata", {"husk:render_stats": "_RenderStats"}, total=False, extra_items=JSONValue
)

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
    # A list in husk's stats, which normalize_stats() also gives by name.
    aov_buffers: list[_AovBuffer] | dict[str, _AovBuffer]
    # Added by normalize_stats(): the first AOV's metadata, and husk's stats in it.
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

class Thumbnail:
    def __str__(self) -> str: ...
    def dataUrl(self) -> str: ...

def image_metadata(image_path: pathlib.Path) -> _RenderStats: ...
def normalize_stats(data: _RenderStats) -> _RenderStats: ...
def find_aov(data: _RenderStats, aov: int | str) -> _ImageAov: ...
def resolution_from_metadata(data: _RenderStats, aov: int | str = ...) -> Sequence[int]: ...
def aov_datas(data: _RenderStats) -> Iterator[_ImageAov]: ...
def crypto_data_names(data: _RenderStats) -> set[str] | tuple[()]: ...
def filtered_aov_names(
    data: _RenderStats, level: Level, include_aovs: Collection[str], exclude_aovs: Collection[str]
) -> list[str]: ...
def oiiotool_checks(size: int, c1: str = ..., c2: str = ...) -> str: ...
def generate_preview_image(
    input_file: pathlib.Path,
    output_file: pathlib.Path,
    resize: str | None,
    aov: int | str = ...,
    color_space: str = ...,
    over_checkerboard: bool = ...,
    check_size: int = ...,
    c1: str = ...,
    c2: str = ...,
) -> None: ...
def generate_aov_thumbnails(
    image_path: pathlib.Path,
    dir_path: pathlib.Path,
    data: _RenderStats | None = ...,
    size: int = ...,
    level: Level = ...,
    include_aovs: Collection[str] = ...,
    exclude_aovs: Collection[str] = ...,
    heatmap_aovs: Collection[str | int] = ...,
    colormap: str = ...,
    format: str = ...,
    heatmap_scale: str | float = ...,
    create_color_scale: bool = ...,
    color_space: str = ...,
    check_size: int = ...,
    c1: str = ...,
    c2: str = ...,
    ignore_errors: bool = ...,
    verbosity: int = ...,
) -> list[Thumbnail]: ...
