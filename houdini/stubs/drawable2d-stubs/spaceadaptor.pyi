import enum
import cop.spaceutils as cop
import hou
import typing
from . import utils as utils
from collections.abc import Mapping
from drawable2d.dragger2d import Dragger2D as Dragger2D
from enum import Enum
from houtypes import ViewerParmProperties
from typing import Callable as Callable, Literal

from typing import TypeAlias
from typing import TypeVar
from typing import TypeAlias
from typing import TypeVar
_T = TypeVar('_T')
_SpaceToken: TypeAlias = str | int | cop.Space | None
_BoundParm: TypeAlias = ViewerParmProperties | hou.Parm
_PosValue: TypeAlias = float | tuple[float, ...] | list[float] | hou.Vector2 | hou.Vector3
_RoleBinding: TypeAlias = 'Mapping[SpaceAdaptor.Role, str | tuple[str | None, ...] | list[str | None]]'
_SpaceBindingSpec: TypeAlias = 'dict[str | int | cop.Space, _RoleBinding]'
_BindingSpec: TypeAlias = 'dict[str, _SpaceBindingSpec]'
class SpaceAdaptor:
    """ Encapsulates parameter handling for COP multi-space.

        SpaceAdaptor tracks how parameters map to different coordinate 
        COP spaces (local, buffer, image, pixel, texture). 

        The adaptor handles conversion into the active target space and 
        writes values back to the bound parameters.

        Conversions always follow the pattern: 
            - image -> target space.
            - target space -> image.

        NOTE: WORLD space is not supported by the adaptor. LOCAL 
              should be used instead of WORLD if possible.
    """
    class Role(Enum):
        """ Defines the parameter roles manipulated by a SpaceAdaptor.

            These roles indicate which aspect of a drawable or 
            handle is being controlled during interaction 
            (position, rotation, scaling, etc.).
        """
        POS = enum.auto()
        ROT = enum.auto()
        SCALE = enum.auto()
        USCALE = enum.auto()
        PIVOT_POS = enum.auto()
    def __init__(self, node: hou.CopNode, parm_dict: Mapping[str, ViewerParmProperties], binding_spec: _BindingSpec | list[_BindingSpec] | tuple[_BindingSpec, ...], *, space_token: _SpaceToken | None = None, validator_fn: Callable[[str], bool] | None = None, layer_xform_fn: Callable[[], hou.Matrix4] | None = None) -> None:
        '''
        Args:
            node:           COP node providing the layer.
            parm_dict:      Parameters dict.
            binding_spec:   Parameter binding specification(s).
            space_token:    Initial space to use. It\'s either a 
                            Houdini parameter name to evaluate to 
                            access the space name, or a space name.
            validator_fn:   Function validator for bound parameters.
            layer_xform_fn: Function provider for the image layer
                            transform.

        Use a dictionary to define the space bindings.        
        binding_spec structure:
        
        {
          "<binding_name>": {
              <space_key>: {
                  <role_key>: <parm>,...
              }
          }
        }
        
        binding_name: Name of the binding spec 
        space_key: COP\'s LOCAL, BUFFER, IMAGE, PIXEL, TEXTURE
        role_key: Role to parm binding
            - POS    : tuple of (x,y[,z]) parms
            - ROT    : single parm for rotation
            - SCALE  : tuple of (sx,sy) parms
            - USCALE : single parm for uniform scale
        parm: handle parm name

        Examples:
        
        1. Single spec with multiple spaces:
        binding_spec = {
            "t2d": {
                cop.LOCAL: {
                    cop.POS:   (LX, LY),
                    cop.ROT:   RZ,
                    cop.SCALE: (SX, SY),
                    cop.USCALE: S
                },
                cop.BUFFER:  {POS: (BX, BY)},
                cop.IMAGE:   {POS: (IX, IY)},
                cop.PIXEL:   {POS: (PX, PY)},
                cop.TEXTURE: {POS: (TXX, TXY)}
            }
        }
        
        2. Multiple specs 
        (e.g. spec for each parm in sidefx_tangentpivot):

        binding_spec = (
            {"TX":   {cop.IMAGE: {POS: (TX, TY)}}},
            {"TTX1": {cop.IMAGE: {POS: (TTX1, TTY1)}}},
            {"TTX2": {cop.IMAGE: {POS: (TTX2, TTY2)}}}
        )
        '''
    def name(self) -> cop.Space | None: ...
    def node(self) -> hou.CopNode | None: ...
    def bindingSpec(self, space_name: str | None = None) -> dict[cop.Space, _RoleBinding] | None:
        """ Return a binding spec for a give space.
        """
    def setActiveBindingSpec(self, name: str) -> None:
        """ Set which binding spec is currently active by name.
            Args:
                name (str): Binding spec name to activate.
        """
    def activeBindingSpec(self) -> dict[cop.Space, _RoleBinding]:
        """ Return the active binding spec dictionary.
        """
    def layer(self) -> hou.ImageLayer | None: ...
    def updateLayerFromPort(self, layer_output: bool = True, layer_port_index: int = 0) -> hou.ImageLayer | None:
        """ Pull a layer from a node/port and setting it on the adaptor.
        Args:
            layer_output: True to get the node layer going out; 
                False to get the layer of a connected node at 
                port layer_port_index.
            layer_port_index: 0-based output port index to select 
                the layer (defaults to 0). 
        Returns: The new image layer if the update is successful.
        """
    def _updateLayerTransformFunc(self, layer_xform_fn: Callable[[], hou.Matrix4] | None = None) -> Callable[[], hou.Matrix4]:
        """ Update the layer transform function proivider with 
            layer_xform_fn or with the current layer transform 
            if None.
        """
    def canSupportSpace(self, space_token: _SpaceToken) -> bool:
        """ Determine if the adaptor can support the space 
            specfied with space_token. 

            Args:
                space_token: Either a parameter name to evaluate 
                    to access the space name, or a space name.
            Returns:
                True if the space is supported, False otherwise.
        """
    def switchSpace(self, space_token: _SpaceToken) -> cop.Space | None:
        """ Set the COP layer space used by the binding.

        Args:
            space_token (str|int|Space|None): Parm name, int index, 
                string key/alias, or Space value to set as the 
                active space.
        """
    def pushSpace(self, space: _SpaceToken) -> None:
        """ Save current space and switch to new space.
        """
    def popSpace(self) -> None:
        """ Restore previously saved space.
        """
    @typing.overload
    def parms(self, role: Literal[Role.POS], space: _SpaceToken = ...) -> tuple[_BoundParm | None, _BoundParm | None, _BoundParm | None] | None: ...
    @typing.overload
    def parms(self, role: Literal[Role.PIVOT_POS, Role.SCALE], space: _SpaceToken = ...) -> tuple[_BoundParm | None, _BoundParm | None] | None: ...
    @typing.overload
    def parms(self, role: Literal[Role.ROT, Role.USCALE], space: _SpaceToken = ...) -> tuple[_BoundParm | None] | None: ...
    @typing.overload
    def parms(self, role: Role, space: _SpaceToken = ...) -> tuple[_BoundParm | None, _BoundParm | None, _BoundParm | None] | tuple[_BoundParm | None, _BoundParm | None] | tuple[_BoundParm | None] | None: ...
    @typing.overload
    def parmValue(self, role: Literal[Role.POS], *, target_space: _SpaceToken = ..., def_val: float = ...) -> tuple[float, float, float]: ...
    @typing.overload
    def parmValue(self, role: Literal[Role.PIVOT_POS, Role.SCALE], *, target_space: _SpaceToken = ..., def_val: float = ...) -> tuple[float, float]: ...
    @typing.overload
    def parmValue(self, role: Literal[Role.ROT, Role.USCALE], *, target_space: _SpaceToken = ..., def_val: float = ...) -> float: ...
    @typing.overload
    def parmValue(self, role: Role, *, target_space: _SpaceToken = ..., def_val: float = ...) -> float | tuple[float, float] | tuple[float, float, float]: ...
    def updateParm(self, role: Role, tuple_value: _PosValue | None, space: _SpaceToken | None = None, increment: bool = False) -> bool:
        """ Update bound parms for `role` using `tuple_value` 
            (interpreted in IMAGE). 
          1 - reads current parm values,
          2 - converts through IMAGE if needed,
          3 - applies absolute or incremental change,
          4 - writes back to the target space.

        Args:
            role (str): POS | ROT | SCALE | USCALE
            tuple_value (float|tuple|list|None): value(s) in IMAGE
            space (str|None): target space key/alias; defaults to current
            increment (bool): if True, add on top of current; else set

        Returns:
            bool: True if any bound parm was written.
        """
    def updateTransform(self, value: hou.Matrix4 | tuple[float, ...] | list[float], role: Role | None = None, increment: bool = False) -> None:
        """ Update this class world state from either a transform 
            matrix or direct role values.

        Args:
            value (hou.Matrix4|tuple):
                - hou.Matrix4: Full 2D/3D transform to extract T/R/S.
                - tuple: Role-specific value(s) if `role` is provided.
            role (str|None):
                If None:
                    value must be a hou.Matrix4. Updates all world
                    state components (T/R/S).
                If not None:
                    value must be a tuple matching the role:
                      - POS    -> (x, y[, z])
                      - SCALE  -> (sx, sy[, sz])
                      - ROT    -> (rx, ry, rz) or (rz,) for 2D
                      - USCALE -> (s,)
            increment (bool): If True, add on top of current state
                instead of replacing it.
        """
    @typing.overload
    def transform(self, role: None = ..., def_val: float = ...) -> hou.Matrix4: ...
    @typing.overload
    def transform(self, role: Role, def_val: float = ...) -> tuple[float, float, float] | float: ...
    def orientTransform(self) -> hou.Matrix4:
        """ Build an orientation transform for image-aligned 
            drawables.

            This transform extracts the space transform world-space 
            rotation while neutralizing its XY translation (to 
            avoid double-applying the origin offset). The 
            Z translation is preserved so that drawables remain 
            positioned correctly in depth.

        Usage:
            Typically used when placing 2D drawables (handles, 
            guides, overlays) in a 3D scene, where they must 
            inherit the space's orientation but not its XY world 
            translation.

        Returns:
            hou.Matrix4: A transform matrix that applies the 
            space's world rotation and Z position, while keeping 
            XY centered around the local pivot.
        """
    def boundPivotDelta(self) -> tuple[float, float]:
        """ Return the bound pivot parm as an IMAGE-space delta.

            Converts the raw bound pivot parm (in the current space)
            to an offset in IMAGE space. 

        Returns:
            (dx, dy): Bound pivot offset in IMAGE space.
        """

