from _typeshed import FileDescriptorLike as FileDescriptorLike, HasFileno
from collections.abc import Callable, Container, Mapping
from types import FrameType, TracebackType
from typing import NoReturn, Protocol, Self

from typing import TypeAlias
from typing import TypeAlias
import signal
_SignalHandler: TypeAlias = Callable[[int, FrameType | None], object] | int | signal.Handlers | None
_SignalTarget: TypeAlias = _SignalHandler | str
class _PidFile(Protocol):
    def __enter__(self) -> object: ...
    def __exit__(self) -> object: ...

class DaemonError(Exception):
    """ Base exception class for errors from this module. """
class DaemonOSEnvironmentError(DaemonError, OSError):
    """ Exception raised when daemon OS environment setup receives error. """
class DaemonProcessDetachError(DaemonError, OSError):
    """ Exception raised when process detach fails. """

class DaemonContext:
    """ Context for turning the current program into a daemon process.

        A `DaemonContext` instance represents the behaviour settings and
        process context for the program when it becomes a daemon. The
        behaviour and environment is customised by setting options on the
        instance, before calling the `open` method.

        Each option can be passed as a keyword argument to the `DaemonContext`
        constructor, or subsequently altered by assigning to an attribute on
        the instance at any time prior to calling `open`. That is, for
        options named `wibble` and `wubble`, the following invocation::

            foo = daemon.DaemonContext(wibble=bar, wubble=baz)
            foo.open()

        is equivalent to::

            foo = daemon.DaemonContext()
            foo.wibble = bar
            foo.wubble = baz
            foo.open()

        The following options are defined.

        `files_preserve`
            :Default: ``None``

            List of files that should *not* be closed when starting the
            daemon. If ``None``, all open file descriptors will be closed.

            Elements of the list are file descriptors (as returned by a file
            object's `fileno()` method) or Python `file` objects. Each
            specifies a file that is not to be closed during daemon start.

        `chroot_directory`
            :Default: ``None``

            Full path to a directory to set as the effective root directory of
            the process. If ``None``, specifies that the root directory is not
            to be changed.

        `working_directory`
            :Default: ``'/'``

            Full path of the working directory to which the process should
            change on daemon start.

            Since a filesystem cannot be unmounted if a process has its
            current working directory on that filesystem, this should either
            be left at default or set to a directory that is a sensible “home
            directory” for the daemon while it is running.

        `umask`
            :Default: ``0``

            File access creation mask (“umask”) to set for the process on
            daemon start.

            Since a process inherits its umask from its parent process,
            starting the daemon will reset the umask to this value so that
            files are created by the daemon with access modes as it expects.

        `pidfile`
            :Default: ``None``

            Context manager for a PID lock file. When the daemon context opens
            and closes, it enters and exits the `pidfile` context manager.

        `detach_process`
            :Default: ``None``

            If ``True``, detach the process context when opening the daemon
            context; if ``False``, do not detach.

            If unspecified (``None``) during initialisation of the instance,
            this will be set to ``True`` by default, and ``False`` only if
            detaching the process is determined to be redundant; for example,
            in the case when the process was started by `init`, by `initd`, or
            by `inetd`.

        `signal_map`
            :Default: system-dependent

            Mapping from operating system signals to callback actions.

            The mapping is used when the daemon context opens, and determines
            the action for each signal's signal handler:

            * A value of ``None`` will ignore the signal (by setting the
              signal action to ``signal.SIG_IGN``).

            * A string value will be used as the name of an attribute on the
              ``DaemonContext`` instance. The attribute's value will be used
              as the action for the signal handler.

            * Any other value will be used as the action for the signal
              handler.

            The default value depends on which signals are defined on the
            running system. Each item from the list below whose signal is
            actually defined in the ``signal`` module will appear in the
            default map:

            * ``signal.SIGCLD``: ``None``

            * ``signal.SIGTTIN``: ``None``

            * ``signal.SIGTTOU``: ``None``

            * ``signal.SIGTSTP``: ``None``

            * ``signal.SIGTERM``: ``'terminate'``

        `uid`
            :Default: ``os.getuid()``

        `gid`
            :Default: ``os.getgid()``

            The user ID (“UID”) value and group ID (“GID”) value to switch
            the process to on daemon start.

            The default values, the real UID and GID of the process, will
            relinquish any effective privilege elevation inherited by the
            process.

        `prevent_core`
            :Default: ``True``

            If true, prevents the generation of core files, in order to avoid
            leaking sensitive information from daemons run as `root`.

        `stdin`
            :Default: ``None``

        `stdout`
            :Default: ``None``

        `stderr`
            :Default: ``None``

            Each of `stdin`, `stdout`, and `stderr` is a file-like object
            which will be used as the new file for the standard I/O stream
            `sys.stdin`, `sys.stdout`, and `sys.stderr` respectively. The file
            should therefore be open, with a minimum of mode 'r' in the case
            of `stdin`, and mode 'w+' in the case of `stdout` and `stderr`.

            If the object has a `fileno()` method that returns a file
            descriptor, the corresponding file will be excluded from being
            closed during daemon start (that is, it will be treated as though
            it were listed in `files_preserve`).

            If ``None``, the corresponding system stream is re-bound to the
            file named by `os.devnull`.

        """
    chroot_directory: str | None
    working_directory: str
    umask: int
    files_preserve: list[FileDescriptorLike | None] | None
    pidfile: _PidFile | None
    stdin: HasFileno | None
    stdout: HasFileno | None
    stderr: HasFileno | None
    uid: int
    gid: int
    detach_process: bool
    signal_map: Mapping[int, _SignalTarget]
    @staticmethod
    def registerPreOpenCallback(func: Callable[[DaemonContext], object]) -> None: ...
    @staticmethod
    def registerPostOpenCallback(func: Callable[[DaemonContext], object]) -> None: ...
    def __init__(self, chroot_directory: str | None = None, working_directory: str = '/', umask: int = 0, uid: int | None = None, gid: int | None = None, detach_process: bool | None = None, files_preserve: list[FileDescriptorLike | None] | None = None, pidfile: _PidFile | None = None, stdin: HasFileno | None = None, stdout: HasFileno | None = None, stderr: HasFileno | None = None, signal_map: Mapping[int, _SignalTarget] | None = None) -> None:
        """ Set up a new instance. """
    @property
    def is_open(self) -> bool:
        """ ``True`` if the instance is currently open. """
    def open(self) -> None:
        """ Become a daemon process.
            :Return: ``None``

            Open the daemon context, turning the current program into a daemon
            process. This performs the following steps:

            * If this instance's `is_open` property is true, return
              immediately. This makes it safe to call `open` multiple times on
              an instance.

            * If the `prevent_core` attribute is true, set the resource limits
              for the process to prevent any core dump from the process.

            * If the `chroot_directory` attribute is not ``None``, set the
              effective root directory of the process to that directory (via
              `os.chroot`).

              This allows running the daemon process inside a “chroot gaol”
              as a means of limiting the system's exposure to rogue behaviour
              by the process. Note that the specified directory needs to
              already be set up for this purpose.

            * Set the process UID and GID to the `uid` and `gid` attribute
              values.

            * Close all open file descriptors. This excludes those listed in
              the `files_preserve` attribute, and those that correspond to the
              `stdin`, `stdout`, or `stderr` attributes.

            * Change current working directory to the path specified by the
              `working_directory` attribute.

            * Reset the file access creation mask to the value specified by
              the `umask` attribute.

            * If the `detach_process` option is true, detach the current
              process into its own process group, and disassociate from any
              controlling terminal.

            * Set signal handlers as specified by the `signal_map` attribute.

            * If any of the attributes `stdin`, `stdout`, `stderr` are not
              ``None``, bind the system streams `sys.stdin`, `sys.stdout`,
              and/or `sys.stderr` to the files represented by the
              corresponding attributes. Where the attribute has a file
              descriptor, the descriptor is duplicated (instead of re-binding
              the name).

            * If the `pidfile` attribute is not ``None``, enter its context
              manager.

            * Mark this instance as open (for the purpose of future `open` and
              `close` calls).

            * Register the `close` method to be called during Python's exit
              processing.

            When the function returns, the running program is a daemon
            process.

            """
    def __enter__(self) -> Self:
        """ Context manager entry point. """
    def close(self) -> None:
        """ Exit the daemon process context.
            :Return: ``None``

            Close the daemon context. This performs the following steps:

            * If this instance's `is_open` property is false, return
              immediately. This makes it safe to call `close` multiple times
              on an instance.

            * If the `pidfile` attribute is not ``None``, exit its context
              manager.

            * Mark this instance as closed (for the purpose of future `open`
              and `close` calls).

            """
    def __exit__(self, exc_type: type[BaseException] | None, exc_value: BaseException | None, traceback: TracebackType | None) -> None:
        """ Context manager exit point. """
    def terminate(self, signal_number: int, stack_frame: FrameType | None) -> NoReturn:
        """ Signal handler for end-process signals.
            :Return: ``None``

            Signal handler for the ``signal.SIGTERM`` signal. Performs the
            following step:

            * Raise a ``SystemExit`` exception explaining the signal.

            """

