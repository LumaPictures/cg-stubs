import rez.resolved_context
from _typeshed import Incomplete
from collections.abc import Generator
from rez.config import Config as Config, config as config
from rez.developer_package import DeveloperPackage as DeveloperPackage
from rez.exceptions import PackageFamilyNotFoundError as PackageFamilyNotFoundError, ResourceError as ResourceError
from rez.package_repository import PackageRepository as PackageRepository, package_repository_manager as package_repository_manager
from rez.package_resources import PackageFamilyResource as PackageFamilyResource, PackageResource as PackageResource, VariantResource as VariantResource, late_requires_schema as late_requires_schema, package_family_schema as package_family_schema, package_release_keys as package_release_keys, package_schema as package_schema, variant_schema as variant_schema
from rez.package_serialise import dump_package_data as dump_package_data
from rez.resolved_context import ResolvedContext as ResolvedContext
from rez.serialise import FileFormat as FileFormat
from rez.utils import reraise as reraise
from rez.utils.data_utils import cached_property as cached_property
from rez.utils.formatting import StringFormatMixin as StringFormatMixin, StringFormatType as StringFormatType
from rez.utils.resources import ResourceHandle as ResourceHandle, ResourceWrapper as ResourceWrapper
from rez.utils.schema import schema_keys as schema_keys
from rez.utils.sourcecode import SourceCode as SourceCode
from rez.version import Requirement as Requirement, Version as Version, VersionRange as VersionRange, VersionedObject as VersionedObject
from typing import Any, Iterator, Literal, overload

class PackageRepositoryResourceWrapper(ResourceWrapper, StringFormatMixin):
    format_expand: Incomplete
    def validated_data(self): ...
    @property
    def repository(self) -> PackageRepository:
        """The package repository this resource comes from.

        Returns:
            `PackageRepository`.
        """

class PackageFamily(PackageRepositoryResourceWrapper):
    """A package family.

    Note:
        Do not instantiate this class directly, instead use the function
        `iter_package_families`.
    """
    keys: Incomplete
    def __init__(self, resource: PackageFamilyResource) -> None: ...
    def iter_packages(self) -> Iterator[Package]:
        """Iterate over the packages within this family, in no particular order.

        Returns:
            `Package` iterator.
        """

class PackageBaseResourceWrapper(PackageRepositoryResourceWrapper):
    """Abstract base class for `Package` and `Variant`.
    """
    late_bind_schemas: Incomplete
    context: rez.resolved_context.ResolvedContext | None
    _late_binding_returnvalues: dict[Any, Any]
    def __init__(self, resource: PackageResource | VariantResource, context: ResolvedContext | None = None) -> None: ...
    def set_context(self, context: ResolvedContext) -> None: ...
    def arbitrary_keys(self) -> None: ...
    @property
    def uri(self): ...
    @property
    def config(self) -> Config:
        """Returns the config for this package.

        Defaults to global config if this package did not provide a 'config'
        section.
        """
    @cached_property
    def is_local(self) -> bool:
        """Returns True if the package is in the local package repository"""
    def print_info(self, buf: Incomplete | None = None, format_=..., skip_attributes: Incomplete | None = None, include_release: bool = False) -> None:
        """Print the contents of the package.

        Args:
            buf (typing.IO): Stream to write to.
            format_ (`FileFormat`): Format to write in.
            skip_attributes (list of str): List of attributes to not print.
            include_release (bool): If True, include release-related attributes,
                such as 'timestamp' and 'changelog'
        """
    def _wrap_forwarded(self, key, value): ...
    def _eval_late_binding(self, sourcecode: SourceCode): ...

class Package(PackageBaseResourceWrapper):
    """A package.

    Warning:
        Do not instantiate this class directly, instead use the function
        :func:`iter_packages` or :meth:`PackageFamily.iter_packages`.
    """
    keys: Incomplete
    is_package: bool
    is_variant: bool
    def __init__(self, resource: PackageResource, context: Incomplete | None = None) -> None: ...
    def __getattr__(self, name: str): ...
    def arbitrary_keys(self):
        """Get the arbitrary keys present in this package.

        These are any keys not in the standard list ('name', 'version' etc).

        Returns:
            set of str: Arbitrary keys.
        """
    @cached_property
    def qualified_name(self) -> str:
        '''Get the qualified name of the package.

        Returns:
            str: Name of the package with version, eg "maya-2016.1".
        '''
    def as_exact_requirement(self) -> str:
        '''Get the package, as an exact requirement string.

        Returns:
            Equivalent requirement string, eg "maya==2016.1"
        '''
    @cached_property
    def parent(self) -> PackageFamily | None:
        """Get the parent package family.

        Returns:
            `PackageFamily`.
        """
    @cached_property
    def num_variants(self) -> int: ...
    @property
    def is_relocatable(self) -> bool:
        """True if the package and its payload is safe to copy.
        """
    @property
    def is_cachable(self) -> bool:
        """True if the package and its payload is safe to cache locally.
        """
    def iter_variants(self) -> Iterator[Variant]:
        """Iterate over the variants within this package, in index order.

        Returns:
            `Variant` iterator.
        """
    def get_variant(self, index: Incomplete | None = None) -> Variant | None:
        """Get the variant with the associated index.

        Returns:
            `Variant` object, or None if no variant with the given index exists.
        """

