# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

from NodegraphAPI.GroupStack import GroupStackNode as GroupStackNode
from NodegraphAPI_cmodule import node_registerPythonGroupType as node_registerPythonGroupType

_ExtraHints: dict

class InteractiveRenderFiltersNode(GroupStackNode):
    def __init__(self): ...
    def addParameterHints(self, attrName, inputDict): ...
    def getDisplayNameForChildNode(self, child): ...