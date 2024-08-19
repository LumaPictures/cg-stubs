# mypy: disable-error-code="misc, override, no-redef"

import Boost.Python
import pxr.Ar
import pxr.Tf
import pxr.Usd
import typing
from _typeshed import Incomplete
from typing import Any, ClassVar, overload

MIN_ORTHO_TOLERANCE: float
MIN_VECTOR_LENGTH: float
__MFB_FULL_PACKAGE_NAME: str

class BBox3d(Boost.Python.instance):
    """
    Basic type: arbitrarily oriented 3D bounding box.


    This class represents a three-dimensional bounding box as an axis-
    aligned box ( C{GfRange3d}) and a matrix ( C{GfMatrix4d}) to transform
    it into the correct space.

    A C{GfBBox3d} is more useful than using just C{GfRange3d} instances
    (which are always axis-aligned) for these reasons:

       - When an axis-aligned bounding box is transformed several times,
         each transformation can result in inordinate growth of the bounding
         box. By storing the transformation separately, it can be applied once
         at the end, resulting in a much better fit. For example, if the
         bounding box at the leaf of a scene graph is transformed through
         several levels of the graph hierarchy to the coordinate space at the
         root, a C{GfBBox3d} is generally much smaller than the C{GfRange3d}
         computed by transforming the box at each level.

       - When two or more such bounding boxes are combined, having the
         transformations stored separately means that there is a better
         opportunity to choose a better coordinate space in which to combine
         the boxes.
         B{The Zero-area Primitives Flag}

    When bounding boxes are used in intersection test culling, it is
    sometimes useful to extend them a little bit to allow lower-
    dimensional objects with zero area, such as lines and points, to be
    intersected. For example, consider a cube constructed of line
    segments. The bounding box for this shape fits the cube exactly. If an
    application wants to allow a near-miss of the silhouette edges of the
    cube to be considered an intersection, it has to loosen the bbox
    culling test a little bit.

    To distinguish when this loosening is necessary, each C{GfBBox3d}
    instance maintains a flag indicating whether any zero-area primitives
    are contained within it. The application is responsible for setting
    this flag correctly by calling C{SetHasZeroAreaPrimitives()} . The
    flag can be accessed during intersection tests by calling
    C{HasZeroAreaPrimitives()} . This flag is set by default in all
    constructors to C{false}.
    """
    __instance_size__: ClassVar[int] = ...
    box: Range3d
    hasZeroAreaPrimitives: Incomplete
    matrix: Matrix4d
    @overload
    def __init__(self) -> None:
        '''
        The default constructor leaves the box empty, the transformation
        matrix identity, and the zero-area primitives flag" C{false}.
        '''
    @overload
    def __init__(self, _box: BBox3d, /) -> None:
        """
        This constructor takes a box and sets the matrix to identity.
        """
    @overload
    def __init__(self, _box: Range3d | list[float] | tuple[float, float, float], _matrix: Matrix4d, /) -> None:
        """
        This constructor takes a box and a transformation matrix.
        """
    @overload
    def __init__(self, arg2: Range3d | list[float] | tuple[float, float, float], /) -> None: ...
    @staticmethod
    def Combine(_b1: BBox3d, _b2: BBox3d, /) -> BBox3d:
        """
        Combines two bboxes, returning a new bbox that contains both.


        This uses the coordinate space of one of the two original boxes as the
        space of the result; it uses the one that produces whe smaller of the
        two resulting boxes.
        """
    def ComputeAlignedBox(self) -> Range3d:
        """
        Returns the axis-aligned range (as a C{GfRange3d}) that results from
        applying the transformation matrix to the axis-aligned box and
        aligning the result.


        This synonym for C{ComputeAlignedRange} exists for compatibility
        purposes.
        """
    def ComputeAlignedRange(self) -> Range3d:
        """
        Returns the axis-aligned range (as a C{GfRange3d}) that results from
        applying the transformation matrix to the wxis-aligned box and
        aligning the result.
        """
    def ComputeCentroid(self) -> Vec3d:
        """
        Returns the centroid of the bounding box.


        The centroid is computed as the transformed centroid of the range.
        """
    def GetBox(self) -> Range3d:
        """
        Returns the range of the axis-aligned untransformed box.


        This synonym of C{GetRange} exists for compatibility purposes.
        """
    def GetInverseMatrix(self) -> Matrix4d:
        """
        Returns the inverse of the transformation matrix.


        This will be the identity matrix if the transformation matrix is not
        invertible.
        """
    def GetMatrix(self) -> Matrix4d:
        """
        Returns the transformation matrix.
        """
    def GetRange(self) -> Range3d:
        """
        Returns the range of the axis-aligned untransformed box.
        """
    def GetVolume(self) -> float:
        """
        Returns the volume of the box (0 for an empty box).
        """
    def HasZeroAreaPrimitives(self) -> bool:
        '''
        Returns the current state of the zero-area primitives flag".
        '''
    @overload
    def Set(self, _box: Range3d | list[float] | tuple[float, float, float], _matrix: Matrix4d, /) -> BBox3d:
        """
        Sets the axis-aligned box and transformation matrix.
        """
    @overload
    def Set(self, arg2: Range3d | list[float] | tuple[float, float, float], arg3: Matrix4d, /) -> BBox3d: ...
    def SetHasZeroAreaPrimitives(self, _hasThem: bool, /) -> None:
        """
        Sets the zero-area primitives flag to the given value.
        """
    def SetMatrix(self, _matrix: Matrix4d, /) -> BBox3d:
        """
        Sets the transformation matrix only.


        The axis-aligned box is not modified.
        """
    def SetRange(self, _box: Range3d | list[float] | tuple[float, float, float], /) -> BBox3d:
        """
        Sets the range of the axis-aligned box only.


        The transformation matrix is not modified.
        """
    def Transform(self, _matrix: Matrix4d, /) -> BBox3d:
        """
        Transforms the bounding box by the given matrix, which is assumed to
        be a global transformation to apply to the box.


        Therefore, this just post-multiplies the box's matrix by C{matrix}.
        """
    def __eq__(self, other: object) -> bool:
        """
        Component-wise equality test.


        The axis-aligned boxes and transformation matrices match exactly for
        bboxes to be considered equal. (To compare equality of the actual
        boxes, you can compute both aligned boxes and test the results for
        equality.)
        """
    def __hash__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...

class Camera(Boost.Python.instance):
    """
    Object-based representation of a camera.


    This class provides a thin wrapper on the camera data model, with a
    small number of computations.
    """

    class FOVDirection(pxr.Tf.Tf_PyEnumWrapper):
        _baseName: ClassVar[str] = ...
        allValues: ClassVar[tuple] = ...
        def __init__(self, *args, **kwargs) -> None:
            """Raises an exception
            This class cannot be instantiated from Python
            """
        @staticmethod
        def GetValueFromName(name: str | pxr.Ar.ResolvedPath) -> Any: ...

    class Projection(pxr.Tf.Tf_PyEnumWrapper):
        _baseName: ClassVar[str] = ...
        allValues: ClassVar[tuple] = ...
        def __init__(self, *args, **kwargs) -> None:
            """Raises an exception
            This class cannot be instantiated from Python
            """
        @staticmethod
        def GetValueFromName(name: str | pxr.Ar.ResolvedPath) -> Any: ...
    APERTURE_UNIT: ClassVar[float] = ...
    DEFAULT_HORIZONTAL_APERTURE: ClassVar[float] = ...
    DEFAULT_VERTICAL_APERTURE: ClassVar[float] = ...
    FOCAL_LENGTH_UNIT: ClassVar[float] = ...
    FOVHorizontal: ClassVar[Camera.FOVDirection] = ...
    FOVVertical: ClassVar[Camera.FOVDirection] = ...
    Orthographic: ClassVar[Camera.Projection] = ...
    Perspective: ClassVar[Camera.Projection] = ...
    __instance_size__: ClassVar[int] = ...
    clippingPlanes: list[Vec4f]
    clippingRange: Range1f
    fStop: float
    focalLength: float
    focusDistance: float
    horizontalAperture: float
    horizontalApertureOffset: float
    projection: Camera.Projection
    transform: Matrix4d
    verticalAperture: float
    verticalApertureOffset: float
    @overload
    def __init__(self, transform: Matrix4d = ..., projection: Camera.Projection = ..., horizontalAperture: float = ..., verticalAperture: float = ..., horizontalApertureOffset: float = ..., verticalApertureOffset: float = ..., focalLength: float = ..., clippingRange: Range1f = ..., clippingPlanes: typing.Iterable[Vec4f | list[float] | tuple[float, float, float, float]] = ..., fStop: float = ..., focusDistance: float = ...) -> None:
        """0.0, 1.0, 0.0, 0.0,
        0.0, 0.0, 1.0, 0.0,
        0.0, 0.0, 0.0, 1.0) [, (object)projection=Gf.Camera.Perspective [, (float)horizontalAperture=20.955 [, (float)verticalAperture=15.290799999999999 [, (float)horizontalApertureOffset=0.0 [, (float)verticalApertureOffset=0.0 [, (float)focalLength=50.0 [, (Range1f)clippingRange=Gf.Range1f(1.0, 1000000.0) [, (object)clippingPlanes=[] [, (float)fStop=0.0 [, (float)focusDistance=0.0]]]]]]]]]]]) -> None"""
    @overload
    def __init__(self, arg2: Camera, /) -> None:
        """0.0, 1.0, 0.0, 0.0,
        0.0, 0.0, 1.0, 0.0,
        0.0, 0.0, 0.0, 1.0) [, (object)projection=Gf.Camera.Perspective [, (float)horizontalAperture=20.955 [, (float)verticalAperture=15.290799999999999 [, (float)horizontalApertureOffset=0.0 [, (float)verticalApertureOffset=0.0 [, (float)focalLength=50.0 [, (Range1f)clippingRange=Gf.Range1f(1.0, 1000000.0) [, (object)clippingPlanes=[] [, (float)fStop=0.0 [, (float)focusDistance=0.0]]]]]]]]]]]) -> None"""
    def GetFieldOfView(self, _direction: Camera.FOVDirection, /) -> float:
        """
        Returns the horizontal or vertical field of view in degrees.
        """
    def SetFromViewAndProjectionMatrix(self, viewMatrix: Matrix4d, projMatrix: Matrix4d, focalLength: float = ...) -> None:
        """
        Sets the camera from a view and projection matrix.


        Note that the projection matrix does only determine the ratio of
        aperture to focal length, so there is a choice which defaults to 50mm
        (or more accurately, 50 tenths of a world unit).
        """
    def SetOrthographicFromAspectRatioAndSize(self, aspectRatio: float, orthographicSize: float, direction: Camera.FOVDirection) -> None:
        """
        Sets the frustum to be orthographic such that it has the given
        C{aspectRatio} and such that the orthographic width, respectively,
        orthographic height (in cm) is equal to C{orthographicSize} (depending
        on direction).
        """
    def SetPerspectiveFromAspectRatioAndFieldOfView(self, aspectRatio: float, fieldOfView: float, direction: Camera.FOVDirection, horizontalAperture: float = ...) -> None:
        """
        Sets the frustum to be projective with the given C{aspectRatio} and
        horizontal, respectively, vertical field of view C{fieldOfView}
        (similar to gluPerspective when direction = FOVVertical).


        Do not pass values for C{horionztalAperture} unless you care about
        DepthOfField.
        """
    def __eq__(self, other: object) -> bool:
        """
        Equality operator. true iff all parts match.
        """
    def __ne__(self, other: object) -> bool: ...
    @property
    def aspectRatio(self) -> float:
        """
        Returns the projector aperture aspect ratio.
        """
    @property
    def frustum(self) -> Frustum:
        """
        Returns the computed, world-space camera frustum.


        The frustum will always be that of a Y-up, -Z-looking camera.
        """
    @property
    def horizontalFieldOfView(self): ...
    @property
    def verticalFieldOfView(self): ...

class DualQuatd(Boost.Python.instance):
    """
    Basic type: a real part quaternion and a dual part quaternion.


    This class represents a generalized dual quaternion that has a real
    part and a dual part quaternions. Dual quaternions are used to
    represent a combination of rotation and translation.

    References:
    https://www.cs.utah.edu/~ladislav/kavan06dual/kavan06dual.pdf
    http://web.cs.iastate.edu/~cs577/handouts/dual-quaternion.pdf
    """
    dual: Quatd
    real: Quatd
    @overload
    def __init__(self) -> None:
        """
        The default constructor leaves the dual quaternion undefined.
        """
    @overload
    def __init__(self, realVal: float) -> None:
        """
        Initialize the real part to C{realVal} and the imaginary part to zero
        quaternion.


        Since quaternions typically must be normalized, reasonable values for
        C{realVal} are -1, 0, or 1. Other values are legal but are likely to
        be meaningless.
        """
    @overload
    def __init__(self, real: Quatd | Quatf | Quath) -> None:
        """
        Initialize the real part to C{real} quaternion and the imaginary part
        to zero quaternion.
        """
    @overload
    def __init__(self, real: Quatd | Quatf | Quath, dual: Quatd | Quatf | Quath) -> None:
        """
        This constructor initializes the real and dual parts.
        """
    @overload
    def __init__(self, rotation: Quatd | Quatf | Quath, translation: Vec3d | list[float] | tuple[float, float, float]) -> None:
        """
        This constructor initializes from a rotation and a translation
        components.
        """
    @overload
    def __init__(self, arg2: DualQuatd | DualQuatf | DualQuath, /) -> None: ...
    def GetConjugate(self) -> DualQuatd:
        """
        Returns the conjugate of this dual quaternion.
        """
    def GetDual(self) -> Quatd:
        """
        Returns the dual part of the dual quaternion.
        """
    @staticmethod
    def GetIdentity() -> DualQuatd:
        """
        Returns the identity dual quaternion, which has a real part of
        (1,0,0,0) and a dual part of (0,0,0,0).
        """
    def GetInverse(self) -> DualQuatd:
        """
        Returns the inverse of this dual quaternion.
        """
    def GetLength(self) -> tuple[float, float]:
        """
        Returns geometric length of this dual quaternion.
        """
    def GetNormalized(self, eps: float = ...) -> DualQuatd:
        """
        Returns a normalized (unit-length) version of this dual quaternion.


        If the length of this dual quaternion is smaller than C{eps}, this
        returns the identity dual quaternion.
        """
    def GetReal(self) -> Quatd:
        """
        Returns the real part of the dual quaternion.
        """
    def GetTranslation(self) -> Vec3d:
        """
        Get the translation component of this dual quaternion.
        """
    @staticmethod
    def GetZero() -> DualQuatd:
        """
        Returns the zero dual quaternion, which has a real part of (0,0,0,0)
        and a dual part of (0,0,0,0).
        """
    def Normalize(self, eps: float = ...) -> DualQuatd:
        """
        Normalizes this dual quaternion in place.


        Normalizes this dual quaternion in place to unit length, returning the
        length before normalization. If the length of this dual quaternion is
        smaller than C{eps}, this sets the dual quaternion to identity.
        """
    def SetDual(self, _dual: Quatd | Quatf | Quath, /) -> None:
        """
        Sets the dual part of the dual quaternion.
        """
    def SetReal(self, _real: Quatd | Quatf | Quath, /) -> None:
        """
        Sets the real part of the dual quaternion.
        """
    def SetTranslation(self, _translation: Vec3d | list[float] | tuple[float, float, float], /) -> None:
        """
        Set the translation component of this dual quaternion.
        """
    def Transform(self, _vec: Vec3d | list[float] | tuple[float, float, float], /) -> Vec3d:
        """
        Transforms the row vector *vec* by the dual quaternion.
        """
    def __add__(self, arg2: DualQuatd | DualQuatf | DualQuath, /) -> Any: ...
    def __eq__(self, other: object) -> bool:
        """
        Component-wise dual quaternion equality test.


        The real and dual parts must match exactly for dual quaternions to be
        considered equal.
        """
    def __hash__(self) -> int: ...
    def __iadd__(self, arg2: DualQuatd | DualQuatf | DualQuath, /) -> Any: ...
    def __idiv__(self, arg2: float, /) -> Any: ...
    @overload
    def __imul__(self, arg2: DualQuatd | DualQuatf | DualQuath, /) -> Any: ...
    @overload
    def __imul__(self, arg2: float, /) -> Any: ...
    def __isub__(self, arg2: DualQuatd | DualQuatf | DualQuath, /) -> Any: ...
    def __itruediv__(self, arg2: float, /) -> DualQuatd: ...
    @overload
    def __mul__(self, arg2: DualQuatd | DualQuatf | DualQuath, /) -> Any: ...
    @overload
    def __mul__(self, arg2: float, /) -> Any: ...
    def __ne__(self, other: object) -> bool: ...
    def __rmul__(self, arg2: float, /) -> Any: ...
    def __sub__(self, arg2: DualQuatd | DualQuatf | DualQuath, /) -> Any: ...
    def __truediv__(self, arg2: float, /) -> Any: ...

class DualQuatf(Boost.Python.instance):
    """
    Basic type: a real part quaternion and a dual part quaternion.


    This class represents a generalized dual quaternion that has a real
    part and a dual part quaternions. Dual quaternions are used to
    represent a combination of rotation and translation.

    References:
    https://www.cs.utah.edu/~ladislav/kavan06dual/kavan06dual.pdf
    http://web.cs.iastate.edu/~cs577/handouts/dual-quaternion.pdf
    """
    dual: Quatf
    real: Quatf
    @overload
    def __init__(self) -> None:
        """
        The default constructor leaves the dual quaternion undefined.
        """
    @overload
    def __init__(self, realVal: float) -> None:
        """
        Initialize the real part to C{realVal} and the imaginary part to zero
        quaternion.


        Since quaternions typically must be normalized, reasonable values for
        C{realVal} are -1, 0, or 1. Other values are legal but are likely to
        be meaningless.
        """
    @overload
    def __init__(self, real: Quatf | Quath) -> None:
        """
        Initialize the real part to C{real} quaternion and the imaginary part
        to zero quaternion.
        """
    @overload
    def __init__(self, real: Quatf | Quath, dual: Quatf | Quath) -> None:
        """
        This constructor initializes the real and dual parts.
        """
    @overload
    def __init__(self, rotation: Quatf | Quath, translation: Vec3f | list[float] | tuple[float, float, float]) -> None:
        """
        This constructor initializes from a rotation and a translation
        components.
        """
    @overload
    def __init__(self, _other: DualQuatd | DualQuatf | DualQuath, /) -> None:
        """
        Construct from GfDualQuatd.
        """
    @overload
    def __init__(self, _other: DualQuatf | DualQuath, /) -> None:
        """
        Implicitly convert from GfDualQuath.
        """
    def GetConjugate(self) -> DualQuatf:
        """
        Returns the conjugate of this dual quaternion.
        """
    def GetDual(self) -> Quatf:
        """
        Returns the dual part of the dual quaternion.
        """
    @staticmethod
    def GetIdentity() -> DualQuatf:
        """
        Returns the identity dual quaternion, which has a real part of
        (1,0,0,0) and a dual part of (0,0,0,0).
        """
    def GetInverse(self) -> DualQuatf:
        """
        Returns the inverse of this dual quaternion.
        """
    def GetLength(self) -> tuple[float, float]:
        """
        Returns geometric length of this dual quaternion.
        """
    def GetNormalized(self, eps: float = ...) -> DualQuatf:
        """
        Returns a normalized (unit-length) version of this dual quaternion.


        If the length of this dual quaternion is smaller than C{eps}, this
        returns the identity dual quaternion.
        """
    def GetReal(self) -> Quatf:
        """
        Returns the real part of the dual quaternion.
        """
    def GetTranslation(self) -> Vec3f:
        """
        Get the translation component of this dual quaternion.
        """
    @staticmethod
    def GetZero() -> DualQuatf:
        """
        Returns the zero dual quaternion, which has a real part of (0,0,0,0)
        and a dual part of (0,0,0,0).
        """
    def Normalize(self, eps: float = ...) -> DualQuatf:
        """
        Normalizes this dual quaternion in place.


        Normalizes this dual quaternion in place to unit length, returning the
        length before normalization. If the length of this dual quaternion is
        smaller than C{eps}, this sets the dual quaternion to identity.
        """
    def SetDual(self, _dual: Quatf | Quath, /) -> None:
        """
        Sets the dual part of the dual quaternion.
        """
    def SetReal(self, _real: Quatf | Quath, /) -> None:
        """
        Sets the real part of the dual quaternion.
        """
    def SetTranslation(self, _translation: Vec3f | list[float] | tuple[float, float, float], /) -> None:
        """
        Set the translation component of this dual quaternion.
        """
    def Transform(self, _vec: Vec3f | list[float] | tuple[float, float, float], /) -> Vec3f:
        """
        Transforms the row vector *vec* by the dual quaternion.
        """
    def __add__(self, arg2: DualQuatf | DualQuath, /) -> Any: ...
    def __eq__(self, other: object) -> bool:
        """
        Component-wise dual quaternion equality test.


        The real and dual parts must match exactly for dual quaternions to be
        considered equal.
        """
    def __hash__(self) -> int: ...
    def __iadd__(self, arg2: DualQuatf | DualQuath, /) -> Any: ...
    def __idiv__(self, arg2: float, /) -> Any: ...
    @overload
    def __imul__(self, arg2: DualQuatf | DualQuath, /) -> Any: ...
    @overload
    def __imul__(self, arg2: float, /) -> Any: ...
    def __isub__(self, arg2: DualQuatf | DualQuath, /) -> Any: ...
    def __itruediv__(self, arg2: float, /) -> DualQuatf: ...
    @overload
    def __mul__(self, arg2: DualQuatf | DualQuath, /) -> Any: ...
    @overload
    def __mul__(self, arg2: float, /) -> Any: ...
    def __ne__(self, other: object) -> bool: ...
    def __rmul__(self, arg2: float, /) -> Any: ...
    def __sub__(self, arg2: DualQuatf | DualQuath, /) -> Any: ...
    def __truediv__(self, arg2: float, /) -> Any: ...

class DualQuath(Boost.Python.instance):
    """
    Basic type: a real part quaternion and a dual part quaternion.


    This class represents a generalized dual quaternion that has a real
    part and a dual part quaternions. Dual quaternions are used to
    represent a combination of rotation and translation.

    References:
    https://www.cs.utah.edu/~ladislav/kavan06dual/kavan06dual.pdf
    http://web.cs.iastate.edu/~cs577/handouts/dual-quaternion.pdf
    """
    dual: Quath
    real: Quath
    @overload
    def __init__(self) -> None:
        """
        The default constructor leaves the dual quaternion undefined.
        """
    @overload
    def __init__(self, realVal: float) -> None:
        """
        Initialize the real part to C{realVal} and the imaginary part to zero
        quaternion.


        Since quaternions typically must be normalized, reasonable values for
        C{realVal} are -1, 0, or 1. Other values are legal but are likely to
        be meaningless.
        """
    @overload
    def __init__(self, real: Quath) -> None:
        """
        Initialize the real part to C{real} quaternion and the imaginary part
        to zero quaternion.
        """
    @overload
    def __init__(self, real: Quath, dual: Quath) -> None:
        """
        This constructor initializes the real and dual parts.
        """
    @overload
    def __init__(self, rotation: Quath, translation: Vec3h | list[float] | tuple[float, float, float]) -> None:
        """
        This constructor initializes from a rotation and a translation
        components.
        """
    @overload
    def __init__(self, _other: DualQuatd | DualQuatf | DualQuath, /) -> None:
        """
        Construct from GfDualQuatd.
        """
    @overload
    def __init__(self, _other: DualQuatf | DualQuath, /) -> None:
        """
        Construct from GfDualQuatf.
        """
    @overload
    def __init__(self, arg2: DualQuath, /) -> None: ...
    def GetConjugate(self) -> DualQuath:
        """
        Returns the conjugate of this dual quaternion.
        """
    def GetDual(self) -> Quath:
        """
        Returns the dual part of the dual quaternion.
        """
    @staticmethod
    def GetIdentity() -> DualQuath:
        """
        Returns the identity dual quaternion, which has a real part of
        (1,0,0,0) and a dual part of (0,0,0,0).
        """
    def GetInverse(self) -> DualQuath:
        """
        Returns the inverse of this dual quaternion.
        """
    def GetLength(self) -> tuple[float, float]:
        """
        Returns geometric length of this dual quaternion.
        """
    def GetNormalized(self, eps: float = ...) -> DualQuath:
        """
        Returns a normalized (unit-length) version of this dual quaternion.


        If the length of this dual quaternion is smaller than C{eps}, this
        returns the identity dual quaternion.
        """
    def GetReal(self) -> Quath:
        """
        Returns the real part of the dual quaternion.
        """
    def GetTranslation(self) -> Vec3h:
        """
        Get the translation component of this dual quaternion.
        """
    @staticmethod
    def GetZero() -> DualQuath:
        """
        Returns the zero dual quaternion, which has a real part of (0,0,0,0)
        and a dual part of (0,0,0,0).
        """
    def Normalize(self, eps: float = ...) -> DualQuath:
        """
        Normalizes this dual quaternion in place.


        Normalizes this dual quaternion in place to unit length, returning the
        length before normalization. If the length of this dual quaternion is
        smaller than C{eps}, this sets the dual quaternion to identity.
        """
    def SetDual(self, _dual: Quath, /) -> None:
        """
        Sets the dual part of the dual quaternion.
        """
    def SetReal(self, _real: Quath, /) -> None:
        """
        Sets the real part of the dual quaternion.
        """
    def SetTranslation(self, _translation: Vec3h | list[float] | tuple[float, float, float], /) -> None:
        """
        Set the translation component of this dual quaternion.
        """
    def Transform(self, _vec: Vec3h | list[float] | tuple[float, float, float], /) -> Vec3h:
        """
        Transforms the row vector *vec* by the dual quaternion.
        """
    def __add__(self, arg2: DualQuath, /) -> Any: ...
    def __eq__(self, other: object) -> bool:
        """
        Component-wise dual quaternion equality test.


        The real and dual parts must match exactly for dual quaternions to be
        considered equal.
        """
    def __hash__(self) -> int: ...
    def __iadd__(self, arg2: DualQuath, /) -> Any: ...
    def __idiv__(self, arg2: object, /) -> Any: ...
    @overload
    def __imul__(self, arg2: DualQuath, /) -> Any: ...
    @overload
    def __imul__(self, arg2: object, /) -> Any: ...
    def __isub__(self, arg2: DualQuath, /) -> Any: ...
    def __itruediv__(self, arg2: object, /) -> DualQuath: ...
    @overload
    def __mul__(self, arg2: DualQuath, /) -> Any: ...
    @overload
    def __mul__(self, arg2: object, /) -> Any: ...
    def __ne__(self, other: object) -> bool: ...
    def __rmul__(self, arg2: object, /) -> Any: ...
    def __sub__(self, arg2: DualQuath, /) -> Any: ...
    def __truediv__(self, arg2: object, /) -> Any: ...

class Frustum(Boost.Python.instance):
    '''
    Basic type: View frustum.


    This class represents a viewing frustum in three dimensional eye
    space. It may represent either a parallel (orthographic) or
    perspective projection. One can think of the frustum as being defined
    by 6 boundary planes.

    The frustum is specified using these parameters:
       - The *position* of the viewpoint.

       - The *rotation* applied to the default view frame, which is
         looking along the -z axis with the +y axis as the"up"direction.

       - The 2D *window* on the reference plane that defines the left,
         right, top, and bottom planes of the viewing frustum, as described
         below.

       - The distances to the *near* and *far* planes.

       - The *projection* *type*

       - The view distance.
         The window and near/far parameters combine to define the view frustum
         as follows. Transform the -z axis and the +y axis by the frustum
         rotation to get the world-space *view* *direction* and *up*
         *direction*. Now consider the *reference* *plane* that is
         perpendicular to the view direction, a distance of referencePlaneDepth
         from the viewpoint, and whose y axis corresponds to the up direction.
         The window rectangle is specified in a 2D coordinate system embedded
         in this plane. The origin of the coordinate system is the point at
         which the view direction vector intersects the plane. Therefore, the
         point (0,1) in this plane is found by moving 1 unit along the up
         direction vector in this plane. The vector from the viewpoint to the
         resulting point will form a 45-degree angle with the view direction.

    The view distance is only useful for interactive applications. It can
    be used to compute a look at point which is useful when rotating
    around an object of interest.
    '''

    class ProjectionType(pxr.Tf.Tf_PyEnumWrapper):
        _baseName: ClassVar[str] = ...
        allValues: ClassVar[tuple] = ...
        def __init__(self, *args, **kwargs) -> None:
            """Raises an exception
            This class cannot be instantiated from Python
            """
        @staticmethod
        def GetValueFromName(name: str | pxr.Ar.ResolvedPath) -> Any: ...
    Orthographic: ClassVar[Frustum.ProjectionType] = ...
    Perspective: ClassVar[Frustum.ProjectionType] = ...
    __instance_size__: ClassVar[int] = ...
    nearFar: Range1d
    position: Vec3d
    projectionType: Frustum.ProjectionType
    rotation: Rotation
    viewDistance: float
    window: Range2d
    @overload
    def __init__(self) -> None:
        '''
        This constructor creates an instance with default viewing parameters:



           - The position is the origin.

           - The rotation is the identity rotation. (The view is along the -z
             axis, with the +y axis as"up").

           - The window is -1 to +1 in both dimensions.

           - The near/far interval is (1, 10).

           - The view distance is 5.0.

           - The projection type is C{GfFrustum::Perspective}.

        '''
    @overload
    def __init__(self, _o: Frustum, /) -> None:
        """
        Copy constructor.
        """
    @overload
    def __init__(self, position: Vec3d | list[float] | tuple[float, float, float], rotation: Rotation, window: Range2d | list[float] | tuple[float, float], nearFar: Range1d, projectionType: Frustum.ProjectionType, viewDistance: float = ...) -> None:
        """
        This constructor creates an instance with the given viewing
        parameters.
        """
    @overload
    def __init__(self, camToWorldXf: Matrix4d, window: Range2d | list[float] | tuple[float, float], nearFar: Range1d, projectionType: Frustum.ProjectionType, viewDistance: float = ...) -> None:
        """
        This constructor creates an instance from a camera matrix (always of a
        y-Up camera, also see SetPositionAndRotationFromMatrix) and the given
        viewing parameters.
        """
    def ComputeAspectRatio(self) -> float:
        """
        Returns the aspect ratio of the frustum, defined as the width of the
        window divided by the height.


        If the height is zero or negative, this returns 0.
        """
    def ComputeCorners(self) -> tuple:
        """
        Returns the world-space corners of the frustum as a vector of 8
        points, ordered as:



           - Left bottom near

           - Right bottom near

           - Left top near

           - Right top near

           - Left bottom far

           - Right bottom far

           - Left top far

           - Right top far

        """
    def ComputeCornersAtDistance(self, _d: float, /) -> tuple:
        """
        Returns the world-space corners of the intersection of the frustum
        with a plane parallel to the near/far plane at distance d from the
        apex, ordered as:



           - Left bottom

           - Right bottom

           - Left top

           - Right top In particular, it gives the partial result of
             ComputeCorners when given near or far distance.

        """
    def ComputeLookAtPoint(self) -> Vec3d:
        """
        Computes and returns the world-space look-at point from the eye point
        (position), view direction (rotation), and view distance.
        """
    @overload
    def ComputeNarrowedFrustum(self, _windowPos: Vec2d | list[float] | tuple[float, float], _size: Vec2d | list[float] | tuple[float, float], /) -> Frustum:
        """
        Returns a frustum that is a narrowed-down version of this frustum.


        The new frustum has the same near and far planes, but the other planes
        are adjusted to be centered on C{windowPos} with the new width and
        height obtained from the existing width and height by multiplying by
        C{size} [0] and C{size} [1], respectively. Finally, the new frustum is
        clipped against this frustum so that it is completely contained in the
        existing frustum.

        C{windowPos} is given in normalized coords (-1 to +1 in both
        dimensions). C{size} is given as a scalar (0 to 1 in both dimensions).

        If the C{windowPos} or C{size} given is outside these ranges, it may
        result in returning a collapsed frustum.

        This method is useful for computing a volume to use for interactive
        picking.
        """
    @overload
    def ComputeNarrowedFrustum(self, _worldPoint: Vec3d | list[float] | tuple[float, float, float], _size: Vec2d | list[float] | tuple[float, float], /) -> Frustum:
        """
        Returns a frustum that is a narrowed-down version of this frustum.


        The new frustum has the same near and far planes, but the other planes
        are adjusted to be centered on C{worldPoint} with the new width and
        height obtained from the existing width and height by multiplying by
        C{size} [0] and C{size} [1], respectively. Finally, the new frustum is
        clipped against this frustum so that it is completely contained in the
        existing frustum.

        C{worldPoint} is given in world space coordinates. C{size} is given as
        a scalar (0 to 1 in both dimensions).

        If the C{size} given is outside this range, it may result in returning
        a collapsed frustum.

        If the C{worldPoint} is at or behind the eye of the frustum, it will
        return a frustum equal to this frustum.

        This method is useful for computing a volume to use for interactive
        picking.
        """
    @overload
    def ComputePickRay(self, _windowPos: Vec2d | list[float] | tuple[float, float], /) -> Ray:
        """
        Builds and returns a C{GfRay} that can be used for picking at the
        given normalized (-1 to +1 in both dimensions) window position.


        Contrasted with ComputeRay() , that method returns a ray whose origin
        is the eyepoint, while this method returns a ray whose origin is on
        the near plane.
        """
    @overload
    def ComputePickRay(self, _worldSpacePos: Vec3d | list[float] | tuple[float, float, float], /) -> Ray:
        """
        Builds and returns a C{GfRay} that can be used for picking that
        connects the viewpoint to the given 3d point in worldspace.
        """
    def ComputeProjectionMatrix(self) -> Matrix4d:
        """
        Returns a GL-style projection matrix corresponding to the frustum's
        projection.
        """
    def ComputeUpVector(self) -> Vec3d:
        """
        Returns the normalized world-space up vector, which is computed by
        rotating the y axis by the frustum's rotation.
        """
    def ComputeViewDirection(self) -> Vec3d:
        """
        Returns the normalized world-space view direction vector, which is
        computed by rotating the -z axis by the frustum's rotation.
        """
    def ComputeViewFrame(self) -> tuple:
        """
        Computes the view frame defined by this frustum.


        The frame consists of the view direction, up vector and side vector,
        as shown in this diagram. ::

          up
          ^   ^
          |  / 
          | / view
          |/
          +- - - - > side

        """
    def ComputeViewInverse(self) -> Matrix4d:
        """
        Returns a matrix that represents the inverse viewing transformation
        for this frustum.


        That is, it returns the matrix that converts points from eye (frustum)
        space to world space.
        """
    def ComputeViewMatrix(self) -> Matrix4d:
        """
        Returns a matrix that represents the viewing transformation for this
        frustum.


        That is, it returns the matrix that converts points from world space
        to eye (frustum) space.
        """
    def FitToSphere(self, _center: Vec3d | list[float] | tuple[float, float, float], _radius: float, _slack: float = ..., /) -> None:
        """
        Modifies the frustum to tightly enclose a sphere with the given center
        and radius, using the current view direction.


        The planes of the frustum are adjusted as necessary. The given amount
        of slack is added to the sphere's radius is used around the sphere to
        avoid boundary problems.
        """
    def GetFOV(self, isFovVertical: bool = ...) -> float:
        """
        Returns the horizontal or vertical fov of the frustum.


        The fov of the frustum is not necessarily the same value as displayed
        in the viewer. The displayed fov is a function of the focal length or
        FOV avar. The frustum's fov may be different due to things like lens
        breathing.

        If the frustum is not of type C{GfFrustum::Perspective}, the returned
        FOV will be 0.0.

        The default value for C{isFovVertical} is false so calling C{GetFOV}
        without an argument will return the horizontal field of view which is
        compatible with menv2x's old GfFrustum::GetFOV routine.
        """
    def GetNearFar(self) -> Range1d:
        """
        Returns the near/far interval.
        """
    def GetOrthographic(self) -> tuple:
        """
        Returns the current frustum in the format used by C{SetOrthographic()}
        .


        If the current frustum is not an orthographic projection, this returns
        C{false} and leaves the parameters untouched.
        """
    def GetPerspective(self, isFovVertical: bool = ...) -> tuple[float, float, float, float]:
        """
        Returns the current frustum in the format used by C{SetPerspective()}
        .


        If the current frustum is not a perspective projection, this returns
        C{false} and leaves the parameters untouched.
        """
    def GetPosition(self) -> Vec3d:
        """
        Returns the position of the frustum in world space.
        """
    def GetProjectionType(self) -> Frustum.ProjectionType:
        """
        Returns the projection type.
        """
    @staticmethod
    def GetReferencePlaneDepth() -> float:
        """
        Returns the depth of the reference plane.
        """
    def GetRotation(self) -> Rotation:
        """
        Returns the orientation of the frustum in world space as a rotation to
        apply to the -z axis.
        """
    def GetViewDistance(self) -> float:
        """
        Returns the view distance.
        """
    def GetWindow(self) -> Range2d:
        """
        Returns the window rectangle in the reference plane.
        """
    @overload
    def Intersects(self, _bbox: BBox3d, /) -> bool:
        """
        Returns true if the given axis-aligned bbox is inside or intersecting
        the frustum.


        Otherwise, it returns false. Useful when doing picking or frustum
        culling.
        """
    @overload
    def Intersects(self, _point: Vec3d | list[float] | tuple[float, float, float], /) -> bool:
        """
        Returns true if the given point is inside or intersecting the frustum.


        Otherwise, it returns false.
        """
    @overload
    def Intersects(self, _p0: Vec3d | list[float] | tuple[float, float, float], _p1: Vec3d | list[float] | tuple[float, float, float], /) -> bool:
        """
        Returns C{true} if the line segment formed by the given points is
        inside or intersecting the frustum.


        Otherwise, it returns false.
        """
    @overload
    def Intersects(self, _p0: Vec3d | list[float] | tuple[float, float, float], _p1: Vec3d | list[float] | tuple[float, float, float], _p2: Vec3d | list[float] | tuple[float, float, float], /) -> bool:
        """
        Returns C{true} if the triangle formed by the given points is inside
        or intersecting the frustum.


        Otherwise, it returns false.
        """
    @staticmethod
    def IntersectsViewVolume(_bbox: BBox3d, _vpMat: Matrix4d, /) -> bool:
        """
        Returns C{true} if the bbox volume intersects the view volume given by
        the view-projection matrix, erring on the side of false positives for
        efficiency.


        This method is intended for cases where a GfFrustum is not available
        or when the view-projection matrix yields a view volume that is not
        expressable as a GfFrustum.

        Because it errs on the side of false positives, it is suitable for
        early-out tests such as draw or intersection culling.
        """
    def SetNearFar(self, _nearFar: Range1d, /) -> None:
        """
        Sets the near/far interval.
        """
    def SetOrthographic(self, _left: float, _right: float, _bottom: float, _top: float, _nearPlane: float, _farPlane: float, /) -> None:
        """
        Sets up the frustum in a manner similar to C{glOrtho()} .


        Sets the projection to C{GfFrustum::Orthographic} and sets the window
        and near/far specifications based on the given values.
        """
    @overload
    def SetPerspective(self, fovHeight: float, aspectRatio: float, nearDist: float, farDist: float) -> None:
        """
        Sets up the frustum in a manner similar to C{gluPerspective()} .


        It sets the projection type to C{GfFrustum::Perspective} and sets the
        window specification so that the resulting symmetric frustum encloses
        an angle of C{fieldOfViewHeight} degrees in the vertical direction,
        with C{aspectRatio} used to figure the angle in the horizontal
        direction. The near and far distances are specified as well. The
        window coordinates are computed as: ::

          top    = tan(fieldOfViewHeight / 2)
          bottom = -top
          right  = top * aspectRatio
          left   = -right
          near   = nearDistance
          far    = farDistance

        """
    @overload
    def SetPerspective(self, fov: float, isFovVertical: bool, aspectRatio: float, nearDist: float, farDist: float) -> None:
        """
        Sets up the frustum in a manner similar to gluPerspective().


        It sets the projection type to C{GfFrustum::Perspective} and sets the
        window specification so that:

        If *isFovVertical* is true, the resulting symmetric frustum encloses
        an angle of C{fieldOfView} degrees in the vertical direction, with
        C{aspectRatio} used to figure the angle in the horizontal direction.

        If *isFovVertical* is false, the resulting symmetric frustum encloses
        an angle of C{fieldOfView} degrees in the horizontal direction, with
        C{aspectRatio} used to figure the angle in the vertical direction.

        The near and far distances are specified as well. The window
        coordinates are computed as follows:

           - if isFovVertical:

           - top = tan(fieldOfView / 2)

           - right = top * aspectRatio

           - if NOT isFovVertical:

           - right = tan(fieldOfView / 2)

           - top = right / aspectRation

           - bottom = -top

           - left = -right

           - near = nearDistance

           - far = farDistance

        """
    def SetPosition(self, _position: Vec3d | list[float] | tuple[float, float, float], /) -> None:
        """
        Sets the position of the frustum in world space.
        """
    def SetPositionAndRotationFromMatrix(self, camToWorldXf: Matrix4d) -> None:
        """
        Sets the position and rotation of the frustum from a camera matrix
        (always from a y-Up camera).


        The resulting frustum's transform will always represent a right-handed
        and orthonormal coordinate sytem (scale, shear, and projection are
        removed from the given C{camToWorldXf}).
        """
    def SetProjectionType(self, _projectionType: Frustum.ProjectionType, /) -> None:
        """
        Sets the projection type.
        """
    def SetRotation(self, _rotation: Rotation, /) -> None:
        '''
        Sets the orientation of the frustum in world space as a rotation to
        apply to the default frame: looking along the -z axis with the +y axis
        as"up".
        '''
    def SetViewDistance(self, _viewDistance: float, /) -> None:
        """
        Sets the view distance.
        """
    def SetWindow(self, _window: Range2d | list[float] | tuple[float, float], /) -> None:
        """
        Sets the window rectangle in the reference plane that defines the
        left, right, top, and bottom planes of the frustum.
        """
    def Transform(self, _matrix: Matrix4d, /) -> Frustum:
        """
        Transforms the frustum by the given matrix.


        The transformation matrix is applied as follows: the position and the
        direction vector are transformed with the given matrix. Then the
        length of the new direction vector is used to rescale the near and far
        plane and the view distance. Finally, the points that define the
        reference plane are transformed by the matrix. This method assures
        that the frustum will not be sheared or perspective-projected.

        Note that this definition means that the transformed frustum does not
        preserve scales very well. Do *not* use this function to transform a
        frustum that is to be used for precise operations such as intersection
        testing.
        """
    def __eq__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...

