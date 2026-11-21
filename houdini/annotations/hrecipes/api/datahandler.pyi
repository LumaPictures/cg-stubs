from collections.abc import Callable, Iterable, Mapping, Sequence
from typing import Any, Generic, TypeVar

import hou

_ObjT = TypeVar("_ObjT", bound=hou.NetworkMovableItem | hou.ParmTuple | hou.ParmTemplate)
# The data dictionary built from, and applied to, an _ObjT: rtypes.ParmData, ParmTemplateData, ...
_DataT = TypeVar("_DataT", bound=Mapping[str, object])

# The *_chooser tables map each data key to its own callbacks, so the value a callback gets or
# returns has that key's type; opts is the **opts option bag the data functions are called with.
class DataHandler(Generic[_ObjT, _DataT]):
    keys: list[str]
    metakeys: list[str]
    is_at_default_chooser: dict[str, Callable[[_ObjT, Any, dict[str, Any]], object]]
    getter_method_chooser: dict[str, Callable[[_ObjT, dict[str, Any]], Any]]
    setter_method_chooser: dict[str, Callable[[_ObjT, Any, dict[str, Any]], object]]
    enable_chooser: dict[str, Callable[[dict[str, Any]], object]]
    def __init__(self) -> None: ...
    def initKeysForData(self, keys: Iterable[str]) -> None: ...
    def initMetakeysForData(self, metakeys: Iterable[str]) -> None: ...
    def getData(self, hou_obj: _ObjT, **opts: Any) -> _DataT: ...
    def setData(self, hou_obj: _ObjT, data: _DataT, skip_keys: Sequence[str] | None = ..., **opts: Any) -> None: ...
