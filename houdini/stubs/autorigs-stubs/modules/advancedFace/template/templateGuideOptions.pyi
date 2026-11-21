# Houdini stubs generated from Houdini 22.0.466

from autorigs.modules.advancedFace.template.buildTemplateGuide import TemplateGuide as TemplateGuide
from autorigs.modules.advancedFace.template.templateGuideModel import TemplateGuideModel as TemplateGuideModel
from autorigs.modules.base.autoRigsBaseWidget import BaseOptionsWidget as BaseOptionsWidget
from hutil.Qt import QtWidgets
from typing import TypedDict

class _TemplateLinkJson(TypedDict):
    enabled: bool
    toggled: bool

class _TemplateOptionsJson(TypedDict):
    link: _TemplateLinkJson

class ModuleOptionsWidget(BaseOptionsWidget[_TemplateOptionsJson, TemplateGuideModel]):
    buildguide: TemplateGuide
    templateLabel: QtWidgets.QLabel
    unlink_toggle: QtWidgets.QCheckBox
    def __init__(self, buildguide: TemplateGuide, model: TemplateGuideModel) -> None: ...
    def fromJSON(self, json: _TemplateOptionsJson) -> None: ...
    def toJSON(self) -> _TemplateOptionsJson: ...
    def setLinkEnabled(self, toggle: bool) -> None: ...
    def updateLinkToggled(self) -> None: ...
