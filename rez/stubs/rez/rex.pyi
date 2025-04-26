import _collections_abc
import os
import rez.rex
from _typeshed import Incomplete
from collections.abc import Generator, MutableMapping
from contextlib import contextmanager
from enum import Enum
from rez.config import config as config
from rez.exceptions import RexError as RexError, RexUndefinedVariableError as RexUndefinedVariableError, RezSystemError as RezSystemError, _NeverError as _NeverError
from rez.system import system as system
from rez.util import is_non_string_iterable as is_non_string_iterable, shlex_join as shlex_join
from rez.utils import reraise as reraise
from rez.utils.data_utils import AttrDictWrapper as AttrDictWrapper
from rez.utils.execution import Popen as Popen
from rez.utils.formatting import expandvars as expandvars
from rez.utils.platform_ import platform_ as platform_
from rez.utils.sourcecode import SourceCode as SourceCode, SourceCodeError as SourceCodeError
from string import Formatter
from typing import Any, Callable, Iterable

class Action:
    name: str
    _registry: Incomplete
    args: tuple[Any, ...]
    def __init__(self, *args) -> None: ...
    def __repr__(self) -> str: ...
    def __eq__(self, other): ...
    @classmethod
    def register_command_type(cls, name, klass) -> None: ...
    @classmethod
    def register(cls) -> None: ...
    @classmethod
    def get_command_types(cls): ...

class EnvAction(Action):
    @property
    def key(self) -> str: ...
    @property
    def value(self) -> str | None: ...

class Unsetenv(EnvAction):
    name: str

class Setenv(EnvAction):
    name: str
    args: Incomplete
    def pre_exec(self, interpreter) -> None: ...
    def post_exec(self, interpreter, result): ...

class Resetenv(EnvAction):
    name: str
    @property
    def friends(self): ...
    args: Incomplete
    def pre_exec(self, interpreter) -> None: ...
    def post_exec(self, interpreter, result): ...

class Prependenv(Setenv):
    name: str

class Appendenv(Setenv):
    name: str

class Alias(Action):
    name: str

class Info(Action):
    name: str

class Error(Action):
    name: str

class Stop(Action):
    name: str

class Command(Action):
    name: str

class Comment(Action):
    name: str

class Source(Action):
    name: str

class Shebang(Action):
    name: str

class OutputStyle(Enum):
    """ Enum to represent the style of code output when using Rex.
    """
    file = ('Code as it would appear in a script file.',)
    eval = ('Code in a form that can be evaluated.',)

class ActionManager:
    """Handles the execution book-keeping.  Tracks env variable values, and
    triggers the callbacks of the `ActionInterpreter`.
    """
    interpreter: rez.rex.ActionInterpreter
    verbose: bool
    parent_environ: os._Environ[str] | dict[str, str]
    parent_variables: set[str]
    environ: dict[Any, Any]
    formatter: Any | Overload(Callable[[object], str], Callable[[_collections_abc.Buffer, str, str], str])  # type: ignore[valid-type]
    actions: list[Any]
    _env_sep_map: Any
    def __init__(self, interpreter: ActionInterpreter, parent_environ: dict[str, str] | None = None, parent_variables: Iterable[str] | None = None, formatter: Incomplete | None = None, verbose: bool = False, env_sep_map: Incomplete | None = None) -> None:
        """
        interpreter: string or `ActionInterpreter`
            the interpreter to use when executing rex actions
        parent_environ: environment to execute the actions within. If None,
            defaults to the current environment.
        parent_variables: List of variables to append/prepend to, rather than
            overwriting on first reference. If this is set to True instead of a
            list, all variables are treated as parent variables.
        formatter: func or None
            function to use for formatting string values
        verbose : bool or list of str
            if True, causes commands to print additional feedback (using info()).
            can also be set to a list of strings matching command names to add
            verbosity to only those commands.
        """
    def get_action_methods(self):
        """
        return a list of methods on this class for executing actions.
        methods are return as a list of (name, func) tuples
        """
    def get_public_methods(self):
        """
        return a list of methods on this class which should be exposed in the rex
        API.
        """
    def _env_sep(self, name): ...
    def _is_verbose(self, command): ...
    def _format(self, value): ...
    def _expand(self, value): ...
    def _key(self, key): ...
    def _value(self, value): ...
    def get_output(self, style=...): ...
    def undefined(self, key) -> bool: ...
    def defined(self, key) -> bool: ...
    def expandvars(self, value, format: bool = True): ...
    def getenv(self, key): ...
    def setenv(self, key, value) -> None: ...
    def unsetenv(self, key) -> None: ...
    def resetenv(self, key, value, friends: Incomplete | None = None) -> None: ...
    def _pendenv(self, key, value, action, interpfunc, addfunc) -> None: ...
    def prependenv(self, key, value) -> None: ...
    def appendenv(self, key, value) -> None: ...
    def alias(self, key, value) -> None: ...
    def info(self, value: str = '') -> None: ...
    def error(self, value) -> None: ...
    def stop(self, msg, *nargs) -> None: ...
    def command(self, value) -> None: ...
    def comment(self, value) -> None: ...
    def source(self, value) -> None: ...
    def shebang(self) -> None: ...
    def _keytoken(self, key): ...

