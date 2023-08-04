# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import NodegraphAPI as NodegraphAPI
import RenderingAPI as RenderingAPI
import Utils as Utils
import Utils.UndoStack
import _CatalogItemProjectSettings
from CatalogItem import CatalogItem as CatalogItem
from typing import ClassVar, Set, Tuple

kPrimaryView: int
kSecondaryView: int

class _CatalogItemProjectSettings:
    class _GSV(tuple):
        _field_defaults: ClassVar[dict] = ...
        _fields: ClassVar[tuple] = ...
        _fields_defaults: ClassVar[dict] = ...
        def __init__(self, _cls, name, value, enabled) -> None: ...
        def _asdict(self): ...
        @classmethod
        def _make(cls, iterable): ...
        def _replace(self, _self, **kwds): ...
        def __getnewargs__(self): ...
        @property
        def enabled(self): ...
        @property
        def name(self): ...
        @property
        def value(self): ...
    def __init__(self, catalogItem: CatalogItem) -> None: ...
    @staticmethod
    def gsvsToString(gsvs: list[_CatalogItemProjectSettings._GSV]) -> str: ...
    @property
    def gsvs(self): ...
    @property
    def startFrame(self): ...

class _ClientSlotUpdateUndoEntry(Utils.UndoStack.UndoEntry):
    def __init__(self, clientKey: int, view: int, prevCatalogItem: CatalogItem, newCatalogItem: CatalogItem) -> None: ...
    def _ClientSlotUpdateUndoEntry__setClientCatalogItem(self, catalogItem: CatalogItem): ...
    def redo(self): ...
    def undo(self): ...

class _RootNodeProjectSettings:
    def __init__(self, rootNode: NodegraphAPI.GroupNode) -> None: ...
    @staticmethod
    def _RootNodeProjectSettings__canMatchGSV(param: NodegraphAPI.Parameter, gsv: _CatalogItemProjectSettings._GSV) -> bool: ...
    def applyCatalogItemFrameTime(self, catalogItemProjectSettings: _CatalogItemProjectSettings): ...
    def applyCatalogItemGSVs(self, catalogItemProjectSettings: _CatalogItemProjectSettings) -> list[_CatalogItemProjectSettings._GSV]: ...

def ApplyCatalogItemProjectSettings(catalogItem: CatalogItem): ...
def AutoViewCatalogItem(catalogItem): ...
def CreateCatalogClientKey(): ...
def DeleteCatalogClientKey(clientKey): ...
def GetAllowedViewSlots(): ...
def GetClientCatalogItems(clientKey): ...
def GetClientKeys(): ...
def GetClientViewSlots(clientKey): ...
def GetCurrentlyViewedSlots(): ...
def GetPrimaryClientKey(): ...
def GetRecommendedRenderSlots(nodeNames): ...
def GetUnassignedSlot(): ...
def IsClientPinned(clientKey: int) -> bool: ...
def SetClientCatalogItem(clientKey: int, view: int, catalogItem: CatalogItem.CatalogItem | None, isUndoable: bool = ...): ...
def SetClientPinned(clientKey: int, isPinned: bool): ...
def SetClientViewSlot(clientKey, view, slot): ...
def SwapClientViewSlots(clientKey): ...
