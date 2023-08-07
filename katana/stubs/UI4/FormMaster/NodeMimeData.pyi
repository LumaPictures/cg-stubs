# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import DrawingModule as DrawingModule
import UI4.Util.IconManager as IconManager
import NodeGraphTab
import NodegraphAPI as NodegraphAPI
import PyQt5.QtCore
import QT4Widgets as QT4Widgets
import PyQt5.QtCore as QtCore
import Nodes3DAPI.ShadingNodeBase as ShadingNodeBase
import Utils as Utils
from UI4.Util.ScenegraphLocation import GetNodesCreatingSceneGraphLocations as GetNodesCreatingSceneGraphLocations
from typing import Set, Tuple

MIME_TYPE_NODEREFS: str
MIME_TYPE_NODES: str

def CheckNodeMimeData(mimeData, requireExtant: bool = ...): ...
def GetNodeMimeData(nodeList): ...
def GetNodesFromMimeData(mimeData: PyQt5.QtCore.QMimeData, raiseIfMissingData: bool = ...) -> list: ...
def StartNodeDrag(nodeList, dragSource): ...
def StartPortDrag(port: NodegraphAPI.Port, dragSource: NodeGraphTab.NodegraphWidget): ...
