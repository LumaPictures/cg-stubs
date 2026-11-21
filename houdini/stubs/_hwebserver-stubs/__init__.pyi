from collections.abc import Sequence
from typing import Never
import _hwebserver
import asyncio
from collections.abc import Callable
from typing import ClassVar
from typing import Any, Callable, ClassVar, overload

AbortSeverity: webServerSeverity
FatalSeverity: webServerSeverity
High: webServerVerbosity
Low: webServerVerbosity
Medium: webServerVerbosity
MessageSeverity: webServerSeverity
PromptSeverity: webServerSeverity
WarningSeverity: webServerSeverity
__version__: str

class APIError(Exception): ...

class DisallowedHost(Exception): ...

class HTTPStatus:
    __members__: ClassVar[dict[str, HTTPStatus]] = ...  # read-only
    Accepted: ClassVar[HTTPStatus] = ...
    BadGateway: ClassVar[HTTPStatus] = ...
    BadRequest: ClassVar[HTTPStatus] = ...
    Conflict: ClassVar[HTTPStatus] = ...
    Continue: ClassVar[HTTPStatus] = ...
    Created: ClassVar[HTTPStatus] = ...
    ExpectationFailed: ClassVar[HTTPStatus] = ...
    Forbidden: ClassVar[HTTPStatus] = ...
    Found: ClassVar[HTTPStatus] = ...
    GatewayTimeout: ClassVar[HTTPStatus] = ...
    Gone: ClassVar[HTTPStatus] = ...
    HeaderFieldsTooLarge: ClassVar[HTTPStatus] = ...
    InternalServerError: ClassVar[HTTPStatus] = ...
    LegalReasons: ClassVar[HTTPStatus] = ...
    LengthRequired: ClassVar[HTTPStatus] = ...
    MethodNotAllowed: ClassVar[HTTPStatus] = ...
    MovedPermanently: ClassVar[HTTPStatus] = ...
    MultipleChoice: ClassVar[HTTPStatus] = ...
    NetworkAuthRequired: ClassVar[HTTPStatus] = ...
    NoContent: ClassVar[HTTPStatus] = ...
    NonAuthoritativeInfo: ClassVar[HTTPStatus] = ...
    NotAcceptable: ClassVar[HTTPStatus] = ...
    NotFound: ClassVar[HTTPStatus] = ...
    NotImplemented: ClassVar[HTTPStatus] = ...
    NotModified: ClassVar[HTTPStatus] = ...
    Null: ClassVar[HTTPStatus] = ...
    Ok: ClassVar[HTTPStatus] = ...
    PartitionContent: ClassVar[HTTPStatus] = ...
    PayloadLarge: ClassVar[HTTPStatus] = ...
    PaymentRequired: ClassVar[HTTPStatus] = ...
    PermRedirect: ClassVar[HTTPStatus] = ...
    PreconditionFailed: ClassVar[HTTPStatus] = ...
    PreconditionRequired: ClassVar[HTTPStatus] = ...
    ProxyAuthRequired: ClassVar[HTTPStatus] = ...
    RangeNotSatisfiable: ClassVar[HTTPStatus] = ...
    RequestTimeout: ClassVar[HTTPStatus] = ...
    ResetContent: ClassVar[HTTPStatus] = ...
    SeeOther: ClassVar[HTTPStatus] = ...
    ServiceUnavailable: ClassVar[HTTPStatus] = ...
    SwitchProtocol: ClassVar[HTTPStatus] = ...
    TempRedirect: ClassVar[HTTPStatus] = ...
    TooEarly: ClassVar[HTTPStatus] = ...
    TooManyRequests: ClassVar[HTTPStatus] = ...
    URITooLong: ClassVar[HTTPStatus] = ...
    Unauthorized: ClassVar[HTTPStatus] = ...
    UnprocessableEntity: ClassVar[HTTPStatus] = ...
    UnsupportedMedia: ClassVar[HTTPStatus] = ...
    UpgradeRequired: ClassVar[HTTPStatus] = ...
    VersionNotSupported: ClassVar[HTTPStatus] = ...
    __entries: ClassVar[dict[str, tuple[HTTPStatus, str | None]]] = ...
    def __init__(self, value: int) -> None:
        """__init__(self: _hwebserver.HTTPStatus, value: int) -> None"""
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object) -> bool"""
    def __hash__(self) -> int:
        """__hash__(self: object) -> int"""
    def __index__(self) -> int:
        """__index__(self: _hwebserver.HTTPStatus) -> int"""
    def __int__(self) -> int:
        """__int__(self: _hwebserver.HTTPStatus) -> int"""
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object) -> bool"""
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class OperationFailed(Exception): ...

