# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import CatalogAPI as CatalogAPI
import UI4.NodeMaster.NodeInteractionDelegateManager as NodeInteractionDelegateManager
import NodegraphAPI as NodegraphAPI
import PyQt5.QtWidgets as QtWidgets
import UI4 as UI4
import UI4.NodeMaster.NodeInteractionDelegateManager
import Utils as Utils
from typing import Set, Tuple

class FileInDelegate(UI4.NodeMaster.NodeInteractionDelegateManager.Delegate):
    def _FileInDelegate__dialogPrompt(self): ...
    def _FileInDelegate__validCatalogDrop(self, targetNode, event): ...
    def _FileInDelegate__validNodeDrop(self, targetNode, event): ...
    def acceptsDrop(self, targetNode, event): ...
    def processDrop(self, targetNode, event): ...
