from typing import ClassVar, TypedDict, Unpack

import apex
import hou
from apex.control_2 import ControlTransformData
from apex.xformgadget import ApexXformHandle, _HandleStartUpdateKwargs

HK_CTXT: str
HK_HANDLE_MODE: str

class _HomUIEventKwargs(TypedDict, total=False):
    start_drag_pos: hou.Vector3

# The xform handle's start callback kwargs (Animate state), with what the caller adds.
class _XformGadgetParmsKwargs(_HandleStartUpdateKwargs, total=False):
    force_world: bool
    key_pressed: str | None
    ui_event: hou.ViewerEvent

class ApexUIEventParms:
    defaults: ClassVar[apex.Dict]
    @staticmethod
    def uiEventKeys() -> list[str]: ...
    @staticmethod
    def cloneDefaultDict() -> apex.Dict: ...
    @staticmethod
    def initValueIfMissing(apexdict: apex.Dict, key: str) -> None: ...
    @staticmethod
    def setNDCMousePos(apexdict: apex.Dict, ui_event: hou.ViewerEvent, is_dragging: bool) -> None: ...
    @staticmethod
    def setViewerScale(apexdict: apex.Dict, scene_viewer: hou.SceneViewer) -> None: ...
    @staticmethod
    def updateFromHomUIEvent(apexdict: apex.Dict, ui_event: hou.ViewerEvent, is_dragging: bool = ..., **kwargs: Unpack[_HomUIEventKwargs]) -> None: ...
    @staticmethod
    def updateReferenceTransformData(apexdict: apex.Dict, xform: hou.Matrix4, is_dragging: bool = ..., modifier_status: int = ...) -> None: ...

class ApexHandleUIParms:
    defaults: ClassVar[apex.Dict]
    @staticmethod
    def updateXformGadgetParms(apexdict: apex.Dict, xform_gadget: ApexXformHandle, gadget_kwargs: _XformGadgetParmsKwargs) -> None: ...
    # xform is unused.
    @staticmethod
    def updateUITransformData(apexdict: apex.Dict, xform: hou.Matrix4, control_data: ControlTransformData, is_dragging: bool = ...) -> None: ...
