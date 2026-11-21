# Houdini stubs generated from Houdini 22.0.466

import hou
from enum import Enum as Enum, StrEnum

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

def normalizeToTuple(p: _Point | float, dims: int, *, pad_value: float = 0.0, min_len: int | None = None) -> tuple[float, ...]:
    """ Helper used for normalizing cop space API arguments.
        Convert `p` (tuple/list or hou.Vector2/3) to a `dims`
        tuple of floats. Truncates extra components if necessary. 

        - If `min_len` is set, require at least that many components.
        - Pads with `pad_value` if too short.
    """
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
def imageToSpace(layer: hou.ImageLayer | None, image_pos: _Point, target_space: str | int | Space | None = None) -> tuple[float, ...]:
    """
    Convert an image position into the specified layer space and return 
    it as a 3-tuple (x, y, z).

    Args:
        layer (hou.ImageLayer | None): 
            The target image layer. If None, the image position 
            is returned unchanged.
        image_pos (tuple | hou.Vector2 | hou.Vector3): 
            The position in image space to convert.
        target_space (str | int | Space | None): 
            Target space identifier. Can be a string key/alias, 
            an integer index, or None for the default.

    Returns:
        tuple[float, float, float]: 
            The converted coordinates in the requested layer space.
    """
def spaceToImage(layer: hou.ImageLayer | None, pos: _Point, src_space: str | int | Space | None) -> tuple[float, ...]:
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
