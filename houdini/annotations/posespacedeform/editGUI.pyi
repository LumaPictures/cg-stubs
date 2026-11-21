from collections.abc import Callable

import hou
from PySide6 import QtWidgets

ACTIVE_EDIT_NONE: int
ACTIVE_EDIT_POSE: int
ACTIVE_EDIT_POSE_SHAPE: int

class ActiveEdit:
    def __init__(self) -> None: ...
    def start(
        self,
        name: str,
        mode: int,
        node: hou.ChopNode | hou.SopNode,
        edit: "EditPoseShapeButton | EditPoseButton",
        save_current_edit: bool = ...,
        export_on_edit: bool = ...,
    ) -> bool: ...
    def allow_refresh_drivers(self) -> bool: ...
    def finish_allowed(self, mode: int, node: hou.ChopNode | hou.SopNode | None) -> bool: ...
    def test_finish(
        self,
        mode: int = ...,
        node: hou.ChopNode | hou.SopNode | None = ...,
        save_edit: bool = ...,
        do_not_reset_view: bool = ...,
    ) -> bool: ...
    def test_allowed(
        self,
        mode: int = ...,
        node: hou.ChopNode | hou.SopNode | None = ...,
        save_edit: bool = ...,
        do_not_reset_view: bool = ...,
    ) -> bool: ...
    def finish(self, save_edit: bool = ..., do_not_reset_view: bool = ...) -> None: ...

class BypassToggleButton(QtWidgets.QToolButton):
    node: hou.SopNode
    activeEdit: ActiveEdit
    def __init__(self, parent: QtWidgets.QWidget | None) -> None: ...
    def initButton(self, node: hou.SopNode, activeEdit: ActiveEdit) -> None: ...
    def refreshButton(self) -> None: ...

class FreezeToggleButton(QtWidgets.QToolButton):
    node: hou.SopNode
    activeEdit: ActiveEdit
    def __init__(self, parent: QtWidgets.QWidget | None) -> None: ...
    def initButton(self, node: hou.SopNode, activeEdit: ActiveEdit) -> None: ...
    def refreshButton(self) -> None: ...

class ViewPoseShapeButton(QtWidgets.QWidget):
    button: QtWidgets.QToolButton
    posestash: hou.ChopNode
    activeEdit: ActiveEdit
    channel_node: hou.ChopNode | None
    def __init__(self, parent: QtWidgets.QWidget | None) -> None: ...
    def initButton(self, posestash: hou.ChopNode, activeEdit: ActiveEdit) -> None: ...

class EditPoseShapeButton(QtWidgets.QWidget):
    button: QtWidgets.QToolButton
    isEditing: bool
    startfnc: Callable[["EditPoseShapeButton"], object]
    stopfnc: Callable[["EditPoseShapeButton"], object]
    name: str
    poseshape_node: hou.SopNode
    activeEdit: ActiveEdit
    skelroot_node: hou.ObjNode
    def __init__(
        self,
        parent: QtWidgets.QWidget | None,
        startfnc: Callable[["EditPoseShapeButton"], object],
        stopfnc: Callable[["EditPoseShapeButton"], object],
    ) -> None: ...
    def initButton(
        self, name: str, poseshape_node: hou.SopNode, skelroot_node: hou.ObjNode, activeEdit: ActiveEdit
    ) -> None: ...
    def stopEdit(self, do_not_reset_view: bool = ...) -> None: ...

class EditPoseButton(QtWidgets.QWidget):
    button: QtWidgets.QToolButton
    isEditing: bool
    startfnc: Callable[["EditPoseButton"], object]
    stopfnc: Callable[["EditPoseButton"], object]
    name: str
    activeEdit: ActiveEdit
    pose_node: hou.ChopNode
    skelroot_node: hou.ObjNode
    setup_type: int
    export_on_edit: bool
    def __init__(
        self,
        parent: QtWidgets.QWidget | None,
        startfnc: Callable[["EditPoseButton"], object],
        stopfnc: Callable[["EditPoseButton"], object],
    ) -> None: ...
    def initButton(
        self, name: str, setup_type: int, pose_node: hou.ChopNode, skelroot_node: hou.ObjNode, activeEdit: ActiveEdit
    ) -> None: ...
    def stopEdit(self, do_not_reset_view: bool = ...) -> None: ...
