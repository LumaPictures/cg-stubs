from _typeshed import Incomplete
from rez.config import config as config
from rez.exceptions import RezBindError as RezBindError
from rez.util import which as which
from rez.utils.execution import Popen as Popen
from rez.utils.logging_ import print_debug as print_debug
from rez.version import Version as Version

def log(msg) -> None: ...
def make_dirs(*dirs): ...
def run_python_command(commands, exe: Incomplete | None = None): ...
def get_version_in_python(name, commands): ...
def check_version(version, range_: Incomplete | None = None) -> None:
    """Check that the found software version is within supplied range.

    Args:
        version: Version of the package as a Version object.
        range_: Allowable version range as a VersionRange object.
    """
def find_exe(name, filepath: Incomplete | None = None):
    """Find an executable.

    Args:
        name: Name of the program, eg 'python'.
        filepath: Path to executable, a search is performed if None.

    Returns:
        Path to the executable if found, otherwise an error is raised.
    """
def extract_version(exepath, version_arg, word_index: int = -1, version_rank: int = 3):
    '''Run an executable and get the program version.

    Args:
        exepath: Filepath to executable.
        version_arg: Arg to pass to program, eg "-V". Can also be a list.
        word_index: Expect the Nth word of output to be the version.
        version_rank: Cap the version to this many tokens.

    Returns:
        `Version` object.
    '''
def _run_command(args): ...
