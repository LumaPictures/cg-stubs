import rez.package_filter
import rez.package_order
import rez.packages
import rez.resolved_context
import rez.resolver
import rez.solver
import rez.version._requirement
from _typeshed import Incomplete
from contextlib import contextmanager
from enum import Enum
from rez.config import config as config
from rez.package_filter import PackageFilterList as PackageFilterList, TimestampRule as TimestampRule
from rez.package_order import PackageOrder as PackageOrder
from rez.package_repository import package_repository_manager as package_repository_manager
from rez.packages import Variant as Variant, get_last_release_time as get_last_release_time, get_variant as get_variant
from rez.resolved_context import ResolvedContext as ResolvedContext
from rez.solver import Solver as Solver, SolverCallbackReturn as SolverCallbackReturn, SolverState as SolverState, SolverStatus as SolverStatus
from rez.utils.logging_ import log_duration as log_duration
from rez.utils.memcached import Client as Client, memcached_client as memcached_client, pool_memcached_connections as pool_memcached_connections
from rez.version import Requirement as Requirement
from typing import Any, Callable, Iterator

class ResolverStatus(Enum):
    """ Enum to represent the current state of a resolver instance.  The enum
    also includes a human readable description of what the state represents.
    """
    pending = ('The resolve has not yet started.',)
    solved = ('The resolve has completed successfully.',)
    failed = ('The resolve is not possible.',)
    aborted = ('The resolve was stopped by the user (via callback).',)
    description: Any
    def __init__(self, description) -> None: ...

class Resolver:
    """The package resolver.

    The Resolver uses a combination of Solver(s) and cache(s) to resolve a
    package request as quickly as possible.
    """
    context: rez.resolved_context.ResolvedContext
    package_requests: list[rez.version._requirement.Requirement]
    package_paths: list[str]
    timestamp: float | None
    callback: Callable[[rez.solver.SolverState], tuple[rez.solver.SolverCallbackReturn, str]] | None
    package_orderers: list[rez.package_order.PackageOrder] | None
    package_load_callback: Any
    building: bool
    testing: bool
    verbosity: bool
    caching: bool
    buf: Any
    suppress_passive: bool
    print_stats: bool
    package_orderers_hash: str
    package_filter_hash: str
    package_filter: rez.package_filter.PackageFilterList | None
    status_: rez.resolver.ResolverStatus
    resolved_packages_: list[rez.packages.Variant] | None
    resolved_ephemerals_: list[rez.version._requirement.Requirement] | None
    failure_description: None
    graph_: None
    from_cache: bool
    memcached_servers: Any | None
    solve_time: float
    load_time: float
    _print: Any
    def __init__(self, context: ResolvedContext, package_requests: list[Requirement], package_paths: list[str], package_filter: PackageFilterList | None = None, package_orderers: list[PackageOrder] | None = None, timestamp: float | None = 0, callback: Callable[[SolverState], tuple[SolverCallbackReturn, str]] | None = None, building: bool = False, testing: bool = False, verbosity: bool = False, buf: Incomplete | None = None, package_load_callback: Incomplete | None = None, caching: bool = True, suppress_passive: bool = False, print_stats: bool = False) -> None:
        """Create a Resolver.

        Args:
            package_requests: List of Requirement objects representing the
                request.
            package_paths: List of paths to search for pkgs.
            package_filter (`PackageFilterList`): Package filter.
            package_orderers (list of `PackageOrder`): Custom package ordering.
            callback: See `Solver`.
            package_load_callback: If not None, this callable will be called
                prior to each package being loaded. It is passed a single
                `Package` object.
            building: True if we're resolving for a build.
            testing: True if we're resolving for a rez (rez-test).
            caching: If True, cache(s) may be used to speed the resolve. If
                False, caches will not be used.
            print_stats (bool): If true, print advanced solver stats at the end.
        """
    @pool_memcached_connections
    def solve(self) -> None:
        """Perform the solve.
        """
    @property
    def status(self) -> ResolverStatus:
        """Return the current status of the resolve.

        Returns:
          ResolverStatus.
        """
    @property
    def resolved_packages(self) -> list[Variant] | None:
        """Get the list of resolved packages.

        Returns:
            List of `Variant` objects, or None if the resolve has not
            completed.
        """
    @property
    def resolved_ephemerals(self) -> list[Requirement] | None:
        """Get the list of resolved ewphemerals.

        Returns:
            List of `Requirement` objects, or None if the resolve has not
            completed.
        """
    @property
    def graph(self):
        """Return the resolve graph.

        The resolve graph shows unsuccessful as well as successful resolves.

        Returns:
            A pygraph.digraph object, or None if the solve has not completed.
        """
    def _get_variant(self, variant_handle) -> Variant: ...
    def _get_cached_solve(self):
        """Find a memcached resolve.

        If there is NOT a resolve timestamp:
            - fetch a non-timestamped memcache entry;
            - if no entry, then fail;
            - if packages have changed, then:
              - delete the entry;
              -  fail;
            - if no packages in the entry have been released since, then
              - use the entry and return;
            - else:
              - delete the entry;
              - fail.

        If there IS a resolve timestamp (let us call this T):
            - fetch a non-timestamped memcache entry;
            - if entry then:
              - if no packages have changed, then:
                - if no packages in the entry have been released since:
                  - if no packages in the entry were released after T, then
                    - use the entry and return;
                - else:
                  - delete the entry;
              - else:
                - delete the entry;
            - fetch a timestamped (T) memcache entry;
            - if no entry, then fail;
            - if packages have changed, then:
              - delete the entry;
              - fail;
            - else:
              - use the entry.

        This behaviour exists specifically so that resolves that use a
        timestamp but set that to the current time, can be reused by other
        resolves if nothing has changed. Older resolves however, can only be
        reused if the timestamp matches exactly (but this might happen a lot -
        consider a workflow where a work area is tied down to a particular
        timestamp in order to 'lock' it from any further software releases).
        """
    @contextmanager
    def _memcached_client(self) -> Iterator[Client]: ...
    def _set_cached_solve(self, solver_dict) -> None:
        """Store a solve to memcached.

        If there is NOT a resolve timestamp:
            - store the solve to a non-timestamped entry.

        If there IS a resolve timestamp (let us call this T):
            - if NO newer package in the solve has been released since T,
              - then store the solve to a non-timestamped entry;
            - else:
              - store the solve to a timestamped entry.
        """
    def _memcache_key(self, timestamped: bool = False):
        """Makes a key suitable as a memcache entry."""
    def _solve(self) -> Solver: ...
    def _set_result(self, solver_dict) -> None: ...
    @classmethod
    def _solver_to_dict(cls, solver): ...
