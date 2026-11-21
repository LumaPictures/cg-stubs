from typing import TypeAlias

import hou

_Point: TypeAlias = hou.Vector2 | hou.Vector3 | tuple[float, ...] | list[float]

BUFFER: Space
IMAGE: Space
LOCAL: Space
PIXEL: Space
TEXTURE: Space
WORLD: Space
SPACE_ORDER: list[Space]
SPACE_INDEX: dict[Space, int]
SPACE_NAMES: list[str]
FIRST_SPACE: int
LAST_SPACE: int

def normalizeToTuple(p: _Point | float, dims: int, *, pad_value: float = ..., min_len: int | None = ...) -> tuple[float, ...]: ...
def space(value: Space | str | int) -> Space: ...
def spaceIndex(key: str | int | Space) -> int: ...
def imageToSpace(layer: hou.ImageLayer | None, image_pos: _Point, target_space: str | int | Space | None = ...) -> tuple[float, ...]: ...
def spaceToImage(layer: hou.ImageLayer | None, pos: _Point, src_space: str | int | Space | None) -> tuple[float, ...]: ...
