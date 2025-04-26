import rez.package_order
import rez.utils.typing
import rez.version._version
from _typeshed import Incomplete
from rez.config import config as config
from rez.packages import Package as Package, iter_packages as iter_packages
from rez.utils.data_utils import cached_class_property as cached_class_property
from rez.utils.typing import SupportsLessThan as SupportsLessThan
from rez.version import Version as Version, VersionRange as VersionRange
from rez.version._version import _Bound as _Bound, _Comparable as _Comparable, _LowerBound as _LowerBound, _ReversedComparable as _ReversedComparable, _UpperBound as _UpperBound
from typing import Any, Callable, Iterable, Self

ALL_PACKAGES: str

class FallbackComparable(_Comparable):
    """First tries to compare objects using the main_comparable, but if that
    fails, compares using the fallback_comparable object.
    """
    main_comparable: rez.utils.typing.SupportsLessThan
    fallback_comparable: rez.utils.typing.SupportsLessThan
    def __init__(self, main_comparable: SupportsLessThan, fallback_comparable: SupportsLessThan) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __lt__(self, other: object) -> bool: ...
    def __repr__(self) -> str: ...

class PackageOrder:
    """Package reorderer base class."""
    name: str
    _packages: list[str]
    def __init__(self, packages: Iterable[str] | None = None) -> None:
        """
        Args:
            packages: If not provided, PackageOrder applies to all packages.
        """
    @property
    def packages(self) -> list[str]:
        """Returns an iterable over the list of package family names that this
        order applies to

        Returns:
            (Iterable[str]) Package families that this orderer is used for
        """
    @packages.setter
    def packages(self, packages: str | Iterable[str] | None) -> None: ...
    def reorder(self, iterable: Iterable[Package], key: Callable[[Any], Package] | None = None) -> list[Package] | None:
        """Put packages into some order for consumption.

        You can safely assume that the packages referred to by `iterable` are
        all versions of the same package family.

        Note:
            Returning None, and an unchanged `iterable` list, are not the same
            thing. Returning None may cause rez to pass the package list to the
            next orderer; whereas a package list that has been reordered (even
            if the unchanged list is returned) is not passed onto another orderer.

        Args:
            iterable: Iterable list of packages, or objects that contain packages.
            key (typing.Callable[typing.Any, Package]): Callable, where key(iterable)
                gives a :class:`~rez.packages.Package`. If None, iterable is assumed
                to be a list of :class:`~rez.packages.Package` objects.

        Returns:
            list: Reordered ``iterable``
        """
    @staticmethod
    def _get_package_name_from_iterable(iterable: Iterable[Package], key: Callable[[Any], Package] | None = None) -> str | None:
        """Utility method for getting a package from an iterable"""
    def sort_key(self, package_name: str, version_like) -> SupportsLessThan:
        """Returns a sort key usable for sorting packages within the same family

        Args:
            package_name: (str) The family name of the package we are sorting
            version_like: (Version|_LowerBound|_UpperBound|_Bound|VersionRange|None)
                The version-like object to be used as a basis for generating a sort key.
                Note that 'None' is also a supported value, which maintains the default sorting order.

        Returns:
            Sortable object
                The returned object must be sortable, which means that it must implement __lt__.
                The specific return type is not important.
        """
    def sort_key_implementation(self, package_name: str, version: Version) -> SupportsLessThan:
        """Returns a sort key usable for sorting these packages within the
        same family
        Args:
            package_name: (str) The family name of the package we are sorting
            version: (Version) the version object you wish to generate a key for

        Returns:
            Sortable object
                The returned object must be sortable, which means that it must implement __lt__.
                The specific return type is not important.
        """
    def to_pod(self) -> None: ...
    @classmethod
    def from_pod(cls, data) -> PackageOrder: ...
    @property
    def sha1(self) -> str: ...
    def __str__(self) -> str: ...
    def __eq__(self, other): ...
    def __ne__(self, other) -> bool: ...
    def __repr__(self) -> str: ...

class NullPackageOrder(PackageOrder):
    """An orderer that does not change the order - a no op.

    This orderer is useful in cases where you want to apply some default orderer
    to a set of packages, but may want to explicitly NOT reorder a particular
    package. You would use a :class:`NullPackageOrder` in a :class:`PerFamilyOrder` to do this.
    """
    name: str
    def sort_key_implementation(self, package_name: str, version: Version) -> SupportsLessThan: ...
    def __str__(self) -> str: ...
    def __eq__(self, other): ...
    def to_pod(self) -> dict:  # type: ignore[override]
        '''
        Example (in yaml):

        .. code-block:: yaml

           type: no_order
           packages: ["foo"]
        '''
    @classmethod
    def from_pod(cls, data) -> Self: ...

class SortedOrder(PackageOrder):
    """An orderer that sorts based on :attr:`Package.version <rez.packages.Package.version>`.
    """
    name: str
    descending: bool
    def __init__(self, descending: bool, packages: Incomplete | None = None) -> None: ...
    def sort_key_implementation(self, package_name: str, version: Version) -> SupportsLessThan: ...
    def __str__(self) -> str: ...
    def __eq__(self, other): ...
    def to_pod(self) -> dict:  # type: ignore[override]
        '''
        Example (in yaml):

        .. code-block:: yaml

           type: sorted
           descending: true
           packages: ["foo"]
        '''
    @classmethod
    def from_pod(cls, data) -> Self: ...