class Interval(Boost.Python.instance):
    """
    A basic mathematical interval class.


    Can represent intervals with either open or closed boundary
    conditions.
    """
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None:
        """
        Construct an empty open interval, (0,0).
        """
    @overload
    def __init__(self, _val: Interval, /) -> None:
        """
        Construct a closed interval representing the single point, as
        [val,val].
        """
    @overload
    def __init__(self, _min: float, _max: float, _minClosed: bool, _maxClosed: bool, /) -> None:
        """
        Construct an interval with the given arguments.
        """
    @overload
    def __init__(self, arg2: float, /) -> None:
        """    Create a closed interval representing the single point [val,val].

        __init__( (object)arg1, (float)arg2, (float)arg3) -> None :
            Create a closed interval representing the range [v1,v2].

        __init__( (object)arg1, (float)arg2, (float)arg3, (bool)arg4, (bool)arg5) -> None :
            Create the interval.

        __init__( (object)arg1, (Interval)arg2) -> None"""
    @overload
    def __init__(self, arg2: float, arg3: float, /) -> None:
        """    Create a closed interval representing the single point [val,val].

        __init__( (object)arg1, (float)arg2, (float)arg3) -> None :
            Create a closed interval representing the range [v1,v2].

        __init__( (object)arg1, (float)arg2, (float)arg3, (bool)arg4, (bool)arg5) -> None :
            Create the interval.

        __init__( (object)arg1, (Interval)arg2) -> None"""
    @overload
    def Contains(self, _d: float, /) -> bool:
        """
        Return true iff the value d is contained in the interval.


        An empty interval contains no values.
        """
    @overload
    def Contains(self, _i: Interval, /) -> bool:
        """
        Return true iff the interval i is entirely contained in the interval.


        An empty interval contains no intervals, not even other empty
        intervals.
        """
    @staticmethod
    def GetFullInterval() -> Interval:
        """
        Returns the full interval (-inf, inf).
        """
    def GetMax(self) -> float:
        """
        Maximum value.
        """
    def GetMin(self) -> float:
        """
        Minimum value.
        """
    def GetSize(self) -> float:
        """
        Width of the interval.


        An empty interval has size 0.
        """
    def In(self, _d: float, /) -> bool:
        """Returns true if x is inside the interval."""
    def Intersects(self, _i: Interval, /) -> bool:
        """
        Return true iff the given interval i intersects this interval.
        """
    def IsEmpty(self) -> bool:
        """
        Return true iff the interval is empty.
        """
    def IsFinite(self) -> bool:
        """
        Returns true if both the maximum and minimum value are finite.
        """
    def IsMaxClosed(self) -> bool:
        """
        Maximum boundary condition.
        """
    def IsMaxFinite(self) -> bool:
        """
        Returns true if the maximum value is finite.
        """
    def IsMaxOpen(self) -> bool:
        """
        Maximum boundary condition.
        """
    def IsMinClosed(self) -> bool:
        """
        Minimum boundary condition.
        """
    def IsMinFinite(self) -> bool:
        """
        Returns true if the minimum value is finite.
        """
    def IsMinOpen(self) -> bool:
        """
        Minimum boundary condition.
        """
    @overload
    def SetMax(self, _v: float, /) -> None:
        """
        Set maximum value.
        """
    @overload
    def SetMax(self, _v: float, _maxClosed: bool, /) -> None:
        """
        Set maximum value and boundary condition.
        """
    @overload
    def SetMin(self, _v: float, /) -> None:
        """
        Set minimum value.
        """
    @overload
    def SetMin(self, _v: float, _minClosed: bool, /) -> None:
        """
        Set minimum value and boundary condition.
        """
    def __add__(self, arg2: Interval, /) -> Any: ...
    def __and__(self, arg2: Interval, /) -> Any: ...
    def __eq__(self, other: object) -> bool:
        """
        Equality operator.
        """
    def __ge__(self, other: object) -> bool:
        """
        Greater than or equal operator.
        """
    def __gt__(self, other: object) -> bool:
        """
        Greater than operator.
        """
    def __hash__(self) -> int: ...
    def __iadd__(self, arg2: Interval, /) -> Any: ...
    def __iand__(self, arg2: Interval, /) -> Any: ...
    def __imul__(self, arg2: Interval, /) -> Any: ...
    def __ior__(self, arg2: Interval, /) -> Any: ...
    def __isub__(self, arg2: Interval, /) -> Any: ...
    def __le__(self, other: object) -> bool:
        """
        Less than or equal operator.
        """
    def __lt__(self, other: object) -> bool:
        """
        Less-than operator.
        """
    def __mul__(self, arg2: Interval, /) -> Any: ...
    def __ne__(self, other: object) -> bool: ...
    def __neg__(self) -> Any: ...
    def __or__(self, arg2: Interval, /) -> Any: ...
    def __sub__(self, arg2: Interval, /) -> Any: ...
    @property
    def finite(self): ...
    @property
    def isEmpty(self) -> bool:
        """
        Return true iff the interval is empty.
        """
    @property
    def max(self) -> float:
        """
        Maximum value.
        """
    @property
    def maxClosed(self): ...
    @property
    def maxFinite(self): ...
    @property
    def maxOpen(self): ...
    @property
    def min(self) -> float:
        """
        Minimum value.
        """
    @property
    def minClosed(self): ...
    @property
    def minFinite(self): ...
    @property
    def minOpen(self): ...
    @property
    def size(self) -> float:
        """
        Width of the interval.


        An empty interval has size 0.
        """

class Line(Boost.Python.instance):
    """
    Basic type: 3D line.


    This class represents a three-dimensional line in space. Lines are
    constructed from a point, C{p0}, and a direction, dir. The direction
    is normalized in the constructor.

    The line is kept in a parametric represention, p = p0 + t * dir.
    """
    __instance_size__: ClassVar[int] = ...
    direction: Vec3d
    @overload
    def __init__(self) -> None:
        """
        The default constructor leaves line parameters undefined.
        """
    @overload
    def __init__(self, _p0: Vec3d | list[float] | tuple[float, float, float], _dir: Vec3d | list[float] | tuple[float, float, float], /) -> None:
        """
        Construct a line from a point and a direction.
        """
    def FindClosestPoint(self, _point: Vec3d | list[float] | tuple[float, float, float], /) -> tuple:
        """
        Returns the point on the line that is closest to C{point}.


        If C{t} is not C{None}, it will be set to the parametric distance
        along the line of the returned point.
        """
    def GetDirection(self) -> Vec3d:
        """
        Return the normalized direction of the line.
        """
    def GetPoint(self, _t: float, /) -> Vec3d:
        """
        Return the point on the line at C{} ( p0 + t * dir).


        Remember dir has been normalized so t represents a unit distance.
        """
    def Set(self, _p0: Vec3d | list[float] | tuple[float, float, float], _dir: Vec3d | list[float] | tuple[float, float, float], /) -> Line: ...
    def __eq__(self, other: object) -> bool:
        """
        Component-wise equality test.


        The starting points and directions, must match exactly for lines to be
        considered equal.
        """
    def __ne__(self, other: object) -> bool: ...

class LineSeg(Boost.Python.instance):
    """
    Basic type: 3D line segment.


    This class represents a three-dimensional line segment in space.
    """
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None:
        """
        The default constructor leaves line parameters undefined.
        """
    @overload
    def __init__(self, _p0: Vec3d | list[float] | tuple[float, float, float], _p1: Vec3d | list[float] | tuple[float, float, float], /) -> None:
        """
        Construct a line segment that spans two points.
        """
    def FindClosestPoint(self, _point: Vec3d | list[float] | tuple[float, float, float], /) -> tuple:
        """
        Returns the point on the line that is closest to C{point}.


        If C{t} is not C{None}, it will be set to the parametric distance
        along the line of the closest point.
        """
    def GetDirection(self) -> Vec3d:
        """
        Return the normalized direction of the line.
        """
    def GetLength(self) -> float:
        """
        Return the length of the line.
        """
    def GetPoint(self, _t: float, /) -> Vec3d:
        """
        Return the point on the segment specified by the parameter t.


        p = p0 + t * (p1 - p0)
        """
    def __eq__(self, other: object) -> bool:
        """
        Component-wise equality test.


        The starting points and directions, must match exactly for lines to be
        considered equal.
        """
    def __ne__(self, other: object) -> bool: ...
    @property
    def direction(self) -> Vec3d:
        """
        Return the normalized direction of the line.
        """
    @property
    def length(self) -> float:
        """
        Return the length of the line.
        """

class Matrix2d(Boost.Python.instance):
    """
    Stores a 2x2 matrix of C{double} elements.


    A basic type.

    Matrices are defined to be in row-major order, so C{matrix[i][j]}
    indexes the element in the *i* th row and the *j* th column.
    """
    dimension: ClassVar[tuple] = ...  # read-only
    __safe_for_unpickling__: ClassVar[bool] = ...
    @overload
    def __init__(self) -> None:
        """
        Default constructor. Leaves the matrix component values undefined.
        """
    @overload
    def __init__(self, _m00: float, _m01: float, _m10: float, _m11: float, /) -> None:
        """
        Constructor.


        Initializes the matrix from 4 independent C{double} values, specified
        in row-major order. For example, parameter *m10* specifies the value
        in row 1 and column 0.
        """
    @overload
    def __init__(self, _s: int, /) -> None:
        """
        This explicit constructor initializes the matrix to C{s} times the
        identity matrix.
        """
    @overload
    def __init__(self, _v: Vec2d | list[float] | tuple[float, float], /) -> None:
        """
        Constructor.


        Explicitly initializes the matrix to diagonal form, with the *i* th
        element on the diagonal set to C{v[i]} .
        """
    @overload
    def __init__(self, _m: Matrix2f, /) -> None:
        '''
        This explicit constructor converts a"float"matrix to a"double"matrix.
        '''
    @overload
    def __init__(self, arg2: Matrix2d, /) -> None: ...
    @overload
    def __init__(self, arg2: float, /) -> None: ...
    @overload
    def __init__(self, arg2: object, /) -> None: ...
    def GetColumn(self, _i: int, /) -> Vec2d:
        """
        Gets a column of the matrix as a Vec2.
        """
    def GetDeterminant(self) -> float:
        """
        Returns the determinant of the matrix.
        """
    def GetInverse(self) -> Matrix2d:
        """
        Returns the inverse of the matrix, or FLT_MAX * SetIdentity() if the
        matrix is singular.


        (FLT_MAX is the largest value a C{float} can have, as defined by the
        system.) The matrix is considered singular if the determinant is less
        than or equal to the optional parameter *eps*. If *det* is non-null,
        C{*det} is set to the determinant.
        """
    def GetRow(self, _i: int, /) -> Vec2d:
        """
        Gets a row of the matrix as a Vec2.
        """
    def GetTranspose(self) -> Matrix2d:
        """
        Returns the transpose of the matrix.
        """
    def Set(self, _m00: float, _m01: float, _m10: float, _m11: float, /) -> Matrix2d:
        """
        Sets the matrix from 4 independent C{double} values, specified in row-
        major order.


        For example, parameter *m10* specifies the value in row 1 and column
        0.
        """
    def SetColumn(self, _i: int, _v: Vec2d | list[float] | tuple[float, float], /) -> None:
        """
        Sets a column of the matrix from a Vec2.
        """
    @overload
    def SetDiagonal(self, _s: float, /) -> Matrix2d:
        """
        Sets the matrix to *s* times the identity matrix.
        """
    @overload
    def SetDiagonal(self, _unknownArg1: Vec2d | list[float] | tuple[float, float], /) -> Matrix2d:
        """
        Sets the matrix to have diagonal ( C{v[0], v[1]} ).
        """
    def SetIdentity(self) -> Matrix2d:
        """
        Sets the matrix to the identity matrix.
        """
    def SetRow(self, _i: int, _v: Vec2d | list[float] | tuple[float, float], /) -> None:
        """
        Sets a row of the matrix from a Vec2.
        """
    def SetZero(self) -> Matrix2d:
        """
        Sets the matrix to zero.
        """
    def __add__(self, arg2: Matrix2d, /) -> Any: ...
    @overload
    def __contains__(self, arg2: float, /) -> bool:
        """Check rows against GfVec"""
    @overload
    def __contains__(self, arg2: Vec2d | list[float] | tuple[float, float], /) -> bool:
        """Check rows against GfVec"""
    def __eq__(self, other: object) -> bool:
        """
        Tests for element-wise matrix equality.


        All elements must match exactly for matrices to be considered equal.
        """
    def __getinitargs__(self) -> tuple: ...
    @overload
    def __getitem__(self, _i: tuple, /) -> float:
        """
        Accesses an indexed row *i* of the matrix as an array of 2 C{double}
        values so that standard indexing (such as C{m[0][1]} ) works
        correctly.
        """
    @overload
    def __getitem__(self, arg2: int, /) -> Vec2d: ...
    def __hash__(self) -> int: ...
    def __iadd__(self, arg2: Matrix2d, /) -> Any: ...
    @overload
    def __imul__(self, arg2: Matrix2d, /) -> Any: ...
    @overload
    def __imul__(self, arg2: float, /) -> Any: ...
    def __isub__(self, arg2: Matrix2d, /) -> Any: ...
    def __len__(self) -> int:
        """Return number of rows"""
    @overload
    def __mul__(self, arg2: Matrix2d, /) -> Any: ...
    @overload
    def __mul__(self, arg2: float, /) -> Any: ...
    @overload
    def __mul__(self, arg2: Vec2d | list[float] | tuple[float, float], /) -> Any: ...
    @overload
    def __mul__(self, arg2: Vec2f | list[float] | tuple[float, float], /) -> Any: ...
    def __ne__(self, other: object) -> bool: ...
    def __neg__(self) -> Any: ...
    @overload
    def __rmul__(self, arg2: float, /) -> Any: ...
    @overload
    def __rmul__(self, arg2: Vec2d | list[float] | tuple[float, float], /) -> Any: ...
    @overload
    def __rmul__(self, arg2: Vec2f | list[float] | tuple[float, float], /) -> Any: ...
    @overload
    def __setitem__(self, arg2: tuple, arg3: float, /) -> None: ...
    @overload
    def __setitem__(self, arg2: int, arg3: Vec2d | list[float] | tuple[float, float], /) -> None: ...
    def __sub__(self, arg2: Matrix2d, /) -> Any: ...
    def __truediv__(self, arg2: Matrix2d, /) -> Any: ...

class Matrix2f(Boost.Python.instance):
    """
    Stores a 2x2 matrix of C{float} elements.


    A basic type.

    Matrices are defined to be in row-major order, so C{matrix[i][j]}
    indexes the element in the *i* th row and the *j* th column.
    """
    dimension: ClassVar[tuple] = ...  # read-only
    __safe_for_unpickling__: ClassVar[bool] = ...
    @overload
    def __init__(self) -> None:
        """
        Default constructor. Leaves the matrix component values undefined.
        """
    @overload
    def __init__(self, _m00: float, _m01: float, _m10: float, _m11: float, /) -> None:
        """
        Constructor.


        Initializes the matrix from 4 independent C{float} values, specified
        in row-major order. For example, parameter *m10* specifies the value
        in row 1 and column 0.
        """
    @overload
    def __init__(self, _s: int, /) -> None:
        """
        This explicit constructor initializes the matrix to C{s} times the
        identity matrix.
        """
    @overload
    def __init__(self, _v: Vec2f | list[float] | tuple[float, float], /) -> None:
        """
        Constructor.


        Explicitly initializes the matrix to diagonal form, with the *i* th
        element on the diagonal set to C{v[i]} .
        """
    @overload
    def __init__(self, _m: Matrix2d, /) -> None:
        '''
        This explicit constructor converts a"double"matrix to a"float"matrix.
        '''
    @overload
    def __init__(self, arg2: Matrix2f, /) -> None: ...
    @overload
    def __init__(self, arg2: float, /) -> None: ...
    @overload
    def __init__(self, arg2: object, /) -> None: ...
    def GetColumn(self, _i: int, /) -> Vec2f:
        """
        Gets a column of the matrix as a Vec2.
        """
    def GetDeterminant(self) -> float:
        """
        Returns the determinant of the matrix.
        """
    def GetInverse(self) -> Matrix2f:
        """
        Returns the inverse of the matrix, or FLT_MAX * SetIdentity() if the
        matrix is singular.


        (FLT_MAX is the largest value a C{float} can have, as defined by the
        system.) The matrix is considered singular if the determinant is less
        than or equal to the optional parameter *eps*. If *det* is non-null,
        C{*det} is set to the determinant.
        """
    def GetRow(self, _i: int, /) -> Vec2f:
        """
        Gets a row of the matrix as a Vec2.
        """
    def GetTranspose(self) -> Matrix2f:
        """
        Returns the transpose of the matrix.
        """
    def Set(self, _m00: float, _m01: float, _m10: float, _m11: float, /) -> Matrix2f:
        """
        Sets the matrix from 4 independent C{float} values, specified in row-
        major order.


        For example, parameter *m10* specifies the value in row 1 and column
        0.
        """
    def SetColumn(self, _i: int, _v: Vec2f | list[float] | tuple[float, float], /) -> None:
        """
        Sets a column of the matrix from a Vec2.
        """
    @overload
    def SetDiagonal(self, _s: float, /) -> Matrix2f:
        """
        Sets the matrix to *s* times the identity matrix.
        """
    @overload
    def SetDiagonal(self, _unknownArg1: Vec2f | list[float] | tuple[float, float], /) -> Matrix2f:
        """
        Sets the matrix to have diagonal ( C{v[0], v[1]} ).
        """
    def SetIdentity(self) -> Matrix2f:
        """
        Sets the matrix to the identity matrix.
        """
    def SetRow(self, _i: int, _v: Vec2f | list[float] | tuple[float, float], /) -> None:
        """
        Sets a row of the matrix from a Vec2.
        """
    def SetZero(self) -> Matrix2f:
        """
        Sets the matrix to zero.
        """
    def __add__(self, arg2: Matrix2f, /) -> Any: ...
    @overload
    def __contains__(self, arg2: float, /) -> bool:
        """Check rows against GfVec"""
    @overload
    def __contains__(self, arg2: Vec2f | list[float] | tuple[float, float], /) -> bool:
        """Check rows against GfVec"""
    def __eq__(self, other: object) -> bool:
        """
        Tests for element-wise matrix equality.


        All elements must match exactly for matrices to be considered equal.
        """
    def __getinitargs__(self) -> tuple: ...
    @overload
    def __getitem__(self, _i: tuple, /) -> float:
        """
        Accesses an indexed row *i* of the matrix as an array of 2 C{float}
        values so that standard indexing (such as C{m[0][1]} ) works
        correctly.
        """
    @overload
    def __getitem__(self, arg2: int, /) -> Vec2f: ...
    def __hash__(self) -> int: ...
    def __iadd__(self, arg2: Matrix2f, /) -> Any: ...
    @overload
    def __imul__(self, arg2: Matrix2f, /) -> Any: ...
    @overload
    def __imul__(self, arg2: float, /) -> Any: ...
    def __isub__(self, arg2: Matrix2f, /) -> Any: ...
    def __len__(self) -> int:
        """Return number of rows"""
    @overload
    def __mul__(self, arg2: Matrix2f, /) -> Any: ...
    @overload
    def __mul__(self, arg2: float, /) -> Any: ...
    @overload
    def __mul__(self, arg2: Vec2f | list[float] | tuple[float, float], /) -> Any: ...
    def __ne__(self, other: object) -> bool: ...
    def __neg__(self) -> Any: ...
    @overload
    def __rmul__(self, arg2: float, /) -> Any: ...
    @overload
    def __rmul__(self, arg2: Vec2f | list[float] | tuple[float, float], /) -> Any: ...
    @overload
    def __setitem__(self, arg2: tuple, arg3: float, /) -> None: ...
    @overload
    def __setitem__(self, arg2: int, arg3: Vec2f | list[float] | tuple[float, float], /) -> None: ...
    def __sub__(self, arg2: Matrix2f, /) -> Any: ...
    def __truediv__(self, arg2: Matrix2f, /) -> Any: ...

class Matrix3d(Boost.Python.instance):
    """
    Stores a 3x3 matrix of C{double} elements.


    A basic type.

    Matrices are defined to be in row-major order, so C{matrix[i][j]}
    indexes the element in the *i* th row and the *j* th column.

    3D Transformations
    ==================

    Three methods, SetRotate() , SetScale() , and ExtractRotation() ,
    interpret a GfMatrix3d as a 3D transformation. By convention, vectors
    are treated primarily as row vectors, implying the following:

       - Transformation matrices are organized to deal with row vectors,
         not column vectors.

       - Each of the Set() methods in this class completely rewrites the
         matrix; for example, SetRotate() yields a matrix which does nothing
         but rotate.

       - When multiplying two transformation matrices, the matrix on the
         left applies a more local transformation to a row vector. For example,
         if R represents a rotation matrix and S represents a scale matrix, the
         product R*S will rotate a row vector, then scale it.

    """
    dimension: ClassVar[tuple] = ...  # read-only
    __safe_for_unpickling__: ClassVar[bool] = ...
    @overload
    def __init__(self) -> None:
        """
        Default constructor. Leaves the matrix component values undefined.
        """
    @overload
    def __init__(self, _m00: float, _m01: float, _m02: float, _m10: float, _m11: float, _m12: float, _m20: float, _m21: float, _m22: float, /) -> None:
        """
        Constructor.


        Initializes the matrix from 9 independent C{double} values, specified
        in row-major order. For example, parameter *m10* specifies the value
        in row 1 and column 0.
        """
    @overload
    def __init__(self, _s: int, /) -> None:
        """
        This explicit constructor initializes the matrix to C{s} times the
        identity matrix.
        """
    @overload
    def __init__(self, _v: Vec3d | list[float] | tuple[float, float, float], /) -> None:
        """
        Constructor.


        Explicitly initializes the matrix to diagonal form, with the *i* th
        element on the diagonal set to C{v[i]} .
        """
    @overload
    def __init__(self, _rot: Rotation, /) -> None:
        """
        Constructor. Initialize matrix from rotation.
        """
    @overload
    def __init__(self, _rot: Quatd | Quatf | Quath, /) -> None:
        """
        Constructor. Initialize matrix from a quaternion.
        """
    @overload
    def __init__(self, _m: Matrix3f, /) -> None:
        '''
        This explicit constructor converts a"float"matrix to a"double"matrix.
        '''
    @overload
    def __init__(self, arg2: Matrix3d, /) -> None: ...
    @overload
    def __init__(self, arg2: float, /) -> None: ...
    @overload
    def __init__(self, arg2: object, /) -> None: ...
    def ExtractRotation(self) -> Rotation:
        """
        Returns the rotation corresponding to this matrix.


        This works well only if the matrix represents a rotation.

        For good results, consider calling Orthonormalize() before calling
        this method.
        """
    def GetColumn(self, _i: int, /) -> Vec3d:
        """
        Gets a column of the matrix as a Vec3.
        """
    def GetDeterminant(self) -> float:
        """
        Returns the determinant of the matrix.
        """
    def GetHandedness(self) -> float:
        """
        Returns the sign of the determinant of the matrix, i.e.


        1 for a right-handed matrix, -1 for a left-handed matrix, and 0 for a
        singular matrix.
        """
    def GetInverse(self) -> Matrix3d:
        """
        Returns the inverse of the matrix, or FLT_MAX * SetIdentity() if the
        matrix is singular.


        (FLT_MAX is the largest value a C{float} can have, as defined by the
        system.) The matrix is considered singular if the determinant is less
        than or equal to the optional parameter *eps*. If *det* is non-null,
        C{*det} is set to the determinant.
        """
    def GetOrthonormalized(self, issueWarning: bool = ...) -> Matrix3d:
        """
        Returns an orthonormalized copy of the matrix.
        """
    def GetRow(self, _i: int, /) -> Vec3d:
        """
        Gets a row of the matrix as a Vec3.
        """
    def GetTranspose(self) -> Matrix3d:
        """
        Returns the transpose of the matrix.
        """
    def IsLeftHanded(self) -> bool:
        """
        Returns true if the vectors in matrix form a left-handed coordinate
        system.
        """
    def IsRightHanded(self) -> bool:
        """
        Returns true if the vectors in the matrix form a right-handed
        coordinate system.
        """
    def Orthonormalize(self, issueWarning: bool = ...) -> bool:
        """
        Makes the matrix orthonormal in place.


        This is an iterative method that is much more stable than the previous
        cross/cross method. If the iterative method does not converge, a
        warning is issued.

        Returns true if the iteration converged, false otherwise. Leaves any
        translation part of the matrix unchanged. If *issueWarning* is true,
        this method will issue a warning if the iteration does not converge,
        otherwise it will be silent.
        """
    def Set(self, _m00: float, _m01: float, _m02: float, _m10: float, _m11: float, _m12: float, _m20: float, _m21: float, _m22: float, /) -> Matrix3d:
        """
        Sets the matrix from 9 independent C{double} values, specified in row-
        major order.


        For example, parameter *m10* specifies the value in row 1 and column
        0.
        """
    def SetColumn(self, _i: int, _v: Vec3d | list[float] | tuple[float, float, float], /) -> None:
        """
        Sets a column of the matrix from a Vec3.
        """
    @overload
    def SetDiagonal(self, _s: float, /) -> Matrix3d:
        """
        Sets the matrix to *s* times the identity matrix.
        """
    @overload
    def SetDiagonal(self, _unknownArg1: Vec3d | list[float] | tuple[float, float, float], /) -> Matrix3d:
        """
        Sets the matrix to have diagonal ( C{v[0], v[1], v[2]} ).
        """
    def SetIdentity(self) -> Matrix3d:
        """
        Sets the matrix to the identity matrix.
        """
    @overload
    def SetRotate(self, _rot: Quatd | Quatf | Quath, /) -> Matrix3d:
        """
        Sets the matrix to specify a rotation equivalent to *rot*.
        """
    @overload
    def SetRotate(self, _rot: Rotation, /) -> Matrix3d:
        """
        Sets the matrix to specify a rotation equivalent to *rot*.
        """
    def SetRow(self, _i: int, _v: Vec3d | list[float] | tuple[float, float, float], /) -> None:
        """
        Sets a row of the matrix from a Vec3.
        """
    @overload
    def SetScale(self, _scaleFactors: Vec3d | list[float] | tuple[float, float, float], /) -> Matrix3d:
        """
        Sets the matrix to specify a nonuniform scaling in x, y, and z by the
        factors in vector *scaleFactors*.
        """
    @overload
    def SetScale(self, _scaleFactor: float, /) -> Matrix3d:
        """
        Sets matrix to specify a uniform scaling by *scaleFactor*.
        """
    def SetZero(self) -> Matrix3d:
        """
        Sets the matrix to zero.
        """
    def __add__(self, arg2: Matrix3d, /) -> Any: ...
    @overload
    def __contains__(self, arg2: float, /) -> bool:
        """Check rows against GfVec"""
    @overload
    def __contains__(self, arg2: Vec3d | list[float] | tuple[float, float, float], /) -> bool:
        """Check rows against GfVec"""
    def __eq__(self, other: object) -> bool:
        """
        Tests for element-wise matrix equality.


        All elements must match exactly for matrices to be considered equal.
        """
    def __getinitargs__(self) -> tuple: ...
    @overload
    def __getitem__(self, _i: tuple, /) -> float:
        """
        Accesses an indexed row *i* of the matrix as an array of 3 C{double}
        values so that standard indexing (such as C{m[0][1]} ) works
        correctly.
        """
    @overload
    def __getitem__(self, arg2: int, /) -> Vec3d: ...
    def __hash__(self) -> int: ...
    def __iadd__(self, arg2: Matrix3d, /) -> Any: ...
    @overload
    def __imul__(self, arg2: Matrix3d, /) -> Any: ...
    @overload
    def __imul__(self, arg2: float, /) -> Any: ...
    def __isub__(self, arg2: Matrix3d, /) -> Any: ...
    def __len__(self) -> int:
        """Return number of rows"""
    @overload
    def __mul__(self, arg2: Matrix3d, /) -> Any: ...
    @overload
    def __mul__(self, arg2: float, /) -> Any: ...
    @overload
    def __mul__(self, arg2: Vec3d | list[float] | tuple[float, float, float], /) -> Any: ...
    @overload
    def __mul__(self, arg2: Vec3f | list[float] | tuple[float, float, float], /) -> Any: ...
    def __ne__(self, other: object) -> bool: ...
    def __neg__(self) -> Any: ...
    @overload
    def __rmul__(self, arg2: float, /) -> Any: ...
    @overload
    def __rmul__(self, arg2: Vec3d | list[float] | tuple[float, float, float], /) -> Any: ...
    @overload
    def __rmul__(self, arg2: Vec3f | list[float] | tuple[float, float, float], /) -> Any: ...
    @overload
    def __setitem__(self, arg2: tuple, arg3: float, /) -> None: ...
    @overload
    def __setitem__(self, arg2: int, arg3: Vec3d | list[float] | tuple[float, float, float], /) -> None: ...
    def __sub__(self, arg2: Matrix3d, /) -> Any: ...
    def __truediv__(self, arg2: Matrix3d, /) -> Any: ...

