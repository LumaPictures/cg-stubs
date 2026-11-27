import apex
import hou
import typing
from apex.apexutils import extractCharGeo as extractCharGeo
from apex.componentutils import _DsCategory, _ParmOptions, _ParmTupleEventKwargs
from collections.abc import Iterable, Mapping, Sequence
from houtypes import ParmCallbackKwargs, ViewerStateCommandKwargs, ViewerStateDrawKwargs, ViewerStateEnterKwargs, ViewerStateEventKwargs, ViewerStateHandleToStateKwargs, ViewerStateKwargs, ViewerStateStateToHandleKwargs
from typing import Any, Literal, NoReturn
from typing_extensions import Unpack

CTRL_PROPERTY_TEMPLATE: dict[str, int | hou.Matrix4 | dict[str, dict[str, str]]]
CTRL_OVERRIDES: list[str]
DRAWABLE_OUTPUT: str
CONTROL_EXTENSION: str
GRAPH_EXTENSION: str
COMPONENTSCRIPT_TXT_WARNING: str
COMPONENTSCRIPT_TITLE_WARNING: str
COMPONENTSCRIPT_DETAILS_WARNING: str
COMPONENTSCRIPT_NULL: str
COMPONENTSCRIPT_PARMNODE: str
COMPONENTSTRIPT_SOURCE_PARM: str
COMPONENTSCRIPT_PARM_BLACKLIST: list[str]
COMPONENTSCRIPT_SETUP_FOLDER: str
COMPONENTSCRIPT_SETUP_TUPLE: tuple[str, str]
COMPONENTSCRIPT_PARM_FOLDER: str
COMPONENTSCRIPT_ANIM_FOLDER: str
COMPONENTSCRIPT_SETUP_MULTI: str
COMPONENTSCRIPT_ANIM_PARMS: list[str]
GRAPH_NULL: str
GRAPH_PARMNODE: str
GRAPH_SETUP_FOLDER: str

def getParmTypeFromConnected(vtx: hou.Vertex, registry: apex.Registry) -> None: ...

HUD_TEMPLATE: hou._HudTemplate
type_info: dict[str, tuple[str, int]]
begin_templ: str
end_templ: str
entry_templ: str
begin_tab_templ: str
end_tab_templ: str
menu_templ: str
menu_entry_temp: str
toggle_templ: str
TOGGLE_MENU_TEMPL: str
FLOAT_RAMP_TEMPL: str
COLOR_RAMP_TEMPL: str

def get_dict_array_keys(parms: Iterable[object]) -> list[list[Any]]:
    """returns the keys containing a dict array of a dict. This is needed for filtering out multiparm entries of the attribform parm style dict"""
def get_value_info(value: object) -> tuple[Literal['string', 'multiparm', 'vector', 'int', 'float'], int] | None:
    """returns the value info of a given value formatted in the the ds style """
def ds_menu_template(name: str, entries: Iterable[str], add_overrride_toggles: bool = False, joinnext: str = '', help: str = '') -> str:
    """create ds menu template for a menu with the given name and entries"""
def ds_parm_template(name: str, type_info: tuple[str, int], parm_options: _ParmOptions | None = None, add_overrride_toggles: bool = False, namespace: str | None = None) -> str: ...
def add_multiparm_category(parms: Mapping[str, hou._OptionValue], multi_name: str, all_names: list[str], all_categories: list[_DsCategory], parm_options: _ParmOptions, add_overrride_toggles: bool = False, namespace: str | None = None) -> None: ...
def add_ds_category(ds: str, category: _DsCategory, all_category_names: Sequence[str], all_categories: Sequence[_DsCategory], built_categories: list[str]) -> tuple[str, list[str]]: ...
@typing.overload
def dsFromGraphInputs(apexgraph: hou.Geometry, graph: apex.Graph, add_overrride_toggles: bool = ..., namespace: str | None = ..., getParms: Literal[False] = ...) -> str: ...
@typing.overload
def dsFromGraphInputs(apexgraph: hou.Geometry, graph: apex.Graph, add_overrride_toggles: bool = ..., namespace: str | None = ..., *, getParms: Literal[True]) -> tuple[str, list[str]]: ...
@typing.overload
def dsFromGraphInputs(apexgraph: hou.Geometry, graph: apex.Graph, add_overrride_toggles: bool, namespace: str | None, getParms: Literal[True]) -> tuple[str, list[str]]: ...
@typing.overload
def dsFromGraphInputs(apexgraph: hou.Geometry, graph: apex.Graph, add_overrride_toggles: bool = ..., namespace: str | None = ..., getParms: bool = ...) -> str | tuple[str, list[str]]: ...
def set_parm(node: hou.OpNode, parm: str, value: hou._OptionValue) -> None:
    """Sets the parm value for a node. Multiparms and parm tuples will automatically detected and the values will be 
    accordingly set for those types as well. Only existing parms will be set. 
    :param node: the hou.Node 
    :param parm: the name of the parm to be set
    :param value: the value of the parm to be set. 
    """
