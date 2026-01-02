import os
import sys

HERE = os.path.dirname(__file__)
sys.path.append(os.path.dirname(HERE))
from stubgen_pyside6 import helper

import PySide6

helper.set_pyside_version(6)


def test_enums() -> None:
    assert helper.is_flag(PySide6.QtCore.QDir.Filter) is True
    assert helper.is_flag_item(PySide6.QtCore.QDir.Filter.AllDirs) is True
    assert helper.is_flag_item_type(type(PySide6.QtCore.QDir.Filter.AllDirs)) is True
    assert helper.is_enum(PySide6.QtCore.QLocale.Language) is True
    assert helper.is_enum_item(PySide6.QtCore.QLocale.Language.Abkhazian) is True