class PyServer:
    def __init__(self, arg0: str) -> None:
        """__init__(self: _hwebserver.PyServer, arg0: str) -> None"""
    def findHandlerForPort(self, method: str, path: str, port_name: str = ...) -> PyURLHandler | None:
        """findHandlerForPort(self: _hwebserver.PyServer, method: str, path: str, port_name: str = '') -> _hwebserver.PyURLHandler"""
    def insertHandlerForPort(self, handler: PyURLHandler, port_name: str = ...) -> None:
        """insertHandlerForPort(self: _hwebserver.PyServer, handler: _hwebserver.PyURLHandler, port_name: str = '') -> None"""
    def insertWebSocketForPort(self, creator: Callable[[], PyWebSocket], path: str, is_prefix: bool = ..., port_name: str = ...) -> None:
        """insertWebSocketForPort(self: _hwebserver.PyServer, creator: Callable, path: str, is_prefix: bool = False, port_name: str = '') -> None"""
    def isInDebugMode(self) -> bool:
        """isInDebugMode(self: _hwebserver.PyServer) -> bool"""
    def name(self) -> str:
        """name(self: _hwebserver.PyServer) -> str"""
    def registerArchiveFile(self, archive_file: str, url_prefix: str, port_name: str = ..., cache_control: str = ...) -> None:
        """registerArchiveFile(self: _hwebserver.PyServer, archive_file: str, url_prefix: str, port_name: str = '', *, cache_control: str = '') -> None"""
    def registerStaticFilesDirectory(self, directory: str, url_prefix: str = ..., port_name: str = ..., cache_control: str = ...) -> None:
        """registerStaticFilesDirectory(self: _hwebserver.PyServer, directory: str, url_prefix: str = '/static', port_name: str = '', *, cache_control: str = '') -> None"""
    def requestShutdown(self) -> None:
        """requestShutdown(self: _hwebserver.PyServer) -> None"""
    def runServer(self, port: int = ..., debug: bool = ..., max_num_threads: int = ..., set_max_in_memory_file_upload_size: bool = ..., max_in_memory_file_upload_size: int = ..., set_max_request_size: bool = ..., max_request_size: int = ..., verbosity: webServerVerbosity = ..., port_callback: Callable[[str, int], object] | None = ..., run_in_thread: bool = ...) -> None:
        """runServer(self: _hwebserver.PyServer, port: int = -1, debug: bool = False, max_num_threads: int = 4, set_max_in_memory_file_upload_size: bool = False, max_in_memory_file_upload_size: int = 0, set_max_request_size: bool = False, max_request_size: int = 0, verbosity: _hwebserver.webServerVerbosity = <webServerVerbosity.Low: 0>, port_callback: object = None, run_in_thread: bool = False) -> None"""
    def setCORSWhitelist(self, whitelist: Sequence[str], port_name: str = ...) -> None:
        """setCORSWhitelist(self: _hwebserver.PyServer, whitelist: UT_Array[str], port_name: str = '') -> None"""
    def setLogInfo(self, log_file: str, min_severity: webServerSeverity, port_name: str = ...) -> None:
        """setLogInfo(self: _hwebserver.PyServer, log_file: str, min_severity: _hwebserver.webServerSeverity, port_name: str = '') -> None"""
    def setPortInfo(self, port_name: str, port: int, up_to_port: int, use_free_port_on_failure: bool, address: str, use_v6: bool, allowed_hosts: Sequence[str], use_xforwarded: bool) -> None:
        """setPortInfo(self: _hwebserver.PyServer, port_name: str, port: int, up_to_port: int, use_free_port_on_failure: bool, address: str, use_v6: bool, allowed_hosts: UT_Array[str], use_xforwarded: bool) -> None"""
    def setSSL(self, port_name: str, certificate: str, certificate_key: str, dh_param: str, verify_peer: bool) -> None:
        """setSSL(self: _hwebserver.PyServer, port_name: str, certificate: str, certificate_key: str, dh_param: str, verify_peer: bool) -> None"""
    def setSecurity(self, port_name: str, redirect: bool, redirect_exempt: Sequence[str], redirect_host: str, sts_seconds: int, sts_include_subdomains: bool, sts_preload: bool, no_sniff: bool, referrer_policy: Sequence[str], cross_origin_opener_policy: str) -> None:
        """setSecurity(self: _hwebserver.PyServer, port_name: str, redirect: bool, redirect_exempt: UT_Array[str], redirect_host: str, sts_seconds: int, sts_include_subdomains: bool, sts_preload: bool, no_sniff: bool, referrer_policy: UT_Array[str], cross_origin_opener_policy: str) -> None"""

