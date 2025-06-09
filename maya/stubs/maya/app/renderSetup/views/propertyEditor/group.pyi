from maya.app.renderSetup.views.propertyEditor.collectionPropertyEditorStrings import *
from PySide6.QtWidgets import QGroupBox
from _typeshed import Incomplete
from maya.app.general.mayaMixin import MayaQWidgetBaseMixin as MayaQWidgetBaseMixin

vSpc: int
hSpc: int

class Group(MayaQWidgetBaseMixin, QGroupBox):
    PATH_LINEEDIT_TRANSPARENT_STYLESHEET: str
    item: Incomplete
    path: Incomplete
    treeView: Incomplete
    def __init__(self, item, parent) -> None: ...
    def paintEvent(self, event) -> None: ...
    def populateFields(self) -> None: ...
