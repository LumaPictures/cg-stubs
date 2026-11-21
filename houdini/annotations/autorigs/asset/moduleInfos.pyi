from collections.abc import Callable

from PySide6 import QtGui

from autorigs.asset.autoRigsAsset import AutoRigsAsset
from autorigs.modules.base.rootModule import Module

ICON_SIZE: int
ARM_ICON: QtGui.QIcon
LEG_ICON: QtGui.QIcon
HAND_ICON: QtGui.QIcon
HEAD_ICON: QtGui.QIcon
QUADRUPED_HEAD_ICON: QtGui.QIcon
FOOT_ICON: QtGui.QIcon
SPINE_ICON: QtGui.QIcon
BLANK_RIG_ICON: QtGui.QIcon
QUADRUPED_ICON: QtGui.QIcon
NULL_ICON: QtGui.QIcon
ADD_ICON: QtGui.QIcon
FILE_ICON: QtGui.QIcon
BIPED_ICON: QtGui.QIcon
QUADRUPED_LEG_ICON: QtGui.QIcon
QUADRUPED_ARM_ICON: QtGui.QIcon
TAIL_ICON: QtGui.QIcon
QUADRUPED_FOOT_ICON: QtGui.QIcon
HIDDEN_DEFAULT_MODULES: list[tuple[QtGui.QIcon, str]]
BIPED_MODULES_DATA: list[tuple[str, str, QtGui.QIcon]]
QUAD_MODULES_DATA: list[tuple[str, str, QtGui.QIcon]]
FACE_MODULES_DATA: list[tuple[str, str, QtGui.QIcon]]
CREATE_MODULE_CLASS: dict[str, Callable[[AutoRigsAsset], Module]]
BUILD_MODULE_ORDER: list[str]
DEFAULT_ADD_PRESETS: tuple[str, str, QtGui.QIcon]
DEFAULT_IMPORT_PRESETS: tuple[str, str, QtGui.QIcon]
DEFAULT_PRESET_BIPED: str
DEFAULT_PRESET_QUADRUPED: str
DEFAULT_PRESETS: list[tuple[str, str, QtGui.QIcon]]
