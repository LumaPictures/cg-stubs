from _typeshed import Incomplete
from rez import __version__ as __version__
from rez.packages import Package as Package, iter_packages as iter_packages
from rez.resolved_context import ResolvedContext as ResolvedContext
from rez.suite import Suite as Suite
from rez.utils.colorize import Printer as Printer, critical as critical, warning as warning
from rez.utils.data_utils import cached_property as cached_property
from rez.utils.formatting import PackageRequest as PackageRequest, print_colored_columns as print_colored_columns
from rez.utils.which import which as which
from rez.wrapper import Wrapper as Wrapper

class Status:
    """Access to current status of the environment.

    The current status tells you things such as if you are within a context, or
    if suite(s) are visible on $PATH.
    """
    def __init__(self) -> None: ...
    @cached_property
    def context_file(self):
        """Get path to the current context file.

        Returns:
            Str, or None if not in a context.
        """
    @cached_property
    def context(self):
        """Get the current context.

        Returns:
            `ResolvedContext` or None if not in a context.
        """
    @cached_property
    def suites(self):
        """Get currently visible suites.

        Visible suites are those whos bin path appea on $PATH.

        Returns:
            List of `Suite` objects.
        """
    @cached_property
    def parent_suite(self):
        """Get the current parent suite.

        A parent suite exists when a context within a suite is active. That is,
        during execution of a tool within a suite, or after a user has entered
        an interactive shell in a suite context, for example via the command-
        line syntax 'tool +i', where 'tool' is an alias in a suite.

        Returns:
            `Suite` object, or None if there is no current parent suite.
        """
    @cached_property
    def active_suite_context_name(self):
        """Get the name of the currently active context in a parent suite.

        If a parent suite exists, then an active context exists - this is the
        context that a tool in the suite is currently running in.

        Returns:
            (str) Context name, or None if there is no parent suite (and thus
            no active context).
        """
    def print_info(self, obj: Incomplete | None = None, buf=...):
        """Print a status message about the given object.

        If an object is not provided, status info is shown about the current
        environment - what the active context is if any, and what suites are
        visible.

        Args:
            obj (str): String which may be one of the following:
                - A tool name;
                - A package name, possibly versioned;
                - A context filepath;
                - A suite filepath;
                - The name of a context in a visible suite.
        """
    def print_tools(self, pattern: Incomplete | None = None, buf=...) -> bool:
        """Print a list of visible tools.

        Args:
            pattern (str): Only list tools that match this glob pattern.
        """
    def _print_tool_info(self, value, buf=..., b: bool = False) -> bool: ...
    def _print_package_info(self, value, buf=..., b: bool = False) -> bool: ...
    def _print_suite_info(self, value, buf=..., b: bool = False) -> bool: ...
    def _print_context_info(self, value, buf=..., b: bool = False) -> bool: ...
    def _print_info(self, buf=...) -> None: ...

status: Incomplete
