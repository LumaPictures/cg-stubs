from collections.abc import Collection, Mapping, MutableSequence, Sequence
from typing import Any, TypeAlias, TypeVar

from _typeshed import SupportsWrite
from houtypes import JSONValue
from typing_extensions import Required, TypedDict

TIMESTAMP_FORMAT: str
MEMORY_TIERS: tuple[tuple[int, str], tuple[int, str], tuple[int, str], tuple[int, str]]
OIIO_CONFIG_KEYS: tuple[str, str, str, str, str, str, str, str, str, str, str, str, str, str, str]
OIIO_STAT_KEYS: tuple[str, str, str, str, str, str, str, str, str, str, str, str, str]
LIGHT_TYPE_ALIASES: dict[str, str]
OBJECT_ALIASES: dict[str, str]
GEOMETRY_ALIASES: dict[str, str]
SHADER_NODE_ALIASES: dict[str, str]
RAY_ALIASES: dict[str, str]
SHADER_CALL_ALIASES: dict[str, str]
CACHE_HEADINGS: tuple[str, str, str, str, str]
CACHE_FORMAT: str
PRIMVAR_HEADINGS: tuple[str, str, str]
PRIMVAR_FORMAT: str
BUCKET_HEADINGS: tuple[str, str, str]
BUCKET_FORMAT: str
XPU_TIMINGS_HEADINGS: tuple[str, str]
XPU_TIMINGS_FORMAT: str
XPU_COMPILES_HEADINGS: tuple[str, str]
XPU_COMPILES_FORMAT: str
MAX_HISTORY_SIZE: int

_T = TypeVar("_T")

# A count of each kind of thing: a number, or [unique, total], or {"unique": ..., "total": ...}.
_Counts: TypeAlias = dict[str, int | list[int] | dict[str, int]]

class _SystemTime(TypedDict, extra_items=JSONValue):  # type: ignore[call-arg]
    totaltime: float
    wallclock: float
    cpu: float
    sys: float

class _SystemMemory(TypedDict, extra_items=JSONValue):  # type: ignore[call-arg]
    current: int
    peak: int

class _RenderStats(TypedDict, total=False, extra_items=JSONValue):  # type: ignore[call-arg]
    """The `render_stats` of Karma's stats JSON. Some keys depend on the stats mode."""

    percent_complete: Required[float]
    resolution: Required[list[int]]
    hostname: Required[str]
    cpu_brand: Required[str]
    cpu_architecture: Required[str]
    threads: Required[int]
    engine: Required[str]
    system_time: Required[_SystemTime]
    system_memory: Required[_SystemMemory]
    render_settings: Required[dict[str, JSONValue]]
    username: str
    time_to_first_pixel: float
    render_camera: str
    renderStatsAnnotation: str
    object_counts: _Counts
    geometry_counts: _Counts
    light_types: _Counts
    shader_nodes: _Counts
    ray_counts: _Counts
    shader_calls: _Counts
    timings: dict[str, float]
    xpu_timings: dict[str, float]
    xpu_compiles: dict[str, float]
    unified_cache: CacheDict
    oiio_stats: dict[str, int | float | str]
    oiio_stats_string: str
    rat_stats: dict[str, int]
    rat_disk_cache: dict[str, int]
    texture_error_files: list[str]
    texture_conversions: dict[str, int]
    primvar_cache: dict[str, JSONValue]

class _Stats(TypedDict, total=False, extra_items=JSONValue):  # type: ignore[call-arg]
    """The stats JSON husk passes to its verbose callback."""

    render_stats: Required[_RenderStats]
    frame: Required[float]
    product: Required[str]
    frame_count: int
    frame_index: int
    usdfile: str

def compact(ls: MutableSequence[_T]) -> None: ...

class State:
    is_printing: bool
    image_basename: str | None
    generating_images: bool
    stream: SupportsWrite[str] | None
    frame_count: int
    current_frame: int
    global_start_time: float
    frame_start_time: float
    current_time: float
    last_time: float
    frame_percent_complete: float
    frame_time_remaining: float
    total_time_remaining: float
    memory_history: list[Any]
    product_name: str
    image_width: int
    image_height: int
    usd_file: str
    ttfp: float
    frame_number: float
    host_name: str
    cpu_brand: str
    cpu_arch: str
    current_mem_bytes: int
    peak_mem_bytes: int
    light_types: _Counts
    object_counts: _Counts
    geometry_counts: _Counts
    shader_node_counts: _Counts
    ray_counts: _Counts
    shader_call_counts: _Counts
    render_stats: _RenderStats
    thread_count: int
    user_name: str
    render_camera: str
    karma_engine: str
    frame_wall_time: float
    total_wall_time: float
    total_cpu_time: float
    system_cpu_time: float
    pathtrace_samples: int
    pixel_samples: int
    render_stats_annotations: str
    verbosity: int
    say_timestamps: bool
    elapsed_time_in_timestamps: bool
    verbose_color: bool
    def __init__(self, stream: SupportsWrite[str] | None = ..., printing: bool = ...) -> None: ...
    def setVerbosityFromCode(self, code: str) -> None: ...
    def say(self, *objs: object) -> None: ...
    def startFrame(self, frame_index: int) -> None: ...
    def totalTimeRemaining(self) -> float: ...
    def sayAovInfo(self, names: Sequence[str], bytecounts: Sequence[int], sources: Sequence[str]) -> None: ...
    def sayUnifiedCache(self) -> None: ...
    def sayOiioConfig(self) -> None: ...
    def sayOiioStats(self) -> None: ...
    def sayRatStats(self) -> None: ...
    def sayRatCacheStats(self) -> None: ...
    def sayTextureErrors(self) -> None: ...
    def sayCounts(
        self,
        label: str,
        counts: Mapping[str, int | Sequence[int] | Mapping[str, int]],
        aliases: Mapping[str, str] | None = ...,
        show_single: Collection[str] | None = ...,
    ) -> None: ...
    def sayPrimvarCacheStats(self) -> None: ...
    def sayTimings(self) -> None: ...
    def sayCompileStats(self) -> None: ...
    def populateStats(self, stats: _Stats) -> None: ...
    def sayFrameHeading(self) -> None: ...
    def sayProgress(self) -> None: ...
    def dumpRenderStats(self) -> None: ...
    def sayRenderStatsAnnotation(self) -> None: ...
    def sayObjectCounts(self) -> None: ...
    def sayGeometryCounts(self) -> None: ...
    def sayLightTypes(self) -> None: ...
    def sayShaderCounts(self) -> None: ...
    def sayRayCounts(self) -> None: ...
    def sayShaderCallCounts(self) -> None: ...
    def sayVerboseInfo(self) -> None: ...
    def sayResourceInfo(self) -> None: ...
    def printUpdate(self, frame_heading: bool, should_update: bool) -> None: ...
    def generateImage(self, start_of_frame: bool) -> None: ...
    def update(self, start_of_frame: bool, should_update: bool) -> None: ...
    def run(self, verbosity: str, mode: str, stats: _Stats) -> None: ...
    def parseArguments(self, argv: Sequence[str]) -> tuple[str, str, _Stats]: ...
    def main(self, argv: Sequence[str]) -> None: ...

global_state: State
