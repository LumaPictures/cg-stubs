# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import UI4.NodeMaster.NodeInteractionDelegateManager as NodeInteractionDelegateManager
import UI4.NodeMaster.NodeInteractionDelegateManager
from typing import Set, Tuple

class GroupStackDelegate(UI4.NodeMaster.NodeInteractionDelegateManager.Delegate):
    def addToNodeSpecificShelfEnvironment(self, targetNode, editor, envDict): ...
