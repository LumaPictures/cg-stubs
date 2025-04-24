from _typeshed import Incomplete
from rez.package_repository import PackageRepository
from rez.package_resources import PackageFamilyResource, PackageRepositoryResource, PackageResourceHelper, VariantResourceHelper, package_pod_schema
from rez.packages import VariantResource
from rez.utils.resources import ResourcePool, cached_property as cached_property
from typing import Iterator

class MemoryPackageFamilyResource(PackageFamilyResource):
    key: str
    repository_type: str
    def _uri(self): ...
    def iter_packages(self) -> Iterator[MemoryPackageResource]: ...

class MemoryPackageResource(PackageResourceHelper):
    key: str
    variant_key: str
    repository_type: str
    schema = package_pod_schema
    def _uri(self) -> str: ...
    @property
    def base(self) -> str | None: ...
    @cached_property
    def parent(self) -> PackageRepositoryResource: ...
    def _load(self): ...

class MemoryVariantResource(VariantResourceHelper):
    key: str
    repository_type: str
    def _root(self, ignore_shortlinks: bool = False) -> str | None: ...
    @cached_property
    def parent(self) -> PackageRepositoryResource: ...

class MemoryPackageRepository(PackageRepository):
    '''An in-memory package repository.

    Packages are stored in a dict, organised like so:

        {
            "foo": {
                "1.0.0": {
                    "name":         "foo",
                    "version":      "1.0.0",
                    "description":  "does foo-like things.",
                }
            },

            "bah": {
                "_NO_VERSION": {
                    "name":         "bah",
                    "description":  "does bah-like things.",
                    "requires":     ["python-2.6", "foo-1+"]
                }
            }
        }

        This example repository contains one versioned package \'foo\', and one
        unversioned package \'bah\'.
    '''
    @classmethod
    def name(cls): ...
    @classmethod
    def create_repository(cls, repository_data) -> MemoryPackageRepository:
        """Create a standalone, in-memory repository.

        Using this function bypasses the `package_repository_manager` singleton.
        This is usually desired however, since in-memory repositories are for
        temporarily storing programmatically created packages, which we do not
        want to cache and that do not persist.

        Args:
            repository_data (dict): Repository data, see class docstring.

        Returns:
            `MemoryPackageRepository` object.
        """
    data: Incomplete
    def __init__(self, location: str, resource_pool: ResourcePool) -> None:
        """Create an in-memory package repository.

        Args:
            location (str): Path containing the package repository.
        """
    def get_package_family(self, name: str) -> MemoryPackageFamilyResource | None: ...
    def iter_package_families(self) -> Iterator[MemoryPackageFamilyResource | None]: ...
    def iter_packages(self, package_family_resource: MemoryPackageFamilyResource) -> Iterator[MemoryPackageResource]: ...
    def iter_variants(self, package_resource: PackageResourceHelper) -> Iterator[VariantResource]: ...
    def get_parent_package_family(self, package_resource: PackageResourceHelper) -> PackageFamilyResource: ...
    def get_parent_package(self, variant_resource: VariantResource): ...

def register_plugin(): ...