class ActionInterpreter:
    '''
    Abstract base class that provides callbacks for rex Actions.  This class
    should not be used directly. Its methods are called by the
    `ActionManager` in response to actions issued by user code written using
    the rex python API.

    Sub-classes should override the `get_output` method to return
    implementation-specific data structure.  For example, an interpreter for a
    shell language like bash would return a string of shell code.  An interpreter
    for an active python session might return a dictionary of the modified
    environment.

    Sub-classes can override the `expand_env_vars` class variable to instruct
    the `ActionManager` whether or not to expand the value of environment
    variables which reference other variables (e.g. "this-${THAT}").
    '''
    expand_env_vars: bool
    pathsep: Incomplete
    ENV_VAR_REGEX: Incomplete
    def get_output(self, style=...) -> None:
        """Returns any implementation specific data.

        Args:
            style (`OutputStyle`): Style affecting output format.

        Returns:
            Depends on implementation, but usually a code string.
        """
    def setenv(self, key, value) -> None: ...
    def unsetenv(self, key) -> None: ...
    def resetenv(self, key, value, friends: Incomplete | None = None) -> None: ...
    def prependenv(self, key, value) -> None:
        """This is optional, but if it is not implemented, you must
        implement setenv."""
    def appendenv(self, key, value) -> None:
        """This is optional, but if it is not implemented, you must
        implement setenv."""
    def alias(self, key, value) -> None: ...
    def info(self, value: str): ...
    def error(self, value: str): ...
    def command(self, value) -> None: ...
    def comment(self, value) -> None: ...
    def source(self, value) -> None: ...
    def shebang(self) -> None: ...
    def escape_string(self, value, is_path: bool = False):
        """Escape a string.

        Escape the given string so that special characters (such as quotes and
        whitespace) are treated properly. If `value` is a string, assume that
        this is an expandable string in this interpreter.

        Note that `is_path` provided because of the special case where a
        path-like envvar is set. In this case, path normalization, if it needs
        to occur, has to be part of the string escaping process.

        Note:
            This default implementation returns the string with no escaping
            applied.

        Args:
            value (str or `EscapedString`): String to escape.
            is_path (bool): True if the value is path-like.

        Returns:
            str: The escaped string.
        """
    @classmethod
    def _is_pathed_key(cls, key): ...
    def normalize_path(self, path):
        """Normalize a path.

        Change `path` to a valid filepath representation for this interpreter.

        IMPORTANT: Because var references like ${THIS} might be passed to funcs
        like appendvar, `path` might be in this form. You need to take that
        into account (ie, ensure normalization doesn't break such a var reference).

        Args:
            path (str): A filepath which may be in posix format, or windows
                format, or some combination of the two. For eg, a string like
                `{root}/bin` on windows will evaluate to `C:\\.../bin` - in this
                case, the `cmd` shell would want to normalize this and convert
                to all forward slashes.

        Returns:
            str: The normalized path.
        """
    def normalize_paths(self, value):
        """Normalize value if it's a path(s).

        Note that `value` may be more than one pathsep-delimited paths.
        """
    def _saferefenv(self, key) -> None:
        """
        make the var safe to reference, even if it does not yet exist. This is
        needed because of different behaviours in shells - eg, tcsh will fail
        on ref to undefined var, but sh will expand to the empty string.
        """
    def _bind_interactive_rez(self) -> None:
        """
        apply changes to the env needed to expose rez in an interactive shell,
        for eg prompt change, sourcing completion scripts etc. Do NOT add rez
        to PATH, this is done elsewhere.
        """

