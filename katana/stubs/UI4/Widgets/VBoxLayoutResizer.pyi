# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyQt5.QtGui
import PyQt5.QtWidgets
import PyQt5.QtCore as QtCore
from UI4.Widgets.BaseLayoutResizer import BaseLayoutResizer as BaseLayoutResizer
from typing import Set, Tuple

class VBoxLayoutResizer(BaseLayoutResizer):
    def __init__(self, targetWidget: PyQt5.QtWidgets.QWidget, initialTargetWidgetHeight: int = ..., minimumTargetWidgetHeight: int = ..., beforeTargetWidget: bool = ...) -> None: ...
    def mouseMoveEvent(self, event: PyQt5.QtGui.QMouseEvent): ...
