# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import NodegraphAPI.Version.Utils as Utils
from typing import Set, Tuple

VERSION_SCRIPT_TYPE_XML: int
VERSION_SCRIPT_TYPE_XMLIO: int

def GetCurrentNodeTypeVersion(nodeTypeName): ...
def GetFcnStack(oldVersion, currentVersion): ...
def GetNodeTypeVersionUpdateFunctions(nodeTypeName, nodeTypeVersionToUpdate): ...
def HasAnyNodeTypeVersionUpdateFunctions(): ...
def RegisterVersionScript(versionTag, fcn, scriptType): ...
def SetCurrentNodeTypeVersion(nodeTypeName, currentNodeTypeVersion): ...
def SetNodeTypeVersionUpdateFunction(nodeTypeName, nodeTypeVersion, fnc): ...
