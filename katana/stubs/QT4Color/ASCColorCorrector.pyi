# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyOpenColorIO as OCIO
import PyQt5.QtCore
import PyQt5.QtWidgets
import QT4FormWidgets as QT4FormWidgets
import PyQt5.QtCore as QtCore
import PyQt5.QtGui as QtGui
import PyQt5.QtWidgets as QtWidgets
from QT4Color.WidgetUtils import MiniLabelButton as MiniLabelButton, SetCompactWidgetWidth as SetCompactWidgetWidth, StripedFrame as StripedFrame
from _typeshed import Incomplete
from typing import ClassVar, Set, Tuple

class ColorGradeWidget(PyQt5.QtWidgets.QWidget):
    valueChanged: ClassVar[PyQt5.QtCore.pyqtSignal] = ...
    def __init__(self, parent, addTitle: bool = ..., title: str = ..., createChildrenInScroll: bool = ...) -> None: ...
    def _ColorGradeWidget__muteClicked_CB(self): ...
    def _ColorGradeWidget__resetClicked_CB(self): ...
    def _ColorGradeWidget__valuePolicy_CB(self, valuePolicyEvent): ...
    def emitChanged(self, final): ...
    def getCC(self, policyRoot: Incomplete | None = ...): ...
    def isMuted(self): ...
    def reset(self): ...
    def setCC(self, cc, emitValueChanged: bool = ...): ...
    def setMuted(self, isMuted): ...

class MonitorGammaWidget(PyQt5.QtWidgets.QWidget):
    valueChanged: ClassVar[PyQt5.QtCore.pyqtSignal] = ...
    def __init__(self, parent, addTitle: bool = ..., title: str = ...) -> None: ...
    def _MonitorGammaWidget__muteClicked_CB(self): ...
    def _MonitorGammaWidget__resetClicked_CB(self): ...
    def _MonitorGammaWidget__valuePolicy_CB(self, valuePolicyEvent): ...
    def emitChanged(self, final): ...
    def getValueDict(self, policyRoot: Incomplete | None = ...): ...
    def isMuted(self): ...
    def reset(self): ...
    def setMuted(self, isMuted): ...
    def setValueDict(self, d, emitValueChanged: bool = ...): ...
