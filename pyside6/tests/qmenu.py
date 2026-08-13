from typing import Any

from PySide6.QtWidgets import QMenu, QTreeWidget

# PySide2 exposed only exec_(), because `exec` was a keyword in Python 2.
# PySide6 has a real exec() method: this checks that the stubs agree it exists,
# including when reached through an annotated member.
# Note: this module is not collected by pytest (its name has no test_ prefix),
# so it is a static assertion only -- the runtime check is
# test_general.py::test_qmenu_exec.


class Toto(QTreeWidget):
    m: QMenu

    def __init__(self, *args: Any) -> None:
        super().__init__(*args)
        self.m = QMenu()

    def toto(self) -> None:
        # never called: exec() blocks until the menu is dismissed
        self.m.exec()