class PyURLHandler:
    @overload
    def __init__(self, path: str, allows_partial: bool = ...) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: _hwebserver.PyURLHandler, path: str, allows_partial: bool = False) -> None

        2. __init__(self: _hwebserver.PyURLHandler, path: str, methods: UT_Array[str], allows_partial: bool = False) -> None
        """
    @overload
    def __init__(self, path: str, methods: Sequence[str], allows_partial: bool = ...) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: _hwebserver.PyURLHandler, path: str, allows_partial: bool = False) -> None

        2. __init__(self: _hwebserver.PyURLHandler, path: str, methods: UT_Array[str], allows_partial: bool = False) -> None
        """
    @property
    def methods(self) -> list[str]: ...
    @property
    def path(self) -> str: ...

class PyWebSocket:
    def __init__(self) -> None:
        """__init__(self: _hwebserver.PyWebSocket) -> None"""
    def accept(self) -> asyncio.Future[None]:
        """accept(self: _hwebserver.PyWebSocket) -> object"""
    def close(self, code: int = ...) -> asyncio.Future[None]:
        """close(self: _hwebserver.PyWebSocket, code: int = 1000) -> object"""
    def send(self, message: str | bytes, is_binary: bool = ...) -> asyncio.Future[None]:
        """send(self: _hwebserver.PyWebSocket, message: str, is_binary: bool = False) -> object"""

