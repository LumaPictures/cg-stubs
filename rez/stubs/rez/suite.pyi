import collections
import rez.packages
import rez.resolved_context
from _typeshed import Incomplete
from rez.exceptions import ResolvedContextError as ResolvedContextError, SuiteError as SuiteError
from rez.packages import Variant as Variant
from rez.resolved_context import ResolvedContext as ResolvedContext
from rez.utils.colorize import Printer as Printer, critical as critical, warning as warning
from rez.utils.data_utils import cached_property as cached_property
from rez.utils.execution import create_forwarding_script as create_forwarding_script
from rez.utils.formatting import PackageRequest as PackageRequest, columnise as columnise
from rez.utils.yaml import dump_yaml as dump_yaml
from rez.vendor import yaml as yaml  # type: ignore[import-not-found]
from rez.vendor.yaml.error import YAMLError as YAMLError  # type: ignore[import-not-found]
from typing import TypedDict

class Tool(TypedDict):
    tool_name: str
    tool_alias: str
    context_name: str
    variant: Variant | set[Variant]

class Context(TypedDict):
    name: str
    context: ResolvedContext
    tool_aliases: dict[str, str]
    hidden_tools: set[str]
    priority: int
    prefix_char: str | None
    loaded: bool
    prefix: str
    suffix: str

