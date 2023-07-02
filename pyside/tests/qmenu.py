from typing import Any
from PySide2.QtWidgets import QMenu, QTreeWidget

# FIXME: this test does not execute at runtime
# the default version of pyside2 stubs would not detect missing attributes
# this test verifies that this is fixed


class Toto(QTreeWidget):
    m: QMenu

    def __init__(self, *args: Any) -> None:
        super().__init__(*args)
        self.m = QMenu()

    def toto(self) -> None:
        try:
            # exec() is actually not available
            self.m.exec()  # type: ignore[attr-defined]
            assert False, "Should not reach here"
        except AttributeError:
            pass
