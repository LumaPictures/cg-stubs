from collections.abc import Iterable
from typing import ClassVar, TypeAlias

import hou
from houtypes import ViewerStateDrawKwargs
from kinefx.attribwatcher import AttributeWatcher as _AttributeWatcher

scale_comp_strings: list[str]
transform_components: list[str]
AttributeWatcher: TypeAlias = _AttributeWatcher

def formatVector(v: Iterable[float]) -> str: ...

class kinefxJointDataDrawable:
    base_template: ClassVar[hou._HudTemplate]
    scene_viewer: hou.SceneViewer
    panel: hou.EnumValue[hou.hudPanel]
    watcher: _AttributeWatcher
    compute_local: hou.SopVerb
    def __init__(self, scene_viewer: hou.SceneViewer, pt: hou.Point | None = ...) -> None: ...
    def show(self, on: bool) -> None: ...
    @property
    def visible(self) -> bool: ...
    @property
    def pt(self) -> hou.Point | None: ...
    @pt.setter
    def pt(self, pt: hou.Point | None) -> None: ...
    # The kwargs are unused.
    def draw(self, kwargs: ViewerStateDrawKwargs) -> None: ...
