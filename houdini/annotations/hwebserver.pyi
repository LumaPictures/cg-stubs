import asyncio
import threading
from collections.abc import Awaitable, Callable, Iterable, Mapping, MutableMapping, Sequence
from typing import Any, Concatenate, Never, TypeAlias, TypedDict, TypeVar, Unpack, overload

from _hwebserver import (
    PyServer,
    PyURLHandler,
    PyWebSocket,
    Request,
    Response,
    webServerSeverity,
    webServerVerbosity,
)
from _typeshed import SupportsRead
from _typeshed.wsgi import WSGIApplication
from houtypes import JSONLike

_SyncURLHandlerFunction: TypeAlias = Callable[[Request], Response]
_AsyncURLHandlerFunction: TypeAlias = Callable[[Request], Awaitable[Response | asyncio.Future[Response]]]
_URLHandlerFunctionT = TypeVar("_URLHandlerFunctionT", bound=_SyncURLHandlerFunction | _AsyncURLHandlerFunction)
# Called as function(request, *args, **kwargs) with the arguments of the API call.
_APIFunction: TypeAlias = Callable[Concatenate[Request, ...], object]
_APIFunctionT = TypeVar("_APIFunctionT", bound=_APIFunction)
_ArgTypes: TypeAlias = MutableMapping[str, Callable[[str], object]]
_Ports: TypeAlias = str | Sequence[str] | None
_ASGIReceiveEvent: TypeAlias = dict[str, str | bytes | int | None]
# Plain dicts, not TypedDicts, so that apps typed with Starlette's MutableMapping[str, Any]
# scopes and messages are accepted.
_ASGIScope: TypeAlias = dict[str, str | bytes | dict[str, str] | list[list[bytes]] | tuple[str, int]]
# What an app sends: type, status, headers, body, more_body, text, bytes, code, reason, ...
_ASGISendEvent: TypeAlias = Mapping[str, str | bytes | int | Iterable[Sequence[bytes]] | None]
_ASGIApplication: TypeAlias = Callable[
    [
        _ASGIScope,
        Callable[[], Awaitable[_ASGIReceiveEvent]],
        Callable[[_ASGISendEvent], Awaitable[None]],
    ],
    Awaitable[None],
]
_JSONT = TypeVar("_JSONT", bound=JSONLike)

class _PortSettings(TypedDict, total=False):
    CORS_ORIGIN_WHITELIST: Sequence[str]
    PORT: int
    MAX_PORT: int
    ALLOW_SYSTEM_PORT: bool
    ADDRESS: str
    IPV6: bool
    ALLOWED_HOSTS: Sequence[str]
    USE_X_FORWARDED_HOST: bool
    LOG_FILE: str
    MIN_LOG_SEVERITY: webServerSeverity
    SSL_CERTIFICATE: str
    SSL_CERTIFICATE_KEY: str
    SSL_DH_PARAMS: str
    SSL_VERIFY_PEER: bool
    SSL_REDIRECT: bool
    SSL_REDIRECT_HOST: str
    SSL_REDIRECT_EXEMPT: Sequence[str]
    SECURE_HSTS_SECONDS: int
    SECURE_HSTS_INCLUDE_SUBDOMAINS: bool
    SECURE_HSTS_PRELOAD: bool
    SECURE_CONTENT_TYPE_NOSNIFF: bool
    SECURE_REFFERER_POLICY: Sequence[str]
    SECURE_CROSS_ORIGIN_OPENER_POLICY: str

class _RunOptions(TypedDict, total=False):
    port: int
    debug: bool
    max_num_threads: int
    in_background: bool | None
    reload_source_changes: bool | None
    max_in_memory_file_upload_size: int | None
    max_request_size: int | None
    settings: str | _PortSettings | None
    verbosity: webServerVerbosity
    port_callback: Callable[[str, int], object] | None
    set_max_in_memory_file_upload_size: bool
    set_max_request_size: bool
    run_in_thread: bool

THREAD_SERVER: threading.local

def run(*args: int, **kwargs: Unpack[_RunOptions]) -> None: ...
def setSettingsForPort(settings: str | _PortSettings, port_name: str) -> None: ...

