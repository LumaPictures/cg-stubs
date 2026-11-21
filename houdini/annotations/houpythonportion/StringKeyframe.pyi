from typing import TypedDict

import hou

class _StringKeyframeJSON(TypedDict, total=False):
    frame: float
    time: float
    expression: str
    language: str

def asJSON(self: hou.StringKeyframe, brief: bool = ..., save_keys_in_frames: bool = ...) -> _StringKeyframeJSON: ...
def fromJSON(self: hou.StringKeyframe, keyframe_dict: _StringKeyframeJSON) -> None: ...