class Request:
    def __init__(self, *, no_constructor: Never) -> None: ...
    def GET(self) -> dict[str, str]:
        """GET(self: _hwebserver.Request) -> dict[str, str]

        Returns a dictionary of the parsed query string variables provided
        in the URL of the request.

        Calling this method generates a new copy of the dictionary each
        time, so you are advised to avoid calling it more times than
        necessary.

        If you need to support multiple GET values with the same key, you
        can use Python's parse_qs function to parse the query string and
        extract them.

        > try:
        >     from urllib.parse import parse_qs
        > except Importerror:
        >     from urlparse import parse_qs
        > 
        > `parse_qs(request.queryString())`

        """
    def POST(self) -> dict[str, str]:
        """POST(self: _hwebserver.Request) -> dict[str, str]

        Returns a dictionary of the parsed query variables provided in the
        body of the request. The server can receive URL-encoded and
        multipart/form-data encoded values.

        Calling this method generates a new copy of the dictionary each
        time, so you are advised to avoid calling it more times than
        necessary.

        Note that files in multipart/form-data do not show up in this
        dictionary, are are instead accessible via files.

        """
    def absoluteURI(self, location: str) -> str:
        """absoluteURI(self: _hwebserver.Request, location: str) -> str

        If location is None, returns the full URI used to make the current
        request. Otherwise, location is a string containing a path on the
        server, and returns a full URI to that path.

        This method is used to build Location headers for .

        """
    def body(self) -> bytes:
        """body(self: _hwebserver.Request) -> bytes

        Returns the fully unparsed body of the request.

        Calling this method generates a new copy of the string each time, so
        you are advised to avoid calling it more times than necessary.

        """
    def clientAddress(self) -> tuple[str, int]:
        """clientAddress(self: _hwebserver.Request) -> tuple"""
    def contentLength(self) -> str:
        """contentLength(self: _hwebserver.Request) -> str

        Returns the content length header. If none is present an empty
        string is returned. This is meant as a convenience method to going
        through the headers directly.

        """
    def contentType(self) -> str:
        """contentType(self: _hwebserver.Request) -> str

        Returns the content type header. If none is present an empty string
        is returned. This is meant as a convenience method to going through
        the headers directly.

        """
    def cookies(self) -> dict[str, str]:
        """cookies(self: _hwebserver.Request) -> dict[str, str]

        Returns the parsed cookie data from the Cookie header sent in the
        request.

        Calling this method generates a new copy of the dictionary each
        time, so you are advised to avoid calling it more times than
        necessary.

        """
    def files(self) -> dict[str, UploadedFile]:
        """files(self: _hwebserver.Request) -> dict

        Returns a dictionary of the file uploads passed in multipart/form-
        data. If these file uploads were large they may have been saved to
        disk instead of being stored in memory. See for more information.

        Calling this method generates a new copy of the dictionary each
        time, so you are advised to avoid calling it more times than
        necessary.

        """
    def headers(self) -> dict[str, str]:
        """headers(self: _hwebserver.Request) -> dict[str, str]

        Returns a dictionary of the headers provided with the request.

        Calling this method generates a new copy of the dictionary each
        time, so you are advised to avoid calling it more times than
        necessary.

        Note that cookies will parse the contents of the Cookie header.

        The web server does not provide support for authentication, but you
        could add it, for example, by creating decorators that inspect the
        contents of the Authorization header.

        """
    def host(self) -> str:
        """host(self: _hwebserver.Request) -> str

        Returns the host found in the request host header. If none is found
        then an empty string is returned.

        """
    def isInDebugMode(self) -> bool:
        """isInDebugMode(self: _hwebserver.Request) -> bool"""
    def isSecure(self) -> bool:
        """isSecure(self: _hwebserver.Request) -> bool

        Returns True if the request was made using https instead of just
        http.

        """
    def method(self) -> str:
        '''method(self: _hwebserver.Request) -> str

        Returns the HTTP method used in the request, such as \\\\\\"GET\\\\\\", \\\\\\"POST\\\\\\",
        \\\\\\"PATCH\\\\\\", etc.

        '''
    def path(self) -> str:
        '''path(self: _hwebserver.Request) -> str

        Returns the path that was requested on the server. For example, if
        the URI is \\\\\\"http://127.0.0.1:8008/asset/torus?divisions=20&tx=2\\\\\\",
        the path would be \\\\\\"/asset/torus\\\\\\".

        '''
    def pathWithQueryString(self) -> str:
        '''pathWithQueryString(self: _hwebserver.Request) -> str

        Returns the path that was requested on the server, including the
        query string part. For example, if the URI is
        \\\\\\"http://127.0.0.1:8008/asset/torus?divisions=20&tx=2\\\\\\", the result
        would be \\\\\\"/asset/torus?divisions=20&tx=2\\\\\\".

        Note that the contents of the query string in this example are also
        accessible via request.GET()[\\\\\\"divisions\\\\\\"] and request.GET()[\\\\\\"tx\\\\\\"].

        '''
    def port(self) -> int:
        """port(self: _hwebserver.Request) -> int

        Returns the server port the request came from.

        """
    def portName(self) -> str:
        """portName(self: _hwebserver.Request) -> str"""
    def protocol(self) -> str:
        """protocol(self: _hwebserver.Request) -> str

        Returns the protocol used for the request. An example would be
        HTTP/1.1 for an http 1.1 request.

        """
    def queryString(self) -> str:
        '''queryString(self: _hwebserver.Request) -> str

        Returns the query string in the request, not including the leading
        ?. For example, if the URI is
        \\\\\\"http://127.0.0.1:8008/asset/torus?divisions=20&tx=2\\\\\\", the result
        would be \\\\\\"divisions=20&tx=2\\\\\\". If the URI is
        \\\\\\"http://127.0.0.1:8008/asset/torus\\\\\\" the result would be \\\\\\"\\\\\\".

        '''
    def requestServerShutdown(self) -> bool:
        """requestServerShutdown(self: _hwebserver.Request) -> bool"""
    def scheme(self) -> str:
        """scheme(self: _hwebserver.Request) -> str"""
    def send(self, response: Response) -> None:
        """send(self: _hwebserver.Request, response: HWEB_WebServerResponse) -> None"""
    def sendBody(self, body: str | bytes, more_body: bool) -> asyncio.Future[None]:
        """sendBody(self: _hwebserver.Request, body: str, more_body: bool) -> object"""
    def sendHeaders(self, status: int, headers: dict[str, str]) -> asyncio.Future[None]:
        """sendHeaders(self: _hwebserver.Request, status: int, headers: dict[str, str]) -> object"""
    def serverAddress(self) -> tuple[str, int]:
        """serverAddress(self: _hwebserver.Request) -> tuple"""
    def socketFD(self) -> int:
        """socketFD(self: _hwebserver.Request) -> int"""

