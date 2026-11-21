import typing
from . import chopdata as chopdata, helpers as helpers, infowindow as infowindow, itemlibrary as itemlibrary, plglobals as plglobals, pose as pose
from collections.abc import Sequence
from houtypes import JSONValue
from hutil.PySide import QtCore
from poselib.posebrowser import PoseBrowser as PoseBrowser
from poselib.settings import Settings as Settings
from typing import Literal

from typing import TypeVar
from typing import TypeVar
_P = TypeVar('_P', bound=JSONValue | bytes)
CLIP_FILE: str

class Pose(itemlibrary.Item[pose.PoseData]):
    def __init__(self, name: str, animation_data: pose.PoseData | None, image_data: QtCore.QByteArray | None, image_type: str | None, data_path: str | None = None, image_path: str | None = None, item_type: str | None = None, data_type: str | None = None, item_id: int | None = None, full_data_path: str | None = None) -> None: ...
    @typing.overload  # type: ignore[override]
    def serializeData(self, to_string: Literal[True]) -> str: ...
    @typing.overload
    def serializeData(self, to_string: Literal[False] = ...) -> pose._PoseDataJson | bytes | str | None: ...
    @typing.overload
    def serializeData(self, to_string: bool = ...) -> pose._PoseDataJson | bytes | str | None: ...
    def saveData(self, save_path: str) -> str | None:
        """Save item data file to the given path."""
    def exportClip(self, file_path: str) -> bool:
        """
        Save item data to the given file, using the file extension
        to determine the output clip format. If the file_name does not
        specify the format, bclip is used by default and '.bclip'
        is added to the given file path.

        Calling this method may raise a hou.OperationFailed exception since
        callees of this method call methods in hou for converting clip data.
        """
    def getData(self) -> pose.PoseData | JSONValue | bytes: ...
    @staticmethod
    def deserializeData(data: _P, data_type: str) -> pose.PoseData | _P:
        """ Deserializes data from JSON and returns a PoseData
        instance representing the data. """

class PoseTreeModel(itemlibrary.TreeModel):
    def flags(self, index: QtCore.QModelIndex | QtCore.QPersistentModelIndex) -> QtCore.Qt.ItemFlag: ...
    def editMode(self) -> bool: ...

class PoseGridModel(itemlibrary.GridModel):
    def flags(self, index: QtCore.QModelIndex | QtCore.QPersistentModelIndex) -> QtCore.Qt.ItemFlag: ...
    def editMode(self) -> bool: ...

class PoseLibraryModel(itemlibrary.ItemModel):
    editMode: bool
    def __init__(self, parent: PoseBrowser, item_type: str, hda_section_name: str) -> None: ...
    def itemFromJSON(self, json: itemlibrary._ItemJson, recursive: bool = False) -> itemlibrary.Item[pose.PoseData] | itemlibrary.Item[JSONValue]: ...
    def isSavingToHDA(self) -> bool:
        """Return True if this library is currently saving to the source
           HDA definition and False otherwise."""
    def exportTo(self, save_format: str, indexes: Sequence[QtCore.QModelIndex | QtCore.QPersistentModelIndex], name: str, path: str) -> bool:
        """ Export to a bclip file. Items must be clips. """
    def addSettings(self, settings: Settings) -> None: ...
