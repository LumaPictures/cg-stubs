import hou
import numpy as np
from collections.abc import Sequence
from kinefx.utils import matrix4ToMatrix3 as matrix4ToMatrix3, mirrorTransform as mirrorTransform
from typing import Literal, TypedDict

from typing import TypeVar
from typing import TypeVar
_T = TypeVar('_T')
class _SymmetryKwargs(TypedDict, total=False):
    mirroraxis: int | Literal['X', 'Y', 'Z']
    max_dist: float
    max_points: int
    threshold: float

parms: dict[str, int | str]
edgetransport_forward: hou.SopVerb
edgetransport_backward: hou.SopVerb

def levenshtein(seq1: Sequence[_T], seq2: Sequence[_T]) -> np.float64:
    """
    Implementation of Levenshtein Distance: minimum number of single-character edits(insertions, deletions or substitutions)
    required to change one word into the other.

    :param seq1: source word
    :type seq1: str
    :param seq2: target word
    :type seq2: str
    """
def getSymmetry(geo: hou.Geometry, kwargs: _SymmetryKwargs = ...) -> list[int]:
    """
    Get the symmetrical point for all the points in the passed in geometry using a combination of position threshold and
    name similarity.
    The position component is computed by mirroring the position of the current point and finding the closest point to it.
    The name component is computed by finding the closest similarity between the name of the current point and its potential mirror.
    This is done using the **levenshtein** method.

    :param geo: geometry to compute the point symmetry for
    :type geo: hou.Geometry
    :param kwargs: dictionary of arguments 
    keys consumed by method are:
    * mirroraxis: axis of symmetry expressed as int or str(0 1 2 or X Y Z)
    * max_dist: maximum distance to search for a point from the mirrored position
    * max_points: maximum amount of points to consider as canditates from the mirrored position, using the nearestPoint method
    * threshold: maximum number of single-character edits to perform on the point's name in order to get the mirrored point's name;
    number of single-character edits is returned by the **levenshtein** method
    :type kwargs: dict
    :return: point number of the found mirror
    :rtype: int
    .. note::
        If no mirror was found, it returns -1.
    """
def getFlipAxes(pt: hou.Point, mirrored_pt: hou.Point, mirror_axis: hou.Vector3) -> int:
    """
    Get the flip axes, computed from the passed in pt and mirrored_pt, as a bit field.
    """
def getFlipAxesFromTransforms(first_pt_rotation_mat: hou.Matrix3, second_pt_rotation_mat: hou.Matrix3) -> int:
    """
    Get the flip axes, computed from passed in pt transforms, as a bit field.
    """
