from collections.abc import Callable as Callable
from hutil.Qt import QtWidgets

class ConnectDialog(QtWidgets.QDialog):
    """
        Display remote connection options
    """
    callback: Callable[[str, str], object]
    address: str
    layout: QtWidgets.QVBoxLayout
    interface_types: dict[str, str]
    selected_type_label: str | None
    def __init__(self, callback: Callable[[str, str], object], parent: QtWidgets.QWidget | None = None) -> None: ...
    def interfaceTypeChanged(self, interface_type: str) -> None: ...
    def connect(self) -> None: ...
    def addressChanged(self, address: str) -> None: ...
