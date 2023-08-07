# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import AssetAPI as AssetAPI
import UI4.FormMaster.EnableableParameterPolicy as EnableableParameterPolicy
import UI4.FormMaster.HintsDelegate as HintsDelegate
import UI4.Util.ManipulatorManager as ManipulatorManager
import UI4.FormMaster.ParameterPolicy as ParameterPolicy
import PyQt5.QtCore
import QT4FormWidgets as QT4FormWidgets
import QT4FormWidgets.Conditional
import PyQt5.QtCore as QtCore
from UI4.FormMaster.NodeHints.Common2D import GetBoundsParamDict as GetBoundsParamDict
from typing import ClassVar, Set, Tuple

_NodeHints: dict

class ImageWriteExtensionOp(QT4FormWidgets.Conditional.ConditionalVisibilityOpBase):
    conditionalStateEval: ClassVar[PyQt5.QtCore.pyqtSignal] = ...
    def __init__(self, targetPolicy, hints, prefix) -> None: ...
    def _ImageWriteExtensionOp__operandChanged(self, state): ...
    def checkState(self): ...
    def freeze(self): ...
    def getValue(self, policyName): ...
    def thaw(self): ...
