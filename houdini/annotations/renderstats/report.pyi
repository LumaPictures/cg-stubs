import argparse
import pathlib
from collections.abc import Collection, Iterator, Sequence
from typing import Never, NoReturn

import jinja2
import jsonpathfx
from houtypes import JSONLike
from markupsafe import Markup

from hutil.qt.data import models

from . import images
from .images import _RenderStats

DEFAULT_TEMPLATE_NAME: str
DEFAULT_THUMBNAIL_DIR_NAME: str

def chip(i: int) -> Markup: ...

class Slice:
    @property
    def degrees(self) -> float: ...
    @staticmethod
    def coordString(degrees: float, ctr: float, dist: float) -> str: ...
    def pathString(self, radius: float, ring_width: float, size: int) -> str: ...
    def chip(self) -> Markup: ...

class ChartData:
    slices: Sequence[Slice]
    total: float
    def __init__(self, slices: Sequence[Slice], total: float = ...) -> None: ...
    def __iter__(self) -> Iterator[Slice]: ...
    def nonzero(self) -> list[Slice]: ...
    def sorted(self, field: str = ..., include_zero: bool = ..., reverse: bool = ...) -> list[Slice]: ...
    def donut_svg(self, size: int = ..., radius: float = ..., ring_width: float = ...) -> Markup: ...

def chart_data(
    data: models.DataSource,
    total: float = ...,
    name_key: str | None = ...,
    value_key: str | None = ...,
    hide: Collection[str] = ...,
    key_order: dict[str, str] | list[str] | tuple[()] = ...,
    renames: dict[str, str] | None = ...,
) -> ChartData: ...

class PathCache:
    def __init__(self, data: JSONLike) -> None: ...
    def find_all(self, pathstr: str) -> list[jsonpathfx.JsonValue]: ...
    def find(self, pathstr: str) -> jsonpathfx.JsonValue: ...

class Thumbnails:
    inline: bool
    level: images.Level
    size: int
    include_aovs: Collection[str]
    exclude_aovs: Collection[str]
    heatmap_aovs: list[str | int]
    colormap: str
    format: str
    thumbnail_dir: str
    color_space: str
    heatmap_scale: str | float
    verbosity: Verbosity
    def __init__(
        self,
        level: images.Level,
        image_path: pathlib.Path,
        output_dir: pathlib.Path,
        data: _RenderStats,
        inlining: bool = ...,
        size: int = ...,
        include_aovs: Collection[str] = ...,
        exclude_aovs: Collection[str] = ...,
        heatmap_aovs: Collection[str | int] = ...,
        colormap: str = ...,
        heatmap_scale: str | float = ...,
        thumbnail_format: str = ...,
        thumbnail_dir: str = ...,
        color_space: str = ...,
        temp_dir: pathlib.Path | None = ...,
        verbosity: Verbosity = ...,
    ) -> None: ...
    def has(self, name: str) -> bool: ...
    def used(self, name: str) -> bool: ...
    def ref(self, aov_spec: int | str) -> str: ...
    def cleanup(self) -> None: ...

class Resources:
    def __init__(
        self, resource_dir: pathlib.Path, output_dir: pathlib.Path, inlining: bool = ..., prefix: str = ...
    ) -> None: ...
    def script(self, name: str) -> str: ...
    def css(self, name: str) -> str: ...

def sorted_dict(d: dict[str, float], by: str, reverse: bool = ...) -> list[tuple[str, float]]: ...
def shorten_channel(aov_name: str, ch_name: str) -> Markup: ...

MISSING_VALUE: Markup

class ReportUndefined(jinja2.ChainableUndefined):
    def __iter__(self) -> Iterator[Never]: ...

def generate(
    image_path: pathlib.Path,
    output_path: pathlib.Path | None = ...,
    resource_dir: pathlib.Path | None = ...,
    template_name: str = ...,
    template_path: pathlib.Path | None = ...,
    colormap: str = ...,
    mode: Mode = ...,
    resource_prefix: str = ...,
    thumbnail_level: images.Level = ...,
    include_aovs: Collection[str] = ...,
    exclude_aovs: Collection[str] = ...,
    heatmap_aovs: Collection[str | int] = ...,
    heatmap_scale: str | float = ...,
    data: _RenderStats | None = ...,
    thumbnail_size: int = ...,
    thumbnail_format: str = ...,
    color_space: str = ...,
    create_dirs: bool = ...,
    thumbnail_dir: str = ...,
    title: str | None = ...,
    subtitle: str | None = ...,
    verbosity: Verbosity = ...,
) -> None: ...

value_to_level: dict[str, images.Level]

def commaSplit(names: str | list[str] | tuple[str, ...]) -> list[str] | tuple[str, ...]: ...
def makeArgParser() -> argparse.ArgumentParser: ...
def run() -> NoReturn: ...
