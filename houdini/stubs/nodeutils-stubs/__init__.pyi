import hou
import re
from collections import defaultdict
from collections.abc import Generator, Iterable, Mapping, Sequence
from typing import Generic

from typing import TypeVar
from typing import TypeVar
_PosT_co = TypeVar('_PosT_co', bound=int | None, covariant=True, default=int | None)
part_pattern: str
neg_pattern: str
part_exp: re.Pattern[str]
valid_name: re.Pattern[str]

class NodeMissingError(Exception): ...

class Part(Generic[_PosT_co]):
    pos: _PosT_co
    is_glob: bool
    def __init__(self) -> None: ...
    def as_regex(self) -> str: ...
    def replacement(self, context: RenameContext) -> str: ...
    def is_star(self) -> bool: ...
    def is_negation(self) -> bool: ...

class Literal(Part[int | None]):
    text: str
    def __init__(self, text: str) -> None: ...
    def as_regex(self) -> str: ...
    def replacement(self, context: RenameContext) -> str: ...

class Glob(Part[int]):
    pattern: str
    pos: int
    capturing: bool
    unique: bool
    following_negation: Negation | None
    is_glob: bool
    def __init__(self, pattern: str, pos: int, capturing: bool = True) -> None: ...
    def is_star(self) -> bool: ...
    def as_regex(self) -> str: ...
    def replacement(self, context: RenameContext) -> str: ...

class Negation(Part[int | None]):
    glob: Glob
    def __init__(self, pattern: str) -> None: ...
    def is_negation(self) -> bool: ...
    def as_regex(self) -> str: ...
    def replacement(self, context: RenameContext) -> str: ...

class GroupRef(Part[int | None]):
    text: str
    num: int
    def __init__(self, text: str, num: int) -> None: ...
    def as_regex(self) -> str: ...
    def replacement(self, context: RenameContext) -> str: ...

class RenameContext:
    pattern_map: dict[str, int]
    counters: defaultdict[str, int]
    groups: tuple[str, ...]
    def __init__(self, find_parts: Iterable[Part[int | None]]) -> None: ...

def find_and_replace(find: str, replace: str, names: Iterable[str], whole_name: bool = False, ignore_case: bool = True) -> list[tuple[str, str]]:
    '''
    Returns a list of `(oldname, newname)` changes to make given the find
    string, replace string, and list of names to consider. The list of names can
    be from all nodes in the current network or the selected nodes.

    :param find: a string containing the text/globs to search for.
    :param replace: a string containg the text/globs to replace matches with.
    :param names: the list of names to consider for renaming.
    :param whole_name: whether the "find" pattern must match the entire name.
        If this is False, substring matches are allowed.
    :param ignore_case: whether to ignore uppercase/lowercase differences when
        comparing names.
    :return: list of `(oldname, newname)` tuples.
    '''
def find_renames(network: hou.Node, find: str, replace: str, selected: bool = False, whole_name: bool = False, unique_names: bool = False, ignore_case: bool = True) -> list[tuple[str, str, str | None]]:
    '''
    For use by the GUI, finds renames for the given network, and returns a list
    of `(oldname, newname, error)` tuples. This does not rename anything; it
    just returns the information to populate the GUI.

    :param network: a hou.Node object representing the parent network.
    :param find: the string/globs to find.
    :param replace: the string/globs to replace matches with.
    :param selected: whether to try to rename all nodes (selected=False) or only
        the currently selected nodes (selected=True).
    :param whole_name: whether the "find" pattern must match the entire name.
        If this is False, substring matches are allowed.
    :param unique_names: If True, renames that conflict with existing names will
        have numbers appended.
    :param ignore_case: whether to ignore uppercase/lowercase differences when
        comparing names.
    :return: list of `(oldname, newname, error)` tuples.
    '''
def find_renames_list(matching_networks: Iterable[hou.Node], find: str, replace: str, selected: bool = False, whole_name: bool = False, unique_names: bool = False, enable_pattern: bool = False, ignore_case: bool = True) -> list[tuple[str, str, str | None]]:
    """
    Returns find_renames changes for a list of networks. If pattern_matching is
    enabled, oldname and newname are replaced by the full path of the old node
    name and new node name instead.
    """
def count_conflicts(changes: Iterable[tuple[str, str, str | None]]) -> int: ...
def check_conflicts(network: hou.Node, find: str, replace: str, selected: bool = False, whole_name: bool = False, unique_names: bool = False) -> bool: ...
def find_conflicts(network: hou.Node, changes: Iterable[tuple[str, str]], unique_names: bool = False) -> Generator[tuple[str, str, str | None], None, None]:
    """
    Generates a list of (oldname, newname, error) tuples. This can be used to
    present a preview to the user with any potential conflicts noted.

    :param network: a hou.Node object representing the network in which
        the renames will take place.
    :param changes: a list of `(oldname, newname)` tuples.
    :param unique_names: If True, renames that conflict with existing names will
        have numbers appended. This means this function will not report existing
        name conflicts as errors.
    :return: a generator of `(oldname, newname, message)` tuples, where
        `message` is an error message string or `None`.
    """
