# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import QT4GLLayerStack.LayerStack as LayerStack
import QT4GLLayerStack.LayerStack
import PyQt5.QtGui as QtGui
from typing import Set, Tuple

ARRAY_TYPE_TO_CONSTANT: list
GL_VOID_P: object
GLvoid: None
ctypes_version: list
integer_types: tuple
void: None

class ClearLayer(QT4GLLayerStack.LayerStack.Layer):
    def __init__(self, *args, **kwargs): ...
    def paintGL(self): ...
    def setColor(self, rgba): ...
