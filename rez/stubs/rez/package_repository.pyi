import rez.utils.resources
import threading
from _typeshed import Incomplete
from contextlib import contextmanager
from rez.config import config as config
from rez.exceptions import ResourceError as ResourceError
from rez.package_resources import PackageFamilyResource as PackageFamilyResource, PackageRepositoryResource as PackageRepositoryResource, PackageResource as PackageResource, PackageResourceHelper as PackageResourceHelper, VariantResource as VariantResource
from rez.plugin_managers import plugin_manager as plugin_manager
from rez.utils.data_utils import cached_property as cached_property
from rez.utils.resources import Resource as Resource, ResourceHandle as ResourceHandle, ResourcePool as ResourcePool
from rez.version import Version as Version
from rezplugins.package_repository.memory import MemoryPackageRepository
from typing import Any, Hashable, Iterator

def get_package_repository_types():
    """Returns the available package repository implementations."""
def create_memory_package_repository(repository_data: dict) -> MemoryPackageRepository:
    """Create a standalone in-memory package repository from the data given.

    See rezplugins/package_repository/memory.py for more details.

    Args:
        repository_data (dict): Package repository data.

    Returns:
        `PackageRepository` object.
    """

class PackageRepositoryGlobalStats(threading.local):
    """Gathers stats across package repositories.
    """
    package_load_time: float
    def __init__(self) -> None: ...
    @contextmanager
    def package_loading(self) -> Iterator[None]:
        """Use this around code in your package repository that is loading a
        package, for example from file or cache.
        """

package_repo_stats: Incomplete

