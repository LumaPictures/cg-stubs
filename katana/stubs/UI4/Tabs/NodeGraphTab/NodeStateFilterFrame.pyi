# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import UI4.Util.IconManager as IconManager
import UI4.KatanaPrefs.PrefNames as PrefNames
import PyQt5.QtWidgets
import PyQt5.QtCore as QtCore
import PyQt5.QtWidgets as QtWidgets
import Utils as Utils
from UI4.KatanaPrefs.KatanaPrefsObject import KatanaPrefs as KatanaPrefs
from UI4.Widgets.ToolbarButton import ToolbarButton as ToolbarButton
from typing import ClassVar, Set, Tuple

class NodeStateFilterFrame(PyQt5.QtWidgets.QFrame):
    def __init__(self, parent) -> None: ...
    def _NodeStateFilterFrame__onNodeViewChanged(self, _prevViewNode, currViewNode): ...
    def _NodeStateFilterFrame__onShowHideFilters(self): ...

class _ToggleFrame(PyQt5.QtWidgets.QFrame):
    class _ToggleFrame__Toggle(tuple):
        _field_defaults: ClassVar[dict] = ...
        _fields: ClassVar[tuple] = ...
        _fields_defaults: ClassVar[dict] = ...
        def __init__(self, _cls, name, label) -> None: ...
        def _asdict(self): ...
        @classmethod
        def _make(cls, iterable): ...
        def _replace(self, _self, **kwds): ...
        def __getnewargs__(self): ...
        @property
        def label(self): ...
        @property
        def name(self): ...
    _ToggleFrame__buttonStyle: ClassVar[str] = ...
    _ToggleFrame__togglesByPref: ClassVar[dict] = ...
    def __init__(self, parent) -> None: ...
    @staticmethod
    def _ToggleFrame__onButtonClicked(button): ...
    def _ToggleFrame__onPrefChanged(self, _eventType, _eventID, prefKey, prefValue): ...
