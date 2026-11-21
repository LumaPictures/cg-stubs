import PySide6.QtWidgets

class Window:
    @staticmethod
    def __new__(cls: "type[Window]") -> PySide6.QtWidgets.QWidget: ...
