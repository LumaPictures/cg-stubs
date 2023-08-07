# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyFnAttribute as FnAttribute
import Nodes3DAPI as Nodes3DAPI
import PyFnGeolibProducers
import PyQt5.QtWidgets
import QT4FormWidgets as QT4FormWidgets
import QT4Widgets as QT4Widgets
import PyQt5.QtWidgets as QtWidgets
import Nodes3DAPI.ScenegraphManager as ScenegraphManager
from QT4FormWidgets.GroupFormWidget import GroupFormWidget
from typing import Set, Tuple

class FacesetTexturesDialog(PyQt5.QtWidgets.QDialog):
    def __init__(self, producer: PyFnGeolibProducers.GeometryProducer) -> None: ...
    def _FacesetTexturesDialog__viewSelected(self): ...

class TexturesGroupFormWidget(GroupFormWidget):
    def _TexturesGroupFormWidget__facesetInterpret(self): ...
    def _TexturesGroupFormWidget__update(self, eventType, scenegraphID, isRenderProducer, **kwargs): ...
    def _buildControlWidget(self, layout): ...
