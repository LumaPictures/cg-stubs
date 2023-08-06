# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import ConfigurationAPI_cmodule as Configuration
import PyFnAttribute as FnAttribute
import Nodes3DAPI.Node3D as Node3D
import NodegraphAPI as NodegraphAPI
from Nodes3DAPI.GenericAssign import GenericAssign as GenericAssign
from typing import ClassVar, Set, Tuple

_ParamHints: dict
_Parameter_XML: str
_baseXML: None

class CameraImagePlaneCreate(GenericAssign):
    _CameraImagePlaneCreate__parsedArgTree: ClassVar[None] = ...
    def __init__(self) -> None: ...
    def _filterAttrList(self, graphState: NodegraphAPI.GraphState, attrList): ...
    def _getIncomingSceneOpAndLocation(self, port: NodegraphAPI.Port, graphState: NodegraphAPI.GraphState, transaction): ...
    def addParameterHints(self, attrName, inputDict): ...
