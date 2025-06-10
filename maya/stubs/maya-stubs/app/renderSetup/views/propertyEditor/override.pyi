from maya.app.renderSetup.views.propertyEditor.overridePropertyEditorStrings import *
from PySide6.QtWidgets import QGroupBox
from _typeshed import Incomplete
from maya.app.general.mayaMixin import MayaQWidgetBaseMixin as MayaQWidgetBaseMixin
from maya.app.renderSetup.common.utils import ReportableException as ReportableException
from maya.app.renderSetup.views.propertyEditor.layout import Layout as Layout

class Override(MayaQWidgetBaseMixin, QGroupBox):
    path: Incomplete
    attributeUI: Incomplete
    item: Incomplete
    target: Incomplete
    def __init__(self, item, parent) -> None: ...
    def update(self) -> None: ...
    def paintEvent(self, event) -> None: ...
