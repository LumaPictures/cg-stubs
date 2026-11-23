from collections.abc import Iterable, Mapping
from typing import TypedDict

import PySide6.QtCore
import PySide6.QtWidgets
from PySide6 import QtCore, QtWidgets

SECTION_TITLE: str
SECTION_ICON: str
SECTION_CONTENTS: str

# One section of the info window; SECTION_TITLE, SECTION_ICON and SECTION_CONTENTS are its keys.
class _InfoSection(TypedDict):
    sectiontitle: str
    sectionicon: str
    sectioncontents: Mapping[str, object]

class InfoWindow(PySide6.QtWidgets.QDialog):
    reloadRequested: QtCore.Signal
    INFO_WINDOW_WIDTH: int
    ICON_WIDTH: int
    ICON_HEIGHT: int
    title: QtWidgets.QLabel
    def __init__(self) -> None: ...
    def cleanup(self) -> None: ...
    def bringToFocus(self) -> None: ...
    def setPosition(self, global_point: PySide6.QtCore.QPoint) -> None: ...
    def setPersistent(self, persistent: bool) -> None: ...
    def setTitle(self, title: str) -> None: ...
    def loadJSON(self, json: Iterable[_InfoSection]) -> None: ...
