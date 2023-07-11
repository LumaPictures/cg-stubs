# mypy: disable-error-code="misc, override, no-redef"

import Boost.Python
import pxr.Sdf
import pxr.Tf
import pxr.Usd
import typing
from typing import Any, ClassVar, overload

__MFB_FULL_PACKAGE_NAME: str

class GenerativeProceduralAPI(pxr.Usd.APISchemaBase):
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @classmethod
    def Apply(cls, prim: pxr.Usd.Prim) -> GenerativeProceduralAPI: ...
    @classmethod
    def CanApply(cls, prim: pxr.Usd.Prim) -> _CanApplyResult: ...
    def CreateProceduralSystemAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateProceduralTypeAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    @classmethod
    def Get(cls, stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> GenerativeProceduralAPI: ...
    def GetProceduralSystemAttr(self) -> pxr.Usd.Attribute: ...
    def GetProceduralTypeAttr(self) -> pxr.Usd.Attribute: ...
    @classmethod
    def GetSchemaAttributeNames(cls, includeInherited: bool = ...) -> list[str]: ...
    @classmethod
    def _GetStaticTfType(cls) -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...

class Tokens(Boost.Python.instance):
    HwPrimvar_1: ClassVar[str] = ...  # read-only
    HwPtexTexture_1: ClassVar[str] = ...  # read-only
    HwUvTexture_1: ClassVar[str] = ...  # read-only
    HydraGenerativeProceduralAPI: ClassVar[str] = ...  # read-only
    black: ClassVar[str] = ...  # read-only
    clamp: ClassVar[str] = ...  # read-only
    displayLookBxdf: ClassVar[str] = ...  # read-only
    faceIndex: ClassVar[str] = ...  # read-only
    faceOffset: ClassVar[str] = ...  # read-only
    frame: ClassVar[str] = ...  # read-only
    hydraGenerativeProcedural: ClassVar[str] = ...  # read-only
    infoFilename: ClassVar[str] = ...  # read-only
    infoVarname: ClassVar[str] = ...  # read-only
    linear: ClassVar[str] = ...  # read-only
    linearMipmapLinear: ClassVar[str] = ...  # read-only
    linearMipmapNearest: ClassVar[str] = ...  # read-only
    magFilter: ClassVar[str] = ...  # read-only
    minFilter: ClassVar[str] = ...  # read-only
    mirror: ClassVar[str] = ...  # read-only
    nearest: ClassVar[str] = ...  # read-only
    nearestMipmapLinear: ClassVar[str] = ...  # read-only
    nearestMipmapNearest: ClassVar[str] = ...  # read-only
    primvarsHdGpProceduralType: ClassVar[str] = ...  # read-only
    proceduralSystem: ClassVar[str] = ...  # read-only
    repeat: ClassVar[str] = ...  # read-only
    textureMemory: ClassVar[str] = ...  # read-only
    useMetadata: ClassVar[str] = ...  # read-only
    uv: ClassVar[str] = ...  # read-only
    wrapS: ClassVar[str] = ...  # read-only
    wrapT: ClassVar[str] = ...  # read-only
    def __init__(self, *args, **kwargs) -> None: ...

class _CanApplyResult(Boost.Python.instance):
    __instance_size__: ClassVar[int] = ...
    def __init__(self, arg2: bool, arg3: object) -> None: ...
    def __bool__(self) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    def __getitem__(self, arg2: int) -> Any: ...
    def __iter__(self) -> typing.Iterator[Any]: ...
    def __ne__(self, other: object) -> bool: ...
    @property
    def whyNot(self) -> Any: ...
