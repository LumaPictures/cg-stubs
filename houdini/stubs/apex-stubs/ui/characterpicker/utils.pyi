import hou
from apex.characterpicker.commands import Commands as Commands
from apex.ui.characterpicker.panel import ApexCharacterPicker as ApexCharacterPicker
from apex.utils import prependCharToControlPath as prependCharToControlPath
from charpicker.tabwindow import _TabDict
from collections.abc import Mapping
from typing import Never, TypedDict

from typing import TypeAlias
from typing import TypeAlias
_ImageCatalogDict: TypeAlias = dict[str, str | dict[str, str]]
_PickerLayout: TypeAlias = tuple[str, list[_TabDict]] | tuple[str, list[_TabDict], _ImageCatalogDict]
class _PickerSource(TypedDict):
    layout: _PickerLayout | dict[str, Never]
    read_only: bool

APEX_CHARPICKER_ATTRIB_NAME: str
PANEL_INTERFACE_NAMES: tuple[str, str]

def getLayoutDataFromApexSceneGeometry(geo: hou.Geometry, picker_path: str = '') -> list[_TabDict]: ...
def sceneViewer() -> hou.SceneViewer | None:
    """Find and return a scene viewer"""
def retrieveLayout() -> tuple[dict[str, _PickerSource] | None, hou.SceneViewer | None]: ...
def saveLayout(layout: str, source: str | None = None) -> bool | None: ...
def unload() -> None: ...
def setLayout(layout: Mapping[str, _PickerSource] | None, scene_viewer: hou.SceneViewer | None = None, panel: ApexCharacterPicker | None = None) -> None:
    """
    Updates layout for Character Picker Panels by passing them a source geometry
    and scene_viewer to hook in to
    """
