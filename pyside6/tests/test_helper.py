import os
import sys

HERE = os.path.dirname(__file__)
sys.path.append(os.path.dirname(HERE))
from stubgen_pyside6 import helper

from PySide6 import QtCore

helper.set_pyside_version(6)


def test_enums() -> None:
    assert helper.is_flag(QtCore.QDir.Filter) is True
    assert helper.is_flag_item(QtCore.QDir.Filter.AllDirs) is True
    assert helper.is_flag_item_type(type(QtCore.QDir.Filter.AllDirs)) is True
    assert helper.is_enum(QtCore.QLocale.Language) is True
    assert helper.is_enum_item(QtCore.QLocale.Language.Abkhazian) is True
