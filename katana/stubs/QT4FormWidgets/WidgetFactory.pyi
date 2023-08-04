# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

from QT4FormWidgets.ArrayFormWidget import ArrayFormWidget as ArrayFormWidget
from QT4FormWidgets.CapsuleFormWidget import CapsuleFormWidget as CapsuleFormWidget
from QT4FormWidgets.CheckBoxFormWidget import CheckBoxFormWidget as CheckBoxFormWidget
from QT4FormWidgets.FormWidget import FormWidget as FormWidget
from QT4FormWidgets.GroupFormWidget import GroupFormWidget as GroupFormWidget
from QT4FormWidgets.MenuGroupFormWidget import MenuGroupFormWidget as MenuGroupFormWidget
from QT4FormWidgets.MultiFormWidget import MultiFormWidget as MultiFormWidget
from QT4FormWidgets.NullFormWidget import NullFormWidget as NullFormWidget
from QT4FormWidgets.NumberFormWidget import NumberFormWidget as NumberFormWidget
from QT4FormWidgets.PopupFormWidget import BooleanFormWidget as BooleanFormWidget, MappingPopupFormWidget as MappingPopupFormWidget, PopupFormWidget as PopupFormWidget
from QT4FormWidgets.StringFormWidget import StringFormWidget as StringFormWidget
from QT4FormWidgets.TabGroupFormWidget import TabGroupFormWidget as TabGroupFormWidget
from QT4FormWidgets.TextFormWidget import TextFormWidget as TextFormWidget
from typing import Set, Tuple

class WidgetFactory:
    def __init__(self) -> None: ...
    def _getWidgetClass(self, policy, hints): ...
    def buildWidget(self, parent, policy): ...
    def registerWidgetType(self, name, cls): ...

def GetDefaultWidgetFactory(): ...
