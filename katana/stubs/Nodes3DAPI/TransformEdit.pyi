# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import Nodes3DAPI.DynamicParameterUtil as DynamicParameterUtil
import PyFnAttribute as FnAttribute
import PyFnGeolib as FnGeolib
import NodegraphAPI as NodegraphAPI
import Nodes3DAPI_cmodule as Nodes3DAPI_cmodule
import Utils as Utils
from Nodes3DAPI.Node3D import Node3D as Node3D
from _typeshed import Incomplete
from typing import ClassVar

_ParamHints: dict
_Parameter_XML: str

class TransformEditNode(Node3D):
    Action_addNewTransform: ClassVar[str] = ...
    Action_overrideInteractive: ClassVar[str] = ...
    Action_replaceAll: ClassVar[str] = ...
    def __init__(self): ...
    def _TransformEditNode__getOverrideParameterPath(self, attrPath: str, index: Incomplete | None = ...) -> str | None: ...
    def _getIncomingSceneOpAndLocation(self, port, graphState, transaction): ...
    def _getOpChain(self, interface): ...
    def _getStaticAttrHintsForIncomingSceneQuery(self, attrPath: str) -> dict: ...
    def _updateParameters(self, groupAttr, force: bool = ..., defaultAttr: Incomplete | None = ...): ...
    def addParameterHints(self, attrName, inputDict): ...
    def canOverride(self, attrName): ...
    def checkDynamicParameters(self, *args, **kwds): ...
    def findOverrideParameter(self, path, attrName, time, index: Incomplete | None = ..., editable: bool = ...): ...
    def getScenegraphLocation(self, frameTime: float = ...) -> str: ...
    def setInteractiveTransform(self, path, absScale, absRotate, absTranslate, time): ...
    def setInteractiveTransformFlag(self, path, time): ...
    def setOverride(self, locationPath, attrName, frameTime, attrData, index: Incomplete | None = ..., **kwargs): ...