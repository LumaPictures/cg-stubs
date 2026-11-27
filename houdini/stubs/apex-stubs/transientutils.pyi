import _apex
import apex
import hou
from apex.bookmarkmanager import _BookmarkMetadata
from typing import NoReturn

TYPE_CONSTRAINT: str

def getUniqueTransientID(data: apex.Dict) -> int: ...
def validateTransientEntry(entry: apex.Dict, type_name: str) -> bool: ...
def getTransientData(scene: apex.Scene, type_name: str, folder: str = '', layer: str | None = None, uuid: int | str | None = None) -> tuple[str, apex.Dict | None, apex.Dict | None] | tuple[None, None, None]:
    """
    A helper function to get the path to the transient data dictionary and the
    dictionary.

    :param scene: The scene from which the transient data is retrieved.
    :type  scene: apex.Scene
    :param type_name: The type name of the data.
    :type type_name: String
    :param folder: The folder in the scene for the transient data.
    :type  folder: String
    :param layer: The animation layer on which the transient data is defined.
    :type  layer: String
    :param uuid: An optional Id for the entry to return
    :type uuid: String, Int, or None
    """
def removeTransientEntry(scene: apex.Scene, type_name: str, uuid: int | str, key: str | None = None, folder: str = '', layer: str | None = None) -> bool:
    """
    Remove a transient entry, returning true if successful

    :param scene: The scene to remove the transient entry from.
    :type  scene: apex.Scene
    :param type_name: The type name of the data.
    :type type_name: String
    :param uuid: A unique id that identifies the entry to alter.
    :type uuid: Int
    :param key: The key of the entry data to remove. If none, the full entry
                will be removed
    :type  key: String or None
    :param folder: The folder in the scene for the transient data.
    :type  folder: String
    :param layer: The animation layer to remove the transient data from.
    :type  layer: String
    """
def updateTransientEntryMetadataFromDict(scene: apex.Scene, type_name: str, uuid: int | str, metadata: _BookmarkMetadata, folder: str = '', layer: str | None = None) -> bool:
    """
    Updates the metadata of a transient entry, returning True anything changed.

    :param scene: The scene in which to update the transient entry.
    :type  scene: apex.Scene
    :param type_name: The type name of the data.
    :type type_name: String
    :param uuid: A unique id that identifies the entry to alter.
    :type uuid: Int
    :param metadata: A dictionary of the metadata to update
    :type metadat: Dict
    :param folder: The folder in the scene for the transient data.
    :type  folder: String
    :param layer: The animation layer to write the transient data to.
    :type  layer: String
    """
def updateTransientEntryMetadata(scene: apex.Scene, type_name: str, uuid: int | str, label: str | None = None, start_frame: int | None = None, end_frame: int | None = None, folder: str = '', layer: str | None = None) -> NoReturn:
    """
    Updates the metadata of a transient entry, returning True if successful.

    :param scene: The scene in which to update the transient entry.
    :type  scene: apex.Scene
    :param type_name: The type name of the data.
    :type type_name: String
    :param uuid: A unique id that identifies the entry to alter.
    :type uuid: Int
    :param label: The label of the transient entry.
    :type label: String or None
    :param start_frame: The start frame of the transient entry.
    :type start_frame: Int or None
    :param end_frame: The end frame of the transient entry.
    :type end_frame: Int or None
    :param folder: The folder in the scene for the transient data.
    :type  folder: String
    :param layer: The animation layer to write the transient data to.
    :type  layer: String
    """
def getTransientEntryMetadata(scene: apex.Scene, type_name: str, uuid: int | str, folder: str = '', layer: str | None = None) -> _BookmarkMetadata | None:
    """
    Returns the metadata for a transient entry.

    :param scene: The scene which owns the transient entry.
    :type  scene: apex.Scene
    :param type_name: The type name of the data.
    :type type_name: String
    :param uuid: A unique id that identifies the entry to alter.
    :type uuid: Int
    :param folder: The folder in the scene for the transient data.
    :type  folder: String
    :param layer: The animation layer for the transient data.
    :type  layer: String
    """
def addTransientEntry(scene: apex.Scene, type_name: str, entry: apex.Dict, folder: str = '', layer: str | None = None) -> int:
    """
    Adds a transient entry to the scene, returning the
    unique id of the entry.

    :param scene: The scene to push the transient entry to.
    :type  scene: apex.Scene
    :param type_name: The type of the entry
    :type type_name: String
    :param entry: The new entry transient entry.
    :type  entry: Dict
    :param folder: The folder in the scene for the transient data.
    :type  folder: String
    :param layer: The animation layer to write the transient data to.
    :type  layer: String or None
    """
def buildTransientEntry(label: str, start_frame: int, end_frame: int, data: _apex._ValueArg, color: hou.Color = ...) -> apex.Dict:
    """
    Builds and returns a transient entry dictionary.

    :param label: The label of the transient entry.
    :type label: String
    :param start_frame: The start frame of the transient entry.
    :type start_frame: Int
    :param end_frame: The end frame of the transient entry.
    :type end_frame: Int
    :param data: The custom entry data.
    :type  data: Any APEX type
    :param color: The color of the transient entry
    :type color: hou.Color
    """
