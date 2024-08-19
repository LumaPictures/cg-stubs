# mypy: disable-error-code="misc, override, no-redef"

import Boost.Python
import pxr.Ar
import pxr.Usd
from _typeshed import Incomplete
from typing import Callable, overload

TraceFunction: Callable
TraceMethod: Callable
TraceScope: Callable
__MFB_FULL_PACKAGE_NAME: str

class AggregateNode(Boost.Python.instance):
    """
    A representation of a call tree.


    Each node represents one or more calls that occurred in the trace.
    Multiple calls to a child node are aggregated into one node.
    """
    expanded: Incomplete
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """
    def __bool__(self) -> bool:
        """True if this object has not expired.  False otherwise."""
    def __eq__(self, other: object) -> bool:
        """Equality operator:  x == y"""
    def __lt__(self, other: object) -> bool:
        """Less than operator: x < y"""
    def __ne__(self, other: object) -> bool:
        """Non-equality operator: x != y"""
    @property
    def children(self) -> list[AggregateNode]: ...
    @property
    def count(self):
        """
        Returns the call count of this node.


        C{recursive} determines if recursive calls are counted.
        """
    @property
    def exclusiveCount(self) -> int:
        """
        Returns the exclusive count.
        """
    @property
    def exclusiveTime(self):
        """
        Returns the time spent in this node but not its children.
        """
    @property
    def expired(self): ...
    @property
    def id(self) -> pxr.Usd.StageCache.Id:
        """
        Returns the node's id.
        """
    @property
    def inclusiveTime(self) -> TimeStamp:
        """
        Returns the total time of this node ands its children.
        """
    @property
    def key(self) -> str:
        """
        Returns the node's key.
        """

class Collector(Boost.Python.instance):
    """
    This is a singleton class that records TraceEvent instances and
    populates TraceCollection instances.


    All public methods of TraceCollector are safe to call from any thread.
    """
    enabled: Incomplete
    pythonTracingEnabled: Incomplete
    def __init__(self) -> None: ...
    def BeginEvent(self, _key: str | pxr.Ar.ResolvedPath, /) -> int:
        """
        Record a begin event with *key* if C{Category} is enabled.


        A matching end event is expected some time in the future.

        If the key is known at compile time C{BeginScope} and C{Scope} methods
        are preferred because they have lower overhead.

        The TimeStamp of the TraceEvent or 0 if the collector is disabled.

        BeginScope

        Scope
        """
    def BeginEventAtTime(self, _key: str | pxr.Ar.ResolvedPath, _ms: float, /) -> None:
        """
        Record a begin event with *key* at a specified time if C{Category} is
        enabled.


        This version of the method allows the passing of a specific number of
        elapsed milliseconds, *ms*, to use for this event. This method is used
        for testing and debugging code.
        """
    def Clear(self) -> None:
        """
        Clear all pending events from the collector.


        No TraceCollection will be made for these events.
        """
    def EndEvent(self, _key: str | pxr.Ar.ResolvedPath, /) -> int:
        """
        Record an end event with *key* if C{Category} is enabled.


        A matching begin event must have preceded this end event.

        If the key is known at compile time EndScope and Scope methods are
        preferred because they have lower overhead.

        The TimeStamp of the TraceEvent or 0 if the collector is disabled.

        EndScope

        Scope
        """
    def EndEventAtTime(self, _key: str | pxr.Ar.ResolvedPath, _ms: float, /) -> None:
        """
        Record an end event with *key* at a specified time if C{Category} is
        enabled.


        This version of the method allows the passing of a specific number of
        elapsed milliseconds, *ms*, to use for this event. This method is used
        for testing and debugging code.
        """
    def GetLabel(self) -> str:
        """
        Return the label associated with this collector.
        """
    def __bool__(self) -> bool:
        """True if this object has not expired.  False otherwise."""
    def __eq__(self, other: object) -> bool:
        """Equality operator:  x == y"""
    def __lt__(self, other: object) -> bool:
        """Less than operator: x < y"""
    def __ne__(self, other: object) -> bool:
        """Non-equality operator: x != y"""
    @property
    def expired(self): ...

class Reporter(Boost.Python.instance):
    """
    This class converts streams of TraceEvent objects into call trees
    which can then be used as a data source to a GUI or written out to a
    file.
    """
    foldRecursiveCalls: bool
    groupByFunction: bool
    shouldAdjustForOverheadAndNoise: Incomplete
    def __init__(self, arg2: str | pxr.Ar.ResolvedPath, /) -> None: ...
    def ClearTree(self) -> None:
        """
        Clears event tree and counters.
        """
    def GetLabel(self) -> str:
        """
        Return the label associated with this reporter.
        """
    @overload
    def Report(self, iterationCount: int = ...) -> None: ...
    @overload
    def Report(self, arg2: str | pxr.Ar.ResolvedPath, /, iterationCount: int = ..., append: bool = ...) -> None: ...
    def ReportChromeTracing(self) -> None:
        """
        Generates a timeline trace report suitable for viewing in Chrome's
        trace viewer.
        """
    def ReportChromeTracingToFile(self, arg2: str | pxr.Ar.ResolvedPath, /) -> None: ...
    def ReportTimes(self) -> None:
        """
        Generates a report of the times to the ostream *s*.
        """
    def UpdateTraceTrees(self) -> None:
        """
        This fully re-builds the event and aggregate trees from whatever the
        current collection holds.


        It is ok to call this multiple times in case the collection gets
        appended on inbetween.

        If we want to have multiple reporters per collector, this will need to
        be changed so that all reporters reporting on a collector update their
        respective trees.
        """
    @classmethod
    def globalReporter(cls, *args, **kwargs): ...
    def __bool__(self) -> bool:
        """True if this object has not expired.  False otherwise."""
    def __eq__(self, other: object) -> bool:
        """Equality operator:  x == y"""
    def __lt__(self, other: object) -> bool:
        """Less than operator: x < y"""
    def __ne__(self, other: object) -> bool:
        """Non-equality operator: x != y"""
    @property
    def aggregateTreeRoot(self) -> AggregateNode:
        """
        Returns the root node of the aggregated call tree.
        """
    @property
    def expired(self): ...

def GetElapsedSeconds(arg1: int, arg2: int, /) -> float: ...
def GetTestEventName() -> str: ...
def PythonGarbageCollectionCallback(arg1: str | pxr.Ar.ResolvedPath, arg2: object, /) -> None: ...
def TestAuto() -> None: ...
def TestCreateEvents() -> None: ...
def TestNesting() -> None: ...
