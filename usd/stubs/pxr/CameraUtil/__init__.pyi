# mypy: disable-error-code="misc, override, no-redef"

import Boost.Python
import pxr.Gf
import pxr.Tf
from _typeshed import Incomplete
from typing import Any, ClassVar, overload

Crop: ConformWindowPolicy
DontConform: ConformWindowPolicy
Fit: ConformWindowPolicy
MatchHorizontally: ConformWindowPolicy
MatchVertically: ConformWindowPolicy
__MFB_FULL_PACKAGE_NAME: str

class ConformWindowPolicy(pxr.Tf.Tf_PyEnumWrapper):
    _baseName: ClassVar[str] = ...
    allValues: ClassVar[tuple] = ...
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def GetValueFromName(name: object) -> Any: ...

class Framing(Boost.Python.instance):
    """
    Framing information.


    That is information determining how the filmback plane of a camera
    maps to the pixels of the rendered image (displayWindow together with
    pixelAspectRatio and window policy) and what pixels of the image will
    be filled by the renderer (dataWindow).

    The concepts of displayWindow and dataWindow are similar to the ones
    in OpenEXR, including that the x- and y-axis of the coordinate system
    point right and down, respectively.

    In fact, these windows mean the same here and in OpenEXR if the
    displayWindow has the same aspect ratio (when accounting for the
    pixelAspectRatio) as the filmback plane of the camera (that is the
    ratio of the horizontalAperture to verticalAperture of, e.g., Usd's
    Camera or GfCamera).

    In particular, overscan can be achieved by making the dataWindow
    larger than the displayWindow.

    If the aspect ratios differ, a window policy is applied to the
    displayWindow to determine how the pixels correspond to the filmback
    plane. One such window policy is to take the largest rect that fits
    (centered) into the displayWindow and has the camera's aspect ratio.
    For example, if the displayWindow and dataWindow are the same and both
    have an aspect ratio smaller than the camera, the image is created by
    enlarging the camera frustum slightly in the bottom and top direction.

    When using the AOVs, the render buffer size is determined
    independently from the framing info. However, the dataWindow is
    supposed to be contained in the render buffer rect (in particular, the
    dataWindow cannot contain pixels with negative coordinates - this
    restriction does not apply if, e.g., hdPrman circumvents AOVs and
    writes directly to EXR). In other words, unlike in OpenEXR, the rect
    of pixels for which we allocate storage can differ from the rect the
    renderer fills with data (dataWindow).

    For example, an application can set the render buffer size to match
    the widget size but use a dataWindow and displayWindow that only fills
    the render buffer horizontally to have slates at the top and bottom.
    """
    __instance_size__: ClassVar[int] = ...
    dataWindow: Incomplete
    displayWindow: Incomplete
    pixelAspectRatio: Incomplete
    @overload
    def __init__(self) -> None:
        """
        Creates an invalid framing, i.e., with empty display and data window.
        """
    @overload
    def __init__(self, displayWindow: pxr.Gf.Range2f | list[float] | tuple[float, float], dataWindow: pxr.Gf.Rect2i, pixelAspectRatio: float = ...) -> None:
        """
        Creates a framing with given display and data window and pixel aspect
        ratio.
        """
    @overload
    def __init__(self, _dataWindow: Framing, /) -> None:
        """
        Creates a framing with equal display and data window (and assuming
        square pixels).
        """
    @overload
    def __init__(self, dataWindow: pxr.Gf.Rect2i) -> None: ...
    def ApplyToProjectionMatrix(self, projectionMatrix: pxr.Gf.Matrix4d, windowPolicy: ConformWindowPolicy) -> pxr.Gf.Matrix4d:
        """
        Given the projectionMatrix computed from a camera, applies the
        framing.


        To obtain a correct result, a rasterizer needs to use the resulting
        projection matrix and set the viewport to the data window.
        """
    def ComputeFilmbackWindow(self, cameraAspectRatio: float, windowPolicy: ConformWindowPolicy) -> pxr.Gf.Range2f:
        """
        The filmback window is the rectangle in pixel space corresponding to
        the filmback plane.


        It is obtained by conforming the display window using the camera's
        aspect ratio.

        Note that the window policy describes how the camera frustum is
        modified to match the display window's aspect ratio. The filmback
        window is transforming differently: if, e.g., the camera frustum's
        height had to be increased to match the displayWindow's aspect ratio
        (since it is less than the camera's aspect ratio and the policy is
        CameraUtilFit), then the filmback window height will be less than that
        of the displayWindow. In other words, imagine an application window
        too tall to display the camera. We will increase the camera frustum's
        height to fill the entire window. To show only what the camera would
        see, we need to add slates on the bottom and top. The filmback window
        is the rect cut out by the slates.
        """
    def IsValid(self) -> bool:
        """
        Is display and data window non-empty.
        """
    def __eq__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...

