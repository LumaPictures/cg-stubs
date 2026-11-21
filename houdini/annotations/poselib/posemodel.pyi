from collections.abc import Sequence
from typing import Literal, TypeVar, overload

from houtypes import JSONValue
from PySide6 import QtCore

from poselib import itemlibrary, pose
from poselib.posebrowser import PoseBrowser
from poselib.settings import Settings

_P = TypeVar("_P", bound=JSONValue | bytes)

CLIP_FILE: str

class Pose(itemlibrary.Item[pose.PoseData]):
    def __init__(
        self,
        name: str,
        animation_data: pose.PoseData | None,
        image_data: QtCore.QByteArray | None,
        image_type: str | None,
        data_path: str | None = ...,
        image_path: str | None = ...,
        item_type: str | None = ...,
        data_type: str | None = ...,
        item_id: int | None = ...,
        full_data_path: str | None = ...,
    ) -> None: ...
    @overload
    # SideFX's override returns the pose's own serialized form where the base returns the item's JSON payload.
    def serializeData(self, to_string: Literal[True]) -> str: ...  # type: ignore[override]
    @overload
    def serializeData(self, to_string: Literal[False] = ...) -> pose._PoseDataJson | bytes | str | None: ...
    @overload
    def serializeData(self, to_string: bool = ...) -> pose._PoseDataJson | bytes | str | None: ...
    def serializeData(self, to_string: bool = ...) -> pose._PoseDataJson | bytes | str | None: ...
    def saveData(self, save_path: str) -> str | None: ...
    def exportClip(self, file_path: str) -> bool: ...
    def getData(self) -> pose.PoseData | JSONValue | bytes: ...
    @staticmethod
    def deserializeData(data: _P, data_type: str) -> pose.PoseData | _P: ...

class PoseTreeModel(itemlibrary.TreeModel):
    def flags(self, index: QtCore.QModelIndex | QtCore.QPersistentModelIndex) -> QtCore.Qt.ItemFlag: ...
    def editMode(self) -> bool: ...

class PoseGridModel(itemlibrary.GridModel):
    def flags(self, index: QtCore.QModelIndex | QtCore.QPersistentModelIndex) -> QtCore.Qt.ItemFlag: ...
    def editMode(self) -> bool: ...

class PoseLibraryModel(itemlibrary.ItemModel):
    editMode: bool
    def __init__(self, parent: PoseBrowser, item_type: str, hda_section_name: str) -> None: ...
    def itemFromJSON(self, json: itemlibrary._ItemJson, recursive: bool = ...) -> itemlibrary.Item[pose.PoseData] | itemlibrary.Item[JSONValue]: ...
    def isSavingToHDA(self) -> bool: ...
    def exportTo(
        self,
        save_format: str,
        indexes: Sequence[QtCore.QModelIndex | QtCore.QPersistentModelIndex],
        name: str,
        path: str,
    ) -> bool: ...
    def addSettings(self, settings: Settings) -> None: ...
