# Houdini stubs generated from Houdini 22.0.466

import builtins
import typing
from _hashlib import HASH
from builtins import range
from collections.abc import Buffer, Callable, Iterable
from types import ModuleType
from typing import Protocol
from typing_extensions import TypeIs

__all__ = ['PBKDF2', 'crypt']

class _Crypt(Protocol):
    def __call__(self, word: str | builtins.bytes, salt: str | builtins.bytes | None = ..., iterations: int | None = ...) -> str: ...

__version__: str

def isunicode(s: object) -> TypeIs[str]: ...
def isbytes(s: object) -> TypeIs[builtins.bytes]: ...
def isinteger(n: object) -> TypeIs[int]: ...
def callable(obj: object) -> bool: ...
def b(s: str) -> builtins.bytes: ...
def binxor(a: Iterable[int], b: Iterable[int]) -> builtins.bytes: ...
@typing.overload
def b64encode(data: Buffer, chars: str = ...) -> str: ...
@typing.overload
def b64encode(data: Buffer, chars: builtins.bytes) -> builtins.bytes: ...
def b2a_hex(s: Buffer) -> str: ...

xrange: type[range]

class PBKDF2:
    """PBKDF2.py : PKCS#5 v2.0 Password-Based Key Derivation

    This implementation takes a passphrase and a salt (and optionally an
    iteration count, a digest module, and a MAC module) and provides a
    file-like object from which an arbitrarily-sized key can be read.

    If the passphrase and/or salt are unicode objects, they are encoded as
    UTF-8 before they are processed.

    The idea behind PBKDF2 is to derive a cryptographic key from a
    passphrase and a salt.

    PBKDF2 may also be used as a strong salted password hash.  The
    'crypt' function is provided for that purpose.

    Remember: Keys generated using PBKDF2 are only as strong as the
    passphrases they are derived from.
    """
    closed: bool
    crypt: _Crypt
    def __init__(self, passphrase: str | builtins.bytes, salt: str | builtins.bytes, iterations: int = 1000, digestmodule: str | ModuleType | Callable[[], HASH] = ..., macmodule: ModuleType = ...) -> None: ...
    def read(self, bytes: int) -> builtins.bytes:
        """Read the specified number of key bytes."""
    def hexread(self, octets: int) -> str:
        """Read the specified number of octets. Return them as hexadecimal.

        Note that len(obj.hexread(n)) == 2*n.
        """
    def close(self) -> None:
        """Close the stream."""

def crypt(word: str | builtins.bytes, salt: str | builtins.bytes | None = None, iterations: int | None = None) -> str:
    """PBKDF2-based unix crypt(3) replacement.

    The number of iterations specified in the salt overrides the 'iterations'
    parameter.

    The effective hash length is 192 bits.
    """
