import collections.abc
import typing
T = typing.TypeVar('T')

__version_info__: tuple

class VoidPtr:
    def __init__(self, *args, **kwargs) -> None: ...
    def toBytes(self, *args, **kwargs): ...
    def __eq__(self, other: object) -> bool: ...
    def __ge__(self, other: object) -> bool: ...
    def __gt__(self, other: object) -> bool: ...
    def __int__(self) -> int: ...
    def __le__(self, other: object) -> bool: ...
    def __len__(self) -> int: ...
    def __lt__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...

def _unpickle_enum(*args, **kwargs): ...
def createdByPython(*args, **kwargs): ...
def delete(*args, **kwargs): ...
def dump(*args, **kwargs): ...
def getAllValidWrappers(*args, **kwargs): ...
def getCppPointer(*args, **kwargs): ...
def invalidate(*args, **kwargs): ...
def isValid(*args, **kwargs): ...
def ownedByPython(*args, **kwargs): ...
def wrapInstance(*args, **kwargs): ...

class Object:
    pass