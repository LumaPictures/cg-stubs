# Houdini stubs generated from Houdini 22.0.466

from collections.abc import Sequence
from typing import Never, TypeAlias, Unpack

_PropertyValue: TypeAlias = (
    int | float | str | Sequence[int] | Sequence[float] | Sequence[str]
)
def property(*args: Unpack[tuple[str]], **kwargs: Never) -> list[int] | list[float] | list[str] | None:
    """Get the value of a string property"""
def setproperty(*args: Unpack[tuple[str, _PropertyValue]], **kwargs: Never) -> None:
    """Set a property value"""
