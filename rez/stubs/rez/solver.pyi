import rez.package_filter
import rez.package_order
import rez.packages
import rez.resolved_context
import rez.solver
import rez.version._requirement
import rez.version._version
from _typeshed import Incomplete
from contextlib import contextmanager
from enum import Enum
from rez.config import config as config
from rez.exceptions import PackageFamilyNotFoundError as PackageFamilyNotFoundError, PackageNotFoundError as PackageNotFoundError, ResolveError as ResolveError, RezSystemError as RezSystemError
from rez.package_filter import PackageFilterBase as PackageFilterBase
from rez.package_order import PackageOrder as PackageOrder
from rez.package_repository import package_repo_stats as package_repo_stats
from rez.packages import Package as Package, Variant as Variant, iter_packages as iter_packages
from rez.resolved_context import ResolvedContext as ResolvedContext
from rez.utils.data_utils import cached_property as cached_property
from rez.utils.logging_ import print_debug as print_debug
from rez.utils.typing import Protocol as Protocol, SupportsLessThan as SupportsLessThan  # type: ignore[attr-defined]
from rez.vendor.pygraph.algorithms.accessibility import accessibility as accessibility  # type: ignore[import-not-found]
from rez.vendor.pygraph.algorithms.cycles import find_cycle as find_cycle  # type: ignore[import-not-found]
from rez.vendor.pygraph.classes.digraph import digraph as digraph  # type: ignore[import-not-found]
from rez.version import Requirement as Requirement, RequirementList as RequirementList, Version as Version, VersionRange as VersionRange, VersionedObject as VersionedObject
from typing import Any, Callable, Generator, Iterator, TypeVar

T = TypeVar('T')

class SupportsWrite(Protocol):
    def write(self, /, __s: str) -> object: ...

_force_unoptimised_solver: Incomplete
SOLVER_VERSION: int

class VariantSelectMode(Enum):
    """Variant selection mode."""
    version_priority = 0
    intersection_priority = 1

class SolverStatus(Enum):
    """Enum to represent the current state of a solver instance.  The enum
    also includes a human readable description of what the state represents.
    """
    pending = ('The solve has not yet started.',)
    solved = ('The solve has completed successfully.',)
    exhausted = ('The current solve is exhausted and must be split to continue further.',)
    failed = ('The solve is not possible.',)
    cyclic = ('The solve contains a cycle.',)
    unsolved = ('The solve has started, but is not yet solved.',)

class SolverCallbackReturn(Enum):
    """Enum returned by the `callback` callable passed to a `Solver` instance.
    """
    keep_going = ('Continue the solve',)
    abort = ('Abort the solve',)
    fail = 'Stop the solve and set to most recent failure'

class _Printer:
    verbosity: Any
    buf: rez.solver.SupportsWrite | Any
    suppress_passive: bool
    pending_sub: str | None
    pending_br: bool
    last_pr: bool
    def __init__(self, verbosity, buf: SupportsWrite | None = None, suppress_passive: bool = False) -> None: ...
    def header(self, txt: str, *args: Any) -> None: ...
    def subheader(self, txt: str) -> None: ...
    def __call__(self, txt: str, *args: Any) -> None: ...
    def passive(self, txt: str, *args: Any) -> None: ...
    def br(self) -> None: ...
    def pr(self, txt: str = '', *args: Any) -> None: ...
    def __bool__(self) -> bool: ...

class SolverState:
    """Represent the current state of the solver instance for use with a
    callback.
    """
    num_solves: int
    num_fails: int
    phase: rez.solver._ResolvePhase
    def __init__(self, num_solves: int, num_fails: int, phase: _ResolvePhase) -> None: ...
    def __str__(self) -> str: ...

class _Common:
    def __repr__(self) -> str: ...

class Reduction(_Common):
    """A variant was removed because its dependencies conflicted with another
    scope in the current phase."""
    name: str
    version: Any
    variant_index: int | None
    dependency: rez.version._requirement.Requirement
    conflicting_request: rez.version._requirement.Requirement
    def __init__(self, name: str, version, variant_index: int | None, dependency: Requirement, conflicting_request: Requirement) -> None: ...
    def reducee_str(self) -> str: ...
    def involved_requirements(self) -> list[Requirement]: ...
    def __eq__(self, other: object) -> bool: ...
    def __str__(self) -> str: ...

