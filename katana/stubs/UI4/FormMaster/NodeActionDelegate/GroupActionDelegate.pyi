# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import NodegraphAPI.LiveGroup as LiveGroup
import UI4.FormMaster.NodeActionDelegate.NodeActionDelegate as NodeActionDelegate
import UI4.Util.NodeGraphTab as NodeGraphTab
import NodegraphAPI as NodegraphAPI
import PyQt5.QtWidgets
import PyQt5.QtWidgets as QtWidgets
import Utils as Utils
from UI4.FormMaster.NodeActionDelegate.BaseNodeActionDelegate import BaseNodeActionDelegate as BaseNodeActionDelegate
from _typeshed import Incomplete
from typing import Set, Tuple

class GroupActionDelegate(BaseNodeActionDelegate):
    class _ConvertToLiveGroupAction(PyQt5.QtWidgets.QAction):
        def __init__(self, parent, node: NodegraphAPI.Node) -> None: ...
        def _ConvertToLiveGroupAction__triggered(self, checked): ...

    class _ShowUserParametersAtTopLevelAction(PyQt5.QtWidgets.QAction):
        def __init__(self, parent, node: NodegraphAPI.Node) -> None: ...
        def _ShowUserParametersAtTopLevelAction__triggered(self, checked): ...

    class _ToggleGroupNodeAppearanceAction(PyQt5.QtWidgets.QAction):
        def __init__(self, parent, node: NodegraphAPI.Node) -> None: ...
        def _ToggleGroupNodeAppearanceAction__triggered(self, checked): ...
    def addToContextMenu(self, menu, node: NodegraphAPI.Node): ...
    def addToWrenchMenu(self, menu, node: NodegraphAPI.Node, hints: Incomplete | None = ...): ...
