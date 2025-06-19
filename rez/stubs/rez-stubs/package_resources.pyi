import abc
from _typeshed import Incomplete
from abc import abstractmethod
from rez.config import Config as Config, config as config, create_config as create_config
from rez.exceptions import PackageMetadataError as PackageMetadataError, ResourceError as ResourceError
from rez.packages import Variant as Variant
from rez.utils.data_utils import AttributeForwardMeta as AttributeForwardMeta, LazyAttributeMeta as LazyAttributeMeta, cached_property as cached_property
from rez.utils.filesystem import find_matching_symlink as find_matching_symlink
from rez.utils.formatting import PackageRequest as PackageRequest
from rez.utils.logging_ import print_warning as print_warning
from rez.utils.resources import Resource as Resource
from rez.utils.schema import Required as Required, extensible_schema_dict as extensible_schema_dict, schema_keys as schema_keys
from rez.utils.sourcecode import SourceCode as SourceCode
from rez.vendor.schema.schema import And as And, Optional as Optional, Or as Or, Schema as Schema, SchemaError as SchemaError, Use as Use  # type: ignore[import-not-found]
from rez.version import Requirement as Requirement, Version as Version
from types import FunctionType, MethodType
from typing import Any, Iterator

package_release_keys: Incomplete
package_build_only_keys: Incomplete
package_rex_keys: Incomplete
help_schema: Incomplete
_is_late: Incomplete

def late_bound(schema): ...

late_requires_schema: Incomplete
base_resource_schema_dict: dict[Schema, Any]
package_family_schema_dict: Incomplete
tests_schema: Incomplete
package_base_schema_dict: Incomplete
package_schema_dict: Incomplete
variant_schema_dict: Incomplete
package_family_schema: Incomplete
package_schema: Incomplete
variant_schema: Incomplete
_commands_schema: Incomplete
_function_schema: Incomplete
_package_request_schema: Incomplete
package_pod_schema_dict: Incomplete
large_string_dict: Incomplete
package_pod_schema: Incomplete

class PackageRepositoryResource(Resource):
    """Base class for all package-related resources.
    """
    schema_error = PackageMetadataError
    repository_type: str
    @classmethod
    def normalize_variables(cls, variables): ...
    def __init__(self, variables: Incomplete | None = None) -> None: ...
    @cached_property
    def uri(self) -> str: ...
    @property
    def location(self) -> str | None: ...
    @property
    def name(self) -> str | None: ...
    def _uri(self) -> str:
        """Return a URI.

        Implement this function to return a short, readable string that
        uniquely identifies this resource.
        """

class PackageFamilyResource(PackageRepositoryResource):
    """A package family.

    A repository implementation's package family resource(s) must derive from
    this class. It must satisfy the schema `package_family_schema`.
    """
    def iter_packages(self) -> Iterator[PackageResourceHelper]: ...

class PackageResource(PackageRepositoryResource):
    """A package.

    A repository implementation's package resource(s) must derive from this
    class. It must satisfy the schema `package_schema`.
    """
    @classmethod
    def normalize_variables(cls, variables):
        """Make sure version is treated consistently
        """
    @cached_property
    def version(self) -> Version: ...

class VariantResource(PackageResource, metaclass=abc.ABCMeta):  # type: ignore[misc]
    """A package variant.

    A repository implementation's variant resource(s) must derive from this
    class. It must satisfy the schema `variant_schema`.

    Even packages that do not have a 'variants' section contain a variant - in
    this case it is the 'None' variant (the value of `index` is None). This
    provides some internal consistency and simplifies the implementation.
    """
    @property
    @abstractmethod
    def parent(self) -> PackageRepositoryResource: ...
    @property
    def index(self) -> int | None: ...
    @cached_property
    def root(self) -> str:
        """Return the 'root' path of the variant."""
    @cached_property
    def subpath(self) -> str:
        """Return the variant's 'subpath'

        The subpath is the relative path the variant's payload should be stored
        under, relative to the package base. If None, implies that the variant
        root matches the package base.
        """
    @abstractmethod
    def _root(self, ignore_shortlinks: bool = False): ...
    @abstractmethod
    def _subpath(self, ignore_shortlinks: bool = False): ...

class PackageResourceHelper(PackageResource, metaclass=abc.ABCMeta):  # type: ignore[misc]
    """PackageResource with some common functionality included.
    """
    variant_key: str
    _commands: list[str] | str | FunctionType | MethodType | SourceCode
    _pre_commands: list[str] | str | FunctionType | MethodType | SourceCode
    _post_commands: list[str] | str | FunctionType | MethodType | SourceCode
    variants: list[Variant]
    @property
    @abstractmethod
    def base(self) -> str | None: ...
    @property
    @abstractmethod
    def parent(self) -> PackageRepositoryResource: ...
    @cached_property
    def commands(self) -> SourceCode: ...
    @cached_property
    def pre_commands(self) -> SourceCode: ...
    @cached_property
    def post_commands(self) -> SourceCode: ...
    def iter_variants(self) -> Iterator[VariantResourceHelper]: ...
    def _convert_to_rex(self, commands: list[str] | str | FunctionType | MethodType | SourceCode) -> SourceCode: ...

class _Metas(AttributeForwardMeta, LazyAttributeMeta): ...

class VariantResourceHelper(VariantResource, metaclass=_Metas):  # type: ignore[misc]
    """Helper class for implementing variants that inherit properties from their
    parent package.

    Since a variant overlaps so much with a package, here we use the forwarding
    metaclass to forward our parent package's attributes onto ourself (with some
    exceptions - eg 'variants', 'requires'). This is a common enough pattern
    that it's supplied here for other repository plugins to use.
    """
    schema = variant_schema
    keys: Incomplete
    def _uri(self) -> str: ...
    def _subpath(self, ignore_shortlinks: bool = False) -> str | None: ...
    def _root(self, ignore_shortlinks: bool = False) -> str | None: ...
    @cached_property
    def variant_requires(self) -> list[Requirement]: ...
    @property
    def wrapped(self): ...
    def _load(self) -> None: ...