class Matrix3f(Boost.Python.instance):
    """
    Stores a 3x3 matrix of C{float} elements.


    A basic type.

    Matrices are defined to be in row-major order, so C{matrix[i][j]}
    indexes the element in the *i* th row and the *j* th column.

    3D Transformations
    ==================

    Three methods, SetRotate() , SetScale() , and ExtractRotation() ,
    interpret a GfMatrix3f as a 3D transformation. By convention, vectors
    are treated primarily as row vectors, implying the following:

       - Transformation matrices are organized to deal with row vectors,
         not column vectors.

       - Each of the Set() methods in this class completely rewrites the
         matrix; for example, SetRotate() yields a matrix which does nothing
         but rotate.

       - When multiplying two transformation matrices, the matrix on the
         left applies a more local transformation to a row vector. For example,
         if R represents a rotation matrix and S represents a scale matrix, the
         product R*S will rotate a row vector, then scale it.

    """
    dimension: ClassVar[tuple] = ...  # read-only
    __safe_for_unpickling__: ClassVar[bool] = ...
    @overload
    def __init__(self) -> None:
        """
        Default constructor. Leaves the matrix component values undefined.
        """
    @overload
    def __init__(self, _m00: float, _m01: float, _m02: float, _m10: float, _m11: float, _m12: float, _m20: float, _m21: float, _m22: float, /) -> None:
        """
        Constructor.


        Initializes the matrix from 9 independent C{float} values, specified
        in row-major order. For example, parameter *m10* specifies the value
        in row 1 and column 0.
        """
    @overload
    def __init__(self, _s: int, /) -> None:
        """
        This explicit constructor initializes the matrix to C{s} times the
        identity matrix.
        """
    @overload
    def __init__(self, _v: Vec3f | list[float] | tuple[float, float, float], /) -> None:
        """
        Constructor.


        Explicitly initializes the matrix to diagonal form, with the *i* th
        element on the diagonal set to C{v[i]} .
        """
    @overload
    def __init__(self, _rot: Rotation, /) -> None:
        """
        Constructor. Initialize matrix from rotation.
        """
    @overload
    def __init__(self, _rot: Quatf | Quath, /) -> None:
        """
        Constructor. Initialize matrix from a quaternion.
        """
    @overload
    def __init__(self, _m: Matrix3d, /) -> None:
        '''
        This explicit constructor converts a"double"matrix to a"float"matrix.
        '''
    @overload
    def __init__(self, arg2: Matrix3f, /) -> None: ...
    @overload
    def __init__(self, arg2: float, /) -> None: ...
    @overload
    def __init__(self, arg2: object, /) -> None: ...
    def ExtractRotation(self) -> Rotation:
        """
        Returns the rotation corresponding to this matrix.


        This works well only if the matrix represents a rotation.

        For good results, consider calling Orthonormalize() before calling
        this method.
        """
    def GetColumn(self, _i: int, /) -> Vec3f:
        """
        Gets a column of the matrix as a Vec3.
        """
    def GetDeterminant(self) -> float:
        """
        Returns the determinant of the matrix.
        """
    def GetHandedness(self) -> float:
        """
        Returns the sign of the determinant of the matrix, i.e.


        1 for a right-handed matrix, -1 for a left-handed matrix, and 0 for a
        singular matrix.
        """
    def GetInverse(self) -> Matrix3f:
        """
        Returns the inverse of the matrix, or FLT_MAX * SetIdentity() if the
        matrix is singular.


        (FLT_MAX is the largest value a C{float} can have, as defined by the
        system.) The matrix is considered singular if the determinant is less
        than or equal to the optional parameter *eps*. If *det* is non-null,
        C{*det} is set to the determinant.
        """
    def GetOrthonormalized(self, issueWarning: bool = ...) -> Matrix3f:
        """
        Returns an orthonormalized copy of the matrix.
        """
    def GetRow(self, _i: int, /) -> Vec3f:
        """
        Gets a row of the matrix as a Vec3.
        """
    def GetTranspose(self) -> Matrix3f:
        """
        Returns the transpose of the matrix.
        """
    def IsLeftHanded(self) -> bool:
        """
        Returns true if the vectors in matrix form a left-handed coordinate
        system.
        """
    def IsRightHanded(self) -> bool:
        """
        Returns true if the vectors in the matrix form a right-handed
        coordinate system.
        """
    def Orthonormalize(self, issueWarning: bool = ...) -> bool:
        """
        Makes the matrix orthonormal in place.


        This is an iterative method that is much more stable than the previous
        cross/cross method. If the iterative method does not converge, a
        warning is issued.

        Returns true if the iteration converged, false otherwise. Leaves any
        translation part of the matrix unchanged. If *issueWarning* is true,
        this method will issue a warning if the iteration does not converge,
        otherwise it will be silent.
        """
    def Set(self, _m00: float, _m01: float, _m02: float, _m10: float, _m11: float, _m12: float, _m20: float, _m21: float, _m22: float, /) -> Matrix3f:
        """
        Sets the matrix from 9 independent C{float} values, specified in row-
        major order.


        For example, parameter *m10* specifies the value in row 1 and column
        0.
        """
    def SetColumn(self, _i: int, _v: Vec3f | list[float] | tuple[float, float, float], /) -> None:
        """
        Sets a column of the matrix from a Vec3.
        """
    @overload
    def SetDiagonal(self, _s: float, /) -> Matrix3f:
        """
        Sets the matrix to *s* times the identity matrix.
        """
    @overload
    def SetDiagonal(self, _unknownArg1: Vec3f | list[float] | tuple[float, float, float], /) -> Matrix3f:
        """
        Sets the matrix to have diagonal ( C{v[0], v[1], v[2]} ).
        """
    def SetIdentity(self) -> Matrix3f:
        """
        Sets the matrix to the identity matrix.
        """
    @overload
    def SetRotate(self, _rot: Quatf | Quath, /) -> Matrix3f:
        """
        Sets the matrix to specify a rotation equivalent to *rot*.
        """
    @overload
    def SetRotate(self, _rot: Rotation, /) -> Matrix3f:
        """
        Sets the matrix to specify a rotation equivalent to *rot*.
        """
    def SetRow(self, _i: int, _v: Vec3f | list[float] | tuple[float, float, float], /) -> None:
        """
        Sets a row of the matrix from a Vec3.
        """
    @overload
    def SetScale(self, _scaleFactors: Vec3f | list[float] | tuple[float, float, float], /) -> Matrix3f:
        """
        Sets the matrix to specify a nonuniform scaling in x, y, and z by the
        factors in vector *scaleFactors*.
        """
    @overload
    def SetScale(self, _scaleFactor: float, /) -> Matrix3f:
        """
        Sets matrix to specify a uniform scaling by *scaleFactor*.
        """
    def SetZero(self) -> Matrix3f:
        """
        Sets the matrix to zero.
        """
    def __add__(self, arg2: Matrix3f, /) -> Any: ...
    @overload
    def __contains__(self, arg2: float, /) -> bool:
        """Check rows against GfVec"""
    @overload
    def __contains__(self, arg2: Vec3f | list[float] | tuple[float, float, float], /) -> bool:
        """Check rows against GfVec"""
    def __eq__(self, other: object) -> bool:
        """
        Tests for element-wise matrix equality.


        All elements must match exactly for matrices to be considered equal.
        """
    def __getinitargs__(self) -> tuple: ...
    @overload
    def __getitem__(self, _i: tuple, /) -> float:
        """
        Accesses an indexed row *i* of the matrix as an array of 3 C{float}
        values so that standard indexing (such as C{m[0][1]} ) works
        correctly.
        """
    @overload
    def __getitem__(self, arg2: int, /) -> Vec3f: ...
    def __hash__(self) -> int: ...
    def __iadd__(self, arg2: Matrix3f, /) -> Any: ...
    @overload
    def __imul__(self, arg2: Matrix3f, /) -> Any: ...
    @overload
    def __imul__(self, arg2: float, /) -> Any: ...
    def __isub__(self, arg2: Matrix3f, /) -> Any: ...
    def __len__(self) -> int:
        """Return number of rows"""
    @overload
    def __mul__(self, arg2: Matrix3f, /) -> Any: ...
    @overload
    def __mul__(self, arg2: float, /) -> Any: ...
    @overload
    def __mul__(self, arg2: Vec3f | list[float] | tuple[float, float, float], /) -> Any: ...
    def __ne__(self, other: object) -> bool: ...
    def __neg__(self) -> Any: ...
    @overload
    def __rmul__(self, arg2: float, /) -> Any: ...
    @overload
    def __rmul__(self, arg2: Vec3f | list[float] | tuple[float, float, float], /) -> Any: ...
    @overload
    def __setitem__(self, arg2: tuple, arg3: float, /) -> None: ...
    @overload
    def __setitem__(self, arg2: int, arg3: Vec3f | list[float] | tuple[float, float, float], /) -> None: ...
    def __sub__(self, arg2: Matrix3f, /) -> Any: ...
    def __truediv__(self, arg2: Matrix3f, /) -> Any: ...

class Matrix4d(Boost.Python.instance):
    """
    Stores a 4x4 matrix of C{double} elements.


    A basic type.

    Matrices are defined to be in row-major order, so C{matrix[i][j]}
    indexes the element in the *i* th row and the *j* th column.

    3D Transformations
    ==================

    The following methods interpret a GfMatrix4d as a 3D transformation:
    SetRotate() , SetScale() , SetTranslate() , SetLookAt() , Factor() ,
    ExtractTranslation() , ExtractRotation() , Transform() ,
    TransformDir() . By convention, vectors are treated primarily as row
    vectors, implying the following:
       - Transformation matrices are organized to deal with row vectors,
         not column vectors. For example, the last row of a matrix contains the
         translation amounts.

       - Each of the Set() methods below completely rewrites the matrix;
         for example, SetTranslate() yields a matrix which does nothing but
         translate.

       - When multiplying two transformation matrices, the matrix on the
         left applies a more local transformation to a row vector. For example,
         if R represents a rotation matrix and T represents a translation
         matrix, the product R*T will rotate a row vector, then translate it.

    """
    dimension: ClassVar[tuple] = ...  # read-only
    __safe_for_unpickling__: ClassVar[bool] = ...
    @overload
    def __init__(self) -> None:
        """
        Default constructor. Leaves the matrix component values undefined.
        """
    @overload
    def __init__(self, _m00: float, _m01: float, _m02: float, _m03: float, _m10: float, _m11: float, _m12: float, _m13: float, _m20: float, _m21: float, _m22: float, _m23: float, _m30: float, _m31: float, _m32: float, _m33: float, /) -> None:
        """
        Constructor.


        Initializes the matrix from 16 independent C{double} values, specified
        in row-major order. For example, parameter *m10* specifies the value
        in row 1 and column 0.
        """
    @overload
    def __init__(self, _v: Vec4d | list[float] | tuple[float, float, float, float], /) -> None:
        """
        Constructor.


        Explicitly initializes the matrix to diagonal form, with the *i* th
        element on the diagonal set to C{v[i]} .
        """
    @overload
    def __init__(self, _r0: typing.Iterable[float], _r1: typing.Iterable[float], _r2: typing.Iterable[float], _r3: typing.Iterable[float], /) -> None:
        """
        Constructor.


        Initialize the matrix from 4 row vectors of double. Each vector is
        expected to length 4. If it is too big, only the first 4 items will be
        used. If it is too small, uninitialized elements will be filled in
        with the corresponding elements from an identity matrix.
        """
    @overload
    def __init__(self, _rotate: Rotation, _translate: Vec3d | list[float] | tuple[float, float, float], /) -> None:
        """
        Constructor.


        Initializes a transformation matrix to perform the indicated rotation
        and translation.
        """
    @overload
    def __init__(self, _rotmx: Matrix3d, _translate: Vec3d | list[float] | tuple[float, float, float], /) -> None:
        """
        Constructor.


        Initializes a transformation matrix to perform the indicated rotation
        and translation.
        """
    @overload
    def __init__(self, _m: Matrix4f, /) -> None:
        '''
        This explicit constructor converts a"float"matrix to a"double"matrix.
        '''
    @overload
    def __init__(self, arg2: Matrix4d, /) -> None: ...
    @overload
    def __init__(self, arg2: int, /) -> None: ...
    @overload
    def __init__(self, arg2: float, /) -> None: ...
    @overload
    def __init__(self, arg2: object, /) -> None: ...
    @overload
    def __init__(self, arg2: object, arg3: object, arg4: object, arg5: object, /) -> None: ...
    def ExtractRotation(self) -> Rotation:
        """
        Returns the rotation corresponding to this matrix.


        This works well only if the matrix represents a rotation.

        For good results, consider calling Orthonormalize() before calling
        this method.
        """
    def ExtractRotationMatrix(self) -> Matrix3d:
        """
        Returns the rotation corresponding to this matrix.


        This works well only if the matrix represents a rotation.

        For good results, consider calling Orthonormalize() before calling
        this method.
        """
    def ExtractRotationQuat(self) -> Quatd:
        """
        Return the rotation corresponding to this matrix as a quaternion.


        This works well only if the matrix represents a rotation.

        For good results, consider calling Orthonormalize() before calling
        this method.
        """
    def ExtractTranslation(self) -> Vec3d:
        """
        Returns the translation part of the matrix, defined as the first three
        elements of the last row.
        """
    def Factor(self, _eps: float = ..., /) -> tuple:
        """
        Factors the matrix into 5 components:



           - C{*M* = r * s * -r * u * t} where

           - *t* is a translation.

           - *u* and *r* are rotations, and *-r* is the transpose (inverse) of
             *r*. The *u* matrix may contain shear information.

           - *s* is a scale. Any projection information could be returned in
             matrix *p*, but currently p is never modified.
             Returns C{false} if the matrix is singular (as determined by *eps*).
             In that case, any zero scales in *s* are clamped to *eps* to allow
             computation of *u*.
        """
    def GetColumn(self, _i: int, /) -> Vec4d:
        """
        Gets a column of the matrix as a Vec4.
        """
    def GetDeterminant(self) -> float:
        """
        Returns the determinant of the matrix.
        """
    def GetDeterminant3(self) -> float:
        """
        Returns the determinant of the upper 3x3 matrix.


        This method is useful when the matrix describes a linear
        transformation such as a rotation or scale because the other values in
        the 4x4 matrix are not important.
        """
    def GetHandedness(self) -> float:
        """
        Returns the sign of the determinant of the upper 3x3 matrix, i.e.


        1 for a right-handed matrix, -1 for a left-handed matrix, and 0 for a
        singular matrix.
        """
    def GetInverse(self) -> Matrix4d:
        """
        Returns the inverse of the matrix, or FLT_MAX * SetIdentity() if the
        matrix is singular.


        (FLT_MAX is the largest value a C{float} can have, as defined by the
        system.) The matrix is considered singular if the determinant is less
        than or equal to the optional parameter *eps*. If *det* is non-null,
        C{*det} is set to the determinant.
        """
    def GetOrthonormalized(self, issueWarning: bool = ...) -> Matrix4d:
        """
        Returns an orthonormalized copy of the matrix.
        """
    def GetRow(self, _i: int, /) -> Vec4d:
        """
        Gets a row of the matrix as a Vec4.
        """
    def GetRow3(self, _i: int, /) -> Vec3d:
        """
        Gets a row of the matrix as a Vec3.
        """
    def GetTranspose(self) -> Matrix4d:
        """
        Returns the transpose of the matrix.
        """
    def HasOrthogonalRows3(self) -> bool:
        """
        Returns true, if the row vectors of the upper 3x3 matrix form an
        orthogonal basis.


        Note they do not have to be unit length for this test to return true.
        """
    def IsLeftHanded(self) -> bool:
        """
        Returns true if the vectors in the upper 3x3 matrix form a left-handed
        coordinate system.
        """
    def IsRightHanded(self) -> bool:
        """
        Returns true if the vectors in the upper 3x3 matrix form a right-
        handed coordinate system.
        """
    def Orthonormalize(self, issueWarning: bool = ...) -> bool:
        """
        Makes the matrix orthonormal in place.


        This is an iterative method that is much more stable than the previous
        cross/cross method. If the iterative method does not converge, a
        warning is issued.

        Returns true if the iteration converged, false otherwise. Leaves any
        translation part of the matrix unchanged. If *issueWarning* is true,
        this method will issue a warning if the iteration does not converge,
        otherwise it will be silent.
        """
    def RemoveScaleShear(self) -> Matrix4d:
        """
        Returns the matrix with any scaling or shearing removed, leaving only
        the rotation and translation.


        If the matrix cannot be decomposed, returns the original matrix.
        """
    def Set(self, _m00: float, _m01: float, _m02: float, _m03: float, _m10: float, _m11: float, _m12: float, _m13: float, _m20: float, _m21: float, _m22: float, _m23: float, _m30: float, _m31: float, _m32: float, _m33: float, /) -> Matrix4d:
        """
        Sets the matrix from 16 independent C{double} values, specified in
        row-major order.


        For example, parameter *m10* specifies the value in row 1 and column
        0.
        """
    def SetColumn(self, _i: int, _v: Vec4d | list[float] | tuple[float, float, float, float], /) -> None:
        """
        Sets a column of the matrix from a Vec4.
        """
    @overload
    def SetDiagonal(self, _s: float, /) -> Matrix4d:
        """
        Sets the matrix to *s* times the identity matrix.
        """
    @overload
    def SetDiagonal(self, _unknownArg1: Vec4d | list[float] | tuple[float, float, float, float], /) -> Matrix4d:
        """
        Sets the matrix to have diagonal ( C{v[0], v[1], v[2], v[3]} ).
        """
    def SetIdentity(self) -> Matrix4d:
        """
        Sets the matrix to the identity matrix.
        """
    @overload
    def SetLookAt(self, _eyePoint: Vec3d | list[float] | tuple[float, float, float], _centerPoint: Vec3d | list[float] | tuple[float, float, float], _upDirection: Vec3d | list[float] | tuple[float, float, float], /) -> Matrix4d:
        """
        Sets the matrix to specify a viewing matrix from parameters similar to
        those used by C{gluLookAt(3G)} .


        *eyePoint* represents the eye point in world space. *centerPoint*
        represents the world-space center of attention. *upDirection* is a
        vector indicating which way is up.
        """
    @overload
    def SetLookAt(self, _eyePoint: Vec3d | list[float] | tuple[float, float, float], _orientation: Rotation, /) -> Matrix4d:
        """
        Sets the matrix to specify a viewing matrix from a world-space
        *eyePoint* and a world-space rotation that rigidly rotates the
        orientation from its canonical frame, which is defined to be looking
        along the C{-z} axis with the C{+y} axis as the up direction.
        """
    @overload
    def SetRotate(self, _rot: Quatd | Quatf | Quath, /) -> Matrix4d:
        """
        Sets the matrix to specify a rotation equivalent to *rot*, and clears
        the translation.
        """
    @overload
    def SetRotate(self, _rot: Rotation, /) -> Matrix4d:
        """
        Sets the matrix to specify a rotation equivalent to *rot*, and clears
        the translation.
        """
    @overload
    def SetRotate(self, _mx: Matrix3d, /) -> Matrix4d:
        """
        Sets the matrix to specify a rotation equivalent to *mx*, and clears
        the translation.
        """
    @overload
    def SetRotateOnly(self, _rot: Quatd | Quatf | Quath, /) -> Matrix4d:
        """
        Sets the matrix to specify a rotation equivalent to *rot*, without
        clearing the translation.
        """
    @overload
    def SetRotateOnly(self, _rot: Rotation, /) -> Matrix4d:
        """
        Sets the matrix to specify a rotation equivalent to *rot*, without
        clearing the translation.
        """
    @overload
    def SetRotateOnly(self, _mx: Matrix3d, /) -> Matrix4d:
        """
        Sets the matrix to specify a rotation equivalent to *mx*, without
        clearing the translation.
        """
    def SetRow(self, _i: int, _v: Vec4d | list[float] | tuple[float, float, float, float], /) -> None:
        """
        Sets a row of the matrix from a Vec4.
        """
    def SetRow3(self, _i: int, _v: Vec3d | list[float] | tuple[float, float, float], /) -> None:
        """
        Sets a row of the matrix from a Vec3.


        The fourth element of the row is ignored.
        """
    @overload
    def SetScale(self, _scaleFactors: Vec3d | list[float] | tuple[float, float, float], /) -> Matrix4d:
        """
        Sets the matrix to specify a nonuniform scaling in x, y, and z by the
        factors in vector *scaleFactors*.
        """
    @overload
    def SetScale(self, _scaleFactor: float, /) -> Matrix4d:
        """
        Sets matrix to specify a uniform scaling by *scaleFactor*.
        """
    @overload
    def SetTransform(self, _rotate: Rotation, _translate: Vec3d | list[float] | tuple[float, float, float], /) -> Matrix4d:
        """
        Sets matrix to specify a rotation by *rotate* and a translation by
        *translate*.
        """
    @overload
    def SetTransform(self, _rotmx: Matrix3d, _translate: Vec3d | list[float] | tuple[float, float, float], /) -> Matrix4d:
        """
        Sets matrix to specify a rotation by *rotmx* and a translation by
        *translate*.
        """
    def SetTranslate(self, _trans: Vec3d | list[float] | tuple[float, float, float], /) -> Matrix4d:
        """
        Sets matrix to specify a translation by the vector *trans*, and clears
        the rotation.
        """
    def SetTranslateOnly(self, _t: Vec3d | list[float] | tuple[float, float, float], /) -> Matrix4d:
        """
        Sets matrix to specify a translation by the vector *trans*, without
        clearing the rotation.
        """
    def SetZero(self) -> Matrix4d:
        """
        Sets the matrix to zero.
        """
    @overload
    def Transform(self, _vec: Vec3d | list[float] | tuple[float, float, float], /) -> Vec3d:
        """
        Transforms the row vector *vec* by the matrix, returning the result.


        This treats the vector as a 4-component vector whose fourth component
        is 1.
        """
    @overload
    def Transform(self, _vec: Vec3f | list[float] | tuple[float, float, float], /) -> Vec3f:
        """
        Transforms the row vector *vec* by the matrix, returning the result.


        This treats the vector as a 4-component vector whose fourth component
        is 1. This is an overloaded method; it differs from the other version
        in that it returns a different value type.
        """
    @overload
    def TransformAffine(self, _vec: Vec3d | list[float] | tuple[float, float, float], /) -> Vec3d:
        """
        Transforms the row vector *vec* by the matrix, returning the result.


        This treats the vector as a 4-component vector whose fourth component
        is 1 and ignores the fourth column of the matrix (i.e. assumes it is
        (0, 0, 0, 1)).
        """
    @overload
    def TransformAffine(self, _vec: Vec3f | list[float] | tuple[float, float, float], /) -> Vec3f:
        """
        Transforms the row vector *vec* by the matrix, returning the result.


        This treats the vector as a 4-component vector whose fourth component
        is 1 and ignores the fourth column of the matrix (i.e. assumes it is
        (0, 0, 0, 1)).
        """
    @overload
    def TransformDir(self, _vec: Vec3d | list[float] | tuple[float, float, float], /) -> Vec3d:
        """
        Transforms row vector *vec* by the matrix, returning the result.


        This treats the vector as a direction vector, so the translation
        information in the matrix is ignored. That is, it treats the vector as
        a 4-component vector whose fourth component is 0.
        """
    @overload
    def TransformDir(self, _vec: Vec3f | list[float] | tuple[float, float, float], /) -> Vec3f:
        """
        Transforms row vector *vec* by the matrix, returning the result.


        This treats the vector as a direction vector, so the translation
        information in the matrix is ignored. That is, it treats the vector as
        a 4-component vector whose fourth component is 0. This is an
        overloaded method; it differs from the other version in that it
        returns a different value type.
        """
    def __add__(self, arg2: Matrix4d, /) -> Any: ...
    @overload
    def __contains__(self, arg2: float, /) -> bool:
        """Check rows against GfVec"""
    @overload
    def __contains__(self, arg2: Vec4d | list[float] | tuple[float, float, float, float], /) -> bool:
        """Check rows against GfVec"""
    def __eq__(self, other: object) -> bool:
        """
        Tests for element-wise matrix equality.


        All elements must match exactly for matrices to be considered equal.
        """
    def __getinitargs__(self) -> tuple: ...
    @overload
    def __getitem__(self, _i: tuple, /) -> float:
        """
        Accesses an indexed row *i* of the matrix as an array of 4 C{double}
        values so that standard indexing (such as C{m[0][1]} ) works
        correctly.
        """
    @overload
    def __getitem__(self, arg2: int, /) -> Vec4d: ...
    def __hash__(self) -> int: ...
    def __iadd__(self, arg2: Matrix4d, /) -> Any: ...
    @overload
    def __imul__(self, arg2: Matrix4d, /) -> Any: ...
    @overload
    def __imul__(self, arg2: float, /) -> Any: ...
    def __isub__(self, arg2: Matrix4d, /) -> Any: ...
    def __len__(self) -> int:
        """Return number of rows"""
    @overload
    def __mul__(self, arg2: Matrix4d, /) -> Any: ...
    @overload
    def __mul__(self, arg2: float, /) -> Any: ...
    @overload
    def __mul__(self, arg2: Vec4d | list[float] | tuple[float, float, float, float], /) -> Any: ...
    @overload
    def __mul__(self, arg2: Vec4f | list[float] | tuple[float, float, float, float], /) -> Any: ...
    def __ne__(self, other: object) -> bool: ...
    def __neg__(self) -> Any: ...
    @overload
    def __rmul__(self, arg2: float, /) -> Any: ...
    @overload
    def __rmul__(self, arg2: Vec4d | list[float] | tuple[float, float, float, float], /) -> Any: ...
    @overload
    def __rmul__(self, arg2: Vec4f | list[float] | tuple[float, float, float, float], /) -> Any: ...
    @overload
    def __setitem__(self, arg2: tuple, arg3: float, /) -> None: ...
    @overload
    def __setitem__(self, arg2: int, arg3: Vec4d | list[float] | tuple[float, float, float, float], /) -> None: ...
    def __sub__(self, arg2: Matrix4d, /) -> Any: ...
    def __truediv__(self, arg2: Matrix4d, /) -> Any: ...

class Matrix4f(Boost.Python.instance):
    """
    Stores a 4x4 matrix of C{float} elements.


    A basic type.

    Matrices are defined to be in row-major order, so C{matrix[i][j]}
    indexes the element in the *i* th row and the *j* th column.

    3D Transformations
    ==================

    The following methods interpret a GfMatrix4f as a 3D transformation:
    SetRotate() , SetScale() , SetTranslate() , SetLookAt() , Factor() ,
    ExtractTranslation() , ExtractRotation() , Transform() ,
    TransformDir() . By convention, vectors are treated primarily as row
    vectors, implying the following:
       - Transformation matrices are organized to deal with row vectors,
         not column vectors. For example, the last row of a matrix contains the
         translation amounts.

       - Each of the Set() methods below completely rewrites the matrix;
         for example, SetTranslate() yields a matrix which does nothing but
         translate.

       - When multiplying two transformation matrices, the matrix on the
         left applies a more local transformation to a row vector. For example,
         if R represents a rotation matrix and T represents a translation
         matrix, the product R*T will rotate a row vector, then translate it.

    """
    dimension: ClassVar[tuple] = ...  # read-only
    __safe_for_unpickling__: ClassVar[bool] = ...
    @overload
    def __init__(self) -> None:
        """
        Default constructor. Leaves the matrix component values undefined.
        """
    @overload
    def __init__(self, _m00: float, _m01: float, _m02: float, _m03: float, _m10: float, _m11: float, _m12: float, _m13: float, _m20: float, _m21: float, _m22: float, _m23: float, _m30: float, _m31: float, _m32: float, _m33: float, /) -> None:
        """
        Constructor.


        Initializes the matrix from 16 independent C{float} values, specified
        in row-major order. For example, parameter *m10* specifies the value
        in row 1 and column 0.
        """
    @overload
    def __init__(self, _v: Vec4f | list[float] | tuple[float, float, float, float], /) -> None:
        """
        Constructor.


        Explicitly initializes the matrix to diagonal form, with the *i* th
        element on the diagonal set to C{v[i]} .
        """
    @overload
    def __init__(self, _r0: typing.Iterable[float], _r1: typing.Iterable[float], _r2: typing.Iterable[float], _r3: typing.Iterable[float], /) -> None:
        """
        Constructor.


        Initialize the matrix from 4 row vectors of double. Each vector is
        expected to length 4. If it is too big, only the first 4 items will be
        used. If it is too small, uninitialized elements will be filled in
        with the corresponding elements from an identity matrix.
        """
    @overload
    def __init__(self, _rotate: Rotation, _translate: Vec3f | list[float] | tuple[float, float, float], /) -> None:
        """
        Constructor.


        Initializes a transformation matrix to perform the indicated rotation
        and translation.
        """
    @overload
    def __init__(self, _rotmx: Matrix3f, _translate: Vec3f | list[float] | tuple[float, float, float], /) -> None:
        """
        Constructor.


        Initializes a transformation matrix to perform the indicated rotation
        and translation.
        """
    @overload
    def __init__(self, _m: Matrix4d, /) -> None:
        '''
        This explicit constructor converts a"double"matrix to a"float"matrix.
        '''
    @overload
    def __init__(self, arg2: Matrix4f, /) -> None: ...
    @overload
    def __init__(self, arg2: int, /) -> None: ...
    @overload
    def __init__(self, arg2: float, /) -> None: ...
    @overload
    def __init__(self, arg2: object, /) -> None: ...
    @overload
    def __init__(self, arg2: object, arg3: object, arg4: object, arg5: object, /) -> None: ...
    def ExtractRotation(self) -> Rotation:
        """
        Returns the rotation corresponding to this matrix.


        This works well only if the matrix represents a rotation.

        For good results, consider calling Orthonormalize() before calling
        this method.
        """
    def ExtractRotationMatrix(self) -> Matrix3f:
        """
        Returns the rotation corresponding to this matrix.


        This works well only if the matrix represents a rotation.

        For good results, consider calling Orthonormalize() before calling
        this method.
        """
    def ExtractRotationQuat(self) -> Quatf:
        """
        Return the rotation corresponding to this matrix as a quaternion.


        This works well only if the matrix represents a rotation.

        For good results, consider calling Orthonormalize() before calling
        this method.
        """
    def ExtractTranslation(self) -> Vec3f:
        """
        Returns the translation part of the matrix, defined as the first three
        elements of the last row.
        """
    def Factor(self, _eps: float = ..., /) -> tuple:
        """
        Factors the matrix into 5 components:



           - C{*M* = r * s * -r * u * t} where

           - *t* is a translation.

           - *u* and *r* are rotations, and *-r* is the transpose (inverse) of
             *r*. The *u* matrix may contain shear information.

           - *s* is a scale. Any projection information could be returned in
             matrix *p*, but currently p is never modified.
             Returns C{false} if the matrix is singular (as determined by *eps*).
             In that case, any zero scales in *s* are clamped to *eps* to allow
             computation of *u*.
        """
    def GetColumn(self, _i: int, /) -> Vec4f:
        """
        Gets a column of the matrix as a Vec4.
        """
    def GetDeterminant(self) -> float:
        """
        Returns the determinant of the matrix.
        """
    def GetDeterminant3(self) -> float:
        """
        Returns the determinant of the upper 3x3 matrix.


        This method is useful when the matrix describes a linear
        transformation such as a rotation or scale because the other values in
        the 4x4 matrix are not important.
        """
    def GetHandedness(self) -> float:
        """
        Returns the sign of the determinant of the upper 3x3 matrix, i.e.


        1 for a right-handed matrix, -1 for a left-handed matrix, and 0 for a
        singular matrix.
        """
    def GetInverse(self) -> Matrix4f:
        """
        Returns the inverse of the matrix, or FLT_MAX * SetIdentity() if the
        matrix is singular.


        (FLT_MAX is the largest value a C{float} can have, as defined by the
        system.) The matrix is considered singular if the determinant is less
        than or equal to the optional parameter *eps*. If *det* is non-null,
        C{*det} is set to the determinant.
        """
    def GetOrthonormalized(self, issueWarning: bool = ...) -> Matrix4f:
        """
        Returns an orthonormalized copy of the matrix.
        """
    def GetRow(self, _i: int, /) -> Vec4f:
        """
        Gets a row of the matrix as a Vec4.
        """
    def GetRow3(self, _i: int, /) -> Vec3f:
        """
        Gets a row of the matrix as a Vec3.
        """
    def GetTranspose(self) -> Matrix4f:
        """
        Returns the transpose of the matrix.
        """
    def HasOrthogonalRows3(self) -> bool:
        """
        Returns true, if the row vectors of the upper 3x3 matrix form an
        orthogonal basis.


        Note they do not have to be unit length for this test to return true.
        """
    def IsLeftHanded(self) -> bool:
        """
        Returns true if the vectors in the upper 3x3 matrix form a left-handed
        coordinate system.
        """
    def IsRightHanded(self) -> bool:
        """
        Returns true if the vectors in the upper 3x3 matrix form a right-
        handed coordinate system.
        """
    def Orthonormalize(self, issueWarning: bool = ...) -> bool:
        """
        Makes the matrix orthonormal in place.


        This is an iterative method that is much more stable than the previous
        cross/cross method. If the iterative method does not converge, a
        warning is issued.

        Returns true if the iteration converged, false otherwise. Leaves any
        translation part of the matrix unchanged. If *issueWarning* is true,
        this method will issue a warning if the iteration does not converge,
        otherwise it will be silent.
        """
    def RemoveScaleShear(self) -> Matrix4f:
        """
        Returns the matrix with any scaling or shearing removed, leaving only
        the rotation and translation.


        If the matrix cannot be decomposed, returns the original matrix.
        """
    def Set(self, _m00: float, _m01: float, _m02: float, _m03: float, _m10: float, _m11: float, _m12: float, _m13: float, _m20: float, _m21: float, _m22: float, _m23: float, _m30: float, _m31: float, _m32: float, _m33: float, /) -> Matrix4f:
        """
        Sets the matrix from 16 independent C{float} values, specified in row-
        major order.


        For example, parameter *m10* specifies the value in row 1 and column
        0.
        """
    def SetColumn(self, _i: int, _v: Vec4f | list[float] | tuple[float, float, float, float], /) -> None:
        """
        Sets a column of the matrix from a Vec4.
        """
    @overload
    def SetDiagonal(self, _s: float, /) -> Matrix4f:
        """
        Sets the matrix to *s* times the identity matrix.
        """
    @overload
    def SetDiagonal(self, _unknownArg1: Vec4f | list[float] | tuple[float, float, float, float], /) -> Matrix4f:
        """
        Sets the matrix to have diagonal ( C{v[0], v[1], v[2], v[3]} ).
        """
    def SetIdentity(self) -> Matrix4f:
        """
        Sets the matrix to the identity matrix.
        """
    @overload
    def SetLookAt(self, _eyePoint: Vec3f | list[float] | tuple[float, float, float], _centerPoint: Vec3f | list[float] | tuple[float, float, float], _upDirection: Vec3f | list[float] | tuple[float, float, float], /) -> Matrix4f:
        """
        Sets the matrix to specify a viewing matrix from parameters similar to
        those used by C{gluLookAt(3G)} .


        *eyePoint* represents the eye point in world space. *centerPoint*
        represents the world-space center of attention. *upDirection* is a
        vector indicating which way is up.
        """
    @overload
    def SetLookAt(self, _eyePoint: Vec3f | list[float] | tuple[float, float, float], _orientation: Rotation, /) -> Matrix4f:
        """
        Sets the matrix to specify a viewing matrix from a world-space
        *eyePoint* and a world-space rotation that rigidly rotates the
        orientation from its canonical frame, which is defined to be looking
        along the C{-z} axis with the C{+y} axis as the up direction.
        """
    @overload
    def SetRotate(self, _rot: Quatf | Quath, /) -> Matrix4f:
        """
        Sets the matrix to specify a rotation equivalent to *rot*, and clears
        the translation.
        """
    @overload
    def SetRotate(self, _rot: Rotation, /) -> Matrix4f:
        """
        Sets the matrix to specify a rotation equivalent to *rot*, and clears
        the translation.
        """
    @overload
    def SetRotate(self, _mx: Matrix3f, /) -> Matrix4f:
        """
        Sets the matrix to specify a rotation equivalent to *mx*, and clears
        the translation.
        """
    @overload
    def SetRotateOnly(self, _rot: Quatf | Quath, /) -> Matrix4f:
        """
        Sets the matrix to specify a rotation equivalent to *rot*, without
        clearing the translation.
        """
    @overload
    def SetRotateOnly(self, _rot: Rotation, /) -> Matrix4f:
        """
        Sets the matrix to specify a rotation equivalent to *rot*, without
        clearing the translation.
        """
    @overload
    def SetRotateOnly(self, _mx: Matrix3f, /) -> Matrix4f:
        """
        Sets the matrix to specify a rotation equivalent to *mx*, without
        clearing the translation.
        """
    def SetRow(self, _i: int, _v: Vec4f | list[float] | tuple[float, float, float, float], /) -> None:
        """
        Sets a row of the matrix from a Vec4.
        """
    def SetRow3(self, _i: int, _v: Vec3f | list[float] | tuple[float, float, float], /) -> None:
        """
        Sets a row of the matrix from a Vec3.


        The fourth element of the row is ignored.
        """
    @overload
    def SetScale(self, _scaleFactors: Vec3f | list[float] | tuple[float, float, float], /) -> Matrix4f:
        """
        Sets the matrix to specify a nonuniform scaling in x, y, and z by the
        factors in vector *scaleFactors*.
        """
    @overload
    def SetScale(self, _scaleFactor: float, /) -> Matrix4f:
        """
        Sets matrix to specify a uniform scaling by *scaleFactor*.
        """
    @overload
    def SetTransform(self, _rotate: Rotation, _translate: Vec3f | list[float] | tuple[float, float, float], /) -> Matrix4f:
        """
        Sets matrix to specify a rotation by *rotate* and a translation by
        *translate*.
        """
    @overload
    def SetTransform(self, _rotmx: Matrix3f, _translate: Vec3f | list[float] | tuple[float, float, float], /) -> Matrix4f:
        """
        Sets matrix to specify a rotation by *rotmx* and a translation by
        *translate*.
        """
    def SetTranslate(self, _trans: Vec3f | list[float] | tuple[float, float, float], /) -> Matrix4f:
        """
        Sets matrix to specify a translation by the vector *trans*, and clears
        the rotation.
        """
    def SetTranslateOnly(self, _t: Vec3f | list[float] | tuple[float, float, float], /) -> Matrix4f:
        """
        Sets matrix to specify a translation by the vector *trans*, without
        clearing the rotation.
        """
    def SetZero(self) -> Matrix4f:
        """
        Sets the matrix to zero.
        """
    @overload
    def Transform(self, _vec: Vec3d | list[float] | tuple[float, float, float], /) -> Vec3d:
        """
        Transforms the row vector *vec* by the matrix, returning the result.


        This treats the vector as a 4-component vector whose fourth component
        is 1.
        """
    @overload
    def Transform(self, _vec: Vec3f | list[float] | tuple[float, float, float], /) -> Vec3f:
        """
        Transforms the row vector *vec* by the matrix, returning the result.


        This treats the vector as a 4-component vector whose fourth component
        is 1. This is an overloaded method; it differs from the other version
        in that it returns a different value type.
        """
    @overload
    def TransformAffine(self, _vec: Vec3d | list[float] | tuple[float, float, float], /) -> Vec3d:
        """
        Transforms the row vector *vec* by the matrix, returning the result.


        This treats the vector as a 4-component vector whose fourth component
        is 1 and ignores the fourth column of the matrix (i.e. assumes it is
        (0, 0, 0, 1)).
        """
    @overload
    def TransformAffine(self, _vec: Vec3f | list[float] | tuple[float, float, float], /) -> Vec3f:
        """
        Transforms the row vector *vec* by the matrix, returning the result.


        This treats the vector as a 4-component vector whose fourth component
        is 1 and ignores the fourth column of the matrix (i.e. assumes it is
        (0, 0, 0, 1)).
        """
    @overload
    def TransformDir(self, _vec: Vec3d | list[float] | tuple[float, float, float], /) -> Vec3d:
        """
        Transforms row vector *vec* by the matrix, returning the result.


        This treats the vector as a direction vector, so the translation
        information in the matrix is ignored. That is, it treats the vector as
        a 4-component vector whose fourth component is 0.
        """
    @overload
    def TransformDir(self, _vec: Vec3f | list[float] | tuple[float, float, float], /) -> Vec3f:
        """
        Transforms row vector *vec* by the matrix, returning the result.


        This treats the vector as a direction vector, so the translation
        information in the matrix is ignored. That is, it treats the vector as
        a 4-component vector whose fourth component is 0. This is an
        overloaded method; it differs from the other version in that it
        returns a different value type.
        """
    def __add__(self, arg2: Matrix4f, /) -> Any: ...
    @overload
    def __contains__(self, arg2: float, /) -> bool:
        """Check rows against GfVec"""
    @overload
    def __contains__(self, arg2: Vec4f | list[float] | tuple[float, float, float, float], /) -> bool:
        """Check rows against GfVec"""
    def __eq__(self, other: object) -> bool:
        """
        Tests for element-wise matrix equality.


        All elements must match exactly for matrices to be considered equal.
        """
    def __getinitargs__(self) -> tuple: ...
    @overload
    def __getitem__(self, _i: tuple, /) -> float:
        """
        Accesses an indexed row *i* of the matrix as an array of 4 C{float}
        values so that standard indexing (such as C{m[0][1]} ) works
        correctly.
        """
    @overload
    def __getitem__(self, arg2: int, /) -> Vec4f: ...
    def __hash__(self) -> int: ...
    def __iadd__(self, arg2: Matrix4f, /) -> Any: ...
    @overload
    def __imul__(self, arg2: Matrix4f, /) -> Any: ...
    @overload
    def __imul__(self, arg2: float, /) -> Any: ...
    def __isub__(self, arg2: Matrix4f, /) -> Any: ...
    def __len__(self) -> int:
        """Return number of rows"""
    @overload
    def __mul__(self, arg2: Matrix4f, /) -> Any: ...
    @overload
    def __mul__(self, arg2: float, /) -> Any: ...
    @overload
    def __mul__(self, arg2: Vec4f | list[float] | tuple[float, float, float, float], /) -> Any: ...
    def __ne__(self, other: object) -> bool: ...
    def __neg__(self) -> Any: ...
    @overload
    def __rmul__(self, arg2: float, /) -> Any: ...
    @overload
    def __rmul__(self, arg2: Vec4f | list[float] | tuple[float, float, float, float], /) -> Any: ...
    @overload
    def __setitem__(self, arg2: tuple, arg3: float, /) -> None: ...
    @overload
    def __setitem__(self, arg2: int, arg3: Vec4f | list[float] | tuple[float, float, float, float], /) -> None: ...
    def __sub__(self, arg2: Matrix4f, /) -> Any: ...
    def __truediv__(self, arg2: Matrix4f, /) -> Any: ...

