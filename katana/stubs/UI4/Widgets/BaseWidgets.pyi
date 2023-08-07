# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyQt5.QtWidgets
import PyQt5.QtWidgets as QtWidgets
from UI4.App.KeyboardShortcutManager.KeyboardShortcutManagerMixin import KeyboardShortcutManagerMixin as KeyboardShortcutManagerMixin, KeyboardShortcutManagerMixinMetaclass as KeyboardShortcutManagerMixinMetaclass
from typing import Set, Tuple

class BaseFrame(PyQt5.QtWidgets.QFrame, KeyboardShortcutManagerMixin): ...

class BaseMainWindow(PyQt5.QtWidgets.QMainWindow, KeyboardShortcutManagerMixin): ...

class BaseWidget(PyQt5.QtWidgets.QWidget, KeyboardShortcutManagerMixin): ...
