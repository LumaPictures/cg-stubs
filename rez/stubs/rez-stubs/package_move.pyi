from rez.exceptions import PackageMoveError as PackageMoveError
from rez.package_copy import copy_package as copy_package
from rez.package_repository import package_repository_manager as package_repository_manager
from rez.utils.logging_ import print_info as print_info

def move_package(package, dest_repository, keep_timestamp: bool = False, force: bool = False, verbose: bool = False):
    """Move a package.

    Moving a package means copying the package to a destination repo, and
    ignoring (ie hiding - not removing) the source package. The package must
    not already exist in the destination repo.

    Args:
        package (`Package`): Package to move.
        dest_repository (`PackageRepository` or str): The package repository, or
            a package repository path, to move the package into.
        keep_timestamp (bool): By default, a newly copied package will get a
            new timestamp (because that's when it was added to the target repo).
            By setting this option to True, the original package's timestamp
            is kept intact.
        force (bool): Move the package regardless of its relocatable attribute.
            Use at your own risk (there is no guarantee the resulting package
            will be functional).
        verbose (bool): Verbose mode.

    Returns:
        `Package`: The newly created package in the destination repo.
    """
