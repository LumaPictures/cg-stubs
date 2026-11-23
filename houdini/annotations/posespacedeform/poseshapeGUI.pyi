from collections.abc import Callable, Sequence
from types import TracebackType
from typing import ClassVar, TypeAlias, Unpack

import hou
from houtypes import NodeEventKwargs
from PySide6 import QtCore, QtGui, QtWidgets

from posespacedeform.buildGUI import BuildGUI
from posespacedeform.editGUI import (
    ActiveEdit,
    BypassToggleButton,
    EditPoseButton,
    EditPoseShapeButton,
    FreezeToggleButton,
    ViewPoseShapeButton,
)
from posespacedeform.openGUI import OpenGUI
from posespacedeform.qtExtendedClasses import InLineEdit
from posespacedeform.ui.uiLineEditList import UiTable

_NetworkLayoutCallback: TypeAlias = Callable[[Sequence[hou.OpNode | None]], object]

RECORDING_BLINK_TIMEOUT: int
SHOW_EDIT_BUTTONS_TIMEOUT: int
DRIVER_VALUE_DIFFERENCE_THRESHOLD: float
REFRESH_POSESHAPE_LIST_TIMEOUT: int

class PoseShapeItem(QtWidgets.QWidget):
    childGUI: None
    psd_node: hou.SopNode | None
    poseshape: hou.SopNode | None
    posestash: hou.ChopNode | None
    activeEdit: ActiveEdit | None
    item: QtWidgets.QTableWidgetItem
    poseshape_list: "PoseShapeListGUI"
    name: InLineEdit
    info: QtWidgets.QLabel
    view: ViewPoseShapeButton
    bypass: BypassToggleButton
    freeze: FreezeToggleButton
    edit_poseshape: EditPoseShapeButton
    edit_pose: EditPoseButton
    deletebutton: QtWidgets.QToolButton
    stopbutton: QtWidgets.QPushButton
    stop_record_state: int
    use_live_driver_value: bool
    timer: QtCore.QTimer
    contextmenu: QtWidgets.QMenu
    setup_type: int
    disabled: bool
    posestash_drivers: hou.ChopNode | None
    def __init__(
        self, poseshape_list: "PoseShapeListGUI", parent: QtWidgets.QWidget | None, item: QtWidgets.QTableWidgetItem
    ) -> None: ...
    def __exit__(
        self, exc_type: type[BaseException] | None, exc_value: BaseException | None, traceback: TracebackType | None
    ) -> None: ...
    def buildContextMenu(self) -> None: ...
    def startStopButtonRefresh(self, editbutton: EditPoseShapeButton | EditPoseButton) -> None: ...
    def stopStopButtonRefresh(self) -> None: ...
    def initializePoseShapeItem(
        self,
        setup_type: int,
        psd_node: hou.SopNode,
        poseshape: hou.SopNode,
        posestash: hou.ChopNode,
        skelroot_node: hou.ObjNode,
        activeEdit: ActiveEdit,
        disabled: bool,
    ) -> None: ...
    def onPoseshapeNameChanged(self, **kwargs: Unpack[NodeEventKwargs]) -> None: ...

class PoseShapeListGUI(UiTable):
    start_drag_and_drop: ClassVar[QtCore.Signal]
    stop_drag_and_drop: ClassVar[QtCore.Signal]
    rebuild_poseshape_list: bool
    psd_node: hou.SopNode | None
    setup_type: int
    drivers_node: hou.ChopNode | None
    transforms_node: hou.ChopNode | None
    poseshapessubnet: hou.OpNode | None
    childGUI: OpenGUI | BuildGUI | None
    editPSDCallback: _NetworkLayoutCallback | None
    onSelectedCallback: Callable[[PoseShapeItem, int], object] | None
    activeEdit: ActiveEdit
    disable_first_pose: bool
    skelroot_node: hou.ObjNode | None
    label: str
    def __init__(self, activeEdit: ActiveEdit) -> None: ...
    def dragEnterEvent(self, event: QtGui.QDragEnterEvent) -> None: ...
    def dragMoveEvent(self, event: QtGui.QDragMoveEvent) -> None: ...
    def dragLeaveEvent(self, event: QtGui.QDragLeaveEvent) -> None: ...
    def initPoseShapesGUI(
        self,
        psd_node: hou.SopNode,
        setup_type: int,
        drivers_node: hou.ChopNode | None,
        transforms_node: hou.ChopNode | None,
        skelroot_node: hou.ObjNode | None,
        poseshapessubnet: hou.OpNode | None,
    ) -> None: ...
    def rebuildPoseShapeList(self) -> None: ...
    def setOnPoseShapeSelected(self, fcn: Callable[[PoseShapeItem, int], object] | None) -> None: ...
    def setEditPSDCallback(self, fcn: _NetworkLayoutCallback | None) -> None: ...
    def toggleEditFirstPoseshape(self) -> None: ...
    def refreshPoseShapes(self) -> None: ...
    def validPoseShapeDriverValues(self) -> bool: ...
    def validCurrentDriverValue(self) -> bool: ...
    def onAddNewPoseShapeAtCurrentPose(self) -> None: ...
    def onExportImportGeoNewPoseShapeAtCurrentPose(self) -> None: ...
    def onImportGeoNewPoseShapeAtCurrentPose(self) -> None: ...
    def getSelectedPoseShapes(self) -> list[hou.SopNode]: ...
    def copySelectedTo(self) -> None: ...
    def copySelectedToNewSiblingPSD(self) -> None: ...
    def moveSelectedTo(self) -> None: ...
    def moveSelectedToNewSiblingPSD(self) -> None: ...
    def deleteSelected(self, warn_user: bool = ...) -> None: ...
    def deletePoseShapes(self, selected_poseshape_nodes: Sequence[hou.SopNode], warn_user: bool = ...) -> bool | None: ...
    def renameSelected(self) -> None: ...
    def jumpToSkelRoot(self) -> None: ...
    def diveIntoSkelRoot(self) -> None: ...
    def diveIntoPoseShapeSubnet(self) -> None: ...
    def diveIntoPoseSubnet(self) -> None: ...
    def jumpToPoseSpaceDeformOutput(self) -> None: ...
    def clearSelection(self) -> None: ...
