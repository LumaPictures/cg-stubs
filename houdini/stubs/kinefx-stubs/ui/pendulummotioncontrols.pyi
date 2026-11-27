import hou
from collections.abc import Iterable, Sequence
from houtypes import ViewerStateDrawKwargs, ViewerStateEnterKwargs, ViewerStateEventKwargs, ViewerStateHandleToStateKwargs, ViewerStateKwargs, ViewerStateMenuActionKwargs, ViewerStateMenuPreOpenKwargs, ViewerStateParmChangeKwargs, ViewerStateSelectionKwargs, ViewerStateStateToHandleKwargs
from kinefx.ui.selectabledrawable import KinefxSelectableDrawable as KinefxSelectableDrawable, KinefxSelectableDrawableCollection as KinefxSelectableDrawableCollection
from typing import Never, Protocol

from typing import TypeAlias
from collections.abc import Mapping
from houtypes import ViewerParmProperties
from typing import TypeAlias
_VerbParms: TypeAlias = Mapping[str, hou.OptionMultiArgType | hou.Ramp | Sequence[Mapping[str, hou.OptionMultiArgType | hou.Ramp]]]
_StateParms: TypeAlias = Mapping[str, ViewerParmProperties]
class _Handle(Protocol):
    def show(self, value: bool, /) -> object: ...
    def update(self) -> object: ...

XFORM_SRT: int
XFORM_STR: int
XFORM_RST: int
XFORM_RTS: int
XFORM_TSR: int
XFORM_TRS: int
XFORM_XYZ: int
XFORM_XZY: int
XFORM_YXZ: int
XFORM_YZX: int
XFORM_ZXY: int
XFORM_ZYX: int
HANDLE_NONE: int
HANDLE_INITIAL_POS: int
HANDLE_TARGET_POS: int
HANDLE_PIVOT: int
PEND_TYPE_SIMPLE: int
PEND_TYPE_CONICAL: int
pend_type_menu_items: list[tuple[str, str]]
pend_type_enum_lookup: dict[str, int]

def addRadioStripMenu(menu: hou.ViewerStateMenu, name: str, label: str, menu_items: Sequence[tuple[str, str]]) -> None:
    """
    Adds the a radio strip to the menu with entries corresponding to the menu
    items.
    """
def findMenuIndex(menu: Iterable[tuple[str, str]], key: str) -> int: ...

class KinefxPendulumMotionControls:
    scene_viewer: hou.SceneViewer
    xform_handle: _Handle
    motionpath_handle: _Handle | None
    delay_traj_computation: bool
    input_geos: Sequence[hou.Geometry] | None
    eval_pend: bool
    show_traj_guide: bool
    pack_verb: hou.SopVerb
    pend_verb: hou.SopVerb
    traj_verb: hou.SopVerb
    pend_geo: hou.Geometry
    pend_guide: hou.SimpleDrawable
    traj_geo: hou.Geometry
    traj_guide: hou.SimpleDrawable
    cube_verb: hou.SopVerb
    sphere_verb: hou.SopVerb
    pivot_geo: hou.Geometry
    pivot_guide: KinefxSelectableDrawable
    start_pos_geo: hou.Geometry
    start_pos_guide: KinefxSelectableDrawable
    end_pos_geo: hou.Geometry
    end_pos_guide: KinefxSelectableDrawable
    selectable_collection: KinefxSelectableDrawableCollection
    selected_handle: int
    pivot: hou.Vector3
    pos_init: hou.Vector3
    pos_final: hou.Vector3
    use_motionpath: bool
    motionpath: str
    pivot_size: float
    start_pos_size: float
    end_pos_size: float
    pend_type: int
    speed_init: float
    def __init__(self, scene_viewer: hou.SceneViewer, xform_handle: _Handle, motionpath_handle: _Handle | None = None, eval_pend: bool = True, input_geos: Sequence[hou.Geometry] | None = None, delay_traj_computation: bool = True, show_traj: bool = True) -> None: ...
    do_read_peak: bool
    def onEnter(self, kwargs: ViewerStateEnterKwargs) -> None: ...
    def onExit(self, kwargs: ViewerStateKwargs) -> None: ...
    def onDraw(self, kwargs: ViewerStateDrawKwargs) -> None: ...
    def setSelectedHandle(self, kwargs: ViewerStateKwargs, handle: int) -> dict[str, Never]: ...
    def onLocatedSelection(self, kwargs: ViewerStateSelectionKwargs) -> None: ...
    def onSelection(self, kwargs: ViewerStateSelectionKwargs) -> dict[str, Never]: ...
    def drawableMask(self) -> None: ...
    def onMouseEvent(self, kwargs: ViewerStateEventKwargs, drawable_selector: str) -> tuple[bool, dict[str, Never]]: ...
    def onMouseWheelEvent(self, kwargs: ViewerStateEventKwargs) -> None: ...
    def onStateToMotionPathHandle(self, kwargs: ViewerStateStateToHandleKwargs, path_geo: hou.Geometry | None = None, key_source_times: Sequence[float] | None = None, source_time_attr: hou.Attrib | None = None) -> None: ...
    def onStateToXformHandle(self, kwargs: ViewerStateStateToHandleKwargs) -> None: ...
    def onXformHandleToState(self, kwargs: ViewerStateHandleToStateKwargs) -> dict[str, int | hou.Vector3]: ...
    def updateHandleEnableParms(self, update_guides: bool = True) -> None: ...
    def updateGuideColors(self) -> None: ...
    def onParmChangeEvent(self, kwargs: ViewerStateParmChangeKwargs) -> dict[str, int]: ...
    def onMenuPreOpen(self, kwargs: ViewerStateMenuPreOpenKwargs) -> None:
        """ onMenuPreOpen handler """
    def onMenuAction(self, kwargs: ViewerStateMenuActionKwargs) -> dict[str, int]:
        """ onMenuAction handler """
    def nodeParms(self) -> dict[str, hou._VerbParmValue]: ...
    def setNodeParmsFromNode(self, node: hou.OpNode, state_parms: _StateParms | None = None) -> None: ...
    def setNodeParms(self, parms: _VerbParms, state_parms: _StateParms | None = None) -> None: ...
    def setPendType(self, pend_type: int, state_parms: _StateParms) -> None: ...
    def trajectoryGeometry(self) -> hou.Geometry: ...
    def trajectoryParm(self, parm: str) -> hou._VerbParmValue: ...
    def setInputGeometry(self, input_geos: Sequence[hou.Geometry] | None) -> None: ...
    def setDisplayGeometry(self, input_geos: Sequence[hou.Geometry] | None = None) -> None: ...
    def setPivotGeometry(self) -> None: ...
    def getPivot(self) -> hou.Vector3: ...
    def startPosition(self) -> hou.Vector3: ...
    def targetPosition(self) -> hou.Vector3: ...
    @staticmethod
    def addDisplayOptionsToMenu(menu: hou.ViewerStateMenu) -> None: ...
    @staticmethod
    def addDisplayParmsToState(template: hou.ViewerStateTemplate, use_motionpath: bool = True) -> None: ...