def naturalSortKey(s: str) -> tuple[str | int, ...]: ...
def rename_nodes(network: hou.Node, find: str, replace: str, selected: bool = False, whole_name: bool = False, errors: list[tuple[str, str, str]] | None = None, unique_names: bool = False, fail_fast: bool = False, ignore_case: bool = True) -> bool:
    '''
    A high-level function to rename nodes, for use in scripts. Unlike the GUI
    equivalent, this function does not check the validity of the renames first.
    
    This function will perform the renames it can, and ignore renames that
    cause an error (such as renaming to an invalid name or renaming to a name
    that exists). If you supply a list in the `errors` argument, the function
    will append tuples to it representing the renames that failed.
    
    The function returns True if all renames were successful, or False if
    there were any errors.
                 
    The function puts the renames inside an undo block, you can undo any renames
    performed by calling `hou.undos.performUndo()`.

    :param network: a hou.Node object representing the parent network.
    :param find: the string/globs to find.
    :param replace: the string/globs to replace matches with.
    :param selected: whether to try to rename all nodes (selected=False) or only
        the currently selected nodes (selected=True).
    :param whole_name: whether the "find" pattern must match the entire name.
        If this is False, substring matches are allowed.
    :param errors: if this is not None, the function assumes it\'s a list and
        appends `(oldname, newname, error_msg)` tuples to it each time a rename
        fails.
    :param unique_names: If True, renames that conflict with existing names will
        have numbers appended.
    :param fail_fast: if True, the function exits after the first error, instead
        of ignoring errors and trying to perform the other renames.
    :param ignore_case: whether to ignore uppercase/lowercase differences when
        comparing names.
    '''
def rename_nodes_list(matching_networks: Iterable[hou.Node], find: str, replace: str, selected: bool = False, whole_name: bool = False, errors: list[tuple[str, str, str]] | None = None, unique_names: bool = False, fail_fast: bool = False, ignore_case: bool = True) -> None:
    """
    Rename nodes for a list of networks.
    """

class NodeCommentEditor:
    """ Class for editing node tags. 
    """
    theNodeCommentEditors: dict[hou.Node, NodeCommentEditor]
    @staticmethod
    def findOrCreateDialogFor(node: hou.Node) -> None:
        """ Looks for an existing comment editor dialog for the given node
            and returns it, or if not found, creates a new one and returns it.
        """
    def __init__(self, node: hou.Node) -> None: ...
    def show(self) -> None: ...
    def raise_(self) -> None: ...

def show_comment_editor(node: hou.Node | None) -> None:
    """ Pops up a text editor dialog for editing node comment, and
        allows the user to inspect and edit comment for the given node.

        :param node: a hou.Node whose comment to edit.
    """

class NodeTagEditor:
    """ Class for editing node tags. 
    """
    theNodeTagEditors: dict[tuple[hou.UniNode, ...], NodeTagEditor]
    @staticmethod
    def findOrCreateDialogFor(node_or_nodes: hou.UniNode | Iterable[hou.UniNode]) -> None:
        """ Looks for an existing node tag editor dialog for the given nodes
            and returns it, or if not found, creates a new one and returns it.
        """
    def __init__(self, nodes: tuple[hou.UniNode, ...]) -> None: ...
    def show(self) -> None: ...
    def raise_(self) -> None: ...

def show_tag_editor(node_or_nodes: hou.UniNode | Sequence[hou.UniNode] | None) -> None:
    """ Pops up a string list editor dialog for editing node tags, and
        allows the user to inspect and edit tags for the given node or nodes.

        :param node: a hou.Node or a list of hou.Nodes whose tags to edit.
    """

class NodePropertyViewer:
    theNodePropertyViewers: dict[hou.ApexNode, NodePropertyViewer]
    @staticmethod
    def findOrCreateDialogFor(node: hou.ApexNode, props: Mapping[str, object]) -> None:
        """ Looks for an existing property viewer dialog for the given node
            and returns it, or if not found, creates a new one and returns it.
        """
    def __init__(self, node: hou.ApexNode, props: Mapping[str, object]) -> None: ...
    def show(self) -> None: ...
    def raise_(self) -> None: ...

def show_property_viewer(node: hou.ApexNode | None, props: Mapping[str, object]) -> None:
    """ Opens a text dialog for viewing node properties."""
