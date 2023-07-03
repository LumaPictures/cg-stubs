import PySide2
from _typeshed import Incomplete

class MessageType:
    DEBUG: int
    INFO: int
    WARNING: int
    ERROR: int

class Preferences(PySide2.QtCore.QObject):
    preferenceChanged: Incomplete
    def __init__(self) -> None: ...
    OBJECTS_FOLDER: Incomplete
    IMAGES_FOLDER: Incomplete
    TEXTURES_FOLDER: Incomplete
    PROJECTORS_FOLDER: Incomplete
    NODEGRAPH_FOLDER: Incomplete
    EXPORT_FLOAT_IMG_TYPE: Incomplete
    EXPORT_HALF_IMG_TYPE: Incomplete
    EXPORT_BYTE_IMG_TYPE: Incomplete