def change_working_directory(directory: str) -> None:
    """ Change the working directory of this process.
        """
def change_root_directory(directory: str) -> None:
    """ Change the root directory of this process.

        Sets the current working directory, then the process root
        directory, to the specified `directory`. Requires appropriate
        OS privileges for this process.

        """
def change_file_creation_mask(mask: int) -> None:
    """ Change the file creation mask for this process.
        """
def change_process_owner(uid: int, gid: int) -> None:
    """ Change the owning UID and GID of this process.

        Sets the GID then the UID of the process (in that order, to
        avoid permission errors) to the specified `gid` and `uid`
        values. Requires appropriate OS privileges for this process.

        """
def prevent_core_dump() -> None:
    """ Prevent this process from generating a core dump.

        Sets the soft and hard limits for core dump size to zero. On
        Unix, this prevents the process from creating core dump
        altogether.

        """
def detach_process_context() -> None:
    """ Detach the process context from parent and session.

        Detach from the parent process and session group, allowing the
        parent to exit while this process continues running.

        Reference: “Advanced Programming in the Unix Environment”,
        section 13.3, by W. Richard Stevens, published 1993 by
        Addison-Wesley.
    
        """
def is_process_started_by_init() -> bool:
    """ Determine if the current process is started by `init`.

        The `init` process has the process ID of 1; if that is our
        parent process ID, return ``True``, otherwise ``False``.
    
        """
