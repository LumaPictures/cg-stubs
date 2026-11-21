from . import cpglobals as cpglobals
from .controlbutton import ControlButton as ControlButton
from .shaperegistry import ShapeDefinition as ShapeDefinition
from hutil.PySide import QtWidgets

class ControlButtonMenu(QtWidgets.QMenu):
    """Persistent RMB menu for a control button.

    `setOwnerButton()` should be called to update the menu's dynamic state
    before each show.
    """
    def __init__(self, edit_mode: bool, shapes: list[ShapeDefinition]) -> None: ...
    def hasContent(self) -> bool: ...
    def setOwnerButton(self, owner_button: ControlButton, edit_paths_text: str = '') -> None: ...
