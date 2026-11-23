from PySide6 import QtCore

theCustomMimeType: str
theCustomFileMimeType: str

def getFilePathsFromMimeData(data: QtCore.QMimeData) -> list[str]: ...
