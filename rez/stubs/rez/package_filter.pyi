import rez.version._requirement
from _typeshed import Incomplete
from rez.config import config as config
from rez.exceptions import ConfigurationError as ConfigurationError
from rez.packages import Package as Package, iter_packages as iter_packages
from rez.utils.data_utils import cached_class_property as cached_class_property, cached_property as cached_property
from rez.version import Requirement as Requirement, VersionRange as VersionRange, VersionedObject as VersionedObject
from typing import Any, Pattern, Self

class PackageFilterBase:
    """Base class for package filters."""
    def excludes(self, package: Package) -> Rule | None:
        """Determine if the filter excludes the given package.

        Args:
            package (Package): Package to filter.

        Returns:
            typing.Optional[Rule]: Rule object that excludes the package, or None if the package was
            not excluded.
        """
    def add_exclusion(self, rule: Rule):
        """Add an exclusion rule.

        Args:
            rule (Rule): Rule to exclude on.
        """
    def add_inclusion(self, rule: Rule):
        """Add an inclusion rule.

        Args:
            rule (Rule): Rule to include on.
        """
    @classmethod
    def from_pod(cls, data) -> None:
        """Convert from POD types to equivalent package filter."""
    def to_pod(self) -> None:
        """Convert to POD type, suitable for storing in an rxt file.

        Returns:
            dict[str, list[str]]:
        """
    def iter_packages(self, name: str, range_: VersionRange | str | None = None, paths: Incomplete | None = None):
        """Same as :func:`~rez.packages.iter_packages`, but also applies this filter.

        Args:
            name (str): Name of the package, eg 'maya'.
            range_ (VersionRange or str): If provided, limits the versions returned
                to those in ``range_``.
            paths (typing.Optional[list[str]]): paths to search for packages, defaults
                to :data:`packages_path`.

        Returns:
            typing.Iterator[Package]: iterator
        """
    @property
    def sha1(self) -> str:
        """
        SHA1 representation

        Returns:
            str:
        """
    def __repr__(self) -> str: ...

class PackageFilter(PackageFilterBase):
    """
    A package filter is a set of rules that hides some packages but leaves others
    visible. For example, a package filter might be used to hide all packages
    whos version ends in the string ``.beta``. A package filter might also be used
    simply to act as a blacklist, hiding some specific packages that are known
    to be problematic.

    Rules can be added as 'exclusion' or 'inclusion' rules. A package is only
    excluded if it matches one or more exclusion rules, and does not match any
    inclusion rules.
    """
    _excludes: dict[Any, Any]
    _includes: dict[Any, Any]
    def __init__(self) -> None: ...
    def excludes(self, package: Package) -> Rule | None: ...
    def add_exclusion(self, rule: Rule) -> None: ...
    def add_inclusion(self, rule: Rule) -> None: ...
    def copy(self) -> PackageFilter:
        """Return a shallow copy of the filter.

        Adding rules to the copy will not alter the source.
        """
    def __and__(self, other):
        """Combine two filters."""
    def __bool__(self) -> bool: ...
    @cached_property
    def cost(self):
        """Get the approximate cost of this filter.

        Cost is the total cost of the exclusion rules in this filter. The cost
        of family-specific filters is divided by 10.

        Returns:
            float: The approximate cost of the filter.
        """
    @classmethod
    def from_pod(cls, data):
        """Convert from POD types to equivalent package filter.

        Returns:
            PackageFilter:
        """
    def to_pod(self): ...
    def _add_rule(self, rules_dict, rule) -> None: ...
    def __str__(self) -> str: ...

class PackageFilterList(PackageFilterBase):
    """A list of package filters.

    A package is excluded by a filter list iff any filter within the list
    excludes it.
    """
    filters: list[Any]
    def __init__(self) -> None: ...
    def add_filter(self, package_filter: PackageFilter) -> None:
        """Add a filter to the list.

        Args:
            package_filter (`PackageFilter`): Filter to add.
        """
    def add_exclusion(self, rule: Rule) -> None: ...
    def add_inclusion(self, rule: Rule) -> None:
        """
        See also: :meth:`PackageFilterBase.add_inclusion`

        Note:
            Adding an inclusion to a filter list applies that inclusion across
            all filters.
        """
    def excludes(self, package: Package) -> Rule | None:
        """Returns the first rule that exlcudes ``package``, if any.

        Returns:
            Rule:
        """
    def copy(self) -> PackageFilterList:
        """Return a copy of the filter list.

        Adding rules to the copy will not alter the source.
        """
    @classmethod
    def from_pod(cls, data) -> PackageFilterList:  # type: ignore[override]
        """Convert from POD types to equivalent package filter.

        Returns:
            PackageFilterList:
        """
    def to_pod(self): ...
    def __bool__(self) -> bool: ...
    def __str__(self) -> str: ...
    @cached_class_property
    def singleton(cls):
        """Filter list as configured by :data:`package_filter`.

        Returns:
            PackageFilterList:
        """

