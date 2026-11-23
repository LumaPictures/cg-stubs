from collections.abc import Callable as Callable
from typing import Generic

from typing import ParamSpec
from typing import TypeVar
from PySide6 import QtCore
from typing import ParamSpec
from typing import TypeVar
_T = TypeVar('_T', bound=QtCore.QObject)
_P = ParamSpec('_P')
class QtObjectHandle(Generic[_T]):
    """ A utility class for managing a qt object's life cycle
        based upon its number of references within python.

        When this is destroyed, there should be no python references left
        for the object and it will be marked for destruction.
    """
    def __init__(self, object_type: Callable[_P, _T], *args: _P.args, **kwargs: _P.kwargs) -> None:
        """ Initialize the handle and the corresponding object, given the input
            object type and its constructors arguments.
            :param object_type: Is the class of the object.
            :args: The arguments for the object's constructor
            :kwargs: The keyword arguments for the object's constructr
        """
    def __call__(self) -> _T:
        """ Calling this object returns the held Qt object
        """
    def __del__(self) -> None:
        """ When this handle is deleted, the corresponding Qt object will be marked
            for destruction.
        """
