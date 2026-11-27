import apex
import hou
from _apex import _PlainValue
from apex.control_2 import ControlMapping as ControlMapping
from collections.abc import Callable as Callable, Sequence
from hrecipes import rtypes
from hrecipes.api import parmtemplatesnippet as pts
from typing_extensions import TypedDict

class _PresetOptions(TypedDict, total=False):
    label: str
    label_hidden: bool
    hidden: bool
    joins_with_next: bool
    hide_when: str
    disable_when: str
    default_value: _PlainValue | None
    default_points: rtypes.RampPointDataList
    inputparmdata: rtypes.ParmTemplateDataDict
    menu_items: list[str] | list[int] | list[float] | apex.StringArray | apex.IntArray | apex.FloatArray
    menu_labels: list[str]
    prompt_text: str
    help: str
    tooltip: str
    attrib_class: str
    attrib_type: str
    input_geo: int
    path: str
    usepattern: bool | str
    filename: bool | str
    tags_only: bool
    controls_menu: bool
    script_action: str
    script_action_help: str
    script_action_icon: str

class _PresetKwargs(_PresetOptions, total=False, extra_items=_PlainValue | None):  # type: ignore[call-arg]
    parmname: str
    parmtype: str
    type: str

class _PresetFuncKwargs(_PresetOptions, extra_items=_PlainValue | None):  # type: ignore[call-arg]
    parmname: str
    parmtype: str
    type: str

PARMS_PROP: str
PARMVALUE_PROP: str
PARMTEMPLATE_PROP: str
PARMORDER_PROP: str
PARMNAME_PROP: str
PARMTYPE_PROP: str
INPUTDATA_PROP: str
INSERT_FIRST_PROP: str
LABEL_DATA: str
LABEL_VIS_DATA: str
DEFAULT_VALUE_DATA: str
DEFAULT_POINTS_DATA: str
LABELS_DATA: str
ITEMS_DATA: str
HIDE_WHEN_DATA: str
DISABLE_WHEN_DATA: str
JOIN_NEXT_DATA: str
HIDDEN_DATA: str
PROMPT_DATA: str
TYPE_DATA: str
HELP_DATA: str
TOOLTIP_DATA: str
DEFAULT_KWARGS: list[str]
FOLDER_KWARGS: list[str]
OVERRIDE_PRESET: str
PYTHON_PRESET: str
VEX_PRESET: str
OPENCL_PRESET: str
TAGS_PRESET: str
CONTROLS_PRESET: str
ATTR_PRESET: str
PATH_PRESET: str
CONTROL_SHAPE_PRESET: str
MENU_PRESET: str
COLOR_PRESET: str
SCRIPT_ACTION_PRESET: str
ATTR_CLS_MAP: dict[str, str]
ATTR_TYPE_MAP: dict[str, str]
ATTR_CLS_KWARGS: str
ATTR_TYPE_KWARGS: str
INPUT_GEO_KWARGS: str
TAGS_ONLY_KWARGS: str
CONTROLS_MENU_KWARGS: str
INPUT_PATH_KWARGS: str
TAG_PATTERN_KWARGS: str
FILENAME_KWARGS: str
SCRIPT_ACTION_HELP_KWARGS: str
SCRIPT_ACTION_ICON_KWARGS: str
SCRIPT_ACTION_KWARGS: str
PARMTYPE_MAP_DATA: dict[str, str]
PARMTYPE_DEFAULT_DATA: dict[str, int | float | str | bool | hou.Vector2 | hou.Vector3 | hou.Vector4]
FOLDERTYPE_MAP_DATA: dict[str, str]
FOLDER_TAB: str
STORE_PARMDATA: bool

def overrideTogglePreset(kwargs: _PresetFuncKwargs) -> rtypes.ParmTemplateDataDict: ...
def pythonCodePreset(kwargs: _PresetFuncKwargs) -> rtypes.ParmTemplateDataDict:
    """python code multi line string snippet for a string input
    """
def vexCodePreset(kwargs: _PresetFuncKwargs) -> rtypes.ParmTemplateDataDict:
    """vex code multi line string snippet for a string input
    """
def packedPathPreset(kwargs: _PresetFuncKwargs) -> rtypes.ParmTemplateDataDict:
    """
    dropdown menu for paths of a packed input geo. the paths can be filtered with a path pattern.
    'filename': True shows only the last path component instead of the full path
    """
def packedGeoAttrPreset(kwargs: _PresetFuncKwargs) -> rtypes.ParmTemplateDataDict:
    """
    dropdown menu for attribs on a packed input geo defined by a path
    """
def geoGroupPreset(kwargs: _PresetFuncKwargs) -> rtypes.ParmTemplateDataDict:
    """
    fetches defaults from 
    """
def tagsPreset(kwargs: _PresetFuncKwargs) -> rtypes.ParmTemplateDataDict:
    """
    fetches defaults from 
    """
def actionButtonPreset(kwargs: _PresetFuncKwargs) -> rtypes.ParmTemplateDataDict:
    """
    generates an action button for 
    """
