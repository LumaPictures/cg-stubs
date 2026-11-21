# Houdini stubs generated from Houdini 22.0.466

import _pdg
import logging
from collections.abc import Iterable, Mapping, Sequence

staticlogger: logging.Logger

class StaticCookMixin:
    """
    Implementation of the static cooking logic
    """
    def __init__(self) -> None: ...
    def static_onStartCook(self) -> None:
        """
        Reset our state
        """
    def static_loadDependencies(self, dependencies: Mapping[_pdg.WorkItem, Sequence[_pdg.WorkItem]], dependents: Mapping[_pdg.WorkItem, Iterable[_pdg.WorkItem]], ready_items: Iterable[_pdg.WorkItem]) -> None:
        """
        Called at the beginning of a static cook, in onScheduleStatic
        """
    def static_completed(self, work_item_name: str, index: int) -> None:
        """
        Called when a work item finished successfully
        """
    def static_tick(self) -> None:
        """
        Called by the tick timer
        """
    def static_isWorkItemReady(self, work_item_name: str, index: int) -> bool: ...
    def static_schedule(self, work_item: _pdg.WorkItem | None) -> None:
        """
        Called when the schedule wishes to schedule an item from the
        static dependency graph
        """
