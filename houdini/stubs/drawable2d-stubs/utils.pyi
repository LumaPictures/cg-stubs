# Houdini stubs generated from Houdini 22.0.466

import hou
import typing
from collections.abc import Iterable, Mapping, Sequence
from cop.spaceutils import Space
from drawable2d.spaceadaptor import SpaceAdaptor as SpaceAdaptor
from houtypes import ViewerParmProperties
from typing import Callable as Callable, Generic, Literal, Protocol

from typing import TypeAlias
from typing import TypeVar
from typing import TypeAlias
from typing import TypeVar
_V = TypeVar('_V')
_T = TypeVar('_T')
_ParmValue: TypeAlias = bool | int | float | str | list[int] | list[float] | list[str] | dict[str, str] | hou.Ramp | hou.Geometry | None
_ParmInput: TypeAlias = hou.ParmArgType | Sequence[float] | Sequence[str]
class _ModeControl(Protocol):
    def show(self, value: bool, /) -> None: ...

class _HandleOwner(Protocol):
    _handle_obj: hou.Handle
    def isModeEnabled(self, mode_name: str, /) -> bool: ...
    def handleByName(self, mode_name: str, /) -> _ModeControl | None: ...
    def setActiveHandle(self, control: _ModeControl, /) -> None: ...
    def activeHandle(self) -> _ModeControl | None: ...
    def onModeChanged(self, mode_name: str, index: int, /, undo_handle_mode: bool) -> None: ...
    def currentSpace(self) -> Space | None: ...

class HandleController:
    """ Manages cycling and switching between named handle modes.

        This class tracks and updates the active mode used by a 
        handle, such as sidefx_transform2d.ROTATE, TRANSLATE, or 
        SCALE. It provides utilities to cycle through available 
        modes, check whether a mode is enabled, and activate a 
        mode by name or index.

        It operates in coordination with a handle object that 
        exposes an interface for managing mode controls, visibility, 
        and state. HandleController assumes that each mode is 
        associated with a control visual object (e.g., a 
        DrawableGroup2D or Drawable2D) and that the handle provides 
        access to these controls.

        Args:
            owner: An object implementing the required control 
                   interface. This is typically the object 
                   implementing the handle.
            modes: Ordered list of supported mode names.

        Expected handle interface:
            isModeEnabled(mode_name: str) -> bool
            handleByName(mode_name: str) -> object
            setActiveHandle(control: object) -> None
            activeHandle() -> object
            onModeChanged(mode_name: str, index: int) -> None  (optional)
            currentSpace() -> cop.Space
    """
    def __init__(self, owner: _HandleOwner, modes: Sequence[str], space_handle_mode: Mapping[Space, Sequence[str]]) -> None: ...
    def currentMode(self) -> str: ...
    def _currentIndex(self) -> int: ...
    def _setCurrentIndex(self, index: int) -> None: ...
    def setCurrentModeFromSpace(self, space_name: Space, visible: bool = True) -> bool: ...
    def setCurrentMode(self, mode_name: str | int, visible: bool = True, undo_handle_mode: bool = False) -> bool:
        """ Attempt to set the mode by name. If not successful,
            fall back to the next available mode.

        Args:
            mode_name: The desired mode to set.
            visible: Whether to make the group visible.

        Returns:
            bool: True if mode was successfully set.
        """
    def isCurrentMode(self, mode_name: str | int) -> bool: ...
    def isModeEnabled(self, mode_name: str | int) -> bool: ...
    def nextMode(self) -> str:
        ''' Return the next enabled handle mode, cycling 
            through HandleModeController.MODES starting from the 
            current index + 1.
        Returns:
            str: Name of the next enabled mode or "" if none found.
        '''
    def nextEnabledMode(self, mode_name: str | int) -> str | int: ...
    def _modeByIndex(self, index: int) -> str:
        ''' Return the handle mode name corresponding to the given 
            index.

        Args:
            index (int): Index to query.

        Returns:
            str: Mode name if the group is enabled, else "".

        Raises:
            ValueError: If the index is out of range.
        '''
    def _indexByMode(self, mode_name: str | int) -> int:
        """ Return the index for a given mode name.

        Args:
            mode_name (str or int): Mode name to look up.

        Returns:
            int: Index of the mode, or 0 if not found.
        """
    def modeName(self, mode_name: str | int) -> str: ...

