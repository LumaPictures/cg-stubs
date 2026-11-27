import apex
import hou
from apex.control_2 import ControlTransformData as ControlTransformData
from apex.xformgadget import ApexXformHandle as ApexXformHandle, _HandleStartUpdateKwargs
from typing import ClassVar, TypedDict, Unpack

class _HomUIEventKwargs(TypedDict, total=False):
    start_drag_pos: hou.Vector3

class _XformGadgetParmsKwargs(_HandleStartUpdateKwargs, total=False):
    force_world: bool
    key_pressed: str | None
    ui_event: hou.ViewerEvent

MOUSE_LEFT_BUTTON: int
MOUSE_RIGHT_BUTTON: int
MOUSE_MIDDLE_BUTTON: int
NO_MODIFIER: int
SHIFT_MODIFIER: int
CTRL_MODIFIER: int
SHIFT_CTRL_MODIFIER: int
HK_CTXT: str
HK_HANDLE_MODE: str

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
    def updateFromHomUIEvent(apexdict: apex.Dict, ui_event: hou.ViewerEvent, is_dragging: bool = False, **kwargs: Unpack[_HomUIEventKwargs]) -> None: ...
    @staticmethod
    def updateReferenceTransformData(apexdict: apex.Dict, xform: hou.Matrix4, is_dragging: bool = False, modifier_status: int = 0) -> None:
        """updates the xform of the primary control of the current selection for the ui event. We usually update
        that reference xform only on drag start but we also can query the position of the xform 
        if a modifier key got pressed during drag. 

        :param apexdict: ui parms of for the drag interaction
        :param xform: the xform of the primary control
        :param is_dragging: defines if the we currently are dragging or not, defaults to False
        :param modifier_status: _description_, defaults to 0
        """

class ApexHandleUIParms:
    defaults: ClassVar[apex.Dict]
    @staticmethod
    def updateXformGadgetParms(apexdict: apex.Dict, xform_gadget: ApexXformHandle, gadget_kwargs: _XformGadgetParmsKwargs) -> None: ...
    @staticmethod
    def updateUITransformData(apexdict: apex.Dict, xform: hou.Matrix4, control_data: ControlTransformData, is_dragging: bool = False) -> None: ...
