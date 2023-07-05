# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import CatalogAPI.Client as Client
import PyUtilModule.KatanaFile as KatanaFile
import NodegraphAPI as NodegraphAPI
import Nodes2DAPI as Nodes2DAPI
import PyXmlIO as PyXmlIO
import Utils as Utils
from CatalogAPI.CatalogItem import CatalogItem as CatalogItem, _ClearItemAttrs as _ClearItemAttrs
from _typeshed import Incomplete

DEFAULT_ITEM_XML: str
RENDER_STATE_CANCELLED: str
RENDER_STATE_COMPLETED: str
RENDER_STATE_ERROR: str
RENDER_STATE_IN_PROGRESS: str
RENDER_STATE_NONE: str
_CatalogThumbnailWidth: int
_unique_counter: int

def CreateCatalogItem(itemXML: str = ...): ...
def DeleteCatalogItems(items): ...
def DuplicateCatalogItem(item): ...
def FillDragDataFromItem(mimeData, catalogItem): ...
def FindCatalogItemBySequenceID(sequenceID): ...
def FindUnlockedCatalogItemBySlot(slot: Incomplete | None = ...): ...
def GetCatalogItems(slot: Incomplete | None = ...): ...
def GetCatalogThumbnailWidth() -> int: ...
def GetFirstCatalogItem(slot: Incomplete | None = ...): ...
def GetItemFromDragData(dragData): ...
def GetLastCatalogItem(slot: Incomplete | None = ...): ...
def GetNextCatalogItem(item, slot: Incomplete | None = ...): ...
def GetNumCatalogItems(slot): ...
def GetPreviousCatalogItem(item, slot: Incomplete | None = ...): ...
def MoveCatalogItem(catalogItem, newIndex, slot: Incomplete | None = ...): ...
def MoveCatalogItemToTop(catalogItem): ...
def SetCatalogThumbnailWidth(width: int): ...
def _CreateUniqueCatalogItemID(): ...
def _GetCameraPathFromRenderSettings(nodeName: str) -> str | None: ...
def _OnRerenderCameraChanged(eventType: str | None, eventID: object, cameraType: Incomplete | None = ..., cameraPath: Incomplete | None = ...): ...
def __nodegraph_setCurrentTime_CB(args): ...
def __nodegraph_setRootNode_cb(args): ...
def __parameter_reorderChild(args): ...
def __parameter_replaceXML(args): ...
def _cacheManager_flush_CB(args): ...