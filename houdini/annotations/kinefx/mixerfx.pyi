from collections.abc import Iterable, Mapping, MutableMapping
from typing import NotRequired, TypedDict, Unpack

import hou

# A registered effect: `filename` is set here, the rest by the effect module's registerFX().
class _FXDict(TypedDict):
    filename: str
    fxtype: str
    label: str
    icon: str

# What SOP_MotionMixer passes createFX(); createFX adds the NotRequired keys before passing them
# on to the effect module's initFX().
class _CreateFXKwargs(TypedDict):
    mixer_node: hou.SopNode
    fxsopnet: hou.OpNode
    fxtype: str
    fxname: str
    ids: list[int] | None
    filename: str
    subnet: NotRequired[hou.OpNode]
    node: NotRequired[hou.OpNode | None]
    mixerfx_path: NotRequired[str]
    py_file: NotRequired[str]
    cpio_file: NotRequired[str]

class _ExportFXKwargs(TypedDict):
    fx_name: str
    fx_net: hou.OpNode | None
    py_file: NotRequired[str]

def registerMixerNode(d: MutableMapping[str, _FXDict], n: hou.OpNode | None) -> None: ...
def FXDicttoStr(d: Mapping[str, _FXDict]) -> str: ...
def registerFXFilesStr(files: Iterable[str]) -> str: ...
def registerMixerNodeStr(n: hou.OpNode | None) -> str: ...
def registerFXFiles(d: MutableMapping[str, _FXDict], files: Iterable[str]) -> None: ...
def registerFX(d: MutableMapping[str, _FXDict], file_pattern: str) -> None: ...
def createFX(**kwargs: Unpack[_CreateFXKwargs]) -> str: ...
def exportFX(**kwargs: Unpack[_ExportFXKwargs]) -> None: ...
def connectMixerFxAnimatedSops(geo: hou.Geometry, key: str, sop_path: str) -> None: ...