class PerFamilyOrder(PackageOrder):
    """An orderer that applies different orderers to different package families.
    """
    name: str
    order_dict: dict[str, rez.package_order.PackageOrder]
    default_order: rez.package_order.PackageOrder | None
    def __init__(self, order_dict: dict[str, PackageOrder], default_order: PackageOrder | None = None) -> None:
        """Create a reorderer.

        Args:
            order_dict (dict[str, PackageOrder]): Orderers to apply to
                each package family.
            default_order (PackageOrder): Orderer to apply to any packages
                not specified in ``order_dict``.
        """
    def reorder(self, iterable: Iterable[Package], key: Callable[[Any], Package] | None = None) -> list[Package] | None: ...
    def sort_key_implementation(self, package_name: str, version: Version) -> SupportsLessThan: ...
    def __str__(self) -> str: ...
    def __eq__(self, other): ...
    def to_pod(self) -> dict:  # type: ignore[override]
        """
        Example (in yaml):

        .. code-block:: yaml

           type: per_family
           orderers:
           - packages: ['foo', 'bah']
             type: version_split
             first_version: '4.0.5'
           - packages: ['python']
             type: sorted
             descending: false
           default_order:
             type: sorted
             descending: true
        """
    @classmethod
    def from_pod(cls, data) -> Self: ...

class VersionSplitPackageOrder(PackageOrder):
    """Orders package versions <= a given version first.

    For example, given the versions [5, 4, 3, 2, 1], an orderer initialized
    with ``version=3`` would give the order [3, 2, 1, 5, 4].
    """
    name: str
    first_version: rez.version._version.Version
    def __init__(self, first_version: Version, packages: Incomplete | None = None) -> None:
        """Create a reorderer.

        Args:
            first_version (Version): Start with versions <= this value.
        """
    def sort_key_implementation(self, package_name: str, version: Version) -> SupportsLessThan: ...
    def __str__(self) -> str: ...
    def __eq__(self, other): ...
    def to_pod(self) -> dict:  # type: ignore[override]
        '''
        Example (in yaml):

        .. code-block:: yaml

           type: version_split
           first_version: "3.0.0"
           packages: ["foo"]
        '''
    @classmethod
    def from_pod(cls, data) -> Self: ...

class TimestampPackageOrder(PackageOrder):
    """A timestamp order function.

    Given a time ``T``, this orderer returns packages released before ``T``, in descending
    order, followed by those released after. If ``rank`` is non-zero, version
    changes at that rank and above are allowed over the timestamp.

    For example, consider the common case where we want to prioritize packages
    released before ``T``, except for newer patches. Consider the following package
    versions, and time ``T``:

    .. code-block:: text

       2.2.1
       2.2.0
       2.1.1
       2.1.0
       2.0.6
       2.0.5
             <-- T
       2.0.0
       1.9.0

    A timestamp orderer set to ``rank=3`` (patch versions) will attempt to consume
    the packages in the following order:

    .. code-block:: text

       2.0.6
       2.0.5
       2.0.0
       1.9.0
       2.1.1
       2.1.0
       2.2.1
       2.2.0

    Notice that packages before ``T`` are preferred, followed by newer versions.
    Newer versions are consumed in ascending order, except within rank (this is
    why 2.1.1 is consumed before 2.1.0).
    """
    name: str
    timestamp: int
    rank: int
    _cached_first_after: dict[Any, Any]
    _cached_sort_key: dict[Any, Any]
    def __init__(self, timestamp: int, rank: int = 0, packages: Incomplete | None = None) -> None:
        """Create a reorderer.

        Args:
            timestamp (int): Epoch time of timestamp. Packages before this time
                are preferred.
            rank (int): If non-zero, allow version changes at this rank or above
                past the timestamp.
        """
    def _get_first_after(self, package_family: str):
        """Get the first package version that is after the timestamp"""
    def _calc_first_after(self, package_family: str): ...
    def _calc_sort_key(self, package_name: str, version): ...
    def sort_key_implementation(self, package_name: str, version: Version) -> SupportsLessThan: ...
    def __str__(self) -> str: ...
    def __eq__(self, other): ...
    def to_pod(self) -> dict:  # type: ignore[override]
        '''
        Example (in yaml):

        .. code-block:: yaml

           type: soft_timestamp
           timestamp: 1234567
           rank: 3
           packages: ["foo"]
        '''
    @classmethod
    def from_pod(cls, data) -> Self: ...

class PackageOrderList(list[PackageOrder]):
    """A list of package orderer.
    """
    by_package: dict[str, rez.package_order.PackageOrder]
    dirty: bool
    def __init__(self, *args, **kwargs) -> None: ...
    def to_pod(self) -> list: ...
    @classmethod
    def from_pod(cls, data) -> PackageOrderList: ...
    @cached_class_property
    def singleton(cls) -> PackageOrderList:
        """Filter list as configured by rezconfig.package_filter."""
    @staticmethod
    def _to_orderer(orderer: dict | PackageOrder) -> PackageOrder: ...
    def refresh(self) -> None:
        """Update the internal order-by-package mapping"""
    def get(self, key: str, default: PackageOrder | None = None) -> PackageOrder | None:
        """
        Get an orderer that sorts a package by name.
        """

def to_pod(orderer: PackageOrder) -> dict: ...
def from_pod(data) -> PackageOrder: ...
def get_orderer(package_name, orderers: Incomplete | None = None): ...
def register_orderer(cls) -> bool:
    """Register an orderer

    Args:
        cls (type[PackageOrder]): Package orderer class to register.

    returns:
        bool: True if successfully registered, else False.
    """

_orderers: Incomplete
