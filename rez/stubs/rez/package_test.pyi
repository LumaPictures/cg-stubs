import rez.package_test
import rez.packages
import typing
from _typeshed import Incomplete
from rez.config import config as config
from rez.exceptions import PackageNotFoundError as PackageNotFoundError, PackageTestError as PackageTestError, RezError as RezError
from rez.packages import Package as Package, get_latest_package_from_string as get_latest_package_from_string
from rez.resolved_context import ResolvedContext as ResolvedContext
from rez.utils.colorize import Printer as Printer, heading as heading
from rez.utils.data_utils import RO_AttrDictWrapper as RO_AttrDictWrapper
from rez.utils.logging_ import print_error as print_error, print_info as print_info, print_warning as print_warning
from rez.version import Requirement as Requirement, RequirementList as RequirementList
from typing import Any

class PackageTestRunner:
    '''Object for running a package\'s tests.

    This runs the tests listed in the package\'s "tests" attribute.

    An example tests entry in a package.py might look like this:

    .. code-block:: python

       tests = {
           "unit": "python -m unittest -s {root}/tests",
           "CI": {
               "command": "python {root}/ci_tests/main.py",
               "requires": ["maya-2017"],
               "replace": True
           }
       }

    By default tests are run in an environment containing the current package.

    If a test entry is just a string, then it is treated as the test
    command. If a dict, the "command" string is the command, and the "requires"
    list is added to the test env.

    Command strings automatically expand references such as ``{root}``, much
    as happens in a :data:`commands` function.

    Commands can also be a list - in this case, the test process is launched
    directly, rather than interpreted via a shell.
    '''
    package_request: Any
    use_current_env: bool
    extra_package_requests: Any
    stdout: Any | typing.TextIO
    stderr: Any | typing.TextIO
    dry_run: bool
    stop_on_fail: bool
    cumulative_test_results: Any
    context_kwargs: dict[str, Any]
    verbose: int
    package_paths: Any
    test_results: rez.package_test.PackageTestResults
    package: rez.packages.Package | None
    contexts: dict[Any, Any]
    stopped_on_fail: bool
    timestamp: int
    def __init__(self, package_request, use_current_env: bool = False, extra_package_requests: Incomplete | None = None, package_paths: Incomplete | None = None, stdout: Incomplete | None = None, stderr: Incomplete | None = None, verbose: int = 0, dry_run: bool = False, stop_on_fail: bool = False, cumulative_test_results: Incomplete | None = None, **context_kwargs) -> None:
        """Create a package tester.

        Args:
            package_request (str or PackageRequest): The package to test.
            use_current_env (bool): If True, run the test directly in the current
                rez-resolved environment, if there is one, and if it contains
                packages that meet the test's requirements.
            extra_package_requests (list[str] or PackageRequest): Extra
                requests, these are appended to the test environment.
            package_paths: List of paths to search for pkgs, defaults to
                :data:`packages_path`.
            stdout (typing.IO): Defaults to :data:`sys.stdout`.
            stderr (typing.IO): Defaults to :data:`sys.stderr`.
            verbose (int): Verbose mode (valid values: 0, 1, 2)
            dry_run (bool): If True, do everything except actually run tests.
            cumulative_test_results (PackageTestResults): If supplied, test
                run results can be stored across multiple runners.
            context_kwargs (dict[typing.Any, typing.Any]): Extra arguments which are passed to the
                :class:`~rez.resolved_context.ResolvedContext` instances used to run the tests within.
                Ignored if ``use_current_env`` is True.
        """
    def get_package(self):
        """Get the target package.

        Returns:
            Package: Package to run tests on.
        """
    @classmethod
    def get_package_test_names(cls, package, run_on: Incomplete | None = None, ran_once: Incomplete | None = None):
        """Get the names of tests in the given package.

        Args:
            run_on (list of str): If provided, only include tests with run_on
                tags that overlap with the given list.
            ran_once (list of str): If provided, skip tests that are in this
                list, and are configured for on_variants=False (ie, just run
                the test on one variant).

        Returns:
            List of str: Test names.
        """
    def get_test_names(self, run_on: Incomplete | None = None):
        """Get the names of tests in this package.

        Args:
            run_on (list of str): If provided, only include tests with run_on
                tags that overlap with the given list.

        Returns:
            List of str: Test names.
        """
    @property
    def num_tests(self):
        """Get the number of tests, regardless of stats.
        """
    @property
    def num_success(self):
        """Get the number of successful test runs.
        """
    @property
    def num_failed(self):
        """Get the number of failed test runs.
        """
    @property
    def num_skipped(self):
        """Get the number of skipped test runs.
        """
    def run_test(self, test_name, extra_test_args: Incomplete | None = None):
        """Run a test.

        Runs the test in its correct environment. Note that if tests share the
        same requirements, the contexts will be reused.

        Args:
            test_name (str): Name of test to run.
            extra_test_args (list of str): Any extra arguments that we want to
                pass to the test command.

        Returns:
            int: Exit code of first failed test, or 0 if none failed. If the first
                test to fail did so because it was not able to run (eg its
                environment could not be configured), -1 is returned.
        """
    def print_summary(self) -> None: ...
    def _add_test_result(self, *nargs, **kwargs) -> None: ...
    @classmethod
    def _print_header(cls, txt, *nargs) -> None: ...
    def _on_variant_requires(self, variant, params):
        """
        Only run test on variants whose direct requirements are a subset of, and
        do not conflict with, the list given in 'value' param.

        For example, if on_variants.value is ['foo', 'bah'] then only variants
        containing both these requirements will be selected; ['!foo', 'bah'] would
        select those variants with bah present and not foo; ['!foo'] would
        select all variants without foo present.
        """
    def _get_test_info(self, test_name: str, variant) -> dict | None: ...
    def _get_context(self, requires, quiet: bool = False): ...
    def _get_target_variants(self, test_name):
        """
        If the test is not variant-specific, then attempt to find the 'preferred'
        variant (as per setting :data:`variant_select_mode`). Otherwise, just run tests
        over all variants.
        """

class PackageTestResults:
    """Contains results of running tests with a :class:`PackageTestRunner`.

    Use this class (and pass it to the :class:`PackageTestRunner` constructor) if you
    need to gather test run results from separate runners, and display them in
    a single table.
    """
    valid_statuses: Incomplete
    test_results: list[Any]
    def __init__(self) -> None: ...
    @property
    def num_tests(self) -> int:
        """Get the number of tests, regardless of stats.
        """
    @property
    def num_success(self) -> int:
        """Get the number of successful test runs.
        """
    @property
    def num_failed(self) -> int:
        """Get the number of failed test runs.
        """
    @property
    def num_skipped(self) -> int:
        """Get the number of skipped test runs.
        """
    def add_test_result(self, test_name, variant, status, description) -> None: ...
    def print_summary(self) -> None: ...
