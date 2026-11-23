from typing import TypedDict

from PySide6 import QtWidgets

from autorigs.modules.advancedFace.tongue.buildTongueGuide import TongueGuide
from autorigs.modules.advancedFace.tongue.tongueGuideModel import TongueGuideModel
from autorigs.modules.base.autoRigsBaseWidget import BaseOptionsWidget

# The tongue has no options: toJSON writes {} and fromJSON reads nothing.
class _TongueOptionsJson(TypedDict): ...

class ModuleOptionsWidget(BaseOptionsWidget[_TongueOptionsJson, TongueGuideModel]):
    buildguide: TongueGuide
    templateLabel: QtWidgets.QLabel
    def __init__(self, buildguide: TongueGuide, model: TongueGuideModel) -> None: ...
    def toJSON(self) -> _TongueOptionsJson: ...
    def fromJSON(self, json: _TongueOptionsJson) -> None: ...
