# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import UI4.NodeMaster.NodeInteractionDelegateManager as NodeInteractionDelegateManager
import PyQt5.QtCore as QtCore
import UI4.NodeMaster.NodeInteractionDelegateManager
import Utils as Utils
from typing import Set, Tuple

class PruneDelegate(UI4.NodeMaster.NodeInteractionDelegateManager.Delegate):
    def _PruneDelegate__appendScenegraphLocations(self, targetNode, locations): ...
    def _PruneDelegate__replaceScenegraphLocations(self, targetNode, locations): ...
    def _PruneDelegate__validScenegraphDrop(self, targetNode, event): ...
    def acceptsDrop(self, targetNode, event): ...
    def processDrop(self, targetNode, event): ...
