import hou
from collections.abc import Iterable
from houtypes import ViewerStateDrawKwargs
from kinefx import attribwatcher as attribwatcher, rigapi as rigapi
from kinefx.attribwatcher import AttributeWatcher as _AttributeWatcher
from typing import ClassVar, TypeAlias

from typing import TypeAlias
AttributeWatcher: TypeAlias = _AttributeWatcher
scale_comp_strings: list[str]
transform_components: list[str]

def formatVector(v: Iterable[float]) -> str: ...

class kinefxJointDataDrawable:
    scene_viewer: hou.SceneViewer
    panel: hou.EnumValue[hou.hudPanel]
    watcher: _AttributeWatcher
    compute_local: hou.SopVerb
    base_template: ClassVar[hou._HudTemplate]
    hud_visible: bool
    def __init__(self, scene_viewer: hou.SceneViewer, pt: hou.Point | None = None) -> None: ...
    def show(self, on: bool) -> None: ...
    @property
    def visible(self) -> bool: ...
    @property
    def pt(self) -> hou.Point | None: ...
    @pt.setter
    def pt(self, pt: hou.Point | None) -> None: ...
    def draw(self, kwargs: ViewerStateDrawKwargs) -> None: ...
