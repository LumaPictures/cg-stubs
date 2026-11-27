from collections.abc import Sequence
from typing import Literal, TypedDict, TypeVar

import hou
import numpy as np

_T = TypeVar("_T")

# The options getSymmetry reads from its kwargs dict.
class _SymmetryKwargs(TypedDict, total=False):
    mirroraxis: int | Literal["X", "Y", "Z"]
    max_dist: float
    max_points: int
    threshold: float

parms: dict[str, int | str]
edgetransport_forward: hou.SopVerb
edgetransport_backward: hou.SopVerb

def levenshtein(seq1: Sequence[_T], seq2: Sequence[_T]) -> np.float64: ...
# The number of each point's mirror point, or -1.
def getSymmetry(geo: hou.Geometry, kwargs: _SymmetryKwargs = ...) -> list[int]: ...
# mirror_axis is the normal of the mirror plane, through the origin.
def getFlipAxes(pt: hou.Point, mirrored_pt: hou.Point, mirror_axis: hou.Vector3) -> int: ...
def getFlipAxesFromTransforms(first_pt_rotation_mat: hou.Matrix3, second_pt_rotation_mat: hou.Matrix3) -> int: ...
