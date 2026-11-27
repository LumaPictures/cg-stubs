import hou
import typing
from autorigs.asset.autoRigsAsset import AutoRigsAsset as AutoRigsAsset
from autorigs.modules.base.baseGuideModel import BaseGuideModel as BaseGuideModel
from autorigs.modules.base.buildBaseGuide import BaseGuide as BaseGuide
from autorigs.modules.base.rootModule import Module as Module
from autorigs.modules.geometry.autoRigsGeoBuilder import AutoRigsGeoBuilder as AutoRigsGeoBuilder
from autorigs.utils import captureutils as captureutils, geometryutils as geometryutils, rigutils as rigutils
from collections.abc import Callable as Callable, Iterable, Mapping, Sequence as Sequence
from typing import Any, Concatenate, Generic, TypedDict

from typing import ParamSpec
from typing import TypeAlias
from typing import TypeVar
from typing import ParamSpec
from typing import TypeAlias
from typing_extensions import TypeVar
_PT = TypeVar('_PT', bound=hou.ParmTemplate)
_P = ParamSpec('_P')
_InterfaceEntry: TypeAlias = tuple[str, str] | tuple[str, str, list[str]]
_Guide = TypeVar('_Guide', bound=BaseGuide, default=Any)
_Model = TypeVar('_Model', bound=BaseGuideModel | None, default=Any)
class _BuilderKwargs(TypedDict, total=False):
    prefix: str
    parent: hou.ObjNode | None
    geo_builder: AutoRigsGeoBuilder | None

class AutoRigsBaseBuilder(Generic[_Guide, _Model]):
    index: int
    modulename: str
    moduletype: str
    autorigs_asset: AutoRigsAsset
    assetnode: hou.ObjNode
    buildguide: _Guide
    model: _Model
    parentinfo: tuple[Module, hou.OpNode]
    prefix: str
    parent: hou.ObjNode | None
    geo_builder: AutoRigsGeoBuilder | None
    nodesdatagroups: list['BuilderGroup']
    interface_dict: dict[str, tuple[str, str]]
    main_group: BuilderGroup
    NODEGROUP: str
    BONEGROUP: str
    CONTROLGROUP: str
    VISIBLENODEGROUP: str
    NODES: dict[str, tuple[str]]
    INTERFACE: dict[str, _InterfaceEntry]
    def __init__(self, index: int, modulename: str, moduletype: str, autorigs_asset: AutoRigsAsset, buildguide: _Guide, model: _Model, parentinfo: tuple[Module, hou.OpNode], prefix: str = '', parent: hou.ObjNode | None = None, geo_builder: AutoRigsGeoBuilder | None = None) -> None:
        """
        index: the unique index number of the module for determining the prefix
        modulename: the module's name
        assetnode: the autorig assset node in which to create the rig
        model: the module's model for build options
        buildguide: the module's buildguides
        parentinfo: parentinfo from the parentwidget
        prefix: override prefix to use
        parent: explicit parent node to parent to
        """
    def buildRig(self) -> None:
        """
        Build the rig and creates the autorig interface for the module.
        Override this function if the function orders need to be different.
        """
    def addToNodesDict(self, key: str, name: str) -> None: ...
    def addToInterfaceDict(self, key: str, name: str, label: str) -> None: ...
    def createGroups(self) -> None: ...
    def buildRigControls(self) -> None:
        """
        Creates the bones and controls based on the guide objects.
        prefix: the prefix to use for all the nodes created
        assetnode: the autorig assset node in which to create the rig
        model: the module's model for build options
        buildguide: the module's buildguides 
        parent: a function takes a node as the argument and parent the node
        """
    def createFolderTemplate(self) -> hou.FolderParmTemplate | None:
        """
        Creates the folder parm template for the module.
        model: the module's model for build options
        """
    def linkRigInterfaceParms(self) -> None: ...
    def createAllNodeGroups(self) -> None: ...
    def createNodeGroups(self, grp_idx: int = 0) -> None: ...
    def linkParm(self, node: hou.OpNode, parm_info: tuple[str, str, Iterable[str]]) -> None:
        """
        Links the parameter of a node based on given parm_info
        node: the node to set up the parm expression
        parm_info: (tuple) (parm_id, parm_label, link_parm_id)
        """
    @typing.overload
    def createParm(self, template_type: Callable[Concatenate[str, str, _P], _PT], key: str, *args: _P.args, **kwargs: _P.kwargs) -> _PT: ...
    @typing.overload
    def createParm(self, template_type: type[_PT], key: str, *args: Any, grp_idx: int, **kwargs: Any) -> _PT: ...
    def captureGeometry(self) -> None:
        """Captures the geometry"""
    def addBoneGroupToGeoSkin(self, group: hou.NodeGroup) -> None: ...
    def onCaptureCompleted(self) -> None:
        """Processes to run after geometry is captured"""
    def createGroup(self, group_prefix: str, nodes_dict: Mapping[str, tuple[str]] | None = None, interface_dict: Mapping[str, _InterfaceEntry] | None = None) -> BuilderGroup:
        """
        Creates a new builder group.
        prefix: the prefix for the builder group. The prefix of the module is included by default.
        """
    def createRoot(self, key: str, name: str = '', grp_idx: int = 0, node: hou.ObjNode | None = None) -> hou.ObjNode:
        """Creates a root null modifies node"""
    def createControl(self, key: str, name: str = '', grp_idx: int = 0, node: hou.ObjNode | None = None) -> hou.ObjNode:
        """Creates a control null modifies node"""
    def createNode(self, node_type: str, key: str, name: str = '', grp_idx: int = 0, network: hou.OpNode | None = None, node: hou.OpNode | None = None) -> hou.OpNode:
        """Creates a node of type node_type"""
    def createBone(self, key: str, name: str = '', deform: bool = True, grp_idx: int = 0, node: hou.ObjNode | None = None) -> hou.ObjNode:
        """Creates a bone modifies node
        deform: whether the bone will be captured or not
        """
    def createGeometry(self, key: str, name: str = '', grp_idx: int = 0, node: hou.ObjNode | None = None) -> hou.ObjNode:
        """Creates a geometry node or modifies node"""
    def setParent(self, node: hou.ObjNode | None) -> None: ...
    def getParent(self) -> hou.ObjNode | None:
        """Get the parent hook object"""
    def getPrefix(self, index: int) -> str:
        """Return the node-naming prefix for this module"""
    def getNodeName(self, name: str) -> str: ...
    def getNode(self, key: str, grp_idx: int = 0) -> hou.OpNode: ...
    def getNodes(self, grp_idx: int = 0) -> dict[str, hou.OpNode]: ...
    def getControls(self, grp_idx: int = 0) -> list[hou.ObjNode]: ...
    def getBones(self, grp_idx: int = 0) -> list[hou.ObjNode]: ...
    def getDeformBones(self, grp_idx: int = 0) -> list[hou.ObjNode]: ...
    def getNodeGroups(self, grp_idx: int = 0) -> dict[str, hou.NodeGroup]: ...
    def getGroups(self) -> list['BuilderGroup']: ...
    def getMainGroup(self) -> BuilderGroup: ...
    def getGroup(self, grp_idx: int) -> BuilderGroup: ...

