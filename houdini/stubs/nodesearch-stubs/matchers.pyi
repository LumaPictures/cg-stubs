# Houdini stubs generated from Houdini 22.0.466

import hou
from collections.abc import Callable, Sequence

from typing import TypeAlias
from typing import TypeAlias
_ParmOp: TypeAlias = Callable[[int | float | str | dict[str, str] | hou.Ramp | hou.Geometry | None, float | str], bool]
class Matcher:
    """
    Base class for all matchers.
    """
    fast: bool
    def __eq__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    def matches_items(self) -> bool: ...
    def normalized(self) -> Matcher:
        """
        Returns a normalized version of this matcher.
        """
    def nodes(self, network: hou.Node, ignore_case: bool = False, recursive: bool = False, recurse_in_locked_nodes: bool = True) -> Sequence[hou.NetworkMovableItem]:
        """
        Returns a sequence of nodes matching this criterion in the given
        network.
        :param network: a hou.Node representing the parent network.
        """
    def matches(self, node: hou.NetworkMovableItem, ignore_case: bool = False) -> bool:
        """
        Returns True if this criterion matches the given hou.Node instance.
        """
    def matches_container(self, node: hou.NetworkMovableItem, ignore_case: bool = False) -> bool: ...

class All(Matcher):
    """
    Matches all nodes in the network.
    """
    fast: bool
    def nodes(self, network: hou.Node, ignore_case: bool = False, recursive: bool = False, recurse_in_locked_nodes: bool = True) -> tuple[hou.NetworkMovableItem, ...]: ...
    def matches(self, node: hou.NetworkMovableItem, ignore_case: bool = False) -> bool: ...

class Null(Matcher):
    """
    Matches no nodes.
    """
    fast: bool
    def nodes(self, network: hou.Node, ignore_case: bool = False, recursive: bool = False, recurse_in_locked_nodes: bool = True) -> tuple[()]: ...
    def matches(self, node: hou.NetworkMovableItem, ignore_case: bool = False) -> bool: ...

class Name(Matcher):
    """
    Matches nodes by name.
    """
    name: str
    exact: bool
    fast: bool
    def __init__(self, name: str, exact: bool = False) -> None:
        """
        :param name: the string to match.
        :param exact: if True, only match the name exactly. Otherwise, match
            a substring.
        """
    def normalized(self) -> All | Name: ...
    def nodes(self, network: hou.Node, ignore_case: bool = False, recursive: bool = False, recurse_in_locked_nodes: bool = True) -> Sequence[hou.NetworkMovableItem]: ...
    def matches(self, node: hou.NetworkMovableItem, ignore_case: bool = False) -> bool: ...

class Tag(Matcher):
    """
    Matches nodes by their tags.
    """
    tag: str
    exact: bool
    fast: bool
    def __init__(self, tag: str, exact: bool = False) -> None:
        """
        :param tag: the string to match.
        :param exact: if True, only match the name exactly. Otherwise, match
            a substring.
        """
    def matches(self, node: hou.NetworkMovableItem, ignore_case: bool = False) -> bool: ...

class Parm(Matcher):
    """
    Matches by the value of a parameter.
    """
    name: str
    op: str | _ParmOp
    value: str | float
    ops: dict[str, _ParmOp]
    def __init__(self, name: str, op: str | _ParmOp, value: str | float) -> None:
        '''
        :param name: The internal name of the parameter.
        :param op: The function to use to compare the parameter\'s value with
            the given value. This can be a string, e.g. "<=", in which case
            the object will use the appropriate function. The special operation
            "~=" means compare using Houdini\'s pattern matching function.
        :param value: Compare the current parameter value to this value.
        '''
    def matches(self, node: hou.NetworkMovableItem, ignore_case: bool = False) -> bool: ...

class RawParm(Matcher):
    """
    Matches by the raw (unevaluated, unexpanded) value of a parameter.
    """
    name: str
    value: str
    is_pattern: bool
    exact: bool
    def __init__(self, name: str, value: str, is_pattern: bool = False, exact: bool = False) -> None:
        """
        :param name: The internal name of the parameter.
        :param value: Compare the current parameter value to this value.
        :param is_pattern: Treat the value as a pattern to match against the
            parameter value.
        :param exact: Only match if the whole string matches; otherwise match
            if the parameter value contains the target value.
        """
    def matches(self, node: hou.NetworkMovableItem, ignore_case: bool = False) -> bool | None: ...

class State(Matcher):
    """
    Matches node flags and certain other states (has a comment, has a warning,
    has an error, has descriptive text) being on or off.
    """
    name: str
    value: bool
    fn: Callable[[hou.OpNode], bool] | None
    states: dict[str, Callable[[hou.OpNode], bool]]
    def __init__(self, name: str, value: bool) -> None:
        """
        :param name: the name of the flag/state to check.
        :param value: the value (True or False) the named flag/state must have.
        """
    def matches(self, node: hou.NetworkMovableItem, ignore_case: bool = False) -> bool: ...

