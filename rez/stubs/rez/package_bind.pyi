from _typeshed import Incomplete
from rez import module_root_path as module_root_path
from rez.config import config as config
from rez.exceptions import RezBindError as RezBindError, _NeverError as _NeverError
from rez.util import get_close_pkgs as get_close_pkgs
from rez.utils.formatting import columnise as columnise
from rez.utils.logging_ import print_error as print_error

def get_bind_modules(verbose: bool = False) -> dict[str, str]:
    """Get available bind modules.

    Returns:
        dict[str, str]: Map of (name, filepath) listing all bind modules.
    """
def find_bind_module(name: str, verbose: bool = False) -> str | None:
    """Find the bind module matching the given name.

    Args:
        name (str): Name of package to find bind module for.
        verbose (bool): If True, print extra output.

    Returns:
        str: Filepath to bind module .py file, or None if not found.
    """
def bind_package(name: str, path: str | None = None, version_range: Incomplete | None = None, no_deps: bool = False, bind_args: list[str] | None = None, quiet: bool = False):
    """Bind software available on the current system, as a rez package.

    Note:
        `bind_args` is provided when software is bound via the 'rez-bind'
        command line tool. Bind modules can define their own command line
        options, and they will be present in `bind_args` if applicable.

    Args:
        name (str): Package name.
        path (str): Package path to install into; local packages path if None.
        version_range (rez.vendor.version.version.VersionRange): If provided, only bind the software if
            it falls within this version range.
        no_deps (bool): If True, don't bind dependencies.
        bind_args (list of str): Command line options.
        quiet (bool): If True, suppress superfluous output.

    Returns:
        list[rez.packages.Variant]: The variant(s) that were installed as a result of
        binding this package.
    """
def _bind_package(name: str, path: str | None = None, version_range: Incomplete | None = None, bind_args: list[str] | None = None, quiet: bool = False): ...
def _print_package_list(variants) -> None: ...
