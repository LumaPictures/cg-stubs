from collections.abc import Mapping
from typing import Never, TypeAlias, TypedDict

import hou
from apex.ui.characterpicker.panel import ApexCharacterPicker
from charpicker.tabwindow import _TabDict

# A layout's image catalog (`charpicker.imagecatalog.ImageCatalog.toDict()`).
_ImageCatalogDict: TypeAlias = dict[str, str | dict[str, str]]

# A picker layout, as stored in the `layout` attribute of a `.pick` geometry: the JSON array
# [character path, tabs] or [character path, tabs, image catalog]. A list once loaded, but typed
# as the tuple its positions are, as the code only unpacks, indexes and measures it.
_PickerLayout: TypeAlias = tuple[str, list[_TabDict]] | tuple[str, list[_TabDict], _ImageCatalogDict]

# A picker source of the Animate state's RETRIEVE_PICKER_LAYOUT command, keyed by picker path.
class _PickerSource(TypedDict):
    # `{}` when the picker has no layout data yet.
    layout: _PickerLayout | dict[str, Never]
    read_only: bool

PANEL_INTERFACE_NAMES: tuple[str, str]

def getLayoutDataFromApexSceneGeometry(geo: hou.Geometry, picker_path: str = ...) -> list[_TabDict]: ...
def sceneViewer() -> hou.SceneViewer | None: ...
def retrieveLayout() -> tuple[dict[str, _PickerSource] | None, hou.SceneViewer | None]: ...
def saveLayout(layout: str, source: str | None = ...) -> bool | None: ...
def unload() -> None: ...
def setLayout(
    layout: Mapping[str, _PickerSource] | None, scene_viewer: hou.SceneViewer | None = ..., panel: ApexCharacterPicker | None = ...
) -> None: ...
