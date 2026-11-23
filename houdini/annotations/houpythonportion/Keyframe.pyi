from typing import TypedDict

import hou

class _KeyframeJSON(TypedDict, total=False):
    frame: float
    time: float
    value: float
    inValue: float
    valueUsed: int
    slope: float
    inSlope: float
    slopeUsed: int
    slopeAuto: int
    inSlopeAuto: int
    accel: float
    inAccel: float
    accelUsed: int
    accelRatio: int
    expression: str
    language: str

def asJSON(self: hou.Keyframe, brief: bool = ..., save_keys_in_frames: bool = ...) -> _KeyframeJSON: ...
def fromJSON(self: hou.Keyframe, keyframe_dict: _KeyframeJSON) -> None: ...
