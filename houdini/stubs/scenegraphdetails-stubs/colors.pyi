from PySide6 import QtGui as QtGui

theBrushes: dict[str, QtGui.QBrush]

def getBrush(name: str) -> QtGui.QBrush: ...
