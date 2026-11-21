# Houdini stubs generated from Houdini 22.0.466

from typing import Any
import hou
import os
import hwebserver
import sop
from _hwebserver import *
import asyncio
import threading
import typing
from _hwebserver import PyServer as PyServer, PyURLHandler as PyURLHandler, PyWebSocket as PyWebSocket, Request as Request, Response as Response, webServerSeverity as webServerSeverity, webServerVerbosity as webServerVerbosity
from _typeshed import SupportsRead
from _typeshed.wsgi import WSGIApplication as WSGIApplication
from collections.abc import Callable, Sequence
from typing import Never, TypedDict, Unpack

from typing import TypeAlias
from typing import TypeVar
from collections.abc import Awaitable
from collections.abc import Iterable
from collections.abc import Mapping
from collections.abc import MutableMapping
from houtypes import JSONLike
from typing import Concatenate
from typing import TypeAlias
from typing import TypeVar
_SyncURLHandlerFunction: TypeAlias = Callable[[Request], Response]
_AsyncURLHandlerFunction: TypeAlias = Callable[[Request], Awaitable[Response | asyncio.Future[Response]]]
_URLHandlerFunctionT = TypeVar('_URLHandlerFunctionT', bound=_SyncURLHandlerFunction | _AsyncURLHandlerFunction)
_APIFunction: TypeAlias = Callable[Concatenate[Request, ...], object]
_APIFunctionT = TypeVar('_APIFunctionT', bound=_APIFunction)
_ArgTypes: TypeAlias = MutableMapping[str, Callable[[str], object]]
_Ports: TypeAlias = str | Sequence[str] | None
_ASGIReceiveEvent: TypeAlias = dict[str, str | bytes | int | None]
_ASGIScope: TypeAlias = dict[str, str | bytes | dict[str, str] | list[list[bytes]] | tuple[str, int]]
_ASGISendEvent: TypeAlias = Mapping[str, str | bytes | int | Iterable[Sequence[bytes]] | None]
_ASGIApplication: TypeAlias = Callable[[_ASGIScope, Callable[[], Awaitable[_ASGIReceiveEvent]], Callable[[_ASGISendEvent], Awaitable[None]]], Awaitable[None]]
_JSONT = TypeVar('_JSONT', bound=JSONLike)
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

def run(*args: int, **kwargs: Unpack[_RunOptions]) -> None:
    """
hwebserver.run

Starts Houdini's web server.

USAGE
  run(port=8008, debug=False, max_num_threads=4, in_background=None,
  reload_source_changes=None, max_in_memory_file_upload_size=None,
  max_request_size=None, settings=None, ports=[])

  * Start the server, making it listen a the port for incoming HTTP
    connections, calling previously registered URL and API handlers.

  * When the server is started from hython when in_background is not
    True, you can stop it by pressing [Ctrl + C] (Linux and Mac) or
    [Ctrl + Break]/[Ctrl + ScrLk] on Windows in the terminal.


port
    The port number to listen on. If this port is already in use or the
    process does not have permission to listen on it, the function
    raises .

debug
    If this is True, the server writes console log messages and displays
    stack traces for Python exceptions raised when handling requests. It
    also returns the stack traces in response bodies.

    When running in hython, this also sets reload_source_changes to
    True.

    You can check if the server is running in debug mode using .

max_num_threads
    The maximum number of simultaneous worker threads created to handle
    concurrent requests.

    Any calls in the hwebserver package acquire a global lock, and
    Python handler functions must acquire the GIL, so handlers cannot
    usually run concurrently. The main speed benefit of multithreading
    comes when serving static files or making blocking I/O operations
    from Python that do not involve Houdini.

in_background
    Whether the function should start the server in a separate thread.
    If you pass in_background=False, this function will never return
    unless the server is interrupted or server code calls .

    If in_background is None (the default value), it will be set to True
    in a graphical Houdini session and False otherwise.

reload_source_changes
    If this is True, the server monitors all loaded Python source files
    and restarts the server whenever any of them change. This lets you
    edit your Python code and see the results without needing to stop
    and restart the server manually.

max_in_memory_file_upload_size
    The maximum size, in bytes, of uploaded files that will be kept in
    RAM rather than written to a temp file. By default, the server will
    keep uploaded files that are less than 2.5 MB in memory, but write
    files larger than that to disk. This argument lets you override that
    threshold.

max_request_size
    The maximum size of an HTTP request, in bytes. If this is None, the
    default value is 3 GB.

settings
    Specify the settings file to add extra settings to the web server.
    Currently this only allows you to specify the CORS whitelist. This
    works similarly to djangos settings file.

ports
    The extra ports the server should listen on.

verbosity
    The verbosity of the server. The default settings is low.

port_callback
    If the program needs to know the actual port number the server is
    running on a port callback can be used to retrieve the actual port
    number. It is not recommended to use this callback as an
    initialization function as there is no guarantee made on where in
    the initialization stage this callback will be called.

up_to_port
    If the port number from the port parameter failed to listen then try
    every port up to this parameters port number. As an example, if the
    port number is 80 and this parameter is 90, then every port from
    81-90 will be tried before giving up. The first port in this range
    that is able to listen to will be used as the main port for the
    server.

use_free_port_on_failure
    If the port range and initial port both fail to find a free port
    then let the OS pick a free port. This parameter can be used instead
    of the port range if the server just needs to find a free port with
    little care about the actual port number.

RELATED



"""
def setSettingsForPort(settings: str | _PortSettings, port_name: str) -> None:
    '''
hwebserver.setSettingsForPort

Set the settings for a specific port.

USAGE
  setSettingsForPort(settings, port_name=\\"\\")

This function allows adjusting settings for a specific port.


PORT
    The port number to listen on.

MAX_PORT
    If specified the server will try from PORT up to the specified
    MAX_PORT. The server will stop at the first port that is usable.

ALLOW_SYSTEM_PORT
    Allow the system to pick a port if the range of ports fail to find
    an available port.

ADDRESS
    The address to bind the server on. The default is the any address
    (i.e. 0.0.0.0).

IPV6
    Enable IPv6 support.

ALLOWED_HOSTS
    The list of hosts the server is allowed to serve. This is a security
    measure to prevent host header attacks. The default is all hosts are
    allowed.

USE_X_FORWARDED_HOST
    A boolean that specifies whether to use the X-Forwarded-Host instead
    of the Host header. The default is False.

LOG_FILE
    The log file this port should log all of its information too.

MIN_LOG_SEVERITY
    The minimum severity entries will be logged to the log file. The
    default is hwebserver.WarningSeverity.

SSL_CERTIFICATE
    The SSL certificate chain the server should use.

SSL_CERTIFICATE_KEY
    The private key the server should use. The key must be in PEM
    format.

SSL_DH_PARAMS
    The Diffie-Hellman (DH) params the server should use.

SSL_VERIFY_PEER
    If the server should verify the peer when using HTTPS. The default
    is True.

SSL_REDIRECT
    If an HTTP request is received it will be redirected to HTTPS. If
    the request does not contain header Upgrade-Insecure-Requests: \\"1\\"
    then the server will reject the request with 403 (Forbidden).

SSL_REDIRECT_HOST
    When redirecting an insecure request use this host instead of the
    host in the request. This has no affect if SSL_REDIRECT is False.

SSL_REDIRECT_EXEMPT
    List of hosts that are exempt from being redirected to HTTPS. This
    has no affect if SSL_REDIRECT is False.

SECURE_HSTS_SECONDS
    The number of seconds the client should remember the path is only to
    be accessed using HTTPS. The default is 0.

SECURE_HSTS_INCLUDE_SUBDOMAINS
    If this is set to True then all subdomains should be treated as only
    accessible via HTTPS. The default is False.

SECURE_HSTS_PRELOAD
    If this is set to True then the client should never attempt to use
    an insecure request. The default is False.

SECURE_CONTENT_TYPE_NOSNIFF
    If this is set to True X-Content-Type-Options: nosniff is added to
    the response. This prevents against some types of drive-by-
    downloads. The default is True.

SECURE_REFERRER_POLICY
    If this is set the Referrer Policy is added to all responses that do
    not already have this header set. The default is same-origin.

SECURE_CROSS_ORIGIN_OPENER_POLICY
    This settings helps to prevent a set of cross-origin attacks dubbed
    XS-Leaks. This settings if specified will set the Cross-Origin-
    Opener-Policy if not already set. The default is same-origin.

'''

