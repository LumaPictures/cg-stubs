from collections.abc import Sequence

import hou

PYS_CTX_SPLIT_LEFT_RIGHT: str
PYS_CTX_SPLIT_TOP_BOTTOM: str
PYS_CTX_DELETE_VIEW: str
PYS_LAYOUT: str
PYS_IMPORT: str
PYS_EXPORT: str
PYS_ADD_BUTTON_TOOLTIP: str
PYS_ADD_IMAGE: str
PYS_ADD_IMAGE_VIEWPORT: str
PYS_ADD_IMAGE_URL: str
PYS_IMAGE_SCALE_TO_CANVAS: str
PYS_IMAGE_FIT_CANVAS: str
PYS_IMAGE_BRING_TO_FRONT: str
PYS_IMAGE_SEND_TO_BACK: str
PYS_IMAGE_RESET_ROTATION: str
PYS_IMAGE_FLIP_H: str
PYS_IMAGE_FLIP_V: str
PYS_IMAGE_DUPLICATE: str
PYS_IMAGE_DELETE: str
PYS_ADD_LABEL: str
PYS_LABEL_EDIT: str
PYS_LABEL_DELETE: str
PYS_FIT_CANVAS_TO_CONTENTS: str
PYS_HELP_TEXT: str
PYS_HELP_LINK_TEXT: str
HELP_LINK_URL: str
HELP_LINK: dict[str, str]
HDA_SECTION_NAME: str
HDA_SECTION_SC_NAME: str
HL_NONE: int
HL_STYLE_1: int
HL_STYLE_2: int
HL_STYLE_3: int
BUTTON_TEXT_PADDING: int
MINIMUM_BUTTON_SIZE: int
MINIMUM_IMAGE_SIZE: int
MINIMUM_LABEL_SIZE: int
DEFAULT_LABEL_WIDTH: int
DEFAULT_LABEL_HEIGHT: int
DEFAULT_LABEL_FONT_SIZE: int
MINIMUM_LABEL_FONT_SIZE: int
MAXIMUM_LABEL_FONT_SIZE: int
ITEM_SNAP_DISTANCE: int
MINIMUM_GRID_CELL_SIZE: int
MAXIMUM_GRID_CELL_SIZE: int
DEFAULT_GRID_CELL_SIZE: int
MINIMUM_CANVAS_SIZE: int
MAXIMUM_CANVAS_SIZE: int
MINIMUM_VIEW_SCALE: float
MAXIMUM_VIEW_SCALE: float
VIEW_SCALE_ZOOM_FACTOR: float
RIG_POSE_VIEWER_STATE: str

def inputDialog(text: str, title: str, initial_contents: str = ...) -> str | None: ...
def multiInputDialog(text: str, input_labels: Sequence[str], title: str, initial_contents: Sequence[str]) -> tuple[str, ...] | None: ...
def warningDialog(message: str, true_button: str = ..., false_button: str = ..., show_cancel: bool = ...) -> bool: ...
def errorDialog(main_message: str, additional_message: str | None = ...) -> bool: ...
def confirmDialog(message: str) -> int: ...
def saveOptionsDialog(message: str) -> int: ...
def firstVisibleSceneViewer() -> hou.SceneViewer | None: ...