class Response:
    @overload
    def __init__(self, data: str, status: int = ..., content_type: str = ..., is_file_name: bool = ..., delete_file: bool = ...) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: _hwebserver.Response, data: str, status: int = 200, content_type: str = 'text/html', is_file_name: bool = False, delete_file: bool = False) -> None

        2. __init__(self: _hwebserver.Response, data: bytes, status: int = 200, content_type: str = 'text/html', is_file_name: bool = False, delete_file: bool = False) -> None
        """
    @overload
    def __init__(self, data: bytes, status: int = ..., content_type: str = ..., is_file_name: bool = ..., delete_file: bool = ...) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: _hwebserver.Response, data: str, status: int = 200, content_type: str = 'text/html', is_file_name: bool = False, delete_file: bool = False) -> None

        2. __init__(self: _hwebserver.Response, data: bytes, status: int = 200, content_type: str = 'text/html', is_file_name: bool = False, delete_file: bool = False) -> None
        """
    def body(self) -> str:
        """body(self: _hwebserver.Response) -> str

        Returns the body of the response.

        Calling this method generates a new copy of the string each time, so
        you are advised to avoid calling it more times than necessary.

        """
    def contentLength(self) -> int:
        """contentLength(self: _hwebserver.Response) -> int

        Returns the current content length of the response.

        """
    def headers(self) -> dict[str, str]:
        """headers(self: _hwebserver.Response) -> dict[str, str]

        Returns a dictionary of all headers in the response.

        Calling this method generates a new copy of the dictionary each
        time, so you are advised to avoid calling it more times than
        necessary.

        """
    def isChunked(self) -> bool:
        """isChunked(self: _hwebserver.Response) -> bool

        Returns True if the response is a chunked response.

        """
    def setBody(self, body: str | bytes, content_type: str = ...) -> None:
        """setBody(self: _hwebserver.Response, body: str, content_type: str = '') -> None

        In some cases the body may change after the initial construction of
        the response. This allows setting the body with a custom content
        type.

        """
    def setHeader(self, header_name: str, header_value: str) -> None:
        """setHeader(self: _hwebserver.Response, header_name: str, header_value: str) -> None

        Add/change an HTTP header in the response.

        """
    def statusLabel(self) -> str:
        """statusLabel(self: _hwebserver.Response) -> str

        Return the status label of the response. An exampe label would be
        200 OK.

        Calling this method generates a new copy of the string each time, so
        you are advised to avoid calling it more times than necessary.

        """

