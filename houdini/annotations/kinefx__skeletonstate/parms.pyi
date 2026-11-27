from typing import Literal, TypeAlias

import hou
from kinefx.rigapi import _AxisName

_Mode: TypeAlias = Literal["create", "modify"]
_ScaleInheritanceToken: TypeAlias = Literal["default", "offset", "offsetscale", "scale", "ignore"]
_JointPlacementToken: TypeAlias = Literal["view", "normal", "freehand", "surface"]

MODE_CREATE: Literal["create"]
MODE_MODIFY: Literal["modify"]
modes: list[_Mode]
# (menu token, label) pairs for the state's menu parameters.
axis_options: list[tuple[_AxisName, str]]
secondary_options_x: list[tuple[_AxisName, str]]
secondary_options_y: list[tuple[_AxisName, str]]
secondary_options_z: list[tuple[_AxisName, str]]
scale_inheritance_options: list[tuple[_ScaleInheritanceToken, str]]
scale_inheritance_modes: list[hou.EnumValue[hou.scaleInheritanceMode]]
joint_placement_options: list[tuple[_JointPlacementToken, str]]
