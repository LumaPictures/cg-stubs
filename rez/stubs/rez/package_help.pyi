import rez.packages
from _typeshed import Incomplete
from rez.config import config as config
from rez.packages import iter_packages as iter_packages
from rez.rex_bindings import VersionBinding as VersionBinding
from rez.system import system as system
from rez.utils.backcompat import convert_old_command_expansions as convert_old_command_expansions
from rez.utils.execution import Popen as Popen
from rez.utils.scope import scoped_formatter as scoped_formatter

class PackageHelp:
    """Object for extracting and viewing help for a package.

    Given a package and version range, help will be extracted from the latest
    package in the version range that provides it.
    """
    package: rez.packages.Package | None
    _verbose: bool
    _sections: list[list[str]]
    def __init__(self, package_name, version_range: Incomplete | None = None, paths: Incomplete | None = None, verbose: bool = False) -> None:
        """Create a PackageHelp object.

        Args:
            package_name (str): Package to search.
            version_range (`VersionRange`): Versions to search.
        """
    @property
    def success(self):
        """Return True if help was found, False otherwise."""
    @property
    def sections(self):
        """Returns a list of (name, uri) 2-tuples."""
    def open(self, section_index: int = 0) -> None:
        """Launch a help section."""
    def print_info(self, buf: Incomplete | None = None) -> None:
        """Print help sections."""
    @classmethod
    def open_rez_manual(cls) -> None:
        """Open the Rez user manual."""
    @classmethod
    def _open_url(cls, url) -> None: ...
