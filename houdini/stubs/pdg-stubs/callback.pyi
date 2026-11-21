import _pdg
from typing import Any, NoReturn

from typing import TypeVar
from typing import TypeVar
_T = TypeVar('_T')
class PythonCallback:
    """
    Base class for all object that are created in Python, but owned and called
    from C++
    """
    def __init__(self, cpp_object: object) -> None:
        """
        __init__(self, object) -> NoneType

        Initializes the callback wrapper with an object created in C++
        """
    def __getitem__(self, key: str) -> _pdg.Port | _pdg._Attribute:
        """
        __getitem__(self, key) -> pdg.Port

        Returns a pdg.Port for the specified port name, using the implementation
        defined in C++
        """
    def __setitem__(self, key: str, value: object) -> None:
        """
        __setitem__(self, key, value) -> pdg.Port

        Set the pdg.Port with the specified port name, using the implementation
        defined in C++
        """
    def __iter__(self) -> NoReturn:
        """
        __iter__(self) -> None

        Iteration is not possible on a python callback, call into the C++
        iter implementation
        """
    def __rshift__(self, value: _T) -> _T:
        """
        __rshift__(self, value) -> pdg.Node

        Connects two nodes. Calls into the C++ bound object implementation.
        """
    def __dir__(self) -> list[str]:
        """
        __dir__(self) -> [str]

        Returns a list of attributes on the object
        """
    def __getattr__(self, attr_name: str) -> Any:
        """
        __getattr__(self, str) -> attr

        Called whenever the PythonCallback instance is missing an attribute.
        The attribute lookup is passed up to the wrapped C++ object. This
        allows seamless passthrough from  the wrapper to methods and
        properties on the underlying bound C++ object.
        """
    def __setattr__(self, attr_name: str, attr_val: object) -> None:
        """
        __setattr__(self, str, val) -> None

        Called whenever the PythonCallback instance should set an attribute.
        Attempts to forward the call on to the C++ base class, otherwise
        simply sets the attribute using the normal Python mechanism
        """
