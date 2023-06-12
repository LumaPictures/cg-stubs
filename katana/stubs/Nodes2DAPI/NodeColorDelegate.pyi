# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import NodegraphAPI as NodegraphAPI

_ColorLabels: dict
_PastelLabels: dict
_SHOW: str
_SPI: str
rules: list

class NodeColorDelegate(NodegraphAPI.NodeDelegateManager.SuperDelegate):
    def getPreferredNodeColor(self, nodeType, nodeName): ...
    def processNodeCreate(self, node): ...

def _GetColor(flavors): ...