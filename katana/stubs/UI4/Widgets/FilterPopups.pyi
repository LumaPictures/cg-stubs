# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import AssetAPI as AssetAPI
import PyFnGeolibProducers as FnGeolibProducers
import QT4FormWidgets as QT4FormWidgets
import QT4Widgets as QT4Widgets
import PyQt5.QtWidgets as QtWidgets
import RenderingAPI as RenderingAPI
import Utils as Utils
from QT4FormWidgets.FilterablePopupFormWidget.FilterablePopupFormWidget import Popup
from QT4Widgets.MenuButton import MenuButton as MenuButton
from _typeshed import Incomplete
from typing import ClassVar, Set, Tuple

class LookFileMaterialFilterPopup(Popup):
    def __init__(self, *args) -> None: ...
    def _LookFileMaterialFilterPopup__assetValueChangedEvent(self, *args): ...
    def _LookFileMaterialFilterPopup__cachesFlushed(self, *args, **kwargs): ...
    def _refreshContents(self): ...

class ShaderFilterPopup(Popup):
    _ShaderFilterPopup__TAILPAT: ClassVar[builtin_function_or_method] = ...
    def __init__(self, valuePolicy, parent: Incomplete | None = ...) -> None: ...
    @staticmethod
    def _ShaderFilterPopup__getKey(o): ...
    def _ShaderFilterPopup__locationFilterCallback(self, state, name, meta): ...
    def _ShaderFilterPopup__reloadShaders(self): ...
    def _ShaderFilterPopup__shadersReloaded(self, args): ...
    def _refreshContents(self): ...
    def _shouldIncludeShader(self, name, location): ...

class ShaderTypeFilterPopup(Popup):
    def __init__(self, *args) -> None: ...
    def _getShaderTypesXML(self): ...
    def _refreshContents(self): ...
