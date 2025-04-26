import rez.version._version
import typing
from _typeshed import Incomplete
from rez.version._util import ParseException as ParseException, VersionError as VersionError, _Common as _Common, dedup as dedup
from typing import Any, Callable, Generic, Iterable, TypeVar
from typing_extensions import Self

T = TypeVar('T')
re_token: Incomplete

class _Comparable(_Common):
    def __gt__(self, other: object) -> bool: ...
    def __le__(self, other: object) -> bool: ...
    def __ge__(self, other: object) -> bool: ...

class _ReversedComparable(_Common):
    value: Any
    def __init__(self, value) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __lt__(self, other: object) -> bool: ...
    def __gt__(self, other: object) -> bool: ...
    def __le__(self, other: object) -> bool: ...
    def __ge__(self, other: object) -> bool: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...

class VersionToken(_Comparable):
    """Token within a version number.

    A version token is that part of a version number that appears between a
    delimiter, typically ``.`` or ``-``. For example, the version number ``2.3.07b``
    contains the tokens ``2``, ``3`` and ``07b`` respectively.

    Version tokens are only allowed to contain alphanumerics (any case) and
    underscores.
    """
    def __init__(self, token: str) -> None:
        '''
        Args:
            token (str): Token string, eg "rc02"
        '''
    @classmethod
    def create_random_token_string(cls) -> str:
        """Create a random token string. For testing purposes only.

        :meta private:
        """
    def less_than(self, other: VersionToken) -> bool:
        """Compare to another :class:`VersionToken`.

        Args:
            other (VersionToken): The VersionToken object to compare against.

        Returns:
            bool: True if this token is less than other, False otherwise.
        """
    def next(self) -> None:
        """Returns the next largest token."""
    def __str__(self) -> str: ...
    def __lt__(self, other): ...
    def __eq__(self, other) -> bool: ...

class NumericToken(VersionToken):
    """Numeric version token.

    Version token supporting numbers only. Padding is ignored.
    """
    n: int
    def __init__(self, token: str) -> None: ...
    @classmethod
    def create_random_token_string(cls) -> str: ...
    def __str__(self) -> str: ...
    def __eq__(self, other): ...
    def less_than(self, other: NumericToken) -> bool: ...  # type: ignore[override]
    def __next__(self): ...
    def next(self): ...

class _SubToken(_Comparable):
    """Used internally by AlphanumericVersionToken."""
    s: Any
    n: int | None
    def __init__(self, s) -> None: ...
    def __lt__(self, other): ...
    def __eq__(self, other): ...
    def __str__(self) -> str: ...

class AlphanumericVersionToken(VersionToken):
    """Alphanumeric version token.

    These tokens compare as follows:

    - each token is split into alpha and numeric groups (subtokens);
    - the resulting subtoken list is compared.
    - alpha comparison is case-sensitive, numeric comparison is padding-sensitive.

    Subtokens compare as follows:

    - alphas come before numbers;
    - alphas are compared alphabetically (``_``, then A-Z, then a-z);
    - numbers are compared numerically. If numbers are equivalent but zero-padded
      differently, they are then compared alphabetically. Thus ``01`` < ``1``.

    Some example comparisons that equate to true:

    - ``3`` < ``4``
    - ``01`` < ``1``
    - ``beta`` < ``1``
    - ``alpha3`` < ``alpha4``
    - ``alpha`` < ``alpha3``
    - ``gamma33`` < ``33gamma``
    """
    numeric_regex: Incomplete
    regex: Incomplete
    subtokens: list[rez.version._version._SubToken]
    def __init__(self, token: str) -> None: ...
    @classmethod
    def create_random_token_string(cls) -> str: ...
    def __str__(self) -> str: ...
    def __eq__(self, other): ...
    def less_than(self, other): ...
    def __next__(self): ...
    def next(self): ...
    @classmethod
    def _parse(cls, s: str) -> list[_SubToken]: ...

def reverse_sort_key(comparable):
    '''Key that gives reverse sort order on versions and version ranges.

    Example:

        >>> Version("1.0") < Version("2.0")
        True
        >>> reverse_sort_key(Version("1.0")) < reverse_sort_key(Version("2.0"))
        False

    Args:
        comparable (Version or VersionRange): Object to wrap.

    Returns:
        _ReversedComparable: Wrapper object that reverses comparisons.
    '''