class DependencyConflict(_Common):
    """A common dependency shared by all variants in a scope, conflicted with
    another scope in the current phase."""
    dependency: rez.version._requirement.Requirement
    conflicting_request: rez.version._requirement.Requirement
    def __init__(self, dependency: Requirement, conflicting_request: Requirement) -> None:
        """
        Args:
            dependency (`Requirement`): Merged requirement from a set of variants.
            conflicting_request (`Requirement`): The request they conflict with.
        """
    def __eq__(self, other: object) -> bool: ...
    def __str__(self) -> str: ...

class FailureReason(_Common):
    def involved_requirements(self) -> list[Requirement]: ...
    def description(self) -> str: ...

class TotalReduction(FailureReason):
    """All of a scope's variants were reduced away."""
    reductions: list[rez.solver.Reduction]
    def __init__(self, reductions: list[Reduction]) -> None: ...
    def involved_requirements(self) -> list[Requirement]: ...
    def description(self) -> str: ...
    def __eq__(self, other): ...
    def __str__(self) -> str: ...

class DependencyConflicts(FailureReason):
    """A common dependency in a scope conflicted with another scope in the
    current phase."""
    conflicts: list[rez.solver.DependencyConflict]
    def __init__(self, conflicts: list[DependencyConflict]) -> None: ...
    def involved_requirements(self) -> list[Requirement]: ...
    def description(self) -> str: ...
    def __eq__(self, other) -> bool: ...
    def __str__(self) -> str: ...

class Cycle(FailureReason):
    """The solve contains a cyclic dependency."""
    packages: list[rez.version._requirement.VersionedObject]
    def __init__(self, packages: list[VersionedObject]) -> None: ...
    def involved_requirements(self) -> list[Requirement]: ...
    def description(self) -> str: ...
    def __eq__(self, other) -> bool: ...
    def __str__(self) -> str: ...

class PackageVariant(_Common):
    """A variant of a package.
    """
    variant: rez.packages.Variant
    building: bool
    def __init__(self, variant: Variant, building: bool) -> None:
        """Create a package variant.

        Args:
            variant (`Variant`): Package variant.
            building (bool): True if a build is occurring.
        """
    @property
    def name(self) -> str: ...
    @property
    def version(self) -> Version: ...
    @property
    def index(self) -> int | None: ...
    @property
    def handle(self) -> dict[str, Any]: ...
    @cached_property
    def requires_list(self) -> RequirementList:
        """
        It is important that this property is calculated lazily. Getting the
        'requires' attribute may trigger a package load, which may be avoided if
        this variant is reduced away before that happens.
        """
    @property
    def request_fams(self) -> set[str]: ...
    @property
    def conflict_request_fams(self) -> set[str]: ...
    def get(self, pkg_name: str) -> Requirement | None: ...
    def __eq__(self, other) -> bool: ...
    def __lt__(self, other) -> bool: ...
    def __str__(self) -> str: ...

class _PackageEntry:
    """The variants in a package.

    Holds some extra state data, such as whether the variants are sorted.
    """
    package: rez.packages.Package
    variants: list[rez.solver.PackageVariant]
    solver: rez.solver.Solver
    sorted: bool
    def __init__(self, package: Package, variants: list[PackageVariant], solver: Solver) -> None: ...
    @property
    def version(self) -> Version: ...
    def __len__(self) -> int: ...
    def split(self, nvariants: int) -> tuple[_PackageEntry, _PackageEntry] | None: ...
    def sort(self) -> None:
        """Sort variants from most correct to consume, to least.

        Sort rules:

        version_priority:
        - sort by highest versions of packages shared with request;
        - THEN least number of additional packages added to solve;
        - THEN highest versions of additional packages;
        - THEN alphabetical on name of additional packages;
        - THEN variant index.

        intersection_priority:
        - sort by highest number of packages shared with request;
        - THEN sort according to version_priority

        Note:
            In theory 'variant.index' should never factor into the sort unless
            two variants are identical (which shouldn't happen) - this is just
            here as a safety measure so that sorting is guaranteed repeatable
            regardless.
        """

