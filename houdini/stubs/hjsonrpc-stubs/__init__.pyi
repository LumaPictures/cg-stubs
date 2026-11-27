import http.server
import logging
from houtypes import JSONLike, JSONValue
from typing import Any, Protocol
from wsgiref.types import StartResponse, WSGIEnvironment as WSGIEnvironment

from typing import TypeVar
from collections.abc import Callable
from typing import TypeVar
_F = TypeVar('_F', bound=Callable[..., object])
class _RPCServiceHandler(Protocol):
    def handleRequest(self, json: str | bytes) -> bytes: ...

class RPCException(Exception):
    """This exception is raised to the RPC client when the called function
       raises an exception."""
    name: str | None
    def __init__(self, error: object) -> None: ...

class ServiceProxy:
    '''This class acts as both the proxy to a "module" of functions and as
       a proxy to an individual function.'''
    def __init__(self, service_url: str, timeout: float | None = None, method_name: str | None = None) -> None: ...
    def __getattr__(self, name: str) -> ServiceProxy: ...
    def __call__(self, *args: JSONLike) -> JSONValue: ...

class HTTPRequestHandlerHelper(http.server.BaseHTTPRequestHandler):
    """This class contains useful helper methods that would otherwise be
       duplicated in subclasses."""
    def readPostData(self) -> bytes: ...
    def sendResponse(self, code: int, content_type: str | None, response: bytes) -> None: ...
    def sendNotFound(self) -> None: ...

def rpcMethod(function: _F) -> _F:
    """Use this decorator on methods of the class providing the RPC
       functions."""

class _ServiceHandler:
    service: Any
    def __init__(self, service: Any) -> None: ...
    def handleRequest(self, json: str | bytes) -> bytes: ...

class RPCRequestHandler(HTTPRequestHandlerHelper):
    rpc_service_handler: _RPCServiceHandler
    rpc_path: str
    logger: logging.Logger | None
    def __init__(*args: Any) -> None:
        """All parameters but the last three are for
        BaseHTTPServer.BaseHTTPRequestHandler.  The last three are
        rpc_service_handler, rpc_path, and logger.  See createRPCServer for
        their descriptions.
        """
    def do_POST(self) -> None: ...
    def log_message(self, *args: object) -> None: ...
    def log_error(self, *args: object) -> None: ...
    def proxyToRPCService(self, url: str, service_name: str) -> bool:
        '''Act as a proxy to another RPC server, forwarding this request on.

        Returns a "Service Unavailable" HTTP status code if the service isn\'t
        running.  The service name is only used for error messages.
        '''
    def sendServiceUnavailable(self, service_name: str) -> None: ...

def createRPCServer(rpc_service: object, port: int, rpc_path: str = '/rpc', restrict_to_host: str = '', request_handler_class: type[RPCRequestHandler] = ..., logger: logging.Logger | None = None, fail_on_exception: bool = False) -> http.server.HTTPServer:
    '''Return a web server that will handle RPC requests and delegate them
    to rpc_service, an object whose methods are decorated with rpcMethod.

    port: The port on which the web server will run.
    rpc_path: The web server path that will respond to RPC server requests.
    restrict_to_host: "localhost" if the server should only respond to
        requests from the local machine, and "" if it should handle requests
        from any machine.
    request_handler_class: Either RPCRequestHandler or a subclass.  The server
        will create instances of this class to handle RPC requests.
    logger: The logging.Logger instance that will log messages, or None if
        they should be printed to stderr.  The messages are logged at the "info"
        level.
    fail_on_exception: Whether or not the handle_request call should raise an
        exception if one occurs while handling an RPC call.  If not, the
        traceback will simply be logged an the server will continue to run.
    '''

class WSGIApp:
    """A Web Server Gateway Interface that allows the RPC server to be plugged
    into a number of web servers and frameworks.
    """
    rpc_service_handler: _RPCServiceHandler
    def __init__(self, rpc_service: object) -> None: ...
    def __call__(self, environ: WSGIEnvironment, start_response: StartResponse) -> tuple[bytes | str]: ...
