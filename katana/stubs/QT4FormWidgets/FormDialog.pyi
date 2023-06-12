# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyQt5.QtWidgets
import QT4FormWidgets.WidgetFactory as WidgetFactory
from QT4FormWidgets.PythonValuePolicy import PythonDictValuePolicy as PythonDictValuePolicy
from _typeshed import Incomplete
from typing import ClassVar

class FormDialog(PyQt5.QtWidgets.QDialog):
    _DefaultRootHints: ClassVar[dict] = ...
    def __init__(self, dataSource, parent: Incomplete | None = ..., factory: Incomplete | None = ..., title: Incomplete | None = ..., okLabel: str = ..., cancelLabel: str = ...): ...
    def getValuePolicy(self): ...