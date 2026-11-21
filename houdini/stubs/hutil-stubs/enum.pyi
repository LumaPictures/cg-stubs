# Houdini stubs generated from Houdini 22.0.466

from collections.abc import Iterator

class _EnumeratedValue:
    name: str
    value: int
    def __init__(self, name: str, value: int) -> None: ...

class Enumeration:
    enum_values: list[_EnumeratedValue]
    def __init__(self, *args: str) -> None:
        """Pass strings into __init__ containing the names of the enumerated
           values.
        """
    def __iter__(self) -> Iterator[_EnumeratedValue]: ...
    def __getitem__(self, index: int) -> _EnumeratedValue: ...