class Server(PyServer):
    def __init__(self, *args: Unpack[tuple[str]], **kwargs: Never) -> None: ...
    def urlHandler(self, path: str, is_prefix: bool = False, ports: _Ports = ...) -> Callable[[_URLHandlerFunctionT], _URLHandlerFunctionT]:
        '''
hwebserver.urlHandler

Decorator for functions that handle requests to Houdini\'s web server.

USAGE
  urlHandler(path, is_prefix=False, ports=[])

When you decorate a function with this decorator, it registers the
function as the handler for requests at the given server path.


path
    A string starting with \\"/\\", but which may or may not end with a
    slash. When registering paths, trailing slashes do not affect the
    behavior of the server; if path does not have a slash it is
    implicitly added, and when the server matches paths to request
    handlers, any paths sent in server requests have a path added to
    them if it is missing. Note that contains the unaltered path that
    was requested, though.

is_prefix
    If False, the handler function will only be invoked when the
    requested path matches path. If True, however, the handler will be
    called when the requested path starts with path, followed by a
    slash, followed by anything else.

ports
    Any ports the handler function can be invoked on. If no ports are
    specified the handler function is bound to the main port of the
    webserver. The port name can be any name that is not empty and is
    not main (reserved for the main port).

  * Your function should take a object as an argument. This object has
    methods for getting the request path, URL arguments, form
    parameters, header values, and so on.

  * Your function should return a object. The Response object lets you
    set the response content and HTTP code, add headers, and so on.

  * If you want to the response to be viewable in a web browser, there
    are many ways to generate HTML quickly and easily in Python. Note
    that Houdini ships with the jinja2 templating library.


NOTE
    The name of the decorated function does not matter.

> import hwebserver
> 
> @hwebserver.urlHandler(\\"/hello\\")
> def my_handler(request):
>     return hwebserver.Response(\\"Hello world\\")

To download a file to the client, return the result of :

> import os.path
> import hwebserver
> 
> @hwebserver.urlHandler(\\"/hello\\")
> def my_handler(request):
>     file_path = os.path.expandvars(\\"$HIP/hello.txt\\")
>     return hwebserver.fileResponse(file_path)

To build remote procedure call APIs, use the decorator.


NEW
    URL handlers support asyncio (Python 3 builds only). Since there is
    a performance hit to using asyncio as the web server is C++ first.
    It is recommended to use coroutine API functions only when an API
    function is likely to wait for IO while handling the request. The
    decorator will automatically detect the function type and handle the
    function based on its type.

PREFIX PATHS

    You can use the is_prefix=True argument in the decorator to specify
    that your function will handle all requests starting with the given
    path.

    For example, @hwebserver.urlHandler(\\"/node\\", is_prefix=True) will
    handle all requests that start with /node, such as /node/obj,
    /node/stage/light1, /node/obj/my_hda/sphere1, and so on.

    In the handler, you can get the full request path using
    request.path() and it is up to the handler to strip off the prefix
    path to get the suffix path.

  > import hou
  > import hwebserver
  > 
  > 
  > @hwebserver.urlHandler(\\"/node\\", is_prefix=True)
  > def node_handler(request):
  >     path = request.path()
  >     assert path.startswith(\\"/node\\")
  > 
  >     # Strip off the \\"/node\\" at the start and any trailing slash.
  >     node_path = path[len(\\"/node\\"):]
  >     if not node_path:
  >         node_path = \\"/\\"
  >     if node_path != \\"/\\" and node_path.endswith(\\"/\\"):
  >         node_path = node_path[:-1]
  > 
  >     # Get the hou.Node object at the given path.  If it doesn\'t exist, respond
  >     # with 404 Not Found.
  >     node = hou.node(node_path)
  >     if not node:
  >         return hwebserver.notFoundResponse(request)
  > 
  >     html = \\"<h1>{}</h1>\\".format(node.name())
  >     html += \\"<p>{}</p>\\".format(node.type().name())
  >     html += \\"<ul>
\\"
  >     if node != hou.root():
  >         html += \'<li><a href=\\"/node{}\\">..</a></li>
\'.format(
  >             node.parent().path())
  >     for child_node in node.children():
  >         html += \'<li><a href=\\"/node{}\\">{}</a></li>
\'.format(
  >             child_node.path(), child_node.name())
  >     html += \\"</ul>
\\"
  > 
  >     return hwebserver.Response(html)

PATH MATCHING

  * If a path has an exact match except for a trailing slash, the
    trailing slash is removed.

  * If the suffix of a prefixed match has a trailing slash, the trailing
    slash is removed.

    For example, suppose you\'ve registered / and /exact as exact path
    handlers, and /pre and /pre/usd as prefix handlers.

    /
    /

    /

    /exact
    /exact

    /exact

    /exact/
    /exact

    /exact/

    /exact/geo
    404

    N/A

    /pre/
    /pre

    /pre/

    /pre
    /pre

    /pre

    /pre/geo
    /pre

    /pre/geo

    /pre/geo/
    /pre

    /pre/geo/

    /pre/usd
    /pre/usd

    /pre/usd

    /pre/usd/scene
    /pre/usd

    /pre/usd/scene

    /pregeo
    404

    N/A

    /missing
    404

    N/A

EXAMPLES

  > import hou
  > import hwebserver
  > 
  > 
  > @hwebserver.urlHandler(\\"/\\")
  > def index(request):
  >     return hwebserver.Response(
  >         \'\'\'
  >         <form method=\\"GET\\" action=\\"/crag.bgeo\\">
  >             Download geometry at frame:
  >             <input name=\\"frame\\" value=\\"1\\">
  >             <input type=\\"submit\\" value=\\"Download\\">
  >         </form>
  >         \'\'\')
  > 
  > 
  > @hwebserver.urlHandler(\\"/crag.bgeo\\")
  > def crag(request):
  >     \'\'\'Return a bgeo file of the Crag test geometry at the requested frame.\'\'\'
  >     url_args = request.GET()
  >     frame_str = url_args.get(\\"frame\\", \\"1\\")
  >     try:
  >         frame = float(frame_str)
  >     except ValueError:
  >         return hwebserver.errorResponse(
  >             request, \\"Frame is not a number\\", 422)
  > 
  >     sop = hou.node(\\"/obj/geo1/testgeometry_crag1\\")
  >     if sop is None:
  >         sop = hou.node(\\"/obj\\").createNode(\\"geo\\").createNode(\\"testgeometry_crag\\")
  > 
  >     response = hwebserver.Response(
  >         sop.geometryAtFrame(frame).data(),
  >         content_type=\\"application/octet-stream\\"
  >     )
  >     response.setHeader(
  >         \\"Content-Disposition\\",
  >         \'attachment; filename=\\"crag_%s.bgeo\' % frame
  >     )
  >     return response

RELATED


    URLHandler

'''
    @typing.overload
    def apiFunction(self, namespace: _APIFunctionT, return_binary: bool = ..., arg_types: _ArgTypes | None = ..., ports: _Ports = ...) -> _APIFunctionT: ...
    @typing.overload
    def apiFunction(self, namespace: str | None = ..., return_binary: bool = ..., arg_types: _ArgTypes | None = ..., ports: _Ports = ...) -> Callable[[_APIFunctionT], _APIFunctionT]: ...
    def registerAPIFunction(self, name: str, function: _APIFunction, return_binary: bool = False, arg_types: _ArgTypes | None = None, ports: _Ports = ...) -> None: ...
    def registerWSGIApp(self, application: WSGIApplication, path: str, ports: _Ports = ...) -> None:
        '''
hwebserver.registerWSGIApp

Function used to register a wsgi capable application such as django to
be used on a path prefix.

USAGE
  registerWSGIApp(application=(), path=None, ports=[])

This function allows you to hook in a wsgi capable application such as
flask or django and use the houdini web server as the server backend.

> import os
> import hwebserver
> import testsite.wsgi
> 
> hwebserver.registerWSGIApp(testsite.wsgi.application, \\"/\\")
> hwebserver.run(8000, debug=True)

NOTE
    Currently multi part form requests are not fully supported with
    wsgi. If you need to use these requests you can continue to use hou
    url handlers.

'''
    def registerASGIApp(self, application: _ASGIApplication, path: str, ports: Sequence[str] = ...) -> None:
        '''
hwebserver.registerASGIApp

Function used to register a asgi capable application such as django to
be used on a path prefix.

USAGE
  registerASGIApp(application=(), path=None, ports=[])

This function allows you to hook in a asgi capable application such as
flask or django and use the Houdini web server as the server backend.

> import os
> import hwebserver
> import testsite.asgi
> 
> hwebserver.registerWSGIApp(testsite.asgi.application, \\"/\\")
> hwebserver.run(8000, debug=True)

NOTE
    Currently HTTP is only supported and this feature is currently in
    Alpha.

'''
    def webSocket(self, path: str, is_prefix: bool = False, port_name: str = '') -> Callable[[type['WebSocket']], None]:
        '''
hwebserver.webSocket

Decorator for registering WebSocket classes with Houdini\'s web server.

USAGE
  webSocket(path, is_prefix=False, ports=[])


NOTE
    WebSocket support is Python3 only.

When you decorate a class with this decorator, it registers the class
with the webserver on the given path.


path
    A string starting with \\"/\\", but which may or may not end with a
    slash. When registering paths, trailing slashes do not affect the
    behavior of the server; if path does not have a slash it is
    implicitly added, and when the server matches paths to request
    handlers, any paths sent in server requests have a path added to
    them if it is missing.

is_prefix
    If False, the class will only be created when the requested path
    matches path. If True, however, the class will be created when the
    requested path starts with path, followed by a slash, followed by
    anything else.

ports
    Any ports the websocket class can be created on. If no ports are
    specified the class is bound to the main port of the webserver. The
    port name can be any name that is not empty and is not main
    (reserved for the main port).

RELATED


    WebSocket

'''
    def setSettingsForPort(self, settings: str | _PortSettings, port_name: str) -> None:
        '''
hwebserver.setSettingsForPort

Set the settings for a specific port.

USAGE
  setSettingsForPort(settings, port_name=\\"\\")

This function allows adjusting settings for a specific port.


PORT
    The port number to listen on.

MAX_PORT
    If specified the server will try from PORT up to the specified
    MAX_PORT. The server will stop at the first port that is usable.

ALLOW_SYSTEM_PORT
    Allow the system to pick a port if the range of ports fail to find
    an available port.

ADDRESS
    The address to bind the server on. The default is the any address
    (i.e. 0.0.0.0).

IPV6
    Enable IPv6 support.

ALLOWED_HOSTS
    The list of hosts the server is allowed to serve. This is a security
    measure to prevent host header attacks. The default is all hosts are
    allowed.

USE_X_FORWARDED_HOST
    A boolean that specifies whether to use the X-Forwarded-Host instead
    of the Host header. The default is False.

LOG_FILE
    The log file this port should log all of its information too.

MIN_LOG_SEVERITY
    The minimum severity entries will be logged to the log file. The
    default is hwebserver.WarningSeverity.

SSL_CERTIFICATE
    The SSL certificate chain the server should use.

SSL_CERTIFICATE_KEY
    The private key the server should use. The key must be in PEM
    format.

SSL_DH_PARAMS
    The Diffie-Hellman (DH) params the server should use.

SSL_VERIFY_PEER
    If the server should verify the peer when using HTTPS. The default
    is True.

SSL_REDIRECT
    If an HTTP request is received it will be redirected to HTTPS. If
    the request does not contain header Upgrade-Insecure-Requests: \\"1\\"
    then the server will reject the request with 403 (Forbidden).

SSL_REDIRECT_HOST
    When redirecting an insecure request use this host instead of the
    host in the request. This has no affect if SSL_REDIRECT is False.

SSL_REDIRECT_EXEMPT
    List of hosts that are exempt from being redirected to HTTPS. This
    has no affect if SSL_REDIRECT is False.

SECURE_HSTS_SECONDS
    The number of seconds the client should remember the path is only to
    be accessed using HTTPS. The default is 0.

SECURE_HSTS_INCLUDE_SUBDOMAINS
    If this is set to True then all subdomains should be treated as only
    accessible via HTTPS. The default is False.

SECURE_HSTS_PRELOAD
    If this is set to True then the client should never attempt to use
    an insecure request. The default is False.

SECURE_CONTENT_TYPE_NOSNIFF
    If this is set to True X-Content-Type-Options: nosniff is added to
    the response. This prevents against some types of drive-by-
    downloads. The default is True.

SECURE_REFERRER_POLICY
    If this is set the Referrer Policy is added to all responses that do
    not already have this header set. The default is same-origin.

SECURE_CROSS_ORIGIN_OPENER_POLICY
    This settings helps to prevent a set of cross-origin attacks dubbed
    XS-Leaks. This settings if specified will set the Cross-Origin-
    Opener-Policy if not already set. The default is same-origin.

'''
    def run(self, *args: int, **kwargs: Unpack[_RunOptions]) -> None:
        """
hwebserver.run

Starts Houdini's web server.

USAGE
  run(port=8008, debug=False, max_num_threads=4, in_background=None,
  reload_source_changes=None, max_in_memory_file_upload_size=None,
  max_request_size=None, settings=None, ports=[])

  * Start the server, making it listen a the port for incoming HTTP
    connections, calling previously registered URL and API handlers.

  * When the server is started from hython when in_background is not
    True, you can stop it by pressing [Ctrl + C] (Linux and Mac) or
    [Ctrl + Break]/[Ctrl + ScrLk] on Windows in the terminal.


port
    The port number to listen on. If this port is already in use or the
    process does not have permission to listen on it, the function
    raises .

debug
    If this is True, the server writes console log messages and displays
    stack traces for Python exceptions raised when handling requests. It
    also returns the stack traces in response bodies.

    When running in hython, this also sets reload_source_changes to
    True.

    You can check if the server is running in debug mode using .

max_num_threads
    The maximum number of simultaneous worker threads created to handle
    concurrent requests.

    Any calls in the hwebserver package acquire a global lock, and
    Python handler functions must acquire the GIL, so handlers cannot
    usually run concurrently. The main speed benefit of multithreading
    comes when serving static files or making blocking I/O operations
    from Python that do not involve Houdini.

in_background
    Whether the function should start the server in a separate thread.
    If you pass in_background=False, this function will never return
    unless the server is interrupted or server code calls .

    If in_background is None (the default value), it will be set to True
    in a graphical Houdini session and False otherwise.

reload_source_changes
    If this is True, the server monitors all loaded Python source files
    and restarts the server whenever any of them change. This lets you
    edit your Python code and see the results without needing to stop
    and restart the server manually.

max_in_memory_file_upload_size
    The maximum size, in bytes, of uploaded files that will be kept in
    RAM rather than written to a temp file. By default, the server will
    keep uploaded files that are less than 2.5 MB in memory, but write
    files larger than that to disk. This argument lets you override that
    threshold.

max_request_size
    The maximum size of an HTTP request, in bytes. If this is None, the
    default value is 3 GB.

settings
    Specify the settings file to add extra settings to the web server.
    Currently this only allows you to specify the CORS whitelist. This
    works similarly to djangos settings file.

ports
    The extra ports the server should listen on.

verbosity
    The verbosity of the server. The default settings is low.

port_callback
    If the program needs to know the actual port number the server is
    running on a port callback can be used to retrieve the actual port
    number. It is not recommended to use this callback as an
    initialization function as there is no guarantee made on where in
    the initialization stage this callback will be called.

up_to_port
    If the port number from the port parameter failed to listen then try
    every port up to this parameters port number. As an example, if the
    port number is 80 and this parameter is 90, then every port from
    81-90 will be tried before giving up. The first port in this range
    that is able to listen to will be used as the main port for the
    server.

use_free_port_on_failure
    If the port range and initial port both fail to find a free port
    then let the OS pick a free port. This parameter can be used instead
    of the port range if the server just needs to find a free port with
    little care about the actual port number.

RELATED



"""