class Version(_Comparable):
    """
    A Version is a sequence of zero or more version tokens, separated by either
    a dot ``.`` or hyphen ``-`` delimiters. Note that separators only affect Version
    objects cosmetically. In other words, the version ``1.0.0`` is equivalent to
    ``1-0-0``.

    The empty version ``''`` is the smallest possible version, and can be used to
    represent an unversioned resource.
    """
    inf: Version
    tokens: list[rez.version._version.VersionToken] | None
    seps: list[str | Any]
    _str: str | None
    _hash: int | None
    def __init__(self, ver_str: str | None = '', make_token=...) -> None:
        """
        Args:
            ver_str (str): Version string.
            make_token (typing.Callable[[str], None]): Callable that creates a VersionToken subclass from a
                string.
        """
    def copy(self) -> Version:
        """
        Returns a copy of the version.

        Returns:
            Version:
        """
    def trim(self, len_: int) -> Version:
        """Return a copy of the version, possibly with less tokens.

        Args:
            len_ (int): New version length. If >= current length, an
                unchanged copy of the version is returned.

        Returns:
            Version:
        """
    def __next__(self) -> Version:
        """Return :meth:`next` version. Eg, ``next(1.2)`` is ``1.2_``"""
    def next(self) -> Version: ...
    @property
    def major(self) -> VersionToken:
        """Semantic versioning major version.

        Returns:
            VersionToken: A VersionToken or a subclass of a VersionToken.
        """
    @property
    def minor(self) -> VersionToken:
        """Semantic versioning minor version.

        Returns:
            VersionToken: A VersionToken or a subclass of a VersionToken.
        """
    @property
    def patch(self) -> VersionToken:
        """Semantic versioning patch version.

        Returns:
            VersionToken: A VersionToken or a subclass of a VersionToken.
        """
    def as_tuple(self) -> tuple[str, ...]:
        '''Convert to a tuple of strings.

        Example:

            >>> print Version("1.2.12").as_tuple()
            (\'1\', \'2\', \'12\')

        Returns:
            tuple[str]:
        '''
    def __len__(self) -> int: ...
    def __getitem__(self, index: int) -> VersionToken: ...
    def __bool__(self) -> bool:
        """The empty version equates to False."""
    def __eq__(self, other: object) -> bool: ...
    def __lt__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    def __str__(self) -> str: ...

class _LowerBound(_Comparable):
    min: _LowerBound
    version: rez.version._version.Version
    inclusive: bool
    def __init__(self, version: Version, inclusive: bool) -> None: ...
    def __str__(self) -> str: ...
    def __eq__(self, other): ...
    def __lt__(self, other): ...
    def __hash__(self) -> int: ...
    def contains_version(self, version: Version) -> bool: ...

class _UpperBound(_Comparable):
    inf: _UpperBound
    version: rez.version._version.Version
    inclusive: bool
    def __init__(self, version: Version, inclusive: bool) -> None: ...
    def __str__(self) -> str: ...
    def __eq__(self, other): ...
    def __lt__(self, other): ...
    def __hash__(self) -> int: ...
    def contains_version(self, version: Version) -> bool: ...

class _Bound(_Comparable):
    any: _Bound
    lower: rez.version._version._LowerBound
    upper: rez.version._version._UpperBound
    def __init__(self, lower: _LowerBound | None = None, upper: _UpperBound | None = None, invalid_bound_error: bool = True) -> None: ...
    def __str__(self) -> str: ...
    def __eq__(self, other): ...
    def __lt__(self, other): ...
    def __hash__(self): ...
    def lower_bounded(self) -> bool: ...
    def upper_bounded(self) -> bool: ...
    def contains_version(self, version: Version) -> bool: ...
    def version_containment(self, version: Version) -> int: ...
    def contains_bound(self, bound: _Bound) -> bool: ...
    def intersects(self, other: _Bound) -> bool: ...
    def intersection(self, other: _Bound) -> _Bound | None: ...

def action(fn): ...

