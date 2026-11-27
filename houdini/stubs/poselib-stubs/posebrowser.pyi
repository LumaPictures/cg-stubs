import hou
from . import applywidget as applywidget, capturewidget as capturewidget, infowindow as infowindow, itembrowser as itembrowser, itemlibrary as itemlibrary, itemnavigator as itemnavigator, plglobals as plglobals, pose as pose, posegrid as posegrid, poselibundos as poselibundos, posemodel as posemodel
from PySide6 import QtGui as QtGui
from hutil.PySide import QtCore, QtWidgets
from poselib.poselib import PoseLibrary as PoseLibrary
from poselib.settings import Settings as Settings

class PoseBrowser(itembrowser.ItemBrowser[posemodel.PoseLibraryModel, posegrid.PoseGrid]):
    itemModel: posemodel.PoseLibraryModel
    gridView: posegrid.PoseGrid
    exportToClipAction: QtGui.QAction
    def __init__(self, parent: PoseLibrary, settings: Settings) -> None: ...
    def cleanup(self) -> None: ...
    def reset(self) -> None: ...
    def isSavingToHDA(self) -> bool:
        """Return True if this library is currently saving to the source
           HDA definition and False otherwise."""
    def sourceHDA(self) -> hou.HDADefinition | None:
        """Return the HDA definition that the current library is saved to.

        Return None if the library is not saved to an HDA.
        """
    def itemIsClip(self, index: QtCore.QModelIndex | QtCore.QPersistentModelIndex | None = None) -> bool:
        """
        If `index` is not None, returns True if the index refers to a valid
        clip item, and False if it does not.

        If `index` is None, returns True if there is a selected item
        and the item is a valid clip item.

        """
    def exportToClipFile(self) -> None: ...
    def importClip(self, path: str | None = None) -> None:
        """Imports a single BClip file from the given path."""
    def addPose(self, name: str, pose_data: pose.PoseData, image: QtCore.QByteArray | None = None, image_type: str | None = None) -> None: ...

class ToggleableGroupBox(QtWidgets.QFrame):
    """QFrame containing GroupBox which can be toggled."""
    toggleGroupBoxButton: QtWidgets.QToolButton
    label: QtWidgets.QLabel
    groupBox: QtWidgets.QGroupBox
    def __init__(self, parent: QtWidgets.QWidget, widget: QtWidgets.QWidget, label: str) -> None: ...
