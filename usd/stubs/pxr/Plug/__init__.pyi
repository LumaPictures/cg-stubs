import Boost.Python
import pxr.Ar
import typing
from typing import Any, overload

class Notice(Boost.Python.instance):
    class Base(pxr.Tf.Notice):
        def __init__(self, *args, **kwargs) -> None: ...
        def __reduce__(self) -> Any: ...
    class DidRegisterPlugins(Notice.Base):
        def __init__(self, *args, **kwargs) -> None: ...
        def GetNewPlugins(self) -> list: ...
        def __reduce__(self) -> Any: ...
    def __init__(self, *args, **kwargs) -> None: ...
    def __reduce__(self) -> Any: ...

class Plugin(Boost.Python.instance):
    def __init__(self, *args, **kwargs) -> None: ...
    def DeclaresType(self, type: pxr.Tf.Type, includeSubclasses: bool = ...) -> bool: ...
    def FindPluginResource(self, path: str | pxr.Ar.ResolvedPath, verify: bool = ...) -> str: ...
    def GetMetadataForType(self, arg2: pxr.Tf.Type) -> dict: ...
    def Load(self) -> bool: ...
    def MakeResourcePath(self, arg2: str | pxr.Ar.ResolvedPath) -> str: ...
    def __bool__(self) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    def __lt__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    def __reduce__(self) -> Any: ...
    @property
    def expired(self) -> Any: ...
    @property
    def isLoaded(self) -> bool: ...
    @property
    def isPythonModule(self) -> bool: ...
    @property
    def isResource(self) -> bool: ...
    @property
    def metadata(self) -> JsObject: ...
    @property
    def name(self) -> str: ...
    @property
    def path(self) -> str: ...
    @property
    def resourcePath(self) -> str: ...

class Registry(Boost.Python.instance):
    def __init__(self) -> None: ...
    @classmethod
    def FindDerivedTypeByName(cls, arg1: pxr.Tf.Type, arg2: str | pxr.Ar.ResolvedPath) -> pxr.Tf.Type: ...
    @classmethod
    def FindTypeByName(cls, arg1: str | pxr.Ar.ResolvedPath) -> pxr.Tf.Type: ...
    @classmethod
    def GetAllDerivedTypes(cls, arg1: pxr.Tf.Type) -> tuple: ...
    def GetAllPlugins(self) -> list[Plugin]: ...
    @classmethod
    def GetDirectlyDerivedTypes(cls, arg1: pxr.Tf.Type) -> tuple: ...
    def GetPluginForType(self, arg2: pxr.Tf.Type) -> Plugin: ...
    def GetPluginWithName(self, arg2: str | pxr.Ar.ResolvedPath) -> Plugin: ...
    def GetStringFromPluginMetaData(self, arg2: pxr.Tf.Type, arg3: str | pxr.Ar.ResolvedPath) -> str: ...
    @overload
    def RegisterPlugins(self, arg2: str | pxr.Ar.ResolvedPath) -> list[Plugin]: ...
    @overload
    def RegisterPlugins(self, arg2: typing.Iterable[str | pxr.Ar.ResolvedPath]) -> list[Plugin]: ...
    def __bool__(self) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    def __lt__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    def __reduce__(self) -> Any: ...
    @property
    def expired(self) -> Any: ...

class _TestPlugBase1(Boost.Python.instance):
    @overload
    def __init__(self, arg2: str | pxr.Ar.ResolvedPath) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def GetTypeName(self) -> str: ...
    def __bool__(self) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    def __lt__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    def __reduce__(self) -> Any: ...
    @property
    def expired(self) -> Any: ...

class _TestPlugBase2(Boost.Python.instance):
    @overload
    def __init__(self, arg2: str | pxr.Ar.ResolvedPath) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def GetTypeName(self) -> str: ...
    def __bool__(self) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    def __lt__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    def __reduce__(self) -> Any: ...
    @property
    def expired(self) -> Any: ...

class _TestPlugBase3(Boost.Python.instance):
    @overload
    def __init__(self, arg2: str | pxr.Ar.ResolvedPath) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def GetTypeName(self) -> str: ...
    def __bool__(self) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    def __lt__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    def __reduce__(self) -> Any: ...
    @property
    def expired(self) -> Any: ...

class _TestPlugBase4(Boost.Python.instance):
    @overload
    def __init__(self, arg2: str | pxr.Ar.ResolvedPath) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def GetTypeName(self) -> str: ...
    def __bool__(self) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    def __lt__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    def __reduce__(self) -> Any: ...
    @property
    def expired(self) -> Any: ...

def _LoadPluginsConcurrently(predicate: object, numThreads: int = ..., verbose: bool = ...) -> None: ...