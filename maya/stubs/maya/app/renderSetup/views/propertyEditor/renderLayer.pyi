from PySide6.QtWidgets import QGroupBox
from _typeshed import Incomplete
from maya.app.general.mayaMixin import MayaQWidgetBaseMixin as MayaQWidgetBaseMixin

class RenderLayer(MayaQWidgetBaseMixin, QGroupBox):
    item: Incomplete
    def __init__(self, item, parent) -> None: ...
