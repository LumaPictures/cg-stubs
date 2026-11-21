# Houdini stubs generated from Houdini 22.0.466

from collections.abc import Iterable
from collections.abc import Mapping
import typing
from collections.abc import Callable, Generator, Iterator, Sequence
from typing import IO
from typing_extensions import Self

from typing import TypeAlias
from typing import TypeAlias
_ParamValue: TypeAlias = 'str | IO[str] | MultipartParam'
_Params: TypeAlias = 'Mapping[str, _ParamValue] | Iterable[MultipartParam | tuple[str, _ParamValue]]'
__all__ = ['gen_boundary', 'encode_and_quote', 'MultipartParam', 'encode_string', 'encode_file_header', 'get_body_size', 'get_headers', 'multipart_encode']

def gen_boundary() -> str:
    """Returns a random string to use as the boundary for a message"""
@typing.overload
def encode_and_quote(data: None) -> None: ...
@typing.overload
def encode_and_quote(data: str | bytes) -> str: ...
def _strify(s: object) -> str | None:
    """If s is a unicode string, encode it to UTF-8 and return the results,
    otherwise return str(s), or None if s is None"""

class MultipartParam:
    '''Represents a single parameter in a multipart/form-data request

    ``name`` is the name of this parameter.

    If ``value`` is set, it must be a string or unicode object to use as the
    data for this parameter.

    If ``filename`` is set, it is what to say that this parameter\'s filename
    is.  Note that this does not have to be the actual filename any local file.

    If ``filetype`` is set, it is used as the Content-Type for this parameter.
    If unset it defaults to "text/plain; charset=utf8"

    If ``filesize`` is set, it specifies the length of the file ``fileobj``

    If ``fileobj`` is set, it must be a file-like object that supports
    .read().

    Both ``value`` and ``fileobj`` must not be set, doing so will
    raise a ValueError assertion.

    If ``fileobj`` is set, and ``filesize`` is not specified, then
    the file\'s size will be determined first by stat\'ing ``fileobj``\'s
    file descriptor, and if that fails, by seeking to the end of the file,
    recording the current position as the size, and then by seeking back to the
    beginning of the file.

    ``cb`` is a callable which will be called from iter_encode with (self,
    current, total), representing the current parameter, current amount
    transferred, and the total size.
    '''
    name: str
    value: str | None
    filename: str | None
    filetype: str | None
    filesize: int | None
    fileobj: IO[str] | None
    cb: Callable[[MultipartParam, int, int], object] | None
    def __init__(self, name: str, value: object = None, filename: str | None = None, filetype: str | None = None, filesize: int | None = None, fileobj: IO[str] | None = None, cb: Callable[[MultipartParam, int, int], object] | None = None) -> None: ...
    def __cmp__(self, other: MultipartParam) -> int: ...
    def reset(self) -> None: ...
    @classmethod
    def from_file(cls, paramname: str, filename: str) -> Self:
        """Returns a new MultipartParam object constructed from the local
        file at ``filename``.

        ``filesize`` is determined by os.path.getsize(``filename``)

        ``filetype`` is determined by mimetypes.guess_type(``filename``)[0]

        ``filename`` is set to os.path.basename(``filename``)
        """
    @classmethod
    def from_params(cls, params: _Params) -> list[Self]:
        """Returns a list of MultipartParam objects from a sequence of
        name, value pairs, MultipartParam instances,
        or from a mapping of names to values

        The values may be strings or file objects, or MultipartParam objects.
        MultipartParam object names must match the given names in the
        name,value pairs or mapping, if applicable."""
    def encode_hdr(self, boundary: str) -> str:
        """Returns the header of the encoding of this parameter"""
    def encode(self, boundary: str) -> str:
        """Returns the string encoding of this parameter"""
    def iter_encode(self, boundary: str, blocksize: int = 4096) -> Generator[str, None, None]:
        """Yields the encoding of this parameter
        If self.fileobj is set, then blocks of ``blocksize`` bytes are read and
        yielded."""
    def get_size(self, boundary: str) -> int:
        """Returns the size in bytes that this param will be when encoded
        with the given boundary."""

def encode_string(boundary: str, name: str, value: object) -> str:
    """Returns ``name`` and ``value`` encoded as a multipart/form-data
    variable.  ``boundary`` is the boundary string used throughout
    a single request to separate variables."""
def encode_file_header(boundary: str, paramname: str, filesize: int, filename: str | None = None, filetype: str | None = None) -> str:
    """Returns the leading data for a multipart/form-data field that contains
    file data.

    ``boundary`` is the boundary string used throughout a single request to
    separate variables.

    ``paramname`` is the name of the variable in this request.

    ``filesize`` is the size of the file data.

    ``filename`` if specified is the filename to give to this field.  This
    field is only useful to the server for determining the original filename.

    ``filetype`` if specified is the MIME type of this file.

    The actual file data should be sent after this header has been sent.
    """
def get_body_size(params: _Params, boundary: str) -> int:
    """Returns the number of bytes that the multipart/form-data encoding
    of ``params`` will be."""
def get_headers(params: _Params, boundary: str) -> dict[str, str]:
    """Returns a dictionary with Content-Type and Content-Length headers
    for the multipart/form-data encoding of ``params``."""

class multipart_yielder:
    params: Sequence[MultipartParam]
    boundary: str
    cb: Callable[[MultipartParam | None, int, int], object] | None
    i: int | None
    p: MultipartParam | None
    param_iter: Iterator[str] | None
    current: int
    total: int
    def __init__(self, params: Sequence[MultipartParam], boundary: str, cb: Callable[[MultipartParam | None, int, int], object] | None) -> None: ...
    def __iter__(self) -> Self: ...
    def __next__(self) -> str: ...
    def next(self) -> str:
        """generator function to yield multipart/form-data representation
        of parameters"""
    def reset(self) -> None: ...

def multipart_encode(params: _Params, boundary: str | None = None, cb: Callable[[MultipartParam | None, int, int], object] | None = None) -> tuple[multipart_yielder, dict[str, str]]:
    '''Encode ``params`` as multipart/form-data.

    ``params`` should be a sequence of (name, value) pairs or MultipartParam
    objects, or a mapping of names to values.
    Values are either strings parameter values, or file-like objects to use as
    the parameter value.  The file-like objects must support .read() and either
    .fileno() or both .seek() and .tell().

    If ``boundary`` is set, then it as used as the MIME boundary.  Otherwise
    a randomly generated boundary will be used.  In either case, if the
    boundary string appears in the parameter values a ValueError will be
    raised.

    If ``cb`` is set, it should be a callback which will get called as blocks
    of data are encoded.  It will be called with (param, current, total),
    indicating the current parameter being encoded, the current amount encoded,
    and the total amount to encode.

    Returns a tuple of `datagen`, `headers`, where `datagen` is a
    generator that will yield blocks of data that make up the encoded
    parameters, and `headers` is a dictionary with the assoicated
    Content-Type and Content-Length headers.

    Examples:

    >>> datagen, headers = multipart_encode( [("key", "value1"), ("key", "value2")] )
    >>> s = "".join(datagen)
    >>> assert "value2" in s and "value1" in s

    >>> p = MultipartParam("key", "value2")
    >>> datagen, headers = multipart_encode( [("key", "value1"), p] )
    >>> s = "".join(datagen)
    >>> assert "value2" in s and "value1" in s

    >>> datagen, headers = multipart_encode( {"key": "value1"} )
    >>> s = "".join(datagen)
    >>> assert "value2" not in s and "value1" in s

    '''
