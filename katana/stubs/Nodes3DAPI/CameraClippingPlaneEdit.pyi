# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyFnAttribute as FnAttribute
import Nodes3DAPI.Node3D as Node3D
import NodegraphAPI as NodegraphAPI
from Nodes3DAPI.GenericAssign import GenericAssign as GenericAssign
from _typeshed import Incomplete
from typing import Set, Tuple

_ExtraHints: dict
_Parameter_XML: str

class CameraClippingPlaneEdit(GenericAssign):
    def __init__(self) -> None: ...
    def _filterAttrList(self, graphState, attrList): ...
    def _getExtraAttrs(self, frameTime): ...
    def _getStaticAttrHintsForIncomingSceneQuery(self, attrPath): ...
    def addParameterHints(self, attrName, inputDict): ...
    def canOverride(self, attrName): ...
    def setOverride(self, path, attrName, time, attrData, attrType: Incomplete | None = ..., attrTupleSize: Incomplete | None = ..., makeEmptyGroup: bool = ..., groupInherit: bool = ..., index: Incomplete | None = ...): ...
