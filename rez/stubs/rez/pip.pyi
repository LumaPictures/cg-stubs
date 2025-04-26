from _typeshed import Incomplete
from enum import Enum
from rez.config import config as config
from rez.exceptions import BuildError as BuildError, PackageFamilyNotFoundError as PackageFamilyNotFoundError, PackageNotFoundError as PackageNotFoundError, RezSystemError as RezSystemError
from rez.package_maker import make_package as make_package
from rez.packages import get_latest_package as get_latest_package
from rez.resolved_context import ResolvedContext as ResolvedContext
from rez.utils.execution import Popen as Popen
from rez.utils.logging_ import print_debug as print_debug, print_error as print_error, print_info as print_info, print_warning as print_warning
from rez.utils.pip import get_rez_requirements as get_rez_requirements, pip_to_rez_package_name as pip_to_rez_package_name, pip_to_rez_version as pip_to_rez_version
from rez.vendor.distlib.database import DistributionPath as DistributionPath  # type: ignore[import-not-found]
from rez.vendor.packaging.specifiers import Specifier as Specifier  # type: ignore[import-not-found]
from rez.version import Version as Version

PIP_SPECIFIER: Incomplete

class InstallMode(Enum):
    no_deps = 0
    min_deps = 1

def run_pip_command(command_args, pip_version: Incomplete | None = None, python_version: Incomplete | None = None) -> Popen:
    """Run a pip command.
    Args:
        command_args (list of str): Args to pip.
    Returns:
        `subprocess.Popen`: Pip process.
    """
def find_pip(pip_version: Incomplete | None = None, python_version: Incomplete | None = None):
    """Find pip.

    Pip is searched in the following order:

        1. Search for rezified python matching python version request;
        2. If found, test if pip is present;
        3. If pip is present, use it;
        4. If not present, search for rezified pip (this is for backwards compatibility);
        5. If rezified pip is found, use it;
        6. If not, fall back to rez's python installation.

    Args:
        pip_version (str or `Version`): Version of pip to use, or latest if None.
        python_version (str or `Version`): Python version to use, or latest if
            None.

    Returns:
        2-tuple:
        - str: Python executable.
        - `ResolvedContext`: Context containing pip, or None if we fell back
          to system pip.
    """
def find_python_in_context(context):
    '''Find Python executable within the given context.

    Args:
        context (ResolvedContext): Resolved context with Python and pip.
        name (str): Name of the package for Python instead of "python".
        default (str): Force a particular fallback path for Python executable.

    Returns:
        str or None: Path to Python executable, if any.
    '''
def find_pip_from_context(python_version, pip_version: Incomplete | None = None):
    """Find pip from rez context.

    Args:
        python_version (str or `Version`): Python version to use
        pip_version (str or `Version`): Version of pip to use, or latest.

    Returns:
        3-tuple:
        - str: Python executable or None if we fell back to system pip.
        - str: Pip version or None if we fell back to system pip.
        - `ResolvedContext`: Context containing pip, or None if we fell back
          to system pip.
    """
def pip_install_package(source_name, pip_version: Incomplete | None = None, python_version: Incomplete | None = None, mode=..., release: bool = False, prefix: Incomplete | None = None, extra_args: Incomplete | None = None):
    """Install a pip-compatible python package as a rez package.
    Args:
        source_name (str): Name of package or archive/url containing the pip
            package source. This is the same as the arg you would pass to
            the 'pip install' command.
        pip_version (str or `Version`): Version of pip to use to perform the
            install, uses latest if None.
        python_version (str or `Version`): Python version to use to perform the
            install, and subsequently have the resulting rez package depend on.
        mode (`InstallMode`): Installation mode, determines how dependencies are
            managed.
        release (bool): If True, install as a released package; otherwise, it
            will be installed as a local package.
        extra_args (List[str]): Additional options to the pip install command.

    Returns:
        2-tuple:
            List of `Variant`: Installed variants;
            List of `Variant`: Skipped variants (already installed).
    """
def _is_exe(fpath): ...
def _get_distribution_files_mapping(distribution, targetdir):
    """Get remapping of pip installation to rez package installation.

    Args:
        distribution (`distlib.database.InstalledDistribution`): The installed
            distribution
        targetdir (str): Where distribution was installed to (via pip --target)

    Returns:
        Dict of (str, str):
        * key: Path of pip installed file, relative to `targetdir`;
        * value: Relative path to install into rez package.
    """
def _option_present(opts, *args) -> bool: ...
def _cmd(context, command) -> None: ...
def _check_found(py_exe, version_text, log_invalid: bool = True):
    """Check the Python and pip version text found.

    Args:
        py_exe (str or None): Python executable path found, if any.
        version_text (str or None): Pip version found, if any.
        log_invalid (bool): Whether to log messages if found invalid.

    Returns:
        bool: Python is OK and pip version fits against ``PIP_SPECIFIER``.
    """

_verbose: Incomplete

def _log(msg) -> None: ...
