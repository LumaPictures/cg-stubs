import Boost.Python
from typing import Any, ClassVar, overload

class DrawTarget(Boost.Python.instance):
    @overload
    def __init__(self, arg2: Vec2i) -> None: ...
    @overload
    def __init__(self, arg2: int, arg3: int) -> None: ...
    def AddAttachment(self, arg2: object, arg3: int, arg4: int, arg5: int) -> None: ...
    def Bind(self) -> None: ...
    def Unbind(self) -> None: ...
    def WriteToFile(self, attachment: object, filename: object, viewMatrix: Matrix4d = ..., projectionMatrix: Matrix4d = ...) -> bool: ...
    def __bool__(self) -> bool: ...
    def __eq__(self, other) -> bool: ...
    def __lt__(self, other) -> bool: ...
    def __ne__(self, other) -> bool: ...
    def __reduce__(self) -> Any: ...
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
    def __reduce__(self) -> Any: ...

class SimpleLight(Boost.Python.instance):
    __instance_size__: ClassVar[int] = ...
    ambient: type
    attenuation: type
    diffuse: type
    hasShadow: type
    id: Any
    isCameraSpaceLight: type
    isDomeLight: type
    position: type
    shadowBias: type
    shadowBlur: type
    shadowIndexEnd: type
    shadowIndexStart: type
    shadowMatrices: type
    shadowResolution: type
    specular: type
    spotCutoff: type
    spotDirection: type
    spotFalloff: type
    transform: type
    def __init__(self) -> None: ...
    def __reduce__(self) -> Any: ...

class SimpleMaterial(Boost.Python.instance):
    __instance_size__: ClassVar[int] = ...
    ambient: type
    diffuse: type
    emission: type
    shininess: type
    specular: type
    def __init__(self) -> None: ...
    def __reduce__(self) -> Any: ...

class Texture(Boost.Python.instance):
    memoryRequested: type
    def __init__(self, *args, **kwargs) -> None: ...
    @classmethod
    def GetTextureMemoryAllocated(cls) -> int: ...
    def __reduce__(self) -> Any: ...
    @property
    def magFilterSupported(self) -> type: ...
    @property
    def memoryUsed(self) -> type: ...
    @property
    def minFilterSupported(self) -> type: ...

def RegisterDefaultDebugOutputMessageCallback() -> None: ...