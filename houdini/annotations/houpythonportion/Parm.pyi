from typing import TypeAlias

from hrecipes import rtypes

import hou

# hrecipes._ParmOption, spelled out.
_ParmOption: TypeAlias = bool | list[hou.ParmTuple] | list[str] | set[str] | tuple[str, ...]

def set(
    self: hou.Parm,
    value: int
    | float
    | str
    | dict[str, str]
    | hou.Geometry
    | hou.ImageLayer
    | hou.NanoVDB
    | hou.DetachedAttrib
    | hou.CopCable
    | hou.Ramp
    | hou.Parm
    | None,
    language: hou.EnumValue[hou.exprLanguage] | None = ...,
    follow_parm_reference: bool | None = ...,
) -> None: ...
def setPending(
    self: hou.Parm,
    value: int
    | float
    | str
    | dict[str, str]
    | hou.Geometry
    | hou.ImageLayer
    | hou.NanoVDB
    | hou.DetachedAttrib
    | hou.CopCable
    | hou.Ramp
    | None,
) -> None: ...
def saveClip(
    self: hou.Parm,
    file_name: str,
    start: float | None = ...,
    end: float | None = ...,
    sample_rate: float = ...,
) -> None: ...
def loadClip(
    self: hou.Parm, file_name: str, sample_rate: float = ..., start: float | None = ...
) -> None: ...
def setClipData(
    self: hou.Parm,
    data: bytes,
    binary: bool = ...,
    blosc_compressed: bool = ...,
    sample_rate: float = ...,
    start: float | None = ...,
) -> None: ...
def clipData(
    self: hou.Parm,
    start: float | None = ...,
    end: float | None = ...,
    binary: bool = ...,
    use_blosc_compression: bool = ...,
    sample_rate: float = ...,
) -> bytes: ...
def valueAsData(
    self: hou.Parm | hou.ParmTuple, **parm_value_opts: bool
) -> rtypes.ParmValueData: ...
def setValueFromData(self: hou.Parm | hou.ParmTuple, data: rtypes.ParmValueData) -> None: ...
def asData(self: hou.Parm | hou.ParmTuple, **parm_opts: bool) -> rtypes.ParmUnionData: ...
def setFromData(self: hou.Parm | hou.ParmTuple, data: rtypes.ParmUnionData) -> None: ...
def childrenAsData(
    self: hou.Parm | hou.ParmTuple,
    **parms_opts: _ParmOption | rtypes.ParsingCallback | None,
) -> rtypes.ParmDataDict: ...
def multiParmInstancesAsData(
    self: hou.Parm | hou.ParmTuple,
    start_index: int = ...,
    end_index: int = ...,
    **multiparm_instance_opts: bool,
) -> rtypes.MultiParmInstanceDataList | None: ...
def setMultiParmInstancesFromData(
    self: hou.Parm | hou.ParmTuple, data: rtypes.MultiParmInstanceDataList, index: int = ...
) -> None: ...
def insertMultiParmInstancesFromData(
    self: hou.Parm | hou.ParmTuple, data: rtypes.MultiParmInstanceDataList, index: int = ...
) -> None: ...
def appendMultiParmInstancesFromData(
    self: hou.Parm | hou.ParmTuple, data: rtypes.MultiParmInstanceDataList
) -> None: ...
def rampPointsAsData(
    self: hou.Parm | hou.ParmTuple, **ramppoints_opts: bool
) -> rtypes.RampPointDataList | None: ...
def setRampPointsFromData(
    self: hou.Parm | hou.ParmTuple, data: rtypes.RampPointDataList
) -> None: ...
def templateAsData(
    self: hou.Parm | hou.ParmTuple,
    children: bool = ...,
    **parmtemplate_opts: bool | rtypes.ParsingCallback | None,
) -> rtypes.ParmTemplateDataDict | None: ...
def templateChildrenAsData(
    self: hou.Parm | hou.ParmTuple,
    **parmtemplate_opts: bool | rtypes.ParsingCallback | None,
) -> rtypes.ParmTemplateDataDict | None: ...
def insertTemplatesFromData(
    self: hou.Parm | hou.ParmTuple,
    data: rtypes.ParmTemplateDataDict,
    operation: str = ...,
    rename_conflicts: bool = ...,
) -> dict[str, hou.ParmTuple]: ...
