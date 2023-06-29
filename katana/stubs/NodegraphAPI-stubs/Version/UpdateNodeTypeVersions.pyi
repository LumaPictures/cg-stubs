# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import NodegraphAPI.Xio as Xio
from NodegraphAPI.Version.Registry import GetNodeTypeVersionUpdateFunctions as GetNodeTypeVersionUpdateFunctions

def UpdateNodeTypeVersions(document): ...
def WillUpdateNodeTypeVersions(document): ...