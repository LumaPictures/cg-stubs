# mypy: disable-error-code="misc, override, no-redef"

import Boost.Python
import pxr.Tf
import types
import typing
from _typeshed import Incomplete
from typing import Any, ClassVar, overload

__MFB_FULL_PACKAGE_NAME: str

class AssetInfo(Boost.Python.instance):
    __instance_size__: ClassVar[int] = ...
    assetName: Incomplete
    resolverInfo: Incomplete
    version: Incomplete
    def __init__(self) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...

class DefaultResolver(Resolver):
    def __init__(self, *args, **kwargs) -> None: ...
    @staticmethod
    def SetDefaultSearchPath(searchPath: typing.Iterable[str | ResolvedPath]) -> None: ...

class DefaultResolverContext(Boost.Python.instance):
    @overload
    def __init__(self, searchPaths: typing.Iterable[str | ResolvedPath]) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def GetSearchPath(self) -> list[str]: ...
    def __eq__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...

class Notice(Boost.Python.instance):
    class ResolverChanged(Notice.ResolverNotice):
        def __init__(self, *args, **kwargs) -> None: ...
        def AffectsContext(self, context: ResolverContext) -> bool: ...

    class ResolverNotice(pxr.Tf.Notice):
        def __init__(self, *args, **kwargs) -> None: ...
    def __init__(self, *args, **kwargs) -> None: ...

class ResolvedPath(Boost.Python.instance):
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self, arg2: object) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def GetPathString(self) -> str: ...
    def __bool__(self) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    def __ge__(self, other: object) -> bool: ...
    def __gt__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    def __le__(self, other: object) -> bool: ...
    def __lt__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...

class Resolver(Boost.Python.instance):
    def __init__(self, *args, **kwargs) -> None: ...
    def CanWriteAssetToPath(self, resolvedPath: ResolvedPath) -> _PyAnnotatedBoolResult: ...
    @overload
    def CreateContextFromString(self, uriScheme: str | ResolvedPath, contextStr: str | ResolvedPath) -> ResolverContext: ...
    @overload
    def CreateContextFromString(self, contextStr: str | ResolvedPath) -> ResolverContext: ...
    def CreateContextFromStrings(self, contextStrs: typing.Iterable[tuple[str | ResolvedPath, str | ResolvedPath]]) -> ResolverContext: ...
    def CreateDefaultContext(self) -> ResolverContext: ...
    def CreateDefaultContextForAsset(self, assetPath: str | ResolvedPath) -> ResolverContext: ...
    def CreateIdentifier(self, assetPath: str | ResolvedPath, anchorAssetPath: ResolvedPath = ...) -> str: ...
    def CreateIdentifierForNewAsset(self, assetPath: str | ResolvedPath, anchorAssetPath: ResolvedPath = ...) -> str: ...
    def GetAssetInfo(self, assetPath: str | ResolvedPath, resolvedPath: ResolvedPath) -> AssetInfo: ...
    def GetCurrentContext(self) -> ResolverContext: ...
    def GetExtension(self, assetPath: str | ResolvedPath) -> str: ...
    def GetModificationTimestamp(self, assetPath: str | ResolvedPath, resolvedPath: ResolvedPath) -> Timestamp: ...
    def IsContextDependentPath(self, assetPath: str | ResolvedPath) -> bool: ...
    def RefreshContext(self, arg2: ResolverContext) -> None: ...
    def Resolve(self, assetPath: str | ResolvedPath) -> ResolvedPath: ...
    def ResolveForNewAsset(self, assetPath: str | ResolvedPath) -> ResolvedPath: ...

class ResolverContext(Boost.Python.instance):
    @overload
    def __init__(self, arg2: object) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def Get(self) -> list: ...
    def GetDebugString(self) -> str: ...
    def IsEmpty(self) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    def __lt__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...

class ResolverContextBinder(Boost.Python.instance):
    __instance_size__: ClassVar[int] = ...
    def __init__(self, arg2: ResolverContext) -> None: ...
    def __enter__(self) -> None: ...
    def __exit__(self, type: type[BaseException] | None, value: BaseException | None, traceback: types.TracebackType | None) -> bool: ...

class ResolverScopedCache(Boost.Python.instance):
    __instance_size__: ClassVar[int] = ...
    def __init__(self) -> None: ...
    def __enter__(self) -> None: ...
    def __exit__(self, type: type[BaseException] | None, value: BaseException | None, traceback: types.TracebackType | None) -> bool: ...

class Timestamp(Boost.Python.instance):
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self, arg2: float) -> None: ...
    @overload
    def __init__(self, arg2: Timestamp) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def GetTime(self) -> float: ...
    def IsValid(self) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    def __ge__(self, other: object) -> bool: ...
    def __gt__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    def __le__(self, other: object) -> bool: ...
    def __lt__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...

class _PyAnnotatedBoolResult(Boost.Python.instance):
    __instance_size__: ClassVar[int] = ...
    def __init__(self, arg2: bool, arg3: object) -> None: ...
    def __bool__(self) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    def __getitem__(self, arg2: int) -> Any: ...
    def __iter__(self) -> typing.Iterator[Any]: ...
    def __ne__(self, other: object) -> bool: ...
    @property
    def whyNot(self): ...

def GetRegisteredURISchemes() -> list[str]: ...
def GetResolver() -> Resolver: ...
def GetUnderlyingResolver() -> Resolver: ...
def IsPackageRelativePath(path: str | ResolvedPath) -> bool: ...
@overload
def JoinPackageRelativePath(packagePath: str | ResolvedPath, packagedPath: str | ResolvedPath) -> str: ...
@overload
def JoinPackageRelativePath(paths: typing.Iterable[str | ResolvedPath]) -> str: ...
@overload
def JoinPackageRelativePath(paths: tuple[str | ResolvedPath, str | ResolvedPath]) -> str: ...
def SetPreferredResolver(resolverTypeName: str | ResolvedPath) -> None: ...
def SplitPackageRelativePathInner(path: str | ResolvedPath) -> tuple[str, str]: ...
def SplitPackageRelativePathOuter(path: str | ResolvedPath) -> tuple[str, str]: ...
def _TestImplicitConversion(arg1: ResolverContext) -> ResolverContext: ...
