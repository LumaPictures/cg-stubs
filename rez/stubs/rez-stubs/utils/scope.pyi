from _typeshed import Incomplete
from collections import UserDict
from rez.utils.formatting import StringFormatMixin as StringFormatMixin, StringFormatType as StringFormatType
from typing import Any, Self

class RecursiveAttribute(UserDict, StringFormatMixin):
    """An object that can have new attributes added recursively::

        >>> a = RecursiveAttribute()
        >>> a.foo.bah = 5
        >>> a.foo['eek'] = 'hey'
        >>> a.fee = 1

        >>> print(a.to_dict())
        {'foo': {'bah': 5, 'eek': 'hey'}, 'fee': 1}

    A recursive attribute can also be created from a dict, and made read-only::

        >>> d = {'fee': {'fi': {'fo': 'fum'}}, 'ho': 'hum'}
        >>> a = RecursiveAttribute(d, read_only=True)
        >>> print(str(a))
        {'fee': {'fi': {'fo': 'fum'}}, 'ho': 'hum'}
        >>> print(a.ho)
        hum
        >>> a.new = True
        AttributeError: 'RecursiveAttribute' object has no attribute 'new'
    """
    format_expand: Incomplete
    def __init__(self, data: Incomplete | None = None, read_only: bool = False) -> None: ...
    def __getattr__(self, attr): ...
    def __setattr__(self, attr: str, value: Any) -> None: ...
    def __getitem__(self, attr: str) -> Any: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def _create_child_attribute(self, attr: str) -> RecursiveAttribute:
        """Override this method to create new child attributes.

        Returns:
            `RecursiveAttribute` instance.
        """
    def to_dict(self) -> dict[str, Any]:
        """Get an equivalent dict representation."""
    def copy(self) -> Self: ...
    def update(self, data: dict[str, Any]) -> None:  # type: ignore[override]
        """Dict-like update operation."""
    def _update(self, data: dict[str, Any]) -> None: ...
    def _reparent(self) -> None: ...

class _Scope(RecursiveAttribute):
    def __init__(self, name: str | None = None, context: ScopeContext | None = None) -> None: ...
    def __enter__(self) -> _Scope: ...
    def __exit__(self, *args: Any) -> None: ...
    def _create_child_attribute(self, attr: str) -> RecursiveAttribute: ...

class ScopeContext:
    '''A context manager for creating nested dictionaries::

        >>> scope = ScopeContext()
        >>>
        >>> with scope("animal"):
        >>>     count = 2
        >>>     with scope("cat"):
        >>>         friendly = False
        >>>     with scope("dog") as d:
        >>>         friendly = True
        >>>         d.num_legs = 4
        >>>         d.breed.sub_breed = \'yorkshire terrier\'
        >>> with scope("animal"):
        >>>     count = 3
        >>>     with scope("cat"):
        >>>         num_legs = 4
        >>>     with scope("ostrich"):
        >>>         friendly = False
        >>>         num_legs = 2

    The dictionaries can then be retrieved::

        >>> print(pprint.pformat(scope.to_dict()))
        {\'animal\': {\'count\': 3,
                    \'cat\': {\'friendly\': False,
                            \'num_legs\': 4},
                    \'dog\': {\'breed\': {\'sub_breed\': \'yorkshire terrier\'},
                            \'friendly\': True,
                            \'num_legs\': 4},
                    \'ostrich\': {\'friendly\': False,
                                \'num_legs\': 2}}}

    Note that scopes and recursive attributes can be referenced multiple times,
    and the assigned properties will be merged. If the same property is set
    multiple times, it will be overwritten.
    '''
    scopes: dict[Any, Any]
    scope_stack: list[_Scope]
    def __init__(self) -> None: ...
    def __call__(self, name: str) -> _Scope: ...
    def _scope_exit(self, name: str) -> None: ...
    def to_dict(self) -> dict[str, Any]:
        """Get an equivalent dict representation."""
    def __str__(self) -> str: ...

def scoped_formatter(**objects: Any) -> RecursiveAttribute:
    """Format a string with respect to a set of objects' attributes.

    Use this rather than `scoped_format` when you need to reuse the formatter.
    """
def scoped_format(txt: str, **objects: Any) -> str:
    '''Format a string with respect to a set of objects\' attributes.

    Example:

        >>> Class Foo(object):
        >>>     def __init__(self):
        >>>         self.name = "Dave"
        >>> print(scoped_format("hello {foo.name}", foo=Foo()))
        hello Dave

    Args:
        objects (dict): Dict of objects to format with. If a value is a dict,
            its values, and any further neted dicts, will also format with dot
            notation.
        pretty (bool): See `ObjectStringFormatter`.
        expand (bool): See `ObjectStringFormatter`.
    '''
