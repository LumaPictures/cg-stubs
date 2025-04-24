import subprocess
from _typeshed import Incomplete
from collections.abc import Generator
from contextlib import contextmanager
from enum import Enum
from rez.utils.yaml import dump_yaml as dump_yaml

@contextmanager
def add_sys_paths(paths) -> Generator[None]:
    """Add to sys.path, and revert on scope exit.
    """

class Popen(subprocess.Popen):
    """:class:`subprocess.Popen` wrapper.

    It fixes some issues encountered in Maya and Katana (and potentially other DCCs)
    and also forces the encoding to be utf-8 if text=True or universal_newlines=True
    is set without specifying the encoding.
    """
    def __init__(self, args, **kwargs) -> None: ...

class ExecutableScriptMode(Enum):
    """
    Which scripts to create with util.create_executable_script.
    """
    single = 1
    py = 2
    platform_specific = 3
    both = 4

def create_executable_script(filepath, body, program: Incomplete | None = None, py_script_mode: Incomplete | None = None):
    '''
    Create an executable script. In case a py_script_mode has been set to create
    a .py script the shell is expected to have the PATHEXT environment
    variable to include ".PY" in order to properly launch the command without
    the .py extension.

    Args:
        filepath (str): File to create.
        body (str or typing.Callable): Contents of the script. If a callable, its code
            is used as the script body.
        program (str): Name of program to launch the script. Default is \'python\'
        py_script_mode(ExecutableScriptMode): What kind of script to create.
            Defaults to rezconfig.create_executable_script_mode.
    Returns:
        List of filepaths of created scripts. This may differ from the supplied
        filepath depending on the py_script_mode

    '''
def _get_python_script_files(filepath, py_script_mode, platform):
    """
    Evaluates the py_script_mode for the requested filepath on the given
    platform.

    Args:
        filepath: requested filepath
        py_script_mode (ExecutableScriptMode):
        platform (str): Platform to evaluate the script files for

    Returns:
        list of str: filepaths of scripts to create based on inputs

    """
def create_forwarding_script(filepath, module, func_name, *nargs, **kwargs) -> None:
    """Create a 'forwarding' script.

    A forwarding script is one that executes some arbitrary Rez function. This
    is used internally by Rez to dynamically create a script that uses Rez,
    even though the parent environment may not be configured to do so.
    """
