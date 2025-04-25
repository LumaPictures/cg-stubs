from _typeshed import Incomplete
from rez.version import Requirement as Requirement, VersionRange as VersionRange
from typing import Any

class Binding:
    """Abstract base class.
    """
    _data: Any | dict[Any, Any]
    def __init__(self, data: Incomplete | None = None) -> None: ...
    def _attr_error(self, attr) -> None: ...
    def __getattr__(self, attr): ...

class VersionBinding(Binding):
    '''Binds a version.Version object.

    Examples:

        >>> v = VersionBinding(Version("1.2.3alpha"))
        >>> v.major
        1
        >>> v.patch
        \'3alpha\'
        >>> len(v)
        3
        >>> v[1]
        2
        >>> v[:3]
        (1, 2, \'3alpha\')
        >>> str(v)
        \'1.2.3alpha\'
        >>> print(v[5])
        None
        >>> v.as_tuple():
        (1, 2, \'3alpha\')
    '''
    __version: Any
    def __init__(self, version) -> None: ...
    @property
    def major(self): ...
    @property
    def minor(self): ...
    @property
    def patch(self): ...
    def as_tuple(self): ...
    def _attr_error(self, attr) -> None: ...
    def __getitem__(self, i): ...
    def __getitem(self, i): ...
    def __len__(self) -> int: ...
    def __str__(self) -> str: ...
    def __iter__(self): ...

class VariantBinding(Binding):
    """Binds a packages.Variant object.
    """
    __interpreter: Any
    __variant: Any
    __cached_root: Any
    def __init__(self, variant, cached_root: Incomplete | None = None, interpreter: Incomplete | None = None) -> None: ...
    @property
    def root(self):
        """
        This is here to support package caching. This ensures that references
        such as 'resolve.mypkg.root' resolve to the cached payload location,
        if the package is cached.
        """
    def __getattr__(self, attr): ...
    def _is_in_package_cache(self) -> bool: ...
    def _attr_error(self, attr) -> None: ...
    def __str__(self) -> str: ...

class RO_MappingBinding(Binding):
    """A read-only, dict-like object.
    """
    def __init__(self, data) -> None: ...
    def get(self, name, default: Incomplete | None = None): ...
    def __getitem__(self, name): ...
    def __contains__(self, name) -> bool: ...
    def __str__(self) -> str: ...

class VariantsBinding(RO_MappingBinding):
    """Binds a list of packages.VariantBinding objects, under the package name
    of each variant."""
    def __init__(self, variant_bindings) -> None: ...
    def _attr_error(self, attr) -> None: ...

class RequirementsBinding(RO_MappingBinding):
    """Binds a list of version.Requirement objects."""
    def __init__(self, requirements) -> None: ...
    def _attr_error(self, attr) -> None: ...
    def get_range(self, name, default: Incomplete | None = None):
        """Returns requirement version range object"""

class EphemeralsBinding(RO_MappingBinding):
    '''Binds a list of resolved ephemeral packages.

    Note:
        The leading \'.\' is implied when referring to ephemerals. Eg:

        .. code-block:: python

           # in package.py
           def commands():
               if "foo.cli" in ephemerals:  # will match \'.foo.cli-*\' request
    '''
    def __init__(self, ephemerals) -> None: ...
    def _attr_error(self, attr) -> None: ...
    def get_range(self, name, default: Incomplete | None = None):
        """Returns ephemeral version range object"""

def intersects(obj, range_):
    """Test if an object intersects with the given version range.

    Examples:

        .. code-block:: python

            # in package.py
            def commands():
                # test a request
                if intersects(request.maya, '2019+'):
                    info('requested maya allows >=2019.*')

                # tests if a resolved version intersects with given range
                if intersects(resolve.maya, '2019+')
                    ...

                # same as above
                if intersects(resolve.maya.version, '2019+')
                    ...

        .. code-block:: python

            # disable my cli tools if .foo.cli-0 was specified
            def commands():
                if intersects(ephemerals.get('foo.cli', '1'), '1'):
                    env.PATH.append('{root}/bin')

    Args:
        obj (VariantBinding or str): Object to test, either a
            variant, or requirement string (eg 'foo-1.2.3+').
        range_ (str): Version range, eg '1.2+<2'

    Returns:
        bool: True if the object intersects the given range.
    """
