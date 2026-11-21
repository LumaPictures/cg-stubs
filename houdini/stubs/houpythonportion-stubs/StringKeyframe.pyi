# Houdini stubs generated from Houdini 22.0.466

import hou
from typing import TypedDict

class _StringKeyframeJSON(TypedDict, total=False):
    frame: float
    time: float
    expression: str
    language: str

def asJSON(self: hou.StringKeyframe, brief: bool = False, save_keys_in_frames: bool = False) -> _StringKeyframeJSON:
    """
asJSON(self, brief=False, save_keys_in_frames=False) -> dict

    Returns a JSON dictionary that describes the keyframe. The
    dictionary includes the keyframe time and the expression if it has
    been set. If the save_keys_in_frames parameter is set to True, a
    frame number is used instead of a time.

    See also the fromJSON method.

"""
def fromJSON(self: hou.StringKeyframe, keyframe_dict: _StringKeyframeJSON) -> None:
    """
fromJSON(self, keyframe_dict)

    Sets the keyframe time and expression using the key/value pairs from
    a JSON dictionary.

    See also the asJSON method.

"""
