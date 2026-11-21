from collections.abc import Callable, Iterable, Sequence

import hou
from houtypes import ParmCallbackKwargs
from pxr import Usd

AOV_NAME: str
AOV_CHANNELPREFIX: str
AOV_FORMAT: str
AOV_FILTER: str

class _FrameRange:
    fstart: float
    fend: float
    finc: float
    frames: list[float]
    nframes: int
    animated: list[float]
    def __init__(self, fstart: float, fend: float, finc: float) -> None: ...

def update_rayimport_signature(kwargs: ParmCallbackKwargs) -> None: ...
def update_rayimport_menu() -> list[str]: ...
def renderVars(node: hou.LopNode, stage: Usd.Stage, fstart: float, fend: float, finc: float) -> None: ...
def renderProducts(node: hou.LopNode, stage: Usd.Stage, fstart: float, fend: float, finc: float) -> None: ...
def huskImageMetadata(
    node: hou.LopNode,
    stage: Usd.Stage,
    primlist: Iterable[Usd.Prim],
    fstart: float,
    fend: float,
    finc: float,
) -> None: ...
def renderProperties(
    node: hou.LopNode,
    stage: Usd.Stage,
    fstart: float,
    fend: float,
    finc: float,
    existingvars: Sequence[Usd.Prim],
) -> None: ...
def toonShading(node: hou.LopNode, stage: Usd.Stage, fstart: float, fend: float, finc: float) -> None: ...
def imagefilter(node: hou.LopNode, stage: Usd.Stage, fstart: float, fend: float, finc: float) -> None: ...

slapcomp: Callable[[hou.LopNode, Usd.Stage, float, float, float], None]

def precompile_info_dialog() -> None: ...