class Server(PyServer):
    def __init__(self, *args: Unpack[tuple[str]], **kwargs: Never) -> None: ...
    def urlHandler(
        self, path: str, is_prefix: bool = ..., ports: _Ports = ...
    ) -> Callable[[_URLHandlerFunctionT], _URLHandlerFunctionT]: ...
    @overload
    def apiFunction(
        self,
        namespace: _APIFunctionT,
        return_binary: bool = ...,
        arg_types: _ArgTypes | None = ...,
        ports: _Ports = ...,
    ) -> _APIFunctionT: ...
    @overload
    def apiFunction(
        self,
        namespace: str | None = ...,
        return_binary: bool = ...,
        arg_types: _ArgTypes | None = ...,
        ports: _Ports = ...,
    ) -> Callable[[_APIFunctionT], _APIFunctionT]: ...
    def apiFunction(
        self,
        namespace: str | _APIFunction | None = ...,
        return_binary: bool = ...,
        arg_types: _ArgTypes | None = ...,
        ports: _Ports = ...,
    ) -> Callable[..., object]: ...
    def registerAPIFunction(
        self,
        name: str,
        function: _APIFunction,
        return_binary: bool = ...,
        arg_types: _ArgTypes | None = ...,
        ports: _Ports = ...,
    ) -> None: ...
    def registerWSGIApp(self, application: WSGIApplication, path: str, ports: _Ports = ...) -> None: ...
    def registerASGIApp(self, application: _ASGIApplication, path: str, ports: Sequence[str] = ...) -> None: ...
    def webSocket(
        self, path: str, is_prefix: bool = ..., port_name: str = ...
    ) -> Callable[[type["WebSocket"]], None]: ...
    def setSettingsForPort(self, settings: str | _PortSettings, port_name: str) -> None: ...
    def run(self, *args: int, **kwargs: Unpack[_RunOptions]) -> None: ...

class WebSocket(PyWebSocket):
    def __init__(self, *args: Never, **kwargs: Never) -> None: ...

def webSocket(path: str, is_prefix: bool = ..., port_name: str = ...) -> Callable[[type[WebSocket]], None]: ...

class URLHandler(PyURLHandler):
    @overload
    def __init__(self, path: str, allows_partial: bool = ...) -> None: ...
    @overload
    def __init__(self, path: str, methods: Sequence[str], allows_partial: bool = ...) -> None: ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...

class AsyncURLHandler(PyURLHandler):
    @overload
    def __init__(self, path: str, allows_partial: bool = ...) -> None: ...
    @overload
    def __init__(self, path: str, methods: Sequence[str], allows_partial: bool = ...) -> None: ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...

class AsyncURLCallbackHandler(AsyncURLHandler):
    def __init__(self, path: str, function: _AsyncURLHandlerFunction, is_prefix: bool = ...) -> None: ...
    async def handle(self, request: Request) -> Response | None: ...

class URLCallbackHandler(URLHandler):
    def __init__(self, path: str, function: _SyncURLHandlerFunction, is_prefix: bool = ...) -> None: ...
    def handle(self, request: Request) -> Response: ...

