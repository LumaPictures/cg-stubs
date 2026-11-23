from .box import Box as Box
from collections.abc import Iterable, Mapping, MutableSequence
from houtypes import JSONLike, JSONValue
from hutil.Qt import QtGui
from typing import TypedDict

class _BVHNodeJSON(TypedDict):
    name: str
    box: list[float] | None
    level: int
    weight: int
    memory: int
    netMemory: int
    overlap: float
    netOverlap: float
    peakOverlap: float
    children: list['_BVHNodeJSON']

class _BVHSceneJSON(TypedDict):
    Scene: list[_BVHNodeJSON]
    processed: bool

class _BVHRawSceneJSON(TypedDict):
    Scene: dict[str, JSONValue]

class BVHTreeNode:
    name: str
    box: Box | None
    level: int
    weight: int
    memory: int
    netMemory: int
    overlap: float
    netOverlap: float
    peakOverlap: float
    averageOverlap: float
    children: list['BVHTreeNode']
    parent: BVHTreeNode | None
    def __init__(self, name: str, box: Box | None = None, parent: BVHTreeNode | None = None) -> None: ...
    def append(self, node: BVHTreeNode) -> None: ...
    def toJSONDict(self) -> _BVHNodeJSON: ...
    def getJSON(self, json_parent: MutableSequence[_BVHNodeJSON]) -> None: ...
    def setJSON(self, json_array: Iterable[_BVHNodeJSON]) -> None: ...
    def propogateData(self) -> None: ...

class BVHTreeMenuItem(QtGui.QStandardItem):
    node: BVHTreeNode
    def __init__(self, node: BVHTreeNode) -> None: ...

class BVHTree:
    root: BVHTreeNode | None
    def __init__(self) -> None: ...
    def hasDictChildren(self, value: Mapping[str, JSONLike]) -> bool: ...
    def appendTree(self, key: str, value: object, parent: BVHTreeNode, tree_list: list[BVHTreeNode | None] | None = None) -> None: ...
    def parseJSON(self, json_dict: _BVHSceneJSON | _BVHRawSceneJSON) -> None: ...
    def getJSON(self) -> _BVHSceneJSON: ...
    def appendMenu(self, tree_node: BVHTreeNode, menu_parent: QtGui.QStandardItem) -> None: ...
    def attachToMenu(self, menu_root: QtGui.QStandardItem) -> None: ...
