# Houdini stubs generated from Houdini 22.0.466

import hou
from . import plglobals as plglobals, pose as pose
from houtypes import JSONValue

DISK: str
HDA_DEFINITION: str
DATA_PREFIX: str
ROOT: str

class LazyLoader:
    """
    Helper class for loading pose / clip data on demand.

    **TODO: Add loading UI message so that users know when data is being loaded.**
    """
    data_source_type: str | None
    data_source: str | hou.HDADefinition | None
    hda_section_name_prefix: str | None
    @classmethod
    def setDataSourceInfo(cls, data_source_type: str, data_source: str | hou.HDADefinition | None, hda_section_name_prefix: str | None = None) -> None: ...
    @classmethod
    def assertDataSourceIsSet(cls) -> None: ...
    @classmethod
    def loadData(cls, data_path: str | None, item_id: UniqueId | int | None, data_type: str) -> JSONValue | bytes:
        """
        Loads data from the given data_path. Correctly handles any
        special considerations for loading data depending on data_type.

        Will raise assertion errors if the data source is not set.

        :param data_path: The file path from which data should be loaded
            if loading from disk. This must the the data file path
            relative to the ROOT of the library, not the item's current folder.
        :param item_id: The item's unique id (used for loading from a
            HDA definition).
        :param data_type: The type of data being loaded
            (One of JSON, CLIP, BCLIP, BCLIP_SC).
        :return: The loaded data or None in case of error(s).
        """
    @classmethod
    def hdaSectionNameForItemData(cls, item_id: UniqueId | int, section_name_prefix: str | None = None) -> str:
        """
        Returns the HDA section name for the given item's data.
        The LazyLoader must be setup for loading from an HDA if
        section_name_prefix is None, otherwise an assertion failure will occur.
        The returned section name will end with .sc as data sections
        should all be blosc compressed.
        :param item_id: The id of the item.
        :param section_name_prefix: The section name prefix to use.
            If None, LazyLoader will attempt to use it's section name prefix
            (set by calling setDataSourceInfo()). If it has not been set,
            an assertion failure will occur.
        """
    @classmethod
    def saveState(cls) -> None:
        """
        Saves current data source info.
        Use restoreState() to restore saved info.
        """
    @classmethod
    def restoreState(cls) -> None:
        """
        Restores current data source info. Ensure state was saved
        using saveState() before calling this method.
        """
    @classmethod
    def reset(cls) -> None:
        """
        Resets the LazyLoader to its initial state.
        This should only be called on library exit.
        """

class UniqueIdError(Exception): ...

class UniqueId:
    """
    Helper class for ensuring all Items get a unique id.
    This is used to ensure each item get's its own section for pose/clip
    data and image data in a HDA.

    Note: For proper operation, reload() must **NOT** be called on
    this class/module.

    Usage:
    UniqueId() when creating new Item objects.

    UniqueId(from_id) if loading from saved json files, where from_id is
    the id saved in the JSON file.

    UniqueId.reset() when resetting the library before loading or creating
    a new library. **Important**: Ensure there are no references to UniqueId
    instances that were created before the reset() method was called.

    UniqueId.getId() on an instance returns its id as a long.
    UniqueId.release() should be called on an instance just before
    it is removed to ensure the id is properly freed for reuse.

    **Important**: Do not access any private variables of this class or
    you risk introducing inconsistencies which may lead to duplicate ids
    being used.
    """
    __used_ids: set[int]
    __free_ids: set[int]
    __largest_id: int
    @classmethod
    def reset(cls) -> None:
        """
        Resets all id information. After calling this method,
        all existing UniqueId instances should be considered invalid
        and should not be used.
        """
    def __init__(self, from_id: int | None = None) -> None:
        """
        Create a UniqueId object, automatically fetching an available
        unique id if the given `from_id` is None.

        :param from_id: If not None, attempt to use this id as
            the unique id. If the given id is in use or is not an int/long,
            an UniqueIdError will be raised.
        :type from_id: int or long
        """
    def force_id(self, id_to_use: int) -> None:
        """
        *USE WITH CAUTION*. This forces the use of the given id for
        this UniqueId instance without any checks, tracking, or state saving.
        :param id_to_use: The id to use for this instance.
        """
    def getId(self) -> int: ...
    def release(self) -> None:
        """
        Releases the unique id. Ensure no reference is maintained
        to this object after calling release().
        """

def cleanup() -> None:
    """
    Cleans up helper classes.
    This should only be called on library exit.
    """