class AxisTracker:
    """ Tracks the dominant drag direction (X or Y) during a mouse 
        drag.

        If an angle is set using `setAngle(degrees)`, the tracker 
        compares movement along that angle and its perpendicular. 
        If no angle is set, it falls back to screen-space X/Y 
        detection.
    """
    _active_axis: Literal['x', 'y'] | None
    def __init__(self) -> None: ...
    def setAngle(self, angle_degrees: float) -> None:
        """ Set the angle (in degrees) to define the primary drag 
            axis.
        """
    def onMouseDown(self, ui_event: hou.UIEvent) -> None: ...
    def onMouseMove(self, ui_event: hou.UIEvent) -> None: ...
    def axis(self) -> Literal['x', 'y'] | None: ...
    def reset(self) -> None: ...

class MenuMapping(Generic[_V]):
    """ Maps menu keys to values, with a default fallback.
        Keys serve as menu tokens (label = key). Provides lookup
        by key or by index, and a menu item info list for
        handle settings.
    """
    def __init__(self, entries: Sequence[tuple[str, _V]], default_key: str) -> None:
        """
        Args:
            entries: list of (key, value) tuples.
            default_key: key returned when lookup misses.
        """
    def get(self, key_or_index: object) -> _V: ...
    def value(self, key: str) -> _V: ...
    def valueAt(self, index: int) -> _V: ...
    @typing.overload
    def menuItemInfo(self, use_value_as_label: Literal[False] = ...) -> list[tuple[str, str]]: ...
    @typing.overload
    def menuItemInfo(self, use_value_as_label: Literal[True]) -> list[tuple[str, _V]]: ...
    def defaultValue(self) -> str: ...

def buildTransform2D(x: float = 0.0, y: float = 0.0, z: float = 0.0, r: float = 0, s: float | None = None, sx: float = 1.0, sy: float = 1.0) -> hou.Matrix4:
    """ Builds a transform matrix as a hou.Matrix4. Typically used
        for building a 2D transform matrix with origin at x,y,z=0.
        x,y,z:    translation values.
        r:      degree angle of rotation around 'z'
        s:      Scaling value. If None, sx and sy are used 
                instead.
        sx:     x scaling value
        sy:     y scaling value
    """
def addToDrawablePos(d: hou.Drawable2D, x: float, y: float) -> None:
    """ Increments the position of a hou.Drawable2D object by given 
        X and Y values.

    This function updates the drawable's current position by adding 
    the specified x and y values to its existing X and Y coordinates, 
    respectively. It directly modifies the drawable object's position 
    in-place.

    d: The drawable object whose position is to be incremented.
    x: The value to add to the drawable's X position.
    y: The value to add to the drawable's Y position.
    """
def setDrawablePos(d: hou.Drawable2D, x: float, y: float) -> None:
    """ Sets the position of a hou.Drawable2D object to the given 
        X and Y values.

    This function updates the drawable's current position by 
    assigning the specified x and y values to its X and Y 
    coordinates, respectively. It directly modifies the 
    drawable object's position in-place.

    d: The drawable object whose position is to be incremented.
    x: The new X position for the drawable.
    y: The new Y position for the drawable.
    """
def addToDrawablePoint(d: hou.Drawable2D, index: int, x: float, y: float) -> None:
    """ Increments the coordinates of a specific point on a 
        hou.Drawable2D object.

    This function updates a particular point within the drawable
    by adding the specified x and y values to its existing 
    coordinates. It directly modifies the drawable object's 
    point data in-place.

    d: The drawable object whose point is to be incremented.
    index: The zero-based index of the point to modify. For 
            example, for a line, index 0 refers to the first 
            point, and index 1 refers to the second (last) 
            point.
    x: The value to add to the point's X coordinate.
    y: The value to add to the point's Y coordinate.
    """
def setDrawablePoint(d: hou.Drawable2D, index: int, x: float, y: float) -> None:
    """ Sets the coordinates of a specific point on a hou.Drawable2D 
        object.

    This function updates a particular point within the drawable
    by assigning the specified x and y values to its coordinates.
    It directly modifies the drawable object's point data in-place.

    d: The drawable object whose point is to be set.
    index: The zero-based index of the point to modify. For 
            example, for a line, index 0 refers to the first 
            point, and index 1 refers to the second (last) point.
    x: The new X coordinate for the point.
    y: The new Y coordinate for the point.
    """
def angleFromPoints(x: float, y: float, cx: float, cy: float, axis_angle: float = 0, degrees: bool = True) -> float:
    """
    Computes the angle from the center to the point, relative to 
    an optional rotated axis.

    Parameters:
        x, y:       Coordinates of the point (e.g. mouse).
        cx,cy:      Coordinates of the center (e.g. circle center).
        axis_angle: Angle in degrees of the reference axis 
                    (default is 0 for X-axis).
        degrees:    If True, returns angle in degrees; otherwise 
                    in radians.
    Returns:
        Angle in degrees or radians, clamped to [0, 360) or 
        [0, 2 pi).
    """