POS: Literal[SpaceAdaptor.Role.POS]
PIVOT_POS: Literal[SpaceAdaptor.Role.PIVOT_POS]
ROT: Literal[SpaceAdaptor.Role.ROT]
SCALE: Literal[SpaceAdaptor.Role.SCALE]
USCALE: Literal[SpaceAdaptor.Role.USCALE]

class SpaceAdaptorImage:
    """ Proxy SpaceAdaptor interface used by Dragger2D for 
        parameter updates through a dragger with IMAGE space only 
        support. 

        NOTE: Make sure the class is updated when a new method 
        gets added to SpaceAdaptor or an existing one is renamed.
    """
    def __init__(self, dragger: Dragger2D) -> None: ...
    def updateTransform(self, xform: hou.Matrix4 | tuple[float, ...] | list[float]) -> None: ...
    def transform(self) -> hou.Matrix4: ...
    def updateParm(self, role: SpaceAdaptor.Role | None, tuple_value: _PosValue | None, space: _SpaceToken | None = None, increment: bool = False) -> bool: ...
    def spaceName(self) -> cop.Space: ...
    def switchSpace(self, space_token: _SpaceToken) -> cop.Space: ...
    @typing.overload
    def parms(self, role: Literal[SpaceAdaptor.Role.POS], space: _SpaceToken = ...) -> tuple[_BoundParm | None, _BoundParm | None, None]: ...
    @typing.overload
    def parms(self, role: Literal[SpaceAdaptor.Role.SCALE], space: _SpaceToken = ...) -> tuple[_BoundParm | None, _BoundParm | None]: ...
    @typing.overload
    def parms(self, role: Literal[SpaceAdaptor.Role.ROT, SpaceAdaptor.Role.USCALE], space: _SpaceToken = ...) -> _BoundParm | None: ...
    @typing.overload
    def parms(self, role: Literal[SpaceAdaptor.Role.PIVOT_POS], space: _SpaceToken = ...) -> tuple[None, None]: ...
    @typing.overload
    def parms(self, role: SpaceAdaptor.Role | None, space: _SpaceToken = ...) -> tuple[_BoundParm | None, ...] | _BoundParm | None: ...
    @typing.overload
    def parmValue(self, role: Literal[SpaceAdaptor.Role.POS], *, target_space: _SpaceToken = ..., def_val: float = ...) -> tuple[float, float, float]: ...
    @typing.overload
    def parmValue(self, role: Literal[SpaceAdaptor.Role.PIVOT_POS, SpaceAdaptor.Role.SCALE], *, target_space: _SpaceToken = ..., def_val: float = ...) -> tuple[float, float]: ...
    @typing.overload
    def parmValue(self, role: Literal[SpaceAdaptor.Role.ROT, SpaceAdaptor.Role.USCALE], *, target_space: _SpaceToken = ..., def_val: float = ...) -> float: ...
    @typing.overload
    def parmValue(self, role: None, *, target_space: _SpaceToken = ..., def_val: float = ...) -> float: ...
    @typing.overload
    def parmValue(self, role: SpaceAdaptor.Role | None, *, target_space: _SpaceToken = ..., def_val: float = ...) -> float | tuple[float, float] | tuple[float, float, float]: ...
    def posToImage(self, pos_value: _T, def_val: float) -> _T: ...
    def updateLayerFromPort(self, layer_output: bool = True, layer_port_index: int = 0) -> bool: ...
    def setActiveBindingSpec(self, name: str) -> None: ...
    def pushSpace(self, space: _SpaceToken) -> None: ...
    def popSpace(self) -> None: ...
