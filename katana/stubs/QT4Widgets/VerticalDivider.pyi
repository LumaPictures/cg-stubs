# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyQt5.QtWidgets

class VerticalDivider(PyQt5.QtWidgets.QFrame):
    def __init__(self, *args): ...
    def paintEvent(self, event): ...