def controlsPreset(kwargs: _PresetFuncKwargs) -> rtypes.ParmTemplateDataDict:
    """
    string input with a select-controls button and a dropdown menu.
    'controls_menu': True lists the rig controls in the menu instead of the tags
    """
def controlShapesPreset(kwargs: _PresetFuncKwargs) -> rtypes.ParmTemplateDataDict:
    """
    fetches defaults from 
    """
def menuPreset(kwargs: _PresetFuncKwargs) -> rtypes.ParmTemplateDataDict:
    """
    creates an as data preset for an ordered Menu 
    kwargs[menu_items] = defines the item values
    kwargs[menu_labels] = defines the item labels
    """
def colorPreset(kwargs: _PresetFuncKwargs) -> rtypes.ParmTemplateDataDict:
    """
    creates an as data preset for an ordered Menu 
    kwargs[menu_items] = defines the item values
    kwargs[menu_labels] = defines the item labels
    """

PRESET_FUNCS: dict[str, Callable[[_PresetFuncKwargs], rtypes.ParmTemplateDataDict]]

def getValueType(value: _PlainValue | None = None) -> str | None:
    """returns the apex value type name based on a given value"""
def getParmType(valuetype: str | None = None, value: _PlainValue | None = None) -> str | None:
    """returns the as data parameter type wether based on a valuetype name from apex or on a 
    given value"""
def nameToLabel(name: str) -> str:
    """process the name for be a pretty label"""
def getPreset(name: str | None, kwargs: _PresetFuncKwargs) -> rtypes.ParmTemplateDataDict:
    """get a as data dict style preset from the preshipped parm template preset functions. 
    A preset function always needs to return a parm template dict in the as data style"""
def getTooltipFromPresetKwargs(kwargs: _PresetOptions) -> str | None:
    """ Get tooltip/help from preset kwargs. Prioritize 'help' first then 'tooltip'. """
def addTooltipAndHelpToPreset(the_dict: rtypes.ParmTemplateData, preset_kwargs: _PresetOptions) -> None:
    """
    Add the help and tooltip entries to the preset and make them the same.
    Prioritize 'help' in the preset_kwargs, and if not found use 'tooltip'.

    :param the_dict: The preset dict i.e. parmData[name]
    :param preset_kwargs: THe preset kwargs.
    """

class ControlParmdataManager:
    data_manager: pts.DataManager
    def __init__(self, container_folder_name: str = 'parameters') -> None: ...
    def data(self) -> pts.ParmTemplateSnippetData:
        """Returns dictionary data that can be stored under the 'properties' global attribute. This dict has three
        keys, 'parms', 'parmtemplates' and 'source_script'. See functions below if you want to access the content of these keys individually.
        There is no corresponding setter function to this, as this data should not be directly set.
        """
    def parmValues(self) -> dict[str, _PlainValue]:
        """returns the current values of the parameters of the current control
        """
    def control(self) -> str | None: ...
    def addParmData(self, mapping: ControlMapping, key: str, value: _PlainValue | None = None, value_type: str | None = None, preset: str | None = None, preset_kwargs: _PresetKwargs | None = None) -> None:
        """add a parm data entry into the data. We do leave the option open to add an load presets
        :param name: the name of the parameter
        :param value: a numerical or string value type
        :param value_type: name and apex numerical, string or ramp time. other types are currently not supported
        """
    def setControl(self, scene: apex.Scene, ctrl_path: str, include_non_animatable: bool = True) -> None:
        """creates the parminterface for a current provided control. The parm interface can directly
        be provided with a properties entry on the node itself

        :param scene: _description_
        :param ctrl_path: _description_
        :param include_non_animatable: defines if we want to create a parm interface , defaults to True
        """

