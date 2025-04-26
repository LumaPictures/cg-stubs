import functools
import rez.package_resources
import rez.packages
import rez.serialise
from _typeshed import Incomplete
from collections.abc import Generator
from contextlib import contextmanager
from rez.exceptions import PackageMetadataError
from rez.package_repository import PackageRepository
from rez.package_resources import PackageFamilyResource, PackageRepositoryResource, PackageResourceHelper, VariantResource, VariantResourceHelper, package_pod_schema
from rez.packages import Package, Variant
from rez.serialise import FileFormat
from rez.utils.memcached import pool_memcached_connections
from rez.utils.resources import cached_property as cached_property
from rez.version import Version
from typing import Any, Iterator

debug_print: Incomplete
format_version: int

def check_format_version(filename, data) -> None: ...

_settings: Incomplete

class PackageDefinitionFileMissing(PackageMetadataError): ...

class FileSystemPackageFamilyResource(PackageFamilyResource):
    key: str
    repository_type: str
    def _uri(self) -> str: ...
    @cached_property
    def path(self) -> str: ...
    def get_last_release_time(self) -> float: ...
    def iter_packages(self) -> Iterator[FileSystemPackageResource]: ...

class FileSystemPackageResource(PackageResourceHelper):  # type: ignore[misc]
    key: str
    variant_key: str
    repository_type: str
    schema = package_pod_schema
    def _uri(self) -> str: ...
    @cached_property
    def parent(self) -> FileSystemPackageFamilyResource: ...
    @cached_property
    def state_handle(self) -> float | None: ...
    @property
    def base(self) -> str | None: ...
    @cached_property
    def path(self) -> str: ...
    @cached_property
    def filepath(self) -> str: ...
    @cached_property
    def file_format(self): ...
    @cached_property
    def _filepath_and_format(self): ...
    def _load(self): ...
    def _load_old_formats(self): ...
    @staticmethod
    def _update_changelog(file_format, data): ...

class FileSystemVariantResource(VariantResourceHelper):  # type: ignore[misc]
    key: str
    repository_type: str
    @cached_property
    def parent(self) -> FileSystemPackageResource: ...

class FileSystemCombinedPackageFamilyResource(PackageFamilyResource):
    key: str
    repository_type: str
    schema: Incomplete
    @property
    def ext(self): ...
    @property
    def filepath(self): ...
    def _uri(self): ...
    def get_last_release_time(self): ...
    def iter_packages(self) -> Generator[Incomplete]: ...
    def _load(self): ...

class FileSystemCombinedPackageResource(PackageResourceHelper):  # type: ignore[misc]
    key: str
    variant_key: str
    repository_type: str
    schema = package_pod_schema
    def _uri(self) -> str: ...
    @cached_property
    def parent(self) -> FileSystemCombinedPackageFamilyResource: ...
    @property
    def base(self) -> str | None: ...
    @cached_property
    def state_handle(self) -> float: ...
    def iter_variants(self) -> Iterator[FileSystemCombinedVariantResource]: ...
    def _load(self): ...

class FileSystemCombinedVariantResource(VariantResourceHelper):  # type: ignore[misc]
    key: str
    repository_type: str
    @cached_property
    def parent(self) -> PackageRepositoryResource: ...
    def _root(self, ignore_shortlinks: bool = False) -> str | None: ...

