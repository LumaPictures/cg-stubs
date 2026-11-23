from typing import TypedDict

from PySide6 import QtGui
from autorigs.modules.base.rootModule import _ModuleJson

class _PresetJson(TypedDict):
    json_filepath: str
    json_obj: list[_ModuleJson] | None

ICON_SIZE: int
CREATE_MODULE_ICON_NAME: str
CREATE_MODULE_ICON_WIDTH: int
CREATE_MODULE_ICON_HEIGHT: int
HELP_ICON: QtGui.QIcon
DEFAULT_ASSET_ICON: QtGui.QIcon
FILE_PATTERN_IMAGES: None
FILE_PATTERN_ASSET: str
FILE_PATTERN_GEOMETRY: None
FILE_PATTERN_JSON: str
FILE_PATTERN_ICON: str
ASSET_FILE_LOCATION: str
ASSET_ICON_LOCATION: str
autorigs_defaults_path: str
DEFAULT_JSONS: dict[str, str]
autorigs_presets_path: str
DEFAULT_PRESET_JSONS: dict[str, _PresetJson]
