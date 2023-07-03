import collections.abc
import shiboken2
import typing
T = typing.TypeVar('T')

class QtWebEngine(shiboken2.Object):
    @classmethod
    def __init__(cls, *args, **kwargs) -> None: ...
    @classmethod
    def initialize(cls) -> None: ...