class BuilderGroup:
    module_prefix: str
    group_prefix: str
    prefix: str
    assetnode: hou.ObjNode
    allnodes: dict[str, hou.OpNode]
    bones: list[hou.ObjNode]
    controls: list[hou.ObjNode]
    deforms: list[hou.ObjNode]
    roots: list[hou.ObjNode]
    geos: list[hou.ObjNode]
    groups: dict[str, hou.NodeGroup]
    interface_dict: dict[str, tuple[str, str]]
    NODEGROUP: str
    BONEGROUP: str
    CONTROLGROUP: str
    VISIBLENODEGROUP: str
    DEFORMBONEGROUP: str
    NODES: Mapping[str, tuple[str]]
    INTERFACE: Mapping[str, _InterfaceEntry]
    def __init__(self, assetnode: hou.ObjNode, module_prefix: str, group_prefix: str, nodes_dict: Mapping[str, tuple[str]], interface_dict: Mapping[str, _InterfaceEntry]) -> None: ...
    def createParm(self, template_type: Callable[Concatenate[str, str, _P], _PT], key: str, *args: _P.args, **kwargs: _P.kwargs) -> _PT:
        """
        Creates and adds a parmTemplate of template_type as part of the class
        template_type: one of the hou.ParmTemplate type,
        name: the key and name for the parm (without prefix),
        label: the label for the parm
        """
    def getParmName(self, key: str) -> str: ...
    def getLabelName(self, label: str) -> str: ...
    def createNodeGroups(self) -> None:
        """Convert the data stored to nodegroups"""
    def getPrefix(self) -> str: ...
    def setPrefix(self, prefix: str) -> None: ...
    def createRoot(self, key: str, name: str = '', node: hou.ObjNode | None = None) -> hou.ObjNode:
        """Creates a root null"""
    def createGeometry(self, key: str, name: str = '', node: hou.ObjNode | None = None) -> hou.ObjNode: ...
    def createControl(self, key: str, name: str = '', node: hou.ObjNode | None = None) -> hou.ObjNode:
        """Creates a control null"""
    def createNode(self, node_type: str, key: str, name: str = '', network: hou.OpNode | None = None, node: hou.OpNode | None = None) -> hou.OpNode:
        """Creates a node of type node_type"""
    def createBone(self, key: str, name: str = '', deform: bool = True, node: hou.ObjNode | None = None) -> hou.ObjNode:
        """Creates a bone
        deform: whether the bone will be used to capture or not
        """
    def getNodeName(self, name: str) -> str: ...
    def getNode(self, key: str) -> hou.OpNode: ...
    def hasNode(self, key: str) -> bool: ...
    def getNodes(self) -> dict[str, hou.OpNode]: ...
    def getControls(self) -> list[hou.ObjNode]: ...
    def getBones(self) -> list[hou.ObjNode]: ...
    def getDeformBones(self) -> list[hou.ObjNode]: ...
    def setGroups(self, groups: dict[str, hou.NodeGroup]) -> None: ...
    def getNodeGroups(self) -> dict[str, hou.NodeGroup]: ...
    def getNodeGroup(self, key: str) -> hou.NodeGroup | None:
        """
        Get the converted node group.
        Make sure node groups have been converted first.
        """
    def setConvertFlag(self, flag: bool) -> None: ...
