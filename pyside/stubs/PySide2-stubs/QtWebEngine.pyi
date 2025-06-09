import _typeshed
import collections
import shiboken2
import typing
T = typing.TypeVar('T')
import typing_extensions

class QtWebEngine(shiboken2.Object):
    @classmethod
    def __init__(cls, *args, **kwargs) -> None: ...
    @staticmethod
    def initialize() -> None: ...
