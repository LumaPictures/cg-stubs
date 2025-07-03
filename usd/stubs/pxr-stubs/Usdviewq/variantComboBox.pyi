from .common import Timer as Timer
from .qt import QtCore as QtCore, QtGui as QtGui, QtWidgets as QtWidgets
from _typeshed import Incomplete

class VariantComboBox(QtWidgets.QComboBox):
    prim: Incomplete
    variantSetName: Incomplete
    def __init__(self, parent, prim, variantSetName, mainWindow) -> None: ...
    def updateVariantSelection(self, index, timer) -> None: ...