class MultiInterval(Boost.Python.instance):
    """
    GfMultiInterval represents a subset of the real number line as an
    ordered set of non-intersecting GfIntervals.
    """
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, _i: Interval, /) -> None:
        """
        Constructs an multi-interval with the single given interval.
        """
    @overload
    def __init__(self, _intervals: typing.Iterable[Interval], /) -> None:
        """
        Constructs an multi-interval containing the given input intervals.
        """
    @overload
    def __init__(self, arg2: MultiInterval, /) -> None: ...
    @overload
    def Add(self, _i: Interval, /) -> None:
        """
        Add the given interval to the multi-interval.
        """
    @overload
    def Add(self, _s: MultiInterval, /) -> None:
        """
        Add the given multi-interval to the multi-interval.


        Sets this object to the union of the two sets.
        """
    def ArithmeticAdd(self, _i: Interval, /) -> None:
        """
        Uses the given interval to extend the multi-interval in the interval
        arithmetic sense.
        """
    def Clear(self) -> None:
        """
        Clear the multi-interval.
        """
    @overload
    def Contains(self, _d: float, /) -> bool:
        """
        Returns true if the multi-interval contains the given value.
        """
    @overload
    def Contains(self, _i: Interval, /) -> bool:
        """
        Returns true if the multi-interval contains the given interval.
        """
    @overload
    def Contains(self, _s: MultiInterval, /) -> bool:
        """
        Returns true if the multi-interval contains all the intervals in the
        given multi-interval.
        """
    def GetBounds(self) -> Interval:
        """
        Returns an interval bounding the entire multi-interval.


        Returns an empty interval if the multi-interval is empty.
        """
    def GetComplement(self) -> MultiInterval:
        """
        Return the complement of this set.
        """
    def GetContainingInterval(self, _x: float, /) -> pxr.Usd.PrimSiblingIterator:
        """
        Returns an iterator identifying the interval that contains x.


        If no interval contains x, then it returns end()
        """
    @staticmethod
    def GetFullInterval() -> MultiInterval:
        """
        Returns the full interval (-inf, inf).
        """
    def GetNextNonContainingInterval(self, _x: float, /) -> pxr.Usd.PrimSiblingIterator:
        """
        Returns an iterator identifying the first (lowest) interval whose
        minimum value is>x.


        If no such interval exists, returns end().
        """
    def GetPriorNonContainingInterval(self, _x: float, /) -> pxr.Usd.PrimSiblingIterator:
        """
        Returns an iterator identifying the last (highest) interval whose
        maximum value is<x.


        If no such interval exists, returns end().
        """
    def GetSize(self) -> int:
        """
        Returns the number of intervals in the set.
        """
    @overload
    def Intersect(self, _i: Interval, /) -> None: ...
    @overload
    def Intersect(self, _s: MultiInterval, /) -> None: ...
    def IsEmpty(self) -> bool:
        """
        Returns true if the multi-interval is empty.
        """
    @overload
    def Remove(self, _i: Interval, /) -> None:
        """
        Remove the given interval from this multi-interval.
        """
    @overload
    def Remove(self, _s: MultiInterval, /) -> None:
        """
        Remove the given multi-interval from this multi-interval.
        """
    def __eq__(self, other: object) -> bool: ...
    def __ge__(self, other: object) -> bool: ...
    def __gt__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    def __iter__(self) -> Any: ...
    def __le__(self, other: object) -> bool: ...
    def __lt__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    @property
    def bounds(self) -> Interval:
        """
        Returns an interval bounding the entire multi-interval.


        Returns an empty interval if the multi-interval is empty.
        """
    @property
    def isEmpty(self) -> bool:
        """
        Returns true if the multi-interval is empty.
        """
    @property
    def size(self) -> int:
        """
        Returns the number of intervals in the set.
        """

class Plane(Boost.Python.instance):
    """
    Basic type: 3-dimensional plane.


    This class represents a three-dimensional plane as a normal vector and
    the distance of the plane from the origin, measured along the normal.
    The plane can also be used to represent a half-space: the side of the
    plane in the direction of the normal.
    """
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None:
        """
        The default constructor leaves the plane parameters undefined.
        """
    @overload
    def __init__(self, _normal: Vec3d | list[float] | tuple[float, float, float], _distanceToOrigin: float, /) -> None:
        """
        This constructor sets this to the plane perpendicular to C{normal} and
        at C{distance} units from the origin.


        The passed-in normal is normalized to unit length first.
        """
    @overload
    def __init__(self, _normal: Vec3d | list[float] | tuple[float, float, float], _point: Vec3d | list[float] | tuple[float, float, float], /) -> None:
        """
        This constructor sets this to the plane perpendicular to C{normal} and
        that passes through C{point}.


        The passed-in normal is normalized to unit length first.
        """
    @overload
    def __init__(self, _p0: Vec3d | list[float] | tuple[float, float, float], _p1: Vec3d | list[float] | tuple[float, float, float], _p2: Vec3d | list[float] | tuple[float, float, float], /) -> None:
        """
        This constructor sets this to the plane that contains the three given
        points.


        The normal is constructed from the cross product of ( C{p1} - C{p0}) (
        C{p2} - C{p0}). Results are undefined if the points are collinear.
        """
    @overload
    def __init__(self, _eqn: Vec4d | list[float] | tuple[float, float, float, float], /) -> None:
        """
        This constructor creates a plane given by the equation C{eqn} [0] * x
        + C{eqn} [1] * y + C{eqn} [2] * z + C{eqn} [3] = 0.
        """
    def GetDistance(self, _p: Vec3d | list[float] | tuple[float, float, float], /) -> float:
        """
        Returns the distance of point C{from} the plane.


        This distance will be positive if the point is on the side of the
        plane containing the normal.
        """
    def GetDistanceFromOrigin(self) -> float:
        """
        Returns the distance of the plane from the origin.
        """
    def GetEquation(self) -> Vec4d:
        """
        Give the coefficients of the equation of the plane.


        Suitable to OpenGL calls to set the clipping plane.
        """
    def GetNormal(self) -> Vec3d:
        """
        Returns the unit-length normal vector of the plane.
        """
    @overload
    def IntersectsPositiveHalfSpace(self, _box: Range3d | list[float] | tuple[float, float, float], /) -> bool:
        """
        Returns C{true} if the given aligned bounding box is at least
        partially on the positive side (the one the normal points into) of the
        plane.
        """
    @overload
    def IntersectsPositiveHalfSpace(self, _pt: Vec3d | list[float] | tuple[float, float, float], /) -> bool:
        """
        Returns true if the given point is on the plane or within its positive
        half space.
        """
    def Project(self, _p: Vec3d | list[float] | tuple[float, float, float], /) -> Vec3d:
        """
        Return the projection of C{p} onto the plane.
        """
    def Reorient(self, _p: Vec3d | list[float] | tuple[float, float, float], /) -> Plane:
        """
        Flip the plane normal (if necessary) so that C{p} is in the positive
        halfspace.
        """
    @overload
    def Set(self, _normal: Vec3d | list[float] | tuple[float, float, float], _distanceToOrigin: float, /) -> Plane:
        """
        Sets this to the plane perpendicular to C{normal} and at C{distance}
        units from the origin.


        The passed-in normal is normalized to unit length first.
        """
    @overload
    def Set(self, _normal: Vec3d | list[float] | tuple[float, float, float], _point: Vec3d | list[float] | tuple[float, float, float], /) -> Plane:
        """
        This constructor sets this to the plane perpendicular to C{normal} and
        that passes through C{point}.


        The passed-in normal is normalized to unit length first.
        """
    @overload
    def Set(self, _p0: Vec3d | list[float] | tuple[float, float, float], _p1: Vec3d | list[float] | tuple[float, float, float], _p2: Vec3d | list[float] | tuple[float, float, float], /) -> Plane:
        """
        This constructor sets this to the plane that contains the three given
        points.


        The normal is constructed from the cross product of ( C{p1} - C{p0}) (
        C{p2} - C{p0}). Results are undefined if the points are collinear.
        """
    @overload
    def Set(self, _eqn: Vec4d | list[float] | tuple[float, float, float, float], /) -> Plane:
        """
        This method sets this to the plane given by the equation C{eqn} [0] *
        x + C{eqn} [1] * y + C{eqn} [2] * z + C{eqn} [3] = 0.
        """
    def Transform(self, _matrix: Matrix4d, /) -> Plane:
        """
        Transforms the plane by the given matrix.
        """
    def __eq__(self, other: object) -> bool:
        """
        Component-wise equality test.


        The normals and distances must match exactly for planes to be
        considered equal.
        """
    def __ne__(self, other: object) -> bool: ...
    @property
    def distanceFromOrigin(self) -> float:
        """
        Returns the distance of the plane from the origin.
        """
    @property
    def normal(self) -> Vec3d:
        """
        Returns the unit-length normal vector of the plane.
        """

class Quatd(Boost.Python.instance):
    """
    Basic type: a quaternion, a complex number with a real coefficient and
    three imaginary coefficients, stored as a 3-vector.
    """
    imaginary: Vec3d
    real: float
    @overload
    def __init__(self) -> None:
        """
        Default constructor leaves the quaternion undefined.
        """
    @overload
    def __init__(self, real: float) -> None:
        """
        Initialize the real coefficient to C{realVal} and the imaginary
        coefficients to zero.


        Since quaternions typically must be normalized, reasonable values for
        C{realVal} are -1, 0, or 1. Other values are legal but are likely to
        be meaningless.
        """
    @overload
    def __init__(self, real: float, i: float, j: float, k: float) -> None:
        """
        Initialize the real and imaginary coefficients.
        """
    @overload
    def __init__(self, real: float, imaginary: Vec3d | list[float] | tuple[float, float, float]) -> None:
        """
        Initialize the real and imaginary coefficients.
        """
    @overload
    def __init__(self, arg2: Quatd | Quatf | Quath, /) -> None: ...
    def GetConjugate(self) -> Quatd:
        """
        Return this quaternion's conjugate, which is the quaternion with the
        same real coefficient and negated imaginary coefficients.
        """
    @staticmethod
    def GetIdentity() -> Quatd:
        """
        Return the identity quaternion, with real coefficient 1 and an
        imaginary coefficients all zero.
        """
    def GetImaginary(self) -> Vec3d:
        """
        Return the imaginary coefficient.
        """
    def GetInverse(self) -> Quatd:
        """
        Return this quaternion's inverse, or reciprocal.


        This is the quaternion's conjugate divided by it's squared length.
        """
    def GetLength(self) -> float:
        """
        Return geometric length of this quaternion.
        """
    def GetNormalized(self, eps: float = ...) -> Quatd:
        """
        length of this quaternion is smaller than C{eps}, return the identity
        quaternion.
        """
    def GetReal(self) -> float:
        """
        Return the real coefficient.
        """
    @staticmethod
    def GetZero() -> Quatd:
        """
        Return the zero quaternion, with real coefficient 0 and an imaginary
        coefficients all zero.
        """
    def Normalize(self, eps: float = ...) -> Quatd:
        """
        Normalizes this quaternion in place to unit length, returning the
        length before normalization.


        If the length of this quaternion is smaller than C{eps}, this sets the
        quaternion to identity.
        """
    @overload
    def SetImaginary(self, _imaginary: Vec3d | list[float] | tuple[float, float, float], /) -> None:
        """
        Set the imaginary coefficients.
        """
    @overload
    def SetImaginary(self, i: float, j: float, k: float) -> None:
        """
        Set the imaginary coefficients.
        """
    def SetReal(self, _real: float, /) -> None:
        """
        Set the real coefficient.
        """
    def Transform(self, _point: Vec3d | list[float] | tuple[float, float, float], /) -> Vec3d:
        """
        Transform the GfVec3d point.


        If the quaternion is normalized, the transformation is a rotation.
        Given a GfQuatd q, q.Transform(point) is equivalent to: (q *
        GfQuatd(0, point) * q.GetInverse()).GetImaginary() but is more
        efficient.
        """
    def __add__(self, arg2: Quatd | Quatf | Quath, /) -> Any: ...
    def __eq__(self, other: object) -> bool:
        """
        Component-wise quaternion equality test.


        The real and imaginary parts must match exactly for quaternions to be
        considered equal.
        """
    def __hash__(self) -> int: ...
    def __iadd__(self, arg2: Quatd | Quatf | Quath, /) -> Any: ...
    def __idiv__(self, arg2: float, /) -> Any: ...
    @overload
    def __imul__(self, arg2: Quatd | Quatf | Quath, /) -> Any: ...
    @overload
    def __imul__(self, arg2: float, /) -> Any: ...
    def __isub__(self, arg2: Quatd | Quatf | Quath, /) -> Any: ...
    def __itruediv__(self, arg2: float, /) -> Quatd: ...
    @overload
    def __mul__(self, arg2: Quatd | Quatf | Quath, /) -> Any: ...
    @overload
    def __mul__(self, arg2: float, /) -> Any: ...
    def __ne__(self, other: object) -> bool: ...
    def __neg__(self) -> Any: ...
    def __rmul__(self, arg2: float, /) -> Any: ...
    def __sub__(self, arg2: Quatd | Quatf | Quath, /) -> Any: ...
    def __truediv__(self, arg2: float, /) -> Any: ...

class Quaternion(Boost.Python.instance):
    """
    Basic type: complex number with scalar real part and vector imaginary
    part.


    This class represents a generalized complex number that has a scalar
    real part and a vector of three imaginary values. Quaternions are used
    by the C{GfRotation} class to represent arbitrary-axis rotations.
    """
    __instance_size__: ClassVar[int] = ...
    imaginary: Vec3d
    real: float
    @overload
    def __init__(self) -> None:
        """
        The default constructor leaves the quaternion undefined.
        """
    @overload
    def __init__(self, _realVal: Quaternion, /) -> None:
        """
        This constructor initializes the real part to the argument and the
        imaginary parts to zero.


        Since quaternions typically need to be normalized, the only reasonable
        values for C{realVal} are -1, 0, or 1. Other values are legal but are
        likely to be meaningless.
        """
    @overload
    def __init__(self, _real: float, _imaginary: Vec3d | list[float] | tuple[float, float, float], /) -> None:
        """
        This constructor initializes the real and imaginary parts.
        """
    @overload
    def __init__(self, arg2: int, /) -> None: ...
    @staticmethod
    def GetIdentity() -> Quaternion:
        """
        Returns the identity quaternion, which has a real part of 1 and an
        imaginary part of (0,0,0).
        """
    def GetImaginary(self) -> Vec3d:
        """
        Returns the imaginary part of the quaternion.
        """
    def GetInverse(self) -> Quaternion:
        """
        Returns the inverse of this quaternion.
        """
    def GetLength(self) -> float:
        """
        Returns geometric length of this quaternion.
        """
    def GetNormalized(self, _eps: float = ..., /) -> Quaternion:
        """
        Returns a normalized (unit-length) version of this quaternion.


        direction as this. If the length of this quaternion is smaller than
        C{eps}, this returns the identity quaternion.
        """
    def GetReal(self) -> float:
        """
        Returns the real part of the quaternion.
        """
    @staticmethod
    def GetZero() -> Quaternion:
        """
        Returns the zero quaternion, which has a real part of 0 and an
        imaginary part of (0,0,0).
        """
    def Normalize(self, _eps: float = ..., /) -> Quaternion:
        """
        Normalizes this quaternion in place to unit length, returning the
        length before normalization.


        If the length of this quaternion is smaller than C{eps}, this sets the
        quaternion to identity.
        """
    def __add__(self, arg2: Quaternion, /) -> Any: ...
    def __eq__(self, other: object) -> bool:
        """
        Component-wise quaternion equality test.


        The real and imaginary parts must match exactly for quaternions to be
        considered equal.
        """
    def __hash__(self) -> int: ...
    def __iadd__(self, arg2: Quaternion, /) -> Any: ...
    def __idiv__(self, arg2: float, /) -> Any: ...
    @overload
    def __imul__(self, arg2: Quaternion, /) -> Any: ...
    @overload
    def __imul__(self, arg2: float, /) -> Any: ...
    def __isub__(self, arg2: Quaternion, /) -> Any: ...
    def __itruediv__(self, arg2: float, /) -> Quaternion: ...
    @overload
    def __mul__(self, arg2: Quaternion, /) -> Any: ...
    @overload
    def __mul__(self, arg2: float, /) -> Any: ...
    def __ne__(self, other: object) -> bool: ...
    def __rmul__(self, arg2: float, /) -> Any: ...
    def __sub__(self, arg2: Quaternion, /) -> Any: ...
    def __truediv__(self, arg2: float, /) -> Any: ...

class Quatf(Boost.Python.instance):
    """
    Basic type: a quaternion, a complex number with a real coefficient and
    three imaginary coefficients, stored as a 3-vector.
    """
    imaginary: Vec3f
    real: float
    @overload
    def __init__(self) -> None:
        """
        Default constructor leaves the quaternion undefined.
        """
    @overload
    def __init__(self, real: float) -> None:
        """
        Initialize the real coefficient to C{realVal} and the imaginary
        coefficients to zero.


        Since quaternions typically must be normalized, reasonable values for
        C{realVal} are -1, 0, or 1. Other values are legal but are likely to
        be meaningless.
        """
    @overload
    def __init__(self, real: float, i: float, j: float, k: float) -> None:
        """
        Initialize the real and imaginary coefficients.
        """
    @overload
    def __init__(self, real: float, imaginary: Vec3f | list[float] | tuple[float, float, float]) -> None:
        """
        Initialize the real and imaginary coefficients.
        """
    @overload
    def __init__(self, _other: Quatd | Quatf | Quath, /) -> None:
        """
        Construct from GfQuatd.
        """
    @overload
    def __init__(self, _other: Quatf | Quath, /) -> None:
        """
        Implicitly convert from GfQuath.
        """
    def GetConjugate(self) -> Quatf:
        """
        Return this quaternion's conjugate, which is the quaternion with the
        same real coefficient and negated imaginary coefficients.
        """
    @staticmethod
    def GetIdentity() -> Quatf:
        """
        Return the identity quaternion, with real coefficient 1 and an
        imaginary coefficients all zero.
        """
    def GetImaginary(self) -> Vec3f:
        """
        Return the imaginary coefficient.
        """
    def GetInverse(self) -> Quatf:
        """
        Return this quaternion's inverse, or reciprocal.


        This is the quaternion's conjugate divided by it's squared length.
        """
    def GetLength(self) -> float:
        """
        Return geometric length of this quaternion.
        """
    def GetNormalized(self, eps: float = ...) -> Quatf:
        """
        length of this quaternion is smaller than C{eps}, return the identity
        quaternion.
        """
    def GetReal(self) -> float:
        """
        Return the real coefficient.
        """
    @staticmethod
    def GetZero() -> Quatf:
        """
        Return the zero quaternion, with real coefficient 0 and an imaginary
        coefficients all zero.
        """
    def Normalize(self, eps: float = ...) -> Quatf:
        """
        Normalizes this quaternion in place to unit length, returning the
        length before normalization.


        If the length of this quaternion is smaller than C{eps}, this sets the
        quaternion to identity.
        """
    @overload
    def SetImaginary(self, _imaginary: Vec3f | list[float] | tuple[float, float, float], /) -> None:
        """
        Set the imaginary coefficients.
        """
    @overload
    def SetImaginary(self, i: float, j: float, k: float) -> None:
        """
        Set the imaginary coefficients.
        """
    def SetReal(self, _real: float, /) -> None:
        """
        Set the real coefficient.
        """
    def Transform(self, _point: Vec3f | list[float] | tuple[float, float, float], /) -> Vec3f:
        """
        Transform the GfVec3f point.


        If the quaternion is normalized, the transformation is a rotation.
        Given a GfQuatf q, q.Transform(point) is equivalent to: (q *
        GfQuatf(0, point) * q.GetInverse()).GetImaginary() but is more
        efficient.
        """
    def __add__(self, arg2: Quatf | Quath, /) -> Any: ...
    def __eq__(self, other: object) -> bool:
        """
        Component-wise quaternion equality test.


        The real and imaginary parts must match exactly for quaternions to be
        considered equal.
        """
    def __hash__(self) -> int: ...
    def __iadd__(self, arg2: Quatf | Quath, /) -> Any: ...
    def __idiv__(self, arg2: float, /) -> Any: ...
    @overload
    def __imul__(self, arg2: Quatf | Quath, /) -> Any: ...
    @overload
    def __imul__(self, arg2: float, /) -> Any: ...
    def __isub__(self, arg2: Quatf | Quath, /) -> Any: ...
    def __itruediv__(self, arg2: float, /) -> Quatf: ...
    @overload
    def __mul__(self, arg2: Quatf | Quath, /) -> Any: ...
    @overload
    def __mul__(self, arg2: float, /) -> Any: ...
    def __ne__(self, other: object) -> bool: ...
    def __neg__(self) -> Any: ...
    def __rmul__(self, arg2: float, /) -> Any: ...
    def __sub__(self, arg2: Quatf | Quath, /) -> Any: ...
    def __truediv__(self, arg2: float, /) -> Any: ...

class Quath(Boost.Python.instance):
    """
    Basic type: a quaternion, a complex number with a real coefficient and
    three imaginary coefficients, stored as a 3-vector.
    """
    imaginary: Vec3h
    real: float
    @overload
    def __init__(self) -> None:
        """
        Default constructor leaves the quaternion undefined.
        """
    @overload
    def __init__(self, real: float) -> None:
        """
        Initialize the real coefficient to C{realVal} and the imaginary
        coefficients to zero.


        Since quaternions typically must be normalized, reasonable values for
        C{realVal} are -1, 0, or 1. Other values are legal but are likely to
        be meaningless.
        """
    @overload
    def __init__(self, real: float, i: float, j: float, k: float) -> None:
        """
        Initialize the real and imaginary coefficients.
        """
    @overload
    def __init__(self, real: float, imaginary: Vec3h | list[float] | tuple[float, float, float]) -> None:
        """
        Initialize the real and imaginary coefficients.
        """
    @overload
    def __init__(self, _other: Quatd | Quatf | Quath, /) -> None:
        """
        Construct from GfQuatd.
        """
    @overload
    def __init__(self, _other: Quatf | Quath, /) -> None:
        """
        Construct from GfQuatf.
        """
    @overload
    def __init__(self, arg2: Quath, /) -> None: ...
    def GetConjugate(self) -> Quath:
        """
        Return this quaternion's conjugate, which is the quaternion with the
        same real coefficient and negated imaginary coefficients.
        """
    @staticmethod
    def GetIdentity() -> Quath:
        """
        Return the identity quaternion, with real coefficient 1 and an
        imaginary coefficients all zero.
        """
    def GetImaginary(self) -> Vec3h:
        """
        Return the imaginary coefficient.
        """
    def GetInverse(self) -> Quath:
        """
        Return this quaternion's inverse, or reciprocal.


        This is the quaternion's conjugate divided by it's squared length.
        """
    def GetLength(self) -> float:
        """
        Return geometric length of this quaternion.
        """
    def GetNormalized(self, eps: float = ...) -> Quath:
        """
        length of this quaternion is smaller than C{eps}, return the identity
        quaternion.
        """
    def GetReal(self) -> float:
        """
        Return the real coefficient.
        """
    @staticmethod
    def GetZero() -> Quath:
        """
        Return the zero quaternion, with real coefficient 0 and an imaginary
        coefficients all zero.
        """
    def Normalize(self, eps: float = ...) -> Quath:
        """
        Normalizes this quaternion in place to unit length, returning the
        length before normalization.


        If the length of this quaternion is smaller than C{eps}, this sets the
        quaternion to identity.
        """
    @overload
    def SetImaginary(self, _imaginary: Vec3h | list[float] | tuple[float, float, float], /) -> None:
        """
        Set the imaginary coefficients.
        """
    @overload
    def SetImaginary(self, i: float, j: float, k: float) -> None:
        """
        Set the imaginary coefficients.
        """
    def SetReal(self, _real: float, /) -> None:
        """
        Set the real coefficient.
        """
    def Transform(self, _point: Vec3h | list[float] | tuple[float, float, float], /) -> Vec3h:
        """
        Transform the GfVec3h point.


        If the quaternion is normalized, the transformation is a rotation.
        Given a GfQuath q, q.Transform(point) is equivalent to: (q *
        GfQuath(0, point) * q.GetInverse()).GetImaginary() but is more
        efficient.
        """
    def __add__(self, arg2: Quath, /) -> Any: ...
    def __eq__(self, other: object) -> bool:
        """
        Component-wise quaternion equality test.


        The real and imaginary parts must match exactly for quaternions to be
        considered equal.
        """
    def __hash__(self) -> int: ...
    def __iadd__(self, arg2: Quath, /) -> Any: ...
    def __idiv__(self, arg2: object, /) -> Any: ...
    @overload
    def __imul__(self, arg2: Quath, /) -> Any: ...
    @overload
    def __imul__(self, arg2: object, /) -> Any: ...
    def __isub__(self, arg2: Quath, /) -> Any: ...
    def __itruediv__(self, arg2: object, /) -> Quath: ...
    @overload
    def __mul__(self, arg2: Quath, /) -> Any: ...
    @overload
    def __mul__(self, arg2: object, /) -> Any: ...
    def __ne__(self, other: object) -> bool: ...
    def __neg__(self) -> Any: ...
    def __rmul__(self, arg2: object, /) -> Any: ...
    def __sub__(self, arg2: Quath, /) -> Any: ...
    def __truediv__(self, arg2: object, /) -> Any: ...

class Range1d(Boost.Python.instance):
    """
    Basic type: 1-dimensional floating point range.


    This class represents a 1-dimensional range (or interval) All
    operations are component-wise and conform to interval mathematics. An
    empty range is one where max<min. The default empty is
    [FLT_MAX,-FLT_MAX]
    """
    dimension: ClassVar[int] = ...  # read-only
    __instance_size__: ClassVar[int] = ...
    max: float
    min: float
    @overload
    def __init__(self) -> None:
        """
        The default constructor creates an empty range.
        """
    @overload
    def __init__(self, _min: float, _max: float, /) -> None:
        """
        This constructor initializes the minimum and maximum points.
        """
    @overload
    def __init__(self, _other: Range1d, /) -> None:
        """
        Implicitly convert from GfRange1f.
        """
    @overload
    def __init__(self, arg2: Range1f, /) -> None: ...
    @overload
    def Contains(self, _point: float, /) -> bool:
        """
        Returns true if the C{point} is located inside the range.


        As with all operations of this type, the range is assumed to include
        its extrema.
        """
    @overload
    def Contains(self, _range: Range1d, /) -> bool:
        """
        Returns true if the C{range} is located entirely inside the range.


        As with all operations of this type, the ranges are assumed to include
        their extrema.
        """
    def GetDistanceSquared(self, _p: float, /) -> float:
        """
        Compute the squared distance from a point to the range.
        """
    @staticmethod
    def GetIntersection(_a: Range1d, _b: Range1d, /) -> Range1d:
        """
        Returns a C{GfRange1d} that describes the intersection of C{a} and
        C{b}.
        """
    def GetMax(self) -> float:
        """
        Returns the maximum value of the range.
        """
    def GetMidpoint(self) -> float:
        """
        Returns the midpoint of the range, that is, 0.5*(min+max).


        Note: this returns zero in the case of default-constructed ranges, or
        ranges set via SetEmpty() .
        """
    def GetMin(self) -> float:
        """
        Returns the minimum value of the range.
        """
    def GetSize(self) -> float:
        """
        Returns the size of the range.
        """
    @staticmethod
    def GetUnion(_a: Range1d, _b: Range1d, /) -> Range1d:
        """
        Returns the smallest C{GfRange1d} which contains both C{a} and C{b}.
        """
    def IntersectWith(self, _b: Range1d, /) -> Range1d:
        """
        Modifies this range to hold its intersection with C{b} and returns the
        result.
        """
    def IsEmpty(self) -> bool:
        """
        Returns whether the range is empty (max<min).
        """
    def SetEmpty(self) -> None:
        """
        Sets the range to an empty interval.
        """
    def SetMax(self, _max: float, /) -> None:
        """
        Sets the maximum value of the range.
        """
    def SetMin(self, _min: float, /) -> None:
        """
        Sets the minimum value of the range.
        """
    @overload
    def UnionWith(self, _b: Range1d, /) -> Range1d:
        """
        Extend C{this} to include C{b}.
        """
    @overload
    def UnionWith(self, _b: float, /) -> Range1d:
        """
        Extend C{this} to include C{b}.
        """
    def __add__(self, arg2: Range1d, /) -> Any: ...
    def __eq__(self, other: object) -> bool:
        """
        The min and max points must match exactly for equality.
        """
    def __hash__(self) -> int: ...
    def __iadd__(self, arg2: Range1d, /) -> Any: ...
    def __idiv__(self, arg2: float, /) -> Any: ...
    def __imul__(self, arg2: float, /) -> Any: ...
    def __isub__(self, arg2: Range1d, /) -> Any: ...
    def __itruediv__(self, arg2: float, /) -> Range1d: ...
    def __mul__(self, arg2: float, /) -> Any: ...
    def __ne__(self, other: object) -> bool: ...
    def __rmul__(self, arg2: float, /) -> Any: ...
    def __sub__(self, arg2: Range1d, /) -> Any: ...
    def __truediv__(self, arg2: float, /) -> Any: ...

