from _typeshed import Incomplete

_drive_start_regex: Incomplete
_env_var_regex: Incomplete

def to_posix_path(path: str) -> str:
    '''Convert (eg) "C:\x0coo" to "/c/foo"

    TODO: doesn\'t take into account escaped bask slashes, which would be
    weird to have in a path, but is possible.
    '''
def to_windows_path(path: str) -> str:
    '''Convert (eg) "C:\x0coo/bin" to "C:\x0coo\x08in"

    The mixed syntax results from strings in package commands such as
    "{root}/bin" being interpreted in a windows shell.

    TODO: doesn\'t take into account escaped forward slashes, which would be
    weird to have in a path, but is possible.
    '''
def get_syspaths_from_registry() -> list[str]: ...