class Suite:
    """A collection of contexts.

    A suite is a collection of contexts. A suite stores its contexts in a
    single directory, and creates wrapper scripts for each tool in each context,
    which it stores into a single bin directory. When a tool is invoked, it
    executes the actual tool in its associated context. When you add a suite's
    bin directory to PATH, you have access to all these tools, which will
    automatically run in correctly configured environments.

    Tool clashes can occur when a tool of the same name is present in more than
    one context. When a context is added to a suite, or prefixed/suffixed, that
    context's tools override tools from other contexts.

    There are several ways to avoid tool name clashes:

    - Hide a tool. This removes it from the suite even if it does not clash;
    - Prefix/suffix a context. When you do this, all the tools in the context
      have the prefix/suffix applied;
    - Explicitly alias a tool using the `alias_tool` method. This takes
      precedence over context prefix/suffixing.
    """
    load_path: str | None
    contexts: dict[str, TypedDict('rez.suite.Context', {'name': str, 'context': rez.resolved_context.ResolvedContext, 'tool_aliases': dict[str, str], 'hidden_tools': set[str], 'priority': int, 'prefix_char': str | None, 'loaded': bool, 'prefix': str, 'suffix': str})]  # type: ignore[valid-type]
    next_priority: int
    tools: dict[str, TypedDict('rez.suite.Tool', {'tool_name': str, 'tool_alias': str, 'context_name': str, 'variant': rez.packages.Variant | set[rez.packages.Variant]})] | None  # type: ignore[valid-type]
    tool_conflicts: collections.defaultdict[str, list[TypedDict('rez.suite.Tool', {'tool_name': str, 'tool_alias': str, 'context_name': str, 'variant': rez.packages.Variant | set[rez.packages.Variant]})]] | None  # type: ignore[valid-type]
    hidden_tools: list[TypedDict('rez.suite.Tool', {'tool_name': str, 'tool_alias': str, 'context_name': str, 'variant': rez.packages.Variant | set[rez.packages.Variant]})] | None  # type: ignore[valid-type]
    def __init__(self) -> None:
        """Create a suite."""
    @property
    def context_names(self) -> list[str]:
        """Get the names of the contexts in the suite.

        Reurns:
            List of strings.
        """
    @cached_property
    def tools_path(self):
        """Get the path that should be added to $PATH to expose this suite's
        tools.

        Returns:
            Absolute path as a string, or None if this suite was not loaded
            from disk.
        """
    def activation_shell_code(self, shell: Incomplete | None = None):
        """Get shell code that should be run to activate this suite."""
    def __str__(self) -> str: ...
    def context(self, name):
        """Get a context.

        Args:
            name (str): Name to store the context under.

        Returns:
            `ResolvedContext` object.
        """
    def add_context(self, name: str, context: ResolvedContext, prefix_char: Incomplete | None = None):
        """Add a context to the suite.

        Args:
            name (str): Name to store the context under.
            context (ResolvedContext): Context to add.
        """
    def find_contexts(self, in_request: Incomplete | None = None, in_resolve: Incomplete | None = None):
        """Find contexts in the suite based on search criteria.

        Args:
            in_request (str): Match contexts that contain the given package in
                their request.
            in_resolve (str or `Requirement`): Match contexts that contain the
                given package in their resolve. You can also supply a conflict
                requirement - '!foo' will match any contexts whos resolve does
                not contain any version of package 'foo'.

        Returns:
            List of context names that match the search criteria.
        """
    def remove_context(self, name: str) -> None:
        """Remove a context from the suite.

        Args:
            name (str): Name of the context to remove.
        """
    def set_context_prefix(self, name, prefix) -> None:
        """Set a context's prefix.

        This will be applied to all wrappers for the tools in this context. For
        example, a tool called 'foo' would appear as '<prefix>foo' in the
        suite's bin path.

        Args:
            name (str): Name of the context to prefix.
            prefix (str): Prefix to apply to tools.
        """
    def remove_context_prefix(self, name) -> None:
        """Remove a context's prefix.

        Args:
            name (str): Name of the context to de-prefix.
        """
    def set_context_suffix(self, name, suffix) -> None:
        """Set a context's suffix.

        This will be applied to all wrappers for the tools in this context. For
        example, a tool called 'foo' would appear as 'foo<suffix>' in the
        suite's bin path.

        Args:
            name (str): Name of the context to suffix.
            suffix (str): Suffix to apply to tools.
        """
    def remove_context_suffix(self, name) -> None:
        """Remove a context's suffix.

        Args:
            name (str): Name of the context to de-suffix.
        """
    def bump_context(self, name) -> None:
        """Causes the context's tools to take priority over all others."""
    def hide_tool(self, context_name, tool_name) -> None:
        """Hide a tool so that it is not exposed in the suite.

        Args:
            context_name (str): Context containing the tool.
            tool_name (str): Name of tool to hide.
        """
    def unhide_tool(self, context_name, tool_name) -> None:
        """Unhide a tool so that it may be exposed in a suite.

        Note that unhiding a tool doesn't guarantee it can be seen - a tool of
        the same name from a different context may be overriding it.

        Args:
            context_name (str): Context containing the tool.
            tool_name (str): Name of tool to unhide.
        """
    def alias_tool(self, context_name, tool_name, tool_alias) -> None:
        """Register an alias for a specific tool.

        Note that a tool alias takes precedence over a context prefix/suffix.

        Args:
            context_name (str): Context containing the tool.
            tool_name (str): Name of tool to alias.
            tool_alias (str): Alias to give the tool.
        """
    def unalias_tool(self, context_name, tool_name) -> None:
        """Deregister an alias for a specific tool.

        Args:
            context_name (str): Context containing the tool.
            tool_name (str): Name of tool to unalias.
        """
    def get_tools(self):
        """Get the tools exposed by this suite.

        Returns:
            dict: A dict, keyed by aliased tool name, with dict entries:

            - tool_name (str): The original, non-aliased name of the tool;
            - tool_alias (str): Aliased tool name (same as key);
            - context_name (str): Name of the context containing the tool;
            - variant (`Variant` or set): Variant providing the tool. If the
              tool is in conflict within the context (more than one package has
              a tool of the same name), this will be a set of Variants.
        """
    def get_tool_filepath(self, tool_alias):
        """Given a visible tool alias, return the full path to the executable.

        Args:
            tool_alias (str): Tool alias to search for.

        Returns:
            (str): Filepath of executable, or None if the tool is not in the
                suite. May also return None because this suite has not been saved
                to disk, so a filepath hasn't yet been established.
        """
    def get_tool_context(self, tool_alias: str) -> str | None:
        """Given a visible tool alias, return the name of the context it
        belongs to.

        Args:
            tool_alias (str): Tool alias to search for.

        Returns:
            (str): Name of the context that exposes a visible instance of this
            tool alias, or None if the alias is not available.
        """
    def get_hidden_tools(self) -> list[Tool]:
        """Get the tools hidden in this suite.

        Hidden tools are those that have been explicitly hidden via `hide_tool`.

        Returns:
            list[dict]: A list of dicts, where each dict contains:

            - tool_name (str): The original, non-aliased name of the tool;
            - tool_alias (str): Aliased tool name (same as key);
            - context_name (str): Name of the context containing the tool;
            - variant (`Variant`): Variant providing the tool.
        """
    def get_conflicting_aliases(self) -> list[str]:
        """Get a list of tool aliases that have one or more conflicts.

        Returns:
            List of strings.
        """
    def get_alias_conflicts(self, tool_alias: str) -> list[Tool] | None:
        """Get a list of conflicts on the given tool alias.

        Args:
            tool_alias (str): Alias to check for conflicts.

        Returns: None if the alias has no conflicts, or a list of dicts, where
            each dict contains:
            - tool_name (str): The original, non-aliased name of the tool;
            - tool_alias (str): Aliased tool name (same as key);
            - context_name (str): Name of the context containing the tool;
            - variant (`Variant`): Variant providing the tool.
        """
    def validate(self) -> None:
        """Validate the suite."""
    def to_dict(self): ...
    @classmethod
    def from_dict(cls, d): ...
    def save(self, path, verbose: bool = False):
        """Save the suite to disk.

        Args:
            path (str): Path to save the suite to. If a suite is already saved
                at `path`, then it will be overwritten. Otherwise, if `path`
                exists, an error is raised.
        """
    @classmethod
    def load(cls, path): ...
    @classmethod
    def visible_suite_paths(cls, paths: Incomplete | None = None):
        """Get a list of paths to suites that are visible on $PATH.

        Returns:
            List of str.
        """
    @classmethod
    def load_visible_suites(cls, paths: Incomplete | None = None):
        """Get a list of suites whos bin paths are visible on $PATH.

        Returns:
            List of `Suite` objects.
        """
    def print_info(self, buf=..., verbose: bool = False) -> None:
        """Prints a message summarising the contents of the suite."""
    def print_tools(self, buf=..., verbose: bool = False, context_name: Incomplete | None = None) -> None:
        """Print table of tools available in the suite.

        Args:
            context_name (str): If provided, only print the tools from this
                context.
        """
    def _context(self, name: str) -> Context: ...
    def _context_path(self, name, suite_path: Incomplete | None = None): ...
    def _sorted_contexts(self) -> list[Context]: ...
    @property
    def _next_priority(self) -> int: ...
    def _flush_tools(self) -> None: ...
    def _validate_tool(self, context_name, tool_name) -> None: ...
    def _update_tools(self) -> None: ...

def _FWD__invoke_suite_tool_alias(context_name, tool_name, prefix_char: Incomplete | None = None, _script: Incomplete | None = None, _cli_args: Incomplete | None = None) -> None: ...