def angleDiff(a1: float, a2: float) -> float:
    """ Calculates the shortest signed angular difference between 
        two angles in degrees.

        This function computes the angular difference (a1 - a2) 
        and normalizes it to ensure the result is within the 
        range (-180, 180] degrees. 

        Args:
            a1 (float or int): The first angle in degrees.
            a2 (float or int): The second angle in degrees.

        Returns:
            float: The shortest signed angular difference in 
                   degrees, normalized to the range (-180, 180].
    """
def pointOnCircle(x: float, y: float, cx: float, cy: float, radius: float) -> tuple[float, float]:
    """
    Returns the (x, y) position on the circle's perimeter that 
    lies in the direction of the x,y position.

    x, y:   Position in 2D space.
    cx, cy: Center of the circle.
    radius: Radius of the circle.

    Returns:
        (x, y): Closest point on the circle in the direction of 
                the x,y position.
    """
def pointOnCircleFromAngle(cx: float, cy: float, radius: float, angle_deg: float) -> tuple[float, float]:
    """
    Return a point on the circumference of a circle at a given angle.

    Parameters:
        cx, cy: Center of the circle.
        radius: Radius of the circle.
        angle_deg: Angle in degrees.

    Returns:
        tuple[float, float]: (x, y) coordinates of the point on 
        the circle.
    """
def moveAlongAxis(angle_deg: float, dx: float, dy: float, axis: str = 'x') -> hou.Vector2:
    """ Computes translation along an axis (X or Y) rotated by 
        angle_deg using mouse delta.

        Returns hou.Vector2 set with the dragged x,y values 
    """
def isAlmostEqual(a: float, b: float, *, rel_tol: float = 1e-09, abs_tol: float = 0.0) -> bool:
    """
    Compares two floats for approximate equality using math.isclose 
    logic. Equivalent to 'a == b' but accounts for floating-point 
    inaccuracies.

    Args:
        a: The first float.
        b: The second float.
        rel_tol: The relative tolerance.
        abs_tol: The absolute tolerance.

    Returns:
        True if the floats are approximately equal, False otherwise.
    """
def isLessThan(a: float, b: float, *, tol: float = 1e-09) -> bool:
    """
    Compares if 'a' is strictly less than 'b', considering a tolerance.
    This means 'b' must be greater than 'a' by more than the tolerance.

    Args:
        a: The first float.
        b: The second float.
        tol: The absolute tolerance.

    Returns:
        True if 'a' is less than 'b' by more than 'tol', False 
        otherwise.
    """
def isLessThanOrEqual(a: float, b: float, *, tol: float = 1e-09) -> bool:
    """
    Compares if 'a' is less than or approximately equal to 'b', 
    considering a tolerance.

    Args:
        a: The first float.
        b: The second float.
        tol: The absolute tolerance.

    Returns:
        True if 'a' is less than or approximately equal to 'b', 
        False otherwise.
    """
def isGreaterThan(a: float, b: float, *, tol: float = 1e-09) -> bool:
    """
    Compares if 'a' is strictly greater than 'b', considering a 
    tolerance. This means 'a' must be greater than 'b' by more 
    than the tolerance.

    Args:
        a: The first float.
        b: The second float.
        tol: The absolute tolerance.

    Returns:
        True if 'a' is greater than 'b' by more than 'tol', False 
        otherwise.
    """
def isGreaterThanOrEqual(a: float, b: float, *, tol: float = 1e-09) -> bool:
    """
    Compares if 'a' is greater than or approximately equal to 'b', 
    considering a tolerance.

    Args:
        a: The first float.
        b: The second float.
        tol: The absolute tolerance.

    Returns:
        True if 'a' is greater than or approximately equal to 'b', 
        False otherwise.
    """