no_filter: Incomplete

class Rule:
    """Base package filter rule"""
    name: str
    _family: str | None
    def match(self, package: Package) -> bool:
        """Apply the rule to the package.

        Args:
            package (Package): Package to filter.

        Returns:
            bool: True if the package matches the filter, False otherwise.
        """
    def family(self) -> str | None:
        """Returns a package family string if this rule only applies to a given
        package family, otherwise None.

        Returns:
            str | None:
        """
    def cost(self) -> None:
        """Relative cost of filter. Cheaper filters are applied first."""
    @classmethod
    def parse_rule(cls, txt: str):
        """Parse a rule from a string.

        See :data:`package_filter` for an overview of valid strings.

        Args:
            txt (str): String to parse.

        Returns:
            Rule:
        """
    @classmethod
    def _parse(cls, txt: str):
        """Create a rule from a string.

        Returns:
            `Rule` instance, or None if the string does not represent an instance
            of this rule type.
        """
    @classmethod
    def _parse_label(cls, txt: str): ...
    @classmethod
    def _extract_family(cls, txt: str) -> str | None: ...
    def __repr__(self) -> str: ...
    family_re: Incomplete
    label_re: Incomplete

class RegexRuleBase(Rule):
    regex: Pattern[str]
    txt: str
    def match(self, package: Package) -> bool: ...
    def cost(self) -> int: ...  # type: ignore[override]
    @classmethod
    def _parse(cls, txt: str) -> Self: ...
    def __str__(self) -> str: ...

class RegexRule(RegexRuleBase):
    """A rule that matches a package if its qualified name matches a regex string.

    For example, the package ``foo-1.beta`` would match the regex rule ``.*\\.beta$``.
    """
    name: str
    txt: Incomplete
    _family: Incomplete
    regex: Incomplete
    def __init__(self, s: str) -> None:
        """Create a regex rule.

        Args:
            s (str): Regex pattern. Eg ``.*\\.beta$``.
        """

class GlobRule(RegexRuleBase):
    """A rule that matches a package if its qualified name matches a glob string.

    For example, the package ``foo-1.2`` would match the glob rule ``foo-*``.
    """
    name: str
    txt: Incomplete
    _family: Incomplete
    regex: Incomplete
    def __init__(self, s: str) -> None:
        """Create a glob rule.

        Args:
            s (str): Glob pattern. Eg ``foo.*``, ``*.beta``.
        """

class RangeRule(Rule):
    """A rule that matches a package if that package does not conflict with a
    given requirement.

    For example, the package ``foo-1.2`` would match the requirement rule ``foo<10``.
    """
    name: str
    _requirement: rez.version._requirement.Requirement
    _family: Incomplete
    def __init__(self, requirement: Requirement) -> None: ...
    def match(self, package) -> bool: ...
    def cost(self) -> int: ...  # type: ignore[override]
    @classmethod
    def _parse(cls, txt: str) -> Self: ...
    def __str__(self) -> str: ...

class TimestampRule(Rule):
    """A rule that matches a package if that package was released before the
    given timestamp.

    Note:
        The ``timestamp`` argument used for resolves is ANDed with any package
        filters. Providing a filter containing timestamp rules does not override
        the value of ``timestamp``.

    Warning:
        Do NOT use a timestamp rule to mimic what the ``timestamp`` resolve argument
        does. ``timestamp`` is treated differently - the memcache caching system
        is aware of it, so timestamped resolves get cached. Non-timestamped
        resolves also get cached, but their cache entries are invalidated more
        often (when new packages are released).

        There is still a legitimate case to use a global timestamp rule though.
        You might want to ignore all packages released after time X, except for
        some specific packages that you want to let through. To do this you would
        create a package filter containing a timestamp rule with family=None,
        and other family-specific timestamp rules to override that.
    """
    name: str
    timestamp: int
    reverse: bool
    match_untimestamped: bool
    _family: Incomplete
    def __init__(self, timestamp: int, family: Incomplete | None = None, reverse: bool = False, match_untimestamped: bool = False) -> None:
        """Create a timestamp rule.

        Args:
            timestamp (int): Epoch time.
            family (str): Package family to apply the rule to.
            reverse (bool): If True, reverse the logic so that packages released
                *after* the timestamp are matched.
            match_untimestamped (bool): Defines behaviour on non-timestamped
                packages.
        """
    def match(self, package: Package) -> bool: ...
    def cost(self) -> int: ...  # type: ignore[override]
    @classmethod
    def after(cls, timestamp, family: Incomplete | None = None) -> Self: ...
    @classmethod
    def before(cls, timestamp, family: Incomplete | None = None) -> Self: ...
    @classmethod
    def _parse(cls, txt) -> Self: ...
    def __str__(self) -> str: ...