class WebSocket(PyWebSocket):
    '''
hwebserver.WebSocket

Base class for WebSocket support with the embedded server.

This class is the base class for all websocket support in Houdini\'s
embedded server.


NOTE
    WebSocket support is Python3 only.

SETUP

    On its own the WebSocket class cannot do much of anything. The class
    must be registered with the server so that incoming Upgrade:
    websocket requests can create an instance of the class and hand off
    the handling to the websocket instance. To install the instance the
    decorator can be used to install the websocket.

EXAMPLE

    The below example will echo back anything sent from the client. This
    websocket will be used anytime a client sends a HTTP upgrade request
    on path /echo.

  > @webSocket(\\"/echo\\")
  > class WebSocketEcho(hwebserver.WebSocket):
  >     async def connect(self, req):
  >         await self.accept()
  > 
  >     async def receive(self, text_data=None, bytes_data=None):
  >         # Send message as text data
  >         await self.send(text_data)

RELATED



'''
    def __init__(self, *args: Never, **kwargs: Never) -> None: ...

def webSocket(path: str, is_prefix: bool = False, port_name: str = '') -> Callable[[type[WebSocket]], None]:
    '''
hwebserver.webSocket

Decorator for registering WebSocket classes with Houdini\'s web server.

USAGE
  webSocket(path, is_prefix=False, ports=[])


NOTE
    WebSocket support is Python3 only.

When you decorate a class with this decorator, it registers the class
with the webserver on the given path.


path
    A string starting with \\"/\\", but which may or may not end with a
    slash. When registering paths, trailing slashes do not affect the
    behavior of the server; if path does not have a slash it is
    implicitly added, and when the server matches paths to request
    handlers, any paths sent in server requests have a path added to
    them if it is missing.

is_prefix
    If False, the class will only be created when the requested path
    matches path. If True, however, the class will be created when the
    requested path starts with path, followed by a slash, followed by
    anything else.

ports
    Any ports the websocket class can be created on. If no ports are
    specified the class is bound to the main port of the webserver. The
    port name can be any name that is not empty and is not main
    (reserved for the main port).

RELATED


    WebSocket

'''