class _VersionRangeParser:
    debug: bool
    re_flags: Incomplete
    version_group: str
    version_range_regex: Incomplete
    regex: Incomplete
    make_token: Any
    _groups: dict[str, str | Any]
    _input_string: str
    bounds: list[Any]
    invalid_bound_error: bool
    def __init__(self, input_string: str, make_token, invalid_bound_error: bool = True) -> None: ...
    def _is_lower_bound_exclusive(self, token: str) -> bool: ...
    def _is_upper_bound_exclusive(self, token: str) -> bool: ...
    def _create_version_from_token(self, token: str) -> Version: ...
    @action
    def _act_version(self) -> None: ...
    @action
    def _act_exact_version(self) -> None: ...
    @action
    def _act_bound(self) -> None: ...
    @action
    def _act_lower_bound(self) -> None: ...
    @action
    def _act_upper_bound(self) -> None: ...
    @action
    def _act_lower_and_upper_bound_asc(self) -> None: ...
    @action
    def _act_lower_and_upper_bound_desc(self) -> None: ...

class VersionRange(_Comparable):
    '''
    A version range is a set of one or more contiguous ranges of versions. For
    example, "3.0 or greater, but less than 4" is a contiguous range that contains
    versions such as ``3.0``, ``3.1.0``, ``3.99`` etc. Version ranges behave something
    like sets. They can be intersected, added and subtracted, but can also be
    inverted. You can test to see if a :class:`Version` is contained within a :class:`VersionRange`.

    A VersionRange ``3`` (for example) is the superset of any version ``3[.X.X...]``.
    The version ``3`` itself is also within this range, and is smaller than ``3.0``.
    Any version with common leading tokens, but with a larger token count, is
    the larger version of the two.

    VersionRange objects have a flexible syntax that let you describe any
    combination of contiguous ranges, including inclusive and exclusive upper
    and lower bounds. This is best explained by example (those listed on the
    same line are equivalent):

    - ``3``: \'superset\' syntax, contains ``3``, ``3.0``, ``3.1.4`` etc;
    - ``2+``, ``>=2``: inclusive lower bound syntax, contains ``2``, ``2.1``, ``5.0.0`` etc;
    - ``>2``: exclusive lower bound;
    - ``<5``: exclusive upper bound;
    - ``<=5``: inclusive upper bound;
    - ``==2``: a range that contains only the exact single version ``2``.

    ..

    - ``1+<5``, ``>=1<5``: inclusive lower, exclusive upper. The most common form of
      a \'bounded\' version range (ie, one with a lower and upper bound);

    ..

    - ``>1<5``: exclusive lower, exclusive upper;
    - ``>1<=5``: exclusive lower, inclusive upper;
    - ``1+<=5``, ``1..5``: inclusive lower, inclusive upper;

    ..

    - ``<=4,>2``, ``<4,>2``, ``<4,>=2``: Reverse pip syntax (note comma)

    To help with readability, bounded ranges can also have their bounds separated
    with a comma, eg ``>=2,<=6``. The comma is purely cosmetic and is dropped in
    the string representation.

    To describe more than one contiguous range, seperate ranges with the or ``|``
    symbol. For example, the version range ``4|6+`` contains versions such as ``4``,
    ``4.0``, ``4.3.1``, ``6``, ``6.1``, ``10.0.0``, but does not contain any version
    ``5[.X.X...X]``. If you provide multiple ranges that overlap, they will be
    automatically optimised. For example, the version range ``3+<6|4+<8``
    becomes ``3+<8``.

    Note that the empty string version range represents the superset of all
    possible versions. This is called the "any" range. The empty version can
    also be used as an upper or lower bound, leading to some odd but perfectly
    valid version range syntax. For example, ``>`` is a valid range - read like
    ``>\'\'``, it means ``any version greater than the empty version``.
    '''
    _str: str | None
    bounds: list[rez.version._version._Bound]
    def __init__(self, range_str: str | None = '', make_token: type[VersionToken] = ..., invalid_bound_error: bool = True) -> None:
        '''
        Args:
            range_str (str): Range string, such as "3", "3+<4.5", "2|6+". The range
                will be optimised, so the string representation of this instance
                may not match range_str. For example, "3+<6|4+<8" == "3+<8".
            make_token (typing.Type[VersionToken]): Version token class to use.
            invalid_bound_error (bool): If True, raise an exception if an
                impossible range is given, such as \'3+<2\'.
        '''
    def is_any(self) -> bool:
        '''
        Returns:
            bool: True if this is the "any" range, ie the empty string range
            that contains all versions.
        '''
    def lower_bounded(self) -> bool:
        """
        Returns:
            bool: True if the range has a lower bound (that is not the empty
            version).
        """
    def upper_bounded(self) -> bool:
        """
        Returns:
            bool: True if the range has an upper bound.
        """
    def bounded(self) -> bool:
        """
        Returns:
            bool: True if the range has a lower and upper bound.
        """
    def issuperset(self, range) -> bool:
        """
        Returns:
            bool: True if the VersionRange is contained within this range.
        """
    def issubset(self, range) -> bool:
        """
        Returns:
            bool: True if we are contained within the version range.
        """
    def union(self, other: VersionRange | Iterable[VersionRange]) -> VersionRange:
        """OR together version ranges.

        Calculates the union of this range with one or more other ranges.

        Args:
            other (VersionRange or list[VersionRange]): Version range object(s) to OR with.

        Returns:
            VersionRange: Range object representing the union.
        """
    def intersection(self, other: VersionRange | Iterable[VersionRange]) -> VersionRange | None:
        """AND together version ranges.

        Calculates the intersection of this range with one or more other ranges.

        Args:
            other (VersionRange or list[VersionRange]): Version range object(s) to AND with.

        Returns:
            typing.Optional[VersionRange]: New VersionRange object representing the intersection, or None if
            no ranges intersect.
        """
    def inverse(self) -> VersionRange | None:
        """Calculate the inverse of the range.

        Returns:
            typing.Optional[VersionRange]: New VersionRange object representing the inverse of this range, or
            None if there is no inverse (ie, this range is the any range).
        """
    def intersects(self, other: VersionRange) -> bool:
        """Determine if we intersect with another range.

        Args:
            other (VersionRange): Version range object.

        Returns:
            bool: True if the ranges intersect, False otherwise.
        """
    def split(self) -> list[VersionRange]:
        '''Split into separate contiguous ranges.

        Returns:
            list[VersionRange]: A list of VersionRange objects. For example, the range ``3|5+`` will
            be split into ``["3", "5+"]``.
        '''
    @classmethod
    def as_span(cls, lower_version: Version | None = None, upper_version: Version | None = None, lower_inclusive: bool = True, upper_inclusive: bool = True):
        """Create a range from lower_version..upper_version.

        Args:
            lower_version (Version): Version object representing lower bound of the range.
            upper_version (Version): Version object representing upper bound of the range.
            lower_inclusive (bool): Include lower_version into the span.
            upper_inclusive (bool): Include upper_inclusive into the span.
        Returns:
            VersionRange:
        """
    @classmethod
    def from_version(cls, version: Version, op: str | None = None) -> Self:
        """Create a range from a version.

        Args:
            version (Version): This is used as the upper/lower bound of
                the range.
            op (typing.Optional[str]): Operation as a string. One of: gt, >, gte, >=, lt, <,
                lte, <=, eq, ==. If None, a bounded range will be created
                that contains the version superset.

        Returns:
            VersionRange:
        """
    @classmethod
    def from_versions(cls, versions: Iterable[Version]) -> VersionRange:
        """Create a range from a list of versions.

        This method creates a range that contains only the given versions and
        no other. Typically the range looks like (for eg) ``==3|==4|==5.1``.

        Args:
            versions (list[Version]): List of Version objects.

        Returns:
            VersionRange:
        """
    def to_versions(self) -> list[Version] | None:
        """Returns exact version ranges as Version objects, or None if there
        are no exact version ranges present.

        Returns:
            typing.Optional[list[Version]]:
        """
    def contains_version(self, version: Version) -> bool:
        """Returns True if version is contained in this range.

        Returns:
            bool:
        """
    def iter_intersect_test(self, iterable: Iterable[T], key: Callable[[T], Version] | None = None, descending: bool = False) -> _ContainsVersionIterator[T]:
        """Performs containment tests on a sorted list of versions.

        This is more optimal than performing separate containment tests on a
        list of sorted versions.

        Args:
            iterable: An ordered sequence of versioned objects. If the list
                is not sorted by version, behaviour is undefined.
            key (typing.Callable[typing.Any]): Function that returns a :class:`Version` given an object
                from ``iterable``. If None, the identity function is used.
            descending (bool): Set to True if ``iterable`` is in descending
                version order.

        Returns:
            ~collections.abc.Iterator[tuple[bool, typing.Any]]: An iterator that returns (bool, object) tuples,
            where 'object' is the original object in ``iterable``, and the bool indicates whether
            that version is contained in this range.
        """
    def iter_intersecting(self, iterable: Iterable[T], key: Callable[[T], Version] | None = None, descending: bool = False) -> _ContainsVersionIterator[T]:
        """Like :meth:iter_intersect_test`, but returns intersections only.

        Returns:
            An iterator that returns items from `iterable` that intersect.
        """
    def iter_non_intersecting(self, iterable: Iterable[T], key: Callable[[T], Version] | None = None, descending: bool = False) -> _ContainsVersionIterator[T]:
        """Like :meth:`iter_intersect_test`, but returns non-intersections only.

        Returns:
            An iterator that returns items from `iterable` that don't intersect.
        """
    def span(self) -> VersionRange:
        """Return a contiguous range that is a superset of this range.

        Returns:
            VersionRange: A range object representing the span of this range. For
            example, the span of ``2+<4|6+<8`` would be ``2+<8``.
        """
    def visit_versions(self, func) -> None:
        """Visit each version in the range, and apply a function to each.

        This is for advanced usage only.

        If ``func`` returns a :class:`Version`, this call will change the versions in
        place.

        It is possible to change versions in a way that is nonsensical - for
        example setting an upper bound to a smaller version than the lower bound.
        Use at your own risk.

        Args:
            func (typing.Callable[[Version], typing.Optional[Version]]): Takes a
                version, and is applied to every version in the range.
                If ``func`` returns a :class:`Version`, it will replace the existing version,
                updating this :class:`VersionRange` instance in place.

        Returns:
            None:
        """
    def __contains__(self, version_or_range: Version | VersionRange) -> bool: ...
    def __len__(self) -> int: ...
    def __invert__(self) -> VersionRange | None: ...
    def __and__(self, other) -> VersionRange | None: ...
    def __or__(self, other) -> VersionRange: ...
    def __add__(self, other) -> VersionRange: ...
    def __sub__(self, other) -> VersionRange | None: ...
    def __str__(self) -> str: ...
    def __eq__(self, other): ...
    def __lt__(self, other): ...
    def __hash__(self) -> int: ...
    def _contains_version(self, version: Version) -> tuple[int, bool]: ...
    @classmethod
    def _union(cls, bounds: list[_Bound]) -> list[_Bound]: ...
    @classmethod
    def _intersection(cls, bounds1: list[_Bound], bounds2: list[_Bound]) -> list[_Bound]: ...
    @classmethod
    def _inverse(cls, bounds: list[_Bound]) -> list[_Bound]: ...
    @classmethod
    def _issuperset(cls, bounds1: list[_Bound], bounds2: list[_Bound]) -> bool: ...
    @classmethod
    def _intersects(cls, bounds1: list[_Bound], bounds2: list[_Bound]) -> bool: ...

class _ContainsVersionIterator(Generic[T]):
    MODE_INTERSECTING: int
    MODE_NON_INTERSECTING: int
    MODE_ALL: int
    mode: Any
    range_: rez.version._version.VersionRange
    index: int | None
    nbounds: int
    _constant: bool | None
    fn: Callable[[rez.version._version.Version], bool]
    it: typing.Iterator[T]
    keyfunc: Callable[[T], rez.version._version.Version]
    next_fn: Callable[[], tuple[bool, T]] | Callable[[], T]
    def __init__(self, range_: VersionRange, iterable: Iterable[T], key: Callable[[T], Version] | None = None, descending: bool = False, mode=...) -> None: ...
    def __iter__(self) -> _ContainsVersionIterator[T]: ...
    def __next__(self) -> T | tuple[bool, T]: ...
    def next(self) -> T | tuple[bool, T]: ...
    def _next(self) -> tuple[bool, T]: ...
    def _next_intersecting(self) -> T: ...
    def _next_non_intersecting(self) -> T: ...
    @property
    def _bound(self) -> _Bound | None: ...
    def _ascending(self, version: Version) -> bool: ...
    def _descending(self, version: Version) -> bool: ...
