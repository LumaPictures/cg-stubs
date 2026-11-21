from typing import Any

import PySide6.QtWidgets
from _pdgd import DataLayerServer

class ServerList(PySide6.QtWidgets.QWidget):
    group_box: PySide6.QtWidgets.QGroupBox | None
    # Never filled.
    active_server_entries: list[Any]
    def __init__(self, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...
    def refresh(self) -> None: ...
    def stop_server(self, server: DataLayerServer) -> None: ...
