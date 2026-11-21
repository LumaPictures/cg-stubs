import builtins
import json
import xmlrpc.client
from typing import Any, Generic, TypeAlias, overload

from typing_extensions import TypedDict, TypeVar

# Decoded RPC JSON: object_hook turns {"_bytes": ...} and {"_xmlrpclibBinary": ...} back into
# bytes and Binary.  It would also rebuild {"_klass": ...} objects, but only from this module's
# own globals, so in practice that raises KeyError.
_RpcJSON: TypeAlias = (
    bool
    | int
    | float
    | str
    | bytes
    | xmlrpc.client.Binary
    | list["_RpcJSON"]
    | dict[str, "_RpcJSON"]
    | None
)
_J = TypeVar("_J", default=_RpcJSON)

class _RpcCall(TypedDict):
    func: str | None
    args: tuple[Any, ...]

class _BytesJSON(TypedDict):
    _bytes: str

class _BinaryJSON(TypedDict):
    _xmlrpclibBinary: str

class _KlassInfo(TypedDict):
    name: str
    dict: builtins.dict[str, Any]

class _KlassJSON(TypedDict):
    _klass: _KlassInfo

class PDGNetRPCJsonEncoder(json.JSONEncoder):
    def default(self, obj: object) -> _BytesJSON | _BinaryJSON | _KlassJSON: ...

class PDGNetRPCJsonDecoder(json.JSONDecoder):
    def __init__(self, *args: object, **kwargs: Any) -> None: ...
    def object_hook(self, obj: dict[str, _RpcJSON]) -> _RpcJSON: ...

class PDGNetRPCJsonWrapper(Generic[_J]):
    encoder: type[json.JSONEncoder]
    decoder: type[json.JSONDecoder]
    @overload
    def __init__(
        self: "PDGNetRPCJsonWrapper[_RpcJSON]",
        encoder: type[json.JSONEncoder] = ...,
        decoder: type[PDGNetRPCJsonDecoder] = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: "PDGNetRPCJsonWrapper[Any]", encoder: type[json.JSONEncoder] = ..., *, decoder: type[json.JSONDecoder]
    ) -> None: ...
    @overload
    def __init__(
        self: "PDGNetRPCJsonWrapper[Any]", encoder: type[json.JSONEncoder], decoder: type[json.JSONDecoder]
    ) -> None: ...
    def __init__(
        self, encoder: type[json.JSONEncoder] = ..., decoder: type[json.JSONDecoder] = ...
    ) -> None: ...
    def rpcToDict(self, func_name: str | None, *args: object) -> _RpcCall: ...
    def dumps(self, object_: object) -> str: ...
    def loads(self, str_: str | bytes | bytearray) -> _J: ...
    def rpcToString(self, func_name: str | None, *args: object) -> str: ...
    def stringToJson(self, json_str: str | bytes | bytearray) -> _J: ...
    def rpcReplyToString(self, reply_data: object) -> str: ...
