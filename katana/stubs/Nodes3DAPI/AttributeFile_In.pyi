# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import NodegraphAPI.Constants.ApplyWhenOptions as ApplyWhenOptions
import AssetAPI as AssetAPI
import ConditionalStateGrammar as ConditionalStateGrammar
import PyFnAttribute as FnAttribute
import PyFnGeolibServices as FnGeolibServices
import NodegraphAPI as NodegraphAPI
from ConditionalStateGrammar.Parser import ParseCSG as ParseCSG
from Nodes3DAPI.Node3D import Node3D as Node3D
from Nodes3DAPI.TimingUtils import GetModifiedFrameTime as GetModifiedFrameTime, GetTimingParameterHints as GetTimingParameterHints, GetTimingParameterXML as GetTimingParameterXML
from typing import Set, Tuple

_ParamHints: dict
_Parameter_XML: str

class AttributeFile_In(Node3D):
    def __init__(self) -> None: ...
    def _getOpChain(self, interface): ...
    def addParameterHints(self, attrName, inputDict): ...
