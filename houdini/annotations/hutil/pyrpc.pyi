import abc
import io
import socket
import socketserver
import threading
import weakref
from collections.abc import Callable, Iterable
from types import BuiltinFunctionType, EllipsisType, NotImplementedType
from typing import Any, Self, TypeAlias

_Builtin: TypeAlias = "type | BuiltinFunctionType | bool | EllipsisType | NotImplementedType | None"
_Marshalled: TypeAlias = "int | float | str | InvalidSession | BoxedToObjectProxy | BoxedToClassProxy | BoxedFromProxy | _Builtin | tuple[_Marshalled, ...] | frozenset[_Marshalled]"
_AnyMessage: TypeAlias = "ReturnMessage | ImportModuleMessage | GetClassInfoMessage | DelProxyMessage | CallMessage | CallMethodMessage | CallUnboundMethodMessage | InstanceCheckMessage | DirMessage"

class Message:
    session: "Session"
    args: list[_Marshalled]
    arg_names: tuple[str, ...]
    type: int
    def __init__(self, session: "Session", *args: _Marshalled) -> None: ...
    def send_and_receive(self) -> Any: ...
    def send(self) -> None: ...
    @classmethod
    def receive(cls, session: "Session") -> _AnyMessage: ...

class ReturnMessage(Message):
    arg_names: tuple[str, ...]
    marshalled_value: _Marshalled
    is_exception: bool
    def extract_result(self) -> Any: ...

class ImportModuleMessage(Message):
    arg_names: tuple[str, ...]
    module_name: str
    def handle(self) -> ReturnMessage: ...

class GetClassInfoMessage(Message):
    arg_names: tuple[str, ...]
    class_object_id: int
    def handle(self) -> ReturnMessage: ...

class MessageOnObject(Message):
    arg_names: tuple[str, ...]
    object_id: int
    def handle(self) -> ReturnMessage: ...

class DelProxyMessage(MessageOnObject):
    def handle_ignoring_exceptions(self, ignored_obj: object) -> None: ...

class CallMessage(MessageOnObject):
    arg_names: tuple[str, ...]
    marshalled_args: tuple[_Marshalled, ...]
    marshalled_kwargs_items: tuple[tuple[str, _Marshalled], ...]
    def handle_ignoring_exceptions(self, obj: Callable[..., object], args: Iterable[object], kwargs_items: Iterable[tuple[str, object]]) -> Any: ...

class CallMethodMessage(MessageOnObject):
    arg_names: tuple[str, ...]
    method_name: str
    marshalled_args: tuple[_Marshalled, ...]
    def handle_ignoring_exceptions(self, obj: object, method_name: str, args: Iterable[object]) -> Any: ...

class CallUnboundMethodMessage(MessageOnObject):
    arg_names: tuple[str, ...]
    method_name: str
    marshalled_args: tuple[_Marshalled, ...]
    def handle_ignoring_exceptions(self, obj: object, method_name: str, args: Iterable[object]) -> Any: ...

class InstanceCheckMessage(MessageOnObject):
    arg_names: tuple[str, ...]
    marshalled_object: _Marshalled
    def handle_ignoring_exceptions(self, cls: type[object], obj: object) -> bool: ...

class DirMessage(MessageOnObject):
    arg_names: tuple[str, ...]
    def handle_ignoring_exceptions(self, obj: object) -> list[str]: ...

class RemoteObjectProxy:
    def __init__(self, session: "Session", remote_object_id: int) -> None: ...
    def __getattribute__(self, name: str) -> Any: ...
    def __setattr__(self, name: str, value: object) -> None: ...
    def __delattr__(self, name: str) -> None: ...
    def __dir__(self) -> list[str]: ...
    def __call__(self, *args: object, **kwargs: object) -> Any: ...

class RemoteClassProxy(abc.ABCMeta):
    def __getattribute__(cls, name: str) -> Any: ...
    def __setattr__(cls, name: str, value: object) -> None: ...
    def __delattr__(cls, name: str) -> None: ...
    def __instancecheck__(cls, obj: object) -> bool: ...

class Boxed:
    arg_names: tuple[str, ...]
    def __init__(self, *args: object) -> None: ...
    def encode(self, encoder: "DataSerializer") -> None: ...
    @classmethod
    def decode(cls, decoder: "DataSerializer") -> Self: ...
    def __repr__(self) -> str: ...

class BoxedToObjectProxy(Boxed):
    arg_names: tuple[str, ...]
    object_id: int
    class_object_id: int

class BoxedToClassProxy(Boxed):
    arg_names: tuple[str, ...]
    class_object_id: int

class BoxedFromProxy(Boxed):
    arg_names: tuple[str, ...]
    object_id: int

class InvalidSession(Exception):
    def __init__(self) -> None: ...

class ConnectionError(Exception):
    def __init__(self) -> None: ...

class Session:
    class ObjectAndCount:
        obj: Any
        count: int
        def __init__(self, obj: object) -> None: ...
        def __repr__(self) -> str: ...

    class RemoteClassInfo:
        class_name: str
        base_builtin_class: type[object]
        remote_object_proxy_constructor: type[RemoteObjectProxy]
        remote_class_proxy: RemoteClassProxy
        def __init__(self, session: "Session", class_object_id: int, class_name: str, base_builtin_class_name: str, special_method_names: Iterable[str]) -> None: ...

    sock: socket.socket
    objects: dict[int, "Session.ObjectAndCount"]
    classes: dict[int, type[object]]
    remote_object_proxies: weakref.WeakValueDictionary[int, RemoteObjectProxy]
    remote_class_infos: dict[int, "Session.RemoteClassInfo"]
    def __init__(self, sock: socket.socket) -> None: ...
    def marshal(self, obj: object) -> _Marshalled: ...
    def unmarshal(self, obj: _Marshalled) -> Any: ...
    def remove_object_by_id(self, object_id: int) -> None: ...
    def get_class_by_id(self, class_object_id: int) -> type[object]: ...

class DataSerializer:
    builtin_ids_to_names: dict[int, str]
    data_stream: io.StringIO | None
    encoding_methods: dict[type[object], Callable[[Any], object]]
    decoding_methods: dict[str, Callable[[], _Marshalled]]
    def __init__(self) -> None: ...
    def encode(self, obj: object) -> bytes: ...
    def encode_sub_object(self, obj: object) -> None: ...
    def decode_from_socket(self, sock: socket.socket) -> tuple[_Marshalled, ...]: ...
    def decode_sub_object(self) -> _Marshalled: ...

class RPCServer(socketserver.TCPServer):
    allow_reuse_address: bool
    def __init__(self, port: int) -> None: ...
    def finish_request(self, sock: socket.socket, client_address: tuple[str, int]) -> None: ...

def start_server(port: int = ..., use_thread: bool = ...) -> threading.Thread | None: ...
def import_remote_module(module_name: str, server_name: str = ..., port: int = ...) -> RemoteObjectProxy: ...
