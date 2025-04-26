import subprocess
from _typeshed import Incomplete
from rez.config import config as config
from rez.exceptions import RezSystemError as RezSystemError
from rez.rex import ActionInterpreter as ActionInterpreter, EscapedString as EscapedString, OutputStyle as OutputStyle, RexExecutor as RexExecutor
from rez.system import system as system
from rez.util import is_non_string_iterable as is_non_string_iterable, shlex_join as shlex_join
from rez.utils.execution import Popen as Popen
from rez.utils.logging_ import print_warning as print_warning
from rez.utils.which import which as which
from typing import Any, Iterable, Self

def get_shell_types() -> list[str]:
    """Returns the available shell types: bash, tcsh etc.

    Returns:
        list[str]: Shells.
    """
def get_shell_class(shell: str | None = None) -> type[Shell]:
    """Get the plugin class associated with the given or current shell.

    Returns:
        type[Shell]: Plugin class for shell.
    """
def create_shell(shell: str | None = None, **kwargs: Any) -> Shell:
    """Returns a Shell of the given or current type.

    Returns:
        Shell: Instance of given shell.
    """

class Shell(ActionInterpreter):
    """Class representing a shell, such as bash or tcsh.
    """
    schema_dict: Incomplete
    @classmethod
    def name(cls) -> str:
        """Plugin name.
        """
    @classmethod
    def executable_name(cls) -> str:
        """Name of executable to create shell instance.
        """
    @classmethod
    def executable_filepath(cls) -> str:
        """Get full filepath to executable, or raise if not found.
        """
    @property
    def executable(self) -> str: ...
    @classmethod
    def is_available(cls) -> bool:
        """Determine if the shell is available to instantiate.

        Returns:
            bool: True if the shell can be created.
        """
    @classmethod
    def file_extension(cls) -> str:
        """Get the file extension associated with the shell.

        Returns:
            str: Shell file extension.
        """
    @classmethod
    def startup_capabilities(cls, rcfile: bool = False, norc: bool = False, stdin: bool = False, command: bool = False):
        """
        Given a set of options related to shell startup, return the actual
        options that will be applied.

        Returns:
            tuple: 4-tuple representing applied value of each option.
        """
    @classmethod
    def get_syspaths(cls) -> None: ...
    _lines: list[Any]
    settings: Any
    def __init__(self) -> None: ...
    def _addline(self, line: str) -> None: ...
    def get_output(self, style: OutputStyle = ...) -> str: ...  # type: ignore[override]
    def new_shell(self) -> Self:
        """Returns A new, reset shell of the same type."""
    @classmethod
    def _unsupported_option(cls, option, val) -> None: ...
    @classmethod
    def _overruled_option(cls, option, overruling_option, val) -> None: ...
    @classmethod
    def find_executable(cls, name: str, check_syspaths: bool = False) -> str:
        """Find an executable.

        Args:
            name (str): Program name.
            check_syspaths (bool): If True, check the standard system paths as
                well, if program was not found on current $PATH.

        Returns:
            str: Full filepath of executable.
        """
    def spawn_shell(self, context_file: str, tmpdir, rcfile: Incomplete | None = None, norc: bool = False, stdin: bool = False, command: Incomplete | None = None, env: Incomplete | None = None, quiet: bool = False, pre_command: Incomplete | None = None, add_rez: bool = True, package_commands_sourced_first: Incomplete | None = None, **Popen_args) -> subprocess.Popen:
        """Spawn a possibly interactive subshell.

        Args:
            context_file: File that must be sourced in the new shell, this
                configures the Rez environment.
            tmpdir: Tempfiles, if needed, should be created within this path.
            rcfile: Custom startup script.
            norc: Don't run startup scripts. Overrides rcfile.
            stdin: If True, read commands from stdin in a non-interactive shell.
                If a different non-False value, such as subprocess.PIPE, the same
                occurs, but stdin is also passed to the resulting subprocess.Popen
                object.
            command: If not None, execute this command in a non-interactive shell.
                If an empty string, don't run a command, but don't open an
                interactive shell either.
            env: Environ dict to execute the shell within; uses the current
                environment if None.
            quiet: If True, don't show the configuration summary, and suppress
                any stdout from startup scripts.
            pre_command: Command to inject before the shell command itself. This
                is for internal use.
            add_rez: If True, assume this shell is being used with rez, and do
                things such as set the prompt etc.
            package_commands_sourced_first: If True, source the context file before
                sourcing startup scripts (such as .bashrc). If False, source
                the context file AFTER. If None, use the configured setting.
            popen_args: args to pass to the shell process object constructor.

        Returns:
            subprocess.Popen: A subprocess.Popen object representing the shell process.
        """
    @classmethod
    def convert_tokens(cls, value) -> str:
        """
        Converts any token like ${VAR} and $VAR to shell specific form.
        Uses the ENV_VAR_REGEX to correctly parse tokens.

        Args:
            value: str to convert

        Returns:
            str with shell specific variables
        """
    @classmethod
    def get_key_token(cls, key) -> str:
        """
        Encodes the environment variable into the shell specific form.
        Shells might implement multiple forms, but the most common/safest
        should be returned here.

        Args:
            key: Variable name to encode

        Returns:
            str of encoded token form
        """
    @classmethod
    def get_all_key_tokens(cls, key: str) -> list[str]:
        """
        Encodes the environment variable into the shell specific forms.
        Shells might implement multiple forms, but the most common/safest
        should be always returned at index 0.

        Args:
            key: Variable name to encode

        Returns:
            list of str with encoded token forms
        """
    @classmethod
    def line_terminator(cls) -> str:
        """
        Returns:
            str: default line terminator
        """
    @classmethod
    def join(cls, command: Iterable[str]) -> str:
        """
        Note: Default to unix sh/bash- friendly behaviour.

        Args:
            command:
                A sequence of program arguments to be joined into a single
                string that can be executed in the current shell.
        Returns:
            A string object representing the command.
        """

