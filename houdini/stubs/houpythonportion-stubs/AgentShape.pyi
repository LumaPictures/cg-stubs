import hou
from collections.abc import Sequence

def blendshapeInputShapeNames(self: hou.AgentShape) -> tuple[str, ...] | list[str]:
    """
blendshapeInputShapeNames(self) -> tuple of str

    If this shape is a base shape used with the blendshape deformer,
    returns a list of the input shape names.

"""
def blendshapeInputChannels(self: hou.AgentShape) -> tuple[str, ...] | list[str]:
    """
blendshapeInputChannels(self) -> tuple of str

    If this shape is a base shape used with the blendshape deformer,
    returns a list of the input channel names. This list matches the
    order of hou.AgentShape.blendshapeInputShapeNames.

"""
def inBetweenShapeNames(self: hou.AgentShape) -> tuple[str, ...] | list[str]:
    """
inBetweenShapeNames(self) -> tuple of str

    If this shape is used as a blendshape input, returns a list of its
    in-between shape names.

"""
def inBetweenShapeWeights(self: hou.AgentShape) -> tuple[float, ...] | list[float]:
    """
inBetweenShapeWeights(self) -> tuple of float

    If this shape is used as a blendshape input, returns a list of the
    weight that each in-between shape is applied at. This list matches
    the order of hou.AgentShape.inBetweenShapeNames.

"""
def addBlendshapeInputs(self: hou.AgentShape, shapes: Sequence[hou.AgentShape], channel_names: Sequence[str]) -> None:
    """
addBlendshapeInputs(self, shapes, channel_names)

    Adds blendshape inputs to the shape. This sets up the required
    detail attributes (blendshape_shapenames and blendshape_channels)
    for the base shape's geometry. Raises hou.GeometryPermissionError if
    the shape is not modifiable.


    shapes
        A hou.AgentShape sequence to add as blendshape inputs.
        hou.AgentShapeLibrary.addShape should be called separately to
        add these shapes to the shape library.

    channel_names
        A str sequence specifying the channel name to use for each
        shape. Raises hou.InvalidSize if the length does not match the
        shapes list.

"""
def addInBetweenShapes(self: hou.AgentShape, shapes: Sequence[hou.AgentShape], weights: Sequence[float]) -> None:
    """
addInBetweenShapes(self, shapes, weights)

    Adds in-between shapes to a blendshape input. This sets up the
    required detail attributes (blendshape_shapenames and
    blendshape_inbetweenweights) on the primary shape's geometry. Raises
    hou.GeometryPermissionError if the shape is not modifiable.


    shapes
        A hou.AgentShape sequence to add as in-between shapes.
        hou.AgentShapeLibrary.addShape should be called separately to
        add these shapes to the shape library.

    weights
        A float sequence specifying the weight that each in-between
        shape is applied at. Raises hou.InvalidSize if the length does
        not match the shapes list.

"""
def setBlendshapeDeformerParms(self: hou.AgentShape, attribs: str = 'P N', point_id_attrib: str = 'id', prim_id_attrib: str = 'id') -> None:
    '''
setBlendshapeDeformerParms(self, attribs="P N", point_id_attrib="id",
prim_id_attrib="id")

    Adds attributes to the shape\'s geometry to specify parameters for
    the blendshapes deformer. This creates the following detail
    attributes: blendshape_attribs, blendshape_ptidattr, and
    blendshape_primidattr. Raises hou.GeometryPermissionError if the
    shape is not modifiable.


    attribs
        Specifies a list or pattern of attributes to be blended by the
        deformer.

    point_id_attrib
        Specifies the name of a point attribute used to match up points
        between the different blendshape inputs.

    prim_id_attrib
        Specifies the name of a primitive attribute used to match up
        points between the different blendshape inputs.

'''