class Python(ActionInterpreter):
    """Execute commands in the current python session"""
    expand_env_vars: bool
    passive: bool
    manager: rez.rex.ActionManager | None
    target_environ: os._Environ[str]
    update_session: bool
    def __init__(self, target_environ: Incomplete | None = None, passive: bool = False) -> None:
        """
        target_environ: dict
            If target_environ is None or os.environ, interpreted actions are
            applied to the current python interpreter. Otherwise, changes are
            only applied to target_environ. In either case you must call
            `apply_environ` to flush all changes to the target environ dict.

        passive: bool
            If True, commands that do not update the environment (such as info)
            are skipped.
        """
    def set_manager(self, manager: ActionManager) -> None: ...
    def apply_environ(self) -> None:
        """Apply changes to target environ.
        """
    def get_output(self, style=...): ...
    def setenv(self, key, value) -> None: ...
    def unsetenv(self, key) -> None: ...
    def resetenv(self, key, value, friends: Incomplete | None = None) -> None: ...
    def prependenv(self, key, value) -> None: ...
    def appendenv(self, key, value) -> None: ...
    def info(self, value) -> None: ...
    def error(self, value) -> None: ...
    def subprocess(self, args, **subproc_kwargs): ...
    def command(self, value) -> None: ...
    def comment(self, value) -> None: ...
    def source(self, value) -> None: ...
    def alias(self, key, value) -> None: ...
    def _bind_interactive_rez(self) -> None: ...
    def _saferefenv(self, key) -> None: ...
    def shebang(self) -> None: ...
    def get_key_token(self, key) -> str: ...
    def adjust_env_for_platform(self, env) -> None:
        """ Make required platform-specific adjustments to env.
        """
    def _add_systemroot_to_env_win32(self, env) -> None:
        """ Sets ``%SYSTEMROOT%`` environment variable, if not present
        in :py:attr:`target_environ` .

        Args:
            env (dict): desired environment variables

        Notes:
            on windows, python-3.6 startup fails within an environment
            where it ``%PATH%`` includes python3, but ``%SYSTEMROOT%`` is not
            present.

            for example.

            .. code-block:: python

                from subprocess import Popen
                cmds = ['python', '--version']

                # successful
                Popen(cmds)
                Popen(cmds, env={'PATH': 'C:\\\\Python-3.6.5',
                                 'SYSTEMROOT': 'C:\\Windows'})

                # failure
                Popen(cmds, env={'PATH': 'C:\\\\Python-3.6.5'})

                #> Fatal Python Error: failed to get random numbers to initialize Python

        """

