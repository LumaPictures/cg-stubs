import rez.packages
from _typeshed import Incomplete
from contextlib import contextmanager
from rez.exceptions import PackageMetadataError as PackageMetadataError
from rez.package_py_utils import expand_requirement as expand_requirement
from rez.package_repository import create_memory_package_repository as create_memory_package_repository
from rez.package_resources import _commands_schema as _commands_schema, _function_schema as _function_schema, help_schema as help_schema, late_bound as late_bound
from rez.packages import Package as Package, Variant as Variant
from rez.utils._version import _rez_version as _rez_version
from rez.utils.data_utils import AttrDictWrapper as AttrDictWrapper
from rez.utils.filesystem import retain_cwd as retain_cwd
from rez.utils.formatting import PackageRequest as PackageRequest
from rez.utils.logging_ import print_warning as print_warning
from rez.utils.schema import Required as Required, extensible_schema_dict as extensible_schema_dict
from rez.vendor.schema.schema import And as And, Optional as Optional, Or as Or, Schema as Schema, Use as Use  # type: ignore[import-not-found]
from rez.version import Version as Version
from typing import Any, Iterator

package_request_schema: Incomplete
tests_schema: Incomplete
package_schema: Incomplete

class PackageMaker(AttrDictWrapper):
    """Utility class for creating packages."""
    name: str
    package_cls: type[rez.packages.Package]
    installed_variants: list[Any]
    skipped_variants: list[Any]
    def __init__(self, name: str, data: Incomplete | None = None, package_cls: type[Package] | None = None) -> None:
        """Create a package maker.

        Args:
            name (str): Package name.
        """
    def get_package(self) -> Package:
        """Create the analogous package.

        Returns:
            `Package` object.
        """
    def _get_data(self): ...

@contextmanager
def make_package(name: str, path: str, make_base: Incomplete | None = None, make_root: Incomplete | None = None, skip_existing: bool = True, warn_on_skip: bool = True) -> Iterator[PackageMaker]:
    '''Make and install a package.

    Example:

        >>> def make_root(variant, path):
        >>>     os.symlink("/foo_payload/misc/python27", "ext")
        >>>
        >>> with make_package(\'foo\', \'/packages\', make_root=make_root) as pkg:
        >>>     pkg.version = \'1.0.0\'
        >>>     pkg.description = \'does foo things\'
        >>>     pkg.requires = [\'python-2.7\']

    Args:
        name (str): Package name.
        path (str): Package repository path to install package into.
        make_base (typing.Callable): Function that is used to create the package
            payload, if applicable.
        make_root (typing.Callable): Function that is used to create the package
            variant payloads, if applicable.
        skip_existing (bool): If True, detect if a variant already exists, and
            skip with a warning message if so.
        warn_on_skip (bool): If True, print warning when a variant is skipped.

    Yields:
        `PackageMaker` object.

    Note:
        Both `make_base` and `make_root` are called once per variant install,
        and have the signature (variant, path).

    Note:
        The \'installed_variants\' attribute on the `PackageMaker` instance will
        be appended with variant(s) created by this function, if any.
    '''
