# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyFnGeolibServices as FnGeolibServices
import KatanaResources as KatanaResources
import NodegraphAPI as NodegraphAPI
import Utils as Utils
from _typeshed import Incomplete

gCachedGenericAssignArgs: dict
gGenericAssignNodeTypes: dict

def GetGenericAssignFiles() -> list[None]: ...
def GetGenericAssignNodeTypes() -> dict: ...
def InitGenericAssignNodeTypes(searchPaths: Incomplete | None = ...): ...
def RegisterGenericAssignNodeTypes(searchPaths: Incomplete | None = ...): ...
def SearchForGenericAssignNodeTypes(searchPaths: list[str]): ...
def __CreateGenericAssignNode(nodeTypeName): ...
def __GetParsedGenericAssignArgsAttr(nodeTypeName): ...