class EscapedString:
    '''Class for constructing literal or expandable strings, or a combination
    of both.

    This determines how a string is escaped in an interpreter. For example,
    the following rex commands may result in the bash code shown:

        >>> env.FOO = literal(\'oh "noes"\')
        >>> env.BAH = expandable(\'oh "noes"\')
        export FOO=\'oh "noes"\'
        export BAH="oh "noes""

    You do not need to use `expandable` - a string by default is interpreted as
    expandable. However you can mix literals and expandables together, like so:

        >>> env.FOO = literal("hello").expandable(" ${DUDE}")
        export FOO=\'hello\'" ${DUDE}"

    Shorthand methods `e` and `l` are also supplied, for better readability:

        >>> env.FOO = literal("hello").e(" ${DUDE}").l(", and welcome!")
        export FOO=\'hello\'" ${DUDE}"\', and welcome!\'

    Note:
        you can use the `literal` and `expandable` free functions, rather than
        constructing a class instance directly.
    '''
    strings: list[tuple[bool, Any]]
    def __init__(self, value, is_literal: bool = False) -> None: ...
    def copy(self): ...
    def literal(self, value): ...
    def expandable(self, value): ...
    def l(self, value): ...
    def e(self, value): ...
    def _add(self, value, is_literal) -> None: ...
    def __str__(self) -> str:
        """Return the string unescaped."""
    def __repr__(self) -> str: ...
    def __eq__(self, other): ...
    def __ne__(self, other) -> bool: ...
    def __add__(self, other):
        """Join two escaped strings together.

        Returns:
            `EscapedString` object.
        """
    def expanduser(self):
        """Analogous to os.path.expanduser.

        Returns:
            `EscapedString` object with expanded '~' references.
        """
    def formatted(self, func):
        """Return the string with non-literal parts formatted.

        Args:
            func (typing.Callable): Callable that translates a string into a
                formatted string.

        Returns:
            `EscapedString` object.
        """
    def split(self, delimiter: Incomplete | None = None):
        """Same as string.split(), but retains literal/expandable structure.

        Returns:
            List of `EscapedString`.
        """
    @classmethod
    def join(cls, sep, values): ...
    @classmethod
    def promote(cls, value): ...
    @classmethod
    def demote(cls, value): ...
    @classmethod
    def disallow(cls, value): ...

def literal(value):
    """Creates a literal string."""
def expandable(value):
    """Creates an expandable string."""
def optionvars(name, default: Incomplete | None = None):
    """Access arbitrary data from rez config setting 'optionvars'.

    Args:
        name (str): Name of the optionvar. Use dot notation for values in
            nested dicts.
        default (object): Default value if setting is missing.
    """

class NamespaceFormatter(Formatter):
    """String formatter that, as well as expanding '{variable}' strings, also
    protects environment variable references such as ${THIS} so they do not get
    expanded as though {THIS} is a formatting target. Also, environment variable
    references such as $THIS are converted to ${THIS}, which gives consistency
    across shells, and avoids some problems with non-curly-braced variables in
    some situations.
    """
    initial_namespace: Any
    namespace: Any
    def __init__(self, namespace) -> None: ...
    def format(self, format_string, *args, **kwargs): ...  # type: ignore[override]
    def format_field(self, value, format_spec): ...
    def get_value(self, key, args, kwds): ...

class EnvironmentDict(MutableMapping):
    """
    Provides a mapping interface to `EnvironmentVariable` instances,
    which provide an object-oriented interface for recording environment
    variable manipulations.

    `__getitem__` is always guaranteed to return an `EnvironmentVariable`
    instance: it will not raise a KeyError.
    """
    manager: Any
    _var_cache: dict[Any, Any]
    def __init__(self, manager) -> None:
        """Creates an `EnvironmentDict`.

        Args:
            override_existing_lists (bool): If True, the first call to append
                or prepend will override the value in `environ` and effectively
                act as a setenv operation. If False, pre-existing values will
                be appended/prepended to as usual.
        """
    def keys(self): ...
    def __repr__(self) -> str: ...
    def __getitem__(self, key): ...
    def __setitem__(self, key, value) -> None: ...
    def __contains__(self, key) -> bool: ...
    def __delitem__(self, key) -> None: ...
    def __iter__(self): ...
    def __len__(self) -> int: ...

