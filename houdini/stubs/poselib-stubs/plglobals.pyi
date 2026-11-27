import hou
from collections.abc import Collection, Iterable
from enum import Enum
from hutil.Qt import QtCore, QtGui, QtWidgets
from past.utils import old_div as old_div
from poselib.pose import PoseFrame as PoseFrame

POSE_LIB_HDA_SECTION_NAME: str
POSE_LIB_HDA_SECTION_SC_NAME: str
JSON_KEYFRAMES: str
JSON_CHOP_DATA: str
JSON_FRAME_COUNT: str
JSON_PARMS: str
NO_HISTORY: str
CLEAR_HISTORY: str
CONTROLS_WIDTH: int
CONTROLS_H_SPACING: int
CONTROLS_V_SPACING: int
OPTION_GROUP_V_SPACING: int
OPTION_DIALOG_WIDTH: int
ICON_WIDTH: int
ICON_HEIGHT: int
BUTTON_WIDTH: int
BUTTON_HEIGHT: int
ENABLE_APPLY_OPTIONS_DIALOG: bool

class ResizeMode(Enum):
    """
    Mode to use when scaling thumbnails and videos.
    SCALE_ONLY: Directly scale the source image to the provided resolution, making no
                attempt to preserve aspect ratio
    SCALE_AND_CROP: Scale and crop the image to fit, ensuring the aspect
                    ratio and desired resolution are preserved.
    SCALE_AND_CROP_HORIZONTAL: Scale and crop the image, cropping horizontally to
                               preserve the aspect ratio. Resulting image can
                               have smaller width than the specified resolution.
    SCALE_AND_CROP_VERTICAL: Scale and crop the image, cropping vertically to
                               preserve the aspect ratio. Resulting image can
                               have smaller height than the specified resolution.
    """
    SCALE_ONLY = 0
    SCALE_AND_CROP = 1
    SCALE_AND_CROP_HORIZONTAL = 2
    SCALE_AND_CROP_VERTICAL = 3

def joinPaths(*paths: str) -> str:
    """Returns a string representing the normalized directory of the combined 
       path components.

    The string will contain only forward slashes and no trailing slashes.
    """
def getAvailableStringId(name: str, existing_names: Collection[str]) -> str:
    """Creates a unique string identifier by appending a number to the end of
       the provided identifier and incrementing until a unique identifier 
       is obtained.
    """
def loadThumbnailFromFile(image_path: str, show_errors: bool = True) -> tuple[QtCore.QByteArray, bool] | tuple[None, bool]:
    """Loads image file at the given path.

    Returns a 2-tuple containing the image data contained in a QByteArray and 
    a boolean which is set to True if the image is animated.
    """
def getImgDataFromIcon(icon: str, width: int, height: int) -> QtCore.QByteArray:
    """Return img data of provided icon."""
def getViewportImage(frame: float | None = None, resolution: QtCore.QSize | None = None, include_all_objects: bool = False, character_path: str | None = None, thumbnail_quality: int = 2, resize_mode: ResizeMode = ...) -> QtCore.QByteArray:
    """Returns QByteArray containing still image of the current viewport.

    If `character_path` points to a SOP node, this first object node ancestor
    of the SOP node will be used instead.

    """
def getViewportGif(frame_start: float, frame_end: float, frame_increment: int = 1, resolution: QtCore.QSize | None = None, include_all_objects: bool = False, character_path: str | None = None, thumbnail_quality: int = 0, fps: float = 0, resize_mode: ResizeMode = ...) -> QtCore.QByteArray | None:
    """Returns a QByteArray whose content is an animated gif that captures the
        animation of the current viewport from frame_start to frame_end. Ensure
        that frame_end - frame_start >= 2.0 is true before calling this.

    If `character_path` points to a SOP node, this first object node ancestor
    of the SOP node will be used instead.

    :param frame_start: Start frame to capture
    :param frame_end: End frame to capture
    :param resolution: resolution of output gif
    :param include_all_objects: If true, all objects will be captured, otherwise, only
                                the character at character_path will be captured
    :param thumbnail_quality: Thumbnail quality to pass to the viewwrite command
                              for capturing the flipbook.
    :param fps: fps of the resulting gif. If 0, will use hou.fps()

    """
def getSceneViewerSelected() -> hou.SceneViewer: ...
def inputDialog(text: str, title: str, initial_contents: str = '') -> str | None:
    """Create a popup dialog with the given properties
    and return the result or None.
    """
def warningDialog(message: str, true_button: str = 'OK', false_button: str = 'Cancel', show_cancel: bool = True) -> bool:
    """Create a warning dialog with the given properties
    and return if true_button or Ok was pressed.
    """
def errorDialog(main_message: str, additional_message: str | None = None) -> bool:
    """Create an error dialog with the given message(s) and return if OK was
    pressed.
    """
def confirmDialog(message: str) -> int:
    '''Create a confirm dialog with the options of "Save", "Discard" and 
    "Cancel". Returns the option number chosen.
    '''
def formatParmsToStr(parms: Collection[str], indent_size: int, line_length: int, string_length: int) -> str:
    """Converts list of parms into a string, truncated if necessary."""
def formatFilesToStr(files: Collection[str], indent_size: int, line_length: int, string_length: int) -> str:
    """Converts list of file paths into a string, truncated if necessary."""
def scopedChannels(node: hou.OpNode) -> list[hou.Parm]:
    """Return list of scoped channels from the given node."""
def getChannelFrameCount(pose_list: Iterable[PoseFrame]) -> dict[str | None, int]:
    """Return dictionary of captured channels and the number of frames 
       per channel."""
def chooseAndLoadClip(prompt_title: str) -> str | None:
    """Prompt the user to choose a Clip file.

    Return chosen Clip path, or None if no file was chosen.
    """
def createEditor(parent: QtWidgets.QWidget | None, option: QtWidgets.QStyleOptionViewItem, index: QtCore.QModelIndex | QtCore.QPersistentModelIndex, margins: QtCore.QMargins) -> QtWidgets.QWidget:
    """Create custom editor interface for items."""
def jsonToStr(json_struct: object) -> str:
    """Converts JSON structure to string."""
def getPixmapFromIcon(icon: str, width: int, height: int) -> QtGui.QPixmap:
    """Return QPixmap of provided icon."""
def writeFile(file_path: str, string: str | bytes, binary: bool = False) -> bool:
    """Write the provided string to the given file path."""
def clearDirectory(path: str) -> None:
    """Clears provided directory of all contents including subdirectories.

    Return True if operation was successul.  Return False otherwise.
    """
def joinSystemPaths(*paths: str) -> str:
    """Returns a string representing the normalized directory of the 
       combined path components.

    The returned string will contain only forward slashes and no 
    trailing slashes.
    """
