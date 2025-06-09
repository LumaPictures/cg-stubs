from . import find as find
from PySide6.QtGui import QMouseEvent
from PySide6.QtWidgets import QWidget
from _typeshed import Incomplete
from moverlay.higDialog import HIGDialog

QUICK_TOUR_DLG: Incomplete
HOTSPOT_OVERLAY: Incomplete
HOTSPOT_WIDGET: Incomplete
CURRENT_STEP: int
FIRST_HOTSPOT_MOVE: bool
USER_WORKSPACE: Incomplete
TEMP_WORKSPACE_NAME: str

def runQuickTour() -> None: ...

LEARN_MORE_BUTTON: Incomplete
BACK_BUTTON: Incomplete
NEXT_BUTTON: Incomplete
DONE_BUTTON: Incomplete
GREAT_JOB: Incomplete
CONTINUE_LEARNING: Incomplete
BASIC_SKILLS: Incomplete
IN_APP_TUTORIALS: Incomplete
SEE_ALL_TUTORIALS: Incomplete
END_QUICK_TOUR: Incomplete

class TutorialArea(QWidget):
    hover: bool
    def __init__(self, parent: Incomplete | None = None) -> None: ...
    def sizeHint(self): ...
    def enterEvent(self, event) -> None: ...
    def leaveEvent(self, event) -> None: ...
    def paintEvent(self, event) -> None: ...
    def mouseReleaseEvent(self, event: QMouseEvent) -> None: ...

class GreatJobDialog(HIGDialog):
    def __init__(self, parent: Incomplete | None = None) -> None: ...
    def tutorialClicked(self) -> None: ...
    def allTutorialsClicked(self) -> None: ...
    def endTourClicked(self) -> None: ...