class GraphParmdataManager:
    """manages the graph parm interfaces on the properties of an apex graphs or geometry stored in the asData parm format
    """
    graph: apex.Graph | None
    geo: hou.Geometry | None
    data_manager: pts.DataManager
    def __init__(self, graph: apex.Graph | None = None, geo: hou.Geometry | None = None, node: hou.OpNode | None = None, container_folder_name: str = 'parameters') -> None: ...
    def data(self) -> pts.ParmTemplateSnippetData:
        """Returns dictionary data that can be stored under the 'properties' global attribute. This dict has three
        keys, 'parms', 'parmtemplates' and 'source_script'. See functions below if you want to access the content of these keys individually.
        There is no corresponding setter function to this, as this data should not be directly set.
        """
    def parms(self) -> rtypes.ParmDataDict:
        """Returns dictionary of parm values data that can be stored under the 'parms' global attribute.
        It seems that apex::autorigcomponent::2.0 does store this information separately from 'properties'.
        There is no corresponding setter function to this, as this data should not be directly set.
        """
    def parmTemplates(self) -> rtypes.ParmTemplateDataDict:
        """Returns dictionary of parmtemplates data that can be stored under the 'parmtemplates' global attribute.
        There is no corresponding setter function to this, as this data should not be directly set.
        """
    def sourceScript(self) -> str | None:
        """Returns script that is used to generate the data if any.
        """
    def setSourceScript(self, script: str = '') -> None:
        """Sets the script used to generate the data. Setting the script will not update any internal data structure,
        This is helpful to set the script with this manager class, rather than use an Attribute Adjust Dictionary Sop
        to override the corresponding attribute.
        """
    def validateParm(self, name: str) -> bool:
        """we for now just invalidate the parm if a graph is actually provide and the given parm is there, we let the test pass
        if no graph is given. TBD
        """
    def load(self, force: bool = False) -> None:
        """loads the current properties either from a graph or a graph geometry if any provided
        """
    def update(self, graph: bool = True, geo: bool = True) -> None:
        """
        updates the given graph or geometry that is being associated with the properties dict to the current properties
        value
        """
    def addParmData(self, name: str, value: _PlainValue | None = None, value_type: str | None = None, folder_path: str | None = None, preset: str | None = None, preset_kwargs: _PresetKwargs | None = None) -> pts.ParmTemplateSnippetData:
        """add a parm data entry into the data. This can be used, for example, by
        apex script to predefine presets per bind input operation
        :param name: the name of the parameter
        :param value: a numerical or string value type
        :param value_type: name and apex numerical, string or ramp time. other types are currently not supported
        :param folder_path: the name (or unix path) of the folder under which to parent this parameter
        """
    def addFolderData(self, name: str, parm_names: Sequence[str] = ..., label: str | None = None, folder_path: str | None = None, folder_type: str | None = None, preset_kwargs: _PresetKwargs | None = None) -> pts.ParmTemplateSnippetData:
        """adds a given list of predefined parameters of the current template to a given folder
        this allows us to dynamically restructure an existing parm template.
        we can work deep nesting since the parentfolder defines a parent directory. non existing parent folders
        will be automatically added. the directory path is intended to be similar to the packfolder structure

        :param name: name of the new folder to be added
        :param parm_names: the parm names of the existing parm template that are to be parented under the new folder
        ATTENTION. only parm names not folder names are to be listed here
        :param label: label of the new folder, defaults to None
        :param folder_path: the directory of the parent folder, defaults to None
        :param folder_type: the type of folder the naming relies on the asData() folder names, defaults to None
        :param preset_kwargs: optional preset kwargs; the folder-applicable subset (FOLDER_KWARGS, e.g.
        disable_when/hide_when/joins_with_next/hidden) is applied to the folder template, and 'label' is used
        as a fallback when no explicit label arg is given.
        """
    def addMultiparmEntry(self, name: str, value: _PlainValue | None, value_type: str | None = None, folder_path: str | None = None, preset: str | None = None, preset_kwargs: _PresetKwargs | None = None) -> pts.ParmTemplateSnippetData:
        """_summary_

        :param name: _description_
        :param value: _description_
        :param value_type: _description_, defaults to None
        :param folder_path: _description_, defaults to None
        :param preset: _description_, defaults to None
        :param preset_kwargs: _description_, defaults to None
        :raises hou.Error: _description_
        :raises hou.Error: _description_
        :return: _description_
        """
    def updateFromGraphInputs(self, parm_type_blacklist: Sequence[str] | None = None, parm_blacklist: Sequence[str] | None = None, add_overrride: bool = False, update_geo: bool = True, clear: bool = False) -> None:
        """updates the parm template metadata to the current graph inputs on the graph properties
        no op node dependency. 
        the stored format is based on the node.asData() json format style, used for example in recipes

        :param graph: the graph to get create a parm interface for
        :param add_overrride_toggles: add an override toggle in front of each parm of the interface. 
        the parm then gets automatically disabled if the toggle is off, defaults to False
        :param parm_type_blacklist: parm data types that should be excluded from the interface, defaults to None
        :param parm_blacklist: parms that should be excluded from the parm interface, defaults to None
        :param foldername: defines into which folder the spare parms are to be parented if applied to a sop node
        """
    def updateFromSpareParms(self, folder: str = 'parameters', update_geo: bool = True) -> None:
        """updates properties of a graph geo to match the current spare parm interface of a the given sop node

        :param node: the hou node that has the spare parm interface to be stored
        :param geo: the graph geometry to st
        :return: _description_
        """
    def setSpareParms(self, restore_values: bool = True) -> bool:
        """reads asData information either given as an input dict or that have beend stored on geo, 
        and applies the spare parms to a given node under a specified folder

        :param node: _description_
        :param properties: _description_, defaults to None
        :param graph_geo: _description_, defaults to None
        :param folder: _description_, defaults to None
        :return: True if spare parms could be added else false
        """
    def loadAndSetSpareParms(self, parm_blacklist: Sequence[str] | None = None, update_geo: bool = False, add_override: bool = False, update_from_graph: bool = True) -> None:
        """
        wrapper function to update the spare parm interface of graph editing nodes, such as apex script, apex configure graph and graph edit
        loads the current existing properties, updates them to make sure that the given graph input is in matching the parms and updates the spare 
        parm interface of a tiven 

        :param parm_blacklist: a list of parameters to be ignored for the parm interface , defaults to None
        """