class ScreenWindowParameters(Boost.Python.instance):
    """
    Given a camera object, compute parameters suitable for setting up
    RenderMan.
    """
    def __init__(self, arg2: pxr.Gf.Camera, /) -> None:
        """
        Constructs screenwindow parameter.


        The optional C{fitDirection} indicates in which direction the
        screenwindow will have length 2.
        """
    @property
    def fieldOfView(self) -> float:
        '''
        The field of view.


        More precisely, the full angle perspective field of view (in degrees)
        between screen space coordinates (-1,0) and (1,0). Give these
        parameters to RiProjection as parameter after"perspective".
        '''
    @property
    def screenWindow(self) -> pxr.Gf.Vec4d:
        """
        The vector (left, right, bottom, top) defining the rectangle in the
        image plane.


        Give these parameters to RiScreenWindow.
        """
    @property
    def zFacingViewMatrix(self) -> pxr.Gf.Matrix4d:
        """
        Returns the inverse of the transform for a camera that is y-Up and
        z-facing (vs the OpenGL camera that is (-z)-facing).


        Write this transform with RiConcatTransform before RiWorldBegin.
        """

@overload
def ConformWindow(camera: pxr.Gf.Camera, policy: ConformWindowPolicy, targetAspect: float) -> None:
    """
    Conforms the given C{camera} to have aspect ratio C{targetAspect} by
    applying C{policy}.
    """
@overload
def ConformWindow(frustum: pxr.Gf.Frustum, policy: ConformWindowPolicy, targetAspect: float) -> None:
    """
    Conforms the given C{frustum} to have aspect ratio C{targetAspect} by
    applying C{policy}.
    """
@overload
def ConformedWindow(window: pxr.Gf.Range2d | list[float] | tuple[float, float], policy: ConformWindowPolicy, targetAspect: float) -> pxr.Gf.Range2d:
    """
    Conforms the given C{projectionMatrix} to have aspect ratio
    C{targetAspect} by applying C{policy}.


    Note that this function also supports mirroring about the x- or y-axis
    of the image corresponding to flipping all signs in the second,
    respectively, third column of the projection matrix. In other words,
    we get the same result whether we flip the signs in the matrix and
    then give it to this function or call this function first and flip the
    signs of the resulting matrix.
    """
@overload
def ConformedWindow(window: pxr.Gf.Vec2d | list[float] | tuple[float, float], policy: ConformWindowPolicy, targetAspect: float) -> pxr.Gf.Vec2d:
    """
    Returns a window with aspect ratio C{targetAspect} by applying
    C{policy} to C{window} where C{window} is encoded as GfRange2d.
    """
@overload
def ConformedWindow(window: pxr.Gf.Vec4d | list[float] | tuple[float, float, float, float], policy: ConformWindowPolicy, targetAspect: float) -> pxr.Gf.Vec4d:
    """
    Returns a window with aspect ratio C{targetAspect} by applying
    C{policy} to C{window} where C{window} is encoded as vector (left,
    right, bottom, top) similarly to RenderMan's RiScreenWindow.
    """
@overload
def ConformedWindow(window: pxr.Gf.Matrix4d, policy: ConformWindowPolicy, targetAspect: float) -> pxr.Gf.Matrix4d:
    """
    Returns a window with aspect ratio C{targetAspect} by applying
    C{policy} to C{window} where C{window} is encoded as vector (width,
    height).
    """
