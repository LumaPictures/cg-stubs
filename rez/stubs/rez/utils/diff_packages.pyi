from rez.config import config as config
from rez.exceptions import RezError as RezError
from rez.packages import Package as Package, iter_packages as iter_packages
from rez.plugin_managers import plugin_manager as plugin_manager

def diff_packages(pkg1: Package, pkg2: Package | None = None) -> None:
    """Invoke a diff editor to show the difference between the source of two
    packages.

    Args:
        pkg1 (`Package`): Package to diff.
        pkg2 (`Package`): Package to diff against. If None, the next most recent
            package version is used.
    """
