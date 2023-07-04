# mypy: disable_error_code = misc
import Boost.Python
import pxr.Ar
import pxr.Gf
from typing import Any, ClassVar, overload

__MFB_FULL_PACKAGE_NAME: str

class DrawTarget(Boost.Python.instance):
    @overload
    def __init__(self, arg2: int, arg3: int) -> None: ...
    @overload
    def __init__(self, arg2: pxr.Gf.Vec2i | list[int] | pxr.Gf.Size2 | tuple[int, int]) -> None: ...
    def AddAttachment(self, arg2: str | pxr.Ar.ResolvedPath, arg3: int, arg4: int, arg5: int) -> None: ...
    def Bind(self) -> None: ...
    def Unbind(self) -> None: ...
    def WriteToFile(self, attachment: str | pxr.Ar.ResolvedPath, filename: str | pxr.Ar.ResolvedPath, viewMatrix: pxr.Gf.Matrix4d = ..., projectionMatrix: pxr.Gf.Matrix4d = ...) -> bool: ...
    def __bool__(self) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    def __lt__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    def __reduce__(self): ...
    @property
    def expired(self) -> Any: ...

class GLQueryObject(Boost.Python.instance):
    __instance_size__: ClassVar[int] = ...
    def __init__(self) -> None: ...
    def Begin(self, arg2: int) -> None: ...
    def BeginPrimitivesGenerated(self) -> None: ...
    def BeginSamplesPassed(self) -> None: ...
    def BeginTimeElapsed(self) -> None: ...
    def End(self) -> None: ...
    def GetResult(self) -> int: ...
    def GetResultNoWait(self) -> int: ...
    def __reduce__(self): ...

class SimpleLight(Boost.Python.instance):
    __instance_size__: ClassVar[int] = ...
    ambient: pxr.Gf.Vec4f
    attenuation: pxr.Gf.Vec3f
    diffuse: pxr.Gf.Vec4f
    hasShadow: Any
    id: Any
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
    def __reduce__(self): ...

class SimpleMaterial(Boost.Python.instance):
    __instance_size__: ClassVar[int] = ...
    ambient: pxr.Gf.Vec4f
    diffuse: pxr.Gf.Vec4f
    emission: pxr.Gf.Vec4f
    shininess: float
    specular: pxr.Gf.Vec4f
    def __init__(self) -> None: ...
    def __reduce__(self): ...

class Texture(Boost.Python.instance):
    memoryRequested: int
    def __init__(self, *args, **kwargs) -> None: ...
    @classmethod
    def GetTextureMemoryAllocated(cls) -> int: ...
    def __reduce__(self): ...
    @property
    def magFilterSupported(self) -> Any: ...
    @property
    def memoryUsed(self) -> int: ...
    @property
    def minFilterSupported(self) -> Any: ...

def RegisterDefaultDebugOutputMessageCallback() -> None: ...