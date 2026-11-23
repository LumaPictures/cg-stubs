import types
from typing import NoReturn

__version__: str
QT_VERBOSE: bool
QT_PREFERRED_BINDING: str
QT_SIP_API_HINT: str | None
Qt: types.ModuleType
long = int

class MissingMember:
    """
    A placeholder type for a missing Qt object not
    included in Qt.py

    Args:
        name (str): The name of the missing type
        details (str): An optional custom error message
    """
    ERR_TMPL: str
    def __init__(self, name: str, details: str = '') -> None: ...
    def __getattr__(self, name: str) -> NoReturn: ...
    def __call__(self, *a: object, **kw: object) -> NoReturn: ...

# Created at runtime by Qt.py.
from PySide6 import QtCore as QtCore
from PySide6 import QtGui as QtGui
from PySide6 import QtHelp as QtHelp
from PySide6 import QtMultimedia as QtMultimedia
from PySide6 import QtNetwork as QtNetwork
from PySide6 import QtOpenGL as QtOpenGL
from PySide6 import QtPrintSupport as QtPrintSupport
from PySide6 import QtSql as QtSql
from PySide6 import QtSvg as QtSvg
from PySide6 import QtTest as QtTest
from PySide6 import QtUiTools as QtUiTools
from PySide6 import QtWebEngineWidgets as QtWebEngineWidgets
from PySide6 import QtWidgets as QtWidgets
from PySide6 import QtXml as QtXml
