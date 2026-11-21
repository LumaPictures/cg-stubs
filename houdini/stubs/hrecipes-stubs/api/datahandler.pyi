from collections.abc import Callable as Callable
from typing import Any, Generic, Iterable, Sequence

from typing import TypeVar
from collections.abc import Mapping
from typing import TypeVar
import hou
_ObjT = TypeVar('_ObjT', bound=hou.NetworkMovableItem | hou.ParmTuple | hou.ParmTemplate)
_DataT = TypeVar('_DataT', bound=Mapping[str, object])
class DataHandler(Generic[_ObjT, _DataT]):
    """
    A class for storing basic functionalities to get and set data from a Houdini parameter or network item object.
    """
    keys: list[str]
    metakeys: list[str]
    is_at_default_chooser: dict[str, Callable[[_ObjT, Any, dict[str, Any]], object]]
    getter_method_chooser: dict[str, Callable[[_ObjT, dict[str, Any]], Any]]
    setter_method_chooser: dict[str, Callable[[_ObjT, Any, dict[str, Any]], object]]
    enable_chooser: dict[str, Callable[[dict[str, Any]], object]]
    def __init__(self) -> None: ...
    def initKeysForData(self, keys: Iterable[str]) -> None: ...
    def initMetakeysForData(self, metakeys: Iterable[str]) -> None: ...
    def getData(self, hou_obj: _ObjT, **opts: Any) -> _DataT:
        """
        Generic function to build the data for a Houdini object, using keys given by 'self.keys' and 'self.metakeys'
        Options are user provided to filter what is recorded in the data.
        """
    def setData(self, hou_obj: _ObjT, data: _DataT, skip_keys: Sequence[str] | None = None, **opts: Any) -> None:
        """
        Generic function to set values for a Houdini object, using the keys given in the data.
        """