class PackageRepository:
    """Base class for package repositories implemented in the package_repository
    plugin type.

    Note that, even though a package repository does determine where package
    payloads should go, it is not responsible for creating or copying these
    payloads.
    """
    remove: Incomplete
    @classmethod
    def name(cls) -> str:
        """Return the name of the package repository type."""
    location: str
    pool: rez.utils.resources.ResourcePool
    def __init__(self, location: str, resource_pool: ResourcePool) -> None:
        """Create a package repository.

        Args:
            location (str): A string specifying the location of the repository.
                This could be a filesystem path, or a database uri, etc.
            resource_pool (`ResourcePool`): The pool used to manage package
                resources.
        """
    def __str__(self) -> str: ...
    def register_resource(self, resource_class: type[Resource]) -> None:
        """Register a resource with the repository.

        Your derived repository class should call this method in its __init__ to
        register all the resource types associated with that plugin.
        """
    def clear_caches(self) -> None:
        """Clear any cached resources in the pool."""
    @cached_property
    def uid(self) -> tuple[str, str]:
        """Returns a unique identifier for this repository.

        This must be a persistent identifier, for example a filepath, or
        database address + index, and so on.

        Returns:
            tuple[str, str]: Value that uniquely identifies this repository.
        """
    def __eq__(self, other) -> bool: ...
    def is_empty(self) -> bool:
        """Determine if the repository contains any packages.

        Returns:
            True if there are no packages, False if there are at least one.
        """
    def get_package_family(self, name: str) -> PackageFamilyResource | None:
        """Get a package family.

        Args:
            name (str): Package name.

        Returns:
            `PackageFamilyResource`, or None if not found.
        """
    def iter_package_families(self) -> Iterator[PackageFamilyResource]:
        """Iterate over the package families in the repository, in no
        particular order.

        Returns:
            `PackageFamilyResource` iterator.
        """
    def iter_packages(self, package_family_resource: PackageFamilyResource) -> Iterator[PackageResource]:
        """Iterate over the packages within the given family, in no particular
        order.

        Args:
            package_family_resource (`PackageFamilyResource`): Parent family.

        Returns:
            `PackageResource` iterator.
        """
    def iter_variants(self, package_resource: PackageResource) -> Iterator[VariantResource]:
        """Iterate over the variants within the given package.

        Args:
            package_resource (`PackageResource`): Parent package.

        Returns:
            `VariantResource` iterator.
        """
    def get_package(self, name: str, version: Version) -> PackageResourceHelper | None:
        """Get a package.

        Args:
            name (str): Package name.
            version (`Version`): Package version.

        Returns:
            `PackageResourceHelper` or None: Matching package, or None if not found.
        """
    def get_package_from_uri(self, uri: str) -> PackageResource | None:
        """Get a package given its URI.

        Args:
            uri (str): Package URI

        Returns:
            `PackageResource`, or None if the package is not present in this
            package repository.
        """
    def get_variant_from_uri(self, uri: str) -> VariantResource | None:
        """Get a variant given its URI.

        Args:
            uri (str): Variant URI

        Returns:
            `VariantResource`, or None if the variant is not present in this
            package repository.
        """
    def ignore_package(self, pkg_name: str, pkg_version: Version, allow_missing: bool = False) -> int:
        """Ignore the given package.

        Ignoring a package makes it invisible to further resolves.

        Args:
            pkg_name (str): Package name
            pkg_version(`Version`): Package version
            allow_missing (bool): if True, allow for ignoring a package that
                does not exist. This is useful when you want to copy a package
                to a repo and you don't want it visible until the copy is
                completed.

        Returns:
            int:
            * -1: Package not found
            * 0: Nothing was done, package already ignored
            * 1: Package was ignored
        """
    def unignore_package(self, pkg_name: str, pkg_version: Version) -> int:
        """Unignore the given package.

        Args:
            pkg_name (str): Package name
            pkg_version(`Version`): Package version

        Returns:
            int:
            * -1: Package not found
            * 0: Nothing was done, package already visible
            * 1: Package was unignored
        """
    def remove_package(self, pkg_name: str, pkg_version: Version) -> bool:
        """Remove a package.

        Note that this should work even if the specified package is currently
        ignored.

        Args:
            pkg_name (str): Package name
            pkg_version(`Version`): Package version

        Returns:
            bool: True if the package was removed, False if it wasn't found.
        """
    def remove_package_family(self, pkg_name: str, force: bool = False) -> bool:
        """Remove an empty package family.

        Args:
            pkg_name (str): Package name
            force (bool): If Trur, delete even if not empty.

        Returns:
            bool: True if the family was removed, False if it wasn't found.
        """
    def remove_ignored_since(self, days: int, dry_run: bool = False, verbose: bool = False) -> int:
        """Remove packages ignored for >= specified number of days.

        Args:
            days (int): Remove packages ignored >= this many days
            dry_run: Dry run mode
            verbose (bool): Verbose mode

        Returns:
            int: Number of packages removed. In dry-run mode, returns the
            number of packages that _would_ be removed.
        """
    def pre_variant_install(self, variant_resource: VariantResource) -> None:
        """Called before a variant is installed.

        If any directories are created on disk for the variant to install into,
        this is called before that happens.

        Note that it is the responsibility of the `BuildProcess` to call this
        function at the appropriate time.
        """
    def on_variant_install_cancelled(self, variant_resource: VariantResource) -> None:
        """Called when a variant installation is cancelled.

        This is called after `pre_variant_install`, but before `install_variant`,
        which is not expected to be called.

        Variant install cancellation usually happens for one of two reasons -
        either the variant installation failed (ie a build error occurred), or
        one or more of the package tests failed, aborting the installation.

        Note that it is the responsibility of the `BuildProcess` to call this
        function at the appropriate time.
        """
    def install_variant(self, variant_resource: VariantResource, dry_run: bool = False, overrides: dict[str, Any] | None = None) -> VariantResource:
        """Install a variant into this repository.

        Use this function to install a variant from some other package repository
        into this one.

        Args:
            variant_resource (`VariantResource`): Variant to install.
            dry_run (bool): If True, do not actually install the variant. In this
                mode, a `Variant` instance is only returned if the equivalent
                variant already exists in this repository; otherwise, None is
                returned.
            overrides (dict): Use this to change or add attributes to the
                installed variant. To remove attributes, set values to
                `PackageRepository.remove`.

        Returns:
            `VariantResource` object, which is the newly created variant in this
            repository. If `dry_run` is True, None may be returned.
        """
    def get_equivalent_variant(self, variant_resource: VariantResource) -> VariantResource:
        """Find a variant in this repository that is equivalent to that given.

        A variant is equivalent to another if it belongs to a package of the
        same name and version, and it has the same definition (ie package
        requirements).

        Note that even though the implementation is trivial, this function is
        provided since using `install_variant` to find an existing variant is
        nonintuitive.

        Args:
            variant_resource (`VariantResource`): Variant to install.

        Returns:
            `VariantResource` object, or None if the variant was not found.
        """
    def get_parent_package_family(self, package_resource: PackageResourceHelper) -> PackageFamilyResource:
        """Get the parent package family of the given package.

        Args:
            package_resource (`PackageResource`): Package.

        Returns:
            `PackageFamilyResource`.
        """
    def get_parent_package(self, variant_resource: VariantResource) -> PackageRepositoryResource:
        """Get the parent package of the given variant.

        Args:
            variant_resource (`VariantResource`): Variant.

        Returns:
            `PackageResource`.
        """
    def get_variant_state_handle(self, variant_resource: PackageResource) -> Hashable | None:
        """Get a value that indicates the state of the variant.

        This is used for resolve caching. For example, in the 'filesystem'
        repository type, the 'state' is the last modified date of the file
        associated with the variant (perhaps a package.py). If the state of
        any variant has changed from a cached resolve - eg, if a file has been
        modified - the cached resolve is discarded.

        This may not be applicable to your repository type, leave as-is if so.

        Returns:
            A hashable value.
        """
    def get_last_release_time(self, package_family_resource: PackageFamilyResource) -> int:
        """Get the last time a package was added to the given family.

        This information is used to cache resolves via memcached. It can be left
        not implemented, but resolve caching is a substantial optimisation that
        you will be missing out on.

        Returns:
            int: Epoch time at which a package was changed/added/removed from
                the given package family. Zero signifies an unknown last package
                update time.
        """
    def make_resource_handle(self, resource_key: str, **variables) -> ResourceHandle:
        """Create a `ResourceHandle`

        Nearly all `ResourceHandle` creation should go through here, because it
        gives the various resource classes a chance to normalize / standardize
        the resource handles, to improve caching / comparison / etc.
        """
    def get_resource(self, resource_key: str, **variables) -> Resource:
        """Get a resource.

        Attempts to get and return a cached version of the resource if
        available, otherwise a new resource object is created and returned.

        Args:
            resource_key (`str`):  Name of the type of `Resources` to find
            variables: data to identify / store on the resource

        Returns:
            `PackageRepositoryResource` instance.
        """
    def get_resource_from_handle(self, resource_handle: ResourceHandle, verify_repo: bool = True) -> Resource:
        """Get a resource.

        Args:
            resource_handle (`ResourceHandle`): Handle of the resource.

        Returns:
            `PackageRepositoryResource` instance.
        """
    def get_package_payload_path(self, package_name: str, package_version: str | Version | None = None) -> str:
        """Defines where a package's payload should be installed to.

        Args:
            package_name (str): Name of package.
            package_version (str or `Version`): Package version.

        Returns:
            str: Path where package's payload should be installed to.
        """
    def _uid(self) -> tuple[str, str]:
        """Unique identifier implementation.

        You may need to provide your own implementation. For example, consider
        the 'filesystem' repository. A default uri might be 'filesystem@/tmp_pkgs'.
        However /tmp_pkgs is probably a local path for each user, so this would
        not actually uniquely identify the repository - probably the inode number
        needs to be incorporated also.

        Returns:
            Hashable value.
        """

