# Houdini stubs generated from Houdini 22.0.466

import os
from collections.abc import Callable as Callable, Iterable

ASSEMBLING_AND_COMPRESSING: int
CONNECTING: int
SENDING: int
EXTRACTING: int
DONE: int
ERROR: int

class Error(Exception): ...

class RemoteLogin:
    """Contains information about how to log in to the remote machine."""
    machine: str
    user: str
    ssh_key_path: str
    def __init__(self, machine: str, user: str, ssh_key_path: str) -> None: ...

def copyFileToRemoteMachine(local_file_path: str | os.PathLike[str], remote_login: RemoteLogin, remote_directory: str, progress_callback: Callable[[float, str], object] | None = None) -> None:
    """Use scp to copy a file to a remote machine using a passwordless login.

    progress_callback: This callback is invoked with a fraction complete and
    a string containing an estimated duration until completion.  If you're
    not using the update callback then you probably don't need to use this
    module; just invoke the scp command.
    """
def copyFileFromRemoteMachine(remote_login: RemoteLogin, remote_file_path: str, local_file_path: str | os.PathLike[str], progress_callback: Callable[[float, str], object] | None = None) -> None:
    """Use scp to copy a file from a remote machine using a passwordless login.

    See copyFileToRemoteMachine for more information.
    """
def bundleAndCopyFilesToRemoteMachine(local_file_paths: Iterable[str], local_base_directory: str, remote_login: RemoteLogin, remote_base_directory: str, update_callback: Callable[[int, str, float, str], object], archive_prefix: str = '') -> None:
    """Gather local files into a compressed archive, send it to a remote
    machine using passwordless scp, and extract it there.

    - The temporary archive is deleted from both the local and remote machines.
    - The parts of the local file paths relative to local_base_directory are
      copied to the remote machine in remote_base_directory.
    - If archive_prefix is given, entries in the archive are prepended with it.
      This parameter effectively lets you prepend directories to
      remote_base_directory that may not yet exist on the remote machine.
    - The update callback is invoked with four parameters: the current
      status type, the total upload size, the transfer fraction complete, and a
      string describing the estimated time remaining.  Note that if the status
      type is ERROR, the total upload size contains an error message.
    """
def copyBundledFilesToRemoteMachine(tar_path: str, remote_login: RemoteLogin, remote_base_directory: str, update_callback: Callable[[int, str, float, str], object], delete_tarball: bool = False) -> None:
    """Copy a bz2 archive to a remote machine and extract it.

    The local bz2 archive is optionally deleted.  See
    bundleAndCopyFilesToRemoteMachine for a description of the other
    parameters.
    """
def createBZ2Archive(file_paths: Iterable[str], base_directory: str, archive_prefix: str = '', tar_path: str | None = None) -> str:
    """
    Create a bz2 archive file.

    file_paths: A sequence of full paths to the files going in the archive.
    base_directory: Entries in the archive are relative to this directory.
       Each of the entries in file_paths must start with this directory.
    archive_prefix: If given, entries in the archive are prepended with it.
        This parameter effectively lets you prepend directories to
        each file in the archive.
    tar_path: The path to the archive file to create.  If it is None, a path
        to a temporary file is used.
    """
