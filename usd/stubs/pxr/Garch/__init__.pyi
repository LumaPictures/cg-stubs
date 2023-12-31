# mypy: disable-error-code="misc, override, no-redef"

import Boost.Python

__MFB_FULL_PACKAGE_NAME: str

class GLPlatformDebugContext(Boost.Python.instance):
    def __init__(self, arg2: int, arg3: int, arg4: bool, arg5: bool) -> None: ...
    def makeCurrent(self) -> None: ...
    def __bool__(self) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    def __lt__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    @property
    def expired(self): ...