class PackageRepositoryManager:
    """Package repository manager.

    Manages retrieval of resources (packages and variants) from `PackageRepository`
    instances, and caches these resources in a resource pool.
    """
    pool: rez.utils.resources.ResourcePool
    repositories: dict[str, PackageRepository]
    def __init__(self, resource_pool: ResourcePool | None = None) -> None:
        """Create a package repo manager.

        Args:
            resource_pool (`ResourcePool`): Provide your own resource pool. If
                None, a default pool is created based on config settings.
        """
    def get_repository(self, path: str) -> PackageRepository:
        '''Get a package repository.

        Args:
            path (str): Entry from the \'packages_path\' config setting. This may
                simply be a path (which is managed by the \'filesystem\' package
                repository plugin), or a string in the form "type@location",
                where \'type\' identifies the repository plugin type to use.

        Returns:
            `PackageRepository` instance.
        '''
    def are_same(self, path_1: str, path_2: str) -> bool:
        """Test that `path_1` and `path_2` refer to the same repository.

        This is more reliable than testing that the strings match, since slightly
        different strings might refer to the same repository (consider small
        differences in a filesystem path for example, eg '//svr/foo', '/svr/foo').

        Returns:
            True if the paths refer to the same repository, False otherwise.
        """
    def get_resource(self, resource_key: str, repository_type: str, location: str, **variables) -> Resource:
        """Get a resource.

        Attempts to get and return a cached version of the resource if
        available, otherwise a new resource object is created and returned.

        Args:
            resource_key (`str`):  Name of the type of `Resources` to find
            repository_type (`str`): What sort of repository to look for the
                resource in
            location (`str`): location for the repository
            variables: data to identify / store on the resource

        Returns:
            `PackageRepositoryResource` instance.
        """
    def get_resource_from_handle(self, resource_handle: ResourceHandle) -> Resource:
        """Get a resource.

        Args:
            resource_handle (`ResourceHandle`): Handle of the resource.

        Returns:
            `PackageRepositoryResource` instance.
        """
    def clear_caches(self) -> None:
        """Clear all cached data."""
    def _get_repository(self, path: str, **repo_args) -> PackageRepository: ...

package_repository_manager: Incomplete
