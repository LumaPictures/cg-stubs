from ._utils.windows import get_syspaths_from_registry as get_syspaths_from_registry, to_posix_path as to_posix_path
from _typeshed import Incomplete
from rezplugins.shell.bash import Bash as Bash

class GitBash(Bash):
    """Git Bash shell plugin.
    """
    pathsep: str
    _drive_regex: Incomplete
    @classmethod
    def name(cls) -> str: ...
    @classmethod
    def executable_name(cls) -> str: ...
    @classmethod
    def find_executable(cls, name, check_syspaths: bool = False): ...
    @classmethod
    def get_syspaths(cls): ...
    def normalize_path(self, path): ...
    def normalize_paths(self, value):
        """
        This is a bit tricky in the case of gitbash. The problem we hit is that
        our pathsep is ':', _but_ pre-normalised paths also contain ':' (eg
        C:\x0coo). In other words we have to deal with values like  'C:\x0coo:C:\x08ah'.

        To get around this, we do the drive-colon replace here instead of in
        normalize_path(), so we can then split the paths correctly. Note that
        normalize_path() still does drive-colon replace also - it needs to
        behave correctly if passed a string like C:\x0coo.
        """

def register_plugin(): ...