class Variant(PackageBaseResourceWrapper):
    """A package variant.

    Warning:
        Do not instantiate this class directly, instead use the function
        :meth:`Package.iter_variants`.
    """
    keys: Incomplete
    is_package: bool
    is_variant: bool
    _parent: Any
    def __init__(self, resource: VariantResource, context: Incomplete | None = None, parent: Incomplete | None = None) -> None: ...
    def __getattr__(self, name): ...
    def arbitrary_keys(self): ...
    @cached_property
    def qualified_package_name(self) -> str: ...
    @cached_property
    def qualified_name(self) -> str:
        '''Get the qualified name of the variant.

        Returns:
            str: Name of the variant with version and index, eg "maya-2016.1[1]".
        '''
    @cached_property
    def parent(self) -> Package:
        """Get the parent package.

        Returns:
            `Package`.
        """
    @property
    def variant_requires(self) -> list[Requirement]:
        """Get the subset of requirements specific to this variant.

        Returns:
            List of `Requirement` objects.
        """
    @property
    def requires(self) -> list[Requirement]:
        """Get variant requirements.

        This is a concatenation of the package requirements and those of this
        specific variant.

        Returns:
            List of `Requirement` objects.
        """
    def get_requires(self, build_requires: bool = False, private_build_requires: bool = False) -> list[Requirement]:
        """Get the requirements of the variant.

        Args:
            build_requires (bool): If True, include build requirements.
            private_build_requires (bool): If True, include private build
                requirements.

        Returns:
            List of `Requirement` objects.
        """
    def install(self, path, dry_run: bool = False, overrides: Incomplete | None = None) -> Variant:
        """Install this variant into another package repository.

        If the package already exists, this variant will be correctly merged
        into the package. If the variant already exists in this package, the
        existing variant is returned.

        Args:
            path (str): Path to destination package repository.
            dry_run (bool): If True, do not actually install the variant. In this
                mode, a `Variant` instance is only returned if the equivalent
                variant already exists in this repository; otherwise, None is
                returned.
            overrides (dict): Use this to change or add attributes to the
                installed variant.

        Returns:
            `Variant` object - the (existing or newly created) variant in the
            specified repository. If `dry_run` is True, None may be returned.
        """
    @property
    def _non_shortlinked_subpath(self): ...

class PackageSearchPath:
    """A list of package repositories.

    For example, $REZ_PACKAGES_PATH refers to a list of repositories.
    """
    paths: Any
    def __init__(self, packages_path) -> None:
        """Create a package repository list.

        Args:
            packages_path (list of str): List of package repositories.
        """
    def iter_packages(self, name, range_: Incomplete | None = None) -> Generator[Incomplete]:
        """See `iter_packages`.

        Returns:
            `Package` iterator.
        """
    def __contains__(self, package) -> bool:
        """See if a package is in this list of repositories.

        Note:
            This does not verify the existance of the resource, only that the
            resource's repository is in this list.

        Args:
            package (`Package` or `Variant`): Package to search for.

        Returns:
            bool: True if the resource is in the list of repositories, False
            otherwise.
        """
    @cached_property
    def _repository_uids(self): ...

def iter_package_families(paths: list[str] | None = None):
    """Iterate over package families, in no particular order.

    Note that multiple package families with the same name can be returned.
    Unlike packages, families later in the searchpath are not hidden by earlier
    families.

    Args:
        paths (typing.Optional[list[str]]): paths to search for package families,
            defaults to `config.packages_path`.

    Returns:
        `PackageFamily` iterator.
    """
def iter_packages(name: str, range_: VersionRange | str | None = None, paths: list[str] | None = None) -> Iterator[Package]:
    """Iterate over `Package` instances, in no particular order.

    Packages of the same name and version earlier in the search path take
    precedence - equivalent packages later in the paths are ignored. Packages
    are not returned in any specific order.

    Args:
        name (str): Name of the package, eg 'maya'.
        range_ (VersionRange or str): If provided, limits the versions returned
            to those in `range_`.
        paths (typing.Optional[list[str]]): paths to search for packages, defaults
            to `config.packages_path`.

    Returns:
        `Package` iterator.
    """
def get_package(name: str, version: Version | str, paths: list[str] | None = None) -> Package | None:
    """Get a package by searching a list of repositories.

    Args:
        name (str): Name of the package, eg 'maya'.
        version (Version or str): Version of the package, eg '1.0.0'
        paths (typing.Optional[list[str]]): paths to search for package, defaults
            to `config.packages_path`.

    Returns:
        `Package` object, or None if the package was not found.
    """