def urlHandler(
    path: str, is_prefix: bool = ..., ports: _Ports = ...
) -> Callable[[_SyncURLHandlerFunction | _AsyncURLHandlerFunction], None]: ...
def errorResponse(
    request: Request, error_message: str | dict[str, _JSONT] | list[_JSONT], status: int, use_heading: bool = ...
) -> Response: ...
def notFoundResponse(request: Request) -> Response: ...
def redirect(request: Request, path: str, permanent: bool = ...) -> Response: ...
def fileResponse(
    file_path: str,
    content_type: str | None = ...,
    delete_file: bool = ...,
    download_as_filename: str | None = ...,
) -> Response: ...
@overload
def apiFunction(
    namespace: _APIFunction,
    return_binary: bool = ...,
    arg_types: _ArgTypes | None = ...,
    ports: _Ports = ...,
) -> None: ...
@overload
def apiFunction(
    namespace: str | None = ...,
    return_binary: bool = ...,
    arg_types: _ArgTypes | None = ...,
    ports: _Ports = ...,
) -> Callable[[_APIFunction], None]: ...
def apiFunction(
    namespace: str | _APIFunction | None = ...,
    return_binary: bool = ...,
    arg_types: _ArgTypes | None = ...,
    ports: _Ports = ...,
) -> Callable[[_APIFunction], None] | None: ...
def registerAPIFunction(
    name: str,
    function: _APIFunction,
    return_binary: bool = ...,
    arg_types: _ArgTypes | None = ...,
    ports: _Ports = ...,
) -> None: ...
@overload
def registerStaticFilesDirectory(directory: str) -> None: ...
@overload
def registerStaticFilesDirectory(
    directory: str, url_prefix: str = ..., port_name: str = ..., cache_control: str = ...
) -> None: ...
def registerStaticFilesDirectory(*args: str, **kwargs: str) -> None: ...
@overload
def registerArchiveFile(archive_file: str, url_prefix: str) -> None: ...
@overload
def registerArchiveFile(
    archive_file: str, url_prefix: str, port_name: str = ..., cache_control: str = ...
) -> None: ...
def registerArchiveFile(*args: str, **kwargs: str) -> None: ...
@overload
def setCORSWhitelist(whitelist: Sequence[str]) -> None: ...
@overload
def setCORSWhitelist(whitelist: Sequence[str], port_name: str = ...) -> None: ...
def setCORSWhitelist(*args: Any, **kwargs: Any) -> None: ...
@overload
def setPortInfo(
    port_name: str,
    port: int,
    up_to_port: int,
    use_free_port_on_failure: bool,
    address: str,
    use_v6: bool,
    allowed_hosts: Sequence[str],
    use_xforwarded: bool,
    /,
) -> None: ...
@overload
def setPortInfo(
    port_name: str,
    port: int,
    up_to_port: int,
    use_free_port_on_failure: bool,
    address: str,
    use_v6: bool,
    allowed_hosts: Sequence[str],
    use_xforwarded: bool,
) -> None: ...
def setPortInfo(*args: Any, **kwargs: Any) -> None: ...
@overload
def setLogInfo(log_file: str, min_severity: webServerSeverity) -> None: ...
@overload
def setLogInfo(log_file: str, min_severity: webServerSeverity, port_name: str = ...) -> None: ...
def setLogInfo(*args: Any, **kwargs: Any) -> None: ...
@overload
def setSSL(port_name: str, certificate: str, certificate_key: str, dh_param: str, verify_peer: bool, /) -> None: ...
@overload
def setSSL(port_name: str, certificate: str, certificate_key: str, dh_param: str, verify_peer: bool) -> None: ...
def setSSL(*args: Any, **kwargs: Any) -> None: ...
@overload
def setSecurity(
    port_name: str,
    redirect: bool,
    redirect_exempt: Sequence[str],
    redirect_host: str,
    sts_seconds: int,
    sts_include_subdomains: bool,
    sts_preload: bool,
    no_sniff: bool,
    referrer_policy: Sequence[str],
    cross_origin_opener_policy: str,
    /,
) -> None: ...
@overload
def setSecurity(
    port_name: str,
    redirect: bool,
    redirect_exempt: Sequence[str],
    redirect_host: str,
    sts_seconds: int,
    sts_include_subdomains: bool,
    sts_preload: bool,
    no_sniff: bool,
    referrer_policy: Sequence[str],
    cross_origin_opener_policy: str,
) -> None: ...
def setSecurity(*args: Any, **kwargs: Any) -> None: ...
@overload
def findHandlerForPort(method: str, path: str) -> PyURLHandler | None: ...
@overload
def findHandlerForPort(method: str, path: str, port_name: str = ...) -> PyURLHandler | None: ...
def findHandlerForPort(*args: str, **kwargs: str) -> PyURLHandler | None: ...
@overload
def insertHandlerForPort(handler: PyURLHandler) -> None: ...
@overload
def insertHandlerForPort(handler: PyURLHandler, port_name: str = ...) -> None: ...
def insertHandlerForPort(*args: Any, **kwargs: Any) -> None: ...
@overload
def insertWebSocketForPort(creator: Callable[[], WebSocket], path: str) -> None: ...
@overload
def insertWebSocketForPort(
    creator: Callable[[], WebSocket], path: str, is_prefix: bool = ..., port_name: str = ...
) -> None: ...
def insertWebSocketForPort(*args: Any, **kwargs: Any) -> None: ...
def isInDebugMode() -> bool: ...
def requestShutdown() -> None: ...

class APIUrlHandler(URLHandler):
    def __init__(self) -> None: ...
    def insertFunction(self, name: str, function: _APIFunction) -> None: ...

class FileWrapper:
    filelike: SupportsRead[bytes]
    blksize: int
    close: Callable[[], object]
    def __init__(self, filelike: SupportsRead[bytes], bulksize: int = ...) -> None: ...
    def __getitem__(self, key: int) -> bytes: ...

def registerWSGIApp(application: WSGIApplication, path: str, ports: _Ports = ...) -> None: ...

class ASGIHTTPRequest:
    request: Request
    scope: _ASGIScope
    def __init__(self, request: Request) -> None: ...
    async def receive(self) -> _ASGIReceiveEvent: ...
    async def send(self, event: _ASGISendEvent) -> None: ...

class ASGIWebSocket(WebSocket):
    queue: asyncio.Queue[_ASGIReceiveEvent] | None
    application: _ASGIApplication
    app_task: asyncio.Task[None] | None
    scope: _ASGIScope
    def __init__(self, application: _ASGIApplication) -> None: ...
    async def connect(self, req: Request) -> None: ...
    def on_task_complete(self, task: asyncio.Task[None]) -> None: ...
    async def run_asgi(self) -> None: ...
    async def asgi_send(self, event: _ASGISendEvent) -> None: ...
    async def asgi_receive(self) -> _ASGIReceiveEvent: ...
    async def receive(self, text_data: str | None, bytes_data: bytes | None) -> None: ...
    async def disconnect(self, code: int) -> None: ...

class ASGIHandler(AsyncURLHandler):
    application: _ASGIApplication | None
    @overload
    def __init__(self, path: str, allows_partial: bool = ...) -> None: ...
    @overload
    def __init__(self, path: str, methods: Sequence[str], allows_partial: bool = ...) -> None: ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    async def handle(self, request: Request) -> None: ...

def registerASGIApp(application: _ASGIApplication, path: str, ports: Sequence[str] = ...) -> None: ...
