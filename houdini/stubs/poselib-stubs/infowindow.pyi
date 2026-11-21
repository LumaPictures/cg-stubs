# Houdini stubs generated from Houdini 22.0.466

import PySide6.QtCore
from . import plglobals as plglobals
from collections.abc import Iterable, Mapping
from hutil.Qt import QtCore, QtWidgets
from typing import TypedDict

class _InfoSection(TypedDict):
    sectiontitle: str
    sectionicon: str
    sectioncontents: Mapping[str, object]

SECTION_TITLE: str
SECTION_ICON: str
SECTION_CONTENTS: str

class InfoWindow(QtWidgets.QDialog):
    """Window providing interface for displaying information organized into 
       sections, with additional functionality such as refreshing."""
    title: QtWidgets.QLabel
    reloadRequested: QtCore.Signal
    INFO_WINDOW_WIDTH: int
    ICON_WIDTH: int
    ICON_HEIGHT: int
    def __init__(self) -> None: ...
    def cleanup(self) -> None:
        """This is called when the library interface is about to be
           destroyed."""
    def bringToFocus(self) -> None:
        """Opens dialog if not already open, then brings it into focus."""
    def setPosition(self, global_point: PySide6.QtCore.QPoint) -> None:
        """Sets position of this window adjacent to provided point."""
    def setPersistent(self, persistent: bool) -> None:
        """Sets whether the window is persistent (i.e.: window has frame 
           and toolbar.)"""
    def setTitle(self, title: str) -> None: ...
    def loadJSON(self, json: Iterable[_InfoSection]) -> None:
        """Display information from given JSON of a predefined format."""
