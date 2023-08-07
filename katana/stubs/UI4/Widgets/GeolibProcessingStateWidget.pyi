# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyQt5.QtWidgets
import PyQt5.QtCore as QtCore
import UI4.Widgets.StopButton
import Utils as Utils
from UI4.Widgets.StopButton import SimpleStopWidget as SimpleStopWidget
from typing import Set, Tuple

class GeolibProcessingStateWidget(UI4.Widgets.StopButton.SimpleStopWidget):
    def __init__(self, parent: PyQt5.QtWidgets.QWidget) -> None: ...
    def _GeolibProcessingStateWidget__stateChangedCallback(self, eventType: str | None, eventId, state: bool = ...): ...
    def _GeolibProcessingStateWidget__timerTick(self): ...
