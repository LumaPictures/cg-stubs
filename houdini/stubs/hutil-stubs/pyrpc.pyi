import abc
import io
import socket
import socketserver
import threading
import weakref
from collections.abc import Callable as Callable, Iterable
from types import BuiltinFunctionType as BuiltinFunctionType, EllipsisType as EllipsisType, NotImplementedType as NotImplementedType
from typing import Any, Self

from typing import TypeAlias
from typing import TypeAlias
_Builtin: TypeAlias = 'type | BuiltinFunctionType | bool | EllipsisType | NotImplementedType | None'
_Marshalled: TypeAlias = 'int | float | str | InvalidSession | BoxedToObjectProxy | BoxedToClassProxy | BoxedFromProxy | _Builtin | tuple[_Marshalled, ...] | frozenset[_Marshalled]'
_AnyMessage: TypeAlias = 'ReturnMessage | ImportModuleMessage | GetClassInfoMessage | DelProxyMessage | CallMessage | CallMethodMessage | CallUnboundMethodMessage | InstanceCheckMessage | DirMessage'
class ABCStubModule: ...

class Message:
    session: Session
    args: list[_Marshalled]
    arg_names: tuple[str, ...]
    type: int
    def __init__(self, session: Session, *args: _Marshalled) -> None: ...
    def send_and_receive(self) -> Any: ...
    def send(self) -> None: ...
    @classmethod
    def receive(cls, session: Session) -> _AnyMessage:
        """Build an instance of a Message subclass from the data decoded from
        the socket and handle that message.
        """

class ReturnMessage(Message):
    """Receiving this message unmarshals and returns its value, or raises
    an exception if it represents a raised exception.
    """
    marshalled_value: _Marshalled
    is_exception: bool
    arg_names: tuple[str, ...]
    def extract_result(self) -> Any: ...

class ImportModuleMessage(Message):
    """Import a remote module."""
    module_name: str
    arg_names: tuple[str, ...]
    def handle(self) -> ReturnMessage: ...

class GetClassInfoMessage(Message):
    """Return information about a remote class.  This message is invoked on
    with the class object's object id.
    """
    class_object_id: int
    arg_names: tuple[str, ...]
    def handle(self) -> ReturnMessage: ...

class MessageOnObject(Message):
    """A helper base class for messages involving a proxy to a remote object."""
    object_id: int
    arg_names: tuple[str, ...]
    def handle(self) -> ReturnMessage: ...

class DelProxyMessage(MessageOnObject):
    """Remove a proxy to a remote object."""
    def handle_ignoring_exceptions(self, ignored_obj: object) -> None: ...

class CallMessage(MessageOnObject):
    """Call an object."""
    marshalled_args: tuple[_Marshalled, ...]
    marshalled_kwargs_items: tuple[tuple[str, _Marshalled], ...]
    arg_names: tuple[str, ...]
    def handle_ignoring_exceptions(self, obj: Callable[..., object], args: Iterable[object], kwargs_items: Iterable[tuple[str, object]]) -> Any: ...

class CallMethodMessage(MessageOnObject):
    """Call a method on a object.

    This message is only used to invoke the __getattribute__, __setattr__, and
    __delattr__ methods.
    """
    method_name: str
    marshalled_args: tuple[_Marshalled, ...]
    arg_names: tuple[str, ...]
    def handle_ignoring_exceptions(self, obj: object, method_name: str, args: Iterable[object]) -> Any: ...

class CallUnboundMethodMessage(MessageOnObject):
    """Call a method on a object, explicitly passing in the object as the
    first parameter.

    This message is only used to invoke the __getattribute__, __setattr__, and
    __delattr__ methods.
    """
    method_name: str
    marshalled_args: tuple[_Marshalled, ...]
    arg_names: tuple[str, ...]
    def handle_ignoring_exceptions(self, obj: object, method_name: str, args: Iterable[object]) -> Any: ...

