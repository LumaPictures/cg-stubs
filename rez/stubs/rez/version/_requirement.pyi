import rez.version._requirement
import rez.version._version
from _typeshed import Incomplete
from rez.version._util import _Common as _Common
from rez.version._version import Version as Version, VersionRange as VersionRange
from typing import Iterator

class VersionedObject(_Common):
    """Definition of a versioned object, eg ``foo-1.0``.

    ``foo`` is also a valid object definiton. When there is no version part, we
    are defining an unversioned object.

    .. note::
        Note that ``-``, ``@`` or ``#`` can be used as the seperator between object name
        and version, however this is purely cosmetic. ``foo-1`` is the same as ``foo@1``.
    """
    sep_regex_str: str
    sep_regex: Incomplete
    name_: str
    version_: rez.version._version.Version
    sep_: str
    def __init__(self, s: str) -> None:
        """
        Args:
            s (str):
        """
    @classmethod
    def construct(cls, name: str, version: Version | None = None) -> VersionedObject:
        """Create a VersionedObject directly from an object name and version.

        Args:
            name (str): Object name string.
            version (typing.Optional[Version]): Version object.
        """
    @property
    def name(self) -> str:
        """Name of the object.

        Returns:
            str:
        """
    @property
    def version(self) -> Version:
        """Version of the object.

        Returns:
            Version:
        """
    def as_exact_requirement(self) -> str:
        """Get the versioned object, as an exact requirement string.

        Returns:
            str: Equivalent requirement string, eg ``maya==2016.1``
        """
    def __eq__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    def __str__(self) -> str: ...

class Requirement(_Common):
    '''
    Defines a requirement for an object. For example, ``foo-5+`` means that you
    require any version of ``foo``, version 5 or greater. An unversioned
    requirement can also be used (``foo``), this means you require any version of
    foo. You can drop the hyphen between object name and version range if the
    version range starts with a non-alphanumeric character - eg ``foo<2``.

    There are two different prefixes that can be applied to a requirement:

    - ``!``: The conflict requirement. This means that you require this version
      range of an object NOT to be present. To conflict with all versions of an
      object, use "!foo".
    - ``~``: This is known as a "weak reference", and means, "I do not require this
      object, but if present, it must be within this range." It is equivalent to
      the *conflict of the inverse* of the given version range.

    There is one subtle case to be aware of. ``~foo`` is a requirement that has no
    effect. It means "I do not require foo, but if foo is present, it can
    be any version." This statement is still valid, but will produce a
    Requirement object with a None range.

    Examples of valid requirement strings:

    - ``foo-1.0``
    - ``foo@1.0``
    - ``foo#1.0``
    - ``foo-1+``
    - ``foo-1+<4.3``
    - ``foo<3``
    - ``foo==1.0.1``
    '''
    sep_regex: Incomplete
    name_: str
    range_: rez.version._version.VersionRange | None
    negate_: bool
    conflict_: bool
    _str: str | None
    sep_: str
    def __init__(self, s: str | None, invalid_bound_error: bool = True) -> None:
        """
        Args:
            s (str): Requirement string
            invalid_bound_error (bool): If True, raise :exc:`VersionError` if an
                impossible range is given, such as ``3+<2``.
        """
    @classmethod
    def construct(cls, name: str, range: VersionRange | None = None) -> Requirement:
        """Create a requirement directly from an object name and VersionRange.

        Args:
            name (str): Object name string.
            range (typing.Optional[VersionRange]): If None, an unversioned requirement is
                created.
        """
    @property
    def name(self) -> str:
        """Name of the required object.

        Returns:
            str:
        """
    @property
    def range(self) -> VersionRange:
        """Version range of the requirement.

        Returns:
            VersionRange:
        """
    @property
    def conflict(self) -> bool:
        '''True if the requirement is a conflict requirement, eg "!foo", "~foo-1".

        Returns:
            bool:
        '''
    @property
    def weak(self) -> bool:
        '''True if the requirement is weak, eg "~foo".

        .. note::
            Note that weak requirements are also conflict requirements, but not
            necessarily the other way around.

        Returns:
            bool:
        '''
    def safe_str(self) -> str:
        """Return a string representation that is safe for the current filesystem,
        and guarantees that no two different Requirement objects will encode to
        the same value.

        Returns:
            str:
        """
    def conflicts_with(self, other: Requirement | VersionedObject) -> bool:
        """Returns True if this requirement conflicts with another :class:`Requirement`
        or :class:`VersionedObject`.

        Returns:
            bool:
        """
    def merged(self, other: Requirement) -> Requirement | None:
        """Merge two requirements.

        Two requirements can be in conflict and if so, this function returns
        None. For example, requests for ``foo-4`` and ``foo-6`` are in conflict,
        since both cannot be satisfied with a single version of foo.

        Some example successful requirements merges are:

        - ``foo-3+`` and ``!foo-5+`` == ``foo-3+<5``
        - ``foo-1`` and ``foo-1.5`` == ``foo-1.5``
        - ``!foo-2`` and ``!foo-5`` == ``!foo-2|5``

        Returns:
            Requirement: the merged result of two requirements.
        """
    def __eq__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    def __str__(self) -> str: ...

class RequirementList(_Common):
    """A list of requirements.

    This class takes a Requirement list and reduces it to the equivalent
    optimal form, merging any requirements for common objects. Order of objects
    is retained.
    """
    requirements_: list[rez.version._requirement.Requirement]
    conflict_: tuple[rez.version._requirement.Requirement, rez.version._requirement.Requirement] | None
    requirements_dict: dict[str, rez.version._requirement.Requirement]
    names_: set[str]
    conflict_names_: set[str]
    def __init__(self, requirements: list[Requirement]) -> None:
        """
        Args:
            requirements (list[Requirement]): List of requirements.
        """
    @property
    def requirements(self) -> list[Requirement]:
        """Returns optimised list of requirements, or None if there are
        conflicts.

        Returns:
            list[Requirement]:
        """
    @property
    def conflict(self) -> tuple[Requirement, Requirement] | None:
        """Get the requirement conflict, if any.

        Returns:
            typing.Optional[tuple[Requirement]]: None if there is no conflict, otherwise a
            2-tuple containing the conflicting requirement objects.
        """
    @property
    def names(self) -> set[str]:
        """Set of names of requirements, not including conflict requirements.

        Returns:
            set[str]:
        """
    @property
    def conflict_names(self) -> set[str]:
        """Set of conflict requirement names.

        Returns:
            set[str]:
        """
    def __iter__(self) -> Iterator[Requirement]: ...
    def get(self, name: str) -> Requirement | None:
        """Returns the requirement for the given object, or None.

        Args:
            name (str): requirement to get.

        Returns:
            Requirement:
        """
    def __eq__(self, other: object) -> bool: ...
    def __str__(self) -> str: ...
