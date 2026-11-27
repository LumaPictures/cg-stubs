import hou
from typing import TypeGuard

def validateMotionClipSimple(geo: hou.Geometry | None) -> TypeGuard[hou.Geometry]:
    """ A method to quickly determine if a geometry meets some of the
        necessary properties of a MotionClip. Specifically, this checks that
        there is at least one primitive, that the first primitive is a packed
        geometry, and that the 'time' primitive attribute exists.
        
        For a method which is more rigorous and validates that the MotionClip
        can be evaluated, use validateMotionClip. """
def validateMotionClip(geo: hou.Geometry | None) -> TypeGuard[hou.Geometry]:
    """ Validates that a geometry is a MotionClip by passing it through a
        MotionClip Unpack verb"""
def getRestPose(geo: hou.Geometry | None) -> hou.Geometry | None: ...
