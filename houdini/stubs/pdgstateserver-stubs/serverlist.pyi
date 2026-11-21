import PySide6.QtWidgets
from _pdgd import DataLayerServer as DataLayerServer
from hutil.Qt import QtWidgets
from typing import Any

class ServerList(QtWidgets.QWidget):
    """ Lists active servers and allows shutting them down """
    group_box: PySide6.QtWidgets.QGroupBox | None
    active_server_entries: list[Any]
    def __init__(self, parent: PySide6.QtWidgets.QWidget | None = None) -> None: ...
    def refresh(self) -> None: ...
    def stop_server(self, server: DataLayerServer) -> None: ...
