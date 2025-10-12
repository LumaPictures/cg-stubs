import _typeshed
import collections
import shiboken2
import typing
import typing_extensions

T = typing.TypeVar('T')
P = typing.ParamSpec('P')
class QtWebEngine(shiboken2.Object):
    @classmethod
    def __init__(cls, *args, **kwargs) -> None: ...
    @staticmethod
    def initialize() -> None: ...
