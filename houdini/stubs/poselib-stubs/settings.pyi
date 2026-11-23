from hutil.Qt import QtCore

class Settings(QtCore.QObject):
    """This class contains the global settings in the Pose Library."""
    inEditMode: bool
    editModeChanged: QtCore.Signal
    def __init__(self) -> None: ...
    def reset(self) -> None: ...
    def cleanup(self) -> None: ...
    def isInEditMode(self) -> bool:
        """Return True if the Pose Library is in edit mode and False otherwise."""
    def setIsInEditMode(self, on: bool) -> None:
        """Set whether the Pose Library is in Edit Mode or not."""
