import pathlib
from collections.abc import Iterator, Mapping
from importlib.resources.abc import Traversable
from typing import IO, Any, TypeAlias

from hutil.help.config import Config
from hutil.help.paths import WikiPath

DOC_KEY: str
EXTRA_DOC_KEY: str
MOUNTS_KEY: str

_StoreObj: TypeAlias = "str | pathlib.Path | Store | dict[str, Any] | list[_StoreObj] | tuple[_StoreObj, ...] | Config"

def store_from_obj(obj: _StoreObj) -> Store: ...

class Store:
    def open_text(self, path: WikiPath, encoding: str = ...) -> IO[str]: ...
    def mkdir(self, path: WikiPath, name: str, parents: bool = ..., exist_ok: bool = ...) -> None: ...
    def all_paths(self, start: str | WikiPath = ...) -> Iterator[WikiPath]: ...

class FileStore(Store):
    dirpath: pathlib.Path
    def __repr__(self) -> str: ...

class ZipStore(Store):
    zip_path: pathlib.Path

class MountStore(WrappingStore):
    prefix_path: WikiPath

class PackageStore(Store):
    files: Traversable

class DictStore(Store):
    def __init__(self, namespace: Mapping[str, str] | Mapping[WikiPath, str] | Mapping[str | WikiPath, str] | None = ...) -> None: ...