class UploadedFile:
    def __init__(self, *, no_constructor: Never) -> None: ...
    def isInMemory(self) -> bool:
        """isInMemory(self: _hwebserver.UploadedFile) -> bool

        Returns whether the uploaded file is currently stored in memory, or
        if it is too large and was streamed to a temporary file on disk. See
        to change the thresholds for what is considered a large file upload.

        """
    def name(self) -> str:
        """name(self: _hwebserver.UploadedFile) -> str

        Returns the name of the file that was uploaded. Note that this is
        different from the POST variable name; the POST variable name is the
        key in the dict.

        """
    def read(self, max_size: int = ...) -> bytes:
        """read(self: _hwebserver.UploadedFile, max_size: int = -1) -> bytes

        Read up to max_size bytes of the uploaded file. This method handles
        the cases where the file's contents are stored in memory and when
        they are in a temporary file. If max_size is negative this method
        returns the rest of the data in the file, but be careful not to load
        very large file uploads into memory.

        """
    def saveToDisk(self) -> None:
        """saveToDisk(self: _hwebserver.UploadedFile) -> None

        Force a in-memory file to be saved to a temporary file on disk.

        If the file was already saved to a temporary file, calling this
        method has no effect.

        """
    def size(self) -> int:
        """size(self: _hwebserver.UploadedFile) -> int

        Returns the size of the file that was uploaded.

        """
    def temporaryFilePath(self) -> str:
        """temporaryFilePath(self: _hwebserver.UploadedFile) -> str

        If isInMemory returns False, returns the path to the uploaded file
        that was streamed to disk. Otherwise returns an empty string.

        Note that if an uploaded file was saved to disk it is automatically
        deleted after the response is sent.

        """

class webServerSeverity:
    __members__: ClassVar[dict[str, webServerSeverity]] = ...  # read-only
    AbortSeverity: ClassVar[webServerSeverity] = ...
    FatalSeverity: ClassVar[webServerSeverity] = ...
    MessageSeverity: ClassVar[webServerSeverity] = ...
    PromptSeverity: ClassVar[webServerSeverity] = ...
    WarningSeverity: ClassVar[webServerSeverity] = ...
    __entries: ClassVar[dict[str, tuple[webServerSeverity, str | None]]] = ...
    def __init__(self, value: int) -> None:
        """__init__(self: _hwebserver.webServerSeverity, value: int) -> None"""
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object) -> bool"""
    def __hash__(self) -> int:
        """__hash__(self: object) -> int"""
    def __index__(self) -> int:
        """__index__(self: _hwebserver.webServerSeverity) -> int"""
    def __int__(self) -> int:
        """__int__(self: _hwebserver.webServerSeverity) -> int"""
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object) -> bool"""
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class webServerVerbosity:
    __members__: ClassVar[dict[str, webServerVerbosity]] = ...  # read-only
    High: ClassVar[webServerVerbosity] = ...
    Low: ClassVar[webServerVerbosity] = ...
    Medium: ClassVar[webServerVerbosity] = ...
    __entries: ClassVar[dict[str, tuple[webServerVerbosity, str | None]]] = ...
    def __init__(self, value: int) -> None:
        """__init__(self: _hwebserver.webServerVerbosity, value: int) -> None"""
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object) -> bool"""
    def __ge__(self, other: webServerVerbosity) -> bool:
        """__ge__(self: object, other: object) -> bool"""
    def __gt__(self, other: webServerVerbosity) -> bool:
        """__gt__(self: object, other: object) -> bool"""
    def __hash__(self) -> int:
        """__hash__(self: object) -> int"""
    def __index__(self) -> int:
        """__index__(self: _hwebserver.webServerVerbosity) -> int"""
    def __int__(self) -> int:
        """__int__(self: _hwebserver.webServerVerbosity) -> int"""
    def __le__(self, other: webServerVerbosity) -> bool:
        """__le__(self: object, other: object) -> bool"""
    def __lt__(self, other: webServerVerbosity) -> bool:
        """__lt__(self: object, other: object) -> bool"""
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object) -> bool"""
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

def isAsyncioEnabled() -> bool:
    """isAsyncioEnabled() -> bool"""
def isUIAvailable() -> bool:
    """isUIAvailable() -> bool

    Returns True if the Houdini UI is available

    """
def setAsyncioLoop(arg0: asyncio.AbstractEventLoop) -> None:
    """setAsyncioLoop(arg0: object) -> None"""
def version_info() -> str:
    """version_info() -> str"""
