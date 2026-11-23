import http.client
import urllib.request
from collections.abc import Iterable
from typing import IO, ClassVar

from _typeshed import ReadableBuffer, SupportsRead

has_https: bool

class _StreamingHTTPMixin:
    def send(self, value: ReadableBuffer | SupportsRead[bytes] | Iterable[ReadableBuffer]) -> None: ...

class StreamingHTTPRedirectHandler(urllib.request.HTTPRedirectHandler):
    handler_order: ClassVar[int]
    def redirect_request(
        self,
        req: urllib.request.Request,
        fp: IO[bytes],
        code: int,
        msg: str,
        headers: http.client.HTTPMessage,
        newurl: str,
    ) -> urllib.request.Request: ...

class StreamingHTTPHandler(urllib.request.HTTPHandler):
    handler_order: ClassVar[int]
    def http_open(self, req: urllib.request.Request) -> http.client.HTTPResponse: ...
    def http_request(self, req: urllib.request.Request) -> urllib.request.Request: ...

class StreamingHTTPSHandler(urllib.request.HTTPSHandler):
    handler_order: ClassVar[int]
    def https_open(self, req: urllib.request.Request) -> http.client.HTTPResponse: ...
    def https_request(self, req: urllib.request.Request) -> urllib.request.Request: ...

def get_handlers() -> list[type[urllib.request.BaseHandler]]: ...
def register_openers() -> urllib.request.OpenerDirector: ...
