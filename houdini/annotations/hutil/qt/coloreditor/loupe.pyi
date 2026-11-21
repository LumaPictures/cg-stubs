from collections.abc import Callable
from typing import ClassVar

from PySide6 import QtCore, QtGui, QtQuick

from hutil.qt.common import core

class LoupeWindow(QtQuick.QQuickView):
    accepted: ClassVar[QtCore.Signal]
    rejected: ClassVar[QtCore.Signal]
    changed: ClassVar[QtCore.Signal]
    started: ClassVar[QtCore.Signal]

    class LoupeState(core.Info):
        moved: ClassVar[QtCore.Signal]

    class Grabber(QtQuick.QQuickImageProvider):
        def __init__(self, zoom_size: int) -> None: ...

    def __init__(self, old_color: QtGui.QColor, parent_window: QtGui.QWindow | None = ..., color_transform: Callable[[QtGui.QColor], QtGui.QColor] | None = ...) -> None: ...
