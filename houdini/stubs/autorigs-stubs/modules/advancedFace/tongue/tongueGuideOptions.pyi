# Houdini stubs generated from Houdini 22.0.466

from _typeshed import Incomplete
from autorigs.modules.advancedFace.tongue.buildTongueGuide import TongueGuide as TongueGuide
from autorigs.modules.advancedFace.tongue.tongueGuideModel import TongueGuideModel as TongueGuideModel
from autorigs.modules.base.autoRigsBaseWidget import BaseOptionsWidget as BaseOptionsWidget
from autorigs.modules.geometry import geometryGuideOptions as geometryGuideOptions
from hutil.Qt import QtWidgets
from typing import TypedDict

class _TongueOptionsJson(TypedDict): ...

class ModuleOptionsWidget(BaseOptionsWidget[_TongueOptionsJson, TongueGuideModel]):
    buildguide: TongueGuide
    templateLabel: QtWidgets.QLabel
    model: Incomplete
    def __init__(self, buildguide: TongueGuide, model: TongueGuideModel) -> None: ...
    def toJSON(self) -> _TongueOptionsJson: ...
    def fromJSON(self, json: _TongueOptionsJson) -> None: ...