class _PackageVariantList(_Common):
    """A list of package variants, loaded lazily.
    """
    package_name: str
    solver: rez.solver.Solver
    entries: list[list[Any]]
    def __init__(self, package_name: str, solver: Solver) -> None: ...
    def get_intersection(self, range_: VersionRange) -> list[_PackageEntry] | None:
        """Get a list of variants that intersect with the given range.

        Args:
            range_ (`VersionRange`): Package version range.

        Returns:
            List of `_PackageEntry` objects.
        """
    def dump(self) -> None: ...
    def __str__(self) -> str: ...

class _PackageVariantSlice(_Common):
    """A subset of a variant list, but with more dependency-related info."""
    solver: rez.solver.Solver
    package_name: str
    entries: list[rez.solver._PackageEntry]
    extracted_fams: set[Any]
    been_reduced_by: set[Any]
    been_intersected_with: set[Any]
    sorted: bool
    _len: int | None
    _range: rez.version._version.VersionRange | None
    _fam_requires: set[str] | None
    _common_fams: set[str] | None
    def __init__(self, package_name: str, entries: list[_PackageEntry], solver: Solver) -> None:
        """
        Args:
            entries (list of `_PackageEntry`): result of
                _PackageVariantList.get_intersection().
        """
    @property
    def pr(self) -> _Printer: ...
    @property
    def range_(self) -> VersionRange: ...
    @property
    def fam_requires(self) -> set[str]: ...
    @property
    def common_fams(self) -> set[str]: ...
    @property
    def extractable(self) -> bool:
        """True if there are possible remaining extractions."""
    @property
    def first_variant(self) -> PackageVariant: ...
    def iter_variants(self) -> Iterator[PackageVariant]: ...
    def intersect(self, range_: VersionRange) -> _PackageVariantSlice | None: ...
    def reduce_by(self, package_request: Requirement) -> tuple[_PackageVariantSlice | None, list[Reduction]]:
        """Remove variants whos dependencies conflict with the given package
        request.

        Returns:
            (VariantSlice, [Reduction]) tuple, where slice may be None if all
            variants were reduced.
        """
    def _reduce_by(self, package_request: Requirement) -> tuple[_PackageVariantSlice | None, list[Reduction]]: ...
    def extract(self) -> tuple[_PackageVariantSlice, Requirement | None]:
        """Extract a common dependency.

        Note that conflict dependencies are never extracted, they are always
        resolved via reduction.
        """
    def split(self) -> tuple[_PackageVariantSlice, _PackageVariantSlice]:
        """Split the slice.

        Returns:
            (`_PackageVariantSlice`, `_PackageVariantSlice`) tuple, where the
            first is the preferred slice.
        """
    def sort_versions(self) -> None:
        """Sort entries by version.

        The order is typically descending, but package order functions can
        change this.
        """
    def dump(self) -> None: ...
    def _copy(self, new_entries: list[_PackageEntry]) -> _PackageVariantSlice: ...
    def _update_fam_info(self) -> None: ...
    def __len__(self) -> int: ...
    def __str__(self) -> str:
        """
        foo[2..6(3:4)]* means, 3 versions, 4 variants in 2..6, and at least one
            family can still be extracted.
        foo[2..6(2)] means, 2 versions in 2..6.
        [foo==2[1,2]] means, 1st and 2nd variants of exact version foo-2.
        [foo==2]* means, exact version foo-2, families still to extract.
        [foo==2] means a resolved package (no variants in the package).
        [foo=2[0]] means a resolved package (zeroeth variant).
        """

class PackageVariantCache:
    solver: rez.solver.Solver
    variant_lists: dict[str, rez.solver._PackageVariantList]
    def __init__(self, solver: Solver) -> None: ...
    def get_variant_slice(self, package_name: str, range_: VersionRange) -> _PackageVariantSlice | None:
        """Get a list of variants from the cache.

        Args:
            package_name (str): Name of package.
            range_ (`VersionRange`): Package version range.

        Returns:
            `_PackageVariantSlice` object.
        """

