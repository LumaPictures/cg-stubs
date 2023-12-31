# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import NodegraphAPI.Constants.ApplyWhenOptions as ApplyWhenOptions
import NodegraphAPI.Constants.ApplyWhereOptions as ApplyWhereOptions
import ConditionalStateGrammar as ConditionalStateGrammar
import NodegraphAPI.Constants.ExecutionModeOptions as ExecutionModeOptions
import PyFnAttribute as FnAttribute
import PyFnGeolib as FnGeolib
import PyFnGeolibServices as FnGeolibServices
import NodegraphAPI as NodegraphAPI
import PyFnAttribute
import PyXmlIO as PyXmlIO
import Utils as Utils
from ConditionalStateGrammar.Parser import ParseCSG as ParseCSG
from Nodes3DAPI.Node3D import Node3D as Node3D
from typing import ClassVar, Set, Tuple

_ExtraHints: dict

class GenericOp(Node3D):
    def __init__(self) -> None: ...
    def _getOpChain(self, interface): ...
    def addParameterHints(self, attrName, inputDict): ...
    def buildArgsParametersFromAttr(self, attr): ...
    def updateArgsParametersFromAttr(self, groupAttr: PyFnAttribute.GroupAttribute): ...

class _ParamUpdater:
    intHint: ClassVar[str] = ...
    metaPrefix: ClassVar[str] = ...
    typeTable: ClassVar[dict] = ...
    @classmethod
    def _ParamUpdater__deleteParam(cls, parentParam: NodegraphAPI.Parameter, childParam: NodegraphAPI.Parameter): ...
    @classmethod
    def _ensureParamForAttr(cls, parentParam: NodegraphAPI.Parameter, name: str, attr: PyFnAttribute.GroupAttribute) -> NodegraphAPI.Parameter: ...
    @classmethod
    def _setParamValue(cls, parentParam: NodegraphAPI.Parameter, childParam: NodegraphAPI.Parameter, attr: PyFnAttribute.GroupAttribute): ...
    @classmethod
    def clean(cls, parentParam: NodegraphAPI.Parameter, groupAttr: PyFnAttribute.GroupAttribute): ...
    @classmethod
    def update(cls, parentParam: NodegraphAPI.Parameter, groupAttr: PyFnAttribute.GroupAttribute): ...

def _DoInputRequests(interface, inputBehavior, inputPorts, graphState: NodegraphAPI.GraphState): ...
