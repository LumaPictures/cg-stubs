from _typeshed import Incomplete
from rez.config import config as config
from rez.exceptions import RezSystemError as RezSystemError, SuiteError as SuiteError
from rez.resolved_context import ResolvedContext as ResolvedContext
from rez.utils.colorize import Printer as Printer, critical as critical, heading as heading, local as local
from rez.utils.data_utils import cached_property as cached_property
from rez.utils.formatting import columnise as columnise
from rez.vendor import yaml as yaml  # type: ignore[import-not-found]
from rez.vendor.yaml.error import YAMLError as YAMLError  # type: ignore[import-not-found]
from typing import Any

class Wrapper:
    """A Wrapper.

    A wrapper is a tool created by a `Suite`. Wrappers reside in the ./bin
    directory of a suite. They are executable yaml files that are run with the
    internal '_rez-forward' tool.

    When a wrapper is executed, it runs the associated tool within the matching
    context in the suite.
    """
    def __init__(self, filepath) -> None:
        """Create a wrapper given its executable file."""
    suite_path: Any
    context_name: Any
    context: Any
    tool_name: Any
    prefix_char: Any
    def _init(self, suite_path, context_name, context, tool_name, prefix_char: Incomplete | None = None) -> None: ...
    @cached_property
    def suite(self): ...
    def run(self, *args):
        """Invoke the wrapped script.

        Returns:
            Return code of the command, or 0 if the command is not run.
        """
    def _run_no_args(self, args): ...
    def _run(self, prefix_char, args): ...
    def print_about(self) -> int:
        """Print an info message about the tool."""
    def print_package_versions(self) -> int:
        """Print a list of versions of the package this tool comes from, and
        indicate which version this tool is from."""
    def peek(self) -> int: ...
    @classmethod
    def _print_conflicting(cls, variants) -> None: ...
