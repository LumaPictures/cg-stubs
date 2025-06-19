from _typeshed import Incomplete
from rez import __version__ as __version__
from rez.exceptions import RezSystemError as RezSystemError
from rez.utils.data_utils import cached_property as cached_property
from rez.utils.platform_ import platform_ as platform_

class System:
    """Access to underlying system data.
    """
    @property
    def rez_version(self):
        """Returns the current version of Rez."""
    @cached_property
    def platform(self):
        """Get the current platform.

        Returns:
            The current platform (windows, linux, osx, etc).
        """
    @cached_property
    def arch(self):
        """Get the current architecture.

        Returns:
            The current architecture (x86_64, i386, etc).
        """
    @cached_property
    def os(self):
        """Get the current operating system.

        Returns:
            The current operating system (Ubuntu-22.04, CentOS-7.8, windows-6.1.7600.sp1, etc).
        """
    @cached_property
    def variant(self):
        '''Returns a list of the form ``["platform-X", "arch-X", "os-X"]`` suitable
        for use as a variant in a system-dependent package.
        '''
    @cached_property
    def shell(self) -> str:
        '''Get the current shell.

        Returns:
            The current shell this process is running in (bash, tcsh, pwsh, etc). On Windows,
            the return value is always "powershell".
        '''
    @cached_property
    def user(self):
        """Get the current user."""
    @cached_property
    def home(self):
        """Get the home directory for the current user."""
    @cached_property
    def fqdn(self):
        """
        Returns the fully qualified domain name (FQDN) of the current machine, eg ``somesvr.somestudio.com``.
        """
    @cached_property
    def hostname(self):
        """
        Returns the machine hostname, eg ``somesvr``.
        """
    @cached_property
    def domain(self):
        """
        Returns the domain, eg ``somestudio.com``.
        """
    @cached_property
    def rez_bin_path(self):
        """Get path containing rez binaries, or None if no binaries are
        available, or Rez is not a production install.
        """
    @property
    def is_production_rez_install(self):
        """Return True if this is a production rez install."""
    @property
    def selftest_is_running(self):
        """Return True if tests are running via ``rez-selftest`` tool."""
    def get_summary_string(self):
        """Get a string summarising the state of Rez as a whole.
        """
    def clear_caches(self, hard: bool = False) -> None:
        """Clear all caches in Rez.

        Rez caches package contents and iteration during a python session. Thus
        newly released packages, and changes to existing packages, may not be
        picked up. You need to clear the cache for these changes to become
        visible.

        Args:
            hard (bool): Perform a 'hard' cache clear. This just means that the
                memcached cache is also cleared. Generally this is not needed.
                This option is for debugging purposes.
        """
    @classmethod
    def _make_safe_version_string(cls, s): ...

system: Incomplete
