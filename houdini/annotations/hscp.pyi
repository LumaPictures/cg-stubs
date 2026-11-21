import os
from collections.abc import Callable, Iterable

class Error(Exception): ...

class RemoteLogin:
    machine: str
    user: str
    ssh_key_path: str
    def __init__(self, machine: str, user: str, ssh_key_path: str) -> None: ...

def copyFileToRemoteMachine(local_file_path: str | os.PathLike[str], remote_login: RemoteLogin, remote_directory: str, progress_callback: Callable[[float, str], object] | None = ...) -> None: ...
def copyFileFromRemoteMachine(remote_login: RemoteLogin, remote_file_path: str, local_file_path: str | os.PathLike[str], progress_callback: Callable[[float, str], object] | None = ...) -> None: ...

ASSEMBLING_AND_COMPRESSING: int
CONNECTING: int
SENDING: int
EXTRACTING: int
DONE: int
ERROR: int

def bundleAndCopyFilesToRemoteMachine(local_file_paths: Iterable[str], local_base_directory: str, remote_login: RemoteLogin, remote_base_directory: str, update_callback: Callable[[int, str, float, str], object], archive_prefix: str = ...) -> None: ...
def copyBundledFilesToRemoteMachine(tar_path: str, remote_login: RemoteLogin, remote_base_directory: str, update_callback: Callable[[int, str, float, str], object], delete_tarball: bool = ...) -> None: ...
def createBZ2Archive(file_paths: Iterable[str], base_directory: str, archive_prefix: str = ..., tar_path: str | None = ...) -> str: ...
