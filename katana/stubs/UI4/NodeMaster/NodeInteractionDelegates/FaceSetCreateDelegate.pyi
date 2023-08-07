# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import UI4.NodeMaster.NodeInteractionDelegateManager as NodeInteractionDelegateManager
import UI4.NodeMaster.NodeInteractionDelegateManager
import Utils as Utils
from typing import Set, Tuple

class FaceSetCreateDelegate(UI4.NodeMaster.NodeInteractionDelegateManager.Delegate):
    def acceptsDrop(self, targetNode, event): ...
    def processDrop(self, targetNode, event): ...
