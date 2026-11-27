import datetime
from collections.abc import Generator, Iterable, Mapping, Sequence
from typing import Literal, TypeAlias, TypeVar

from hrecipes import rtypes

import hou

_OpNodeT = TypeVar("_OpNodeT", bound=hou.OpNode)

# hrecipes.rtypes.ParmOptionType and ParmTemplateOptionType, spelled out.
_ParmOption: TypeAlias = bool | list[hou.ParmTuple] | list[str] | set[str] | tuple[str, ...]
_ParmTemplateOption: TypeAlias = Literal["none", "spare_only", "all"]
# Values setParms accepts: a parm or parm tuple value, or for a multiparm, one dict of
# instance parm values (names with '#' placeholders) per instance.
_ParmValue: TypeAlias = (
    hou.ParmArgType | hou.ParmTupleArgType | Sequence[Mapping[str, "_ParmValue"]]
)
_ItemOption: TypeAlias = _ParmOption | _ParmTemplateOption | rtypes.ParsingCallback | None

def addSpareParmTuple(
    self: hou.OpNode,
    parm_template: hou.ParmTemplate,
    in_folder: Sequence[str] = ...,
    create_missing_folders: bool = ...,
) -> hou.ParmTuple: ...
def replaceSpareParmTuple(
    self: hou.OpNode, parm_tuple_name: str, parm_template: hou.ParmTemplate
) -> hou.ParmTuple: ...
def removeSpareParmTuple(self: hou.OpNode, parm_tuple: hou.ParmTuple) -> None: ...
def addControlParmFolder(
    self: hou.OpNode, folder_name: str | None = ..., parm_name: str | None = ...
) -> None: ...
def addSpareParmFolder(
    self: hou.OpNode,
    folder_name: str,
    in_folder: Sequence[str] = ...,
    parm_name: str | None = ...,
    create_missing_folders: bool = ...,
) -> None: ...
def removeSpareParmFolder(self: hou.OpNode, folder: Sequence[str]) -> None: ...
def setParms(self: hou.OpNode, parm_dict: Mapping[str, _ParmValue]) -> None: ...
def setParmsPending(
    self: hou.OpNode, parm_dict: Mapping[str, hou.ParmArgType | hou.ParmTupleArgType]
) -> None: ...
def setParmExpressions(
    self: hou.OpNode,
    parm_dict: Mapping[str, str | Sequence[str]],
    language: hou.EnumValue[hou.exprLanguage] | None = ...,
    replace_expressions: bool = ...,
) -> None: ...
def allParms(self: hou.OpNode) -> Generator[hou.Parm, None, None]: ...
def creationTime(self: hou.OpNode) -> datetime.datetime: ...
def modificationTime(self: hou.OpNode) -> datetime.datetime: ...
def saveChildrenToFile(
    self: hou.OpNode,
    nodes: Iterable[hou.NetworkMovableItem],
    network_boxes: Iterable[hou.NetworkMovableItem],
    file_name: str,
) -> None: ...
def loadChildrenFromFile(
    self: hou.OpNode, file_name: str, ignore_load_warnings: bool = ...
) -> None: ...
def saveParmClip(
    self: hou.OpNode,
    file_name: str,
    start: float | None = ...,
    end: float | None = ...,
    sample_rate: float = ...,
    scoped_only: bool = ...,
) -> None: ...
def loadParmClip(
    self: hou.OpNode, file_name: str, sample_rate: float = ..., start: float | None = ...
) -> None: ...
def setParmClipData(
    self: hou.OpNode,
    data: bytes,
    binary: bool = ...,
    blosc_compressed: bool = ...,
    sample_rate: float = ...,
    start: float | None = ...,
) -> None: ...
def parmClipData(
    self: hou.OpNode,
    start: float | None = ...,
    end: float | None = ...,
    binary: bool = ...,
    use_blosc_compression: bool = ...,
    sample_rate: float = ...,
    scoped_only: bool = ...,
) -> bytes: ...
def copyTo(self: _OpNodeT, destination_node: hou.OpNode) -> _OpNodeT: ...
def asData(self: hou.OpNode, **item_opts: _ItemOption) -> rtypes.NetworkItemData: ...
def setFromData(
    self: hou.OpNode, data: rtypes.NetworkItemData, **item_set_opts: bool
) -> dict[str, hou.NetworkMovableItem]: ...
def parmsAsData(
    self: hou.OpNode, **parms_opts: _ParmOption | rtypes.ParsingCallback | None
) -> rtypes.ParmDataDict: ...
def setParmsFromData(self: hou.OpNode, data: rtypes.ParmDataDict) -> None: ...
def childrenAsData(
    self: hou.OpNode, **items_opts: _ItemOption | hou.Vector2
) -> rtypes.NetworkItemDataDict | None: ...
def setChildrenFromData(
    self: hou.OpNode, data: rtypes.NetworkItemDataDict, **children_set_opts: bool | hou.Vector2
) -> dict[str, hou.NetworkMovableItem]: ...
def editablesAsData(
    self: hou.OpNode, **items_opts: _ItemOption
) -> rtypes.NetworkItemDataDict | None: ...
def setEditablesFromData(
    self: hou.OpNode,
    data: rtypes.NetworkItemDataDict,
    **editables_set_opts: bool | hou.Vector2,
) -> dict[str, hou.NetworkMovableItem]: ...
def createDecorationItemsFromData(
    self: hou.OpNode,
    data: rtypes.NetworkItemDataDict,
    target_name_in_data: str,
    **descendentitems_set_opts: bool | hou.Vector2,
) -> dict[str, hou.NetworkMovableItem]: ...
def parmTemplatesAsData(
    self: hou.OpNode,
    name: str = ...,
    children: bool = ...,
    **parmtemplates_opts: bool | rtypes.ParsingCallback | None,
) -> rtypes.ParmTemplateDataDict | None: ...
def parmTemplateChildrenAsData(
    self: hou.OpNode,
    name: str,
    **parmtemplates_opts: bool | rtypes.ParsingCallback | None,
) -> rtypes.ParmTemplateDataDict | None: ...
def appendParmTemplatesFromData(
    self: hou.OpNode, data: rtypes.ParmTemplateDataDict, rename_conflicts: bool = ...
) -> dict[str, hou.ParmTuple]: ...
def replaceParmTemplatesFromData(
    self: hou.OpNode, data: rtypes.ParmTemplateDataDict
) -> dict[str, hou.ParmTuple]: ...
def insertParmTemplatesBeforeFromData(
    self: hou.OpNode,
    data: rtypes.ParmTemplateDataDict,
    parm_name: str,
    rename_conflicts: bool = ...,
) -> dict[str, hou.ParmTuple]: ...
def insertParmTemplatesAfterFromData(
    self: hou.OpNode,
    data: rtypes.ParmTemplateDataDict,
    parm_name: str,
    rename_conflicts: bool = ...,
) -> dict[str, hou.ParmTuple]: ...
def appendParmTemplatesToFolderFromData(
    self: hou.OpNode,
    data: rtypes.ParmTemplateDataDict,
    parm_name: str,
    rename_conflicts: bool = ...,
) -> dict[str, hou.ParmTuple]: ...
def prependParmTemplatesToFolderFromData(
    self: hou.OpNode,
    data: rtypes.ParmTemplateDataDict,
    parm_name: str,
    rename_conflicts: bool = ...,
) -> dict[str, hou.ParmTuple]: ...
def inputsAsData(
    self: hou.OpNode | hou.OpIndirectInput | hou.NetworkDot,
    ignore_network_dots: bool = ...,
    ignore_subnet_indirect_inputs: bool = ...,
    use_names: bool = ...,
) -> rtypes.NetworkItemInputDataList: ...
def outputsAsData(
    self: hou.OpNode | hou.OpIndirectInput | hou.NetworkDot,
    ignore_network_dots: bool = ...,
    use_names: bool = ...,
) -> rtypes.NetworkItemOutputDataList: ...
def setInputsFromData(
    self: hou.OpNode | hou.OpIndirectInput | hou.NetworkDot,
    data: rtypes.NetworkItemInputDataList,
) -> None: ...
def setOutputsFromData(
    self: hou.OpNode | hou.OpIndirectInput | hou.NetworkDot,
    data: rtypes.NetworkItemOutputDataList,
) -> None: ...
def inputsWithIndices(
    self: hou.Node | hou.NetworkDot,
    ignore_network_dots: bool = ...,
    ignore_subnet_indirect_inputs: bool = ...,
    use_names: bool = ...,
) -> list[tuple[hou.NetworkMovableItem, int | str, int | str]]: ...
def outputsWithIndices(
    self: hou.Node | hou.NetworkDot,
    ignore_network_dots: bool = ...,
    use_names: bool = ...,
) -> list[tuple[hou.NetworkMovableItem, int | str, int | str]]: ...
