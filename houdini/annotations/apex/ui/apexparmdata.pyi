from collections.abc import Callable, Sequence

import apex
import hou
from _apex import _PlainValue
from apex.control_2 import ControlMapping
from hrecipes import rtypes
from hrecipes.api import parmtemplatesnippet as pts
from typing_extensions import TypedDict

DEFAULT_KWARGS: list[str]
FOLDER_KWARGS: list[str]
# Attribute class/type name -> the python expression for the hou enum value, for menu scripts.
ATTR_CLS_MAP: dict[str, str]
ATTR_TYPE_MAP: dict[str, str]
PARMTYPE_MAP_DATA: dict[str, str]
PARMTYPE_DEFAULT_DATA: dict[str, int | float | str | bool | hou.Vector2 | hou.Vector3 | hou.Vector4]
FOLDERTYPE_MAP_DATA: dict[str, str]
STORE_PARMDATA: bool

# Preset kwargs: the `preset_kwargs` dict literal of an APEX Script bindInput() call (graphscript's
# _getPresetArgs()), whose values are APEX constants. These are the keys the presets read.
class _PresetOptions(TypedDict, total=False):
    label: str
    label_hidden: bool
    hidden: bool
    joins_with_next: bool
    hide_when: str
    disable_when: str
    # A value, an `{"expression": ...}` dict, or a ramp's number of points.
    default_value: _PlainValue | None
    default_points: rtypes.RampPointDataList
    # The parm templates the override preset wraps.
    inputparmdata: rtypes.ParmTemplateDataDict
    # A control's `menu:<key>` property is an APEX array.
    menu_items: list[str] | list[int] | list[float] | apex.StringArray | apex.IntArray | apex.FloatArray
    menu_labels: list[str]
    prompt_text: str
    help: str
    tooltip: str
    attrib_class: str
    attrib_type: str
    input_geo: int
    path: str
    # Formatted into the menu scripts: a bool or its string form.
    usepattern: bool | str
    filename: bool | str
    tags_only: bool
    controls_menu: bool
    script_action: str
    script_action_help: str
    script_action_icon: str

# What the managers' add*Data() take: the user's dict, to which _createParmTemplateData() adds the
# parm's name and types.
class _PresetKwargs(_PresetOptions, total=False, extra_items=_PlainValue | None):  # type: ignore[call-arg]
    parmname: str
    parmtype: str
    type: str

# What the preset functions get: the kwargs once _createParmTemplateData() has added the parm's
# name, APEX type name and parm template data type.
class _PresetFuncKwargs(_PresetOptions, extra_items=_PlainValue | None):  # type: ignore[call-arg]
    parmname: str
    parmtype: str
    type: str

def overrideTogglePreset(kwargs: _PresetFuncKwargs) -> rtypes.ParmTemplateDataDict: ...
def pythonCodePreset(kwargs: _PresetFuncKwargs) -> rtypes.ParmTemplateDataDict: ...
def vexCodePreset(kwargs: _PresetFuncKwargs) -> rtypes.ParmTemplateDataDict: ...
def packedPathPreset(kwargs: _PresetFuncKwargs) -> rtypes.ParmTemplateDataDict: ...
def packedGeoAttrPreset(kwargs: _PresetFuncKwargs) -> rtypes.ParmTemplateDataDict: ...
def geoGroupPreset(kwargs: _PresetFuncKwargs) -> rtypes.ParmTemplateDataDict: ...
def tagsPreset(kwargs: _PresetFuncKwargs) -> rtypes.ParmTemplateDataDict: ...
def actionButtonPreset(kwargs: _PresetFuncKwargs) -> rtypes.ParmTemplateDataDict: ...
def controlsPreset(kwargs: _PresetFuncKwargs) -> rtypes.ParmTemplateDataDict: ...
def controlShapesPreset(kwargs: _PresetFuncKwargs) -> rtypes.ParmTemplateDataDict: ...
def menuPreset(kwargs: _PresetFuncKwargs) -> rtypes.ParmTemplateDataDict: ...
def colorPreset(kwargs: _PresetFuncKwargs) -> rtypes.ParmTemplateDataDict: ...