class UnixShell(Shell):
    """
    A base class for common \\*nix shells, such as bash and tcsh.
    """
    rcfile_arg: str
    norc_arg: str
    histfile: str
    histvar: str
    command_arg: str
    stdin_arg: str
    last_command_status: str
    syspaths: list[str]
    @classmethod
    def supports_norc(cls) -> bool: ...
    @classmethod
    def supports_command(cls) -> bool: ...
    @classmethod
    def supports_stdin(cls) -> bool: ...
    @classmethod
    def get_startup_sequence(cls, rcfile: str, norc, stdin, command):
        """
        Return a dict containing:

        - 'stdin': resulting stdin setting.
        - 'command': resulting command setting.
        - 'do_rcfile': True if a file should be sourced directly.
        - 'envvar': Env-var that points at a file to source at startup. Can be None.
        - 'files': Existing files that will be sourced (non-user-expanded), in source
            order. This may also incorporate rcfile, and file pointed at via envvar.
            Can be empty.
        - 'bind_files': Files to inject Rez binding into, even if that file doesn't
            already exist.
        - 'source_bind_files': Whether to source bind files, if they exist.
        """
    def spawn_shell(self, context_file, tmpdir, rcfile: Incomplete | None = None, norc: bool = False, stdin: bool = False, command: Incomplete | None = None, env: Incomplete | None = None, quiet: bool = False, pre_command: Incomplete | None = None, add_rez: bool = True, package_commands_sourced_first: Incomplete | None = None, **Popen_args): ...
    def resetenv(self, key, value, friends: Incomplete | None = None) -> None: ...
    def info(self, value: str) -> None: ...
    def error(self, value: str) -> None: ...
    def command(self, value) -> None: ...
    def comment(self, value) -> None: ...
    def shebang(self) -> None: ...
    @classmethod
    def get_all_key_tokens(cls, key): ...
    @classmethod
    def line_terminator(cls) -> str: ...
