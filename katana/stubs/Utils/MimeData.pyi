# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import NodegraphAPI
import PyQt5.QtCore
import PyQt5.QtGui
import PyQt5.QtCore as QtCore
import typing
from typing import Set, Tuple

MIME_TYPE_COLLECTIONS: str
MIME_TYPE_LOCATIONPATHS: str
MIME_TYPE_NODEREFS: str
MIME_TYPE_NODES: str
MIME_TYPE_PYTHON: str

def GetCollections(mimeDataOrDropEvent: PyQt5.QtCore.QMimeData | PyQt5.QtGui.QDropEvent) -> typing.Optional[list[d]]: ...
def GetLocationPaths(mimeDataOrDropEvent: PyQt5.QtCore.QMimeData | PyQt5.QtGui.QDropEvent, excludePolicyXML: bool = ...) -> typing.Optional[list[s]]: ...
def GetNodes(mimeDataOrDropEvent: PyQt5.QtCore.QMimeData | PyQt5.QtGui.QDropEvent, nodesCreatingSceneGraphLocationsOnly: bool = ...) -> list | None: ...
def SetCollections(mimeData: PyQt5.QtCore.QMimeData, collectionMaps: list[dict]): ...
def SetLocationPaths(mimeData: PyQt5.QtCore.QMimeData, locationPaths): ...
def SetNodes(mimeDataOrDragObject: PyQt5.QtCore.QMimeData | PyQt5.QtGui.QDrag, nodeNamesOrNodes: str | NodegraphAPI.Node | list[str | NodegraphAPI.Node]): ...
