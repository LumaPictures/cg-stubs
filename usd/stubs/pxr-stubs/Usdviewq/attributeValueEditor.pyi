from .attributeValueEditorUI import Ui_AttributeValueEditor as Ui_AttributeValueEditor
from .common import GetPropertyColor as GetPropertyColor, UIPropertyValueSourceColors as UIPropertyValueSourceColors
from .qt import QtCore as QtCore, QtWidgets as QtWidgets
from .scalarTypes import ToString as ToString
from _typeshed import Incomplete
from pxr import Usd as Usd

class AttributeValueEditor(QtWidgets.QWidget):
    editComplete: Incomplete
    _ui: Incomplete
    _defaultView: Incomplete
    _extraAttrViews: Incomplete
    def __init__(self, parent) -> None: ...
    _appController: Incomplete
    def setAppController(self, appController) -> None: ...
    _primPath: Incomplete
    _attribute: Incomplete
    _isSet: bool
    def populate(self, primPath, propName) -> None: ...
    def _FindView(self, attr): ...
    _val: Incomplete
    def refresh(self) -> None: ...
    def clear(self) -> None: ...
