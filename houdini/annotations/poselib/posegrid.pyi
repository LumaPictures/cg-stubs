from PySide6 import QtCore, QtGui, QtWidgets

from poselib import itemgrid, posemodel

class PoseGrid(itemgrid.GridView):
    nodeSelectRequested: QtCore.Signal
    blendStarted: QtCore.Signal
    blendEnded: QtCore.Signal
    blendChanged: QtCore.Signal
    blendMoved: QtCore.Signal
    def __init__(self, parent: QtWidgets.QWidget, model: posemodel.PoseGridModel) -> None: ...
    def mousePressEvent(self, event: QtGui.QMouseEvent) -> bool | None: ...
    def mouseMoveEvent(self, event: QtGui.QMouseEvent) -> bool | None: ...
    def mouseReleaseEvent(self, event: QtGui.QMouseEvent) -> bool | None: ...
    def setHasNode(self, has_node: bool) -> None: ...

class PoseGridDelegate(itemgrid.GridDelegate):
    indexRemoved: QtCore.Signal
    def paintLabel(
        self,
        painter: QtGui.QPainter,
        option: QtWidgets.QStyleOptionViewItem,
        index: QtCore.QModelIndex | QtCore.QPersistentModelIndex,
        pose_rect: QtCore.QRect,
        parm_rect: QtCore.QRect,
        frame_rect: QtCore.QRect,
    ) -> None: ...
    def paintOverlayIcons(
        self,
        painter: QtGui.QPainter,
        option: QtWidgets.QStyleOptionViewItem,
        index: QtCore.QModelIndex | QtCore.QPersistentModelIndex,
        rect: QtCore.QRect,
    ) -> None: ...

class BlendOverlay(QtWidgets.QWidget):
    blendChanged: QtCore.Signal
    def __init__(self, parent: PoseGrid) -> None: ...
    def __del__(self) -> None: ...