class ParmWrapper:
    """ Simple wrapper to access parameters by name. Primarily 
        used to abstract parameter access for Dragger2D.

        The parameters are either a dictionary of parameters with
        a format similar to the handle parameters. Can also support
        node parameters access.

        - Tries parameter dict first (if enabled).
        - Falls back to node parameters (if node is supplied).
        - Supports dict-style access via [].
        - Provides value() and setValue() helpers.
    """
    def __init__(self, parms: Mapping[str, ViewerParmProperties], *, node: hou.CopNode | None = None) -> None: ...
    def node(self) -> hou.CopNode | None: ...
    def parm(self, name: str) -> ViewerParmProperties | hou.Parm | None:
        """ Return parm object if enabled, else fallback to node 
            parm.
        """
    def nodeParm(self, name: str) -> hou.Parm | None:
        """ Return the node parm.
        """
    def __getitem__(self, name: str) -> ViewerParmProperties | hou.Parm | None: ...
    @typing.overload
    def value(self, name: str) -> _ParmValue: ...
    @typing.overload
    def value(self, name: str, def_val: _T) -> _ParmValue | _T: ...
    def setValue(self, name: str, value: _ParmInput, increment: bool = False) -> None:
        """ Set the parameter to the given value.
        """
    def increment(self, name: str, value: float) -> None:
        """ Increment value at name .
        Args:
            name:   Setting name.
            value:  Increment value.
        """
    def enable(self, name: str, value: bool = True) -> None:
        """ Enable or disable the 'name' parm.
        """
    def show(self, name: str, value: bool = True) -> None:
        """ Display or hide the parm in the UI.
        """
    @typing.overload
    @staticmethod
    def parmValue(p: ViewerParmProperties | hou.Parm | None) -> _ParmValue: ...
    @typing.overload
    @staticmethod
    def parmValue(p: ViewerParmProperties | hou.Parm | None, def_val: _T) -> _ParmValue | _T: ...
    @staticmethod
    def setParmValue(p: ViewerParmProperties | hou.Parm | None, value: _ParmInput, increment: bool = False) -> None: ...

class SettingCache:
    """ Unified settings storage for handle settings.

        Wraps a ParmWrapper-like store (_parm_settings) and adds
        per-space history for space-aware settings.

        Reads and writes always go through _parm_settings, which
        is authoritative for the current space. On switchSpace,
        the outgoing space's values are snapshotted into _data
        and the incoming space's cached values are restored into
        _parm_settings. Space-independent settings are untouched
        by space switches.

        Entry format (in _data):
            name: {'enable': int, 'value': float,
                   'visible': int, 'label': str}
    """
    def __init__(self, parm_settings: ParmWrapper, space_parm_map: Mapping[Space, Mapping[SpaceAdaptor.Role, str | Iterable[str]]], space: Space | None, undo_label: str | None = None, undo_tag: str | None = None, undo_callback: Callable[[], object] | None = None) -> None:
        """
        Args:
            parm_settings:  ParmWrapper settings object for
                            persistent storage and UI updates.
            space_parm_map: dict mapping space names to
                            {role: parm_name(s)}.
                            e.g. {cop.IMAGE: {POS: (HPX, HPY, HPZ),
                                              ROT: HPRZ}}
            space:          Initial active space.
        """
    def space(self) -> Space | None:
        """ Return the current active space.
        """
    def setSpace(self, space: Space | None) -> None:
        """ Set the current active space without snapshot/restore.
            Use switchSpace() to migrate values across spaces.
        """
    @typing.overload
    def value(self, name: str) -> _ParmValue: ...
    @typing.overload
    def value(self, name: str, def_val: _T) -> _ParmValue | _T: ...
    def setValue(self, name: str, value: _ParmInput, increment: bool = False, undo: bool = False) -> None:
        """ Set value for name in _parm_settings.
            For space-aware settings, _data is refreshed on
            switchSpace, not here.
        Args:
            name:      Setting name.
            value:     New value.
            increment: If True, add to existing value.
        """
    def __getitem__(self, name: str) -> ViewerParmProperties | hou.Parm | None:
        """ Return entry for name from _parm_settings.
        """
    def __setitem__(self, name: str, entry: ViewerParmProperties) -> None:
        """ Set entry for name in _parm_settings.
        """
    def parm(self, name: str) -> ViewerParmProperties | hou.Parm | None:
        """ Return the parm entry for name from _parm_settings.
        """
    def show(self, name: str, visible: bool) -> None:
        """ Set visibility for name.
        Args:
            name:    Setting name.
            visible: True/False.
        """
    def switchSpace(self, space: Space | None) -> None:
        """ Switch to the given space.
            Snapshots the outgoing space's _parm_settings values
            into the cache, then restores the incoming space's
            cached values back into _parm_settings.
        Args:
            space: Space to switch to. If None or same as
                   current, no-op.
        """
    def reset(self) -> None:
        """ Clear all cached per-space data.
            _parm_settings is left untouched - caller is responsible
            for resetting it to the desired values.
        """
