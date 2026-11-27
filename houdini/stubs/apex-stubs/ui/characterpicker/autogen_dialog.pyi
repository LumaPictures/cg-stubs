import PySide6.QtWidgets
from .utils import sceneViewer as sceneViewer
from apex.characterpicker.commands import ControlsFilter as ControlsFilter, ProjectionDirection as ProjectionDirection
from apex.ui.characterpicker.panel import ApexCharacterPicker as ApexCharacterPicker
from hutil.PySide import QtWidgets

class AutogenLayoutDialog(QtWidgets.QDialog):
    def __init__(self, picker: ApexCharacterPicker, parent: PySide6.QtWidgets.QWidget | None = None) -> None: ...
