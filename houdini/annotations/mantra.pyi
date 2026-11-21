from collections.abc import Sequence
from typing import Never, TypeAlias, Unpack

_PropertyValue: TypeAlias = (
    int | float | str | Sequence[int] | Sequence[float] | Sequence[str]
)

# None when there is no property of that name.
def property(
    *args: Unpack[tuple[str]], **kwargs: Never
) -> list[int] | list[float] | list[str] | None: ...
def setproperty(*args: Unpack[tuple[str, _PropertyValue]], **kwargs: Never) -> None: ...