class Range1f(Boost.Python.instance):
    """
    Basic type: 1-dimensional floating point range.


    This class represents a 1-dimensional range (or interval) All
    operations are component-wise and conform to interval mathematics. An
    empty range is one where max<min. The default empty is
    [FLT_MAX,-FLT_MAX]
    """
    dimension: ClassVar[int] = ...  # read-only
    __instance_size__: ClassVar[int] = ...
    max: float
    min: float
    @overload
    def __init__(self) -> None:
        """
        The default constructor creates an empty range.
        """
    @overload
    def __init__(self, _min: float, _max: float, /) -> None:
        """
        This constructor initializes the minimum and maximum points.
        """
    @overload
    def __init__(self, _other: Range1f, /) -> None:
        """
        Construct from GfRange1d.
        """
    @overload
    def __init__(self, arg2: Range1d, /) -> None: ...
    @overload
    def Contains(self, _point: float, /) -> bool:
        """
        Returns true if the C{point} is located inside the range.


        As with all operations of this type, the range is assumed to include
        its extrema.
        """
    @overload
    def Contains(self, _range: Range1f, /) -> bool:
        """
        Returns true if the C{range} is located entirely inside the range.


        As with all operations of this type, the ranges are assumed to include
        their extrema.
        """
    def GetDistanceSquared(self, _p: float, /) -> float:
        """
        Compute the squared distance from a point to the range.
        """
    @staticmethod
    def GetIntersection(_a: Range1f, _b: Range1f, /) -> Range1f:
        """
        Returns a C{GfRange1f} that describes the intersection of C{a} and
        C{b}.
        """
    def GetMax(self) -> float:
        """
        Returns the maximum value of the range.
        """
    def GetMidpoint(self) -> float:
        """
        Returns the midpoint of the range, that is, 0.5*(min+max).


        Note: this returns zero in the case of default-constructed ranges, or
        ranges set via SetEmpty() .
        """
    def GetMin(self) -> float:
        """
        Returns the minimum value of the range.
        """
    def GetSize(self) -> float:
        """
        Returns the size of the range.
        """
    @staticmethod
    def GetUnion(_a: Range1f, _b: Range1f, /) -> Range1f:
        """
        Returns the smallest C{GfRange1f} which contains both C{a} and C{b}.
        """
    def IntersectWith(self, _b: Range1f, /) -> Range1f:
        """
        Modifies this range to hold its intersection with C{b} and returns the
        result.
        """
    def IsEmpty(self) -> bool:
        """
        Returns whether the range is empty (max<min).
        """
    def SetEmpty(self) -> None:
        """
        Sets the range to an empty interval.
        """
    def SetMax(self, _max: float, /) -> None:
        """
        Sets the maximum value of the range.
        """
    def SetMin(self, _min: float, /) -> None:
        """
        Sets the minimum value of the range.
        """
    @overload
    def UnionWith(self, _b: Range1f, /) -> Range1f:
        """
        Extend C{this} to include C{b}.
        """
    @overload
    def UnionWith(self, _b: float, /) -> Range1f:
        """
        Extend C{this} to include C{b}.
        """
    def __add__(self, arg2: Range1f, /) -> Any: ...
    def __eq__(self, other: object) -> bool:
        """
        The min and max points must match exactly for equality.
        """
    def __hash__(self) -> int: ...
    def __iadd__(self, arg2: Range1f, /) -> Any: ...
    def __idiv__(self, arg2: float, /) -> Any: ...
    def __imul__(self, arg2: float, /) -> Any: ...
    def __isub__(self, arg2: Range1f, /) -> Any: ...
    def __itruediv__(self, arg2: float, /) -> Range1f: ...
    def __mul__(self, arg2: float, /) -> Any: ...
    def __ne__(self, other: object) -> bool: ...
    def __rmul__(self, arg2: float, /) -> Any: ...
    def __sub__(self, arg2: Range1f, /) -> Any: ...
    def __truediv__(self, arg2: float, /) -> Any: ...

class Range2d(Boost.Python.instance):
    """
    Basic type: 2-dimensional floating point range.


    This class represents a 2-dimensional range (or interval) All
    operations are component-wise and conform to interval mathematics. An
    empty range is one where max<min. The default empty is
    [FLT_MAX,-FLT_MAX]
    """
    dimension: ClassVar[int] = ...  # read-only
    unitSquare: ClassVar[Range2d] = ...  # read-only
    __instance_size__: ClassVar[int] = ...
    max: Vec2d
    min: Vec2d
    @overload
    def __init__(self) -> None:
        """
        The default constructor creates an empty range.
        """
    @overload
    def __init__(self, _min: Vec2d | list[float] | tuple[float, float], _max: Vec2d | list[float] | tuple[float, float], /) -> None:
        """
        This constructor initializes the minimum and maximum points.
        """
    @overload
    def __init__(self, _other: Range2d | list[float] | tuple[float, float], /) -> None:
        """
        Implicitly convert from GfRange2f.
        """
    @overload
    def __init__(self, arg2: Range2f | list[float] | tuple[float, float], /) -> None: ...
    @overload
    def Contains(self, _point: Vec2d | list[float] | tuple[float, float], /) -> bool:
        """
        Returns true if the C{point} is located inside the range.


        As with all operations of this type, the range is assumed to include
        its extrema.
        """
    @overload
    def Contains(self, _range: Range2d | list[float] | tuple[float, float], /) -> bool:
        """
        Returns true if the C{range} is located entirely inside the range.


        As with all operations of this type, the ranges are assumed to include
        their extrema.
        """
    def GetCorner(self, _i: int, /) -> Vec2d:
        """
        Returns the ith corner of the range, in the following order: SW, SE,
        NW, NE.
        """
    def GetDistanceSquared(self, _p: Vec2d | list[float] | tuple[float, float], /) -> float:
        """
        Compute the squared distance from a point to the range.
        """
    @staticmethod
    def GetIntersection(_a: Range2d | list[float] | tuple[float, float], _b: Range2d | list[float] | tuple[float, float], /) -> Range2d:
        """
        Returns a C{GfRange2d} that describes the intersection of C{a} and
        C{b}.
        """
    def GetMax(self) -> Vec2d:
        """
        Returns the maximum value of the range.
        """
    def GetMidpoint(self) -> Vec2d:
        """
        Returns the midpoint of the range, that is, 0.5*(min+max).


        Note: this returns zero in the case of default-constructed ranges, or
        ranges set via SetEmpty() .
        """
    def GetMin(self) -> Vec2d:
        """
        Returns the minimum value of the range.
        """
    def GetQuadrant(self, _i: int, /) -> Range2d:
        """
        Returns the ith quadrant of the range, in the following order: SW, SE,
        NW, NE.
        """
    def GetSize(self) -> Vec2d:
        """
        Returns the size of the range.
        """
    @staticmethod
    def GetUnion(_a: Range2d | list[float] | tuple[float, float], _b: Range2d | list[float] | tuple[float, float], /) -> Range2d:
        """
        Returns the smallest C{GfRange2d} which contains both C{a} and C{b}.
        """
    def IntersectWith(self, _b: Range2d | list[float] | tuple[float, float], /) -> Range2d:
        """
        Modifies this range to hold its intersection with C{b} and returns the
        result.
        """
    def IsEmpty(self) -> bool:
        """
        Returns whether the range is empty (max<min).
        """
    def SetEmpty(self) -> None:
        """
        Sets the range to an empty interval.
        """
    def SetMax(self, _max: Vec2d | list[float] | tuple[float, float], /) -> None:
        """
        Sets the maximum value of the range.
        """
    def SetMin(self, _min: Vec2d | list[float] | tuple[float, float], /) -> None:
        """
        Sets the minimum value of the range.
        """
    @overload
    def UnionWith(self, _b: Range2d | list[float] | tuple[float, float], /) -> Range2d:
        """
        Extend C{this} to include C{b}.
        """
    @overload
    def UnionWith(self, _b: Vec2d | list[float] | tuple[float, float], /) -> Range2d:
        """
        Extend C{this} to include C{b}.
        """
    def __add__(self, arg2: Range2d | list[float] | tuple[float, float], /) -> Any: ...
    def __eq__(self, other: object) -> bool:
        """
        The min and max points must match exactly for equality.
        """
    def __hash__(self) -> int: ...
    def __iadd__(self, arg2: Range2d | list[float] | tuple[float, float], /) -> Any: ...
    def __idiv__(self, arg2: float, /) -> Any: ...
    def __imul__(self, arg2: float, /) -> Any: ...
    def __isub__(self, arg2: Range2d | list[float] | tuple[float, float], /) -> Any: ...
    def __itruediv__(self, arg2: float, /) -> Range2d: ...
    def __mul__(self, arg2: float, /) -> Any: ...
    def __ne__(self, other: object) -> bool: ...
    def __rmul__(self, arg2: float, /) -> Any: ...
    def __sub__(self, arg2: Range2d | list[float] | tuple[float, float], /) -> Any: ...
    def __truediv__(self, arg2: float, /) -> Any: ...

class Range2f(Boost.Python.instance):
    """
    Basic type: 2-dimensional floating point range.


    This class represents a 2-dimensional range (or interval) All
    operations are component-wise and conform to interval mathematics. An
    empty range is one where max<min. The default empty is
    [FLT_MAX,-FLT_MAX]
    """
    dimension: ClassVar[int] = ...  # read-only
    unitSquare: ClassVar[Range2f] = ...  # read-only
    __instance_size__: ClassVar[int] = ...
    max: Vec2f
    min: Vec2f
    @overload
    def __init__(self) -> None:
        """
        The default constructor creates an empty range.
        """
    @overload
    def __init__(self, _min: Vec2f | list[float] | tuple[float, float], _max: Vec2f | list[float] | tuple[float, float], /) -> None:
        """
        This constructor initializes the minimum and maximum points.
        """
    @overload
    def __init__(self, _other: Range2f | list[float] | tuple[float, float], /) -> None:
        """
        Construct from GfRange2d.
        """
    @overload
    def __init__(self, arg2: Range2d | list[float] | tuple[float, float], /) -> None: ...
    @overload
    def Contains(self, _point: Vec2f | list[float] | tuple[float, float], /) -> bool:
        """
        Returns true if the C{point} is located inside the range.


        As with all operations of this type, the range is assumed to include
        its extrema.
        """
    @overload
    def Contains(self, _range: Range2f | list[float] | tuple[float, float], /) -> bool:
        """
        Returns true if the C{range} is located entirely inside the range.


        As with all operations of this type, the ranges are assumed to include
        their extrema.
        """
    def GetCorner(self, _i: int, /) -> Vec2f:
        """
        Returns the ith corner of the range, in the following order: SW, SE,
        NW, NE.
        """
    def GetDistanceSquared(self, _p: Vec2f | list[float] | tuple[float, float], /) -> float:
        """
        Compute the squared distance from a point to the range.
        """
    @staticmethod
    def GetIntersection(_a: Range2f | list[float] | tuple[float, float], _b: Range2f | list[float] | tuple[float, float], /) -> Range2f:
        """
        Returns a C{GfRange2f} that describes the intersection of C{a} and
        C{b}.
        """
    def GetMax(self) -> Vec2f:
        """
        Returns the maximum value of the range.
        """
    def GetMidpoint(self) -> Vec2f:
        """
        Returns the midpoint of the range, that is, 0.5*(min+max).


        Note: this returns zero in the case of default-constructed ranges, or
        ranges set via SetEmpty() .
        """
    def GetMin(self) -> Vec2f:
        """
        Returns the minimum value of the range.
        """
    def GetQuadrant(self, _i: int, /) -> Range2f:
        """
        Returns the ith quadrant of the range, in the following order: SW, SE,
        NW, NE.
        """
    def GetSize(self) -> Vec2f:
        """
        Returns the size of the range.
        """
    @staticmethod
    def GetUnion(_a: Range2f | list[float] | tuple[float, float], _b: Range2f | list[float] | tuple[float, float], /) -> Range2f:
        """
        Returns the smallest C{GfRange2f} which contains both C{a} and C{b}.
        """
    def IntersectWith(self, _b: Range2f | list[float] | tuple[float, float], /) -> Range2f:
        """
        Modifies this range to hold its intersection with C{b} and returns the
        result.
        """
    def IsEmpty(self) -> bool:
        """
        Returns whether the range is empty (max<min).
        """
    def SetEmpty(self) -> None:
        """
        Sets the range to an empty interval.
        """
    def SetMax(self, _max: Vec2f | list[float] | tuple[float, float], /) -> None:
        """
        Sets the maximum value of the range.
        """
    def SetMin(self, _min: Vec2f | list[float] | tuple[float, float], /) -> None:
        """
        Sets the minimum value of the range.
        """
    @overload
    def UnionWith(self, _b: Range2f | list[float] | tuple[float, float], /) -> Range2f:
        """
        Extend C{this} to include C{b}.
        """
    @overload
    def UnionWith(self, _b: Vec2f | list[float] | tuple[float, float], /) -> Range2f:
        """
        Extend C{this} to include C{b}.
        """
    def __add__(self, arg2: Range2f | list[float] | tuple[float, float], /) -> Any: ...
    def __eq__(self, other: object) -> bool:
        """
        The min and max points must match exactly for equality.
        """
    def __hash__(self) -> int: ...
    def __iadd__(self, arg2: Range2f | list[float] | tuple[float, float], /) -> Any: ...
    def __idiv__(self, arg2: float, /) -> Any: ...
    def __imul__(self, arg2: float, /) -> Any: ...
    def __isub__(self, arg2: Range2f | list[float] | tuple[float, float], /) -> Any: ...
    def __itruediv__(self, arg2: float, /) -> Range2f: ...
    def __mul__(self, arg2: float, /) -> Any: ...
    def __ne__(self, other: object) -> bool: ...
    def __rmul__(self, arg2: float, /) -> Any: ...
    def __sub__(self, arg2: Range2f | list[float] | tuple[float, float], /) -> Any: ...
    def __truediv__(self, arg2: float, /) -> Any: ...

class Range3d(Boost.Python.instance):
    """
    Basic type: 3-dimensional floating point range.


    This class represents a 3-dimensional range (or interval) All
    operations are component-wise and conform to interval mathematics. An
    empty range is one where max<min. The default empty is
    [FLT_MAX,-FLT_MAX]
    """
    dimension: ClassVar[int] = ...  # read-only
    unitCube: ClassVar[Range3d] = ...  # read-only
    __instance_size__: ClassVar[int] = ...
    max: Vec3d
    min: Vec3d
    @overload
    def __init__(self) -> None:
        """
        The default constructor creates an empty range.
        """
    @overload
    def __init__(self, _min: Vec3d | list[float] | tuple[float, float, float], _max: Vec3d | list[float] | tuple[float, float, float], /) -> None:
        """
        This constructor initializes the minimum and maximum points.
        """
    @overload
    def __init__(self, _other: Range3d | list[float] | tuple[float, float, float], /) -> None:
        """
        Implicitly convert from GfRange3f.
        """
    @overload
    def __init__(self, arg2: Range3f | list[float] | tuple[float, float, float], /) -> None: ...
    @overload
    def Contains(self, _point: Vec3d | list[float] | tuple[float, float, float], /) -> bool:
        """
        Returns true if the C{point} is located inside the range.


        As with all operations of this type, the range is assumed to include
        its extrema.
        """
    @overload
    def Contains(self, _range: Range3d | list[float] | tuple[float, float, float], /) -> bool:
        """
        Returns true if the C{range} is located entirely inside the range.


        As with all operations of this type, the ranges are assumed to include
        their extrema.
        """
    def GetCorner(self, _i: int, /) -> Vec3d:
        """
        Returns the ith corner of the range, in the following order: LDB, RDB,
        LUB, RUB, LDF, RDF, LUF, RUF.


        Where L/R is left/right, D/U is down/up, and B/F is back/front.
        """
    def GetDistanceSquared(self, _p: Vec3d | list[float] | tuple[float, float, float], /) -> float:
        """
        Compute the squared distance from a point to the range.
        """
    @staticmethod
    def GetIntersection(_a: Range3d | list[float] | tuple[float, float, float], _b: Range3d | list[float] | tuple[float, float, float], /) -> Range3d:
        """
        Returns a C{GfRange3d} that describes the intersection of C{a} and
        C{b}.
        """
    def GetMax(self) -> Vec3d:
        """
        Returns the maximum value of the range.
        """
    def GetMidpoint(self) -> Vec3d:
        """
        Returns the midpoint of the range, that is, 0.5*(min+max).


        Note: this returns zero in the case of default-constructed ranges, or
        ranges set via SetEmpty() .
        """
    def GetMin(self) -> Vec3d:
        """
        Returns the minimum value of the range.
        """
    def GetOctant(self, _i: int, /) -> Range3d:
        """
        Returns the ith octant of the range, in the following order: LDB, RDB,
        LUB, RUB, LDF, RDF, LUF, RUF.


        Where L/R is left/right, D/U is down/up, and B/F is back/front.
        """
    def GetSize(self) -> Vec3d:
        """
        Returns the size of the range.
        """
    @staticmethod
    def GetUnion(_a: Range3d | list[float] | tuple[float, float, float], _b: Range3d | list[float] | tuple[float, float, float], /) -> Range3d:
        """
        Returns the smallest C{GfRange3d} which contains both C{a} and C{b}.
        """
    def IntersectWith(self, _b: Range3d | list[float] | tuple[float, float, float], /) -> Range3d:
        """
        Modifies this range to hold its intersection with C{b} and returns the
        result.
        """
    def IsEmpty(self) -> bool:
        """
        Returns whether the range is empty (max<min).
        """
    def SetEmpty(self) -> None:
        """
        Sets the range to an empty interval.
        """
    def SetMax(self, _max: Vec3d | list[float] | tuple[float, float, float], /) -> None:
        """
        Sets the maximum value of the range.
        """
    def SetMin(self, _min: Vec3d | list[float] | tuple[float, float, float], /) -> None:
        """
        Sets the minimum value of the range.
        """
    @overload
    def UnionWith(self, _b: Range3d | list[float] | tuple[float, float, float], /) -> Range3d:
        """
        Extend C{this} to include C{b}.
        """
    @overload
    def UnionWith(self, _b: Vec3d | list[float] | tuple[float, float, float], /) -> Range3d:
        """
        Extend C{this} to include C{b}.
        """
    def __add__(self, arg2: Range3d | list[float] | tuple[float, float, float], /) -> Any: ...
    def __eq__(self, other: object) -> bool:
        """
        The min and max points must match exactly for equality.
        """
    def __hash__(self) -> int: ...
    def __iadd__(self, arg2: Range3d | list[float] | tuple[float, float, float], /) -> Any: ...
    def __idiv__(self, arg2: float, /) -> Any: ...
    def __imul__(self, arg2: float, /) -> Any: ...
    def __isub__(self, arg2: Range3d | list[float] | tuple[float, float, float], /) -> Any: ...
    def __itruediv__(self, arg2: float, /) -> Range3d: ...
    def __mul__(self, arg2: float, /) -> Any: ...
    def __ne__(self, other: object) -> bool: ...
    def __rmul__(self, arg2: float, /) -> Any: ...
    def __sub__(self, arg2: Range3d | list[float] | tuple[float, float, float], /) -> Any: ...
    def __truediv__(self, arg2: float, /) -> Any: ...

class Range3f(Boost.Python.instance):
    """
    Basic type: 3-dimensional floating point range.


    This class represents a 3-dimensional range (or interval) All
    operations are component-wise and conform to interval mathematics. An
    empty range is one where max<min. The default empty is
    [FLT_MAX,-FLT_MAX]
    """
    dimension: ClassVar[int] = ...  # read-only
    unitCube: ClassVar[Range3f] = ...  # read-only
    __instance_size__: ClassVar[int] = ...
    max: Vec3f
    min: Vec3f
    @overload
    def __init__(self) -> None:
        """
        The default constructor creates an empty range.
        """
    @overload
    def __init__(self, _min: Vec3f | list[float] | tuple[float, float, float], _max: Vec3f | list[float] | tuple[float, float, float], /) -> None:
        """
        This constructor initializes the minimum and maximum points.
        """
    @overload
    def __init__(self, _other: Range3f | list[float] | tuple[float, float, float], /) -> None:
        """
        Construct from GfRange3d.
        """
    @overload
    def __init__(self, arg2: Range3d | list[float] | tuple[float, float, float], /) -> None: ...
    @overload
    def Contains(self, _point: Vec3f | list[float] | tuple[float, float, float], /) -> bool:
        """
        Returns true if the C{point} is located inside the range.


        As with all operations of this type, the range is assumed to include
        its extrema.
        """
    @overload
    def Contains(self, _range: Range3f | list[float] | tuple[float, float, float], /) -> bool:
        """
        Returns true if the C{range} is located entirely inside the range.


        As with all operations of this type, the ranges are assumed to include
        their extrema.
        """
    def GetCorner(self, _i: int, /) -> Vec3f:
        """
        Returns the ith corner of the range, in the following order: LDB, RDB,
        LUB, RUB, LDF, RDF, LUF, RUF.


        Where L/R is left/right, D/U is down/up, and B/F is back/front.
        """
    def GetDistanceSquared(self, _p: Vec3f | list[float] | tuple[float, float, float], /) -> float:
        """
        Compute the squared distance from a point to the range.
        """
    @staticmethod
    def GetIntersection(_a: Range3f | list[float] | tuple[float, float, float], _b: Range3f | list[float] | tuple[float, float, float], /) -> Range3f:
        """
        Returns a C{GfRange3f} that describes the intersection of C{a} and
        C{b}.
        """
    def GetMax(self) -> Vec3f:
        """
        Returns the maximum value of the range.
        """
    def GetMidpoint(self) -> Vec3f:
        """
        Returns the midpoint of the range, that is, 0.5*(min+max).


        Note: this returns zero in the case of default-constructed ranges, or
        ranges set via SetEmpty() .
        """
    def GetMin(self) -> Vec3f:
        """
        Returns the minimum value of the range.
        """
    def GetOctant(self, _i: int, /) -> Range3f:
        """
        Returns the ith octant of the range, in the following order: LDB, RDB,
        LUB, RUB, LDF, RDF, LUF, RUF.


        Where L/R is left/right, D/U is down/up, and B/F is back/front.
        """
    def GetSize(self) -> Vec3f:
        """
        Returns the size of the range.
        """
    @staticmethod
    def GetUnion(_a: Range3f | list[float] | tuple[float, float, float], _b: Range3f | list[float] | tuple[float, float, float], /) -> Range3f:
        """
        Returns the smallest C{GfRange3f} which contains both C{a} and C{b}.
        """
    def IntersectWith(self, _b: Range3f | list[float] | tuple[float, float, float], /) -> Range3f:
        """
        Modifies this range to hold its intersection with C{b} and returns the
        result.
        """
    def IsEmpty(self) -> bool:
        """
        Returns whether the range is empty (max<min).
        """
    def SetEmpty(self) -> None:
        """
        Sets the range to an empty interval.
        """
    def SetMax(self, _max: Vec3f | list[float] | tuple[float, float, float], /) -> None:
        """
        Sets the maximum value of the range.
        """
    def SetMin(self, _min: Vec3f | list[float] | tuple[float, float, float], /) -> None:
        """
        Sets the minimum value of the range.
        """
    @overload
    def UnionWith(self, _b: Range3f | list[float] | tuple[float, float, float], /) -> Range3f:
        """
        Extend C{this} to include C{b}.
        """
    @overload
    def UnionWith(self, _b: Vec3f | list[float] | tuple[float, float, float], /) -> Range3f:
        """
        Extend C{this} to include C{b}.
        """
    def __add__(self, arg2: Range3f | list[float] | tuple[float, float, float], /) -> Any: ...
    def __eq__(self, other: object) -> bool:
        """
        The min and max points must match exactly for equality.
        """
    def __hash__(self) -> int: ...
    def __iadd__(self, arg2: Range3f | list[float] | tuple[float, float, float], /) -> Any: ...
    def __idiv__(self, arg2: float, /) -> Any: ...
    def __imul__(self, arg2: float, /) -> Any: ...
    def __isub__(self, arg2: Range3f | list[float] | tuple[float, float, float], /) -> Any: ...
    def __itruediv__(self, arg2: float, /) -> Range3f: ...
    def __mul__(self, arg2: float, /) -> Any: ...
    def __ne__(self, other: object) -> bool: ...
    def __rmul__(self, arg2: float, /) -> Any: ...
    def __sub__(self, arg2: Range3f | list[float] | tuple[float, float, float], /) -> Any: ...
    def __truediv__(self, arg2: float, /) -> Any: ...

class Ray(Boost.Python.instance):
    """
    Basic type: Ray used for intersection testing.


    This class represents a three-dimensional ray in space, typically used
    for intersection testing. It consists of an origin and a direction.

    Note that by default a C{GfRay} does not normalize its direction
    vector to unit length.

    Note for ray intersections, the start point is included in the
    computations, i.e., a distance of zero is defined to be intersecting.
    """
    __instance_size__: ClassVar[int] = ...
    direction: Vec3d
    startPoint: Vec3d
    @overload
    def __init__(self) -> None:
        """
        The default constructor leaves the ray parameters undefined.
        """
    @overload
    def __init__(self, _startPoint: Vec3d | list[float] | tuple[float, float, float], _direction: Vec3d | list[float] | tuple[float, float, float], /) -> None:
        """
        This constructor takes a starting point and a direction.
        """
    def FindClosestPoint(self, _point: Vec3d | list[float] | tuple[float, float, float], /) -> tuple:
        """
        Returns the point on the ray that is closest to C{point}.


        If C{rayDistance} is not C{None}, it will be set to the parametric
        distance along the ray of the closest point.
        """
    def GetPoint(self, _distance: float, /) -> Vec3d:
        """
        Returns the point that is C{distance} units from the starting point
        along the direction vector, expressed in parametic distance.
        """
    def Intersect(self, *args, **kwargs):
        """

        Intersect( (Ray)arg1, (Vec3d)arg2, (Vec3d)arg3, (Vec3d)arg4) -> tuple :
            Intersect( p0, p1, p2 ) -> tuple<intersects = bool, dist =
            float, barycentric = GfVec3d, frontFacing = bool>
    
            Intersects the ray with the triangle formed by points p0,
            p1, and p2.  The first item in the tuple is true if the ray
            intersects the triangle. dist is the the parametric
            distance to the intersection point, the barycentric
            coordinates of the intersection point, and the front-facing
            flag. The barycentric coordinates are defined with respect
            to the three vertices taken in order.  The front-facing
            flag is True if the intersection hit the side of the
            triangle that is formed when the vertices are ordered
            counter-clockwise (right-hand rule).
    
            Barycentric coordinates are defined to sum to 1 and satisfy
            this relationsip:
    
                intersectionPoint = (barycentricCoords[0] * p0 +
                                     barycentricCoords[1] * p1 +
                                     barycentricCoords[2] * p2);
            ----------------------------------------------------------------------

        Intersect( (Ray)arg1, (Plane)arg2) -> tuple :
            Intersect( plane ) -> tuple<intersects = bool, dist = float,
            frontFacing = bool>
    
            Intersects the ray with the Gf.Plane.  The first item in
            the returned tuple is true if the ray intersects the plane.
            dist is the parametric distance to the intersection point
            and frontfacing is true if the intersection is on the side
            of the plane toward which the plane's normal points.
            ----------------------------------------------------------------------

        Intersect( (Ray)arg1, (Range3d)arg2) -> tuple :
            Intersect( range3d ) -> tuple<intersects = bool, enterDist
            = float, exitDist = float>
            Intersects the plane with an axis-aligned box in a
            Gf.Range3d.  intersects is true if the ray intersects it at
            all within bounds. If there is an intersection then enterDist
            and exitDist will be the parametric distances to the two
            intersection points.
            ----------------------------------------------------------------------

        Intersect( (Ray)arg1, (BBox3d)arg2) -> tuple :
            Intersect( bbox3d ) -> tuple<intersects = bool, enterDist
            = float, exitDist = float>
            Intersects the plane with an oriented box in a Gf.BBox3d.
            intersects is true if the ray intersects it at all within
            bounds. If there is an intersection then enterDist and
            exitDist will be the parametric distances to the two
            intersection points.
            ----------------------------------------------------------------------

        Intersect( (Ray)arg1, (Vec3d)arg2, (float)arg3) -> tuple :
            Intersect( center, radius ) -> tuple<intersects = bool,
            enterDist = float, exitDist = float>
    
            Intersects the plane with an sphere. intersects is true if
            the ray intersects it at all within the sphere. If there is
            an intersection then enterDist and exitDist will be the
            parametric distances to the two intersection points.
            ----------------------------------------------------------------------

        Intersect( (Ray)arg1, (Vec3d)arg2, (Vec3d)arg3, (float)arg4) -> tuple :
            Intersect( origin, axis, radius ) -> tuple<intersects = bool,
            enterDist = float, exitDist = float>
    
            Intersects the plane with an infinite cylinder. intersects
            is true if the ray intersects it at all within the
            sphere. If there is an intersection then enterDist and
            exitDist will be the parametric distances to the two
            intersection points.
            ----------------------------------------------------------------------

        Intersect( (Ray)arg1, (Vec3d)arg2, (Vec3d)arg3, (float)arg4, (float)arg5) -> tuple :
            Intersect( origin, axis, radius, height ) -> 
            tuple<intersects = bool, enterDist = float, exitDist = float>
    
            Intersects the plane with an cylinder. intersects
            is true if the ray intersects it at all within the
            sphere. If there is an intersection then enterDist and
            exitDist will be the parametric distances to the two
            intersection points.
            ----------------------------------------------------------------------"""
    def SetEnds(self, _startPoint: Vec3d | list[float] | tuple[float, float, float], _endPoint: Vec3d | list[float] | tuple[float, float, float], /) -> Ray:
        """
        Sets the ray by specifying a starting point and an ending point.
        """
    def SetPointAndDirection(self, _startPoint: Vec3d | list[float] | tuple[float, float, float], _direction: Vec3d | list[float] | tuple[float, float, float], /) -> Ray:
        """
        Sets the ray by specifying a starting point and a direction.
        """
    def Transform(self, _matrix: Matrix4d, /) -> Ray:
        """
        Transforms the ray by the given matrix.
        """
    def __eq__(self, other: object) -> bool:
        """
        Component-wise equality test.


        The starting points, directions, and lengths must match exactly for
        rays to be considered equal.
        """
    def __ne__(self, other: object) -> bool: ...

class Rect2i(Boost.Python.instance):
    """
    A 2D rectangle with integer coordinates.


    A rectangle is internally represented as two corners. We refer to
    these as the min and max corner where the min's x-coordinate and
    y-coordinate are assumed to be less than or equal to the max's
    corresponding coordinates. Normally, it is expressed as a min corner
    and a size.

    Note that the max corner is included when computing the size (width
    and height) of a rectangle as the number of integral points in the x-
    and y-direction. In particular, if the min corner and max corner are
    the same, then the width and the height of the rectangle will both be
    one since we have exactly one integral point with coordinates greater
    or equal to the min corner and less or equal to the max corner.

    Specifically, *width = maxX - minX + 1* and *height = maxY - minY +
    1.*
    """
    __instance_size__: ClassVar[int] = ...
    max: Vec2i
    maxX: int
    maxY: int
    min: Vec2i
    minX: int
    minY: int
    @overload
    def __init__(self) -> None:
        """
        Constructs an empty rectangle.
        """
    @overload
    def __init__(self, _min: Vec2i | list[int] | Size2 | tuple[int, int], _max: Vec2i | list[int] | Size2 | tuple[int, int], /) -> None:
        """
        Constructs a rectangle with C{min} and C{max} corners.
        """
    @overload
    def __init__(self, _min: Vec2i | list[int] | Size2 | tuple[int, int], _width: int, _height: int, /) -> None:
        """
        Constructs a rectangle with C{min} corner and the indicated C{width}
        and C{height}.
        """
    @overload
    def __init__(self, arg2: Rect2i, /) -> None: ...
    def Contains(self, _p: Vec2i | list[int] | Size2 | tuple[int, int], /) -> bool:
        """
        Returns true if the specified point in the rectangle.
        """
    def GetArea(self) -> int:
        """
        Return the area of the rectangle.
        """
    def GetCenter(self) -> Vec2i:
        """
        Returns the center point of the rectangle.
        """
    def GetHeight(self) -> int:
        """
        Returns the height of the rectangle.



        If the min and max y-coordinates are coincident, the height is one.
        """
    def GetIntersection(self, _that: Rect2i, /) -> Rect2i:
        """
        Computes the intersection of two rectangles.
        """
    def GetMax(self) -> Vec2i:
        """
        Returns the max corner of the rectangle.
        """
    def GetMaxX(self) -> int:
        """
        Return the X value of the max corner.
        """
    def GetMaxY(self) -> int:
        """
        Return the Y value of the max corner.
        """
    def GetMin(self) -> Vec2i:
        """
        Returns the min corner of the rectangle.
        """
    def GetMinX(self) -> int:
        """
        Return the X value of min corner.
        """
    def GetMinY(self) -> int:
        """
        Return the Y value of the min corner.
        """
    def GetNormalized(self) -> Rect2i:
        """
        Returns a normalized rectangle, i.e.


        one that has a non-negative width and height.

        C{GetNormalized()} swaps the min and max x-coordinates to ensure a
        non-negative width, and similarly for the y-coordinates.
        """
    def GetSize(self) -> Vec2i:
        """
        Returns the size of the rectangle as a vector (width,height).
        """
    def GetUnion(self, _that: Rect2i, /) -> Rect2i:
        """
        Computes the union of two rectangles.
        """
    def GetWidth(self) -> int:
        """
        Returns the width of the rectangle.



        If the min and max x-coordinates are coincident, the width is one.
        """
    def IsEmpty(self) -> bool:
        """
        Returns true if the rectangle is empty.


        An empty rectangle has one or both of its min coordinates strictly
        greater than the corresponding max coordinate.

        An empty rectangle is not valid.
        """
    def IsNull(self) -> bool:
        """
        Returns true if the rectangle is a null rectangle.


        A null rectangle has both the width and the height set to 0, that is
        ::

          GetMaxX() == GetMinX() - 1

         and ::

          GetMaxY() == GetMinY() - 1

         Remember that if C{GetMinX()} and C{GetMaxX()} return the same value
        then the rectangle has width 1, and similarly for the height.

        A null rectangle is both empty, and not valid.
        """
    def IsValid(self) -> bool:
        """
        Return true if the rectangle is valid (equivalently, not empty).
        """
    def SetMax(self, _max: Vec2i | list[int] | Size2 | tuple[int, int], /) -> None:
        """
        Sets the max corner of the rectangle.
        """
    def SetMaxX(self, _x: int, /) -> None:
        """
        Set the X value of the max corner.
        """
    def SetMaxY(self, _y: int, /) -> None:
        """
        Set the Y value of the max corner.
        """
    def SetMin(self, _min: Vec2i | list[int] | Size2 | tuple[int, int], /) -> None:
        """
        Sets the min corner of the rectangle.
        """
    def SetMinX(self, _x: int, /) -> None:
        """
        Set the X value of the min corner.
        """
    def SetMinY(self, _y: int, /) -> None:
        """
        Set the Y value of the min corner.
        """
    def Translate(self, _displacement: Vec2i | list[int] | Size2 | tuple[int, int], /) -> Rect2i:
        """
        Move the rectangle by C{displ}.
        """
    def __add__(self, arg2: Rect2i, /) -> Any: ...
    def __eq__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    def __iadd__(self, arg2: Rect2i, /) -> Any: ...
    def __ne__(self, other: object) -> bool: ...

