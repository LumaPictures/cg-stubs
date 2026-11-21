# Houdini stubs generated from Houdini 22.0.466

import hou
import os
import pprint
from collections.abc import Iterable, Iterator, Mapping
from hutil.PySide import QtCore, QtGui
from typing import Any, TypedDict

class _BrushMetaData(TypedDict, total=False, extra_items=Any):  # type: ignore[call-arg]
    version: int
    brush_id: int

class _BrushInfo(TypedDict):
    id: int
    node_type: hou.OpNodeType
    node_type_name: str
    name: str
    label: str

PRESET_EXT: str
GALLERY_FOLDER: str
BRUSH_TYPE_ROLE: int
BRUSH_NAME_ROLE: int
BRUSH_INFO_ROLE: int
BRUSH_LABEL_ROLE: int
BRUSH_PRESET_ROLE: int
BRUSH_FACTORY_DEFAULT_ID: int

def isFactoryDefaultBrush(brush_info: Mapping[str, object]) -> bool: ...

class BrushItemModel(QtGui.QStandardItemModel):
    """ The brush panel model.
    """
    default_icon_pixmap: QtGui.QPixmap
    default_icon_mask: QtGui.QBitmap
    def __init__(self) -> None: ...
    def brushInfoManager(self) -> BrushInfoManager: ...
    def setData(self, index: QtCore.QModelIndex | QtCore.QPersistentModelIndex, value: Any, role: int) -> bool: ...
    def data(self, index: QtCore.QModelIndex | QtCore.QPersistentModelIndex, role: int) -> str | _BrushInfo | QtGui.QIcon | None: ...

class BrushInfoManager:
    """ Manages brush info objects used by the brush panel. A brush info
        object represents a brush instance and preset, it is used for
        creating gallery entries (aka presets) and also for defining
        toolbar buttons. The brush info name is unique across all
        presets. See _createBrushInfoObject() for details.
    """
    def __init__(self) -> None: ...
    def brushInfoFromName(self, brush_name: str) -> _BrushInfo | None: ...
    def brushInfoIter(self) -> Iterator[_BrushInfo]: ...
    def brushInfoListFromHDA(self, library_path: str) -> list[_BrushInfo]: ...
    def addBrushInfoFromHDA(self, library_path: str) -> list[_BrushInfo]: ...
    def addBrushInfoFromDefinition(self, definition: hou.HDADefinition) -> list[_BrushInfo]: ...
    def addBrushInfoCopy(self, brush_info: _BrushInfo) -> _BrushInfo: ...
    def removeBrushInfoFromList(self, brush_info_list: Iterable[_BrushInfo]) -> None: ...
    def revertBrushInfoEntry(self, brush_info: _BrushInfo, factory_defaults: bool) -> None: ...
    def removeBrushInfoEntry(self, brush_info: _BrushInfo) -> None: ...
    def updateBrushInfoEntry(self, brush_info: _BrushInfo) -> None: ...
    def selectBrush(self, brush_info: _BrushInfo) -> hou.SopNode | None:
        """ Given a brush node type creates a new brush node or select
            an existing one from the layout node container. The node may
            be created as a factory default, or from a gallery entry.
        """
    def saveBrushPresetFromInfo(self, brush_info: _BrushInfo | None) -> None:
        """ Save a preset for the current node.
        """

class BrushGalleryManager:
    """ Manage brush galleries along with their presets (gallery entries).
        Presets are saved to galleries with a unique name created from
        the brush node type + an id managed by BrushInfoManager. A
        preset is applicable to all instances of a given brush type.
    """
    def __init__(self) -> None: ...
    def updateGalleryCache(self, node_type: hou.NodeType) -> hou.Gallery | None:
        """ Update the gallery cache with the gallery matching node_type.
            This method doesn't create a gallery file and may return
            an empty gallery. New gallery files are created with
            _newGallery()

            Returns the gallery object matching node_type.
        """
    def galleryIter(self) -> Iterator[hou.Gallery]:
        """ Return a gallery iterator.
        """
    def gallery(self, node_type_name: str) -> hou.Gallery | None: ...
    def galleryEntry(self, brush_info: _BrushInfo) -> hou.GalleryEntry | None: ...
    def updateGalleryEntry(self, brush_node: hou.Node | None, brush_info: _BrushInfo) -> hou.GalleryEntry:
        """ Add or update an entry to a given brush gallery.
        """
    def removeGalleryEntry(self, brush_info: _BrushInfo) -> None: ...
    def galleryEntryType(self, gentry: hou.GalleryEntry) -> str:
        """ Returns the gallery entry type.
        """
    def encodeMetaData(self, brush_info: _BrushInfo) -> list[str]:
        """ Create some meta data for a brush info object.
            Note: The meta data is persisted in a gallery entry with
                  hou.GalleryEntry.setKeyword. We use an array of
                  key/value pairs to encode the brush info. The
                  dictionary/pickle approach didn't work as
                  hou.GalleryEntry is doing some trimming when
                  reloading the keyword data which ruins the pickle
                  value.
        """
    def decodeMetaData(self, gentry: hou.GalleryEntry) -> _BrushMetaData:
        """ Decode the meta data previously encoded with encodeMetaData.

            Return a dictionary containing the meta data.
        """

class Utils:
    @staticmethod
    def hdaDefinitions(filepath: str) -> Iterator[hou.HDADefinition]: ...
    @staticmethod
    def removeFile(file: str | os.PathLike[str]) -> None: ...
    @staticmethod
    def makeBrushLabel(node_type: hou.OpNodeType, brush_info: Mapping[str, object]) -> str: ...
    @staticmethod
    def logGalleryEntry(gentry: hou.GalleryEntry, title: str = '>', full: bool = True, printer: pprint.PrettyPrinter | None = None) -> None: ...
    @staticmethod
    def logGalleryEntryParms(title: str, entry: hou.GalleryEntry) -> None: ...
    @staticmethod
    def logGalleries(title: str = 'Galleries', full: bool = True, printer: pprint.PrettyPrinter | None = None) -> None: ...
    @staticmethod
    def logGallery(gallery: hou.Gallery, title: str = 'Gallery', full: bool = True, printer: pprint.PrettyPrinter | None = None) -> None: ...
    @staticmethod
    def logBrushInfo(brush_info: _BrushInfo, title: str = 'Brush Info', gm: BrushGalleryManager | None = None, full: bool = True, printer: pprint.PrettyPrinter | None = None) -> None: ...
    @staticmethod
    def logBrushInfoEntry(brush_info: Mapping[str, object], entries: Iterable[str]) -> None: ...
    @staticmethod
    def logBrushInfoCache(cache: Mapping[str, _BrushInfo], title: str = 'Brush info cache', gm: BrushGalleryManager | None = None, full: bool = False, keys: Iterable[str] | None = None) -> None: ...
    @staticmethod
    def logError(err_msg: str) -> None: ...
    @staticmethod
    def error(err_msg: str) -> str: ...