def save_parm_values(node: hou.OpNode) -> tuple[hou._OptionDict, bytes | None]:
    """stores the current values based on an attrib from parm format plus the clip data of a given set of parms. This will be in the future replaces by the node.asData() api. """
def restore_parm_values(node: hou.OpNode, attr_parms: Mapping[str, hou._OptionValue], data: bytes | None, parentfolder: str | None = None, default_dict: Mapping[str, hou._OptionValue] | None = None) -> None:
    """reapllies values plus keyed clip data to a given set of parms. This will be in the future replaces by the node.asData() api. """
def rigparms_from_graph(node: hou.OpNode, graph_geo: hou.Geometry, graph: apex.Graph, name: str, namespace: str = '', parentfolder: str | None = None) -> list[str]: ...
def parms_from_graph(kwargs: ParmCallbackKwargs) -> None: ...
def componentparms_from_graph(kwargs: ParmCallbackKwargs) -> None: ...
def clearComponentAnimationParms(node: hou.OpNode) -> None: ...
def updateComponentAnimationParms(kwargs: ParmCallbackKwargs) -> None: ...
def updateRigNode(node: hou.OpNode, **kwargs: Unpack[_ParmTupleEventKwargs]) -> None: ...
def frameSelectedGeos(scene_viewer: hou.SceneViewer, geos: Iterable[hou.Geometry], zoom_factor: float = 1.0) -> None: ...

class ApexStateError(Exception):
    def __init__(self, text: str) -> None: ...
    def text(self) -> str: ...

def preprosses_ctrl_graph(graph_geo: hou.Geometry, drawable_output_name: str | None = None, character_name: str | None = None) -> hou.Geometry: ...

class PoseToolHotkey:
    """_summary_

    small wrapper to make it easier to fetch custom HK elements for the pose state 
    """
    name: str
    hk: str
    HK_CTXT: str
    def __init__(self, name: str, hotkey: str) -> None: ...
    def hkname(self) -> str: ...
    def fullname(self) -> str: ...
    def nicename(self) -> str: ...

def loadWidget(path: str) -> NoReturn: ...

class Dummy:
    state_name: str
    scene_viewer: hou.SceneViewer
    geometry: hou.Geometry
    line_gadget: hou.GadgetDrawable
    face_gadget: hou.GadgetDrawable
    point_gadget: hou.GadgetDrawable
    def __init__(self, state_name: str, scene_viewer: hou.SceneViewer) -> None: ...
    def onEnter(self, kwargs: ViewerStateEnterKwargs) -> None: ...
    def onGenerate(self, kwargs: ViewerStateKwargs) -> None: ...
    def onMouseEvent(self, kwargs: ViewerStateEventKwargs) -> None: ...
    def onStateToHandle(self, kwargs: ViewerStateStateToHandleKwargs) -> None: ...
    def onHandleToState(self, kwargs: ViewerStateHandleToStateKwargs) -> None: ...
    def onDraw(self, kwargs: ViewerStateDrawKwargs) -> None: ...
    def onDrawInterrupt(self, kwargs: ViewerStateDrawKwargs) -> None: ...
    def onCommand(self, kwargs: ViewerStateCommandKwargs) -> None: ...
    @property
    def state_gadgets(self) -> Mapping[str, hou.GadgetDrawable]: ...
    @property
    def state_context(self) -> hou.ViewerStateContext: ...

def buildStateTemplate(name: str, label: str, obj: hou._SceneViewerStateFactory) -> hou.ViewerStateTemplate: ...
def bindHandle(template: hou.ViewerStateTemplate, name: str) -> hou.ViewerStateTemplate: ...
def bindGadgets(template: hou.ViewerStateTemplate) -> hou.ViewerStateTemplate: ...
def registerState(template: hou.ViewerStateTemplate) -> None: ...
