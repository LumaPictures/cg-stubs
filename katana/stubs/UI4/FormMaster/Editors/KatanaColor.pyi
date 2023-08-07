# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import AssetAPI as AssetAPI
import PyOpenColorIO as OCIO
import QT4Color as QT4Color
import QT4FormWidgets as QT4FormWidgets
import UI4 as UI4
import Utils as Utils
from QT4Color.ColorFormWidget import ColorFormWidget
from QT4FormWidgets.PopupFormWidget import PopupFormWidget
from typing import Set, Tuple

class ColorspacePopup(PopupFormWidget):
    def __init__(self, parent, policy, factory) -> None: ...
    def _ColorspacePopup__updateInfo(self): ...
    def _ColorspacePopup__valueChanged(self, event): ...
    def _freeze(self): ...
    def _thaw(self): ...

class KatanaColorFormWidget(ColorFormWidget):
    def __init__(self, parent, policy, factory) -> None: ...
    def _KatanaColorFormWidget__probeResult_CB(self, probeInfo): ...
    def _buildAdditionalControlWidgets(self, layout): ...
    def colorChange(self, color): ...
    def execColorPicker(self): ...
    def setColor_RGBA(self, color, final: bool = ...): ...
