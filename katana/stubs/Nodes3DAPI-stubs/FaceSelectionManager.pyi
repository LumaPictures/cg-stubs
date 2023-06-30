# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import Utils.EventModule as EventModule
import Utils as Utils
from _typeshed import Incomplete
from typing import ClassVar

class FaceSelectionManager:
    sharedInstance: ClassVar[None] = ...
    def __init__(self): ...
    def getSelectedFaces(self, path: str) -> list: ...
    def getSelectedPathsAndFaces(self): ...
    def setSelectedPathsAndFaces(self, selectedPathsAndFaces: list, sender: Incomplete | None = ...): ...

def convertFaceSetToString(faceSet) -> str: ...
def createFaceSetFromString(faceSetStr: str) -> set: ...
def getFaceSelectionManager() -> FaceSelectionManager: ...