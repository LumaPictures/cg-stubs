from collections.abc import Container, Iterable, Sequence
from typing import TypeAlias, TypeVar

import _apex
import hou
from _typeshed import SupportsKeysAndGetItem

# What nodeToParms() updates and returns: an apex.Dict, or a python dict filled from one.
_ParmsDictT = TypeVar("_ParmsDictT", _apex.Dict, dict[str, _apex._Value | None])

def selectChannels(node: hou.OpNode, parms: Iterable[str], setScope: bool = ..., namespace: str = ...) -> None: ...
def clearChannels(node: hou.OpNode) -> None: ...

# A value is a scalar or a tuple's values, whichever the node's parm of that name is.
_ParmValue: TypeAlias = float | str | hou.Vector2 | hou.Vector3 | hou.Vector4 | Sequence[float | str]

def setNodeparmsFromDict(
    node: hou.OpNode,
    parms: SupportsKeysAndGetItem[str, _ParmValue] | _apex.Dict,
    node_parm_names: Container[str],
    parmgroup: Container[str] | None = ...,
    key: bool = ...,
    namespace: str = ...,
    frame: float | None = ...,
) -> None: ...
def setParm(parm: hou.Parm, value: float | str, frame: float) -> None: ...
def setKey(parm: hou.Parm, value: float, frame: float) -> None: ...
def nodeToParms(
    parms_dict: _ParmsDictT,
    namespace: str = ...,
    nodeparmfilter: str = ...,
    node: hou.OpNode | None = ...,
    parm_verb: hou.SopVerb | None = ...,
    frame: float | None = ...,
) -> _ParmsDictT: ...
