import _pdg
from collections.abc import Iterable, Mapping, Sequence
from pdg import PyProcessor as PyProcessor
from typing import Any

TYPE_MAP: dict[str, type[int | str | float]]
VALID_TYPES: set[type[int | str | float]]

def get_column_type(data: object, column_name: str) -> tuple[type[int | str | float], str, int]:
    '''Parse the column name and determine the type of data.

    The column name is parsed using the format $TYPE_$TAG_$INDEX.

    The "auto" type, when parsed from the column name, means to use the actual
    Python type of data.

    If parsing fails, it uses the Python type, a tag equal to the column name
    itself, and index 0. If the Python type is not valid, it defaults to str.

    Args:
    data:        Value returned by the SQL query.
    column_name: Column name as a string

    Returns:
    (type, tag, index) as a tuple

    Examples:
        - "a string", "string_mycolumn_0" -> (str, "mycolumn", 0)
        - 5, "auto_another_column_0"      -> (int, "another_column", 0)
        - 5, "string_another_column_0"    -> (str, "another_column", 0)
    '''
def get_by_data_tag(tag: str, upstream_item: _pdg.WorkItem | None) -> Any:
    """Using a 'data tag', look up something in a work item.
    The tag is used to look up a workitem by name, or a result item by tag.

    Args:
        tag: the name or tag to search by
        upstream_item: a workitem
    Returns:
        The result of the lookup.
    """
def construct_select_query(table_name: str, extract_all: int, distinct: int, column_names: Iterable[str], order_by_cols: Iterable[tuple[str, str] | tuple[str, str, int]], limit: int) -> str:
    '''Return a string of a SELECT query given by the parameters.

    Args:
        table_name: The SQL table name.
        extract_all: A Truthy type to decide if we want a SELECT *
        distinct:    A Truthy type to decide if we want a SELECT DISTINCT.
        column_names: A tuple of strings of column names used in the query.
                      If columns are to be renamed, the strings can be like
                      "FOO AS BAR".
        order_by_cols: A tuple of pairs (column name, sort type) where column
                       name must be from the above, and sort type is either
                       "ASC" or "DESC".
        limit: An integral limit for the LIMIT clause.
    '''

class SqlNode(PyProcessor):
    """A base class with common utilities for SQL nodes."""
    def __init__(self, node: _pdg.Node) -> None: ...
    def evaluate_query(self, query: str, expr_dict: Mapping[str, object], work_item: _pdg.WorkItem | None) -> str:
        """Evaluate all expressions in the parameters and substitute the values
        into the query where there are placeholders.

        Args:
            query: string of the unevaluated query, with placeholders
            expr_dict: Expression dictionary to use for additional substitution

        Returns:
            The substituted query as a string.
        """
    def sanity_check_params(self, work_item: _pdg.WorkItem | None) -> None:
        """Check common param values."""

class SqlInput(SqlNode):
    """Input node for making a SQL query and creating workitems for each row.
    """
    def __init__(self, node: _pdg.Node) -> None: ...
    @classmethod
    def templateName(cls) -> str: ...
    @classmethod
    def templateBody(cls) -> str:
        """Template for the bare minimum parameters for use from pure Python.

        The only supported params are:
        driver:           Module name of the database driver to use.
        connectionstring: Database connection string.
        querystring:      The SQL query to be executed.
        """
    def onGenerate(self, item_holder: _pdg.WorkItemHolder, upstream_items: _pdg.WorkItemList, generation_type: _pdg.generationType) -> _pdg.result: ...

def construct_insert_query(table_name: str, column_names: Sequence[str]) -> str:
    """Construct an insert query using the given parameters.

    Args:
        table_name: Table to insert to, as a string.
        column_names: List of strings of column names.

    Returns:
        The constructed query as a string.
    """

class SqlOutput(SqlNode):
    """Node for INSERT.

    Unlike the HDA for the SqlInput node, this node does not generate a live
    preview of the query. Thus, the _onGenerate logic does more work in
    building the query compared to the sql input node.
    """
    def __init__(self, node: _pdg.Node) -> None: ...
    @classmethod
    def templateName(cls) -> str: ...
    @classmethod
    def templateBody(cls) -> str:
        """Template for the bare minimum parameters for use from pure Python.

        The only supported params are:
        driver:           Module name of the database driver to use.
        connectionstring: Database connection string.
        querystring:      The SQL query to be executed.
        """
    def setExtractions(self, table_name: str, **extractions: str) -> None:
        """For pure-python use. Set data tags for extractions and the table name.

        The keys should be column names in the table and the values should be
        the data tags used to extract data for them.

        This corresponds to setting the column names and data tags in the TOPS
        multiparm. For each name-tag pair, the value extracted using the tag
        will be inserted into into the column with the given name.

        Args:
            table_name: Table to insert into, as a string
            extractions: key-value pairs as described above.

        Returns: None
        """
    def onGenerate(self, item_holder: _pdg.WorkItemHolder, upstream_items: _pdg.WorkItemList, generation_type: _pdg.generationType) -> _pdg.result: ...

def registerTypes(type_registry: _pdg.TypeRegistry) -> None: ...
