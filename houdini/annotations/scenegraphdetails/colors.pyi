from PySide6 import QtGui

theBrushes: dict[str, QtGui.QBrush]

def getBrush(name: str) -> QtGui.QBrush: ...
