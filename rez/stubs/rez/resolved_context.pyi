import rez.package_filter
import rez.package_order
import rez.packages
import rez.resolved_context
import rez.resolver
import rez.solver
import rez.version._requirement
from _typeshed import Incomplete
from collections.abc import Generator
from contextlib import contextmanager
from enum import Enum
from rez import __version__ as __version__, module_root_path as module_root_path, package_order as package_order
from rez.config import config as config
from rez.exceptions import PackageCacheError as PackageCacheError, PackageCommandError as PackageCommandError, PackageNotFoundError as PackageNotFoundError, ResolvedContextError as ResolvedContextError, RezError as RezError, _NeverError as _NeverError
from rez.package_cache import PackageCache as PackageCache
from rez.package_filter import PackageFilterList as PackageFilterList
from rez.package_order import PackageOrder as PackageOrder, PackageOrderList as PackageOrderList
from rez.package_repository import package_repository_manager as package_repository_manager
from rez.packages import Package as Package, Variant as Variant, get_variant as get_variant, iter_packages as iter_packages
from rez.resolver import Resolver as Resolver, ResolverStatus as ResolverStatus
from rez.rex import ActionInterpreter as ActionInterpreter, OutputStyle as OutputStyle, Python as Python, RexExecutor as RexExecutor, literal as literal
from rez.rex_bindings import EphemeralsBinding as EphemeralsBinding, RequirementsBinding as RequirementsBinding, VariantBinding as VariantBinding, VariantsBinding as VariantsBinding, VersionBinding as VersionBinding, intersects as intersects
from rez.shells import create_shell as create_shell
from rez.solver import SolverCallbackReturn as SolverCallbackReturn, SolverState as SolverState, SupportsWrite as SupportsWrite
from rez.system import system as system
from rez.util import dedup as dedup, is_non_string_iterable as is_non_string_iterable
from rez.utils.colorize import Printer as Printer, critical as critical, heading as heading, implicit as implicit, local as local
from rez.utils.data_utils import deep_del as deep_del
from rez.utils.filesystem import TempDirs as TempDirs, canonical_path as canonical_path, is_subdirectory as is_subdirectory
from rez.utils.formatting import ENV_VAR_REGEX as ENV_VAR_REGEX, PackageRequest as PackageRequest, columnise as columnise, header_comment as header_comment, minor_header_comment as minor_header_comment
from rez.utils.graph_utils import read_graph_from_string as read_graph_from_string, write_compacted as write_compacted, write_dot as write_dot
from rez.utils.logging_ import print_error as print_error, print_warning as print_warning
from rez.utils.memcached import pool_memcached_connections as pool_memcached_connections
from rez.utils.platform_ import platform_ as platform_
from rez.utils.resolve_graph import failure_detail_from_graph as failure_detail_from_graph
from rez.utils.sourcecode import SourceCodeError as SourceCodeError
from rez.utils.which import which as which
from rez.utils.yaml import dump_yaml as dump_yaml
from rez.vendor import yaml as yaml  # type: ignore[import-not-found]
from rez.version import Requirement as Requirement, VersionRange as VersionRange
from typing import Any, Callable, Iterable, NoReturn, Sequence, TypeVar

CallableT = TypeVar('CallableT', bound=Callable)

class RezToolsVisibility(Enum):
    """Determines if/how rez cli tools are added back to PATH within a
    resolved environment.
    """
    never = 0
    append = 1
    prepend = 2

class SuiteVisibility(Enum):
    """Defines what suites on $PATH stay visible when a new rez environment is
    resolved.
    """
    never = 0
    always = 1
    parent = 2
    parent_priority = 3

class PatchLock(Enum):
    """Enum to represent the 'lock type' used when patching context objects.
    """
    no_lock = ('No locking', -1)
    lock_2 = ('Minor version updates only (X.*)', 1)
    lock_3 = ('Patch version updates only (X.X.*)', 2)
    lock_4 = ('Build version updates only (X.X.X.*)', 3)
    lock = ('Exact version', -1)
    __order__ = 'no_lock,lock_2,lock_3,lock_4,lock'
    description: Any
    rank: Any
    def __init__(self, description, rank) -> None: ...

