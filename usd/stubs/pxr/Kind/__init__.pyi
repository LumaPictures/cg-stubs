# mypy: disable-error-code="misc, override, no-redef"

import Boost.Python
import pxr.Ar
from typing import ClassVar

__MFB_FULL_PACKAGE_NAME: str

class Registry(Boost.Python.instance):
    """
    A singleton that holds known kinds and information about them.


    See Kind Overview for a description of why kind exists, what the
    builtin registered kinds are, and how to extend the core kinds.

    KindRegistry Threadsafty
    ========================

    KindRegistry serves performance-critical clients that operate under
    the stl threading model, and therefore itself follows that model in
    order to avoid locking during HasKind() and IsA() queries.

    To make this robust, KindRegistry exposes no means to mutate the
    registry. All extensions must be accomplished via plugInfo.json files,
    which are consumed once during the registry initialization (See
    Extending the KindRegistry)
    """
    def __init__(self) -> None: ...
    @staticmethod
    def GetAllKinds() -> list[str]:
        """
        Return an unordered vector of all kinds known to the registry.
        """
    @staticmethod
    def GetBaseKind(_kind: str | pxr.Ar.ResolvedPath, /) -> str:
        """
        Return the base kind of the given kind.


        If there is no base, the result will be an empty token. Issues a
        coding error if *kind* is unknown to the registry.
        """
    @staticmethod
    def HasKind(_kind: str | pxr.Ar.ResolvedPath, /) -> bool:
        """
        Test whether *kind* is known to the registry.
        """
    @staticmethod
    def IsA(_derivedKind: str | pxr.Ar.ResolvedPath, _baseKind: str | pxr.Ar.ResolvedPath, /) -> bool:
        """
        Test whether *derivedKind* is the same as *baseKind* or has it as a
        base kind (either directly or indirectly).


        It is *not* required that *derivedKind* or *baseKind* be known to the
        registry: if they are unknown but equal, IsA will return C{true};
        otherwise if either is unknown, we will simply return false.

        Therefore this method will not raise any errors.
        """
    @classmethod
    def IsAssembly(cls, _kind: str | pxr.Ar.ResolvedPath, /) -> bool:
        """
        Return true if C{kind} IsA assembly kind.
        """
    @classmethod
    def IsComponent(cls, _kind: str | pxr.Ar.ResolvedPath, /) -> bool:
        """
        Returns true if C{kind} IsA component kind.
        """
    @classmethod
    def IsGroup(cls, _kind: str | pxr.Ar.ResolvedPath, /) -> bool:
        """
        Returns true if C{kind} IsA group kind.
        """
    @classmethod
    def IsModel(cls, _kind: str | pxr.Ar.ResolvedPath, /) -> bool:
        """
        Returns true if C{kind} IsA model kind.
        """
    @classmethod
    def IsSubComponent(cls, _kind: str | pxr.Ar.ResolvedPath, /) -> bool:
        """
        Returns true if C{kind} IsA subcomponent kind.
        """
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

class Tokens(Boost.Python.instance):
    assembly: ClassVar[str] = ...  # read-only
    component: ClassVar[str] = ...  # read-only
    group: ClassVar[str] = ...  # read-only
    model: ClassVar[str] = ...  # read-only
    subcomponent: ClassVar[str] = ...  # read-only
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """
