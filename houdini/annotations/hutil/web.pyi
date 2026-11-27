from collections.abc import Callable, Iterable, Mapping
from typing import Concatenate

def read_url_contents(
    url: str,
    post_data: bytes | None = ...,
    extra_headers: Iterable[tuple[str, str]] = ...,
    require_content_length: bool = ...,
    disable_proxy: bool = ...,
) -> bytes | None: ...
def read_url(
    url: str,
    post_data: bytes | None = ...,
    extra_headers: Iterable[tuple[str, str]] = ...,
    require_content_length: bool = ...,
    timeout: float | None = ...,
    disable_proxy: bool = ...,
) -> tuple[int, str | None, bytes]: ...
def save_url_to_file(
    url: str,
    file_name: str,
    post_data: bytes | None = ...,
    extra_headers: Iterable[tuple[str, str]] = ...,
    progress_callback: Callable[Concatenate[int, int, ...], object] | None = ...,
    callback_additional_kwargs: Mapping[str, object] = ...,
    disable_proxy: bool = ...,
) -> None: ...

class FileArg:
    contents: bytes
    file_name: str
    content_type: str
    def __init__(self, contents: bytes, file_name: str, content_type: str = ...) -> None: ...

def encode_multipart_form_data(fields: Iterable[tuple[str, str | FileArg]]) -> tuple[str, bytes]: ...