class URLHandler(PyURLHandler):
    '''
hwebserver.URLHandler

The general purpose HTTP handler.

In cases where a general purpose url handler is desired over a builtin
handler (i.e. @urlHandler or @apiFunction) the URLHandler class can be
used. With the general purpose handler other RPC can be built on top
(e.g. JSON RPC) while still being able to access all of Houdini.


NOTE
    The URLHandler is best suited for cases where the handler does not
    need to wait for other resources before responding. If the request
    needs to wait for other resources before responding the should be
    used instead.

EXAMPLE

    This example shows how to create a handler that will call a provided
    function when a new request comes in. With this class a similar
    @urlHandler decorator can be created that uses this example.

  > class URLCallbackHandler(hwebserver.URLHandler):
  >     def __init__(self, path, function, is_prefix=False):
  >         URLHandler.__init__(self, path, methods=[\'GET\',\'POST\'], allows_partial=is_prefix)
  >         self._function = function
  > 
  >     def handle(self, request):
  >         if self._function is None:
  >             return hwebserver.errorResponse(request, \\"Handler doesnt have a function attached.\\", 500)
  >         return self._function(request)

RELATED


    urlHandler
    AsyncURLHandler

'''
    @typing.overload
    def __init__(self, path: str, allows_partial: bool = ...) -> None: ...
    @typing.overload
    def __init__(self, path: str, methods: Sequence[str], allows_partial: bool = ...) -> None: ...

