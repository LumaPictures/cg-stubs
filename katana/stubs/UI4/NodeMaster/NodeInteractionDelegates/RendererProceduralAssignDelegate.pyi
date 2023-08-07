# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import UI4.NodeMaster.NodeInteractionDelegateManager as NodeInteractionDelegateManager
import NodegraphAPI as NodegraphAPI
import UI4.NodeMaster.NodeInteractionDelegateManager
import Utils as Utils
from typing import ClassVar, Set, Tuple

class RendererProceduralAssignDelegate(UI4.NodeMaster.NodeInteractionDelegateManager.Delegate):
    _ValidItems: ClassVar[list] = ...
    _ValidNodes: ClassVar[list] = ...
    def _RendererProceduralAssignDelegate__droppedNode(self, targetNode, node: NodegraphAPI.Node): ...
    def _RendererProceduralAssignDelegate__droppedScenegraphItem(self, targetNode, item): ...
    def _RendererProceduralAssignDelegate__validNodeDrop(self, targetNode, event): ...
    def _RendererProceduralAssignDelegate__validScenegraphDrop(self, targetNode, event): ...
    def acceptsDrop(self, targetNode, event): ...
    def processDrop(self, targetNode, event): ...
