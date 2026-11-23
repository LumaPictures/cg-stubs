import hou
from autorigs.modules.base.autoRigsBaseBuilder import BuilderGroup as BuilderGroup
from collections.abc import Iterable, Mapping, Sequence
from typing import Any

from typing import TypeAlias
from typing import TypeAlias
_NameLabel: TypeAlias = Mapping[str, tuple[str, str] | tuple[str, str, Sequence[str]]]
SET_DEFAULT_FCN_PREFIX: str
SET_DEFAULT_ALL_FCN_PREFIX: str
SET_DEFAULT_FCN_HEADER: str
SET_DEFAULT_ALL_FCN_HEADER: str
SET_KEY_FCN_PREFIX: str
SET_KEY_ALL_FCN_PREFIX: str
SET_KEY_FCN_HEADER: str
SET_KEY_ALL_FCN_HEADER: str

def getNameTransform(namelabel: _NameLabel, prefix: str, controltype: str, transform: str) -> str: ...
def getLabelTransform(namelabel: _NameLabel, prefix: str, controltype: str, transform: str) -> str: ...
def createTransformTemplate(namelabel: _NameLabel, prefix: str, controlname: str, transform: str, components: int = 3, defaults: Sequence[float] = (0, 0, 0)) -> hou.FloatParmTemplate: ...
def linkTransformTemplate(namelabel: _NameLabel, assetnode: hou.OpNode, controls: Mapping[str, Any], prefix: str, controlname: str, interfacename: str, transform: str) -> None: ...
def createTransformTemplates(namelabel: _NameLabel, prefix: str, interface_control_keys: Iterable[Sequence[str]], foldertemplate: hou.FolderParmTemplate, controls: Mapping[str, Any]) -> hou.FolderParmTemplate: ...
def createDisplayTemplate(namelabel: _NameLabel, displaykey: str, prefix: str, menulabel: Sequence[str], default_display: int = 0) -> hou.MenuParmTemplate: ...
def createButtonTemplate(namelabel: _NameLabel, displaykey: str, prefix: str) -> hou.ButtonParmTemplate: ...
def addCallback(template: hou.ParmTemplate, function_header: str) -> None: ...
def addResetToDefaultCallback(button: hou.ParmTemplate) -> None: ...
def addSetKeyCallback(button: hou.ParmTemplate) -> None: ...
def linkDisplayTemplateFKIK(controls: Mapping[str, Any], controlkeys: Iterable[str], assetnode: hou.OpNode, displayname: str, displayfkikname: str, displayformat: str) -> None: ...
def linkDisplayTemplate(controls: Mapping[str, Any], controlkeys: Iterable[str], assetnode: hou.OpNode, displayname: str, displayformat: str) -> None: ...
def linkSwitchTemplate(controls: Mapping[str, Any], controlkeys: Iterable[str], assetnode: hou.OpNode, displayname: str, displayformat: str) -> None: ...
def linkTransformTemplates(namelabel: _NameLabel, assetnode: hou.OpNode, controls: Mapping[str, Any], prefix: str, interface_control_keys: Iterable[Sequence[str]]) -> None: ...
def linkTransformTemplatesObj(assetnode: hou.OpNode, interfacename_controls: Iterable[tuple[str, hou.OpNode, str]]) -> None:
    """
    Link the given transform (t, r, s) parm templates
    assetnode: (hou.ObjNode) the assetnode with the autorigs interface
    interfacename_controls: (List) (parmname, rigcontrol, transforms)
    """
def linkTransformTemplateObj(assetnode: hou.OpNode, control: hou.OpNode, interface_name: str, transform: str) -> None:
    """
    Link the transform parm template interface to the control.
    assetnode: (hou.Node) the autorigs node,
    control: (hou.Node) the control with the parameter to be linked,
    interface_name: (str) the interface/parameter name,
    transform: (str) the transform to link 
    """
def getNamePrefix(namelabel: _NameLabel, index: int) -> str: ...
def getName(namelabel: _NameLabel, prefix: str, controltype: str) -> str: ...
def getLabel(namelabel: _NameLabel, controltype: str) -> str: ...
def relativePathChParmTo(node: hou.NetworkMovableItem, relnode: hou.NetworkMovableItem, parm: str) -> str: ...
def linkDisplay(assetnode: hou.OpNode, parm_id: str, nodesgroup: hou.NodeGroup, indexes: Sequence[int]) -> None:
    """
    Link the display of the controlgroup to autorig display enum parameter.
    This function will not override existing linking of display to other parameters.
    assetnode: the autorigs node
    parm_id: the name of the paramater used in expression
    nodesgroup: the nodesgroup to link the display to
    indexes: (Tuples) the indexes of the enum to map the display
    """
def create01Slider(key: str, grp: BuilderGroup) -> hou.FloatParmTemplate:
    """
    Creates a 0 to 1 float slider with strict min and max.
    id: the name/id of the parm,
    label: the label of the parm,
    grp: (BuilderGroup) the builder group to create the parm
    """
