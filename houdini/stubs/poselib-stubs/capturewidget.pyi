# Houdini stubs generated from Houdini 22.0.466

import PySide6.QtCore
import PySide6.QtGui
import PySide6.QtWidgets
import hou
from . import character as character, plglobals as plglobals
from hutil.PySide import QtCore, QtWidgets
from poselib.posebrowser import PoseBrowser as PoseBrowser

class _CaptureNameField(QtWidgets.QLineEdit):
    """The pose name field."""
    def __init__(self) -> None: ...
    def reset(self) -> None: ...
    def focusInEvent(self, event: PySide6.QtGui.QFocusEvent) -> None:
        """Handle focus in."""
    def inputtedName(self) -> str: ...

class _ParmOptions(QtCore.QObject):
    """This class keeps some settings the same in both the Capture Pose
       and Capture Clip options dialogs through the use of custom signals."""
    captureAllParms: bool
    captureAllParmsChanged: QtCore.Signal
    def __init__(self) -> None: ...
    def onRevert(self) -> None: ...
    def setCaptureAllParms(self, captureAllParms: bool) -> None: ...

class _ParmOptionsWidget(QtWidgets.QVBoxLayout):
    """Layout widget for parameter options to both poses and clips."""
    allParmsBox: QtWidgets.QCheckBox
    parmOptions: _ParmOptions
    def __init__(self) -> None: ...
    def captureAllParms(self) -> bool:
        """Returns True if 'Capture All Parameters' is checked"""
    def setCaptureAllParms(self, cap_all_parms: bool) -> None:
        """Set whether all parameters are saved for poses and clips."""

class _ThumbnailOptions(QtCore.QObject):
    """This class keeps some settings the same in both the Capture Pose
       and Capture Clip options dialogs through the use of custom signals."""
    createThumbnail: bool
    includeAllObjects: bool
    thumbnailSize: PySide6.QtCore.QSize
    thumbnailQuality: int
    THUMBNAIL_MIN_SIZE: int
    THUMBNAIL_MAX_SIZE: int
    THUMBNAIL_DEFAULT_SIZE: int
    DEFAULT_SIZES: tuple[int, ...]
    THUMBNAIL_MIN_QUALITY: int
    THUMBNAIL_MAX_QUALITY: int
    THUMBNAIL_DEFAULT_QUALITY: int
    DEFAULT_QUALITY_VALUES: tuple[int, ...]
    createThumbnailChanged: QtCore.Signal
    includeAllObjectsChanged: QtCore.Signal
    thumbnailSizeChanged: QtCore.Signal
    thumbnailQualityChanged: QtCore.Signal
    def __init__(self) -> None: ...
    def onRevert(self) -> None: ...
    def setCreateThumbnail(self, create_thumbnail: bool) -> None:
        """Set whether Thumbnails are created for poses and clips."""
    def setIncludeAllObjects(self, include_all_objects: bool) -> None:
        """Set whether Thumbnails include all objects."""
    def setThumbnailSize(self, size: PySide6.QtCore.QSize) -> None:
        """Set resolution of thumbnail created upon pose capture."""
    def setThumbnailQuality(self, quality: int) -> None:
        """Set quality of thumbnail created upon pose capture."""

class _ThumbnailOptionsWidget(QtWidgets.QVBoxLayout):
    """Layout widget for thumbnail options to both poses and clips."""
    createThumbnailBox: QtWidgets.QCheckBox
    thumbnailSizeLabel: QtWidgets.QLabel
    thumbnailWidthField: QtWidgets.QLineEdit
    thumbnailHeightField: QtWidgets.QLineEdit
    thumbnailSizeSlider: QtWidgets.QSlider
    thumbnailQualityLabel: QtWidgets.QLabel
    thumbnailQualityField: QtWidgets.QLineEdit
    thumbnailQualitySlider: QtWidgets.QSlider
    includeAllObjectsBox: QtWidgets.QCheckBox
    createAnimatedThumbnailBox: QtWidgets.QCheckBox
    thumbnailSizeWidget: QtWidgets.QWidget
    thumbnailOptions: _ThumbnailOptions
    def __init__(self) -> None: ...
    def onRevert(self) -> None:
        """Revert all settings back to defaults."""
    def setCreateThumbnail(self, create_thumbnail: bool) -> None:
        """Set whether Thumbnails are created for poses and clips."""
    def setIncludeAllObjects(self, include_all_objects: bool) -> None:
        """Set whether Thumbnails include all objects."""
    def setThumbnailSize(self, size: PySide6.QtCore.QSize) -> None:
        """Set resolution of thumbnail created upon pose capture."""
    def setThumbnailQuality(self, quality: int) -> None:
        """Set quality of thumbnail created upon pose capture."""
    def createAnimatedThumbnail(self) -> bool:
        """Return True if the Animated Thumbnail box is checked on and False
           otherwise."""
    def createThumbnail(self) -> bool:
        """Return True if the Create Thumbnail box is checked on and False
           otherwise."""
    def includeAllObjects(self) -> bool:
        """Return True if the Include All Objects box is checked on and False
           otherwise."""
    def thumbnailSize(self) -> PySide6.QtCore.QSize:
        """Return resolution of thumbnail to be created upon pose capture."""
    def thumbnailQuality(self) -> int:
        """Return quality of thumbnail to be created upon pose capture."""

