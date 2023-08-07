# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PluginSystemAPI as PluginSystemAPI
import QT4FormWidgets as QT4FormWidgets
import PyQt5.QtCore as QtCore
import Utils as Utils
from QT4FormWidgets.FilterablePopupFormWidget import FilterablePopupFormWidget
from QT4FormWidgets.FilterablePopupFormWidget.FilterablePopupFormWidget import Popup, PopupButton
from typing import Set, Tuple

class PluginPopupFormWidget(FilterablePopupFormWidget):
    class PluginPopup(Popup):
        def __init__(self, *args) -> None: ...
        def _PluginPopup__cachesFlushed(self, *args, **kwargs): ...
        def _refreshContents(self): ...

    class PluginPopupButton(PopupButton):
        def __init__(self, valuePolicy) -> None: ...
        def _buildPopupWindow(self): ...
        def sizeHint(self): ...
    def _buildLabel(self, labelText, pos: int = ...): ...
    def _buildPopupButton(self): ...