class Rotation(Boost.Python.instance):
    """
    Basic type: 3-space rotation specification.


    This class represents a rotation in 3-space. This stores an axis as a
    normalized vector of 3 C{doubles} and an angle in degrees (as a
    double). Rotations follow the right-hand rule: a positive rotation
    about an axis vector appears counter-clockwise when looking from the
    end of the vector toward the origin.
    """
    __instance_size__: ClassVar[int] = ...
    angle: float
    axis: Vec3d
    @overload
    def __init__(self) -> None:
        """
        The default constructor leaves the rotation undefined.
        """
    @overload
    def __init__(self, _axis: Vec3d | list[float] | tuple[float, float, float], _angle: float, /) -> None:
        """
        This constructor initializes the rotation to be C{angle} degrees about
        C{axis}.
        """
    @overload
    def __init__(self, _quaternion: Quaternion, /) -> None:
        """
        This constructor initializes the rotation from a quaternion.
        """
    @overload
    def __init__(self, _quat: Quatd | Quatf | Quath, /) -> None:
        """
        This constructor initializes the rotation from a quaternion.


        Note that this constructor accepts GfQuatf and GfQuath since they
        implicitly convert to GfQuatd.
        """
    @overload
    def __init__(self, _rotateFrom: Vec3d | list[float] | tuple[float, float, float], _rotateTo: Vec3d | list[float] | tuple[float, float, float], /) -> None:
        """
        This constructor initializes the rotation to one that brings the
        C{rotateFrom} vector to align with C{rotateTo}.


        The passed vectors need not be unit length.
        """
    @overload
    def __init__(self, arg2: Rotation, /) -> None: ...
    def Decompose(self, _axis0: Vec3d | list[float] | tuple[float, float, float], _axis1: Vec3d | list[float] | tuple[float, float, float], _axis2: Vec3d | list[float] | tuple[float, float, float], /) -> Vec3d:
        """
        Decompose rotation about 3 orthogonal axes.


        If the axes are not orthogonal, warnings will be spewed.
        """
    @staticmethod
    def DecomposeRotation(rot: Matrix4d, twAxis: Vec3d | list[float] | tuple[float, float, float], fbAxis: Vec3d | list[float] | tuple[float, float, float], lrAxis: Vec3d | list[float] | tuple[float, float, float], handedness: float, thetaTwHint: float, thetaFBHint: float, thetaLRHint: float, thetaSwHint: float = ..., useHint: bool = ..., swShift: float = ...) -> tuple: ...
    @staticmethod
    def DecomposeRotation3(rot: Matrix4d, twAxis: Vec3d | list[float] | tuple[float, float, float], fbAxis: Vec3d | list[float] | tuple[float, float, float], lrAxis: Vec3d | list[float] | tuple[float, float, float], handedness: float, thetaTwHint: float = ..., thetaFBHint: float = ..., thetaLRHint: float = ..., useHint: bool = ...) -> tuple: ...
    def GetAngle(self) -> float:
        """
        Returns the rotation angle in degrees.
        """
    def GetAxis(self) -> Vec3d:
        """
        Returns the axis of rotation.
        """
    def GetInverse(self) -> Rotation:
        """
        Returns the inverse of this rotation.
        """
    def GetQuat(self) -> Quatd:
        """
        Returns the rotation expressed as a quaternion.
        """
    def GetQuaternion(self) -> Quaternion:
        """
        Returns the rotation expressed as a quaternion.
        """
    @staticmethod
    def MatchClosestEulerRotation(_targetTw: float, _targetFB: float, _targetLR: float, _targetSw: float, _thetaTw: float, _thetaFB: float, _thetaLR: float, _thetaSw: float, /) -> tuple:
        """
        Replace the hint angles with the closest rotation of the given
        rotation to the hint.


        Each angle in the rotation will be within Pi of the corresponding hint
        angle and the sum of the differences with the hint will be minimized.
        If a given rotation value is null then that angle will be treated as
        0.0 and ignored in the calculations.

        All angles are in radians. The rotation order is Tw/FB/LR/Sw.
        """
    @staticmethod
    def RotateOntoProjected(_v1: Vec3d | list[float] | tuple[float, float, float], _v2: Vec3d | list[float] | tuple[float, float, float], _axis: Vec3d | list[float] | tuple[float, float, float], /) -> Rotation: ...
    def SetAxisAngle(self, axis: Vec3d | list[float] | tuple[float, float, float], angle: float) -> Rotation:
        """
        Sets the rotation to be C{angle} degrees about C{axis}.
        """
    def SetIdentity(self) -> Rotation:
        """
        Sets the rotation to an identity rotation.


        (This is chosen to be 0 degrees around the positive X axis.)
        """
    def SetQuat(self, quat: Quatd | Quatf | Quath) -> Rotation:
        """
        Sets the rotation from a quaternion.


        Note that this method accepts GfQuatf and GfQuath since they
        implicitly convert to GfQuatd.
        """
    def SetQuaternion(self, quaternion: Quaternion) -> Rotation:
        """
        Sets the rotation from a quaternion.
        """
    def SetRotateInto(self, rotateFrom: Vec3d | list[float] | tuple[float, float, float], rotateTo: Vec3d | list[float] | tuple[float, float, float]) -> Rotation:
        """
        Sets the rotation to one that brings the C{rotateFrom} vector to align
        with C{rotateTo}.


        The passed vectors need not be unit length.
        """
    @overload
    def TransformDir(self, _vec: Vec3f | list[float] | tuple[float, float, float], /) -> Vec3f:
        """
        Transforms row vector C{vec} by the rotation, returning the result.
        """
    @overload
    def TransformDir(self, _vec: Vec3d | list[float] | tuple[float, float, float], /) -> Vec3d:
        """
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        """
    def __eq__(self, other: object) -> bool:
        """
        Component-wise rotation equality test.


        The axes and angles must match exactly for rotations to be considered
        equal. (To compare equality of the actual rotations, you can convert
        both to quaternions and test the results for equality.)
        """
    def __hash__(self) -> int: ...
    def __idiv__(self, arg2: float, /) -> Any: ...
    @overload
    def __imul__(self, arg2: Rotation, /) -> Any: ...
    @overload
    def __imul__(self, arg2: float, /) -> Any: ...
    @overload
    def __mul__(self, arg2: Rotation, /) -> Any: ...
    @overload
    def __mul__(self, arg2: float, /) -> Any: ...
    def __ne__(self, other: object) -> bool: ...
    def __rmul__(self, arg2: float, /) -> Any: ...
    def __truediv__(self, arg2: float, /) -> Any: ...

class Size2(Boost.Python.instance):
    """
    Two-dimensional array of sizes.


    GfSize2 is used to represent pairs of counts. It is based on the
    datatype size_t, and thus can only represent non-negative values in
    each dimension. If you need to represent negative numbers as well, use
    GfVec2i.

    Usage of GfSize2 is similar to that of GfVec2i, except that all
    mathematical operations are componentwise (including multiplication).
    """
    dimension: ClassVar[int] = ...  # read-only
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None:
        """
        Default constructor initializes components to zero.
        """
    @overload
    def __init__(self, _o: Size2 | list[float] | tuple[float, float], /) -> None:
        """
        Copy constructor.
        """
    @overload
    def __init__(self, _o: Vec2i | list[int] | Size2 | tuple[int, int], /) -> None:
        """
        Conversion from GfVec2i.
        """
    @overload
    def __init__(self, _v0: int, _v1: int, /) -> None:
        """
        Construct from two values.
        """
    def Set(self, _v0: int, _v1: int, /) -> Size2:
        """
        Set to values passed directly.
        """
    def __add__(self, arg2: Size2 | list[float] | tuple[float, float], /) -> Any: ...
    def __contains__(self, arg2: int, /) -> bool: ...
    def __eq__(self, other: object) -> bool:
        """
        Component-wise equality.
        """
    def __getitem__(self, _i: int, /) -> int:
        """
        Array operator.
        """
    def __iadd__(self, arg2: Size2 | list[float] | tuple[float, float], /) -> Any: ...
    def __idiv__(self, arg2: int, /) -> Any: ...
    def __imul__(self, arg2: int, /) -> Any: ...
    def __isub__(self, arg2: Size2 | list[float] | tuple[float, float], /) -> Any: ...
    def __itruediv__(self, arg2: int, /) -> Size2: ...
    def __len__(self) -> int: ...
    @overload
    def __mul__(self, arg2: Size2 | list[float] | tuple[float, float], /) -> Any: ...
    @overload
    def __mul__(self, arg2: int, /) -> Any: ...
    def __ne__(self, other: object) -> bool: ...
    def __rmul__(self, arg2: int, /) -> Any: ...
    def __setitem__(self, arg2: int, arg3: int, /) -> None: ...
    def __sub__(self, arg2: Size2 | list[float] | tuple[float, float], /) -> Any: ...
    def __truediv__(self, arg2: int, /) -> Any: ...

class Size3(Boost.Python.instance):
    """
    Three-dimensional array of sizes.


    GfSize3 is used to represent triples of counts. It is based on the
    datatype size_t, and thus can only represent non-negative values in
    each dimension. If you need to represent negative numbers as well, use
    GfVeci.

    Usage of GfSize3 is similar to that of GfVec3i, except that all
    mathematical operations are componentwise (including multiplication).
    """
    dimension: ClassVar[int] = ...  # read-only
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None:
        """
        Default constructor initializes components to zero.
        """
    @overload
    def __init__(self, _o: Size3 | list[float] | tuple[float, float, float], /) -> None:
        """
        Copy constructor.
        """
    @overload
    def __init__(self, _o: Vec3i | list[int] | Size3 | tuple[int, int, int], /) -> None:
        """
        Conversion from GfVec3i.
        """
    @overload
    def __init__(self, _v0: int, _v1: int, _v2: int, /) -> None:
        """
        Construct from three values.
        """
    def Set(self, _v0: int, _v1: int, _v2: int, /) -> Size3:
        """
        Set to values passed directly.
        """
    def __add__(self, arg2: Size3 | list[float] | tuple[float, float, float], /) -> Any: ...
    def __contains__(self, arg2: int, /) -> bool: ...
    def __eq__(self, other: object) -> bool:
        """
        Component-wise equality.
        """
    def __getitem__(self, _i: int, /) -> int:
        """
        Array operator.
        """
    def __iadd__(self, arg2: Size3 | list[float] | tuple[float, float, float], /) -> Any: ...
    def __idiv__(self, arg2: int, /) -> Any: ...
    def __imul__(self, arg2: int, /) -> Any: ...
    def __isub__(self, arg2: Size3 | list[float] | tuple[float, float, float], /) -> Any: ...
    def __itruediv__(self, arg2: int, /) -> Size3: ...
    def __len__(self) -> int: ...
    @overload
    def __mul__(self, arg2: Size3 | list[float] | tuple[float, float, float], /) -> Any: ...
    @overload
    def __mul__(self, arg2: int, /) -> Any: ...
    def __ne__(self, other: object) -> bool: ...
    def __rmul__(self, arg2: int, /) -> Any: ...
    def __setitem__(self, arg2: int, arg3: int, /) -> None: ...
    def __sub__(self, arg2: Size3 | list[float] | tuple[float, float, float], /) -> Any: ...
    def __truediv__(self, arg2: int, /) -> Any: ...

class Transform(Boost.Python.instance):
    """
    Basic type: Compound linear transformation.


    This class represents a linear transformation specified as a series of
    individual components: a *translation*, a *rotation*, a *scale*, a
    *pivotPosition*, and a *pivotOrientation*. When applied to a point,
    the point will be transformed as follows (in order):

       - Scaled by the *scale* with respect to *pivotPosition* and the
         orientation specified by the *pivotOrientation*.

       - Rotated by the *rotation* about *pivotPosition*.

       - Translated by *Translation*
         That is, the cumulative matrix that this represents looks like this.
         ::

      M = -P * -O * S * O * R * P * T

    where
       - *T* is the *translation* matrix

       - *P* is the matrix that translates by *pivotPosition*

       - *R* is the *rotation* matrix

       - *O* is the matrix that rotates to *pivotOrientation*

       - *S* is the *scale* matrix

    """
    __instance_size__: ClassVar[int] = ...
    pivotOrientation: Rotation
    pivotPosition: Vec3d
    rotation: Rotation
    scale: Vec3d
    translation: Vec3d
    @overload
    def __init__(self, scale: Vec3d | list[float] | tuple[float, float, float], pivotOrientation: Rotation, rotation: Rotation, pivotPosition: Vec3d | list[float] | tuple[float, float, float], translation: Vec3d | list[float] | tuple[float, float, float]) -> None:
        """
        This constructor initializes the transformation from all component
        values.


        This is the constructor used by 2x code.
        """
    @overload
    def __init__(self, translation: Vec3d | list[float] | tuple[float, float, float] = ..., rotation: Rotation = ..., scale: Vec3d | list[float] | tuple[float, float, float] = ..., pivotPosition: Vec3d | list[float] | tuple[float, float, float] = ..., pivotOrientation: Rotation = ...) -> None:
        """
        This constructor initializes the transformation from all component
        values.


        This is the constructor used by 3x code.
        """
    @overload
    def __init__(self, _m: Matrix4d, /) -> None:
        """
        This constructor initializes the transformation with a matrix.


        See SetMatrix() for more information.
        """
    def GetMatrix(self) -> Matrix4d:
        """
        Returns a C{GfMatrix4d} that implements the cumulative transformation.
        """
    def GetPivotOrientation(self) -> Rotation:
        """
        Returns the pivot orientation component.
        """
    def GetPivotPosition(self) -> Vec3d:
        """
        Returns the pivot position component.
        """
    def GetRotation(self) -> Rotation:
        """
        Returns the rotation component.
        """
    def GetScale(self) -> Vec3d:
        """
        Returns the scale component.
        """
    def GetTranslation(self) -> Vec3d:
        """
        Returns the translation component.
        """
    @overload
    def Set(self, scale: Vec3d | list[float] | tuple[float, float, float], pivotOrientation: Rotation, rotation: Rotation, pivotPosition: Vec3d | list[float] | tuple[float, float, float], translation: Vec3d | list[float] | tuple[float, float, float]) -> Transform:
        """
        Sets the transformation from all component values.


        This constructor orders its arguments the way that 2x expects.
        """
    @overload
    def Set(self, translation: Vec3d | list[float] | tuple[float, float, float] = ..., rotation: Rotation = ..., scale: Vec3d | list[float] | tuple[float, float, float] = ..., pivotPosition: Vec3d | list[float] | tuple[float, float, float] = ..., pivotOrientation: Rotation = ...) -> Transform:
        """
        Sets the transformation from all component values.


        This constructor orders its arguments the way that 3x expects.
        """
    def SetIdentity(self) -> Transform:
        """
        Sets the transformation to the identity transformation.
        """
    def SetMatrix(self, _m: Matrix4d, /) -> Transform:
        """
        Sets the transform components to implement the transformation
        represented by matrix C{m}, ignoring any projection.


        This tries to leave the current center unchanged.
        """
    def SetPivotOrientation(self, _pivotOrient: Rotation, /) -> None:
        """
        Sets the pivot orientation component, leaving all others untouched.
        """
    def SetPivotPosition(self, _pivPos: Vec3d | list[float] | tuple[float, float, float], /) -> None:
        """
        Sets the pivot position component, leaving all others untouched.
        """
    def SetRotation(self, _rotation: Rotation, /) -> None:
        """
        Sets the rotation component, leaving all others untouched.
        """
    def SetScale(self, _scale: Vec3d | list[float] | tuple[float, float, float], /) -> None:
        """
        Sets the scale component, leaving all others untouched.
        """
    def SetTranslation(self, _translation: Vec3d | list[float] | tuple[float, float, float], /) -> None:
        """
        Sets the translation component, leaving all others untouched.
        """
    def __eq__(self, other: object) -> bool:
        """
        Component-wise transform equality test.


        All components must match exactly for transforms to be considered
        equal.
        """
    def __imul__(self, arg2: Transform, /) -> Any: ...
    def __mul__(self, arg2: Transform, /) -> Any: ...
    def __ne__(self, other: object) -> bool: ...

class Vec2d(Boost.Python.instance):
    """
    Basic type for a vector of 2 double components.


    Represents a vector of 2 components of type C{double}. It is intended
    to be fast and simple.
    """
    __isGfVec: ClassVar[bool] = ...  # read-only
    dimension: ClassVar[int] = ...  # read-only
    __safe_for_unpickling__: ClassVar[bool] = ...
    @overload
    def __init__(self) -> None:
        """
        Default constructor does no initialization.
        """
    @overload
    def __init__(self, _value: float, /) -> None:
        """
        Initialize all elements to a single value.
        """
    @overload
    def __init__(self, _s0: float, _s1: float, /) -> None:
        """
        Initialize all elements with explicit arguments.
        """
    @overload
    def __init__(self, _other: Vec2f | list[float] | tuple[float, float], /) -> None:
        """
        Implicitly convert from GfVec2f.
        """
    @overload
    def __init__(self, _other: Vec2h | list[float] | tuple[float, float], /) -> None:
        """
        Implicitly convert from GfVec2h.
        """
    @overload
    def __init__(self, _other: Vec2i | list[int] | Size2 | tuple[int, int], /) -> None:
        """
        Implicitly convert from GfVec2i.
        """
    @overload
    def __init__(self, _other: Vec2d | list[float] | tuple[float, float], /) -> None:
        """
        Implicitly convert from GfVec2i.
        """
    @staticmethod
    def Axis(_i: int, /) -> Vec2d:
        """
        Create a unit vector along the i-th axis, zero-based.


        Return the zero vector if C{i} is greater than or equal to 2.
        """
    def GetComplement(self, _b: Vec2d | list[float] | tuple[float, float], /) -> Vec2d:
        """
        Returns the orthogonal complement of C{this->GetProjection(b)} .


        That is: ::

          *this - this->GetProjection(b)

        """
    def GetDot(self, arg2: Vec2d | list[float] | tuple[float, float], /) -> float: ...
    def GetLength(self) -> float:
        """
        Length.
        """
    def GetNormalized(self, _eps: float = ..., /) -> Vec2d: ...
    def GetProjection(self, _v: Vec2d | list[float] | tuple[float, float], /) -> Vec2d:
        """
        Returns the projection of C{this} onto C{v}.


        That is: ::

          v * (*this * v)

        """
    def Normalize(self, _eps: float = ..., /) -> float:
        """
        Normalizes the vector in place to unit length, returning the length
        before normalization.


        If the length of the vector is smaller than C{eps}, then the vector is
        set to vector/ C{eps}. The original length of the vector is returned.
        See also GfNormalize() .
        """
    @staticmethod
    def XAxis() -> Vec2d:
        """
        Create a unit vector along the X-axis.
        """
    @staticmethod
    def YAxis() -> Vec2d:
        """
        Create a unit vector along the Y-axis.
        """
    def __add__(self, arg2: Vec2d | list[float] | tuple[float, float], /) -> Any: ...
    def __contains__(self, arg2: float, /) -> bool: ...
    def __eq__(self, other: object) -> bool:
        """
        Equality comparison.
        """
    def __getinitargs__(self) -> tuple: ...
    @overload
    def __getitem__(self, _i: int, /) -> list:
        """
        Indexing.
        """
    @overload
    def __getitem__(self, arg2: int, /) -> float: ...
    def __hash__(self) -> int: ...
    def __iadd__(self, arg2: Vec2d | list[float] | tuple[float, float], /) -> Any: ...
    def __idiv__(self, arg2: float, /) -> Any: ...
    def __imul__(self, arg2: float, /) -> Any: ...
    def __isub__(self, arg2: Vec2d | list[float] | tuple[float, float], /) -> Any: ...
    def __itruediv__(self, arg2: float, /) -> Vec2d: ...
    def __len__(self) -> int: ...
    @overload
    def __mul__(self, arg2: float, /) -> Any: ...
    @overload
    def __mul__(self, arg2: Vec2d | list[float] | tuple[float, float], /) -> Any: ...
    def __ne__(self, other: object) -> bool: ...
    def __neg__(self) -> Any: ...
    def __rmul__(self, arg2: float, /) -> Any: ...
    @overload
    def __setitem__(self, arg2: int, arg3: float, /) -> None: ...
    @overload
    def __setitem__(self, arg2: object, arg3: object, /) -> None: ...
    def __sub__(self, arg2: Vec2d | list[float] | tuple[float, float], /) -> Any: ...
    def __truediv__(self, arg2: float, /) -> Any: ...

class Vec2f(Boost.Python.instance):
    """
    Basic type for a vector of 2 float components.


    Represents a vector of 2 components of type C{float}. It is intended
    to be fast and simple.
    """
    __isGfVec: ClassVar[bool] = ...  # read-only
    dimension: ClassVar[int] = ...  # read-only
    __safe_for_unpickling__: ClassVar[bool] = ...
    @overload
    def __init__(self) -> None:
        """
        Default constructor does no initialization.
        """
    @overload
    def __init__(self, _value: float, /) -> None:
        """
        Initialize all elements to a single value.
        """
    @overload
    def __init__(self, _s0: float, _s1: float, /) -> None:
        """
        Initialize all elements with explicit arguments.
        """
    @overload
    def __init__(self, _other: Vec2d | list[float] | tuple[float, float], /) -> None:
        """
        Construct from GfVec2d.
        """
    @overload
    def __init__(self, _other: Vec2h | list[float] | tuple[float, float], /) -> None:
        """
        Implicitly convert from GfVec2h.
        """
    @overload
    def __init__(self, _other: Vec2i | list[int] | Size2 | tuple[int, int], /) -> None:
        """
        Implicitly convert from GfVec2i.
        """
    @overload
    def __init__(self, _other: Vec2f | list[float] | tuple[float, float], /) -> None:
        """
        Implicitly convert from GfVec2i.
        """
    @staticmethod
    def Axis(_i: int, /) -> Vec2f:
        """
        Create a unit vector along the i-th axis, zero-based.


        Return the zero vector if C{i} is greater than or equal to 2.
        """
    def GetComplement(self, _b: Vec2f | list[float] | tuple[float, float], /) -> Vec2f:
        """
        Returns the orthogonal complement of C{this->GetProjection(b)} .


        That is: ::

          *this - this->GetProjection(b)

        """
    def GetDot(self, arg2: Vec2f | list[float] | tuple[float, float], /) -> float: ...
    def GetLength(self) -> float:
        """
        Length.
        """
    def GetNormalized(self, _eps: float = ..., /) -> Vec2f: ...
    def GetProjection(self, _v: Vec2f | list[float] | tuple[float, float], /) -> Vec2f:
        """
        Returns the projection of C{this} onto C{v}.


        That is: ::

          v * (*this * v)

        """
    def Normalize(self, _eps: float = ..., /) -> float:
        """
        Normalizes the vector in place to unit length, returning the length
        before normalization.


        If the length of the vector is smaller than C{eps}, then the vector is
        set to vector/ C{eps}. The original length of the vector is returned.
        See also GfNormalize() .
        """
    @staticmethod
    def XAxis() -> Vec2f:
        """
        Create a unit vector along the X-axis.
        """
    @staticmethod
    def YAxis() -> Vec2f:
        """
        Create a unit vector along the Y-axis.
        """
    def __add__(self, arg2: Vec2f | list[float] | tuple[float, float], /) -> Any: ...
    def __contains__(self, arg2: float, /) -> bool: ...
    def __eq__(self, other: object) -> bool:
        """
        Equality comparison.
        """
    def __getinitargs__(self) -> tuple: ...
    @overload
    def __getitem__(self, _i: int, /) -> list:
        """
        Indexing.
        """
    @overload
    def __getitem__(self, arg2: int, /) -> float: ...
    def __hash__(self) -> int: ...
    def __iadd__(self, arg2: Vec2f | list[float] | tuple[float, float], /) -> Any: ...
    def __idiv__(self, arg2: float, /) -> Any: ...
    def __imul__(self, arg2: float, /) -> Any: ...
    def __isub__(self, arg2: Vec2f | list[float] | tuple[float, float], /) -> Any: ...
    def __itruediv__(self, arg2: float, /) -> Vec2f: ...
    def __len__(self) -> int: ...
    @overload
    def __mul__(self, arg2: float, /) -> Any: ...
    @overload
    def __mul__(self, arg2: Vec2f | list[float] | tuple[float, float], /) -> Any: ...
    def __ne__(self, other: object) -> bool: ...
    def __neg__(self) -> Any: ...
    def __rmul__(self, arg2: float, /) -> Any: ...
    @overload
    def __setitem__(self, arg2: int, arg3: float, /) -> None: ...
    @overload
    def __setitem__(self, arg2: object, arg3: object, /) -> None: ...
    def __sub__(self, arg2: Vec2f | list[float] | tuple[float, float], /) -> Any: ...
    def __truediv__(self, arg2: float, /) -> Any: ...

class Vec2h(Boost.Python.instance):
    """
    Basic type for a vector of 2 GfHalf components.


    Represents a vector of 2 components of type C{GfHalf}. It is intended
    to be fast and simple.
    """
    __isGfVec: ClassVar[bool] = ...  # read-only
    dimension: ClassVar[int] = ...  # read-only
    __safe_for_unpickling__: ClassVar[bool] = ...
    @overload
    def __init__(self) -> None:
        """
        Default constructor does no initialization.
        """
    @overload
    def __init__(self, _value: float, /) -> None:
        """
        Initialize all elements to a single value.
        """
    @overload
    def __init__(self, _s0: float, _s1: float, /) -> None:
        """
        Initialize all elements with explicit arguments.
        """
    @overload
    def __init__(self, _other: Vec2d | list[float] | tuple[float, float], /) -> None:
        """
        Construct from GfVec2d.
        """
    @overload
    def __init__(self, _other: Vec2f | list[float] | tuple[float, float], /) -> None:
        """
        Construct from GfVec2f.
        """
    @overload
    def __init__(self, _other: Vec2i | list[int] | Size2 | tuple[int, int], /) -> None:
        """
        Implicitly convert from GfVec2i.
        """
    @overload
    def __init__(self, arg2: Vec2h | list[float] | tuple[float, float], /) -> None: ...
    @staticmethod
    def Axis(_i: int, /) -> Vec2h:
        """
        Create a unit vector along the i-th axis, zero-based.


        Return the zero vector if C{i} is greater than or equal to 2.
        """
    def GetComplement(self, _b: Vec2h | list[float] | tuple[float, float], /) -> Vec2h:
        """
        Returns the orthogonal complement of C{this->GetProjection(b)} .


        That is: ::

          *this - this->GetProjection(b)

        """
    def GetDot(self, arg2: Vec2h | list[float] | tuple[float, float], /) -> Any: ...
    def GetLength(self) -> float:
        """
        Length.
        """
    def GetNormalized(self, _eps: float = ..., /) -> Vec2h: ...
    def GetProjection(self, _v: Vec2h | list[float] | tuple[float, float], /) -> Vec2h:
        """
        Returns the projection of C{this} onto C{v}.


        That is: ::

          v * (*this * v)

        """
    def Normalize(self, _eps: float = ..., /) -> float:
        """
        Normalizes the vector in place to unit length, returning the length
        before normalization.


        If the length of the vector is smaller than C{eps}, then the vector is
        set to vector/ C{eps}. The original length of the vector is returned.
        See also GfNormalize() .
        """
    @staticmethod
    def XAxis() -> Vec2h:
        """
        Create a unit vector along the X-axis.
        """
    @staticmethod
    def YAxis() -> Vec2h:
        """
        Create a unit vector along the Y-axis.
        """
    def __add__(self, arg2: Vec2h | list[float] | tuple[float, float], /) -> Any: ...
    def __contains__(self, arg2: object, /) -> bool: ...
    def __eq__(self, other: object) -> bool:
        """
        Equality comparison.
        """
    def __getinitargs__(self) -> tuple: ...
    @overload
    def __getitem__(self, _i: int, /) -> list:
        """
        Indexing.
        """
    @overload
    def __getitem__(self, arg2: int, /) -> Any: ...
    def __hash__(self) -> int: ...
    def __iadd__(self, arg2: Vec2h | list[float] | tuple[float, float], /) -> Any: ...
    def __idiv__(self, arg2: object, /) -> Any: ...
    def __imul__(self, arg2: float, /) -> Any: ...
    def __isub__(self, arg2: Vec2h | list[float] | tuple[float, float], /) -> Any: ...
    def __itruediv__(self, arg2: object, /) -> Vec2h: ...
    def __len__(self) -> int: ...
    @overload
    def __mul__(self, arg2: float, /) -> Any: ...
    @overload
    def __mul__(self, arg2: Vec2h | list[float] | tuple[float, float], /) -> Any: ...
    def __ne__(self, other: object) -> bool: ...
    def __neg__(self) -> Any: ...
    def __rmul__(self, arg2: float, /) -> Any: ...
    @overload
    def __setitem__(self, arg2: int, arg3: object, /) -> None: ...
    @overload
    def __setitem__(self, arg2: object, arg3: object, /) -> None: ...
    def __sub__(self, arg2: Vec2h | list[float] | tuple[float, float], /) -> Any: ...
    def __truediv__(self, arg2: object, /) -> Any: ...

class Vec2i(Boost.Python.instance):
    """
    Basic type for a vector of 2 int components.


    Represents a vector of 2 components of type C{int}. It is intended to
    be fast and simple.
    """
    __isGfVec: ClassVar[bool] = ...  # read-only
    dimension: ClassVar[int] = ...  # read-only
    __safe_for_unpickling__: ClassVar[bool] = ...
    @overload
    def __init__(self) -> None:
        """
        Default constructor does no initialization.
        """
    @overload
    def __init__(self, _value: Vec2i | list[int] | Size2 | tuple[int, int], /) -> None:
        """
        Initialize all elements to a single value.
        """
    @overload
    def __init__(self, _s0: int, _s1: int, /) -> None:
        """
        Initialize all elements with explicit arguments.
        """
    @overload
    def __init__(self, arg2: int, /) -> None: ...
    @staticmethod
    def Axis(_i: int, /) -> Vec2i:
        """
        Create a unit vector along the i-th axis, zero-based.


        Return the zero vector if C{i} is greater than or equal to 2.
        """
    def GetDot(self, arg2: Vec2i | list[int] | Size2 | tuple[int, int], /) -> int: ...
    @staticmethod
    def XAxis() -> Vec2i:
        """
        Create a unit vector along the X-axis.
        """
    @staticmethod
    def YAxis() -> Vec2i:
        """
        Create a unit vector along the Y-axis.
        """
    def __add__(self, arg2: Vec2i | list[int] | Size2 | tuple[int, int], /) -> Any: ...
    def __contains__(self, arg2: int, /) -> bool: ...
    def __eq__(self, other: object) -> bool:
        """
        Equality comparison.
        """
    def __getinitargs__(self) -> tuple: ...
    @overload
    def __getitem__(self, _i: int, /) -> list:
        """
        Indexing.
        """
    @overload
    def __getitem__(self, arg2: int, /) -> int: ...
    def __hash__(self) -> int: ...
    def __iadd__(self, arg2: Vec2i | list[int] | Size2 | tuple[int, int], /) -> Any: ...
    def __idiv__(self, arg2: int, /) -> Any: ...
    def __imul__(self, arg2: float, /) -> Any: ...
    def __isub__(self, arg2: Vec2i | list[int] | Size2 | tuple[int, int], /) -> Any: ...
    def __itruediv__(self, arg2: int, /) -> Vec2i: ...
    def __len__(self) -> int: ...
    @overload
    def __mul__(self, arg2: float, /) -> Any: ...
    @overload
    def __mul__(self, arg2: Vec2i | list[int] | Size2 | tuple[int, int], /) -> Any: ...
    def __ne__(self, other: object) -> bool: ...
    def __neg__(self) -> Any: ...
    def __rmul__(self, arg2: float, /) -> Any: ...
    @overload
    def __setitem__(self, arg2: int, arg3: int, /) -> None: ...
    @overload
    def __setitem__(self, arg2: object, arg3: object, /) -> None: ...
    def __sub__(self, arg2: Vec2i | list[int] | Size2 | tuple[int, int], /) -> Any: ...
    def __truediv__(self, arg2: int, /) -> Any: ...

class Vec3d(Boost.Python.instance):
    """
    Basic type for a vector of 3 double components.


    Represents a vector of 3 components of type C{double}. It is intended
    to be fast and simple.
    """
    __isGfVec: ClassVar[bool] = ...  # read-only
    dimension: ClassVar[int] = ...  # read-only
    __safe_for_unpickling__: ClassVar[bool] = ...
    @overload
    def __init__(self) -> None:
        """
        Default constructor does no initialization.
        """
    @overload
    def __init__(self, _value: float, /) -> None:
        """
        Initialize all elements to a single value.
        """
    @overload
    def __init__(self, _s0: float, _s1: float, _s2: float, /) -> None:
        """
        Initialize all elements with explicit arguments.
        """
    @overload
    def __init__(self, _other: Vec3f | list[float] | tuple[float, float, float], /) -> None:
        """
        Implicitly convert from GfVec3f.
        """
    @overload
    def __init__(self, _other: Vec3h | list[float] | tuple[float, float, float], /) -> None:
        """
        Implicitly convert from GfVec3h.
        """
    @overload
    def __init__(self, _other: Vec3i | list[int] | Size3 | tuple[int, int, int], /) -> None:
        """
        Implicitly convert from GfVec3i.
        """
    @overload
    def __init__(self, _other: Vec3d | list[float] | tuple[float, float, float], /) -> None:
        """
        Implicitly convert from GfVec3i.
        """
    @staticmethod
    def Axis(_i: int, /) -> Vec3d:
        """
        Create a unit vector along the i-th axis, zero-based.


        Return the zero vector if C{i} is greater than or equal to 3.
        """
    def BuildOrthonormalFrame(self, _eps: float = ..., /) -> tuple:
        """
        Sets C{v1} and C{v2} to unit vectors such that v1, v2 and *this are
        mutually orthogonal.


        If the length L of *this is smaller than C{eps}, then v1 and v2 will
        have magnitude L/eps. As a result, the function delivers a continuous
        result as *this shrinks in length.
        """
    def GetComplement(self, _b: Vec3d | list[float] | tuple[float, float, float], /) -> Vec3d:
        """
        Returns the orthogonal complement of C{this->GetProjection(b)} .


        That is: ::

          *this - this->GetProjection(b)

        """
    def GetCross(self, arg2: Vec3d | list[float] | tuple[float, float, float], /) -> Vec3d: ...
    def GetDot(self, arg2: Vec3d | list[float] | tuple[float, float, float], /) -> float: ...
    def GetLength(self) -> float:
        """
        Length.
        """
    def GetNormalized(self, _eps: float = ..., /) -> Vec3d: ...
    def GetProjection(self, _v: Vec3d | list[float] | tuple[float, float, float], /) -> Vec3d:
        """
        Returns the projection of C{this} onto C{v}.


        That is: ::

          v * (*this * v)

        """
    def Normalize(self, _eps: float = ..., /) -> float:
        """
        Normalizes the vector in place to unit length, returning the length
        before normalization.


        If the length of the vector is smaller than C{eps}, then the vector is
        set to vector/ C{eps}. The original length of the vector is returned.
        See also GfNormalize() .
        """
    @staticmethod
    def OrthogonalizeBasis(_tx: Vec3d | list[float] | tuple[float, float, float], _ty: Vec3d | list[float] | tuple[float, float, float], _tz: Vec3d | list[float] | tuple[float, float, float], _normalize: bool, _eps: float = ..., /) -> bool:
        """
        Orthogonalize and optionally normalize a set of basis vectors.


        This uses an iterative method that is very stable even when the
        vectors are far from orthogonal (close to colinear). The number of
        iterations and thus the computation time does increase as the vectors
        become close to colinear, however. Returns a bool specifying whether
        the solution converged after a number of iterations. If it did not
        converge, the returned vectors will be as close as possible to
        orthogonal within the iteration limit. Colinear vectors will be
        unaltered, and the method will return false.
        """
    @staticmethod
    def XAxis() -> Vec3d:
        """
        Create a unit vector along the X-axis.
        """
    @staticmethod
    def YAxis() -> Vec3d:
        """
        Create a unit vector along the Y-axis.
        """
    @staticmethod
    def ZAxis() -> Vec3d:
        """
        Create a unit vector along the Z-axis.
        """
    def __add__(self, arg2: Vec3d | list[float] | tuple[float, float, float], /) -> Any: ...
    def __contains__(self, arg2: float, /) -> bool: ...
    def __eq__(self, other: object) -> bool:
        """
        Equality comparison.
        """
    def __getinitargs__(self) -> tuple: ...
    @overload
    def __getitem__(self, _i: int, /) -> list:
        """
        Indexing.
        """
    @overload
    def __getitem__(self, arg2: int, /) -> float: ...
    def __hash__(self) -> int: ...
    def __iadd__(self, arg2: Vec3d | list[float] | tuple[float, float, float], /) -> Any: ...
    def __idiv__(self, arg2: float, /) -> Any: ...
    def __imul__(self, arg2: float, /) -> Any: ...
    def __isub__(self, arg2: Vec3d | list[float] | tuple[float, float, float], /) -> Any: ...
    def __itruediv__(self, arg2: float, /) -> Vec3d: ...
    def __len__(self) -> int: ...
    @overload
    def __mul__(self, arg2: float, /) -> Any: ...
    @overload
    def __mul__(self, arg2: Vec3d | list[float] | tuple[float, float, float], /) -> Any: ...
    def __ne__(self, other: object) -> bool: ...
    def __neg__(self) -> Any: ...
    def __rmul__(self, arg2: float, /) -> Any: ...
    @overload
    def __setitem__(self, arg2: int, arg3: float, /) -> None: ...
    @overload
    def __setitem__(self, arg2: object, arg3: object, /) -> None: ...
    def __sub__(self, arg2: Vec3d | list[float] | tuple[float, float, float], /) -> Any: ...
    def __truediv__(self, arg2: float, /) -> Any: ...
    def __xor__(self, arg2: Vec3d | list[float] | tuple[float, float, float], /) -> Any: ...

