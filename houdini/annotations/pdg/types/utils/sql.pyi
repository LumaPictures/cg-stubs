from collections.abc import Iterable, Mapping, Sequence
from typing import Any

import _pdg
from pdg import PyProcessor

TYPE_MAP: dict[str, type[int | str | float]]
VALID_TYPES: set[type[int | str | float]]

def get_column_type(data: object, column_name: str) -> tuple[type[int | str | float], str, int]: ...

# The attribute's values, its only value, or the paths of the output files with the tag; a
# python object attribute's value may be anything.
def get_by_data_tag(tag: str, upstream_item: _pdg.WorkItem | None) -> Any: ...
def construct_select_query(
    table_name: str,
    extract_all: int,
    distinct: int,
    column_names: Iterable[str],
    order_by_cols: Iterable[tuple[str, str] | tuple[str, str, int]],
    limit: int,
) -> str: ...

class SqlNode(PyProcessor):
    def __init__(self, node: _pdg.Node) -> None: ...
    def evaluate_query(
        self, query: str, expr_dict: Mapping[str, object], work_item: _pdg.WorkItem | None
    ) -> str: ...
    def sanity_check_params(self, work_item: _pdg.WorkItem | None) -> None: ...

class SqlInput(SqlNode):
    def __init__(self, node: _pdg.Node) -> None: ...
    @classmethod
    def templateName(cls) -> str: ...
    @classmethod
    def templateBody(cls) -> str: ...
    def onGenerate(
        self,
        item_holder: _pdg.WorkItemHolder,
        upstream_items: _pdg.WorkItemList,
        generation_type: _pdg.generationType,
    ) -> _pdg.result: ...

def construct_insert_query(table_name: str, column_names: Sequence[str]) -> str: ...

class SqlOutput(SqlNode):
    def __init__(self, node: _pdg.Node) -> None: ...
    @classmethod
    def templateName(cls) -> str: ...
    @classmethod
    def templateBody(cls) -> str: ...
    def setExtractions(self, table_name: str, **extractions: str) -> None: ...
    def onGenerate(
        self,
        item_holder: _pdg.WorkItemHolder,
        upstream_items: _pdg.WorkItemList,
        generation_type: _pdg.generationType,
    ) -> _pdg.result: ...

def registerTypes(type_registry: _pdg.TypeRegistry) -> None: ...