def get_lock_request(name: str, version, patch_lock: PatchLock, weak: bool = True) -> PackageRequest | None:
    """Given a package and patch lock, return the equivalent request.

    For example, for object 'foo-1.2.1' and lock type 'lock_3', the equivalent
    request is '~foo-1.2'. This restricts updates to foo to patch-or-lower
    version changes only.

    For objects not versioned down to a given lock level, the closest possible
    lock is applied. So 'lock_3' applied to 'foo-1' would give '~foo-1'.

    Args:
        name (str): Package name.
        version (Version): Package version.
        patch_lock (PatchLock): Lock type to apply.

    Returns:
        typing.Optional[PackageRequest]: PackageRequest object, or None if there is no equivalent request.
    """
def _on_success(fn: CallableT) -> CallableT: ...

class ResolvedContext:
    """A class that resolves, stores and spawns Rez environments.

    The main Rez entry point for creating, saving, loading and executing
    resolved environments. A ResolvedContext object can be saved to file and
    loaded at a later date, and it can reconstruct the equivalent environment
    at that time. It can spawn interactive and non-interactive shells, in any
    supported shell plugin type, such as bash and tcsh. It can also run a
    command within a configured python namespace, without spawning a child
    shell.
    """
    serialize_version: Incomplete
    tmpdir_manager: Incomplete
    context_tracking_payload: dict[str, Any] | None
    context_tracking_lock: Incomplete
    package_cache_present: bool
    local: Incomplete
    class Callback:
        max_fails: int
        time_limit: Any
        callback: Any
        start_time: float
        buf: rez.solver.SupportsWrite | Any
        def __init__(self, max_fails: int, time_limit, callback, buf: SupportsWrite | None = None) -> None: ...
        def __call__(self, state): ...
    load_path: str | None
    requested_timestamp: float | None
    timestamp: float | int
    building: bool
    testing: bool
    implicit_packages: list[rez.version._requirement.Requirement]
    caching: Any | bool
    verbosity: int
    _package_requests: list[rez.version._requirement.Requirement]
    package_paths: Any | list[str]
    package_filter: Any | rez.package_filter.PackageFilterList
    package_orderers: rez.package_order.PackageOrderList
    append_sys_path: bool
    package_caching: Any
    package_cache_async: Any
    default_patch_lock: rez.resolved_context.PatchLock
    patch_locks: dict[Any, Any]
    rez_version: str
    rez_path: str
    user: str
    host: Any
    platform: Any
    arch: Any
    os: Any
    created: int
    status_: rez.resolver.ResolverStatus
    _resolved_packages: list[rez.packages.Variant | Any]
    _resolved_ephemerals: list[rez.version._requirement.Requirement] | None
    failure_description: None
    graph_string: None
    graph_: Any | None
    from_cache: bool | None
    solve_time: float
    load_time: float
    num_loaded_packages: int
    pre_resolve_bindings: dict[str, Any] | None
    parent_suite_path: str | None
    suite_context_name: str | None
    def __init__(self, package_requests: Iterable[str | Requirement], verbosity: int = 0, timestamp: float | None = None, building: bool = False, testing: bool = False, caching: bool | None = None, package_paths: list[str] | None = None, package_filter: PackageFilterList | None = None, package_orderers: list[PackageOrder] | None = None, max_fails: int = -1, add_implicit_packages: bool = True, time_limit: int = -1, callback: Callable[[SolverState], tuple[SolverCallbackReturn, str]] | None = None, package_load_callback: Callable[[Package], Any] | None = None, buf: SupportsWrite | None = None, suppress_passive: bool = False, print_stats: bool = False, package_caching: Incomplete | None = None, package_cache_async: Incomplete | None = None) -> None:
        """Perform a package resolve, and store the result.

        Args:
            package_requests (list[typing.Union[str, Requirement]]): request
            verbosity (int): Verbosity level. One of [0,1,2].
            timestamp (float): Ignore packages released after this epoch time. Packages
                released at exactly this time will not be ignored.
            building (bool): True if we're resolving for a build.
            testing (bool): True if we're resolving for a test (rez-test).
            caching (bool): If True, cache(s) may be used to speed the resolve. If
                False, caches will not be used. If None, :data:`resolve_caching`
                is used.
            package_paths (list[str]): List of paths to search for pkgs, defaults to
                :data:`packages_path`.
            package_filter (PackageFilterList): Filter used to exclude certain
                packages. Defaults to settings from :data:`package_filter`. Use
                :data:`rez.package_filter.no_filter` to remove all filtering.
            package_orderers (list[PackageOrder]): Custom package ordering.
                Defaults to settings from :data:`package_orderers`.
            add_implicit_packages (bool): If True, the implicit package list defined
                by :data:`implicit_packages` is appended to the request.
            max_fails (int): Abort the resolve if the number of failed steps is
                greater or equal to this number. If -1, does not abort.
            time_limit (int): Abort the resolve if it takes longer than this
                many seconds. If -1, there is no time limit.
            callback: See :class:`.Solver`.
            package_load_callback: If not None, this callable will be called
                prior to each package being loaded. It is passed a single
                :class:`.Package` object.
            buf (typing.IO): Where to print verbose output to, defaults
                to stdout.
            suppress_passive (bool): If True, don't print debugging info that
                has had no effect on the solve. This argument only has an
                effect if ``verbosity`` > 2.
            print_stats (bool): If True, print advanced solver stats at the end.
            package_caching (bool|None): If True, apply package caching settings
                as per the config. If None, enable as determined by config
                setting :data:`package_cache_during_build`.
            package_cache_async (bool|None): If True, cache packages asynchronously.
                If None, use the config setting :data:`package_cache_async`
        """
    def __str__(self) -> str: ...
    @property
    def success(self) -> bool:
        """True if the context has been solved, False otherwise."""
    @property
    def status(self) -> ResolverStatus:
        """Return the current status of the context.

        Returns:
            ResolverStatus:
        """
    def requested_packages(self, include_implicit: bool = False) -> list[Requirement]:
        """Get packages in the request.

        Args:
            include_implicit (bool): If True, implicit packages are appended
                to the result.

        Returns:
            list[Requirement]:
        """
    @property
    def resolved_packages(self) -> list[Variant] | None:
        """Get packages in the resolve.

        Returns:
            typing.Optional[list[Variant]]: Resolved variant objects, or None if the resolve failed.
        """
    @property
    def resolved_ephemerals(self) -> list[Requirement] | None:
        """Get non-conflict ephemerals in the resolve.

        Returns:
            typing.Optional[list[Requirement]]: Requirement objects, or None if the resolve failed.
        """
    def set_load_path(self, path: str) -> None:
        """Set the path that this context was reportedly loaded from.

        You may want to use this method in cases where a context is saved to
        disk, but you need to associate this new path with the context while it
        is still in use.
        """
    def __eq__(self, other):
        """Equality test.

        Two contexts are considered equal if they have an equivalent request,
        and an equivalent resolve. Other details, such as timestamp, are not
        considered.
        """
    def __hash__(self): ...
    @property
    def has_graph(self):
        """Return True if the resolve has a graph."""
    def get_resolved_package(self, name: str) -> Variant | None:
        """Returns a `Variant` object or None if the package is not in the
        resolve.
        """
    def copy(self) -> ResolvedContext:
        """Returns a shallow copy of the context."""
    def retargeted(self, package_paths: list[str], package_names: list[str] | None = None, skip_missing: bool = False) -> ResolvedContext:
        """Create a retargeted copy of this context.

        Retargeting a context means replacing its variant references with
        the same variants from other package repositories.

        Args:
            package_paths: List of paths to search for pkgs to retarget to.
            package_names (list of str): Only retarget these packages. If None,
                retarget all packages.
            skip_missing (bool): If True, skip retargeting of variants that
                cannot be found in ``package_paths``. By default, a
                :exc:`.PackageNotFoundError` is raised.

        Returns:
            ResolvedContext: The retargeted context.
        """
    def get_patched_request(self, package_requests: Incomplete | None = None, package_subtractions: Incomplete | None = None, strict: bool = False, rank: int = 0):
        """Get a 'patched' request.

        A patched request is a copy of this context's request, but with some
        changes applied. This can then be used to create a new, 'patched'
        context.

        New package requests override original requests based on the type -
        normal, conflict or weak. So 'foo-2' overrides 'foo-1', '!foo-2'
        overrides '!foo-1' and '~foo-2' overrides '~foo-1', but a request such
        as '!foo-2' would not replace 'foo-1' - it would be added instead.

        Note that requests in `package_requests` can have the form '^foo'. This
        is another way of supplying package subtractions.

        Any new requests that don't override original requests are appended,
        in the order that they appear in `package_requests`.

        Args:
            package_requests (list[typing.Union[str, PackageRequest]):
                Overriding requests.
            package_subtractions (list[str]): Any original request with a
                package name in this list is removed, before the new requests
                are added.
            strict (bool): If True, the current context's resolve is used as the
                original request list, rather than the request.
            rank (int): If > 1, package versions can only increase in this rank
                and further - for example, rank=3 means that only version patch
                numbers are allowed to increase, major and minor versions will
                not change. This is only applied to packages that have not been
                explicitly overridden in ``package_requests``. If rank <= 1, or
                ``strict`` is True, rank is ignored.

        Returns:
            list[PackageRequest]: PackageRequests objects that can be used to construct a
            new :class:`ResolvedContext` object.
        """
    def graph(self, as_dot: bool = False):
        """Get the resolve graph.

        Args:
            as_dot: If True, get the graph as a dot-language string. Otherwise,
                a pygraph.digraph object is returned.

        Returns:
            A string or `pygraph.digraph` object, or None if there is no graph
            associated with the resolve.
        """
    def save(self, path: str) -> None:
        """Save the resolved context to file."""
    def write_to_buffer(self, buf: SupportsWrite) -> None:
        """Save the context to a buffer."""
    @classmethod
    def get_current(cls) -> ResolvedContext | None:
        """Get the context for the current env, if there is one.

        Returns:
            ResolvedContext: Current context, or None if not in a resolved env.
        """
    def is_current(self) -> bool | None:
        """
        Returns:
            bool: True if this is the currently sourced context, False otherwise.
        """
    @classmethod
    def load(cls, path: str) -> ResolvedContext:
        """Load a resolved context from file."""
    @classmethod
    def read_from_buffer(cls, buf, identifier_str: Incomplete | None = None) -> ResolvedContext | None:
        """Load the context from a buffer."""
    def get_resolve_diff(self, other: ResolvedContext) -> dict:
        """Get the difference between the resolve in this context and another.

        The difference is described from the point of view of the current context
        - a newer package means that the package in `other` is newer than the
        package in `self`.

        Diffs can only be compared if their package search paths match, an error
        is raised otherwise.

        The diff is expressed in packages, not variants - the specific variant
        of a package is ignored.

        Returns:
            dict: A dict containing:

            - 'newer_packages': A dict containing items:
                - package name (str);
                - List of `Package` objects. These are the packages up to and
                  including the newer package in `self`, in ascending order.
            - 'older_packages': A dict containing:
                - package name (str);
                - List of `Package` objects. These are the packages down to and
                  including the older package in `self`, in descending order.
            - 'added_packages': Set of `Package` objects present in `self` but
               not in `other`;
            - 'removed_packages': Set of `Package` objects present in `other`,
               but not in `self`.

            If any item ('added_packages' etc) is empty, it is not added to the
            resulting dict. Thus, an empty dict is returned if there is no
            difference between contexts.
        """
    @pool_memcached_connections
    def print_info(self, buf: SupportsWrite = ..., verbosity: int = 0, source_order: bool = False, show_resolved_uris: bool = False) -> None:
        """Prints a message summarising the contents of the resolved context.

        Args:
            buf (typing.IO): Where to print this info to.
            verbosity (bool): Verbose mode.
            source_order (bool): If True, print resolved packages in the order
                they are sourced, rather than alphabetical order.
            show_resolved_uris (bool): By default, resolved packages have their
                'root' property listed, or their 'uri' if 'root' is None. Use
                this option to list 'uri' regardless.
        """
    def print_tools(self, buf: SupportsWrite = ...) -> None: ...
    def print_resolve_diff(self, other, heading: Incomplete | None = None) -> None:
        """Print the difference between the resolve of two contexts.

        Args:
            other (ResolvedContext): Context to compare to.
            heading: One of:

                - None: Do not display a heading;
                - True: Display the filename of each context as a heading, if
                  both contexts have a filepath;
                - 2-tuple: Use the given two strings as headings - the first is
                  the heading for `self`, the second for `other`.
        """
    @_on_success
    def get_dependency_graph(self, as_dot: bool = False):
        """Generate the dependency graph.

        The dependency graph is a simpler subset of the resolve graph. It
        contains package name nodes connected directly to their dependencies.
        Weak references and conflict requests are not included in the graph.
        The dependency graph does not show conflicts.

        Returns:
            `pygraph.digraph` object.
        """
    @_on_success
    def validate(self) -> None:
        """Validate the context."""
    @_on_success
    def get_environ(self, parent_environ: Incomplete | None = None) -> dict[str, str]:
        """Get the environ dict resulting from interpreting this context.

        Args:
            parent_environ: Environment to interpret the context within,
                defaults to os.environ if None.

        Returns:
            The environment dict generated by this context, when
            interpreted in a python rex interpreter.
        """
    @_on_success
    def get_key(self, key: str, request_only: bool = False) -> dict[str, tuple[Variant, Any]]:
        """Get a data key value for each resolved package.

        Args:
            key (str): String key of property, eg 'tools'.
            request_only (bool): If True, only return the key from resolved
                packages that were also present in the request.

        Returns:
            Dict of ``{pkg-name: (variant, value)}``.
        """
    @_on_success
    def get_tools(self, request_only: bool = False) -> dict[str, tuple[Variant, list[str]]]:
        """Returns the commandline tools available in the context.

        Args:
            request_only: If True, only return the tools from resolved packages
                that were also present in the request.

        Returns:
            Dict of ``{pkg-name: (variant, [tools])}``.
        """
    @_on_success
    def get_tool_variants(self, tool_name: str) -> set[Variant]:
        """Get the variant(s) that provide the named tool.

        If there are more than one variants, the tool is in conflict, and Rez
        does not know which variant's tool is actually exposed.

        Args:
            tool_name(str): Name of the tool to search for.

        Returns:
            Set of `Variant` objects. If no variant provides the tool, an
            empty set is returned.
        """
    @_on_success
    def get_conflicting_tools(self, request_only: bool = False) -> dict[str, set[Variant]]:
        """Returns tools of the same name provided by more than one package.

        Args:
            request_only: If True, only return the key from resolved packages
                that were also present in the request.

        Returns:
            Dict of ``{tool-name: set([Variant])}``.
        """
    @_on_success
    def get_shell_code(self, shell: str | None = None, parent_environ: Incomplete | None = None, style=...):
        """Get the shell code resulting from intepreting this context.

        Args:
            shell (str): Shell type, for eg 'bash'. If None, the current shell
                type is used.
            parent_environ (dict): Environment to interpret the context within,
                defaults to os.environ if None.
            style (OutputStyle): Style to format shell code in.
        """
    @_on_success
    def get_actions(self, parent_environ: Incomplete | None = None):
        """Get the list of rex.Action objects resulting from interpreting this
        context. This is provided mainly for testing purposes.

        Args:
            parent_environ: Environment to interpret the context within,
                defaults to os.environ if None.

        Returns:
            A list of rex.Action subclass instances.
        """
    @_on_success
    def apply(self, parent_environ: Incomplete | None = None) -> None:
        """Apply the context to the current python session.

        Note that this updates os.environ and possibly sys.path, if
        `parent_environ` is not provided.

        Args:
            parent_environ: Environment to interpret the context within,
                defaults to os.environ if None.
        """
    @_on_success
    def which(self, cmd, parent_environ: Incomplete | None = None, fallback: bool = False):
        """Find a program in the resolved environment.

        Args:
            cmd: String name of the program to find.
            parent_environ: Environment to interpret the context within,
                defaults to os.environ if None.
            fallback: If True, and the program is not found in the context,
                the current environment will then be searched.

        Returns:
            Path to the program, or None if the program was not found.
        """
    @_on_success
    def execute_command(self, args, parent_environ: Incomplete | None = None, **Popen_args):
        """Run a command within a resolved context.

        This applies the context to a python environ dict, then runs a
        subprocess in that namespace. This is not a fully configured subshell -
        shell-specific commands such as aliases will not be applied. To execute
        a command within a subshell instead, use execute_shell().

        Warning:
            This runs a command in a configured environ dict only, not in a true
            shell. To do that, call `execute_shell` using the `command` keyword
            argument.

        Args:
            args: Command arguments, can be a string.
            parent_environ: Environment to interpret the context within,
                defaults to os.environ if None.
            Popen_args: Args to pass to subprocess.Popen.

        Returns:
            A subprocess.Popen object.

        Note:
            This does not alter the current python session.
        """
    @_on_success
    def execute_rex_code(self, code, filename: Incomplete | None = None, shell: Incomplete | None = None, parent_environ: dict[str, str] | None = None, **Popen_args):
        """Run some rex code in the context.

        Note:
            This is just a convenience form of `execute_shell`.

        Args:
            code (str): Rex code to execute.
            filename (str): Filename to report if there are syntax errors.
            shell: Shell type, for eg 'bash'. If None, the current shell type
                is used.
            parent_environ: Environment to run the shell process in, if None
                then the current environment is used.
            Popen_args: args to pass to the shell process object constructor.

        Returns:
            subprocess.Popen: Subprocess object for the shell process.
        """
    @_on_success
    def execute_shell(self, shell: str | None = None, parent_environ: dict[str, str] | None = None, rcfile: str | None = None, norc: bool = False, stdin: bool = False, command: str | Sequence[str] | None = None, quiet: bool = False, block: bool | None = None, actions_callback: Callable[[RexExecutor], Any] | None = None, post_actions_callback: Callable[[RexExecutor], Any] | None = None, context_filepath: Incomplete | None = None, start_new_session: bool = False, detached: bool = False, pre_command: Incomplete | None = None, **Popen_args):
        """Spawn a possibly-interactive shell.

        Args:
            shell: Shell type, for eg 'bash'. If None, the current shell type
                is used.
            parent_environ: Environment to run the shell process in, if None
                then the current environment is used.
            rcfile: Specify a file to source instead of shell startup files.
            norc: If True, skip shell startup files, if possible.
            stdin: If True, read commands from stdin, in a non-interactive
                shell.
            command: If not None, execute this command in a non-interactive shell.
                If an empty string or list, don't run a command, but don't open
                an interactive shell either. Can be a list of args.
            quiet: If True, skip the welcome message in interactive shells.
            block: If True, block until the shell is terminated. If False,
                return immediately. If None, will default to blocking if the
                shell is interactive.
            actions_callback: Callback with signature (RexExecutor). This lets
                the user append custom actions to the context, such as setting
                extra environment variables. Callback is run prior to context Rex
                execution.
            post_actions_callback: Callback with signature (RexExecutor). This lets
                the user append custom actions to the context, such as setting
                extra environment variables. Callback is run after context Rex
                execution.
            context_filepath: If provided, the context file will be written
                here, rather than to the default location (which is in a
                tempdir). If you use this arg, you are responsible for cleaning
                up the file.
            start_new_session: If True, change the process group of the target
                process. Note that this may override the Popen_args keyword
                'preexec_fn'.
            detached: If True, open a separate terminal. Note that this may
                override the `pre_command` argument.
            pre_command: Command to inject before the shell command itself. This
                is for internal use.
            Popen_args: args to pass to the shell process object constructor.

        Returns:
            If blocking, a 3-tuple of (returncode, stdout, stderr).
                Note that if you want to get anything other than None for stdout
                and/or stderr, you need to give stdout=PIPE and/or stderr=PIPE.

            If non-blocking, a subprocess.Popen object for the shell process.
        """
    @_on_success
    def get_resolve_as_exact_requests(self) -> list[PackageRequest]:
        """Convert to a package request list of exact resolved package versions.

            >>> r = ResolvedContext(['foo']
            >>> r.get_resolve_as_exact_requests()
            ['foo==1.2.3', 'bah==1.0.1', 'python==2.7.12']

        Returns:
            List of `PackageRequest`: Context as a list of exact version
            requests.
        """
    def to_dict(self, fields: list[str] | None = None) -> dict:
        """Convert context to dict containing only builtin types.

        Args:
            fields (list of str): If present, only write these fields into the
                dict. This can be used to avoid constructing expensive fields
                (such as 'graph') for some cases.

        Returns:
            dict: Dictified context.
        """
    @classmethod
    def from_dict(cls, d: dict, identifier_str: str | None = None) -> ResolvedContext:
        """Load a `ResolvedContext` from a dict.

        Args:
            d (dict): Dict containing context data.
            identifier_str (str): String identifying the context, this is only
                used to display in an error string if a serialization version
                mismatch is detected.

        Returns:
            `ResolvedContext` object.
        """
    def _execute_bundle_post_actions_callback(self, executor: RexExecutor) -> None:
        """
        In bundles, you can drop a 'post_commands.py' file (rex) alongside the
        'bundle.yaml' file, and it will be sourced after all package commands.
        """
    @classmethod
    @contextmanager
    def _detect_bundle(cls, path) -> Generator[None]: ...
    @classmethod
    def _get_bundle_path(cls): ...
    @classmethod
    def _adjust_variant_for_bundling(cls, handle, out) -> None:
        """
        Deals with making variant pkg repo ref relative/nonrelative to take
        bundling into account.

        Note: Alters `handle` in-place.
        """
    @classmethod
    def _get_package_cache(cls) -> PackageCache | None: ...
    def _update_package_cache(self) -> None: ...
    @classmethod
    def _init_context_tracking_payload_base(cls) -> None: ...
    def _track_context(self, context_data, action: str) -> None: ...
    @classmethod
    def _read_from_buffer(cls, buf, identifier_str: str | None = None) -> ResolvedContext: ...
    @classmethod
    def _load_error(cls, e, path: str | None = None) -> NoReturn: ...
    def _set_parent_suite(self, suite_path, context_name: str) -> None: ...
    def _create_executor(self, interpreter: ActionInterpreter, parent_environ: dict[str, str] | None) -> RexExecutor: ...
    def _get_pre_resolve_bindings(self): ...
    @pool_memcached_connections
    def _execute(self, executor: RexExecutor) -> None:
        """Bind various info to the execution context
        """
    def _append_suite_paths(self, executor: RexExecutor) -> None: ...