class Vec3f(Boost.Python.instance):
    """
    Basic type for a vector of 3 float components.


    Represents a vector of 3 components of type C{float}. It is intended
    to be fast and simple.
    """
    __isGfVec: ClassVar[bool] = ...  # read-only
    dimension: ClassVar[int] = ...  # read-only
    __safe_for_unpickling__: ClassVar[bool] = ...
    @overload
    def __init__(self) -> None:
        """
        Default constructor does no initialization.
        """
    @overload
    def __init__(self, _value: float, /) -> None:
        """
        Initialize all elements to a single value.
        """
    @overload
    def __init__(self, _s0: float, _s1: float, _s2: float, /) -> None:
        """
        Initialize all elements with explicit arguments.
        """
    @overload
    def __init__(self, _other: Vec3d | list[float] | tuple[float, float, float], /) -> None:
        """
        Construct from GfVec3d.
        """
    @overload
    def __init__(self, _other: Vec3h | list[float] | tuple[float, float, float], /) -> None:
        """
        Implicitly convert from GfVec3h.
        """
    @overload
    def __init__(self, _other: Vec3i | list[int] | Size3 | tuple[int, int, int], /) -> None:
        """
        Implicitly convert from GfVec3i.
        """
    @overload
    def __init__(self, _other: Vec3f | list[float] | tuple[float, float, float], /) -> None:
        """
        Implicitly convert from GfVec3i.
        """
    @staticmethod
    def Axis(_i: int, /) -> Vec3f:
        """
        Create a unit vector along the i-th axis, zero-based.


        Return the zero vector if C{i} is greater than or equal to 3.
        """
    def BuildOrthonormalFrame(self, _eps: float = ..., /) -> tuple:
        """
        Sets C{v1} and C{v2} to unit vectors such that v1, v2 and *this are
        mutually orthogonal.


        If the length L of *this is smaller than C{eps}, then v1 and v2 will
        have magnitude L/eps. As a result, the function delivers a continuous
        result as *this shrinks in length.
        """
    def GetComplement(self, _b: Vec3f | list[float] | tuple[float, float, float], /) -> Vec3f:
        """
        Returns the orthogonal complement of C{this->GetProjection(b)} .


        That is: ::

          *this - this->GetProjection(b)

        """
    def GetCross(self, arg2: Vec3f | list[float] | tuple[float, float, float], /) -> Vec3f: ...
    def GetDot(self, arg2: Vec3f | list[float] | tuple[float, float, float], /) -> float: ...
    def GetLength(self) -> float:
        """
        Length.
        """
    def GetNormalized(self, _eps: float = ..., /) -> Vec3f: ...
    def GetProjection(self, _v: Vec3f | list[float] | tuple[float, float, float], /) -> Vec3f:
        """
        Returns the projection of C{this} onto C{v}.


        That is: ::

          v * (*this * v)

        """
    def Normalize(self, _eps: float = ..., /) -> float:
        """
        Normalizes the vector in place to unit length, returning the length
        before normalization.


        If the length of the vector is smaller than C{eps}, then the vector is
        set to vector/ C{eps}. The original length of the vector is returned.
        See also GfNormalize() .
        """
    @staticmethod
    def OrthogonalizeBasis(_tx: Vec3f | list[float] | tuple[float, float, float], _ty: Vec3f | list[float] | tuple[float, float, float], _tz: Vec3f | list[float] | tuple[float, float, float], _normalize: bool, _eps: float = ..., /) -> bool:
        """
        Orthogonalize and optionally normalize a set of basis vectors.


        This uses an iterative method that is very stable even when the
        vectors are far from orthogonal (close to colinear). The number of
        iterations and thus the computation time does increase as the vectors
        become close to colinear, however. Returns a bool specifying whether
        the solution converged after a number of iterations. If it did not
        converge, the returned vectors will be as close as possible to
        orthogonal within the iteration limit. Colinear vectors will be
        unaltered, and the method will return false.
        """
    @staticmethod
    def XAxis() -> Vec3f:
        """
        Create a unit vector along the X-axis.
        """
    @staticmethod
    def YAxis() -> Vec3f:
        """
        Create a unit vector along the Y-axis.
        """
    @staticmethod
    def ZAxis() -> Vec3f:
        """
        Create a unit vector along the Z-axis.
        """
    def __add__(self, arg2: Vec3f | list[float] | tuple[float, float, float], /) -> Any: ...
    def __contains__(self, arg2: float, /) -> bool: ...
    def __eq__(self, other: object) -> bool:
        """
        Equality comparison.
        """
    def __getinitargs__(self) -> tuple: ...
    @overload
    def __getitem__(self, _i: int, /) -> list:
        """
        Indexing.
        """
    @overload
    def __getitem__(self, arg2: int, /) -> float: ...
    def __hash__(self) -> int: ...
    def __iadd__(self, arg2: Vec3f | list[float] | tuple[float, float, float], /) -> Any: ...
    def __idiv__(self, arg2: float, /) -> Any: ...
    def __imul__(self, arg2: float, /) -> Any: ...
    def __isub__(self, arg2: Vec3f | list[float] | tuple[float, float, float], /) -> Any: ...
    def __itruediv__(self, arg2: float, /) -> Vec3f: ...
    def __len__(self) -> int: ...
    @overload
    def __mul__(self, arg2: float, /) -> Any: ...
    @overload
    def __mul__(self, arg2: Vec3f | list[float] | tuple[float, float, float], /) -> Any: ...
    def __ne__(self, other: object) -> bool: ...
    def __neg__(self) -> Any: ...
    def __rmul__(self, arg2: float, /) -> Any: ...
    @overload
    def __setitem__(self, arg2: int, arg3: float, /) -> None: ...
    @overload
    def __setitem__(self, arg2: object, arg3: object, /) -> None: ...
    def __sub__(self, arg2: Vec3f | list[float] | tuple[float, float, float], /) -> Any: ...
    def __truediv__(self, arg2: float, /) -> Any: ...
    def __xor__(self, arg2: Vec3f | list[float] | tuple[float, float, float], /) -> Any: ...

class Vec3h(Boost.Python.instance):
    """
    Basic type for a vector of 3 GfHalf components.


    Represents a vector of 3 components of type C{GfHalf}. It is intended
    to be fast and simple.
    """
    __isGfVec: ClassVar[bool] = ...  # read-only
    dimension: ClassVar[int] = ...  # read-only
    __safe_for_unpickling__: ClassVar[bool] = ...
    @overload
    def __init__(self) -> None:
        """
        Default constructor does no initialization.
        """
    @overload
    def __init__(self, _value: float, /) -> None:
        """
        Initialize all elements to a single value.
        """
    @overload
    def __init__(self, _s0: float, _s1: float, _s2: float, /) -> None:
        """
        Initialize all elements with explicit arguments.
        """
    @overload
    def __init__(self, _other: Vec3d | list[float] | tuple[float, float, float], /) -> None:
        """
        Construct from GfVec3d.
        """
    @overload
    def __init__(self, _other: Vec3f | list[float] | tuple[float, float, float], /) -> None:
        """
        Construct from GfVec3f.
        """
    @overload
    def __init__(self, _other: Vec3i | list[int] | Size3 | tuple[int, int, int], /) -> None:
        """
        Implicitly convert from GfVec3i.
        """
    @overload
    def __init__(self, arg2: Vec3h | list[float] | tuple[float, float, float], /) -> None: ...
    @staticmethod
    def Axis(_i: int, /) -> Vec3h:
        """
        Create a unit vector along the i-th axis, zero-based.


        Return the zero vector if C{i} is greater than or equal to 3.
        """
    def BuildOrthonormalFrame(self, _eps: float = ..., /) -> tuple:
        """
        Sets C{v1} and C{v2} to unit vectors such that v1, v2 and *this are
        mutually orthogonal.


        If the length L of *this is smaller than C{eps}, then v1 and v2 will
        have magnitude L/eps. As a result, the function delivers a continuous
        result as *this shrinks in length.
        """
    def GetComplement(self, _b: Vec3h | list[float] | tuple[float, float, float], /) -> Vec3h:
        """
        Returns the orthogonal complement of C{this->GetProjection(b)} .


        That is: ::

          *this - this->GetProjection(b)

        """
    def GetCross(self, arg2: Vec3h | list[float] | tuple[float, float, float], /) -> Vec3h: ...
    def GetDot(self, arg2: Vec3h | list[float] | tuple[float, float, float], /) -> Any: ...
    def GetLength(self) -> float:
        """
        Length.
        """
    def GetNormalized(self, _eps: float = ..., /) -> Vec3h: ...
    def GetProjection(self, _v: Vec3h | list[float] | tuple[float, float, float], /) -> Vec3h:
        """
        Returns the projection of C{this} onto C{v}.


        That is: ::

          v * (*this * v)

        """
    def Normalize(self, _eps: float = ..., /) -> float:
        """
        Normalizes the vector in place to unit length, returning the length
        before normalization.


        If the length of the vector is smaller than C{eps}, then the vector is
        set to vector/ C{eps}. The original length of the vector is returned.
        See also GfNormalize() .
        """
    @staticmethod
    def OrthogonalizeBasis(_tx: Vec3h | list[float] | tuple[float, float, float], _ty: Vec3h | list[float] | tuple[float, float, float], _tz: Vec3h | list[float] | tuple[float, float, float], _normalize: bool, _eps: float = ..., /) -> bool:
        """
        Orthogonalize and optionally normalize a set of basis vectors.


        This uses an iterative method that is very stable even when the
        vectors are far from orthogonal (close to colinear). The number of
        iterations and thus the computation time does increase as the vectors
        become close to colinear, however. Returns a bool specifying whether
        the solution converged after a number of iterations. If it did not
        converge, the returned vectors will be as close as possible to
        orthogonal within the iteration limit. Colinear vectors will be
        unaltered, and the method will return false.
        """
    @staticmethod
    def XAxis() -> Vec3h:
        """
        Create a unit vector along the X-axis.
        """
    @staticmethod
    def YAxis() -> Vec3h:
        """
        Create a unit vector along the Y-axis.
        """
    @staticmethod
    def ZAxis() -> Vec3h:
        """
        Create a unit vector along the Z-axis.
        """
    def __add__(self, arg2: Vec3h | list[float] | tuple[float, float, float], /) -> Any: ...
    def __contains__(self, arg2: object, /) -> bool: ...
    def __eq__(self, other: object) -> bool:
        """
        Equality comparison.
        """
    def __getinitargs__(self) -> tuple: ...
    @overload
    def __getitem__(self, _i: int, /) -> list:
        """
        Indexing.
        """
    @overload
    def __getitem__(self, arg2: int, /) -> Any: ...
    def __hash__(self) -> int: ...
    def __iadd__(self, arg2: Vec3h | list[float] | tuple[float, float, float], /) -> Any: ...
    def __idiv__(self, arg2: object, /) -> Any: ...
    def __imul__(self, arg2: float, /) -> Any: ...
    def __isub__(self, arg2: Vec3h | list[float] | tuple[float, float, float], /) -> Any: ...
    def __itruediv__(self, arg2: object, /) -> Vec3h: ...
    def __len__(self) -> int: ...
    @overload
    def __mul__(self, arg2: float, /) -> Any: ...
    @overload
    def __mul__(self, arg2: Vec3h | list[float] | tuple[float, float, float], /) -> Any: ...
    def __ne__(self, other: object) -> bool: ...
    def __neg__(self) -> Any: ...
    def __rmul__(self, arg2: float, /) -> Any: ...
    @overload
    def __setitem__(self, arg2: int, arg3: object, /) -> None: ...
    @overload
    def __setitem__(self, arg2: object, arg3: object, /) -> None: ...
    def __sub__(self, arg2: Vec3h | list[float] | tuple[float, float, float], /) -> Any: ...
    def __truediv__(self, arg2: object, /) -> Any: ...
    def __xor__(self, arg2: Vec3h | list[float] | tuple[float, float, float], /) -> Any: ...

class Vec3i(Boost.Python.instance):
    """
    Basic type for a vector of 3 int components.


    Represents a vector of 3 components of type C{int}. It is intended to
    be fast and simple.
    """
    __isGfVec: ClassVar[bool] = ...  # read-only
    dimension: ClassVar[int] = ...  # read-only
    __safe_for_unpickling__: ClassVar[bool] = ...
    @overload
    def __init__(self) -> None:
        """
        Default constructor does no initialization.
        """
    @overload
    def __init__(self, _value: Vec3i | list[int] | Size3 | tuple[int, int, int], /) -> None:
        """
        Initialize all elements to a single value.
        """
    @overload
    def __init__(self, _s0: int, _s1: int, _s2: int, /) -> None:
        """
        Initialize all elements with explicit arguments.
        """
    @overload
    def __init__(self, arg2: int, /) -> None: ...
    @staticmethod
    def Axis(_i: int, /) -> Vec3i:
        """
        Create a unit vector along the i-th axis, zero-based.


        Return the zero vector if C{i} is greater than or equal to 3.
        """
    def GetDot(self, arg2: Vec3i | list[int] | Size3 | tuple[int, int, int], /) -> int: ...
    @staticmethod
    def XAxis() -> Vec3i:
        """
        Create a unit vector along the X-axis.
        """
    @staticmethod
    def YAxis() -> Vec3i:
        """
        Create a unit vector along the Y-axis.
        """
    @staticmethod
    def ZAxis() -> Vec3i:
        """
        Create a unit vector along the Z-axis.
        """
    def __add__(self, arg2: Vec3i | list[int] | Size3 | tuple[int, int, int], /) -> Any: ...
    def __contains__(self, arg2: int, /) -> bool: ...
    def __eq__(self, other: object) -> bool:
        """
        Equality comparison.
        """
    def __getinitargs__(self) -> tuple: ...
    @overload
    def __getitem__(self, _i: int, /) -> list:
        """
        Indexing.
        """
    @overload
    def __getitem__(self, arg2: int, /) -> int: ...
    def __hash__(self) -> int: ...
    def __iadd__(self, arg2: Vec3i | list[int] | Size3 | tuple[int, int, int], /) -> Any: ...
    def __idiv__(self, arg2: int, /) -> Any: ...
    def __imul__(self, arg2: float, /) -> Any: ...
    def __isub__(self, arg2: Vec3i | list[int] | Size3 | tuple[int, int, int], /) -> Any: ...
    def __itruediv__(self, arg2: int, /) -> Vec3i: ...
    def __len__(self) -> int: ...
    @overload
    def __mul__(self, arg2: float, /) -> Any: ...
    @overload
    def __mul__(self, arg2: Vec3i | list[int] | Size3 | tuple[int, int, int], /) -> Any: ...
    def __ne__(self, other: object) -> bool: ...
    def __neg__(self) -> Any: ...
    def __rmul__(self, arg2: float, /) -> Any: ...
    @overload
    def __setitem__(self, arg2: int, arg3: int, /) -> None: ...
    @overload
    def __setitem__(self, arg2: object, arg3: object, /) -> None: ...
    def __sub__(self, arg2: Vec3i | list[int] | Size3 | tuple[int, int, int], /) -> Any: ...
    def __truediv__(self, arg2: int, /) -> Any: ...

class Vec4d(Boost.Python.instance):
    """
    Basic type for a vector of 4 double components.


    Represents a vector of 4 components of type C{double}. It is intended
    to be fast and simple.
    """
    __isGfVec: ClassVar[bool] = ...  # read-only
    dimension: ClassVar[int] = ...  # read-only
    __safe_for_unpickling__: ClassVar[bool] = ...
    @overload
    def __init__(self) -> None:
        """
        Default constructor does no initialization.
        """
    @overload
    def __init__(self, _value: float, /) -> None:
        """
        Initialize all elements to a single value.
        """
    @overload
    def __init__(self, _s0: float, _s1: float, _s2: float, _s3: float, /) -> None:
        """
        Initialize all elements with explicit arguments.
        """
    @overload
    def __init__(self, _other: Vec4f | list[float] | tuple[float, float, float, float], /) -> None:
        """
        Implicitly convert from GfVec4f.
        """
    @overload
    def __init__(self, _other: Vec4h | list[float] | tuple[float, float, float, float], /) -> None:
        """
        Implicitly convert from GfVec4h.
        """
    @overload
    def __init__(self, _other: Vec4i | list[int] | tuple[int, int, int, int], /) -> None:
        """
        Implicitly convert from GfVec4i.
        """
    @overload
    def __init__(self, _other: Vec4d | list[float] | tuple[float, float, float, float], /) -> None:
        """
        Implicitly convert from GfVec4i.
        """
    @staticmethod
    def Axis(_i: int, /) -> Vec4d:
        """
        Create a unit vector along the i-th axis, zero-based.


        Return the zero vector if C{i} is greater than or equal to 4.
        """
    def GetComplement(self, _b: Vec4d | list[float] | tuple[float, float, float, float], /) -> Vec4d:
        """
        Returns the orthogonal complement of C{this->GetProjection(b)} .


        That is: ::

          *this - this->GetProjection(b)

        """
    def GetDot(self, arg2: Vec4d | list[float] | tuple[float, float, float, float], /) -> float: ...
    def GetLength(self) -> float:
        """
        Length.
        """
    def GetNormalized(self, _eps: float = ..., /) -> Vec4d: ...
    def GetProjection(self, _v: Vec4d | list[float] | tuple[float, float, float, float], /) -> Vec4d:
        """
        Returns the projection of C{this} onto C{v}.


        That is: ::

          v * (*this * v)

        """
    def Normalize(self, _eps: float = ..., /) -> float:
        """
        Normalizes the vector in place to unit length, returning the length
        before normalization.


        If the length of the vector is smaller than C{eps}, then the vector is
        set to vector/ C{eps}. The original length of the vector is returned.
        See also GfNormalize() .
        """
    @staticmethod
    def WAxis() -> Vec4d:
        """
        Create a unit vector along the W-axis.
        """
    @staticmethod
    def XAxis() -> Vec4d:
        """
        Create a unit vector along the X-axis.
        """
    @staticmethod
    def YAxis() -> Vec4d:
        """
        Create a unit vector along the Y-axis.
        """
    @staticmethod
    def ZAxis() -> Vec4d:
        """
        Create a unit vector along the Z-axis.
        """
    def __add__(self, arg2: Vec4d | list[float] | tuple[float, float, float, float], /) -> Any: ...
    def __contains__(self, arg2: float, /) -> bool: ...
    def __eq__(self, other: object) -> bool:
        """
        Equality comparison.
        """
    def __getinitargs__(self) -> tuple: ...
    @overload
    def __getitem__(self, _i: int, /) -> list:
        """
        Indexing.
        """
    @overload
    def __getitem__(self, arg2: int, /) -> float: ...
    def __hash__(self) -> int: ...
    def __iadd__(self, arg2: Vec4d | list[float] | tuple[float, float, float, float], /) -> Any: ...
    def __idiv__(self, arg2: float, /) -> Any: ...
    def __imul__(self, arg2: float, /) -> Any: ...
    def __isub__(self, arg2: Vec4d | list[float] | tuple[float, float, float, float], /) -> Any: ...
    def __itruediv__(self, arg2: float, /) -> Vec4d: ...
    def __len__(self) -> int: ...
    @overload
    def __mul__(self, arg2: float, /) -> Any: ...
    @overload
    def __mul__(self, arg2: Vec4d | list[float] | tuple[float, float, float, float], /) -> Any: ...
    def __ne__(self, other: object) -> bool: ...
    def __neg__(self) -> Any: ...
    def __rmul__(self, arg2: float, /) -> Any: ...
    @overload
    def __setitem__(self, arg2: int, arg3: float, /) -> None: ...
    @overload
    def __setitem__(self, arg2: object, arg3: object, /) -> None: ...
    def __sub__(self, arg2: Vec4d | list[float] | tuple[float, float, float, float], /) -> Any: ...
    def __truediv__(self, arg2: float, /) -> Any: ...

class Vec4f(Boost.Python.instance):
    """
    Basic type for a vector of 4 float components.


    Represents a vector of 4 components of type C{float}. It is intended
    to be fast and simple.
    """
    __isGfVec: ClassVar[bool] = ...  # read-only
    dimension: ClassVar[int] = ...  # read-only
    __safe_for_unpickling__: ClassVar[bool] = ...
    @overload
    def __init__(self) -> None:
        """
        Default constructor does no initialization.
        """
    @overload
    def __init__(self, _value: float, /) -> None:
        """
        Initialize all elements to a single value.
        """
    @overload
    def __init__(self, _s0: float, _s1: float, _s2: float, _s3: float, /) -> None:
        """
        Initialize all elements with explicit arguments.
        """
    @overload
    def __init__(self, _other: Vec4d | list[float] | tuple[float, float, float, float], /) -> None:
        """
        Construct from GfVec4d.
        """
    @overload
    def __init__(self, _other: Vec4h | list[float] | tuple[float, float, float, float], /) -> None:
        """
        Implicitly convert from GfVec4h.
        """
    @overload
    def __init__(self, _other: Vec4i | list[int] | tuple[int, int, int, int], /) -> None:
        """
        Implicitly convert from GfVec4i.
        """
    @overload
    def __init__(self, _other: Vec4f | list[float] | tuple[float, float, float, float], /) -> None:
        """
        Implicitly convert from GfVec4i.
        """
    @staticmethod
    def Axis(_i: int, /) -> Vec4f:
        """
        Create a unit vector along the i-th axis, zero-based.


        Return the zero vector if C{i} is greater than or equal to 4.
        """
    def GetComplement(self, _b: Vec4f | list[float] | tuple[float, float, float, float], /) -> Vec4f:
        """
        Returns the orthogonal complement of C{this->GetProjection(b)} .


        That is: ::

          *this - this->GetProjection(b)

        """
    def GetDot(self, arg2: Vec4f | list[float] | tuple[float, float, float, float], /) -> float: ...
    def GetLength(self) -> float:
        """
        Length.
        """
    def GetNormalized(self, _eps: float = ..., /) -> Vec4f: ...
    def GetProjection(self, _v: Vec4f | list[float] | tuple[float, float, float, float], /) -> Vec4f:
        """
        Returns the projection of C{this} onto C{v}.


        That is: ::

          v * (*this * v)

        """
    def Normalize(self, _eps: float = ..., /) -> float:
        """
        Normalizes the vector in place to unit length, returning the length
        before normalization.


        If the length of the vector is smaller than C{eps}, then the vector is
        set to vector/ C{eps}. The original length of the vector is returned.
        See also GfNormalize() .
        """
    @staticmethod
    def WAxis() -> Vec4f:
        """
        Create a unit vector along the W-axis.
        """
    @staticmethod
    def XAxis() -> Vec4f:
        """
        Create a unit vector along the X-axis.
        """
    @staticmethod
    def YAxis() -> Vec4f:
        """
        Create a unit vector along the Y-axis.
        """
    @staticmethod
    def ZAxis() -> Vec4f:
        """
        Create a unit vector along the Z-axis.
        """
    def __add__(self, arg2: Vec4f | list[float] | tuple[float, float, float, float], /) -> Any: ...
    def __contains__(self, arg2: float, /) -> bool: ...
    def __eq__(self, other: object) -> bool:
        """
        Equality comparison.
        """
    def __getinitargs__(self) -> tuple: ...
    @overload
    def __getitem__(self, _i: int, /) -> list:
        """
        Indexing.
        """
    @overload
    def __getitem__(self, arg2: int, /) -> float: ...
    def __hash__(self) -> int: ...
    def __iadd__(self, arg2: Vec4f | list[float] | tuple[float, float, float, float], /) -> Any: ...
    def __idiv__(self, arg2: float, /) -> Any: ...
    def __imul__(self, arg2: float, /) -> Any: ...
    def __isub__(self, arg2: Vec4f | list[float] | tuple[float, float, float, float], /) -> Any: ...
    def __itruediv__(self, arg2: float, /) -> Vec4f: ...
    def __len__(self) -> int: ...
    @overload
    def __mul__(self, arg2: float, /) -> Any: ...
    @overload
    def __mul__(self, arg2: Vec4f | list[float] | tuple[float, float, float, float], /) -> Any: ...
    def __ne__(self, other: object) -> bool: ...
    def __neg__(self) -> Any: ...
    def __rmul__(self, arg2: float, /) -> Any: ...
    @overload
    def __setitem__(self, arg2: int, arg3: float, /) -> None: ...
    @overload
    def __setitem__(self, arg2: object, arg3: object, /) -> None: ...
    def __sub__(self, arg2: Vec4f | list[float] | tuple[float, float, float, float], /) -> Any: ...
    def __truediv__(self, arg2: float, /) -> Any: ...

class Vec4h(Boost.Python.instance):
    """
    Basic type for a vector of 4 GfHalf components.


    Represents a vector of 4 components of type C{GfHalf}. It is intended
    to be fast and simple.
    """
    __isGfVec: ClassVar[bool] = ...  # read-only
    dimension: ClassVar[int] = ...  # read-only
    __safe_for_unpickling__: ClassVar[bool] = ...
    @overload
    def __init__(self) -> None:
        """
        Default constructor does no initialization.
        """
    @overload
    def __init__(self, _value: float, /) -> None:
        """
        Initialize all elements to a single value.
        """
    @overload
    def __init__(self, _s0: float, _s1: float, _s2: float, _s3: float, /) -> None:
        """
        Initialize all elements with explicit arguments.
        """
    @overload
    def __init__(self, _other: Vec4d | list[float] | tuple[float, float, float, float], /) -> None:
        """
        Construct from GfVec4d.
        """
    @overload
    def __init__(self, _other: Vec4f | list[float] | tuple[float, float, float, float], /) -> None:
        """
        Construct from GfVec4f.
        """
    @overload
    def __init__(self, _other: Vec4i | list[int] | tuple[int, int, int, int], /) -> None:
        """
        Implicitly convert from GfVec4i.
        """
    @overload
    def __init__(self, arg2: Vec4h | list[float] | tuple[float, float, float, float], /) -> None: ...
    @staticmethod
    def Axis(_i: int, /) -> Vec4h:
        """
        Create a unit vector along the i-th axis, zero-based.


        Return the zero vector if C{i} is greater than or equal to 4.
        """
    def GetComplement(self, _b: Vec4h | list[float] | tuple[float, float, float, float], /) -> Vec4h:
        """
        Returns the orthogonal complement of C{this->GetProjection(b)} .


        That is: ::

          *this - this->GetProjection(b)

        """
    def GetDot(self, arg2: Vec4h | list[float] | tuple[float, float, float, float], /) -> Any: ...
    def GetLength(self) -> float:
        """
        Length.
        """
    def GetNormalized(self, _eps: float = ..., /) -> Vec4h: ...
    def GetProjection(self, _v: Vec4h | list[float] | tuple[float, float, float, float], /) -> Vec4h:
        """
        Returns the projection of C{this} onto C{v}.


        That is: ::

          v * (*this * v)

        """
    def Normalize(self, _eps: float = ..., /) -> float:
        """
        Normalizes the vector in place to unit length, returning the length
        before normalization.


        If the length of the vector is smaller than C{eps}, then the vector is
        set to vector/ C{eps}. The original length of the vector is returned.
        See also GfNormalize() .
        """
    @staticmethod
    def WAxis() -> Vec4h:
        """
        Create a unit vector along the W-axis.
        """
    @staticmethod
    def XAxis() -> Vec4h:
        """
        Create a unit vector along the X-axis.
        """
    @staticmethod
    def YAxis() -> Vec4h:
        """
        Create a unit vector along the Y-axis.
        """
    @staticmethod
    def ZAxis() -> Vec4h:
        """
        Create a unit vector along the Z-axis.
        """
    def __add__(self, arg2: Vec4h | list[float] | tuple[float, float, float, float], /) -> Any: ...
    def __contains__(self, arg2: object, /) -> bool: ...
    def __eq__(self, other: object) -> bool:
        """
        Equality comparison.
        """
    def __getinitargs__(self) -> tuple: ...
    @overload
    def __getitem__(self, _i: int, /) -> list:
        """
        Indexing.
        """
    @overload
    def __getitem__(self, arg2: int, /) -> Any: ...
    def __hash__(self) -> int: ...
    def __iadd__(self, arg2: Vec4h | list[float] | tuple[float, float, float, float], /) -> Any: ...
    def __idiv__(self, arg2: object, /) -> Any: ...
    def __imul__(self, arg2: float, /) -> Any: ...
    def __isub__(self, arg2: Vec4h | list[float] | tuple[float, float, float, float], /) -> Any: ...
    def __itruediv__(self, arg2: object, /) -> Vec4h: ...
    def __len__(self) -> int: ...
    @overload
    def __mul__(self, arg2: float, /) -> Any: ...
    @overload
    def __mul__(self, arg2: Vec4h | list[float] | tuple[float, float, float, float], /) -> Any: ...
    def __ne__(self, other: object) -> bool: ...
    def __neg__(self) -> Any: ...
    def __rmul__(self, arg2: float, /) -> Any: ...
    @overload
    def __setitem__(self, arg2: int, arg3: object, /) -> None: ...
    @overload
    def __setitem__(self, arg2: object, arg3: object, /) -> None: ...
    def __sub__(self, arg2: Vec4h | list[float] | tuple[float, float, float, float], /) -> Any: ...
    def __truediv__(self, arg2: object, /) -> Any: ...

class Vec4i(Boost.Python.instance):
    """
    Basic type for a vector of 4 int components.


    Represents a vector of 4 components of type C{int}. It is intended to
    be fast and simple.
    """
    __isGfVec: ClassVar[bool] = ...  # read-only
    dimension: ClassVar[int] = ...  # read-only
    __safe_for_unpickling__: ClassVar[bool] = ...
    @overload
    def __init__(self) -> None:
        """
        Default constructor does no initialization.
        """
    @overload
    def __init__(self, _value: Vec4i | list[int] | tuple[int, int, int, int], /) -> None:
        """
        Initialize all elements to a single value.
        """
    @overload
    def __init__(self, _s0: int, _s1: int, _s2: int, _s3: int, /) -> None:
        """
        Initialize all elements with explicit arguments.
        """
    @overload
    def __init__(self, arg2: int, /) -> None: ...
    @staticmethod
    def Axis(_i: int, /) -> Vec4i:
        """
        Create a unit vector along the i-th axis, zero-based.


        Return the zero vector if C{i} is greater than or equal to 4.
        """
    def GetDot(self, arg2: Vec4i | list[int] | tuple[int, int, int, int], /) -> int: ...
    @staticmethod
    def WAxis() -> Vec4i:
        """
        Create a unit vector along the W-axis.
        """
    @staticmethod
    def XAxis() -> Vec4i:
        """
        Create a unit vector along the X-axis.
        """
    @staticmethod
    def YAxis() -> Vec4i:
        """
        Create a unit vector along the Y-axis.
        """
    @staticmethod
    def ZAxis() -> Vec4i:
        """
        Create a unit vector along the Z-axis.
        """
    def __add__(self, arg2: Vec4i | list[int] | tuple[int, int, int, int], /) -> Any: ...
    def __contains__(self, arg2: int, /) -> bool: ...
    def __eq__(self, other: object) -> bool:
        """
        Equality comparison.
        """
    def __getinitargs__(self) -> tuple: ...
    @overload
    def __getitem__(self, _i: int, /) -> list:
        """
        Indexing.
        """
    @overload
    def __getitem__(self, arg2: int, /) -> int: ...
    def __hash__(self) -> int: ...
    def __iadd__(self, arg2: Vec4i | list[int] | tuple[int, int, int, int], /) -> Any: ...
    def __idiv__(self, arg2: int, /) -> Any: ...
    def __imul__(self, arg2: float, /) -> Any: ...
    def __isub__(self, arg2: Vec4i | list[int] | tuple[int, int, int, int], /) -> Any: ...
    def __itruediv__(self, arg2: int, /) -> Vec4i: ...
    def __len__(self) -> int: ...
    @overload
    def __mul__(self, arg2: float, /) -> Any: ...
    @overload
    def __mul__(self, arg2: Vec4i | list[int] | tuple[int, int, int, int], /) -> Any: ...
    def __ne__(self, other: object) -> bool: ...
    def __neg__(self) -> Any: ...
    def __rmul__(self, arg2: float, /) -> Any: ...
    @overload
    def __setitem__(self, arg2: int, arg3: int, /) -> None: ...
    @overload
    def __setitem__(self, arg2: object, arg3: object, /) -> None: ...
    def __sub__(self, arg2: Vec4i | list[int] | tuple[int, int, int, int], /) -> Any: ...
    def __truediv__(self, arg2: int, /) -> Any: ...

def Abs(_f: float, /) -> float:
    """
    Return abs( C{f}).
    """
def Absf(arg1: float, /) -> float:
    """Absf(f) -> float

    f : float

    Use instead of Abs() to return the absolute value of f as a float instead of a double."""
@overload
def ApplyGamma(_v: Vec3f | list[float] | tuple[float, float, float], _gamma: float, /) -> Vec3f:
    """
    Return a new vector with each component of C{v} raised to the power
    C{gamma}.
    """
@overload
def ApplyGamma(_v: Vec3d | list[float] | tuple[float, float, float], _gamma: float, /) -> Vec3d:
    """
    Return a new vector with each component of C{v} raised to the power
    C{gamma}.
    """
@overload
def ApplyGamma(_v: Vec3h | list[float] | tuple[float, float, float], _gamma: float, /) -> Vec3h: ...
@overload
def ApplyGamma(_v: Vec4f | list[float] | tuple[float, float, float, float], _gamma: float, /) -> Vec4f:
    """
    Return a new vector with the first three components of C{v} raised to
    the power C{gamma} and the fourth component unchanged.
    """
@overload
def ApplyGamma(_v: Vec4d | list[float] | tuple[float, float, float, float], _gamma: float, /) -> Vec4d:
    """
    Return a new vector with the first three components of C{v} raised to
    the power C{gamma} and the fourth component unchanged.
    """
@overload
def ApplyGamma(_v: Vec4h | list[float] | tuple[float, float, float, float], _gamma: float, /) -> Vec4h: ...
def Ceil(_f: float, /) -> float:
    """
    Return ceil( C{f}).
    """
def Ceilf(arg1: float, /) -> float:
    """Ceilf(f) -> float

    f : float

    Use instead of Ceil() to return the ceiling of f as a float instead of a double."""
def Clamp(_value: float, _min: float, _max: float, /) -> float:
    """
    Return the resulting of clamping C{value} to lie between C{min} and
    C{max}.


    This function is also defined for GfVecs.
    """
def Clampf(arg1: float, arg2: float, arg3: float, /) -> float:
    """Clampf(f) -> float

    f : float

    Use instead of Clamp() to return the clamped value of f as a float instead of a double."""
@overload
def CompDiv(_left: Vec4d | list[float] | tuple[float, float, float, float], _right: Vec4d | list[float] | tuple[float, float, float, float], /) -> Vec4d:
    """
    Returns component-wise quotient of vectors.


    For scalar types, this is just the regular quotient.
    """
@overload
def CompDiv(arg1: float, arg2: float, /) -> float: ...
@overload
def CompDiv(arg1: Vec2h | list[float] | tuple[float, float], arg2: Vec2h | list[float] | tuple[float, float], /) -> Vec2h: ...
@overload
def CompDiv(arg1: Vec2f | list[float] | tuple[float, float], arg2: Vec2f | list[float] | tuple[float, float], /) -> Vec2f: ...
@overload
def CompDiv(arg1: Vec2d | list[float] | tuple[float, float], arg2: Vec2d | list[float] | tuple[float, float], /) -> Vec2d: ...
@overload
def CompDiv(arg1: Vec3h | list[float] | tuple[float, float, float], arg2: Vec3h | list[float] | tuple[float, float, float], /) -> Vec3h: ...
@overload
def CompDiv(arg1: Vec3f | list[float] | tuple[float, float, float], arg2: Vec3f | list[float] | tuple[float, float, float], /) -> Vec3f: ...
@overload
def CompDiv(arg1: Vec3d | list[float] | tuple[float, float, float], arg2: Vec3d | list[float] | tuple[float, float, float], /) -> Vec3d: ...
@overload
def CompDiv(arg1: Vec4h | list[float] | tuple[float, float, float, float], arg2: Vec4h | list[float] | tuple[float, float, float, float], /) -> Vec4h: ...
@overload
def CompDiv(arg1: Vec4f | list[float] | tuple[float, float, float, float], arg2: Vec4f | list[float] | tuple[float, float, float, float], /) -> Vec4f: ...
@overload
def CompMult(_left: Vec4d | list[float] | tuple[float, float, float, float], _right: Vec4d | list[float] | tuple[float, float, float, float], /) -> Vec4d:
    """
    Returns component-wise multiplication of vectors.


    For scalar types, this is just the regular product.
    """
