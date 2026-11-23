import hjsonrpc
from collections.abc import Callable as Callable

from typing import TypeVar
from typing import TypeVar
_T = TypeVar('_T')
LOCAL_HOST: str

def start_server(api_class: Callable[[int], _T]) -> _T | None:
    """Start a server from inside Houdini, finding an available port, and
    process requests made to it from a new thread.

    api_class: An class with methods decorated with hjsonrpc.rpcMethod.  This
    function will create an instance of the class, passing in the port number.

    Returns an instance of the api_class, or None if all ports are in use.
    """
def port_range() -> list[int]:
    """Return the range of possible port numbers that instances of Houdini
    may be listening on.
    """
def connect_to_server(port: int, timeout: float = 5) -> hjsonrpc.ServiceProxy | None:
    """From a client, connect to a server on a specific port."""
def connect_to_any_server(timeout: float = 5) -> hjsonrpc.ServiceProxy | None:
    """From a client, try multiple ports to find a running instance of Houdini.
    
    Returns an hjsonrpc.ServiceProxy object on success, or None if no
    connection could be made.
    """