class AsyncURLHandler(PyURLHandler):
    '''
hwebserver.AsyncURLHandler

The general purpose Async HTTP handler.

In cases where a general purpose url handler is desired over a builtin
handler (i.e. @urlHandler or @apiFunction) the AsyncURLHandler class can
be used. With the general purpose handler other RPC can be built on top
(e.g. JSON RPC) while still being able to access all of Houdini. This
handler allows for use with asyncio and is therefore Python3 only.

:NOTE

EXAMPLE

    This example shows how to create a handler that will call a provided
    function when a new request comes in.

  > class URLCallbackHandler(hwebserver.AsyncURLHandler):
  >     def __init__(self, path, function, is_prefix=False):
  >         URLHandler.__init__(self, path, methods=[\'GET\',\'POST\'], allows_partial=is_prefix)
  >         self._function = function
  > 
  >     async def handle(self, request):
  >         if self._function is None:
  >             request.send(hwebserver.errorResponse(request, \\"Handler doesnt have a function attached.\\", 500))
  >             return
  >         resp = await self._function(request)
  >         request.send(resp)

RELATED


    urlHandler
    URLHandler

'''
    @typing.overload
    def __init__(self, path: str, allows_partial: bool = ...) -> None: ...
    @typing.overload
    def __init__(self, path: str, methods: Sequence[str], allows_partial: bool = ...) -> None: ...

class AsyncURLCallbackHandler(AsyncURLHandler):
    def __init__(self, path: str, function: _AsyncURLHandlerFunction, is_prefix: bool = False) -> None: ...
    async def handle(self, request: Request) -> Response | None: ...

class URLCallbackHandler(URLHandler):
    def __init__(self, path: str, function: _SyncURLHandlerFunction, is_prefix: bool = False) -> None: ...
    def handle(self, request: Request) -> Response: ...

