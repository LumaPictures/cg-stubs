# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyFnAttribute as FnAttribute
import NodegraphAPI as NodegraphAPI
import PyXmlIO as PyXmlIO
import Naming as UniqueName
import Utils as Utils
import re
from Nodes3DAPI.Node3D import Node3D as Node3D
from _typeshed import Incomplete
from typing import ClassVar

_ExtraHints: dict
_Parameter_XML: str
_global_ForkDict: dict

class ForkNode3D(Node3D):
    _ForkNode3D__forkVarRegex: ClassVar[re.Pattern] = ...
    def __init__(self): ...
    def _ForkNode3D__renumberOutputPorts(self): ...
    def _ForkNode3D__renumberOutputVariables(self): ...
    def _getOp(self, port, graphState, visitedState, transaction): ...
    def addForkOutput(self): ...
    def addForkVariable(self, name, isString): ...
    def addParameterHints(self, attrName, inputDict): ...
    def deleteForkOutput(self, index): ...
    def deleteForkVariable(self, name): ...
    def renameForkVariable(self, oldName, newName): ...
    def reorderForkOutputVariables(self, oldPos, newPos): ...

def GetForkDictHash(): ...
def __nodegraphExpression_GetForkIndex(nodeParamRef): ...
def __nodegraphExpression_GetForkVar(nodeParamRef, varName, default: Incomplete | None = ...): ...