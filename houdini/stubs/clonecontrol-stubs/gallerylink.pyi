# Houdini stubs generated from Houdini 22.0.466

import hou
import typing
from typing import Literal

@typing.overload
def getRenderGallery(lopnet: hou.Node | None = ..., can_switch_tabs: bool = ..., can_create_new: Literal[True] = ...) -> hou.RenderGallery: ...
@typing.overload
def getRenderGallery(lopnet: hou.Node | None = ..., can_switch_tabs: bool = ..., can_create_new: bool = ...) -> hou.RenderGallery | None: ...
def openCloneInGallery(clone: hou.clone.Connection) -> bool: ...
