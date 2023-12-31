# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import NodegraphAPI as NodegraphAPI
import PackageSuperToolAPI.Packages
import Utils as Utils
from Utils.Decorators import deprecated as deprecated
from _typeshed import Incomplete
from typing import Set, Tuple

__NODEDELETIONGUARD_PARAMETER_NAME: str
__g_nodeRefPrefix: str
__g_superToolGroupName: str

def AddNodeRef(destNodeOrGroupParam: NodegraphAPI.Node | NodegraphAPI.GroupParameter, key: str, node: NodegraphAPI.Node): ...
def AddPackageTypeAndPath(node: NodegraphAPI.Node, packageType: str, locationPath: str): ...
def AppendNode(nodeA: NodegraphAPI.Node, nodeB: NodegraphAPI.Node): ...
def AppendNodes(parentGroupNode: NodegraphAPI.Node, nodes: tuple[NodegraphAPI.Node, ...]): ...
def DeleteDeepParameter(parentGroupParam: NodegraphAPI.GroupParameter, paramPath: str): ...
def GetDownstreamNodes(node: NodegraphAPI.Node) -> set[NodegraphAPI.Node]: ...
def GetDownstreamPorts(port: NodegraphAPI.Port): ...
def GetEditPackageForLocationPath(mainNode: NodegraphAPI.Node, locationPath: str) -> PackageSuperToolAPI.Packages.Package | None: ...
def GetEditPackageLocationPaths(mainNode: NodegraphAPI.Node) -> list[str]: ...
def GetEditPackages(mainNode: NodegraphAPI.Node) -> list[PackageSuperToolAPI.Packages.Package]: ...
def GetPackageLocationParameterPath() -> str: ...
def GetPackageTypeParameterPath() -> str: ...
def GetRefNode(nodeOrGroupParam: NodegraphAPI.Node | NodegraphAPI.GroupParameter, key: str) -> NodegraphAPI.Node | None: ...
def GetSceneGraphPathExpression(package: PackageSuperToolAPI.Packages.Package, path: str, raiseOnMissing: bool = ...) -> str: ...
def GetSuperToolGroupName() -> str: ...
def GetUpstreamPort(port: NodegraphAPI.Port): ...
def IsNodeGuardedFromDeletion(node: NodegraphAPI.Node) -> bool: ...
def NodeDeletionGuard(node: NodegraphAPI.Node): ...
def PositionMergeInputs(mergeNode: NodegraphAPI.Node): ...
def PrependNode(nodeA: NodegraphAPI.Node, nodeB: NodegraphAPI.Node): ...
def RemoveNodeRef(nodeOrGroupParam: NodegraphAPI.Node | NodegraphAPI.GroupParameter, key: str): ...
def SetOrCreateDeepArrayParameter(parentGroupParam: NodegraphAPI.GroupParameter, paramPath: str, paramValue: list[str | int | float]) -> NodegraphAPI.GroupParameter: ...
def SetOrCreateDeepScalarParameter(parentGroupParam: NodegraphAPI.GroupParameter, paramPath: str, paramValue: str | int | float, hintString: Incomplete | None = ...) -> NodegraphAPI.GroupParameter: ...
def SetOrCreateDeepVectorParameter(parentGroupParam, paramPath, paramValue): ...
def SetPackageNodeName(package: PackageSuperToolAPI.Packages.Package): ...
def TransferNodeConnections(oldNode: NodegraphAPI.Node, newNode: NodegraphAPI.Node): ...
def UpdateChildPackagePaths(inputPackage: PackageSuperToolAPI.Packages.Package): ...
def UpdateEditPackagePaths(mainNode: NodegraphAPI.Node, previousRootLocationPath: str): ...
def WireInlineNodes(parentGroupNode: NodegraphAPI.GroupNode, nodes: list[NodegraphAPI.Node], x: int = ..., y: int = ...): ...