class InstanceCheckMessage(MessageOnObject):
    """Return whether a proxy to a remote object is an instance of a proxy
    to a remote class.  This message is invoked on the proxy to the remote
    class.
    """
    marshalled_object: _Marshalled
    arg_names: tuple[str, ...]
    def handle_ignoring_exceptions(self, cls: type[object], obj: object) -> bool: ...

class DirMessage(MessageOnObject):
    """Return the result of dir on the remote object."""
    arg_names: tuple[str, ...]
    def handle_ignoring_exceptions(self, obj: object) -> list[str]: ...

class RemoteObjectProxy:
    def __init__(self, session: Session, remote_object_id: int) -> None: ...
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
    def encode(self, encoder: DataSerializer) -> None: ...
    @classmethod
    def decode(cls, decoder: DataSerializer) -> Self: ...

class BoxedToObjectProxy(Boxed):
    """An object that exists on the server, boxed up to be sent to the client
    as a proxy.
    """
    object_id: int
    class_object_id: int
    arg_names: tuple[str, ...]

class BoxedToClassProxy(Boxed):
    """A class that exists on the server, boxed up to be sent to the client
    as a proxy.
    """
    class_object_id: int
    arg_names: tuple[str, ...]

class BoxedFromProxy(Boxed):
    """A proxy to an object that exists on the server, boxed up to be sent back
    to the server.
    """
    object_id: int
    arg_names: tuple[str, ...]

class InvalidSession(Exception):
    """This exception is raised when the client uses proxies from a different
    RPC Session.
    """
    def __init__(self) -> None: ...

class ConnectionError(Exception):
    def __init__(self) -> None: ...

class Session:
    """Both the client and the server create Session objects."""
    sock: socket.socket
    classes: dict[int, type[object]]
    remote_object_proxies: weakref.WeakValueDictionary[int, RemoteObjectProxy]
    class ObjectAndCount:
        """Stores an object and its reference count (i.e. the number of
        proxy objects on the client that refer to it.
        """
        obj: Any
        count: int
        def __init__(self, obj: object) -> None: ...
    class RemoteClassInfo:
        """Stores information about a class on the remote server, including
        how to construct a proxy for an instance of the class and for the
        class itself.
        """
        class_name: str
        base_builtin_class: type[object]
        remote_object_proxy_constructor: type[RemoteObjectProxy]
        remote_class_proxy: RemoteClassProxy
        def __init__(self, session: Session, class_object_id: int, class_name: str, base_builtin_class_name: str, special_method_names: Iterable[str]) -> None: ...
    objects: dict[int, 'Session.ObjectAndCount']
    remote_class_infos: dict[int, 'Session.RemoteClassInfo']
    def __init__(self, sock: socket.socket) -> None: ...
    def marshal(self, obj: object) -> _Marshalled:
        """Return an object that can be encoded by DataSerializer to be
        sent remotely.
        """
    def unmarshal(self, obj: _Marshalled) -> Any:
        """Given data decoded by DataSerializer, return a value to be
        used by the client.
        """
    def remove_object_by_id(self, object_id: int) -> None: ...
    def get_class_by_id(self, class_object_id: int) -> type[object]: ...

class DataSerializer:
    data_stream: io.StringIO | None
    encoding_methods: dict[type[object], Callable[[Any], object]]
    decoding_methods: dict[str, Callable[[], _Marshalled]]
    builtin_ids_to_names: dict[int, str]
    def __init__(self) -> None: ...
    def encode(self, obj: object) -> bytes: ...
    def encode_sub_object(self, obj: object) -> None: ...
    def decode_from_socket(self, sock: socket.socket) -> tuple[_Marshalled, ...]: ...
    def decode_sub_object(self) -> _Marshalled: ...

class RPCServer(socketserver.TCPServer):
    allow_reuse_address: bool
    def __init__(self, port: int) -> None: ...
    def finish_request(self, sock: socket.socket, client_address: tuple[str, int]) -> None: ...

def start_server(port: int = 10888, use_thread: bool = True) -> threading.Thread | None: ...
def import_remote_module(module_name: str, server_name: str = '127.0.0.1', port: int = 10888) -> RemoteObjectProxy: ...
