import PySide6.QtCore
import PySide6.QtWidgets
from hutil.PySide.QtCore import Qt as Qt
from hutil.PySide.QtGui import QPainter as QPainter, QStandardItem as QStandardItem
from hutil.PySide.QtWidgets import QSizePolicy as QSizePolicy

def createSectionAction(widget: PySide6.QtCore.QObject, label: str) -> PySide6.QtWidgets.QWidgetAction:
    """
    Custom implementation of a QMenu.addSection since addSection
    does not behave as intended + we want to format the section entries
    in a specific manner
    """
