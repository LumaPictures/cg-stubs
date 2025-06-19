# mypy: disable-error-code="misc, override, no-redef"

import Boost.Python

__MFB_FULL_PACKAGE_NAME: str

class GLPlatformDebugContext(Boost.Python.instance):
    """
    Platform specific context (e.g.


    X11/GLX) which supports debug output.
    """
    def __init__(self, _majorVersion: int, _minorVersion: int, _coreProfile: bool, _directRenderering: bool, /) -> None: ...
    def makeCurrent(self) -> None: ...
    def __bool__(self) -> bool:
        """True if this object has not expired.  False otherwise."""
    def __eq__(self, other: object) -> bool:
        """Equality operator:  x == y"""
    def __lt__(self, other: object) -> bool:
        """Less than operator: x < y"""
    def __ne__(self, other: object) -> bool:
        """Non-equality operator: x != y"""
    @property
    def expired(self): ...
