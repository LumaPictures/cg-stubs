import hou
from typing import TypedDict

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

def asJSON(self: hou.Keyframe, brief: bool = False, save_keys_in_frames: bool = False) -> _KeyframeJSON:
    """
asJSON(self, brief=False, save_keys_in_frames=False) -> dict

    Returns a JSON dictionary that represents the keyframe. The
    dictionary includes the frame time, value/expression, and the slope
    and acceleration parameters. If the brief parameter is set to True a
    smaller set of key/value pairs are included in the dictionary to
    reduce space usage. If the save_keys_in_frames parameter is True the
    dictionary uses a frame number instead of a time value.

    See also the fromJSON method.

"""
def fromJSON(self: hou.Keyframe, keyframe_dict: _KeyframeJSON) -> None:
    """
fromJSON(self, keyframe_dict)

    Sets the keyframe time, value and parameters using the key/value
    pairs from a JSON dictionary.

    See also the asJSON method.

"""