class _CaptureOptionsDialog(QtWidgets.QDialog):
    """Modal dialog containing thumbnail options for capturing clips and poses.
       Parent of _CaptureClipOptionsDialog, _CapturePoseOptionsDialog."""
    thumbnailOptionsWidget: _ThumbnailOptionsWidget
    parmOptionsWidget: _ParmOptionsWidget
    createThumbnailBox: QtWidgets.QCheckBox
    includeAllObjectsBox: QtWidgets.QCheckBox
    def __init__(self, window_title: str) -> None: ...
    def close(self, force: bool = False) -> None: ...
    def closeEvent(self, event: PySide6.QtGui.QCloseEvent) -> None:
        """Handle 'X' button clicked."""
    def bringToFocus(self) -> None:
        """Opens dialog if not already open, then brings it into focus."""
    def createThumbnail(self) -> bool:
        """Return True if the Create Thumbnail box is checked on and False
           otherwise."""
    def includeAllObjects(self) -> bool:
        """Return True if the Include All Objects box is checked on and False
           otherwise."""
    def thumbnailSize(self) -> PySide6.QtCore.QSize:
        """Return resolution of thumbnail to be created upon pose capture."""
    def thumbnailQuality(self) -> int:
        """Return quality of thumbnail to be created upon pose capture."""
    def keyPressEvent(self, event: PySide6.QtGui.QKeyEvent) -> None: ...

class _CaptureClipOptionsDialog(_CaptureOptionsDialog):
    """Modal dialog containing options for capturing clips."""
    clipOptions: QtWidgets.QVBoxLayout
    bakeClipBox: QtWidgets.QCheckBox
    sampleRateFieldLabel: QtWidgets.QLabel
    sampleRateField: QtWidgets.QLineEdit
    bclipBox: QtWidgets.QCheckBox
    bloscBox: QtWidgets.QCheckBox
    def __init__(self) -> None: ...
    def bakeClip(self) -> bool:
        """Return True if the Bake Clip box is checked on and False
           otherwise."""
    def useBclip(self) -> bool: ...
    def useBloscCompression(self) -> bool: ...
    def sampleRate(self) -> float:
        """Returns Sample Rate field text, or the sample rate default value if 
           Bake Clip box is not checked on."""

class _CapturePoseOptionsDialog(_CaptureOptionsDialog):
    """Modal dialog containing options for capturing poses."""
    def __init__(self) -> None: ...

class CaptureFrameRangeWidget(QtWidgets.QWidget):
    """Widget for capturing frame ranges used for generating clips and
       thumbnails."""
    frameRangeOptionsDropdown: QtWidgets.QPushButton
    frameRangeMenu: QtWidgets.QMenu
    startField: QtWidgets.QLineEdit
    endField: QtWidgets.QLineEdit
    def __init__(self, parent: PySide6.QtWidgets.QWidget) -> None: ...
    def startFrame(self) -> float:
        """Return the start frame captured by this widget."""
    def endFrame(self) -> float:
        """Return the end frame captured by this widget."""
    def showEvent(self, event: PySide6.QtGui.QShowEvent) -> None:
        """Handle the show event."""

class CaptureWidget(QtWidgets.QWidget):
    """Widget containing capture pose controls."""
    ownerLibrary: PoseBrowser
    capturePoseOptionsDialog: _CapturePoseOptionsDialog
    captureClipOptionsDialog: _CaptureClipOptionsDialog
    parmOptionsWidget: _ParmOptionsWidget
    thumbnailOptionsWidget: _ThumbnailOptionsWidget
    nameField: _CaptureNameField
    frameRangeWidget: CaptureFrameRangeWidget
    nodeChanged: QtCore.Signal
    def __init__(self, parent: PySide6.QtWidgets.QWidget, owner_library: PoseBrowser) -> None: ...
    def cleanup(self) -> None:
        """This is called when the pose library interface is about to be
           destroyed."""
    def reset(self) -> None:
        """Reset the capture widget to its default state."""
    def selectedNode(self) -> hou.OpNode | None: ...
    def setNode(self, path: str) -> None: ...
