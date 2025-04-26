import rez.utils.resources
from _typeshed import Incomplete
from rez.config import config as config
from rez.exceptions import ResourceError as ResourceError
from rez.package_repository import PackageRepository as PackageRepository
from rez.utils.data_utils import AttributeForwardMeta as AttributeForwardMeta, LazyAttributeMeta as LazyAttributeMeta, cached_property as cached_property
from rez.utils.logging_ import print_debug as print_debug
from rez.vendor.schema.schema import Schema as Schema  # type: ignore[import-not-found]
from typing import Any, Self

class Resource(metaclass=LazyAttributeMeta):
    """Abstract base class for a data resource.

    A resource is an object uniquely identified by a 'key' (the resource type),
    and a dict of variables. For example, a very simple banking system might
    have a resource type with key 'account.checking', and a single variable
    'account_owner' that uniquely identifies each checking account.

    Resources may have a schema, which describes the data associated with the
    resource. For example, a checking account might have a current balance (an
    integer) and a social security number (also an integer).

    Keys in a resource's schema are mapped onto the resource class. So a
    checking account instance 'account' would have attributes 'account.balance',
    'account.ssn' etc. Attributes are lazily validated, using the schema, on
    first access.

    A resource's data is loaded lazily, on first attribute access. This,
    combined with lazy attribute validation, means that many resources can be
    iterated, while potentially expensive operations (data loading, attribute
    validation) are put off as long as possible.

    Note:
        You can access the entire validated resource data dict using the
        `validated_data` function, and test full validation using `validate_data`.
    """
    key: str
    schema: Schema | None
    schema_error = Exception
    _repository: PackageRepository
    @classmethod
    def normalize_variables(cls, variables):
        """Give subclasses a chance to standardize values for certain variables
        """
    variables: Any
    def __init__(self, variables: Incomplete | None = None) -> None: ...
    @cached_property
    def handle(self) -> ResourceHandle:
        """Get the resource handle."""
    @cached_property
    def _data(self): ...
    def get(self, key, default: Incomplete | None = None):
        """Get the value of a resource variable."""
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def __hash__(self): ...
    def __eq__(self, other): ...
    def _load(self) -> None:
        """Load the data associated with the resource.

        You are not expected to cache this data - the resource system does this
        for you.

        If `schema` is None, this signifies that the resource does not load any
        data. In this case you don't need to implement this function - it will
        never be called.

        Returns:
            dict.
        """

class ResourceHandle:
    """A `Resource` handle.

    A handle uniquely identifies a resource. A handle can be stored and used
    with a `ResourcePool` to retrieve the same resource at a later date.
    """
    key: str
    variables: Any | dict[Any, Any]
    def __init__(self, key: str, variables: Incomplete | None = None) -> None: ...
    def get(self, key, default: Incomplete | None = None):
        """Get the value of a resource variable."""
    def to_dict(self):
        """Serialize the contents of this resource handle to a dictionary
        representation.
        """
    @classmethod
    def from_dict(cls, d) -> Self:
        '''Return a `ResourceHandle` instance from a serialized dict

        This should ONLY be used with dicts created with ResourceHandle.to_dict;
        if you wish to create a "new" ResourceHandle, you should do it through
        PackageRepository.make_resource_handle
        '''
    def _hashable_repr(self): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def __eq__(self, other): ...
    def __ne__(self, other) -> bool: ...
    def __hash__(self): ...

class ResourcePool:
    """A resource pool.

    A resource pool manages a set of registered resource types, and acts as a
    resource cache. It will create any resource you ask for - typically
    resources are created via some factory class, which first checks for the
    existence of the resource before creating one from a pool.
    """
    resource_classes: dict[str, type[rez.utils.resources.Resource]]
    cached_get_resource: Any
    def __init__(self, cache_size: Incomplete | None = None) -> None: ...
    def register_resource(self, resource_class: type[Resource]) -> None: ...
    def get_resource_from_handle(self, resource_handle: ResourceHandle) -> Resource: ...
    def clear_caches(self) -> None: ...
    def get_resource_class(self, resource_key) -> type[Resource]: ...
    def _get_resource(self, resource_handle: ResourceHandle) -> Resource: ...

class ResourceWrapper(metaclass=AttributeForwardMeta):
    """An object that wraps a resource instance.

    A resource wrapper is useful for two main reasons. First, we can wrap
    several different resources with the one class, giving them a common
    interface. This is useful when the same resource can be loaded from various
    different sources (perhaps a database and the filesystem for example), and
    further common functionality needs to be supplied.

    Second, some resource attributes can be derived from the resource's
    variables, which means the resource's data doesn't need to be loaded to get
    these attributes. The wrapper can provide its own properties that do this,
    avoiding unnecessary data loads.

    You must subclass this class and provide `keys` - the list of attributes in
    the resource that you want to expose in the wrapper. The `schema_keys`
    function is provided to help get a list of keys from a resource schema.
    """
    keys: Incomplete
    wrapped: rez.utils.resources.Resource
    def __init__(self, resource: Resource) -> None: ...
    @property
    def resource(self) -> Resource: ...
    @property
    def handle(self) -> ResourceHandle: ...
    @property
    def data(self): ...
    def validated_data(self): ...
    def validate_data(self) -> None: ...
    def __eq__(self, other): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def __hash__(self): ...