def get_package_family_from_repository(name: str, path: str):
    """Get a package family from a repository.

    Args:
        name (str): Name of the package, eg 'maya'.

    Returns:
        `PackageFamily` object, or None if the family was not found.
    """
def get_package_from_repository(name: str, version, path: str):
    """Get a package from a repository.

    Args:
        name (str): Name of the package, eg 'maya'.
        version (Version or str): Version of the package, eg '1.0.0'

    Returns:
        `Package` object, or None if the package was not found.
    """
def get_package_from_handle(package_handle):
    """Create a package given its handle (or serialized dict equivalent)

    Args:
        package_handle (`ResourceHandle` or dict): Resource handle, or
            equivalent serialized dict representation from
            ResourceHandle.to_dict

    Returns:
        `Package`.
    """
def get_package_from_string(txt: str, paths: list[str] | None = None):
    """Get a package given a string.

    Args:
        txt (str): String such as 'foo', 'bah-1.3'.
        paths (typing.Optional[list[str]]): paths to search for package, defaults
            to `config.packages_path`.

    Returns:
        `Package` instance, or None if no package was found.
    """
def get_developer_package(path: str, format: FileFormat | None = None) -> DeveloperPackage:
    """Create a developer package.

    Args:
        path (str): Path to dir containing package definition file.
        format (FileFormat): Package definition file format, detected if None.

    Returns:
        `DeveloperPackage`.
    """
def create_package(name: str, data, package_cls: type[Package] | None = None) -> Package:
    """Create a package given package data.

    Args:
        name (str): Package name.
        data (dict): Package data. Must conform to `package_maker.package_schema`.

    Returns:
        `Package` object.
    """
def get_variant(variant_handle: ResourceHandle | dict, context: ResolvedContext | None = None) -> Variant:
    """Create a variant given its handle (or serialized dict equivalent)

    Args:
        variant_handle (`ResourceHandle` or dict): Resource handle, or
            equivalent serialized dict representation from
            ResourceHandle.to_dict
        context (`ResolvedContext`): The context this variant is associated
            with, if any.

    Returns:
        `Variant`.
    """
def get_package_from_uri(uri: str, paths: list[str] | None = None) -> Package | None:
    """Get a package given its URI.

    Args:
        uri (str): Variant URI
        paths (list of str): paths to search for packages, defaults to
            `config.packages_path`. If None, attempts to find a package that
            may have come from any package repo.

    Returns:
        `Package`, or None if the package could not be found.
    """
def get_variant_from_uri(uri: str, paths: list[str] | None = None) -> Variant | None:
    """Get a variant given its URI.

    Args:
        uri (str): Variant URI
        paths (list of str): paths to search for variants, defaults to
            `config.packages_path`. If None, attempts to find a variant that
            may have come from any package repo.

    Returns:
        `Variant`, or None if the variant could not be found.
    """
def get_last_release_time(name: str, paths: list[str] | None = None) -> int:
    """Returns the most recent time this package was released.

    Note that releasing a variant into an already-released package is also
    considered a package release.

    Args:
        name (str): Package family name.
        paths (list of str): paths to search for packages, defaults to
            `config.packages_path`.

    Returns:
        int: Epoch time of last package release, or zero if this cannot be
        determined.
    """
def get_completions(prefix: str, paths: list[str] | None = None, family_only: bool = False):
    '''Get autocompletion options given a prefix string.

    Example:

        >>> get_completions("may")
        set(["maya", "maya_utils"])
        >>> get_completions("maya-")
        set(["maya-2013.1", "maya-2015.0.sp1"])

    Args:
        prefix (str): Prefix to match.
        paths (list of str): paths to search for packages, defaults to
            `config.packages_path`.
        family_only (bool): If True, only match package names, do not include
            version component.

    Returns:
        Set of strings, may be empty.
    '''
@overload
def get_latest_package(name: str, *, range_: VersionRange | None = None, paths: list[str] | None = None, error: Literal[True] = True) -> Package: ...
@overload
def get_latest_package(name: str, *, range_: VersionRange | None = None, paths: list[str] | None = None, error: Literal[False] | bool = False) -> Package | None: ...
def get_latest_package_from_string(txt: str, paths: list[str] | None = None, error: bool = False) -> Package | None:
    """Get the latest package found within the given request string.

    Args:
        txt (str): Request, eg 'foo-1.2+'
        paths (typing.Optional[list[str]]): paths to search for packages, defaults
            to `config.packages_path`.
        error (bool): If True, raise an error if no package is found.

    Returns:
        `Package` object, or None if no package is found.
    """
def _get_families(name: str, paths: list[str] | None = None) -> list[tuple[PackageRepository, PackageFamilyResource]]: ...
def _check_class(resource, cls) -> None: ...
