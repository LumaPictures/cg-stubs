from collections.abc import Callable

from PySide6 import QtGui, QtWidgets

PARAMETER_DELIM: str
TRACK_DELIM: str
CHANNEL_DELIM: str
PATH_DELIM: str
ICON_SIZE: int
EDIT_ICON_SIZE: int
SWITCH_ICON_HEIGHT: int
SWITCH_ICON_WIDTH: int
SWITCH_ICON_SIZE: int
HELP_ICON: QtGui.QIcon
JUMP_ICON: QtGui.QIcon
FREEZE_ICON: QtGui.QIcon
BYPASS_ICON: QtGui.QIcon
DELETE_ICON: QtGui.QIcon
EDIT_POSE_ICON: QtGui.QIcon
VIEW_POSESHAPE_ICON: QtGui.QIcon
EDIT_POSESHAPE_ICON: QtGui.QIcon
EDIT_FRAME_ICON: QtGui.QIcon
STOP_RECORD_ICON: QtGui.QIcon
STOP_RECORD_DARK_ICON: QtGui.QIcon
STOP_RECORD_LIGHT_ICON: QtGui.QIcon
SETTINGS_ICON: QtGui.QIcon
SWITCH_THUMB_ICON: QtGui.QIcon
SWITCH_OFF_GROOVE_ICON: QtGui.QIcon
SWITCH_ON_GROOVE_ICON: QtGui.QIcon

def showHelp() -> None: ...
def createHelpButton() -> QtWidgets.QToolButton: ...
def createJumpButton(callback_function: Callable[[], object]) -> QtWidgets.QToolButton: ...
def createFreezeButton(callback_function: Callable[[], object]) -> QtWidgets.QToolButton: ...
def createBypassButton(callback_function: Callable[[], object]) -> QtWidgets.QToolButton: ...
