# Houdini stubs generated from Houdini 22.0.466

from hutil.Qt.QtCore import *
from hutil.Qt.QtGui import *
from hutil.Qt.QtWidgets import *
from PySide6 import QtCore as QtCore, QtWidgets as QtWidgets
from collections.abc import Sequence
from typing import Any, NoReturn

APP_VERSION: str
SETTINGS_FILE: str
HOUDINI_ENV: str
LOCAL_ZIPS: list[str]
LOCAL_TOOLSET_ZIP: str | None
LOCAL_TOOLSET_VERSION: str | None
HOU_TEMP_PATH: str

def get_launcher_bin_file_path(launcher_path: str) -> str: ...

class LauncherDialog(QDialog):
    settings: QtCore.QSettings
    path_label: QtWidgets.QLabel
    launcher_path_lineedit: QtWidgets.QLineEdit
    url_label: QtWidgets.QLabel
    launch_button: QtWidgets.QPushButton
    cancel_button: QtWidgets.QPushButton
    def __init__(self, launcher_path: str, settings: QtCore.QSettings, parent: QtWidgets.QWidget | None = None) -> None: ...
    def on_launchbtn_press(self) -> None: ...
    def on_cancelbtn_press(self) -> None: ...

class UpdateDialog(QDialog):
    updater_object: SideFXLabsUpdater
    current_version: str | None
    current_file_path: str | None
    settings: QtCore.QSettings
    launcherButton: QtWidgets.QPushButton
    def __init__(self, parent: QtWidgets.QWidget | None, updater_object: SideFXLabsUpdater) -> None: ...
    def build_ui(self) -> None: ...
    def on_launcherbtn_press(self) -> None: ...

class SideFXLabsUpdater:
    """
        Main updater object, gets called with the shelf button press


    """
    development_releases: list[dict[str, Any]]
    production_releases: list[dict[str, Any]]
    current_version: str | None
    current_file_path: str | None
    def __init__(self, updater_dialog: bool = False) -> None: ...
    def clean_old_installs(self) -> None: ...
    def show_updater_dialog(self) -> None: ...
    def get_current_version(self) -> str | None: ...
    def get_current_file_path(self) -> str | None: ...

def main(argv: Sequence[str]) -> NoReturn: ...
