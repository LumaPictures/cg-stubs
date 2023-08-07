# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyFnAttribute as FnAttribute
import UI4.NodeMaster.NodeInteractionDelegateManager as NodeInteractionDelegateManager
import NodegraphAPI as NodegraphAPI
import UI4.NodeMaster.NodeInteractionDelegateManager
from typing import Set, Tuple

class AttributeEditorDelegate(UI4.NodeMaster.NodeInteractionDelegateManager.Delegate):
    def acceptsDrop(self, targetNode, event): ...
    def processDrop(self, targetNode, event): ...
