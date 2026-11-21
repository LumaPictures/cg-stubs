from collections.abc import Iterable, Sequence

from typing import TypeVar
from collections.abc import Hashable
from typing import TypeVar
_T = TypeVar('_T', bound=Hashable)
_SeqT = TypeVar('_SeqT', bound=Sequence[str])
def computeIndent(line: str) -> int:
    """ Returns the indent level of the given line.
    """
def removeIndent(line: str, indent: int) -> str:
    """ Removes the requested amount of indent from a line.
    """
def uniqueList(list: Iterable[_T]) -> list[_T]:
    """ Removes duplicates from the list, preserves order
    """
def loadSnippets(filelist: Iterable[str], comment_prefix: str) -> tuple[dict[str, list[str]], dict[str, list[str]]]:
    """ Loads all the vexpressions from the VEXpression.txt
        files found in the houdini path.
    """
def expandMultiparms(snippetlist: _SeqT, multiparm_indices: Sequence[int]) -> _SeqT | list[str]:
    """
    Looks for '#' tokens in snippet strings and replaces them with the
    corresponding numeric indices in the multiparm_indices array.

    :param snippetlist: Original list of snippet strings.
    :param multiparm_indices: Array of integer multiparm indices for the parm
        that is generating this snippet list.
    :return: A list of snippet strings with multiparm token replacement done
        on each strnig in the snippetlist.
    """
def filterList(filter: str, list: Sequence[str]) -> list[int]:
    """ Used by the custom type-ahead rules when ? prefixes.

        list - array of labels in the menu
        filter - current typed filter string

        Returns an integer array.  Each element is an index
        into the label list. Results will be displayed in this order.
    """