PRESET_FUNCS: dict[str, Callable[[_PresetFuncKwargs], rtypes.ParmTemplateDataDict]]

def getValueType(value: _PlainValue | None = ...) -> str | None: ...
def getParmType(valuetype: str | None = ..., value: _PlainValue | None = ...) -> str | None: ...
def getPreset(name: str | None, kwargs: _PresetFuncKwargs) -> rtypes.ParmTemplateDataDict: ...
def getTooltipFromPresetKwargs(kwargs: _PresetOptions) -> str | None: ...
def addTooltipAndHelpToPreset(the_dict: rtypes.ParmTemplateData, preset_kwargs: _PresetOptions) -> None: ...

class ControlParmdataManager:
    data_manager: pts.DataManager
    def __init__(self, container_folder_name: str = ...) -> None: ...
    def data(self) -> pts.ParmTemplateSnippetData: ...
    def parmValues(self) -> dict[str, _PlainValue]: ...
    def control(self) -> str | None: ...
    def addParmData(
        self,
        mapping: ControlMapping,
        key: str,
        value: _PlainValue | None = ...,
        value_type: str | None = ...,
        preset: str | None = ...,
        preset_kwargs: _PresetKwargs | None = ...,
    ) -> None: ...
    def setControl(self, scene: apex.Scene, ctrl_path: str, include_non_animatable: bool = ...) -> None: ...

class GraphParmdataManager:
    graph: apex.Graph | None
    geo: hou.Geometry | None
    data_manager: pts.DataManager
    def __init__(
        self,
        graph: apex.Graph | None = ...,
        geo: hou.Geometry | None = ...,
        node: hou.OpNode | None = ...,
        container_folder_name: str = ...,
    ) -> None: ...
    def data(self) -> pts.ParmTemplateSnippetData: ...
    def parms(self) -> rtypes.ParmDataDict: ...
    def parmTemplates(self) -> rtypes.ParmTemplateDataDict: ...
    def sourceScript(self) -> str | None: ...
    def setSourceScript(self, script: str = ...) -> None: ...
    def validateParm(self, name: str) -> bool: ...
    def load(self, force: bool = ...) -> None: ...
    def update(self, graph: bool = ..., geo: bool = ...) -> None: ...
    def addParmData(
        self,
        name: str,
        value: _PlainValue | None = ...,
        value_type: str | None = ...,
        folder_path: str | None = ...,
        preset: str | None = ...,
        preset_kwargs: _PresetKwargs | None = ...,
    ) -> pts.ParmTemplateSnippetData: ...
    def addFolderData(
        self,
        name: str,
        parm_names: Sequence[str] = ...,
        label: str | None = ...,
        folder_path: str | None = ...,
        folder_type: str | None = ...,
        preset_kwargs: _PresetKwargs | None = ...,
    ) -> pts.ParmTemplateSnippetData: ...
    def addMultiparmEntry(
        self,
        name: str,
        value: _PlainValue | None,
        value_type: str | None = ...,
        folder_path: str | None = ...,
        preset: str | None = ...,
        preset_kwargs: _PresetKwargs | None = ...,
    ) -> pts.ParmTemplateSnippetData: ...
    def updateFromGraphInputs(
        self,
        parm_type_blacklist: Sequence[str] | None = ...,
        parm_blacklist: Sequence[str] | None = ...,
        add_overrride: bool = ...,
        update_geo: bool = ...,
        clear: bool = ...,
    ) -> None: ...
    def updateFromSpareParms(self, folder: str = ..., update_geo: bool = ...) -> None: ...
    def setSpareParms(self, restore_values: bool = ...) -> bool: ...
    def loadAndSetSpareParms(
        self,
        parm_blacklist: Sequence[str] | None = ...,
        update_geo: bool = ...,
        add_override: bool = ...,
        update_from_graph: bool = ...,
    ) -> None: ...
