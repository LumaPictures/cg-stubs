import hou
import typing
from enum import Enum as Enum, StrEnum
from typing import Literal

from typing import TypeAlias
from typing import TypeAlias
_Point: TypeAlias = hou.Vector2 | hou.Vector3 | tuple[float, ...] | list[float]
BUFFER: Space
IMAGE: Space
LOCAL: Space
PIXEL: Space
TEXTURE: Space
WORLD: Space

class Space(StrEnum):
    BUFFER = 'buffer'
    IMAGE = 'image'
    LOCAL = 'local'
    PIXEL = 'pixel'
    TEXTURE = 'texture'
    WORLD = 'world'

SPACE_ORDER: list[Space]
SPACE_INDEX: dict[Space, int]
SPACE_NAMES: list[str]
FIRST_SPACE: int
LAST_SPACE: int

@typing.overload
def normalizeToTuple(p: _Point | float, dims: Literal[1], *, pad_value: float = ..., min_len: int | None = ...) -> tuple[float]: ...
@typing.overload
def normalizeToTuple(p: _Point | float, dims: Literal[2], *, pad_value: float = ..., min_len: int | None = ...) -> tuple[float, float]: ...
@typing.overload
def normalizeToTuple(p: _Point | float, dims: Literal[3], *, pad_value: float = ..., min_len: int | None = ...) -> tuple[float, float, float]: ...
@typing.overload
def normalizeToTuple(p: _Point | float, dims: int, *, pad_value: float = ..., min_len: int | None = ...) -> tuple[float, ...]: ...
def space(value: Space | str | int) -> Space:
    """ Return a Space enum value from any supported input type.

        Accepts: 
        - Space enum
        - string name (Space enum name or alias)
        - integer index (0: for first, -1 for last Space enum)
    """
def spaceIndex(key: str | int | Space) -> int:
    """
    Resolve a cop space to its index.

    Args:
        key (str|int|Space):
            - space name (including alias)
            - integer flag:
                0: first index
               -1: last index
            - Space enum

    Returns:
        int: The resolved space index.
    """
@typing.overload
def imageToSpace(layer: hou.ImageLayer | None, image_pos: _Point, target_space: str | int | Space) -> tuple[float, float, float]: ...
@typing.overload
def imageToSpace(layer: None, image_pos: _Point, target_space: None = ...) -> tuple[float, float, float]: ...
@typing.overload
def imageToSpace(layer: hou.ImageLayer | None, image_pos: _Point, target_space: None = ...) -> tuple[float, float, float] | tuple[()]: ...
def spaceToImage(layer: hou.ImageLayer | None, pos: _Point, src_space: str | int | Space | None) -> tuple[float, float, float]:
    """ Convert a position from the given layer space into IMAGE 
        space.
    Args:
        layer (hou.ImageLayer | None): 
            The source image layer. If None, the input 
            coordinates are assumed to already be in IMAGE space.
        pos (tuple | hou.Vector2 | hou.Vector3): 
            Coordinates in the source layer space.
        src_space (Space): 
            Source space identifier.
    Returns:
        tuple[float, float, float] coordinates in IMAGE space.
    """
