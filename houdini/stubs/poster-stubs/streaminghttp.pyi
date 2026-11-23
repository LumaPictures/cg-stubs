import http.client
import urllib.request
from _typeshed import ReadableBuffer, SupportsRead
from collections.abc import Iterable
from typing import ClassVar, IO

__all__ = ['StreamingHTTPConnection', 'StreamingHTTPRedirectHandler', 'StreamingHTTPHandler', 'register_openers', 'StreamingHTTPSHandler', 'StreamingHTTPSConnection']

has_https: bool

class _StreamingHTTPMixin:
    """Mixin class for HTTP and HTTPS connections that implements a streaming
    send method."""
    def send(self, value: ReadableBuffer | SupportsRead[bytes] | Iterable[ReadableBuffer]) -> None:
        """Send ``value`` to the server.

        ``value`` can be a string object, a file-like object that supports
        a .read() method, or an iterable object that supports a .next()
        method.
        """

class StreamingHTTPConnection(_StreamingHTTPMixin, http.client.HTTPConnection):
    """Subclass of `httplib.HTTPConnection` that overrides the `send()` method
    to support iterable body objects"""

class StreamingHTTPRedirectHandler(urllib.request.HTTPRedirectHandler):
    """Subclass of `urllib2.HTTPRedirectHandler` that overrides the
    `redirect_request` method to properly handle redirected POST requests

    This class is required because python 2.5's HTTPRedirectHandler does
    not remove the Content-Type or Content-Length headers when requesting
    the new resource, but the body of the original request is not preserved.
    """
    handler_order: ClassVar[int]
    def redirect_request(self, req: urllib.request.Request, fp: IO[bytes], code: int, msg: str, headers: http.client.HTTPMessage, newurl: str) -> urllib.request.Request:
        """Return a Request or None in response to a redirect.

        This is called by the http_error_30x methods when a
        redirection response is received.  If a redirection should
        take place, return a new Request to allow http_error_30x to
        perform the redirect.  Otherwise, raise HTTPError if no-one
        else should try to handle this url.  Return None if you can't
        but another Handler might.
        """

class StreamingHTTPHandler(urllib.request.HTTPHandler):
    """Subclass of `urllib2.HTTPHandler` that uses
    StreamingHTTPConnection as its http connection class."""
    handler_order: ClassVar[int]
    def http_open(self, req: urllib.request.Request) -> http.client.HTTPResponse:
        """Open a StreamingHTTPConnection for the given request"""
    def http_request(self, req: urllib.request.Request) -> urllib.request.Request:
        """Handle a HTTP request.  Make sure that Content-Length is specified
        if we're using an interable value"""

class StreamingHTTPSConnection(_StreamingHTTPMixin, http.client.HTTPSConnection):
    """Subclass of `httplib.HTTSConnection` that overrides the `send()`
        method to support iterable body objects"""

class StreamingHTTPSHandler(urllib.request.HTTPSHandler):
    """Subclass of `urllib2.HTTPSHandler` that uses
        StreamingHTTPSConnection as its http connection class."""
    handler_order: ClassVar[int]
    def https_open(self, req: urllib.request.Request) -> http.client.HTTPResponse: ...
    def https_request(self, req: urllib.request.Request) -> urllib.request.Request: ...

def get_handlers() -> list[type[urllib.request.BaseHandler]]: ...
def register_openers() -> urllib.request.OpenerDirector:
    """Register the streaming http handlers in the global urllib2 default
    opener object.

    Returns the created OpenerDirector object."""
