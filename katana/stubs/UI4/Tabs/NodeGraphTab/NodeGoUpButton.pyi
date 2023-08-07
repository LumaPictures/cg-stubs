# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import KatanaResources as KatanaResources
import NodegraphAPI as NodegraphAPI
import PyQt5.QtCore as QtCore
import PyQt5.QtGui as QtGui
import typing
from PyUtilModule.VirtualKatana import Widgets as Widgets
from UI4.Widgets.ToolbarButton import ToolbarButton
from _typeshed import Incomplete
from typing import ClassVar, Set, Tuple

class NodeGoUpButton(ToolbarButton):
    _NodeGoUpButton__pixmaps: ClassVar[dict] = ...
    def __init__(self, setCurrentNodeViewCallback: typing.Optional[typing.Callable] = ..., parent: Incomplete | None = ...) -> None: ...
    def _NodeGoUpButton__loadResources(self): ...
    def _NodeGoUpButton__on_clicked(self): ...
    def setCurrentNodeView(self, node: NodegraphAPI.Node): ...
