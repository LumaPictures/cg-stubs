import os
import sys

HERE = os.path.dirname(__file__)
sys.path.append(os.path.dirname(HERE))
import PySide2
from stubgen_pyside import helper

helper.set_pyside_version(2)


def test_enums() -> None:
    assert helper.is_flag(PySide2.QtCore.QDir.Filter) is True
    assert helper.is_flag_item(PySide2.QtCore.QDir.Filter.AllDirs) is True
    assert helper.is_flag_item_type(type(PySide2.QtCore.QDir.Filter.AllDirs)) is True
    assert helper.is_enum(PySide2.QtCore.QLocale.Language) is True
    assert helper.is_enum_item(PySide2.QtCore.QLocale.Language.Abkhazian) is True
