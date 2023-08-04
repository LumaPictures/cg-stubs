# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyQt5.QtCore as QtCore
import PyQt5.QtGui as QtGui
from typing import Set, Tuple

class GroupGuard:
    def __init__(self, settings, name) -> None: ...
    def __enter__(self): ...
    def __exit__(self, excType, excValue, tb): ...

def RestoreGeometry(settings, widget, groupName: str = ...): ...
def SaveGeometry(settings, widget, groupName: str = ...): ...