class NodeType(Matcher):
    """
    Matches nodes with the given node type.
    """
    typecat: hou.NodeTypeCategory | str | None
    typename: str
    exact: bool
    def __init__(self, typename: str, typecat: hou.NodeTypeCategory | str | None = None, exact: bool = False) -> None:
        """
        :param typename: the string to match.
        :param typecat: the type category to match. `None` matches any category.
            If this is a string, it will be converted to a hou.NodeTypeCategory.
        :param exact: if True, only match the typename exactly. Otherwise, match
            a substring.
        """
    def normalized(self) -> All | NodeType: ...
    def matches(self, node: hou.NetworkMovableItem, ignore_case: bool = False) -> bool: ...

class ParameterState(Matcher):
    '''
    Matches nodes which have at least one parameter in a certain state.

    `ParameterState("off_default_parm")` matches nodes with at least one
    parameter that is not at its default value.

    `ParameterState("spare_parm")` matches nodes with at least one
    spare parameter.

    `ParameterState("animated_parm")` matches nodes with at least one animated
    (time-dependent) parameter.

    `ParameterState("expression_parm")` matches nodes with at least one
    non-default parameter with an expression.
    '''
    condition: Callable[[hou.Parm], bool]
    def __init__(self, condition: str | Callable[[hou.Parm], bool]) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def matches(self, node: hou.NetworkMovableItem, ignore_case: bool = False) -> bool: ...

class Netbox(Matcher):
    comment: str
    exact: bool
    def __init__(self, comment: str, exact: bool = False) -> None: ...
    def matches_items(self) -> bool: ...
    def matches(self, node: hou.NetworkMovableItem, ignore_case: bool = False) -> bool: ...
    def matches_container(self, node: hou.NetworkMovableItem, ignore_case: bool = False) -> bool: ...

class StickyNote(Matcher):
    text: str
    exact: bool
    def __init__(self, text: str, exact: bool = False) -> None: ...
    def matches_items(self) -> bool: ...
    def matches(self, node: hou.NetworkMovableItem, ignore_case: bool = False) -> bool: ...

class Wrapper(Matcher):
    """
    Base class for matchers that modify the behavior of other matchers.
    """
    child: Matcher
    fast: bool
    def __init__(self, child: Matcher) -> None: ...
    def matches_items(self) -> bool: ...
    def matches(self, node: hou.NetworkMovableItem, ignore_case: bool = False) -> bool: ...

class Not(Wrapper):
    """
    Reverses the meaning of the wrapped matcher.
    """
    def matches(self, node: hou.NetworkMovableItem, ignore_case: bool = False) -> bool: ...
    def nodes(self, network: hou.Node, ignore_case: bool = False, recursive: bool = False, recurse_in_locked_nodes: bool = True) -> Sequence[hou.NetworkMovableItem]: ...

class Input(Wrapper):
    """
    Matches nodes that have an input that matches the wrapped matcher.
    """
    def matches(self, node: hou.NetworkMovableItem, ignore_case: bool = False) -> bool: ...

class Output(Wrapper):
    """
    Matches nodes that have an output that matches the wrapped matcher.
    """
    def matches(self, node: hou.NetworkMovableItem, ignore_case: bool = False) -> bool: ...

class Contents(Wrapper):
    """
    Matches the nodes _inside_ the nodes/items that match the wrapped matcher.
    """
    def nodes(self, network: hou.Node, ignore_case: bool = False, recursive: bool = False, recurse_in_locked_nodes: bool = True) -> list[hou.NetworkMovableItem]: ...
    def matches(self, node: hou.NetworkMovableItem, ignore_case: bool = False) -> bool: ...

class Group(Matcher):
    """
    Combines the results of multiple sub-matchers.
    """
    children: Sequence[Matcher]
    intersect: bool
    def __init__(self, children: Sequence[Matcher], intersect: bool = True) -> None:
        """

        :param children: The sub-matchers to combine.
        :param intersect: If True, only match if *all* sub-matchers match (AND).
            If False, match if *any* sub-matchers match (OR).
        """
    def matches_items(self) -> bool: ...
    def normalized(self) -> Matcher: ...
    def nodes(self, network: hou.Node, ignore_case: bool = False, recursive: bool = False, recurse_in_locked_nodes: bool = True) -> Sequence[hou.NetworkMovableItem]: ...
    def matches(self, node: hou.NetworkMovableItem, ignore_case: bool = False) -> bool: ...
