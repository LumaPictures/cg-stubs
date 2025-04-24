from _typeshed import Incomplete
from rez.config import config as config
from rez.package_repository import package_repository_manager as package_repository_manager
from rez.utils.logging_ import print_info as print_info
from rez.version import Version as Version

def remove_package_family(name, path, force: bool = False):
    """Remove a package family from its repository.

    A family can only be deleted if it contains no packages, hidden or
    otherwise, unless `force` is True.

    Args:
        name (str): Name of package family.
        path (str): Package repository path containing the package family.
        force (bool): If True, delete family even if not empty.

    Returns:
        bool: True if the package family was removed, False if not found.
    """
def remove_package(name, version, path):
    """Remove a package from its repository.

    Note that you are able to remove a package that is hidden (ie ignored).
    This is why a Package instance is not specified (if the package were hidden,
    you wouldn't be able to get one).

    Args:
        name (str): Name of package.
        version (Version or str): Version of the package, eg '1.0.0'
        path (str): Package repository path containing the package.

    Returns:
        bool: True if the package was removed, False if package not found.
    """
def remove_packages_ignored_since(days, paths: Incomplete | None = None, dry_run: bool = False, verbose: bool = False):
    """Remove packages ignored for >= specified number of days.

    Args:
        days (int): Remove packages ignored >= this many days
        paths (typing.Optional[list[str]]): Paths to search for packages, defaults
            to `config.packages_path`.
        dry_run: Dry run mode
        verbose (bool): Verbose mode

    Returns:
        int: Number of packages removed. In dry-run mode, returns the number of
        packages that _would_ be removed.
    """
