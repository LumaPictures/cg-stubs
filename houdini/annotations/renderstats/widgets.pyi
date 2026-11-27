from collections.abc import Mapping
from typing import Protocol, Unpack

import hou
from PySide6 import QtCore, QtGui, QtQml, QtWidgets

from hutil.formatting import NumberFormatter
from hutil.qt.pluto import colors
from houtypes import JSONLike, JSONValue
from jsonpathfx import JsonPath, JsonValue
from typing_extensions import Required, TypedDict

from .images import _RenderStats

# One XPU device's entry in karma's render stats.
class _XpuDeviceStats(TypedDict, total=False, extra_items=JSONValue):  # type: ignore[call-arg]
    xpu_device_contrib: Required[float]
    xpu_device_label: Required[str]
    xpu_device_type: Required[str]
    xpu_device_status: Required[str]
    xpu_device_error: str
    xpu_device_samples: Required[int]
    xpu_device_memory: dict[str, int]

# BaseInfoState's keyword arguments; the rest go on to QObject.
class _StatsStateKwargs(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    editor: hou.NetworkEditor | None

class _BriefFormatter(Protocol):
    def __call__(self, value: str | float, markup: bool = ...) -> str: ...

default_content: str
brief_fmtr: NumberFormatter
format_brief: _BriefFormatter
timings_order: tuple[str, str, str, str, str, str, str, str]
shader_order: tuple[str, str, str, str, str, str]
husk_stats_path: JsonPath
jsonpath_cache: dict[str, JsonPath]

def toURL(string: str) -> QtCore.QUrl: ...
def findStats(data_paths: Mapping[str, str], stats: JSONLike) -> dict[str, JsonValue]: ...

class ReportJob:
    key: str
    exr: str
    html_path: str
    process: QtCore.QProcess
    is_temp: bool
    handled: bool
    def __init__(self, key: str, exr: str, html_path: str, process: QtCore.QProcess, is_temp: bool) -> None: ...

class XpuDeviceInfo:
    @classmethod
    def forDeviceStats(cls, data: _XpuDeviceStats, color: QtGui.QColor) -> XpuDeviceInfo: ...

class StatsState:
    reloadable: bool
    reportFile: str
    reportState: str
    def __init__(self, **kwargs: Unpack[_StatsStateKwargs]) -> None: ...
    def setupEngine(self, engine: QtQml.QQmlEngine, **kwargs: object) -> None: ...
    def setReportSource(self, report_key: str, from_buffer: bool = ..., viewer_name: str = ...) -> None: ...
    def generateReport(self) -> None: ...

class StatsWidget:
    SOURCE_URL: str
    def __init__(self, parent: QtWidgets.QWidget | None = ...) -> None: ...
    def setContentURL(self, url: QtCore.QUrl) -> None: ...

class StatsPanel:
    def __init__(self, parent: QtWidgets.QWidget | None = ...) -> None: ...
    def theme(self) -> colors.Theme: ...
    def panelActivated(self) -> None: ...
    def panelDeactivated(self) -> None: ...
    def saveReport(self) -> None: ...
    def info(self) -> StatsInfo: ...
    def setGlobalScale(self, scale: float) -> None: ...
    def setStats(
        self, data: _RenderStats, report_file: str | None = ..., report_from_buffer: bool = ..., viewer_name: str = ...
    ) -> None: ...

def renderStatsWidget(parent: QtWidgets.QWidget | None = ..., ui_scale: float = ...) -> StatsPanel: ...
