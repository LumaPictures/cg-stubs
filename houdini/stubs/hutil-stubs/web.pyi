from collections.abc import Callable as Callable, Iterable, Mapping
from hutil import py23 as py23
from typing import Concatenate

def read_url_contents(url: str, post_data: bytes | None = None, extra_headers: Iterable[tuple[str, str]] = ..., require_content_length: bool = False, disable_proxy: bool = False) -> bytes | None:
    """Read the data at a URL.  Return None if the URL could not be read."""
def read_url(url: str, post_data: bytes | None = None, extra_headers: Iterable[tuple[str, str]] = ..., require_content_length: bool = False, timeout: float | None = None, disable_proxy: bool = False) -> tuple[int, str | None, bytes]:
    """Read the contents of a URL and return an (http_response_code,
    content_type, content) tuple.  If the connection generated a socket error
    then it raises urllib2.URLError.
    """
def save_url_to_file(url: str, file_name: str, post_data: bytes | None = None, extra_headers: Iterable[tuple[str, str]] = ..., progress_callback: Callable[Concatenate[int, int, ...], object] | None = None, callback_additional_kwargs: Mapping[str, object] = ..., disable_proxy: bool = False) -> None:
    """This helper function reads the contents of a URL and saves it to a file.

    On an error, it raises an urllib2.URLError exception.  Possible errors
    are a non-200 http response or a missing Content-Length header.

    If progress_callback is provided, it will be called periodically as follows:
        progress_callback(bytes_downloaded, total_num_bytes,
        callback_additional_kwargs)
    """

class FileArg:
    """This class provides a way for the user to encode a file when passed
    as a value into encode_multipart_form_data.
    """
    contents: bytes
    file_name: str
    content_type: str
    def __init__(self, contents: bytes, file_name: str, content_type: str = 'application/octet-stream') -> None: ...

def encode_multipart_form_data(fields: Iterable[tuple[str, str | FileArg]]) -> tuple[str, bytes]:
    """Given a sequence of (field_name, field_value) pairs, return a
    (content_type, post_data) tuple.  The content type header is
    necessary because it identifies the data as multipart/text and it
    contains the boundary.

    Note that field_value may be a FileArg instance.
    """
readURLContents = read_url_contents
readURL = read_url
