import pathlib

from PySide6 import QtCore, QtGui, QtWidgets

from .syntaxcoloring import BaseColorSchemeEditor, Preset, PresetModel

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
    def __init__(self, parent: QtWidgets.QWidget | None = ...) -> None: ...
    def reloadPresets(self, current: Preset | None = ...) -> None: ...
    def setSelectedRow(self, row: int) -> None: ...
    def setColor(self, hcs_name: str, color: QtGui.QColor) -> None: ...
    def refreshPreview(self) -> None: ...
    def saveChanges(self) -> None: ...

def showChannelColorEditor() -> None: ...

class ChannelColorPreview(QtWidgets.QWidget):
    def __init__(self, parent: QtWidgets.QWidget | None = ...) -> None: ...
    def setPreset(self, preset: Preset | None) -> None: ...
    def paintEvent(self, event: QtGui.QPaintEvent) -> None: ...
