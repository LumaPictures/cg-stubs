import enum
from enum import Enum

class DraggerMode(Enum):
    """ Specifies the type of drag interaction.

        Used to determine how parameter values or drawables 
        are updated in response to mouse input.
    """
    PARAM2D = enum.auto()
    PARAM_UNIFORM = enum.auto()
    ROTATE = enum.auto()

class DraggerTransformMode(Enum):
    """ Specifies how the active transform is initialized and 
        applied.

        This controls whether the drag affects parameter values, 
        the drawable's transform, or neither (custom logic).
    """
    DRAWABLE = enum.auto()
    PARAMS = enum.auto()
    CUSTOM = enum.auto()
