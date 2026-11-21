from .images import _RenderStats
from collections.abc import Mapping
from houtypes import JSONLike, JSONValue
from hutil.PySide import QtCore, QtGui as QtGui, QtQml as QtQml, QtWidgets
from hutil.PySide.QtCore import Qt as Qt
from hutil.formatting import NumberFormatter, format_bytes as format_bytes, format_duration as format_duration
from hutil.qt.common import core, qmlviews as qmlviews
from hutil.qt.info import window
from hutil.qt.pluto import colors as colors
from jsonpathfx import JsonPath, JsonValue as JsonValue
from typing import Any, Protocol
from typing_extensions import Required, TypedDict

class _XpuDeviceStats(TypedDict, total=False, extra_items=JSONValue):  # type: ignore[call-arg]
    xpu_device_contrib: Required[float]
    xpu_device_label: Required[str]
    xpu_device_type: Required[str]
    xpu_device_status: Required[str]
    xpu_device_error: str
    xpu_device_samples: Required[int]
    xpu_device_memory: dict[str, int]

class _BriefFormatter(Protocol):
    def __call__(self, value: str | float, markup: bool = ...) -> str: ...

default_content: str
brief_fmtr: NumberFormatter
format_brief: _BriefFormatter
timings_order: tuple[str, ...]
shader_order: tuple[str, ...]
husk_stats_path: JsonPath
jsonpath_cache: dict[str, JsonPath]

def toURL(string: str) -> QtCore.QUrl: ...

class XpuDeviceInfo(core.Info):
    label: str
    color: QtGui.QColor
    contribPercent: float
    fraction: float
    error: str
    samples: int
    status: str
    typeName: str
    geometryMemory: int
    hostMemory: int
    otherMemory: int
    textureMemory: int
    usedMemory: int
    volumeMemory: int
    geometryPeak: int
    hostPeak: int
    otherPeak: int
    texturePeak: int
    usedPeak: int
    volumePeak: int
    @classmethod
    def forDeviceStats(cls, data: _XpuDeviceStats, color: QtGui.QColor) -> XpuDeviceInfo: ...

class StatsInfo(core.Info):
    contentURL: QtCore.QUrl

def findStats(data_paths: Mapping[str, str], stats: JSONLike) -> dict[str, JsonValue]: ...

class ReportJob:
    """Tracks an in-flight `renderstatsreport` process for one image."""
    key: str
    exr: str
    html_path: str
    process: QtCore.QProcess
    is_temp: bool
    handled: bool
    def __init__(self, key: str, exr: str, html_path: str, process: QtCore.QProcess, is_temp: bool) -> None: ...

class StatsState(window.BaseInfoState[window.NodeInfoConfig, StatsInfo]):
    reloadable: bool
    reportFile: str
    reportState: str
    def __init__(self, **kwargs: Any) -> None: ...
    def setupEngine(self, engine: QtQml.QQmlEngine, **kwargs: object) -> None: ...
    def setReportSource(self, report_key: str, from_buffer: bool = False, viewer_name: str = '') -> None:
        """Point the report UI at the current image.

        `report_key` identifies the image's report: an EXR path for a file
        source, or a stable per-source token for a buffer source (from_buffer).
        `viewer_name` is the owning image viewer's name, used as the `imgsave`
        target when the report is produced from a buffer source.
        Reflects whether a report is currently being generated for it.
        """
    def generateReport(self) -> None: ...

class StatsWidget(window.InfoWidget[StatsState, StatsInfo]):
    SOURCE_URL: str
    def __init__(self, parent: QtWidgets.QWidget | None = None) -> None: ...
    def setContentURL(self, url: QtCore.QUrl) -> None: ...

class StatsPanel(QtWidgets.QFrame):
    def __init__(self, parent: QtWidgets.QWidget | None = None) -> None: ...
    def theme(self) -> colors.Theme: ...
    def setSource(self, source: QtCore.QUrl) -> None: ...
    def resizeEvent(self, event: QtGui.QResizeEvent) -> None: ...
    def panelActivated(self) -> None: ...
    def panelDeactivated(self) -> None: ...
    def saveReport(self) -> None: ...
    def info(self) -> StatsInfo: ...
    def setGlobalScale(self, scale: float) -> None: ...
    def setStats(self, data: _RenderStats, report_file: str | None = None, report_from_buffer: bool = False, viewer_name: str = '') -> None: ...

def renderStatsWidget(parent: QtWidgets.QWidget | None = None, ui_scale: float = 1.0) -> StatsPanel: ...