class _PackageScope(_Common):
    """Contains possible solutions for a package, such as a list of variants,
    or a conflict range. As the resolve progresses, package scopes are narrowed
    down.
    """
    package_name: str
    solver: rez.solver.Solver
    variant_slice: rez.solver._PackageVariantSlice | None
    pr: rez.solver._Printer
    is_ephemeral: bool
    package_request: rez.version._requirement.Requirement
    def __init__(self, package_request: Requirement, solver: Solver) -> None: ...
    @property
    def is_conflict(self) -> bool: ...
    def intersect(self, range_: VersionRange) -> _PackageScope | None:
        """Intersect this scope with a package range.

        Returns:
            A new copy of this scope, with variants whos version fall outside
            of the given range removed. If there were no removals, self is
            returned. If all variants were removed, None is returned.
        """
    def reduce_by(self, package_request: Requirement) -> tuple[_PackageScope | None, list[Reduction]]:
        """Reduce this scope wrt a package request.

        Returns:
            A (_PackageScope, [Reduction]) tuple, where the scope is a new
            scope copy with reductions applied, or self if there were no
            reductions, or None if the scope was completely reduced.
        """
    def extract(self) -> tuple[_PackageScope, Requirement | None]:
        """Extract a common dependency.

        Returns:
            A (_PackageScope, Requirement) tuple, containing the new scope copy
            with the extraction, and the extracted package range. If no package
            was extracted, then (self,None) is returned.
        """
    def split(self) -> tuple[_PackageScope, _PackageScope] | None:
        """Split the scope.

        Returns:
            A (_PackageScope, _PackageScope) tuple, where the first scope is
            guaranteed to have a common dependency. Or None, if splitting is
            not applicable to this scope.
        """
    def _copy(self, new_slice: _PackageVariantSlice) -> _PackageScope: ...
    def _is_solved(self) -> bool: ...
    def _get_solved_variant(self) -> PackageVariant | None: ...
    def _get_solved_ephemeral(self) -> Requirement | None: ...
    def _update(self) -> None: ...
    def __str__(self) -> str: ...

def _get_dependency_order(g: digraph, node_list: list[T]) -> list[T]:
    """Return list of nodes as close as possible to the ordering in node_list,
    but with child nodes earlier in the list than parents."""

class _ResolvePhase(_Common):
    """A resolve phase contains a full copy of the resolve state, and runs the
    resolve algorithm until no further action can be taken without 'selecting'
    a sub-range of some package. When this selection occurs, a phase splits
    into two - one with the selected subrange, and one without - and these two
    new phases replace this phase on the solver's phase stack.

    If the resolve phase gets to a point where every package scope is solved,
    then the entire resolve is considered to be solved.
    """
    solver: rez.solver.Solver
    failure_reason: rez.solver.FailureReason | None
    extractions: dict[tuple[str, str], rez.version._requirement.Requirement]
    status: rez.solver.SolverStatus
    scopes: list[rez.solver._PackageScope]
    changed_scopes_i: set[int]
    def __init__(self, solver: Solver) -> None: ...
    @property
    def pr(self) -> _Printer: ...
    def solve(self) -> _ResolvePhase:
        """Attempt to solve the phase."""
    def finalise(self) -> _ResolvePhase:
        """Remove conflict requests, detect cyclic dependencies, and reorder
        packages wrt dependency and then request order.

        Returns:
            A new copy of the phase with conflict requests removed and packages
            correctly ordered; or, if cyclic dependencies were detected, a new
            phase marked as cyclic.
        """
    def split(self) -> tuple[_ResolvePhase, _ResolvePhase]:
        """Split the phase.

        When a phase is exhausted, it gets split into a pair of phases to be
        further solved. The split happens like so:
        1) Select the first unsolved package scope.
        2) Find some common dependency in the first N variants of the scope.
        3) Split the scope into two: [:N] and [N:].
        4) Create two copies of the phase, containing each half of the split
           scope.

        The result of this split is that we have a new phase (the first phase),
        which contains a package scope with a common dependency. This
        dependency can now be intersected with the current resolve, thus
        progressing it.

        Returns:
            A 2-tuple of _ResolvePhase objects, where the first phase is the
            best contender for resolving.
        """
    def get_graph(self) -> digraph:
        """Get the resolve graph.

        The resolve graph shows what packages were resolved, and the
        relationships between them. A failed phase also has a graph, which
        will shows the conflict(s) that caused the resolve to fail.

        Returns:
            A pygraph.digraph object.
        """
    def _get_minimal_graph(self) -> digraph | None: ...
    def _is_solved(self) -> bool: ...
    def _get_solved_variants(self) -> list[PackageVariant]: ...
    def _get_solved_ephemerals(self) -> list[Requirement]: ...
    def __str__(self) -> str: ...

