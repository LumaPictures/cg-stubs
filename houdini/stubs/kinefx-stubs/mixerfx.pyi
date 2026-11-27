import hou
from collections.abc import Iterable, Mapping, MutableMapping
from typing import NotRequired, TypedDict, Unpack

class _FXDict(TypedDict):
    filename: str
    fxtype: str
    label: str
    icon: str

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

def registerMixerNode(d: MutableMapping[str, _FXDict], n: hou.OpNode | None) -> None:
    """ Register a list of patterns and return a string of files separated by ;"""
def FXDicttoStr(d: Mapping[str, _FXDict]) -> str: ...
def registerFXFilesStr(files: Iterable[str]) -> str:
    """ Register a list of patterns and return a string of files separated by ;"""
def registerMixerNodeStr(n: hou.OpNode | None) -> str: ...
def registerFXFiles(d: MutableMapping[str, _FXDict], files: Iterable[str]) -> None:
    """ Register a list of patterns.  """
def registerFX(d: MutableMapping[str, _FXDict], file_pattern: str) -> None:
    """ Register one or more FX using a file pattern for .py files.
        @d is a dict() to write to. An fx type can be overloaded.
    """
def createFX(**kwargs: Unpack[_CreateFXKwargs]) -> str:
    """ Create a Motion Mixer FX for the given fxtype.
        @mixer_node the parent mixer node.
        @fxsopnet the effects sopnet holding all the clip and track fx.
        @fxname the new node name for the fx.
        @fxtype the fxtype use to load a different cpio file and initFx.
    """
def exportFX(**kwargs: Unpack[_ExportFXKwargs]) -> None: ...
def connectMixerFxAnimatedSops(geo: hou.Geometry, key: str, sop_path: str) -> None:
    """ 
        @geo is an APEX scene geometry to read and write to.
        @key is unique string for the hook to avoid overwritting entries setup
         from elsewhere.
        @sop_path is the node path to pull from. This usually points to a
         MotionMixer Fetch node. We assume that it contains the same MixerAnim.skel
         that the APEX scene contains.
    """