@overload
def CompMult(arg1: float, arg2: float, /) -> float: ...
@overload
def CompMult(arg1: Vec2h | list[float] | tuple[float, float], arg2: Vec2h | list[float] | tuple[float, float], /) -> Vec2h: ...
@overload
def CompMult(arg1: Vec2f | list[float] | tuple[float, float], arg2: Vec2f | list[float] | tuple[float, float], /) -> Vec2f: ...
@overload
def CompMult(arg1: Vec2d | list[float] | tuple[float, float], arg2: Vec2d | list[float] | tuple[float, float], /) -> Vec2d: ...
@overload
def CompMult(arg1: Vec3h | list[float] | tuple[float, float, float], arg2: Vec3h | list[float] | tuple[float, float, float], /) -> Vec3h: ...
@overload
def CompMult(arg1: Vec3f | list[float] | tuple[float, float, float], arg2: Vec3f | list[float] | tuple[float, float, float], /) -> Vec3f: ...
@overload
def CompMult(arg1: Vec3d | list[float] | tuple[float, float, float], arg2: Vec3d | list[float] | tuple[float, float, float], /) -> Vec3d: ...
@overload
def CompMult(arg1: Vec4h | list[float] | tuple[float, float, float, float], arg2: Vec4h | list[float] | tuple[float, float, float, float], /) -> Vec4h: ...
@overload
def CompMult(arg1: Vec4f | list[float] | tuple[float, float, float, float], arg2: Vec4f | list[float] | tuple[float, float, float, float], /) -> Vec4f: ...
@overload
def ConvertDisplayToLinear(_v: Vec3f | list[float] | tuple[float, float, float], /) -> Vec3f:
    """
    Given a vec, C{v}, representing an RGB(A) color in the system's
    display gamma space, return an energy-linear vec of the same type.
    """
@overload
def ConvertDisplayToLinear(_v: Vec3d | list[float] | tuple[float, float, float], /) -> Vec3d: ...
@overload
def ConvertDisplayToLinear(_v: Vec3h | list[float] | tuple[float, float, float], /) -> Vec3h: ...
@overload
def ConvertDisplayToLinear(_v: Vec4f | list[float] | tuple[float, float, float, float], /) -> Vec4f: ...
@overload
def ConvertDisplayToLinear(_v: Vec4d | list[float] | tuple[float, float, float, float], /) -> Vec4d: ...
@overload
def ConvertDisplayToLinear(_v: Vec4h | list[float] | tuple[float, float, float, float], /) -> Vec4h: ...
@overload
def ConvertLinearToDisplay(_v: Vec3f | list[float] | tuple[float, float, float], /) -> Vec3f:
    """
    Given a vec, C{v}, representing an energy-linear RGB(A) color, return
    a vec of the same type converted to the system's display gamma.
    """
@overload
def ConvertLinearToDisplay(_v: Vec3d | list[float] | tuple[float, float, float], /) -> Vec3d: ...
@overload
def ConvertLinearToDisplay(_v: Vec3h | list[float] | tuple[float, float, float], /) -> Vec3h: ...
@overload
def ConvertLinearToDisplay(_v: Vec4f | list[float] | tuple[float, float, float, float], /) -> Vec4f: ...
@overload
def ConvertLinearToDisplay(_v: Vec4d | list[float] | tuple[float, float, float, float], /) -> Vec4d: ...
@overload
def ConvertLinearToDisplay(_v: Vec4h | list[float] | tuple[float, float, float, float], /) -> Vec4h: ...
@overload
def Cross(_v1: Vec3d | list[float] | tuple[float, float, float], _v2: Vec3d | list[float] | tuple[float, float, float], /) -> Vec3d:
    """
    Returns the cross product of C{v1} and C{v2}.
    """
@overload
def Cross(arg1: Vec3h | list[float] | tuple[float, float, float], arg2: Vec3h | list[float] | tuple[float, float, float], /) -> Vec3h: ...
@overload
def Cross(arg1: Vec3f | list[float] | tuple[float, float, float], arg2: Vec3f | list[float] | tuple[float, float, float], /) -> Vec3f: ...
def DegreesToRadians(_degrees: float, /) -> float:
    """
    Converts an angle in degrees to radians.
    """
@overload
def Dot(_left: Vec4i | list[int] | tuple[int, int, int, int], _right: Vec4i | list[int] | tuple[int, int, int, int], /) -> int:
    """
    Returns the dot (inner) product of two vectors.


    For scalar types, this is just the regular product.
    """
@overload
def Dot(arg1: DualQuatd | DualQuatf | DualQuath, arg2: DualQuatd | DualQuatf | DualQuath, /) -> float: ...
@overload
def Dot(arg1: DualQuatf | DualQuath, arg2: DualQuatf | DualQuath, /) -> float: ...
@overload
def Dot(arg1: DualQuath, arg2: DualQuath, /) -> Any: ...
@overload
def Dot(arg1: float, arg2: float, /) -> float: ...
@overload
def Dot(arg1: Quatd | Quatf | Quath, arg2: Quatd | Quatf | Quath, /) -> float: ...
@overload
def Dot(arg1: Quatf | Quath, arg2: Quatf | Quath, /) -> float: ...
@overload
def Dot(arg1: Quath, arg2: Quath, /) -> Any: ...
@overload
def Dot(arg1: Quaternion, arg2: Quaternion, /) -> float: ...
@overload
def Dot(arg1: Vec2h | list[float] | tuple[float, float], arg2: Vec2h | list[float] | tuple[float, float], /) -> Any: ...
@overload
def Dot(arg1: Vec2f | list[float] | tuple[float, float], arg2: Vec2f | list[float] | tuple[float, float], /) -> float: ...
@overload
def Dot(arg1: Vec2d | list[float] | tuple[float, float], arg2: Vec2d | list[float] | tuple[float, float], /) -> float: ...
@overload
def Dot(arg1: Vec2i | list[int] | Size2 | tuple[int, int], arg2: Vec2i | list[int] | Size2 | tuple[int, int], /) -> int: ...
@overload
def Dot(arg1: Vec3h | list[float] | tuple[float, float, float], arg2: Vec3h | list[float] | tuple[float, float, float], /) -> Any: ...
@overload
def Dot(arg1: Vec3f | list[float] | tuple[float, float, float], arg2: Vec3f | list[float] | tuple[float, float, float], /) -> float: ...
@overload
def Dot(arg1: Vec3d | list[float] | tuple[float, float, float], arg2: Vec3d | list[float] | tuple[float, float, float], /) -> float: ...
@overload
def Dot(arg1: Vec3i | list[int] | Size3 | tuple[int, int, int], arg2: Vec3i | list[int] | Size3 | tuple[int, int, int], /) -> int: ...
@overload
def Dot(arg1: Vec4h | list[float] | tuple[float, float, float, float], arg2: Vec4h | list[float] | tuple[float, float, float, float], /) -> Any: ...
@overload
def Dot(arg1: Vec4f | list[float] | tuple[float, float, float, float], arg2: Vec4f | list[float] | tuple[float, float, float, float], /) -> float: ...
@overload
def Dot(arg1: Vec4d | list[float] | tuple[float, float, float, float], arg2: Vec4d | list[float] | tuple[float, float, float, float], /) -> float: ...
def Exp(_f: float, /) -> float:
    """
    Return exp( C{f}).
    """
def Expf(arg1: float, /) -> float:
    """Expf(f) -> float

    f : float

    Use instead of Exp() to return the exponent of f as a float instead of a double."""
@overload
def FindClosestPoints(_ray: Ray, _line: Line, /) -> tuple:
    """
    Computes the closest points between a ray and a line.


    The two points are returned in C{rayPoint} and C{linePoint}. The
    parametric distance of each point on the lines is returned in
    C{rayDistance} and C{lineDistance}.

    This returns C{false} if the lines were close enough to parallel that
    no points could be computed; in this case, the other return values are
    undefined.
    """
@overload
def FindClosestPoints(_ray: Ray, _seg: LineSeg, /) -> tuple:
    """
    Computes the closest points between a ray and a line segment.


    The two points are returned in C{rayPoint} and C{segPoint}. The
    parametric distance of each point is returned in C{rayDistance} and
    C{segDistance}.

    This returns C{false} if the lines were close enough to parallel that
    no points could be computed; in this case, the other return values are
    undefined.
    """
@overload
def FindClosestPoints(arg1: Line, arg2: Line, /) -> tuple:
    """    FindClosestPoints( l1, l2 ) -> tuple<intersects = bool, p1 = GfVec3d, p2 = GfVec3d, t1 = double, t2 = double>

        l1 : GfLine
        l2 : GfLine

        Computes the closest points between two lines, returning a tuple.  The first item in the tuple is true if the linesintersect.  The two points are returned in p1 and p2.  The parametric distance of each point on the lines is returned in t1 and t2.
        ----------------------------------------------------------------------

    FindClosestPoints( (Line)arg1, (LineSeg)arg2) -> tuple :
        FindClosestPoints( l1, s2 ) -> tuple< intersects = bool, p1 = GfVec3d, p2 = GfVec3d, t1 = double, t2 = double>

        l1 : GfLine
        s2 : GfLineSeg

        Computes the closest points between a line and a line segment, returning a tuple. The first item in the tuple is true if they intersect. The two points are returned in p1 and p2.  The parametric distance of each point on the line and line segment is returned in t1 and t2.
        ----------------------------------------------------------------------

    FindClosestPoints( (LineSeg)arg1, (LineSeg)arg2) -> tuple :
        FindClosestPoints( s1, s2 ) -> tuple<result = bool,p1 = GfVec3d, p2 = GfVec3d, t1 = double, t2 = double>

        l1 : GfLineSeg
        l2 : GfLineSeg

        Computes the closest points between two line segments, returning a tuple.  The first item in the tuple is true if they intersect.  The two points are returned in p1 and p2.  The parametric distance of each point on the line and line segment is returned in t1 and t2.
        ----------------------------------------------------------------------

    FindClosestPoints( (Ray)arg1, (Line)arg2) -> tuple :
        FindClosestPoints( r1, l2 ) -> tuple<intersects=bool, p1 = GfVec3d, p2 = GfVec3d, t1 = double, t2 = double>

        r1 : GfRay
        l2 : GfLine

        Computes the closest points between a ray and a line,
        returning a tuple. The first item in the tuple is true if they intersect. The two points are returned in p1 and p2.
        The parametric distance of each point on the ray and line is
        returned in t1 and t2.
        ----------------------------------------------------------------------

    FindClosestPoints( (Ray)arg1, (LineSeg)arg2) -> tuple :
        FindClosestPoints( r1, s2 ) -> tuple<intersects = bool, p1 = GfVec3d, p2 = GfVec3d, t1 = double, t2 = double>

        r1 : GfRay
        s2 : GfLineSeg

        Computes the closest points between a ray and a line segment,
        returning a tuple. The first item in the tuple is true if they intersect. The two points are returned in p1 and p2.
        The parametric distance of each point on the ray and line
        segment is returned in t1 and t2.
        ----------------------------------------------------------------------"""
@overload
def FindClosestPoints(arg1: Line, arg2: LineSeg, /) -> tuple:
    """    FindClosestPoints( l1, l2 ) -> tuple<intersects = bool, p1 = GfVec3d, p2 = GfVec3d, t1 = double, t2 = double>

        l1 : GfLine
        l2 : GfLine

        Computes the closest points between two lines, returning a tuple.  The first item in the tuple is true if the linesintersect.  The two points are returned in p1 and p2.  The parametric distance of each point on the lines is returned in t1 and t2.
        ----------------------------------------------------------------------

    FindClosestPoints( (Line)arg1, (LineSeg)arg2) -> tuple :
        FindClosestPoints( l1, s2 ) -> tuple< intersects = bool, p1 = GfVec3d, p2 = GfVec3d, t1 = double, t2 = double>

        l1 : GfLine
        s2 : GfLineSeg

        Computes the closest points between a line and a line segment, returning a tuple. The first item in the tuple is true if they intersect. The two points are returned in p1 and p2.  The parametric distance of each point on the line and line segment is returned in t1 and t2.
        ----------------------------------------------------------------------

    FindClosestPoints( (LineSeg)arg1, (LineSeg)arg2) -> tuple :
        FindClosestPoints( s1, s2 ) -> tuple<result = bool,p1 = GfVec3d, p2 = GfVec3d, t1 = double, t2 = double>

        l1 : GfLineSeg
        l2 : GfLineSeg

        Computes the closest points between two line segments, returning a tuple.  The first item in the tuple is true if they intersect.  The two points are returned in p1 and p2.  The parametric distance of each point on the line and line segment is returned in t1 and t2.
        ----------------------------------------------------------------------

    FindClosestPoints( (Ray)arg1, (Line)arg2) -> tuple :
        FindClosestPoints( r1, l2 ) -> tuple<intersects=bool, p1 = GfVec3d, p2 = GfVec3d, t1 = double, t2 = double>

        r1 : GfRay
        l2 : GfLine

        Computes the closest points between a ray and a line,
        returning a tuple. The first item in the tuple is true if they intersect. The two points are returned in p1 and p2.
        The parametric distance of each point on the ray and line is
        returned in t1 and t2.
        ----------------------------------------------------------------------

    FindClosestPoints( (Ray)arg1, (LineSeg)arg2) -> tuple :
        FindClosestPoints( r1, s2 ) -> tuple<intersects = bool, p1 = GfVec3d, p2 = GfVec3d, t1 = double, t2 = double>

        r1 : GfRay
        s2 : GfLineSeg

        Computes the closest points between a ray and a line segment,
        returning a tuple. The first item in the tuple is true if they intersect. The two points are returned in p1 and p2.
        The parametric distance of each point on the ray and line
        segment is returned in t1 and t2.
        ----------------------------------------------------------------------"""
@overload
def FindClosestPoints(arg1: LineSeg, arg2: LineSeg, /) -> tuple:
    """    FindClosestPoints( l1, l2 ) -> tuple<intersects = bool, p1 = GfVec3d, p2 = GfVec3d, t1 = double, t2 = double>

        l1 : GfLine
        l2 : GfLine

        Computes the closest points between two lines, returning a tuple.  The first item in the tuple is true if the linesintersect.  The two points are returned in p1 and p2.  The parametric distance of each point on the lines is returned in t1 and t2.
        ----------------------------------------------------------------------

    FindClosestPoints( (Line)arg1, (LineSeg)arg2) -> tuple :
        FindClosestPoints( l1, s2 ) -> tuple< intersects = bool, p1 = GfVec3d, p2 = GfVec3d, t1 = double, t2 = double>

        l1 : GfLine
        s2 : GfLineSeg

        Computes the closest points between a line and a line segment, returning a tuple. The first item in the tuple is true if they intersect. The two points are returned in p1 and p2.  The parametric distance of each point on the line and line segment is returned in t1 and t2.
        ----------------------------------------------------------------------

    FindClosestPoints( (LineSeg)arg1, (LineSeg)arg2) -> tuple :
        FindClosestPoints( s1, s2 ) -> tuple<result = bool,p1 = GfVec3d, p2 = GfVec3d, t1 = double, t2 = double>

        l1 : GfLineSeg
        l2 : GfLineSeg

        Computes the closest points between two line segments, returning a tuple.  The first item in the tuple is true if they intersect.  The two points are returned in p1 and p2.  The parametric distance of each point on the line and line segment is returned in t1 and t2.
        ----------------------------------------------------------------------

    FindClosestPoints( (Ray)arg1, (Line)arg2) -> tuple :
        FindClosestPoints( r1, l2 ) -> tuple<intersects=bool, p1 = GfVec3d, p2 = GfVec3d, t1 = double, t2 = double>

        r1 : GfRay
        l2 : GfLine

        Computes the closest points between a ray and a line,
        returning a tuple. The first item in the tuple is true if they intersect. The two points are returned in p1 and p2.
        The parametric distance of each point on the ray and line is
        returned in t1 and t2.
        ----------------------------------------------------------------------

    FindClosestPoints( (Ray)arg1, (LineSeg)arg2) -> tuple :
        FindClosestPoints( r1, s2 ) -> tuple<intersects = bool, p1 = GfVec3d, p2 = GfVec3d, t1 = double, t2 = double>

        r1 : GfRay
        s2 : GfLineSeg

        Computes the closest points between a ray and a line segment,
        returning a tuple. The first item in the tuple is true if they intersect. The two points are returned in p1 and p2.
        The parametric distance of each point on the ray and line
        segment is returned in t1 and t2.
        ----------------------------------------------------------------------"""
def FitPlaneToPoints(_points: typing.Iterable[Vec3d | list[float] | tuple[float, float, float]], /) -> Plane:
    '''
    Fits a plane to the given C{points}.


    There must be at least three points in order to fit the plane; if the
    size of C{points} is less than three, this issues a coding error.

    If the C{points} are all collinear, then no plane can be determined,
    and this function returns C{false}. Otherwise, if the fitting is
    successful, it returns C{true} and sets C{*fitPlane} to the fitted
    plane. If C{points} contains exactly three points, then the resulting
    plane is the exact plane defined by the three points. If C{points}
    contains more than three points, then this function determines the
    best-fitting plane for the given points. The orientation of the plane
    normal is arbitrary with regards to the plane\'s positive and negative
    half-spaces; you can use GfPlane::Reorient() to flip the plane if
    necessary.

    The current implementation uses linear least squares and thus
    defines"best-fitting"as minimizing the sum of the squares of the
    vertical distances between points and the plane surface.
    '''
def Floor(_f: float, /) -> float:
    """
    Return floor( C{f}).
    """
def Floorf(arg1: float, /) -> float:
    """Floorf(f) -> float

    f : float

    Use instead of Floor() to return the floor of f as a float instead of a double."""
@overload
def GetComplement(_a: Vec4d | list[float] | tuple[float, float, float, float], _b: Vec4d | list[float] | tuple[float, float, float, float], /) -> Vec4d:
    """
    Returns the orthogonal complement of C{a.GetProjection(b)} .


    That is: ::

      a - a.GetProjection(b)

    """
@overload
def GetComplement(arg1: Vec2h | list[float] | tuple[float, float], arg2: Vec2h | list[float] | tuple[float, float], /) -> Vec2h: ...
@overload
def GetComplement(arg1: Vec2f | list[float] | tuple[float, float], arg2: Vec2f | list[float] | tuple[float, float], /) -> Vec2f: ...
@overload
def GetComplement(arg1: Vec2d | list[float] | tuple[float, float], arg2: Vec2d | list[float] | tuple[float, float], /) -> Vec2d: ...
@overload
def GetComplement(arg1: Vec3h | list[float] | tuple[float, float, float], arg2: Vec3h | list[float] | tuple[float, float, float], /) -> Vec3h: ...
@overload
def GetComplement(arg1: Vec3f | list[float] | tuple[float, float, float], arg2: Vec3f | list[float] | tuple[float, float, float], /) -> Vec3f: ...
@overload
def GetComplement(arg1: Vec3d | list[float] | tuple[float, float, float], arg2: Vec3d | list[float] | tuple[float, float, float], /) -> Vec3d: ...
@overload
def GetComplement(arg1: Vec4h | list[float] | tuple[float, float, float, float], arg2: Vec4h | list[float] | tuple[float, float, float, float], /) -> Vec4h: ...
@overload
def GetComplement(arg1: Vec4f | list[float] | tuple[float, float, float, float], arg2: Vec4f | list[float] | tuple[float, float, float, float], /) -> Vec4f: ...
def GetDisplayGamma() -> float:
    """
    Return the system display gamma.
    """
@overload
def GetHomogenized(_v: Vec4d | list[float] | tuple[float, float, float, float], /) -> Vec4d:
    """
    Returns a vector which is C{v} homogenized.


    If the fourth element of C{v} is 0, it is set to 1.
    """
@overload
def GetHomogenized(arg1: Vec4f | list[float] | tuple[float, float, float, float], /) -> Vec4f: ...
@overload
def GetLength(_v: Vec4d | list[float] | tuple[float, float, float, float], /) -> float:
    """
    Returns the geometric length of C{v}.
    """
@overload
def GetLength(arg1: Vec2h | list[float] | tuple[float, float], /) -> Any: ...
@overload
def GetLength(arg1: Vec2f | list[float] | tuple[float, float], /) -> float: ...
@overload
def GetLength(arg1: Vec2d | list[float] | tuple[float, float], /) -> float: ...
@overload
def GetLength(arg1: Vec3h | list[float] | tuple[float, float, float], /) -> Any: ...
@overload
def GetLength(arg1: Vec3f | list[float] | tuple[float, float, float], /) -> float: ...
@overload
def GetLength(arg1: Vec3d | list[float] | tuple[float, float, float], /) -> float: ...
@overload
def GetLength(arg1: Vec4h | list[float] | tuple[float, float, float, float], /) -> Any: ...
@overload
def GetLength(arg1: Vec4f | list[float] | tuple[float, float, float, float], /) -> float: ...
@overload
def GetNormalized(_v: Vec4d | list[float] | tuple[float, float, float, float], _eps: float = ..., /) -> Vec4d:
    """
    Returns a normalized (unit-length) vector with the same direction as
    C{v}.


    If the length of this vector is smaller than C{eps}, the vector
    divided by C{eps} is returned.
    """
@overload
def GetNormalized(arg1: Vec2h | list[float] | tuple[float, float], arg2: object = ..., /) -> Vec2h: ...
@overload
def GetNormalized(arg1: Vec2f | list[float] | tuple[float, float], arg2: float = ..., /) -> Vec2f: ...
@overload
def GetNormalized(arg1: Vec2d | list[float] | tuple[float, float], arg2: float = ..., /) -> Vec2d: ...
@overload
def GetNormalized(arg1: Vec3h | list[float] | tuple[float, float, float], arg2: object = ..., /) -> Vec3h: ...
@overload
def GetNormalized(arg1: Vec3f | list[float] | tuple[float, float, float], arg2: float = ..., /) -> Vec3f: ...
@overload
def GetNormalized(arg1: Vec3d | list[float] | tuple[float, float, float], arg2: float = ..., /) -> Vec3d: ...
@overload
def GetNormalized(arg1: Vec4h | list[float] | tuple[float, float, float, float], arg2: object = ..., /) -> Vec4h: ...
@overload
def GetNormalized(arg1: Vec4f | list[float] | tuple[float, float, float, float], arg2: float = ..., /) -> Vec4f: ...
@overload
def GetProjection(_a: Vec4d | list[float] | tuple[float, float, float, float], _b: Vec4d | list[float] | tuple[float, float, float, float], /) -> Vec4d:
    """
    Returns the projection of C{a} onto C{b}.


    That is: ::

      b * (a * b)

    """
@overload
def GetProjection(arg1: Vec2h | list[float] | tuple[float, float], arg2: Vec2h | list[float] | tuple[float, float], /) -> Vec2h: ...
@overload
def GetProjection(arg1: Vec2f | list[float] | tuple[float, float], arg2: Vec2f | list[float] | tuple[float, float], /) -> Vec2f: ...
@overload
def GetProjection(arg1: Vec2d | list[float] | tuple[float, float], arg2: Vec2d | list[float] | tuple[float, float], /) -> Vec2d: ...
@overload
def GetProjection(arg1: Vec3h | list[float] | tuple[float, float, float], arg2: Vec3h | list[float] | tuple[float, float, float], /) -> Vec3h: ...
@overload
def GetProjection(arg1: Vec3f | list[float] | tuple[float, float, float], arg2: Vec3f | list[float] | tuple[float, float, float], /) -> Vec3f: ...
@overload
def GetProjection(arg1: Vec3d | list[float] | tuple[float, float, float], arg2: Vec3d | list[float] | tuple[float, float, float], /) -> Vec3d: ...
@overload
def GetProjection(arg1: Vec4h | list[float] | tuple[float, float, float, float], arg2: Vec4h | list[float] | tuple[float, float, float, float], /) -> Vec4h: ...
@overload
def GetProjection(arg1: Vec4f | list[float] | tuple[float, float, float, float], arg2: Vec4f | list[float] | tuple[float, float, float, float], /) -> Vec4f: ...
@overload
def HomogeneousCross(_a: Vec4f | list[float] | tuple[float, float, float, float], _b: Vec4f | list[float] | tuple[float, float, float, float], /) -> Vec4f:
    """
    Homogenizes C{a} and C{b} and then performs the cross product on the
    first three elements of each.


    Returns the cross product as a homogenized vector.
    """
@overload
def HomogeneousCross(_a: Vec4d | list[float] | tuple[float, float, float, float], _b: Vec4d | list[float] | tuple[float, float, float, float], /) -> Vec4d:
    """
    Homogenizes C{a} and C{b} and then performs the cross product on the
    first three elements of each.


    Returns the cross product as a homogenized vector.
    """
@overload
def IsClose(_a: Vec4d | list[float] | tuple[float, float, float, float], _b: Vec4d | list[float] | tuple[float, float, float, float], _epsilon: float, /) -> bool:
    """
    Returns true if C{a} and C{b} are with C{epsilon} of each other.
    """
@overload
def IsClose(arg1: float, arg2: float, arg3: float, /) -> bool: ...
@overload
def IsClose(arg1: Matrix2d, arg2: Matrix2d, arg3: float, /) -> bool: ...
@overload
def IsClose(arg1: Matrix2f, arg2: Matrix2f, arg3: float, /) -> bool: ...
@overload
def IsClose(arg1: Matrix3d, arg2: Matrix3d, arg3: float, /) -> bool: ...
@overload
def IsClose(arg1: Matrix3f, arg2: Matrix3f, arg3: float, /) -> bool: ...
@overload
def IsClose(arg1: Matrix4f, arg2: Matrix4f, arg3: float, /) -> bool: ...
@overload
def IsClose(arg1: Matrix4d, arg2: Matrix4d, arg3: float, /) -> bool: ...
@overload
def IsClose(arg1: Vec2h | list[float] | tuple[float, float], arg2: Vec2h | list[float] | tuple[float, float], arg3: float, /) -> bool: ...
@overload
def IsClose(arg1: Vec2f | list[float] | tuple[float, float], arg2: Vec2f | list[float] | tuple[float, float], arg3: float, /) -> bool: ...
@overload
def IsClose(arg1: Vec2d | list[float] | tuple[float, float], arg2: Vec2d | list[float] | tuple[float, float], arg3: float, /) -> bool: ...
@overload
def IsClose(arg1: Vec3h | list[float] | tuple[float, float, float], arg2: Vec3h | list[float] | tuple[float, float, float], arg3: float, /) -> bool: ...
@overload
def IsClose(arg1: Vec3f | list[float] | tuple[float, float, float], arg2: Vec3f | list[float] | tuple[float, float, float], arg3: float, /) -> bool: ...
@overload
def IsClose(arg1: Vec3d | list[float] | tuple[float, float, float], arg2: Vec3d | list[float] | tuple[float, float, float], arg3: float, /) -> bool: ...
@overload
def IsClose(arg1: Vec4h | list[float] | tuple[float, float, float, float], arg2: Vec4h | list[float] | tuple[float, float, float, float], arg3: float, /) -> bool: ...
@overload
def IsClose(arg1: Vec4f | list[float] | tuple[float, float, float, float], arg2: Vec4f | list[float] | tuple[float, float, float, float], arg3: float, /) -> bool: ...
@overload
def Lerp(_alpha: float, _a: Vec4d | list[float] | tuple[float, float, float, float], _b: Vec4d | list[float] | tuple[float, float, float, float], /) -> Vec4d:
    """
    Linear interpolation function.


    For any type that supports multiplication by a scalar and binary
    addition, returns ::

      (1-alpha) * a + alpha * b 

    """
@overload
def Lerp(arg1: float, arg2: float, arg3: float, /) -> float: ...
@overload
def Lerp(arg1: float, arg2: Vec2i | list[int] | Size2 | tuple[int, int], arg3: Vec2i | list[int] | Size2 | tuple[int, int], /) -> Vec2i: ...
@overload
def Lerp(arg1: float, arg2: Vec3i | list[int] | Size3 | tuple[int, int, int], arg3: Vec3i | list[int] | Size3 | tuple[int, int, int], /) -> Vec3i: ...
@overload
def Lerp(arg1: float, arg2: Vec2f | list[float] | tuple[float, float], arg3: Vec2f | list[float] | tuple[float, float], /) -> Vec2f: ...
@overload
def Lerp(arg1: float, arg2: Vec3f | list[float] | tuple[float, float, float], arg3: Vec3f | list[float] | tuple[float, float, float], /) -> Vec3f: ...
@overload
def Lerp(arg1: float, arg2: Vec4f | list[float] | tuple[float, float, float, float], arg3: Vec4f | list[float] | tuple[float, float, float, float], /) -> Vec4f: ...
@overload
def Lerp(arg1: float, arg2: Vec2d | list[float] | tuple[float, float], arg3: Vec2d | list[float] | tuple[float, float], /) -> Vec2d: ...
@overload
def Lerp(arg1: float, arg2: Vec3d | list[float] | tuple[float, float, float], arg3: Vec3d | list[float] | tuple[float, float, float], /) -> Vec3d: ...
def Lerpf(arg1: float, arg2: float, arg3: float, /) -> float:
    """Lerpf(f) -> float

    f : float

    Use instead of Lerp() to return the linear interpolation of f as a float instead of a double."""
def Log(_f: float, /) -> float:
    """
    Return log( C{f}).
    """
def Logf(arg1: float, /) -> float:
    """Logf(f) -> float

    f : float

    Use instead of Log() to return the logarithm of f as a float instead of a double."""
@overload
def Max(_a1: int, _a2: int, /) -> int:
    """
    Returns the largest of the given C{values}.
    """
@overload
def Max(arg1: float, arg2: float, /) -> float: ...
@overload
def Max(arg1: float, arg2: float, arg3: float, /) -> float: ...
@overload
def Max(arg1: float, arg2: float, arg3: float, arg4: float, /) -> float: ...
@overload
def Max(arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, /) -> float: ...
@overload
def Max(arg1: int, arg2: int, arg3: int, /) -> int: ...
@overload
def Max(arg1: int, arg2: int, arg3: int, arg4: int, /) -> int: ...
@overload
def Max(arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, /) -> int: ...
@overload
def Min(_a1: int, _a2: int, /) -> int:
    """
    Returns the smallest of the given C{values}.
    """
@overload
def Min(arg1: float, arg2: float, /) -> float: ...
@overload
def Min(arg1: float, arg2: float, arg3: float, /) -> float: ...
@overload
def Min(arg1: float, arg2: float, arg3: float, arg4: float, /) -> float: ...
@overload
def Min(arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, /) -> float: ...
@overload
def Min(arg1: int, arg2: int, arg3: int, /) -> int: ...
@overload
def Min(arg1: int, arg2: int, arg3: int, arg4: int, /) -> int: ...
@overload
def Min(arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, /) -> int: ...
def Mod(_a: float, _b: float, /) -> float:
    '''
    The mod function with"correct"behaviour for negative numbers.


    If C{a} = C{n} C{b} for some integer C{n}, zero is returned.
    Otherwise, for positive C{a}, the value returned is C{fmod(a,b)} , and
    for negative C{a}, the value returned is C{fmod(a,b)+b}.
    '''
def Modf(arg1: float, arg2: float, /) -> float:
    """Modf(f) -> float

    f : float

    Use instead of Mod() to return the modulus of f as a float instead of a double."""
@overload
def Normalize(_v: Vec4d | list[float] | tuple[float, float, float, float], _eps: float = ..., /) -> float:
    """
    Normalizes C{*v} in place to unit length, returning the length before
    normalization.


    If the length of C{*v} is smaller than C{eps} then C{*v} is set to
    C{*v/eps}. The original length of C{*v} is returned.
    """
@overload
def Normalize(arg1: Vec2h | list[float] | tuple[float, float], arg2: object = ..., /) -> Any: ...
@overload
def Normalize(arg1: Vec2f | list[float] | tuple[float, float], arg2: float = ..., /) -> float: ...
@overload
def Normalize(arg1: Vec2d | list[float] | tuple[float, float], arg2: float = ..., /) -> float: ...
@overload
def Normalize(arg1: Vec3h | list[float] | tuple[float, float, float], arg2: object = ..., /) -> Any: ...
@overload
def Normalize(arg1: Vec3f | list[float] | tuple[float, float, float], arg2: float = ..., /) -> float: ...
@overload
def Normalize(arg1: Vec3d | list[float] | tuple[float, float, float], arg2: float = ..., /) -> float: ...
@overload
def Normalize(arg1: Vec4h | list[float] | tuple[float, float, float, float], arg2: object = ..., /) -> Any: ...
@overload
def Normalize(arg1: Vec4f | list[float] | tuple[float, float, float, float], arg2: float = ..., /) -> float: ...
def Pow(_f: float, _p: float, /) -> float:
    """
    Return pow( C{f}, C{p}).
    """
def Powf(arg1: float, arg2: float, /) -> float:
    """Powf(f) -> float

    f : float

    Use instead of Pow() to return the power of f as a float instead of a double."""
@overload
def Project(_v: Vec4f | list[float] | tuple[float, float, float, float], /) -> Vec3f:
    """
    Projects homogeneous C{v} into Euclidean space and returns the result
    as a Vec3f.
    """
@overload
def Project(_v: Vec4d | list[float] | tuple[float, float, float, float], /) -> Vec3d:
    """
    Projects homogeneous C{v} into Euclidean space and returns the result
    as a Vec3d.
    """
def RadiansToDegrees(_radians: float, /) -> float:
    """
    Converts an angle in radians to degrees.
    """
def Round(_f: float, /) -> float:
    """
    Return round( C{f}).
    """
def Roundf(arg1: float, /) -> float:
    """Roundf(f) -> float

    f : float

    Use instead of Round() to return the rounded value of f as a float instead of a double."""
@overload
def Sgn(_v: int, /) -> int:
    """
    Return the signum of C{v} (i.e.


    -1, 0, or 1).

    The type C{T} must implement the<and>operators; the function returns
    zero only if value neither positive, nor negative.
    """
@overload
def Sgn(arg1: float, /) -> float: ...
@overload
def Slerp(_alpha: float, _v0: Vec3d | list[float] | tuple[float, float, float], _v1: Vec3d | list[float] | tuple[float, float, float], /) -> Vec3d:
    """
    Spherical linear interpolation in three dimensions.
    """
@overload
def Slerp(arg1: float, arg2: Quatd | Quatf | Quath, arg3: Quatd | Quatf | Quath, /) -> Quatd: ...
@overload
def Slerp(arg1: float, arg2: Quatf | Quath, arg3: Quatf | Quath, /) -> Quatf: ...
@overload
def Slerp(arg1: float, arg2: Quath, arg3: Quath, /) -> Quath: ...
@overload
def Slerp(arg1: float, arg2: Quaternion, arg3: Quaternion, /) -> Quaternion: ...
@overload
def Slerp(arg1: float, arg2: Vec3h | list[float] | tuple[float, float, float], arg3: Vec3h | list[float] | tuple[float, float, float], /) -> Vec3h: ...
@overload
def Slerp(arg1: float, arg2: Vec3f | list[float] | tuple[float, float, float], arg3: Vec3f | list[float] | tuple[float, float, float], /) -> Vec3f: ...
@overload
def Sqr(_x: Vec4d | list[float] | tuple[float, float, float, float], /) -> float:
    """
    Returns the inner product of C{x} with itself: specifically, C{x*x}.


    Defined for C{int}, C{float}, C{double}, and all C{GfVec} types.
    """
@overload
def Sqr(arg1: float, /) -> float: ...
@overload
def Sqr(arg1: int, /) -> float: ...
@overload
def Sqr(arg1: Vec2i | list[int] | Size2 | tuple[int, int], /) -> float: ...
@overload
def Sqr(arg1: Vec3i | list[int] | Size3 | tuple[int, int, int], /) -> float: ...
@overload
def Sqr(arg1: Vec2f | list[float] | tuple[float, float], /) -> float: ...
@overload
def Sqr(arg1: Vec3f | list[float] | tuple[float, float, float], /) -> float: ...
@overload
def Sqr(arg1: Vec4f | list[float] | tuple[float, float, float, float], /) -> float: ...
@overload
def Sqr(arg1: Vec2d | list[float] | tuple[float, float], /) -> float: ...
@overload
def Sqr(arg1: Vec3d | list[float] | tuple[float, float, float], /) -> float: ...
def Sqrt(_f: float, /) -> float:
    """
    Return sqrt( C{f}).
    """
def Sqrtf(arg1: float, /) -> float:
    """Sqrtf(f) -> float

    f : float

    Use instead of Sqrt() to return the square root of f as a float instead of a double."""
def _HalfRoundTrip(arg1: object, /) -> Any: ...
