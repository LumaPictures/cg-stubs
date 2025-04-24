from _typeshed import Incomplete
from rez.config import config as config
from rez.exceptions import PackageCopyError as PackageCopyError
from rez.package_repository import PackageRepository as PackageRepository, package_repository_manager as package_repository_manager
from rez.packages import Package as Package, Variant as Variant
from rez.serialise import FileFormat as FileFormat
from rez.utils import with_noop as with_noop
from rez.utils.base26 import create_unique_base26_symlink as create_unique_base26_symlink
from rez.utils.filesystem import additive_copytree as additive_copytree, get_existing_path as get_existing_path, make_path_writable as make_path_writable, replacing_copy as replacing_copy, replacing_symlink as replacing_symlink, safe_makedirs as safe_makedirs
from rez.utils.logging_ import print_info as print_info, print_warning as print_warning
from rez.utils.sourcecode import IncludeModuleManager as IncludeModuleManager

def copy_package(package: Package, dest_repository: PackageRepository, variants: list[int] | None = None, shallow: bool = False, dest_name: Incomplete | None = None, dest_version: Incomplete | None = None, overwrite: bool = False, force: bool = False, follow_symlinks: bool = False, dry_run: bool = False, keep_timestamp: bool = False, skip_payload: bool = False, overrides: Incomplete | None = None, verbose: bool = False) -> dict[str, list[tuple[Variant, Variant]]]:
    '''Copy a package from one package repository to another.

    This copies the package definition and payload. The package can also be
    re-named and/or re-versioned using the ``dest_name`` and ``dest_version`` args.

    The result is a dict describing which package variants were and were not
    copied. For example:

    .. code-block:: text

       {
           "copied": [
               (`Variant`, `Variant`)
           ],
           "skipped": [
               (`Variant`, `Variant`)
           ]
       }

    Each 2-tuple in the \'copied\' or \'skipped\' list contains the source and
    destination variant respectively. In the \'skipped\' list, the source variant
    is the variant that was NOT copied, and the dest variant is the existing
    target variant that caused the source not to be copied. Skipped variants
    will only be present when `overwrite` is False.

    .. note::
       Whether or not a package can be copied is determined by its :attr:`relocatable`
       attribute (see the :data:`default_relocatable` config setting for more details).
       An attempt to copy a non-relocatable package will fail. You can override
       this behaviour with the ``force`` argument.

    Args:
        package (Package): Package to copy.
        dest_repository (PackageRepository or str): The package repository, or
            a package repository path, to copy the package into.
        variants (list[int]): Indexes of variants to build, or all if None.
        shallow (bool): If True, symlinks of each variant\'s root directory are
            created, rather than the payload being copied.
        dest_name (str): If provided, copy the package to a new package name.
        dest_version (str or Version): If provided, copy the package to a new
            version.
        overwrite (bool): Overwrite variants if they already exist in the
            destination package. In this case, the existing payload is removed
            before the new payload is copied.
        force (bool): Copy the package regardless of its relocatable attribute.
            Use at your own risk (there is no guarantee the resulting package
            will be functional).
        follow_symlinks (bool): Follow symlinks when copying package payload,
            rather than copying the symlinks themselves.
        keep_timestamp (bool): By default, a newly copied package will get a
            new timestamp (because that\'s when it was added to the target repo).
            By setting this option to True, the original package\'s timestamp
            is kept intact. Note that this will have no effect if variant(s)
            are copied into an existing package.
        skip_payload (bool): If True, do not copy the package payload.
        overrides (dict): See :meth:`.PackageRepository.install_variant`.
        verbose (bool): Verbose mode.
        dry_run (bool): Dry run mode. Dest variants in the result will be None
            in this case.

    Returns:
        Dict: See comments above.
    '''
def _copy_variant_payload(src_variant: Variant, dest_pkg_repo: PackageRepository, shallow: bool = False, follow_symlinks: bool = False, overrides: Incomplete | None = None, verbose: bool = False) -> None: ...
def _get_overlapped_variant_dirs(src_variant) -> list[str]: ...
def _copy_package_include_modules(src_package, dest_pkg_repo, overrides: Incomplete | None = None) -> None: ...
