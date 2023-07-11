# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyQt5.QtCore as QtCore
import PyQt5.QtGui as QtGui
from typing import Set, Tuple

GEOMETRY_GROUP_NAME: str
GEOMETRY_POS_NAME: str
GEOMETRY_SIZE_NAME: str

class GroupGuard:
    def __init__(self, settings, name): ...
    def __enter__(self): ...
    def __exit__(self, excType, excValue, tb): ...

def RestoreGeometry(settings, widget, groupName: str = ...): ...
def SaveGeometry(settings, widget, groupName: str = ...): ...