class EnvironmentVariable:
    """
    class representing an environment variable

    combined with EnvironmentDict class, records changes to the environment
    """
    _name: Any
    _environ_map: Any
    def __init__(self, name, environ_map) -> None: ...
    @property
    def name(self): ...
    def prepend(self, value) -> None: ...
    def append(self, value) -> None: ...
    def reset(self, value, friends: Incomplete | None = None) -> None: ...
    def set(self, value) -> None: ...
    def unset(self) -> None: ...
    def get(self): ...
    def value(self): ...
    def setdefault(self, value) -> None:
        """set value if the variable does not yet exist"""
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def __bool__(self) -> bool: ...
    def __eq__(self, value): ...
    def __ne__(self, value) -> bool: ...

class RexExecutor:
    """
    Runs an interpreter over code within the given namespace. You can also access
    namespaces and rex functions directly in the executor, like so:

    RexExecutor ex()
    ex.setenv('FOO', 'BAH')
    ex.env.FOO_SET = 1
    ex.alias('foo','foo -l')
    """
    globals: Any | dict[Any, Any]
    formatter: rez.rex.NamespaceFormatter
    manager: rez.rex.ActionManager
    environ: rez.rex.EnvironmentDict
    def __init__(self, interpreter: ActionInterpreter | None = None, globals_map: Incomplete | None = None, parent_environ: dict[str, str] | None = None, parent_variables: Incomplete | None = None, shebang: bool = True, add_default_namespaces: bool = True) -> None:
        """
        interpreter: `ActionInterpreter` or None
            the interpreter to use when executing rex actions. If None, creates
            a python interpreter with an empty target environment dict.
        globals_map : dict or None
            dictionary which comprises the main python namespace when rex code
            is executed (via the python `exec` statement). if None, defaults
            to empty dict.
        parent_environ: environment to execute the rex code within. If None, defaults
            to the current environment.
        parent_variables: List of variables to append/prepend to, rather than
            overwriting on first reference. If this is set to True instead of a
            list, all variables are treated as parent variables.
        shebang: bool
            if True, apply a shebang to the result.
        add_default_namespaces: bool
            whether to add default namespaces such as 'system'.
        """
    @property
    def interpreter(self): ...
    @property
    def actions(self):
        """List of Action objects that will be executed."""
    def __getattr__(self, attr):
        """Allows for access such as: self.setenv('FOO','bah')."""
    def bind(self, name, obj) -> None:
        """Binds an object to the execution context.

        Args:
            name (str) Variable name to bind to.
            obj (object): Object to bind.
        """
    def unbind(self, name) -> None:
        """Unbind an object from the execution context.

        Has no effect if the binding does not exist.

        Args:
            name (str) Variable name to bind to.
        """
    @contextmanager
    def reset_globals(self) -> Generator[None]:
        """Remove changes to globals dict post-context.

        Any bindings (self.bind) will only be visible during this context.
        """
    def append_system_paths(self) -> None:
        """Append system paths to $PATH."""
    def prepend_rez_path(self) -> None:
        """Prepend rez path to $PATH."""
    def append_rez_path(self) -> None:
        """Append rez path to $PATH."""
    def normalize_path(self, path):
        """Normalize a path.

        Note that in many interpreters this will be unchanged.

        Returns:
            str: The normalized path.
        """
    @classmethod
    def compile_code(cls, code, filename: Incomplete | None = None, exec_namespace: Incomplete | None = None):
        """Compile and possibly execute rex code.

        Args:
            code (str or SourceCode): The python code to compile.
            filename (str): File to associate with the code, will default to
                '<string>'.
            exec_namespace (dict): Namespace to execute the code in. If None,
                the code is not executed.

        Returns:
            Compiled code object.
        """
    def execute_code(self, code, filename: Incomplete | None = None) -> None:
        """Execute code within the execution context.

        Args:
            code (str or SourceCode): Rex code to execute.
            filename (str): Filename to report if there are syntax errors.
        """
    def execute_function(self, func, *nargs, **kwargs):
        """
        Execute a function object within the execution context.
        @returns The result of the function call.
        """
    def get_output(self, style=...):
        """Returns the result of all previous calls to execute_code."""
    def expand(self, value): ...
