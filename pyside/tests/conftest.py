import sys

import pytest
from PySide2.QtWidgets import QApplication


@pytest.fixture(name="qapplication", scope="session", autouse=True)
def qapplication_fixture() -> QApplication:
    application = QApplication.instance()
    if application is None:
        application = QApplication(["-platform", "minimal"])

    return application


@pytest.fixture
def fix_import():
    if __builtins__['__import__'].__module__ == 'shibokensupport.__feature__':
        __builtins__['__import__'] = sys.modules[
            'PySide2.support.__feature__'
        ].original_import
