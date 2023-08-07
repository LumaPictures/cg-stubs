# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyFnAttribute as FnAttribute
import PyFnGeolib as FnGeolib
import NodegraphAPI as NodegraphAPI
import Nodes3DAPI as Nodes3DAPI
import PyQt5.QtCore as QtCore
import Nodes3DAPI.ScenegraphManager as ScenegraphManager
import typing
from UI4.Widgets.ModalProcessInterruptWidget import ModalProcessInterruptWidget as ModalProcessInterruptWidget
from _typeshed import Incomplete
from typing import Set, Tuple

class CollectAndSelectInScenegraph:
    def __init__(self, cel, loc) -> None: ...
    def _CollectAndSelectInScenegraph__collectionInterruptCallback(self, numFound, t): ...
    def _CollectAndSelectInScenegraph__setInterrupt(self): ...
    def collectAndSelect(self, select: bool = ..., replace: bool = ..., node: typing.Optional[NodegraphAPI.Node] = ...): ...