def urlHandler(path: str, is_prefix: bool = False, ports: _Ports = ...) -> Callable[[_SyncURLHandlerFunction | _AsyncURLHandlerFunction], None]:
    '''
hwebserver.urlHandler

Decorator for functions that handle requests to Houdini\'s web server.

USAGE
  urlHandler(path, is_prefix=False, ports=[])

When you decorate a function with this decorator, it registers the
function as the handler for requests at the given server path.


path
    A string starting with \\"/\\", but which may or may not end with a
    slash. When registering paths, trailing slashes do not affect the
    behavior of the server; if path does not have a slash it is
    implicitly added, and when the server matches paths to request
    handlers, any paths sent in server requests have a path added to
    them if it is missing. Note that contains the unaltered path that
    was requested, though.

is_prefix
    If False, the handler function will only be invoked when the
    requested path matches path. If True, however, the handler will be
    called when the requested path starts with path, followed by a
    slash, followed by anything else.

ports
    Any ports the handler function can be invoked on. If no ports are
    specified the handler function is bound to the main port of the
    webserver. The port name can be any name that is not empty and is
    not main (reserved for the main port).

  * Your function should take a object as an argument. This object has
    methods for getting the request path, URL arguments, form
    parameters, header values, and so on.

  * Your function should return a object. The Response object lets you
    set the response content and HTTP code, add headers, and so on.

  * If you want to the response to be viewable in a web browser, there
    are many ways to generate HTML quickly and easily in Python. Note
    that Houdini ships with the jinja2 templating library.


NOTE
    The name of the decorated function does not matter.

> import hwebserver
> 
> @hwebserver.urlHandler(\\"/hello\\")
> def my_handler(request):
>     return hwebserver.Response(\\"Hello world\\")

To download a file to the client, return the result of :

> import os.path
> import hwebserver
> 
> @hwebserver.urlHandler(\\"/hello\\")
> def my_handler(request):
>     file_path = os.path.expandvars(\\"$HIP/hello.txt\\")
>     return hwebserver.fileResponse(file_path)

To build remote procedure call APIs, use the decorator.


NEW
    URL handlers support asyncio (Python 3 builds only). Since there is
    a performance hit to using asyncio as the web server is C++ first.
    It is recommended to use coroutine API functions only when an API
    function is likely to wait for IO while handling the request. The
    decorator will automatically detect the function type and handle the
    function based on its type.

PREFIX PATHS

    You can use the is_prefix=True argument in the decorator to specify
    that your function will handle all requests starting with the given
    path.

    For example, @hwebserver.urlHandler(\\"/node\\", is_prefix=True) will
    handle all requests that start with /node, such as /node/obj,
    /node/stage/light1, /node/obj/my_hda/sphere1, and so on.

    In the handler, you can get the full request path using
    request.path() and it is up to the handler to strip off the prefix
    path to get the suffix path.

  > import hou
  > import hwebserver
  > 
  > 
  > @hwebserver.urlHandler(\\"/node\\", is_prefix=True)
  > def node_handler(request):
  >     path = request.path()
  >     assert path.startswith(\\"/node\\")
  > 
  >     # Strip off the \\"/node\\" at the start and any trailing slash.
  >     node_path = path[len(\\"/node\\"):]
  >     if not node_path:
  >         node_path = \\"/\\"
  >     if node_path != \\"/\\" and node_path.endswith(\\"/\\"):
  >         node_path = node_path[:-1]
  > 
  >     # Get the hou.Node object at the given path.  If it doesn\'t exist, respond
  >     # with 404 Not Found.
  >     node = hou.node(node_path)
  >     if not node:
  >         return hwebserver.notFoundResponse(request)
  > 
  >     html = \\"<h1>{}</h1>\\".format(node.name())
  >     html += \\"<p>{}</p>\\".format(node.type().name())
  >     html += \\"<ul>
\\"
  >     if node != hou.root():
  >         html += \'<li><a href=\\"/node{}\\">..</a></li>
\'.format(
  >             node.parent().path())
  >     for child_node in node.children():
  >         html += \'<li><a href=\\"/node{}\\">{}</a></li>
\'.format(
  >             child_node.path(), child_node.name())
  >     html += \\"</ul>
\\"
  > 
  >     return hwebserver.Response(html)

PATH MATCHING

  * If a path has an exact match except for a trailing slash, the
    trailing slash is removed.

  * If the suffix of a prefixed match has a trailing slash, the trailing
    slash is removed.

    For example, suppose you\'ve registered / and /exact as exact path
    handlers, and /pre and /pre/usd as prefix handlers.

    /
    /

    /

    /exact
    /exact

    /exact

    /exact/
    /exact

    /exact/

    /exact/geo
    404

    N/A

    /pre/
    /pre

    /pre/

    /pre
    /pre

    /pre

    /pre/geo
    /pre

    /pre/geo

    /pre/geo/
    /pre

    /pre/geo/

    /pre/usd
    /pre/usd

    /pre/usd

    /pre/usd/scene
    /pre/usd

    /pre/usd/scene

    /pregeo
    404

    N/A

    /missing
    404

    N/A

EXAMPLES

  > import hou
  > import hwebserver
  > 
  > 
  > @hwebserver.urlHandler(\\"/\\")
  > def index(request):
  >     return hwebserver.Response(
  >         \'\'\'
  >         <form method=\\"GET\\" action=\\"/crag.bgeo\\">
  >             Download geometry at frame:
  >             <input name=\\"frame\\" value=\\"1\\">
  >             <input type=\\"submit\\" value=\\"Download\\">
  >         </form>
  >         \'\'\')
  > 
  > 
  > @hwebserver.urlHandler(\\"/crag.bgeo\\")
  > def crag(request):
  >     \'\'\'Return a bgeo file of the Crag test geometry at the requested frame.\'\'\'
  >     url_args = request.GET()
  >     frame_str = url_args.get(\\"frame\\", \\"1\\")
  >     try:
  >         frame = float(frame_str)
  >     except ValueError:
  >         return hwebserver.errorResponse(
  >             request, \\"Frame is not a number\\", 422)
  > 
  >     sop = hou.node(\\"/obj/geo1/testgeometry_crag1\\")
  >     if sop is None:
  >         sop = hou.node(\\"/obj\\").createNode(\\"geo\\").createNode(\\"testgeometry_crag\\")
  > 
  >     response = hwebserver.Response(
  >         sop.geometryAtFrame(frame).data(),
  >         content_type=\\"application/octet-stream\\"
  >     )
  >     response.setHeader(
  >         \\"Content-Disposition\\",
  >         \'attachment; filename=\\"crag_%s.bgeo\' % frame
  >     )
  >     return response

RELATED


    URLHandler

'''
def errorResponse(request: Request, error_message: str | dict[str, _JSONT] | list[_JSONT], status: int, use_heading: bool = False) -> Response:
    '''
hwebserver.errorResponse

Generates a Response object representing an HTTP error.

USAGE
  errorResponse(request, error_message, status, use_heading): ->


request
    The Request object passed to the URL handler or API function.

    (The function checks the request to see if the client wants a JSON
    response. If the client provided an Accept: application/json, */*
    header, this returns the JSON response {\\"error\\": error_message}, and
    error_message may be any JSON-encodable value.)

error_message
    Error message to display to the user.

    (This can be any JSON-encodable value if you know the response will
    be JSON rather than HTML.)

use_heading
    If the response is an HTML page (instead of JSON), automatically
    wrap the error_message in an <h1> element.

> import hou
> import hwebserver
> 
> 
> @hwebserver.urlHandler(\\"/node/info/\\", is_prefix=True)
> def node_info(request):
>     path = request.path()
>     assert path.startswith(\\"/node/info\\")
>     node_path = path[10:]
>     node = hou.node(node_path)
>     if node is None:
>         return hwebserver.errorResponse(request, \\"Resource not found\\", 404)
>     # ...

RELATED



'''
def notFoundResponse(request: Request) -> Response:
    '''
hwebserver.notFoundResponse

Generates a Response object representing a 404 Not Found HTTP error.

USAGE
  notFoundResponse(request): ->

This convenience function automatically sets the response code to 404
and generates an error message to indicate the requested resource was
not found or does not exist.

> import hou
> import hwebserver
> 
> 
> @hwebserver.urlHandler(\\"/node/info/\\", is_prefix=True)
> def node_info(request):
>     path = request.path()
>     assert path.startswith(\\"/node/info\\")
>     node_path = path[10:]
>     node = hou.node(node_path)
>     if node is None:
>         return hwebserver.notFoundResponse(request)
>     # ...

RELATED



'''
def redirect(request: Request, path: str, permanent: bool = False) -> Response:
    """
hwebserver.redirect

Generates a Response object representing a 301 Moved or 302 Found HTTP
response.

USAGE
  redirect(request, path, permanent=False): ->

The client must set the Host: HTTP header on the request for this to
work (browsers and other well-written clients will always do this, but
if you're writing your own lightweight client for some reason, you
should keep this in mind).


request
    The Request object passed to the URL handler or API function.

path
    The server path to redirect the client to.

permanent
    If True, the server returns HTTP status 301 Moved Permanently.
    Otherwise it returns 302 Found.

RELATED



"""
def fileResponse(file_path: str, content_type: str | None = None, delete_file: bool = False, download_as_filename: str | None = None) -> Response:
    '''
hwebserver.fileResponse

Generates a Response object that sends the contents of a file.

USAGE
  fileResponse(file_path, content_type=None, delete_file=False,
  download_as_filename=None): ->

  * Any time you are serving the contents of a file on disk, you should
    use this function instead of reading and returning the contents as a
    string.

  * For static files (such as for CSS, JavaScript, image, and video
    files),use to set up the server to automatically serve them instead
    of serving them in a Python handler. Serving static files using this
    approach is more performant and does not invoke Python.

  * The file\'s contents are not all loaded into memory at once.


file_path
    The file path of the file on disk to download to the client.

content_type
    The MIME content type of the response. If this is None (the
    default), the function uses mimetypes.guess_type() to guess the MIME
    type from the disk file\'s extension.

delete_file
    If this is True, the server deletes the file after sending it to the
    client. This is useful for temp files, but could be very dangerous
    if you change how the code works but forget to turn this off.

download_as_filename
    You can optionally supply the filename string the client will
    download the file as. The server will send a Content-Disposition
    header.

> import hou
> import hwebserver
> 
> 
> @hwebserver.urlHandler(\\"/textures\\", prefix=True)
> def texture_download(request):
>     path = request.path()
>     assert path.startswith(\\"/textures\\")
>     parm_name = path[10:]
>     if not parm_name:
>         return hwebserver.notFoundResponse(request)
> 
>     node = hou.node(\\"/mat/my_material\\")
>     texture_parm = node.parm(parm_name)
>     texture_path = texture_parm.evalAsString()
> 
>     return hwebserver.fileResponse(request, texture_path)

SERVING RELATIVE FILES

    Sometimes you want to serve files using a path relative to the
    Python script file containing the handler. Usually the __file__
    variable contains the path of the currently running file, so you can
    get the directory containing it using os.path.dirname(__file__).

    However, sometimes __file__ is not defined, such as when you launch
    Houdini from the command line with a Python script. To compensate
    for this, you can use the following function:


    webutils.py
      > import os
      > import inspect
      > 
      > 
      > def script_file_dir():
      >     try:
      >         file_path = __file__
      >     except NameError:
      >         file_path = inspect.getfile(inspect.currentframe())
      > 
      >     if not os.path.isabs(file_path):
      >         file_path = os.path.normpath(os.path.join(os.getcwd(), file_path))
      > 
      >     return os.path.dirname(file_path)

RENDERED IMAGE EXAMPLE

  > import os
  > import tempfile
  > import hou
  > import hwebserver
  > 
  > @hwebserver.urlHandler(\\"/tommy.jpg\\")
  > def tommy(request):
  >     \\"\\"\\"Render an image of the Tommy test geometry using Mantra.\\"\\"\\"
  >     rop = hou.node(\\"/out/tommy_rop\\")
  >     if rop is None:
  >         rop = create_tommy_scene()
  > 
  >     rop.render()
  >     return hwebserver.fileResponse(rop.evalParm(\\"vm_picture\\"))
  > 
  > def create_tommy_scene():
  >     sop = hou.node(\\"/obj\\").createNode(\\"geo\\").createNode(\\"testgeometry_tommy\\")
  > 
  >     cam = hou.node(\\"/obj\\").createNode(\\"cam\\", \\"tommy_cam\\")
  >     cam.parmTuple(\\"t\\").set((0, 1.3, 2.3))
  > 
  >     output_file = os.path.join(tempfile.gettempdir(), \\"tommy.jpg\\")
  >     rop = hou.node(\\"/out\\").createNode(\\"ifd\\", \\"tommy_rop\\")
  >     rop.parm(\\"camera\\").set(cam.path())
  >     rop.parm(\\"vobject\\").set(sop.parent().name())
  >     rop.parm(\\"vm_picture\\").set(output_file)
  > 
  >     return rop
    3D WEB VIEWER EXAMPLE

        This example uses the GLTF ROP to save the Crag test geometry to
        GTLF format and displays it in the browser using Babylon.js.


        server.py
          > import os
          > import tempfile
          > import json
          > 
          > import hou
          > import hwebserver
          > 
          > import webutils
          > 
          > 
          > OUTPUT_DIR = os.path.join(webutils.script_file_dir(), \\"static\\", \\"temp\\")
          > 
          > 
          > @hwebserver.urlHandler(\\"/\\")
          > def index_view(request):
          >     return hwebserver.redirect(request, \\"/static/index.html\\")
          > 
          > 
          > @hwebserver.urlHandler(\\"/static/output/model.gltf\\")
          > def gltf_view(request):
          >     frame = float(request.GET().get(\\"frame\\", 1))
          > 
          >     # Use the GLTF ROP to write to a temporary gltf file.  It will create
          >     # the .bin and any textures during the process.
          >     gltf_temp_file = temp_file_path(\\".gltf\\")
          >     hou.parm(\\"/out/gltf1/file\\").set(gltf_temp_file)
          >     hou.node(\\"/out/gltf1\\").render(frame_range=(frame, frame))
          > 
          >     # Note that we could read in the JSON and adjust URIs but we don\'t need to.
          >     return hwebserver.fileResponse(
          >         gltf_temp_file, \\"application/json\\",
          >         delete_file=True)
          > 
          > 
          > @hwebserver.urlHandler(\\"/static/output\\", is_prefix=True)
          > def temp_output(request):
          >     # This URL handler is used to serve the temporary .bin and texture files
          >     # for the GTLF.
          >     bin_file_path = os.path.join(OUTPUT_DIR, os.path.basename(request.path()))
          >     response = hwebserver.fileResponse(
          >         bin_file_path, \\"application/octet-stream\\",
          >         delete_file=True)
          >     return response
          > 
          > 
          > def temp_file_path(suffix):
          >     with tempfile.NamedTemporaryFile(
          >             dir=OUTPUT_DIR, suffix=suffix) as temp_file:
          >         return temp_file.name
          > 
          > 
          > def initialize_scene():
          >     hou.node(\\"/obj\\").createNode(\\"geo\\").createNode(\\"testgeometry_crag\\")
          >     hou.node(\\"/out\\").createNode(\\"gltf\\")
          > 
          > 
          > def run_server():
          >     if not os.path.exists(OUTPUT_DIR):
          >         os.makedirs(OUTPUT_DIR)
          >     initialize_scene()
          >     hwebserver.registerStaticFilesDirectory(
          >         os.path.join(webutils.script_file_dir(), \\"static\\"))
          >     hwebserver.run(8008, debug=True)
          > 
          > 
          > if __name__ == \\"__main__\\":
          >     run_server()
        static/index.html
          > <script src=\\"https://cdn.babylonjs.com/viewer/babylon.viewer.js\\"></script>
          > <script src=\\"https://code.jquery.com/jquery-1.12.4.js\\"></script>
          > <script src=\\"/static/index.js\\"></script>
          > 
          > <babylon id=\\"babylon-viewer\\"></babylon>
          > <br>Frame <input onchange=\\"set_frame(parseInt(this.value, 10))\\"
          >     value=\\"1\\" size=\\"4\\">
        static/index.js
          > var app = {
          >     frame: 1,
          >     viewer: null,
          > };
          > 
          > BabylonViewer.viewerManager
          >     .getViewerPromiseById(\'babylon-viewer\').then(function (viewer)
          > {
          >     app.viewer = viewer;
          >     $(viewer.containerElement).css(\\"height\\", \\"90%\\");
          >     viewer.onEngineInitObservable.add(function (scene) {
          >         reload_model();
          >     });
          > });
          > 
          > function set_frame(frame)
          > {
          >     app.frame = frame;
          >     reload_model();
          > }
          > 
          > function reload_model()
          > {
          >     app.viewer.loadModel({url: \\"/static/output/model.gltf?frame=\\" + app.frame});
          > }

RELATED



'''
@typing.overload
def apiFunction(namespace: _APIFunction, return_binary: bool = ..., arg_types: _ArgTypes | None = ..., ports: _Ports = ...) -> None: ...
@typing.overload
def apiFunction(namespace: str | None = ..., return_binary: bool = ..., arg_types: _ArgTypes | None = ..., ports: _Ports = ...) -> Callable[[_APIFunction], None]: ...
def registerAPIFunction(name: str, function: _APIFunction, return_binary: bool = False, arg_types: _ArgTypes | None = None, ports: _Ports = ...) -> None: ...
@typing.overload
def registerStaticFilesDirectory(directory: str) -> None: ...
@typing.overload
def registerStaticFilesDirectory(directory: str, url_prefix: str = ..., port_name: str = ..., cache_control: str = ...) -> None: ...
@typing.overload
def registerArchiveFile(archive_file: str, url_prefix: str) -> None: ...
@typing.overload
def registerArchiveFile(archive_file: str, url_prefix: str, port_name: str = ..., cache_control: str = ...) -> None: ...
@typing.overload
def setCORSWhitelist(whitelist: Sequence[str]) -> None: ...
@typing.overload
def setCORSWhitelist(whitelist: Sequence[str], port_name: str = ...) -> None: ...
@typing.overload
def setPortInfo(port_name: str, port: int, up_to_port: int, use_free_port_on_failure: bool, address: str, use_v6: bool, allowed_hosts: Sequence[str], use_xforwarded: bool, /) -> None: ...
@typing.overload
def setPortInfo(port_name: str, port: int, up_to_port: int, use_free_port_on_failure: bool, address: str, use_v6: bool, allowed_hosts: Sequence[str], use_xforwarded: bool) -> None: ...
@typing.overload
def setLogInfo(log_file: str, min_severity: webServerSeverity) -> None: ...
@typing.overload
def setLogInfo(log_file: str, min_severity: webServerSeverity, port_name: str = ...) -> None: ...
@typing.overload
def setSSL(port_name: str, certificate: str, certificate_key: str, dh_param: str, verify_peer: bool, /) -> None: ...
@typing.overload
def setSSL(port_name: str, certificate: str, certificate_key: str, dh_param: str, verify_peer: bool) -> None: ...
@typing.overload
def setSecurity(port_name: str, redirect: bool, redirect_exempt: Sequence[str], redirect_host: str, sts_seconds: int, sts_include_subdomains: bool, sts_preload: bool, no_sniff: bool, referrer_policy: Sequence[str], cross_origin_opener_policy: str, /) -> None: ...
@typing.overload
def setSecurity(port_name: str, redirect: bool, redirect_exempt: Sequence[str], redirect_host: str, sts_seconds: int, sts_include_subdomains: bool, sts_preload: bool, no_sniff: bool, referrer_policy: Sequence[str], cross_origin_opener_policy: str) -> None: ...
@typing.overload
def findHandlerForPort(method: str, path: str) -> PyURLHandler | None: ...
@typing.overload
def findHandlerForPort(method: str, path: str, port_name: str = ...) -> PyURLHandler | None: ...
@typing.overload
def insertHandlerForPort(handler: PyURLHandler) -> None: ...
@typing.overload
def insertHandlerForPort(handler: PyURLHandler, port_name: str = ...) -> None: ...
@typing.overload
def insertWebSocketForPort(creator: Callable[[], WebSocket], path: str) -> None: ...
@typing.overload
def insertWebSocketForPort(creator: Callable[[], WebSocket], path: str, is_prefix: bool = ..., port_name: str = ...) -> None: ...
def isInDebugMode() -> bool:
    """
hwebserver.isInDebugMode

Returns True if Houdini's web server was started in debug mode
debug=True in )

USAGE
  isInDebugMode() -> bool

RELATED



"""
def requestShutdown() -> None:
    """
hwebserver.requestShutdown

Tells Houdini's web server to shut down after serving all open requests.

USAGE
  requestShutdown()

Call this function from a URL handler or API function to tell the server
to shut down when it is finished handling all active requests. This
function returns immediately.

You can use this function along with a supervisor process that restarts
hython to periodically free up the memory consumed by the Houdini
session.

"""

