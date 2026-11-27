import os
import pathlib
from collections.abc import Callable, Iterable, Iterator, Mapping, Sequence
from typing import Any, TypeVar, overload

from _typeshed.wsgi import WSGIApplication
from werkzeug.routing import Rule

from . import stores
from .processing import Processor
from .search.indexing import Document
from .zones import Zone

_F = TypeVar("_F", bound=Callable[..., Any])

class Config(dict[str, Any]):
    def __init__(
        self,
        *args: Mapping[str, object] | Iterable[tuple[str, object]],
        store: stores._StoreObj | None = ...,
        db_path: str | os.PathLike[str] | None = ...,
        **kwargs: object,
    ) -> None: ...
    def plugins(self) -> Sequence[Plugin]: ...
    def pre_processor(self) -> Processor: ...
    def post_processor(self) -> Processor: ...
    def from_envvar(self, variable_name: str, silent: bool = ...) -> bool: ...
    def from_prefixed_env(self, prefix: str = ..., *, loads: Callable[[str], object] = ...) -> bool: ...
    def from_pyfile(self, path: str | os.PathLike[str], silent: bool = ...) -> bool: ...
    def from_object(self, obj: object) -> None: ...
    def from_file(
        self, path: str | os.PathLike[str], load: Callable[[str], Mapping[str, object]], silent: bool = ...
    ) -> bool: ...
    def from_mapping(self, mapping: Mapping[str, object] | None = ..., **kwargs: object) -> bool: ...
    def get_plugin(self, name: str) -> Plugin | None: ...
    # Forwards to wsgi.WsgiApp.start_server(); an address given positionally comes after the name.
    @overload
    def start_server(
        self,
        name: str | None = ...,
        *,
        address: str = ...,
        port: str | int = ...,
        workers: int = ...,
        debug: bool = ...,
        reload: bool = ...,
        port_callback: Callable[[], int] | None = ...,
    ) -> None: ...
    @overload
    def start_server(
        self,
        name: str | None,
        address: str,
        /,
        port: str | int = ...,
        workers: int = ...,
        debug: bool = ...,
        reload: bool = ...,
        port_callback: Callable[[], int] | None = ...,
    ) -> None: ...
    def start_server(self, name: str | None = ..., *args: Any, **kwargs: Any) -> None: ...

class Plugin:
    name: str
    def __init__(self, config: Config) -> None: ...
    def config(self) -> Config: ...
    def static_map(self) -> dict[str, str] | None: ...
    def start_server(
        self,
        app: WSGIApplication,
        address: str,
        port: str | int,
        workers: int,
        debug: bool,
        reload: bool,
        static_map: dict[str, str] | None = ...,
        port_callback: Callable[[], int] | None = ...,
    ) -> None: ...
    def routing_rules(self) -> Iterator[Rule]: ...
    def process_searchable(self, zone: Zone, fields: Document) -> None: ...

def make_plugin(config: Config, obj: Plugin | str | dict[str, Any]) -> Plugin: ...
def endpoint(
    *points: str, methods: Sequence[str] = ..., alias: str | None = ...
) -> Callable[[_F], _F]: ...
def standard_plugins(config: Config) -> list[Plugin]: ...
def get_default_config() -> Config: ...