class FileSystemPackageRepository(PackageRepository):
    """A filesystem-based package repository.

    TODO: Deprecate YAML
    Packages are stored on disk, in either 'package.yaml' or 'package.py' files.
    These files are stored into an organised directory structure like so:

        /LOCATION/pkgA/1.0.0/package.py
                      /1.0.1/package.py
                 /pkgB/2.1/package.py
                      /2.2/package.py

    Another supported storage format is to store all package versions within a
    single package family in one file, like so:

        /LOCATION/pkgC.yaml
        /LOCATION/pkgD.py

    These 'combined' package files allow for differences between package
    versions via a 'package_overrides' section:

        name: pkgC

        versions:
        - '1.0'
        - '1.1'
        - '1.2'

        version_overrides:
            '1.0':
                requires:
                - python-2.5
            '1.1+':
                requires:
                - python-2.6
    """
    schema_dict: Incomplete
    building_prefix: str
    ignore_prefix: str
    package_file_mode: Incomplete
    @classmethod
    def name(cls) -> str: ...
    disable_pkg_ignore: bool
    disable_memcache: Any
    get_families: functools._lru_cache_wrapper[list[rez.package_resources.PackageFamilyResource]]
    get_family: functools._lru_cache_wrapper[rez.package_resources.PackageFamilyResource | None]
    get_packages: functools._lru_cache_wrapper[list[rez.packages.Package]]
    get_variants: functools._lru_cache_wrapper[list[rez.package_resources.VariantResource]]
    get_file: functools._lru_cache_wrapper[tuple[str, rez.serialise.FileFormat] | tuple[None, None]]
    def __init__(self, location, resource_pool, disable_memcache: Incomplete | None = None, disable_pkg_ignore: bool = False) -> None:
        """Create a filesystem package repository.

        Args:
            location (str): Path containing the package repository.
            disable_memcache (bool): Don't use memcache memcache if True
            disable_pkg_ignore (bool): If True, .ignore* files have no effect
        """
    def _uid(self): ...
    def get_package_family(self, name: str) -> PackageFamilyResource: ...
    @pool_memcached_connections
    def iter_package_families(self) -> Iterator[PackageFamilyResource]: ...
    @pool_memcached_connections
    def iter_packages(self, package_family_resource: PackageFamilyResource) -> Iterator[Package]: ...
    def iter_variants(self, package_resource: PackageResourceHelper) -> Iterator[VariantResource]: ...  # type: ignore[override]
    def get_parent_package_family(self, package_resource: PackageResourceHelper) -> PackageRepositoryResource: ...  # type: ignore[override]
    def get_parent_package(self, variant_resource: VariantResource) -> PackageRepositoryResource: ...
    def get_variant_state_handle(self, variant_resource: VariantResource): ...  # type: ignore[override]
    def get_last_release_time(self, package_family_resource: PackageFamilyResource): ...
    def get_package_from_uri(self, uri: str):
        '''
        Example URIs:
        - /svr/packages/mypkg/1.0.0/package.py
        - /svr/packages/mypkg/package.py  # (unversioned package - rare)
        - /svr/packages/mypkg/package.py<1.0.0>  # ("combined" package type - rare)
        '''
    def get_variant_from_uri(self, uri: str) -> Variant | None:  # type: ignore[override]
        '''
        Example URIs:
        - /svr/packages/mypkg/1.0.0/package.py[1]
        - /svr/packages/mypkg/1.0.0/package.py[]  # ("null" variant)
        - /svr/packages/mypkg/package.py[1]  # (unversioned package - rare)
        - /svr/packages/mypkg/package.py<1.0.0>[1]  # ("combined" package type - rare)
        '''
    def ignore_package(self, pkg_name: str, pkg_version: Version, allow_missing: bool = False) -> int: ...
    def unignore_package(self, pkg_name: str, pkg_version) -> int: ...
    def remove_package(self, pkg_name: str, pkg_version) -> bool: ...
    def remove_package_family(self, pkg_name: str, force: bool = False) -> bool: ...
    def remove_ignored_since(self, days, dry_run: bool = False, verbose: bool = False) -> int: ...
    def get_resource_from_handle(self, resource_handle, verify_repo: bool = True): ...
    @cached_property
    def file_lock_dir(self): ...
    def pre_variant_install(self, variant_resource: VariantResourceHelper) -> None: ...  # type: ignore[override]
    def on_variant_install_cancelled(self, variant_resource) -> None:
        """
        TODO:
            Currently this will not delete a newly created package version
            directory. The reason is because behaviour with multiple rez procs
            installing variants of the same package in parallel is not well
            tested and hasn't been fully designed for yet. Currently, if this
            did delete the version directory, it could delete it while another
            proc is performing a successful variant install into the same dir.

            Note though that this does do useful work, if the cancelled variant
            was getting installed into an existing package. In this case, the
            .building file is deleted, because the existing package.py is valid.

            Work has to be done to change the way that new variant dirs and the
            .building file are created, so that we can safely delete cancelled
            variant dirs in the presence of multiple rez procs.

            See #810
        """
    def install_variant(self, variant_resource: VariantResource, dry_run: bool = False, overrides: Incomplete | None = None) -> VariantResource: ...
    def _copy(self, **kwargs):
        """
        Make a copy of the repo that does not share resources with this one.
        """
    @contextmanager
    def _lock_package(self, package_name, package_version: Incomplete | None = None) -> Generator[None]: ...
    def clear_caches(self) -> None: ...
    def get_package_payload_path(self, package_name: str, package_version: Incomplete | None = None) -> str: ...
    def _get_family_dirs__key(self): ...
    def _get_family_dirs(self): ...
    def _get_version_dirs__key(self, root): ...
    def _get_version_dirs(self, root): ...
    def _is_valid_package_directory(self, path): ...
    def _get_families(self) -> list[PackageFamilyResource]: ...
    def _get_family(self, name: str) -> PackageFamilyResource | None: ...
    def _get_packages(self, package_family_resource: PackageFamilyResource) -> list[Package]: ...
    def _get_variants(self, package_resource: PackageResourceHelper) -> list[VariantResource]: ...
    def _get_file(self, path, package_filename: Incomplete | None = None) -> tuple[str, FileFormat] | tuple[None, None]: ...
    def _create_family(self, name: str): ...
    def _create_variant(self, variant: VariantResource, dry_run: bool = False, overrides: Incomplete | None = None) -> VariantResource | None: ...
    def _on_changed(self, pkg_name: str) -> None:
        """Called when a package is added/removed/changed.
        """
    def _delete_stale_build_tagfiles(self, family_path: str) -> None: ...

def register_plugin(): ...