class APIUrlHandler(URLHandler):
    def __init__(self) -> None: ...
    def insertFunction(self, name: str, function: _APIFunction) -> None: ...

class FileWrapper:
    filelike: SupportsRead[bytes]
    blksize: int
    close: Callable[[], object]
    def __init__(self, filelike: SupportsRead[bytes], bulksize: int = 8196) -> None: ...
    def __getitem__(self, key: int) -> bytes: ...

def registerWSGIApp(application: WSGIApplication, path: str, ports: _Ports = ...) -> None:
    '''
hwebserver.registerWSGIApp

Function used to register a wsgi capable application such as django to
be used on a path prefix.

USAGE
  registerWSGIApp(application=(), path=None, ports=[])

This function allows you to hook in a wsgi capable application such as
flask or django and use the houdini web server as the server backend.

> import os
> import hwebserver
> import testsite.wsgi
> 
> hwebserver.registerWSGIApp(testsite.wsgi.application, \\"/\\")
> hwebserver.run(8000, debug=True)

NOTE
    Currently multi part form requests are not fully supported with
    wsgi. If you need to use these requests you can continue to use hou
    url handlers.

'''

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
    @typing.overload
    def __init__(self, path: str, allows_partial: bool = ...) -> None: ...
    @typing.overload
    def __init__(self, path: str, methods: Sequence[str], allows_partial: bool = ...) -> None: ...
    async def handle(self, request: Request) -> None: ...

def registerASGIApp(application: _ASGIApplication, path: str, ports: Sequence[str] = ...) -> None:
    '''
hwebserver.registerASGIApp

Function used to register a asgi capable application such as django to
be used on a path prefix.

USAGE
  registerASGIApp(application=(), path=None, ports=[])

This function allows you to hook in a asgi capable application such as
flask or django and use the Houdini web server as the server backend.

> import os
> import hwebserver
> import testsite.asgi
> 
> hwebserver.registerWSGIApp(testsite.asgi.application, \\"/\\")
> hwebserver.run(8000, debug=True)

NOTE
    Currently HTTP is only supported and this feature is currently in
    Alpha.

'''
