# Houdini stubs generated from Houdini 22.0.466

import _pdg
import logging
from collections.abc import Iterable, Sequence
from pdg.processor import PyProcessor as PyProcessor

XMLRPC: int
RAW: int
CUSTOM_COUNT: int
UPSTREAM_ITEMS: int
PARTITION_ITEMS: int
PER_PARTITION_LOOP: int
SINGLE_LOOP: int
logger: logging.Logger

def feedbackParameters() -> list[dict[str, str]]: ...
def feedbackDependencies(node: PyProcessor, dependency_holder: _pdg.DependencyHolder, internal_items: Iterable[_pdg.WorkItem]) -> None: ...
def feedbackConfigure(node: PyProcessor, node_options: _pdg.NodeOptions) -> None: ...
def feedbackBegin(node: PyProcessor, item_holder: _pdg.WorkItemHolder, upstream_items: Sequence[_pdg.WorkItem], generation_type: _pdg.generationType) -> None: ...
