# mypy: disable-error-code="misc, override, no-redef"

import Boost.Python
import pxr.Ar
import pxr.Gf
from _typeshed import Incomplete
from typing import ClassVar, overload

__MFB_FULL_PACKAGE_NAME: str

class DrawTarget(Boost.Python.instance):
    """
    A class representing a GL render target with mutliple image
    attachments.


    A DrawTarget is essentially a custom render pass into which several
    arbitrary variables can be output into. These can later be used as
    texture samplers by GLSL shaders.

    The DrawTarget maintains a map of named attachments that correspond to
    GL_TEXTURE_2D mages. By default, DrawTargets also create a depth
    component that is used both as a depth buffer during the draw pass,
    and can later be accessed as a regular GL_TEXTURE_2D data. Stencils
    are also available (by setting the format to GL_DEPTH_STENCIL and the
    internalFormat to GL_DEPTH24_STENCIL8)
    """
    @overload
    def __init__(self, _size: int, _requestMSAA: int, /) -> None: ...
    @overload
    def __init__(self, _drawtarget: pxr.Gf.Vec2i | list[int] | pxr.Gf.Size2 | tuple[int, int], /) -> None: ...
    def AddAttachment(self, _name: str | pxr.Ar.ResolvedPath, _format: int, _type: int, _internalFormat: int, /) -> None:
        """
        Add an attachment to the DrawTarget.
        """
    def Bind(self) -> None:
        """
        Binds the framebuffer.
        """
    def Unbind(self) -> None:
        """
        Unbinds the framebuffer.
        """
    def WriteToFile(self, attachment: str | pxr.Ar.ResolvedPath, filename: str | pxr.Ar.ResolvedPath, viewMatrix: pxr.Gf.Matrix4d = ..., projectionMatrix: pxr.Gf.Matrix4d = ...) -> bool:
        """
        Write the Attachment buffer to an image file (debugging).
        """
    def __bool__(self) -> bool:
        """True if this object has not expired.  False otherwise."""
    def __eq__(self, other: object) -> bool:
        """Equality operator:  x == y"""
    def __lt__(self, other: object) -> bool:
        """Less than operator: x < y"""
    def __ne__(self, other: object) -> bool:
        """Non-equality operator: x != y"""
    @property
    def expired(self): ...

class GLQueryObject(Boost.Python.instance):
    """
    Represents a GL query object in Glf.
    """
    __instance_size__: ClassVar[int] = ...
    def __init__(self) -> None: ...
    def Begin(self, _target: int, /) -> None:
        """
        Begin query for the given C{target} target has to be one of
        GL_SAMPLES_PASSED, GL_ANY_SAMPLES_PASSED,
        GL_ANY_SAMPLES_PASSED_CONSERVATIVE, GL_PRIMITIVES_GENERATED
        GL_TRANSFORM_FEEDBACK_PRIMITIVES_WRITTEN GL_TIME_ELAPSED,
        GL_TIMESTAMP.
        """
    def BeginPrimitivesGenerated(self) -> None:
        """
        equivalent to Begin(GL_PRIMITIVES_GENERATED).


        The number of primitives sent to the rasterizer by the scoped drawing
        command will be returned.
        """
    def BeginSamplesPassed(self) -> None:
        """
        equivalent to Begin(GL_SAMPLES_PASSED).


        The number of samples that pass the depth test for all drawing
        commands within the scope of the query will be returned.
        """
    def BeginTimeElapsed(self) -> None:
        """
        equivalent to Begin(GL_TIME_ELAPSED).


        The time that it takes for the GPU to execute all of the scoped
        commands will be returned in nanoseconds.
        """
    def End(self) -> None:
        """
        End query.
        """
    def GetResult(self) -> int:
        """
        Return the query result (synchronous) stalls CPU until the result
        becomes available.
        """
    def GetResultNoWait(self) -> int:
        """
        Return the query result (asynchronous) returns 0 if the result hasn't
        been available.
        """

class SimpleLight(Boost.Python.instance):
    __instance_size__: ClassVar[int] = ...
    ambient: pxr.Gf.Vec4f
    attenuation: pxr.Gf.Vec3f
    diffuse: pxr.Gf.Vec4f
    hasShadow: Incomplete
    id: Incomplete
    isCameraSpaceLight: bool
    isDomeLight: bool
    position: pxr.Gf.Vec4f
    shadowBias: float
    shadowBlur: float
    shadowIndexEnd: int
    shadowIndexStart: int
    shadowMatrices: list[pxr.Gf.Matrix4d]
    shadowResolution: int
    specular: pxr.Gf.Vec4f
    spotCutoff: float
    spotDirection: pxr.Gf.Vec3f
    spotFalloff: float
    transform: pxr.Gf.Matrix4d
    def __init__(self) -> None: ...

class SimpleMaterial(Boost.Python.instance):
    __instance_size__: ClassVar[int] = ...
    ambient: pxr.Gf.Vec4f
    diffuse: pxr.Gf.Vec4f
    emission: pxr.Gf.Vec4f
    shininess: float
    specular: pxr.Gf.Vec4f
    def __init__(self) -> None: ...

class Texture(Boost.Python.instance):
    """
    Represents a texture object in Glf.


    A texture is typically defined by reading texture image data from an
    image file but a texture might also represent an attachment of a draw
    target.
    """
    memoryRequested: int
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def GetTextureMemoryAllocated() -> int:
        """
        static reporting function
        """
    @property
    def magFilterSupported(self): ...
    @property
    def memoryUsed(self) -> int:
        """
        Amount of memory used to store the texture.
        """
    @property
    def minFilterSupported(self): ...

def RegisterDefaultDebugOutputMessageCallback() -> None:
    """
    Registers GlfDefaultDebugOutputMessageCallback as the debug message
    callback for the current GL context.
    """
