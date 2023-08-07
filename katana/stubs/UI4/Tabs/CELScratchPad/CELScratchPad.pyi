# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyQt5.QtWidgets
import QT4FormWidgets as QT4FormWidgets
import PyQt5.QtGui as QtGui
import PyQt5.QtWidgets as QtWidgets
import UI4 as UI4
from UI4.Tabs.BaseTab import BaseTab as BaseTab
from typing import Set, Tuple

_HelpText: str

class CELPanel(PyQt5.QtWidgets.QScrollArea):
    def __init__(self, parent) -> None: ...

class CELTab(BaseTab):
    def __init__(self, parent) -> None: ...
