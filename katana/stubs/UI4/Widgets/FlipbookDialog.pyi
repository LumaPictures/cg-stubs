# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyUtilModule.ChildProcess as ChildProcess
import ConfigurationAPI_cmodule as Configuration
import NodegraphAPI as NodegraphAPI
import Nodes2DAPI as Nodes2DAPI
import PyQt5.QtWidgets
import QT4Widgets as QT4Widgets
import PyQt5.QtWidgets as QtWidgets
import UI4 as UI4
import Utils as Utils
from typing import ClassVar, Set, Tuple

class FlipbookDialog(PyQt5.QtWidgets.QDialog):
    _dialogList: ClassVar[list] = ...
    def __init__(self, flipbookArguments, *args) -> None: ...
    def _FlipbookDialog__cancelRender(self): ...
    def _FlipbookDialog__idle_callback(self, eventType, eventID, **args): ...
    def _FlipbookDialog__render_flipbook(self): ...
    def _FlipbookDialog__viewerHandler_checkForFirstFrame(self): ...
    def _FlipbookDialog__viewerHandler_connectToItview(self): ...
    def _FlipbookDialog__viewerHandler_loadRemainingSequence(self): ...
    def closeEvent(self, event): ...