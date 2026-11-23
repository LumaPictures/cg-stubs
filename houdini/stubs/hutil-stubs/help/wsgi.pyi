import dataclasses
from . import util as util
from .config import Config as Config, Plugin as Plugin, endpoint as endpoint
from .paths import WikiPath as WikiPath
from .stores import Store as Store
from .zones import Zone as Zone
from _typeshed.wsgi import StartResponse, WSGIApplication as WSGIApplication, WSGIEnvironment as WSGIEnvironment
from collections.abc import Iterable, Mapping
from datetime import datetime
from houtypes import JSONLike, JSONValue
from typing import Callable as Callable, Sequence
from werkzeug.routing import Map, Rule as Rule
from werkzeug.wrappers import Request, Response

class WsgiApp:
    config: Config
    url_map: Map
    static_map: dict[str, str] | None
    def __init__(self, config: Config) -> None: ...
    def zone(self) -> Zone: ...
    def __call__(self, environ: WSGIEnvironment, start_response: StartResponse) -> Iterable[bytes]: ...
    def find_server_plugin(self, name: str | None) -> Plugin: ...
    def start_server(self, name: str | None = 'werkzeug', address: str = '127.0.0.1', port: str | int = 9000, workers: int = 4, debug: bool = False, reload: bool = False, port_callback: Callable[[], int] | None = None) -> None: ...

def static_map_from_config(config: Config) -> dict[str, str] | None: ...

class ServerPlugin(Plugin):
    def provides_server(self) -> bool: ...

class WerkzeugServer(ServerPlugin):
    name: str
    def start_server(self, app: WSGIApplication, address: str, port: str | int, workers: int, debug: bool, reload: bool, static_map: dict[str, str] | None = None, port_callback: Callable[[], int] | None = None) -> None: ...

class WaitressServer(ServerPlugin):
    name: str
    def start_server(self, app: WSGIApplication, address: str, port: str | int, workers: int, debug: bool, reload: bool, static_map: dict[str, str] | None = None, port_callback: Callable[[], int] | None = None) -> None: ...

class HWebServer(ServerPlugin):
    name: str
    def start_server(self, app: WSGIApplication, address: str, port: str | int, workers: int, debug: bool, reload: bool, static_map: dict[str, str] | None = None, port_callback: Callable[[], int] | None = None) -> None: ...

def make_urlmap(plugins: Sequence[Plugin]) -> Map: ...
def session_from_request(request: Request) -> dict[str, JSONValue]: ...
def decode_session(session_bytes: str | bytes) -> dict[str, JSONValue]: ...
def encode_session(session: Mapping[str, JSONLike]) -> bytes: ...
def serve_file(store: Store, path: WikiPath) -> Response: ...

@dataclasses.dataclass
class DirectoryEntry:
    path: WikiPath
    link: WikiPath
    name: str
    is_dir: bool
    size: int
    last_modified: datetime | None

def directory_list(zone: Zone, dirpath: WikiPath) -> Sequence[DirectoryEntry]: ...
def directory_response(zone: Zone, dirpath: WikiPath) -> Response:
    """
    Renders a simple template to show the files in a directory.
    """

class BaseUrls(Plugin):
    def hello(self, request: Request) -> str: ...
    def wiki_preview(self, request: Request, pathstr: str = '') -> Response: ...
    def indexed(self, request: Request, pth: str = '') -> Response: ...
    def show(self, request: Request, pathstr: str = '') -> Response: ...
