from _typeshed import Incomplete
from rez.exceptions import RezSystemError as RezSystemError
from rez.util import which as which
from rez.utils.data_utils import cached_property as cached_property
from rez.utils.execution import Popen as Popen
from rez.utils.platform_mapped import platform_mapped as platform_mapped

class Platform:
    """Abstraction of a platform.
    """
    name: str
    def __init__(self) -> None: ...
    @cached_property
    @platform_mapped
    def arch(self):
        """Returns the name of the architecture."""
    @cached_property
    @platform_mapped
    def os(self):
        """Returns the name of the operating system."""
    @cached_property
    def terminal_emulator_command(self):
        """Returns the command to use to run another command in a separate
        terminal emulator.

        The command is expected to have the target command and arguments
        appended to it.

        Returns:
            List of strings, or None if the terminal emulator could not be
            determined.
        """
    @cached_property
    def new_session_popen_args(self):
        """Return the arguments to pass to subprocess.Popen in order to execute
        a shell in a new process group.

        Returns:
            Dict: kwargs to pass to subprocess.Popen.
        """
    @cached_property
    def image_viewer(self):
        """Returns the system default image viewer.

        If None, rez will use the web browser to display images.
        """
    @cached_property
    def editor(self):
        """Returns the system default text editor."""
    @cached_property
    def difftool(self):
        """Return the system default file diff tool."""
    @cached_property
    def tmpdir(self):
        """Return system default temporary directory path."""
    @cached_property
    def physical_cores(self):
        """Return the number of physical cpu cores on the system."""
    @cached_property
    def logical_cores(self):
        """Return the number of cpu cores as reported to the os.

        May be different from physical_cores if, ie, intel's hyperthreading is
        enabled.
        """
    @property
    def has_case_sensitive_filesystem(self) -> bool: ...
    def _arch(self): ...
    def _os(self) -> None: ...
    def _terminal_emulator_command(self) -> None: ...
    def _new_session_popen_args(self) -> None: ...
    def _image_viewer(self) -> None: ...
    def _editor(self) -> None: ...
    def _difftool(self) -> None: ...
    def _tmpdir(self): ...
    def symlink(self, source, link_name) -> None:
        """Create a symbolic link pointing to source named link_name."""
    def _physical_cores_base(self): ...
    def _physical_cores(self) -> None: ...
    def _logical_cores(self): ...

class _UnixPlatform(Platform):
    def _new_session_popen_args(self): ...

class LinuxPlatform(_UnixPlatform):
    name: str
    def _os(self):
        """
        Note: We cannot replace this with 'distro.linux_distribution' in
        entirety as unfortunately there are slight differences. Eg our code
        gives 'Ubuntu-16.04' whereas distro gives 'ubuntu-16.04'.
        """
    def _terminal_emulator_command(self): ...
    def _image_viewer(self): ...
    def _editor(self): ...
    def _difftool(self): ...
    @classmethod
    def _parse_colon_table_to_dict(cls, table_text):
        '''Given a simple text output where each line gives a key-value pair
      of the form "key: value", parse and return a dict'''
    def _physical_cores_from_cpuinfo(self): ...
    def _physical_cores_from_lscpu(self): ...
    def _physical_cores(self): ...

class OSXPlatform(_UnixPlatform):
    name: str
    def _os(self) -> str: ...  # type: ignore[override]
    def _terminal_emulator_command(self): ...
    def _image_viewer(self) -> str: ...  # type: ignore[override]
    def _editor(self) -> str: ...  # type: ignore[override]
    def _physical_cores_from_osx_sysctl(self): ...
    def _physical_cores(self): ...
    def _difftool(self): ...

class WindowsPlatform(Platform):
    name: str
    def _os(self) -> str: ...  # type: ignore[override]
    @property
    def has_case_sensitive_filesystem(self) -> bool: ...
    def _image_viewer(self) -> str: ...  # type: ignore[override]
    def _editor(self) -> str: ...  # type: ignore[override]
    def _new_session_popen_args(self): ...
    def symlink(self, source, link_name) -> None: ...
    def _terminal_emulator_command(self) -> str: ...  # type: ignore[override]
    def _physical_cores_from_wmic(self): ...
    def _physical_cores(self): ...
    def _difftool(self): ...

platform_: Platform
name: Incomplete
