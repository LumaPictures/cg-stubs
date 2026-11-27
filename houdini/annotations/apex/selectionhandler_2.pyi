from collections.abc import Iterable, Sequence
from typing import TypeAlias, TypeVar

import hou
import resourceutils as ru
from houtypes import ViewerStateEventKwargs

_PrimsT = TypeVar("_PrimsT", bound=Sequence[hou.Prim])

class AttribMapCache:
    geo: hou.Geometry
    query_attrib: str
    data_id: tuple[int, ...]
    # Each value of the prim attribute to the number of the first prim with it.
    query_attrib_map: dict[str, int]

class DrawableSelector(ru.DrawableSelector):
    query_attrib: str
    # The control paths under the cursor (located), or the one picked by a single locate.
    pre_selection: list[str] | str | None
    pre_selection_prims: dict[hou.SimpleDrawable | hou.AdvancedDrawable, list[hou.Prim] | tuple[hou.Prim, ...]]
    pre_selection_paths: dict[hou.SimpleDrawable | hou.AdvancedDrawable, list[str]]
    ctrl_paths: list[str]
    selection: list[str] | list[list[str] | str | None]
    selection_prims: dict[hou.SimpleDrawable | hou.AdvancedDrawable, list[hou.Prim] | tuple[hou.Prim, ...]]
    intersect_pos: hou.Vector3
    is_skin_selector: bool
    rig_paths: list[str]
    attrib_map_caches: dict[int, AttribMapCache]
    def __init__(
        self,
        scene_viewer: hou.SceneViewer,
        drawables: Iterable[hou.SimpleDrawable | hou.AdvancedDrawable],
        query_attrib: str,
        is_skin_selector: bool = ...,
        make_select_region_drawable: bool = ...,
    ) -> None: ...
    @property
    def drawables(self) -> list[hou.SimpleDrawable | hou.AdvancedDrawable]: ...
    @drawables.setter
    def drawables(self, drawables: list[hou.SimpleDrawable | hou.AdvancedDrawable]) -> None: ...
    def getSkinControlValues(
        self, sel_obj: hou.Selection, geo: hou.Geometry, drawable_index: int
    ) -> tuple[list[str], list[hou.Prim]]: ...
    # Skin selectors return new lists; otherwise the given prims come back as they are.
    def getPrimControlValues(
        self, prims: _PrimsT, drawable_index: int = ...
    ) -> tuple[list[str], list[hou.Prim] | _PrimsT]: ...
    def getPrimControlValue(self, prim: hou.Prim, drawable_index: int = ..., absolute_path: bool = ...) -> str | None: ...
    def startBoxSelect(self, ui_event: hou.ViewerEvent) -> None: ...
    # These three return the number of controls selected, not a bool.
    def onLocateBoxSelection(self, kwargs: ViewerStateEventKwargs, box_select_results: ru.BoxSelectResult) -> int: ...
    def onBoxSelection(self, kwargs: ViewerStateEventKwargs, result: ru.BoxSelectResult) -> int: ...
    def onLocateSingleSelection(self, kwargs: ViewerStateEventKwargs, result: ru.SingleSelectResult) -> bool: ...
    def onSingleSelection(self, kwargs: ViewerStateEventKwargs, result: ru.SingleSelectResult) -> int: ...
    def _intersectSingleSelection(
        self, kwargs: ViewerStateEventKwargs, result: ru.SingleSelectResult, precise: bool = ...
    ) -> tuple[str | None, hou.Vector3]: ...
    def performSingleSelect(
        self, kwargs: ViewerStateEventKwargs, ui_event: hou.ViewerEvent
    ) -> tuple[str | None, hou.Vector3]: ...
    def getDragLocate(self, kwargs: ViewerStateEventKwargs) -> bool: ...
    def getAllowSelectDrag(self, kwargs: ViewerStateEventKwargs) -> bool: ...

SelectionRegionDrawable: TypeAlias = ru.SelectionRegionDrawable