def is_socket(fd: int) -> bool:
    """ Determine if the file descriptor is a socket.

        Return ``False`` if querying the socket type of `fd` raises an
        error; otherwise return ``True``.

        """
def is_process_started_by_superserver() -> bool:
    """ Determine if the current process is started by the superserver.

        The internet superserver creates a network socket, and
        attaches it to the standard streams of the child process. If
        that is the case for this process, return ``True``, otherwise
        ``False``.
    
        """
def is_detach_process_context_required() -> bool:
    """ Determine whether detaching process context is required.

        Return ``True`` if the process environment indicates the
        process is already detached:

        * Process was started by `init`; or

        * Process was started by `inetd`.

        """
def close_file_descriptor_if_open(fd: int) -> None:
    """ Close a file descriptor if already open.

        Close the file descriptor `fd`, suppressing an error in the
        case the file was not open.

        """

MAXFD: int

def get_maximum_file_descriptors() -> int:
    """ Return the maximum number of open file descriptors for this process.

        Return the process hard resource limit of maximum number of
        open file descriptors. If the limit is “infinity”, a default
        value of ``MAXFD`` is returned.

        """
def close_all_open_files(exclude: Container[int] = ...) -> None:
    """ Close all open file descriptors.

        Closes every file descriptor (if open) of this process. If
        specified, `exclude` is a set of file descriptors to *not*
        close.

        """
def redirect_stream(system_stream: HasFileno, target_stream: HasFileno | None) -> None:
    """ Redirect a system stream to a specified file.

        `system_stream` is a standard system stream such as
        ``sys.stdout``. `target_stream` is an open file object that
        should replace the corresponding system stream object.

        If `target_stream` is ``None``, defaults to opening the
        operating system's null device and using its file descriptor.

        """
def make_default_signal_map() -> dict[int, str | None]:
    """ Make the default signal map for this system.

        The signals available differ by system. The map will not
        contain any signals not defined on the running system.

        """
def set_signal_handlers(signal_handler_map: Mapping[int, _SignalHandler]) -> None:
    """ Set the signal handlers as specified.

        The `signal_handler_map` argument is a map from signal number
        to signal handler. See the `signal` module for details.

        """
def register_atexit_function(func: Callable[[], object]) -> None:
    """ Register a function for processing at program exit.

        The function `func` is registered for a call with no arguments
        at program exit.

        """
