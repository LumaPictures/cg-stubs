# Houdini stubs generated from Houdini 22.0.466

import pathlib
from .syntaxcoloring import BaseColorSchemeEditor as BaseColorSchemeEditor, ColorSetModel as ColorSetModel, NameDelegate as NameDelegate, Preset as Preset, PresetModel as PresetModel, activeColors as activeColors, hfs_dir as hfs_dir, saveJson as saveJson
from hutil.PySide import QtCore as QtCore, QtGui as QtGui, QtWidgets as QtWidgets
from hutil.PySide.QtCore import Qt as Qt

TINY_MARGIN: int
SMALL_MARGIN: int
BIG_MARGIN: int
WINDOW_WIDTH: int
WINDOW_HEIGHT: int
THUMB_SIZE: QtCore.QSize
CONFIG_FILE_NAME: str
ACTIVE_SCHEME_LABEL: str
prefs_dir: pathlib.Path
user_presets_path: pathlib.Path
active_colors_path: pathlib.Path
fallback_colors: dict[str, QtGui.QColor]
curve_labels: dict[str, str]

class ChannelPreset(Preset):
    def icon(self) -> QtGui.QPixmap: ...
    def toData(self) -> dict[str, str | dict[str, str]]: ...

class ChannelPresetModel(PresetModel):
    def indexOf(self, preset: Preset) -> int: ...

class ChannelColorEditor(BaseColorSchemeEditor):
    START_COMMENT: str
    END_COMMENT: str
    hcs_name_to_label: dict[str, str]
    def __init__(self, parent: QtWidgets.QWidget | None = None) -> None: ...
    def reloadPresets(self, current: Preset | None = None) -> None: ...
    def setSelectedRow(self, row: int) -> None: ...
    def setColor(self, hcs_name: str, color: QtGui.QColor) -> None: ...
    def refreshPreview(self) -> None: ...
    def saveChanges(self) -> None: ...

def showChannelColorEditor() -> None: ...

class ChannelColorPreview(QtWidgets.QWidget):
    def __init__(self, parent: QtWidgets.QWidget | None = None) -> None: ...
    def setPreset(self, preset: Preset | None) -> None: ...
    def paintEvent(self, event: QtGui.QPaintEvent) -> None: ...
