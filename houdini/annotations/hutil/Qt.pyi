import types
from typing import NoReturn

__version__: str
__all__: list[str]
QT_VERBOSE: bool
QT_PREFERRED_BINDING: str
QT_SIP_API_HINT: str | None
Qt: types.ModuleType

class MissingMember:
    ERR_TMPL: str
    def __init__(self, name: str, details: str = ...) -> None: ...
    def __repr__(self) -> str: ...
    def __getattr__(self, name: str) -> NoReturn: ...
    def __call__(self, *a: object, **kw: object) -> NoReturn: ...
