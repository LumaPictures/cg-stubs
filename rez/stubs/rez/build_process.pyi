import rez.build_system
import rez.release_vcs
from _typeshed import Incomplete
from collections.abc import Generator
from contextlib import contextmanager
from enum import Enum
from rez.build_system import BuildSystem as BuildSystem
from rez.config import config as config
from rez.developer_package import DeveloperPackage as DeveloperPackage
from rez.exceptions import BuildContextResolveError as BuildContextResolveError, BuildError as BuildError, BuildProcessError as BuildProcessError, ReleaseError as ReleaseError, ReleaseHookCancellingError as ReleaseHookCancellingError, ReleaseVCSError as ReleaseVCSError, RezError as RezError, _NeverError as _NeverError
from rez.packages import Package as Package, Variant as Variant, iter_packages as iter_packages
from rez.release_hook import create_release_hooks as create_release_hooks
from rez.release_vcs import ReleaseVCS as ReleaseVCS
from rez.resolved_context import ResolvedContext as ResolvedContext
from rez.resolver import ResolverStatus as ResolverStatus
from rez.utils.colorize import Printer as Printer, heading as heading
from rez.utils.logging_ import print_warning as print_warning
from typing import Any

debug_print: Incomplete

def get_build_process_types():
    """Returns the available build process implementations."""
def create_build_process(process_type: str, working_dir: str, build_system: BuildSystem, package: Incomplete | None = None, vcs: ReleaseVCS | None = None, ensure_latest: bool = True, skip_repo_errors: bool = False, ignore_existing_tag: bool = False, verbose: bool = False, quiet: bool = False) -> BuildProcess:
    """Create a :class:`BuildProcess` instance.

    .. warning::

       The working_dir argument and the pacakge keyword argument will are deprecated
       and will be removed in rez 3.0.0
    """

class BuildType(Enum):
    """ Enum to represent the type of build."""
    local = 0
    central = 1

class BuildProcess:
    """A BuildProcess builds and possibly releases a package.

    A build process iterates over the variants of a package, creates the
    correct build environment for each variant, builds that variant using a
    build system (or possibly creates a script so the user can do that
    independently), and then possibly releases the package with the nominated
    VCS. This is an abstract base class, you should use a BuildProcess
    subclass.
    """
    @classmethod
    def name(cls) -> None: ...
    verbose: bool
    quiet: bool
    build_system: rez.build_system.BuildSystem
    vcs: rez.release_vcs.ReleaseVCS | None
    ensure_latest: bool
    skip_repo_errors: bool
    ignore_existing_tag: bool
    build_path: Any
    def __init__(self, working_dir: str, build_system: BuildSystem, package: Incomplete | None = None, vcs: ReleaseVCS | None = None, ensure_latest: bool = True, skip_repo_errors: bool = False, ignore_existing_tag: bool = False, verbose: bool = False, quiet: bool = False) -> None:
        """Create a BuildProcess.

        Args:
            working_dir (DEPRECATED): Will be removed in rez 3.0.0.
            build_system (`BuildSystem`): Build system used to build the package.
            package (DEPRECATED): Will be removed in rez 3.0.0.
            vcs (`ReleaseVCS`): Version control system to use for the release
                process.
            ensure_latest: If True, do not allow the release process to occur
                if an newer versioned package is already released.
            skip_repo_errors: If True, proceed with the release even when errors
                occur. BE CAREFUL using this option, it is here in case a package
                needs to be released urgently even though there is some problem
                with reading or writing the repository.
            ignore_existing_tag: Perform the release even if the repository is
                already tagged at the current version. If the config setting
                plugins.release_vcs.check_tag is False, this has no effect.
            verbose (bool): Verbose mode.
            quiet (bool): Quiet mode (overrides `verbose`).
        """
    @property
    def package(self) -> DeveloperPackage: ...
    @property
    def working_dir(self) -> str: ...
    def build(self, install_path: str | None = None, clean: bool = False, install: bool = False, variants: list[int] | None = None) -> int:
        """Perform the build process.

        Iterates over the package's variants, resolves the environment for
        each, and runs the build system within each resolved environment.

        Args:
            install_path (str): The package repository path to install the
                package to, if installing. If None, defaults to
                `config.local_packages_path`.
            clean (bool): If True, clear any previous build first. Otherwise,
                rebuild over the top of a previous build.
            install (bool): If True, install the build.
            variants (list of int): Indexes of variants to build, all if None.

        Raises:
            `BuildError`: If the build failed.

        Returns:
            int: Number of variants successfully built.
        """
    def release(self, release_message: str | None = None, variants: list[int] | None = None) -> int:
        """Perform the release process.

        Iterates over the package's variants, building and installing each into
        the release path determined by `config.release_packages_path`.

        Args:
            release_message (str): Message to associate with the release.
            variants (list of int): Indexes of variants to release, all if None.

        Raises:
            `ReleaseError`: If the release failed.

        Returns:
            int: Number of variants successfully released.
        """
    def get_changelog(self) -> str | None:
        """Get the changelog since last package release.

        Returns:
            str: Changelog.
        """

class BuildProcessHelper(BuildProcess):
    """A BuildProcess base class with some useful functionality.
    """
    @contextmanager
    def repo_operation(self) -> Generator[None]: ...
    def visit_variants(self, func, variants: list[int] | None = None, **kwargs) -> tuple[int, list[str | None]]:
        """Iterate over variants and call a function on each."""
    def get_package_install_path(self, path: str) -> str:
        """Return the installation path for a package (where its payload goes).

        Args:
            path (str): Package repository path.
        """
    def create_build_context(self, variant: Variant, build_type: BuildType, build_path: str) -> tuple[ResolvedContext, str]:
        """Create a context to build the variant within."""
    def pre_release(self) -> None: ...
    def post_release(self, release_message: Incomplete | None = None) -> None: ...
    def get_current_tag_name(self) -> str: ...
    def run_hooks(self, hook_event, **kwargs) -> None: ...
    def get_previous_release(self) -> Package | None: ...
    def get_changelog(self) -> str | None: ...
    def get_release_data(self):
        """Get release data for this release.

        Returns:
            dict.
        """
    def _print(self, txt, *nargs) -> None: ...
    def _print_header(self, txt, n: int = 1) -> None: ...
    def _n_of_m(self, variant) -> str: ...
