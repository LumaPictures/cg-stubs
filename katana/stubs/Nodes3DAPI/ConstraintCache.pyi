# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyFnAttribute as FnAttribute
import NodegraphAPI as NodegraphAPI
import PyXmlIO as PyXmlIO
import typing
from Nodes3DAPI.Node3D import Node3D as Node3D
from _typeshed import Incomplete
from typing import Set, Tuple

SCRIPT: str
SETUPSCRIPT: str
_ExtraHints: dict
_Parameter_XML: str

class ConstraintCache(Node3D):
    def __init__(self) -> None: ...
    def _ConstraintCache__getLocations(self, frameTime: int = ...): ...
    def _getOpChain(self, interface): ...
    def addParameterHints(self, attrName, inputDict): ...
    def clearCache(self): ...
    def fillCache(self, progressCallback: typing.Optional[typing.Callable] = ...): ...
