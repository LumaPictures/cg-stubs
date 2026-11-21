from typing import ClassVar

import hou
from pdgjob import pdgcmd, pdgjson

class RopCooker:
    rop_map: ClassVar[dict[str, str]]
    post_advance_types: ClassVar[list[str]]
    mantra_parms: ClassVar[list[str]]
    standard_parms: ClassVar[list[str]]
    workItem: pdgjson.NativeWorkItem | None
    server: str | None
    outputs: dict[int, list[str]]
    outputLogger: pdgcmd.StdOutReporter | None
    hasCallback: bool
    preFrame: hou.EnumValue[hou.ropRenderEventType] | None
    postFrame: hou.EnumValue[hou.ropRenderEventType] | None
    mantraFilters: set[str]
    unlockNode: bool
    cookInputs: bool
    targetNode: hou.OpNode
    editNode: hou.OpNode
    renderNode: hou.OpNode
    frameRange: tuple[float, float, float]
    noRange: bool
    singleTask: bool
    customRange: bool
    frameList: list[float]
    cookOrder: hou.EnumValue[hou.renderMethod]
    executeParm: str
    tileIndex: int
    fileTags: list[str]
    outputParms: list[str] | None
    reloadParm: str | None
    customOutputParms: bool
    logParsing: int
    logFormat: str
    usePerfMon: bool
    perfMonFile: str | None
    debugFile: str | None
    reportDebug: bool
    batch: bool
    dist_sim: bool
    batchStart: int
    batch_poll: bool
    @classmethod
    def create(cls, work_item: pdgjson.NativeWorkItem | None, server: str | None = ...) -> "RopCooker | None": ...
    def __init__(self, work_item: pdgjson.NativeWorkItem, server: str | None = ...) -> None: ...
    def cook(self, service_mode: bool) -> tuple[bool, list[tuple[str, str]]]: ...
    def saveDebugFile(self) -> None: ...
    def cleanup(self) -> None: ...

class BakeTextureCooker(RopCooker):
    def __init__(self, work_item: pdgjson.NativeWorkItem, server: str | None = ...) -> None: ...

class GamesBakerCooker(RopCooker):
    def __init__(self, work_item: pdgjson.NativeWorkItem, server: str | None = ...) -> None: ...

def cook(work_item: pdgjson.NativeWorkItem) -> bool: ...
def main() -> None: ...