class Solver(_Common):
    """Solver.

    A package solver takes a list of package requests (the 'request'), then
    runs a resolve algorithm in order to determine the 'resolve' - the list of
    non-conflicting packages that include all dependencies.
    """
    max_verbosity: int
    package_paths: list[str]
    package_filter: rez.package_filter.PackageFilterBase | None
    package_orderers: list[rez.package_order.PackageOrder] | None
    callback: Callable[[rez.solver.SolverState], tuple[rez.solver.SolverCallbackReturn, str]] | None
    prune_unfailed: bool
    package_load_callback: Callable[[rez.packages.Package], Any] | None
    building: bool
    context: rez.resolved_context.ResolvedContext | None
    pr: rez.solver._Printer
    print_stats: bool
    buf: rez.solver.SupportsWrite | None
    optimised: bool
    phase_stack: list[rez.solver._ResolvePhase]
    failed_phase_list: list[rez.solver._ResolvePhase]
    depth_counts: dict[Any, Any]
    solve_begun: bool
    solve_time: float
    load_time: float
    abort_reason: str | None
    callback_return: rez.solver.SolverCallbackReturn | None
    solve_count: int
    extractions_count: int
    intersections_count: int
    intersection_tests_count: int
    intersection_broad_tests_count: int
    reductions_count: int
    reduction_tests_count: int
    reduction_broad_tests_count: int
    extraction_time: list[float]
    intersection_time: list[float]
    intersection_test_time: list[float]
    reduction_time: list[float]
    reduction_test_time: list[float]
    package_cache: rez.solver.PackageVariantCache
    request_list: rez.version._requirement.RequirementList
    def __init__(self, package_requests: list[Requirement], package_paths: list[str], context: ResolvedContext | None = None, package_filter: PackageFilterBase | None = None, package_orderers: list[PackageOrder] | None = None, callback: Callable[[SolverState], tuple[SolverCallbackReturn, str]] | None = None, building: bool = False, optimised: bool = True, verbosity: int = 0, buf: SupportsWrite | None = None, package_load_callback: Callable[[Package], Any] | None = None, prune_unfailed: bool = True, suppress_passive: bool = False, print_stats: bool = False) -> None:
        """Create a Solver.

        Args:
            package_requests: List of Requirement objects representing the
                request.
            package_paths: List of paths to search for pkgs.
            context (`ResolvedContext`): Context this solver is used within, if
                any. This is needed in a solve if any packages contain late
                binding package attributes that need access to context info.
            package_filter (`PackageFilterBase`): Filter for excluding packages.
            package_orderers (list of `PackageOrder`): Custom package ordering.
            building: True if we're resolving for a build.
            optimised: Run the solver in optimised mode. This is only ever set
                to False for testing purposes.
            callback: If not None, this callable will be called after each
                solve step. It is passed a `SolverState` object. It must return
                a 2-tuple:
                - `SolverCallbackReturn` object indicating what to do next;
                - str: Reason for solve abort, ignored if solve not aborted.
                If the callable returns `SolverCallbackReturn.fail`, but there
                has not been a failure, the solver will ignore the callback and
                continue on with the solve.
            package_load_callback: If not None, this callable will be called
                prior to each package being loaded. It is passed a single
                `Package` object.
            prune_unfailed (bool): If the solve failed, and `prune_unfailed` is
                True, any packages unrelated to the conflict are removed from
                the graph.
            suppress_passive (bool): If True, don't print debugging info that
                has had no effect on the solve. This argument only has an
                effect if `verbosity` > 2.
            print_stats (bool): If true, print advanced solver stats at the end.
        """
    @contextmanager
    def timed(self, target: list[float]) -> Generator: ...
    @property
    def status(self) -> SolverStatus:
        """Return the current status of the solve.

        Returns:
          SolverStatus: Enum representation of the state of the solver.
        """
    @property
    def num_solves(self) -> int:
        """Return the number of solve steps that have been executed."""
    @property
    def num_fails(self) -> int:
        """Return the number of failed solve steps that have been executed.
        Note that num_solves is inclusive of failures."""
    @property
    def cyclic_fail(self) -> bool:
        """Return True if the solve failed due to a cycle, False otherwise."""
    @property
    def resolved_packages(self) -> list[PackageVariant] | None:
        """Return a list of resolved variants.

        Returns:
            list of `PackageVariant`: Resolved variants, or None if the resolve
            did not complete or was unsuccessful.
        """
    @property
    def resolved_ephemerals(self) -> list[Requirement] | None:
        """Return the list of final ephemeral package ranges.

        Note that conflict ephemerals are not included.

        Returns:
            List of `Requirement`: Final non-conflict ephemerals, or None
            if the resolve did not complete or was unsuccessful.
        """
    def reset(self) -> None:
        """Reset the solver, removing any current solve."""
    def solve(self) -> None:
        """Attempt to solve the request.
        """
    @property
    def solve_stats(self) -> dict[str, dict[str, Any]]: ...
    def solve_step(self) -> None:
        """Perform a single solve step.
        """
    def failure_reason(self, failure_index: int | None = None) -> FailureReason | None:
        """Get the reason for a failure.

        Args:
            failure_index: Index of the fail to return the graph for (can be
                negative). If None, the most appropriate failure is chosen
                according to these rules:

                - If the fail is cyclic, the most recent fail (the one containing
                  the cycle) is used;
                - If a callback has caused a failure, the most recent fail is used;
                - Otherwise, the first fail is used.

        Returns:
            A `FailureReason` subclass instance describing the failure.
        """
    def failure_description(self, failure_index: int | None = None) -> str:
        """Get a description of the failure.

        This differs from `failure_reason` - in some cases, such as when a
        callback forces a failure, there is more information in the description
        than there is from `failure_reason`.
        """
    def failure_packages(self, failure_index: int | None = None) -> list[Requirement] | None:
        """Get packages involved in a failure.

        Args:
            failure_index: See `failure_reason`.

        Returns:
            A list of Requirement objects.
        """
    def get_graph(self) -> digraph:
        """Returns the most recent solve graph.

        This gives a graph showing the latest state of the solve. The specific
        graph returned depends on the solve status. When status is:
        unsolved: latest unsolved graph is returned;
        solved:   final solved graph is returned;
        failed:   most appropriate failure graph is returned (see `failure_reason`);
        cyclic:   last failure is returned (contains cycle).

        Returns:
            A pygraph.digraph object.
        """
    def get_fail_graph(self, failure_index: int | None = None) -> digraph:
        """Returns a graph showing a solve failure.

        Args:
            failure_index: See `failure_reason`

        Returns:
            A pygraph.digraph object.
        """
    def dump(self) -> None:
        """Print a formatted summary of the current solve state."""
    def _init(self) -> None: ...
    def _latest_nonfailed_phase(self) -> _ResolvePhase | None: ...
    def _do_callback(self) -> bool: ...
    def _get_variant_slice(self, package_name: str, range_: VersionRange) -> _PackageVariantSlice | None: ...
    def _push_phase(self, phase: _ResolvePhase) -> None: ...
    def _pop_phase(self) -> _ResolvePhase: ...
    def _get_failed_phase(self, index: int | None = None) -> tuple[_ResolvePhase, str]: ...
    def _depth_label(self, depth: int | None = None) -> str: ...
    def __str__(self) -> str: ...

def _short_req_str(package_request: Requirement) -> str:
    """print shortened version of '==X|==Y|==Z' ranged requests."""
