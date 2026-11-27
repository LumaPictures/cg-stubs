from collections.abc import Callable, Mapping, MutableMapping
from typing import Any, TypeAlias, TypeVar, overload

import hou
import PySide6.QtCore
import PySide6.QtGui
import PySide6.QtWidgets


_MenuT = TypeVar("_MenuT", bound=PySide6.QtWidgets.QMenu)

_MenuActionKwargs: TypeAlias = hou._MenuActionKwargs

ICON_SIZE: int

class _MenuTitleLabel(PySide6.QtWidgets.QLabel):
    def __init__(self, text: str | None = ..., parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...

class MenuTitleItem(PySide6.QtWidgets.QWidgetAction):
    def __init__(self, text: str | None = ..., parent: PySide6.QtCore.QObject | None = ...) -> None: ...
    def text(self) -> str: ...
    def setText(self, text: str) -> None: ...

class XMLMenuParser:
    def __init__(
        self,
        context: str = ...,
        kwargs: Mapping[str, object] | None = ...,
        kwargsfunc: Callable[[], Mapping[str, object]] | None = ...,
        xmlfilename: str | None = ...,
        xmlstring: str | bytes | None = ...,
    ) -> None: ...
    def setHotkeyContext(self, hotkey_context: str) -> None: ...
    def hotkeyContext(self) -> str: ...
    def parseString(self, xmlstring: str | bytes) -> None: ...
    def parseFile(self, xmlfile: str) -> None: ...
    def parseFiles(self, xmlfilename: str) -> None: ...
    @overload
    def generateMenu(
        self,
        kwargs: MutableMapping[str, Any],
        menu: None = ...,
        actionitem_callback: Callable[[_MenuActionKwargs], object] | None = ...,
    ) -> PySide6.QtWidgets.QMenu: ...
    @overload
    def generateMenu(
        self,
        kwargs: MutableMapping[str, Any],
        menu: _MenuT,
        actionitem_callback: Callable[[_MenuActionKwargs], object] | None = ...,
    ) -> _MenuT: ...
    def handleKeyPress(
        self,
        keystring: str,
        kwargs: MutableMapping[str, Any],
        actionitem_callback: Callable[[_MenuActionKwargs], object] | None = ...,
        hotkey_context: str | None = ...,
    ) -> bool: ...

    class _MenuItem:
        def __init__(self, hotkey_context: str, attributes: Mapping[str, str] | None = ...) -> None: ...
        def addKwargs(self, kwargs: Mapping[str, object]) -> None: ...
        def items(self) -> list["XMLMenuParser._MenuItem"]: ...
        def handleKeyPress(
            self,
            keystring: str,
            kwargs: Mapping[str, object],
            actionitem_callback: Callable[[_MenuActionKwargs], object] | None,
            hotkey_context: str | None = ...,
        ) -> bool: ...
        def isVisible(self, kwargs: Mapping[str, object]) -> bool: ...
        def isEnabled(self, kwargs: Mapping[str, object]) -> bool: ...
        def label(self, kwargs: Mapping[str, object]) -> str: ...
        def icon(self, kwargs: Mapping[str, object]) -> PySide6.QtGui.QIcon | None: ...
        def action(self, kwargs: Mapping[str, object], label: str | None = ...) -> None: ...
        def symbol(self) -> str | None: ...

    class _ActionMenuItem(_MenuItem):
        def addQMenuItem(
            self, menu: PySide6.QtWidgets.QMenu, kwargs: Mapping[str, object], actionitem_callback: Callable[[_MenuActionKwargs], object] | None
        ) -> None: ...
        def handleKeyPress(
            self,
            keystring: str,
            kwargs: Mapping[str, object],
            actionitem_callback: Callable[[_MenuActionKwargs], object] | None,
            hotkey_context: str | None,
        ) -> bool: ...  # type: ignore[override]  # SideFX drops the base class's default

    class _ScriptMenuItem(_MenuItem):
        def addQMenuItem(
            self, menu: PySide6.QtWidgets.QMenu, kwargs: Mapping[str, object], actionitem_callback: Callable[[_MenuActionKwargs], object] | None
        ) -> None: ...

    class _ToggleMenuItem(_MenuItem):
        def __init__(self, hotkey_context: str, attributes: Mapping[str, str]) -> None: ...
        def addQMenuItem(
            self, menu: PySide6.QtWidgets.QMenu, kwargs: Mapping[str, object], actionitem_callback: Callable[[_MenuActionKwargs], object] | None
        ) -> None: ...

    class _SeparatorMenuItem(_MenuItem):
        def addQMenuItem(
            self, menu: PySide6.QtWidgets.QMenu, kwargs: Mapping[str, object], actionitem_callback: Callable[[_MenuActionKwargs], object] | None
        ) -> None: ...

    class _TitleMenuItem(_MenuItem):
        def addQMenuItem(
            self, menu: PySide6.QtWidgets.QMenu, kwargs: Mapping[str, object], actionitem_callback: Callable[[_MenuActionKwargs], object] | None
        ) -> None: ...

    class _SubMenuItem(_MenuItem):
        def addQMenuItem(
            self, menu: PySide6.QtWidgets.QMenu | None, kwargs: Mapping[str, object], actionitem_callback: Callable[[_MenuActionKwargs], object] | None
        ) -> PySide6.QtWidgets.QMenu: ...

    class _ScriptMenuStripDynamicMenuItem(_MenuItem):
        def addQMenuItem(
            self, menu: PySide6.QtWidgets.QMenu, kwargs: Mapping[str, object], actionitem_callback: Callable[[_MenuActionKwargs], object] | None
        ) -> None: ...

    class _RootMenuItem(_SubMenuItem):
        def addQMenuItem(
            self, menu: PySide6.QtWidgets.QMenu | None, kwargs: Mapping[str, object], actionitem_callback: Callable[[_MenuActionKwargs], object] | None
        ) -> PySide6.QtWidgets.QMenu: ...
