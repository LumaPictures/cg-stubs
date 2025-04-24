from rez.utils.execution import Popen as Popen
from rez.utils.filesystem import make_path_writable as make_path_writable

def get_rpaths(elfpath):
    """Get rpaths/runpaths from header.
    """
def patch_rpaths(elfpath, rpaths) -> None:
    """Replace an elf's rpath header with those provided.
    """
def _run(*nargs, **popen_kwargs): ...
