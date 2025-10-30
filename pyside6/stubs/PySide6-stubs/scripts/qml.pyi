from PySide6.QtCore import QCoreApplication as QCoreApplication, QLibraryInfo as QLibraryInfo, QUrl as QUrl, Qt as Qt, SignalInstance as SignalInstance
from PySide6.QtGui import QGuiApplication as QGuiApplication, QSurfaceFormat as QSurfaceFormat
from PySide6.QtQml import QQmlApplicationEngine as QQmlApplicationEngine, QQmlComponent as QQmlComponent
from PySide6.QtQuick import QQuickItem as QQuickItem, QQuickView as QQuickView
from PySide6.QtWidgets import QApplication as QApplication
from pathlib import Path

def import_qml_modules(qml_parent_path: Path, module_paths: list[Path] = []): ...
def print_configurations(): ...
