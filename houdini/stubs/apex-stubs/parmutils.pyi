import _apex
import hou
from _typeshed import SupportsKeysAndGetItem
from collections.abc import Container, Iterable

from typing import TypeAlias
from typing import TypeVar
from collections.abc import Sequence
from typing import TypeAlias
from typing import TypeVar
_ParmsDictT = TypeVar('_ParmsDictT', _apex.Dict, dict[str, _apex._Value | None])
_ParmValue: TypeAlias = float | str | hou.Vector2 | hou.Vector3 | hou.Vector4 | Sequence[float | str]
def selectChannels(node: hou.OpNode, parms: Iterable[str], setScope: bool = True, namespace: str = '') -> None: ...
def clearChannels(node: hou.OpNode) -> None: ...
def setNodeparmsFromDict(node: hou.OpNode, parms: SupportsKeysAndGetItem[str, _ParmValue] | _apex.Dict, node_parm_names: Container[str], parmgroup: Container[str] | None = None, key: bool = False, namespace: str = '', frame: float | None = None) -> None:
    """applies parm values stored out in the dictionary format from the attribFromParms node style to a given hou.Node"""
def setParm(parm: hou.Parm, value: float | str, frame: float) -> None: ...
def setKey(parm: hou.Parm, value: float, frame: float) -> None: ...
def nodeToParms(parms_dict: _ParmsDictT, namespace: str = '', nodeparmfilter: str = '', node: hou.OpNode | None = None, parm_verb: hou.SopVerb | None = None, frame: float | None = None) -> _ParmsDictT: ...
