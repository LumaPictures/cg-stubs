from typing import NotRequired, TypedDict

import hou

from poselib import chopdata

JSON: str
ASCII_CLIP: str
BCLIP: str
BCLIP_SC: str
CLIP_TYPES: set[str]
BCLIP_TYPES: set[str]
CLIP: str
POSE: str
FRAME_COUNT_UNKNOWN: int
CAPTURED_PARMS_UNKNOWN: str

def getClipTypeFromPath(path: str) -> str | None: ...

# hou.Keyframe.asJSON() or hou.StringKeyframe.asJSON(), with `strkeyframe` for a string keyframe.
class _PoseKeyframeJson(TypedDict, total=False):
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
    strkeyframe: int

class _PoseFrameJson(TypedDict):
    key: str | None
    frame: float | None
    chop: int
    value: NotRequired[float | str | None]
    complex_value: NotRequired[_PoseKeyframeJson]

class _PoseDataJson(TypedDict):
    poses: list[_PoseFrameJson]
    chop_data: dict[str, list[bytes]] | None
    frames: int
    captured_parameters: list[str] | list[str | None] | str

class PoseFrame:
    key: str | None
    value: hou.Keyframe | hou.StringKeyframe | float | str | None
    frame: float | None
    chop: bool
    def __init__(
        self,
        key: str | None = ...,
        value: hou.Keyframe | hou.StringKeyframe | float | str | None = ...,
        frame: float | None = ...,
        chop: bool = ...,
    ) -> None: ...
    def parmDict(self) -> dict[str | None, hou.Keyframe | hou.StringKeyframe | float | str | None]: ...
    def jsonDict(self) -> _PoseFrameJson: ...
    def setJSONDict(self, json_dict: _PoseFrameJson) -> None: ...

class PoseData:
    keyframes: list[PoseFrame]
    chopData: chopdata.ChopData | None
    clipLength: str | None
    clipRate: float | str | None
    clipData: bytes | str | None
    frameCount: int
    capturedParms: list[str] | list[str | None] | str
    def __init__(
        self,
        animation_type: str,
        animation_data: list[PoseFrame] | bytes | str | None,
        chop_data: chopdata.ChopData | None = ...,
        frame_count: int | None = ...,
        captured_parms: list[str] | str | None = ...,
    ) -> None: ...
    def serialize(self) -> _PoseDataJson | bytes | str | None: ...
    @classmethod
    def bclipSerialize(cls, raw_data: bytes | str) -> str: ...
    @classmethod
    def bclipDeserialize(cls, serialized_data: str) -> bytes: ...
    def convertToClipData(self, clip_type: str) -> bytes | str | None: ...
    def animationDataType(self) -> str: ...
    def singleFrame(self) -> bool: ...
    def canBlend(self) -> bool: ...
