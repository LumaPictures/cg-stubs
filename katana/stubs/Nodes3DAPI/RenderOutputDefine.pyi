# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import ConditionalStateGrammar as ConditionalStateGrammar
import ConfigurationAPI_cmodule as Configuration
import Nodes3DAPI.DynamicParameterUtil as DynamicParameterUtil
import PyFnAttribute as FnAttribute
import PyFnGeolib as FnGeolib
import Nodes3DAPI.Node3D as Node3D
import NodegraphAPI as NodegraphAPI
import Nodes3DAPI_cmodule as Nodes3DAPI_cmodule
import PyXmlIO as PyXmlIO
import Utils as Utils
import PyXmlIO as XmlIO
from ConditionalStateGrammar.Parser import ParseCSG as ParseCSG
from Nodes3DAPI.GenericAssign import GenericAssign as GenericAssign
from _typeshed import Incomplete
from typing import ClassVar, Set, Tuple

_ExtraHints: dict
_Parameter_XML: str
_baseXML: None

class RenderOutputDefine(GenericAssign):
    _RenderOutputDefine__incomingCookKey: ClassVar[str] = ...
    __pychecker__: ClassVar[str] = ...
    def __init__(self) -> None: ...
    def _getIncomingSceneOpAndLocation(self, port: NodegraphAPI.Port, graphState: NodegraphAPI.GraphState, transaction): ...
    def _getOpChain(self, interface): ...
    def _updateParameters(self, groupAttr, force: bool = ..., defaultAttr: Incomplete | None = ...): ...
    def addParameterHints(self, attrName, inputDict): ...
    def checkDynamicParameters(self, *args, **kwds): ...
    def updateParameters(self, universalAttr: Incomplete | None = ..., buildParameters: bool = ...): ...
