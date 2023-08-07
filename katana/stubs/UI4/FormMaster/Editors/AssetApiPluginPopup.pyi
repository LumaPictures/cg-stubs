# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import AssetAPI as AssetAPI
import PyQt5.QtWidgets
import QT4FormWidgets as QT4FormWidgets
import QT4FormWidgets.ValuePolicy
from QT4FormWidgets.PopupFormWidget import PopupFormWidget
from QT4FormWidgets.WidgetFactory import WidgetFactory
from typing import Set, Tuple

class AssetPluginPopupFormWidget(BaseAssetApiPluginPopupFormWidget):
    def __init__(self, parent: PyQt5.QtWidgets.QWidget, policy: QT4FormWidgets.ValuePolicy.AbstractValuePolicy, factory: WidgetFactory) -> None: ...

class BaseAssetApiPluginPopupFormWidget(PopupFormWidget):
    def __init__(self, pluginNames: list[str], parent: PyQt5.QtWidgets.QWidget, policy: QT4FormWidgets.ValuePolicy.AbstractValuePolicy, factory: WidgetFactory) -> None: ...

class FileSequencePluginPopupFormWidget(BaseAssetApiPluginPopupFormWidget):
    def __init__(self, parent: PyQt5.QtWidgets.QWidget, policy: QT4FormWidgets.ValuePolicy.AbstractValuePolicy, factory: WidgetFactory) -> None: ...
