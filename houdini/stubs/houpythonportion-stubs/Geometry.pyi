# Houdini stubs generated from Houdini 22.0.466

import hou
from collections.abc import Sequence

def pointAttribs(self: hou.Geometry, scope: hou.EnumValue[hou.attribScope] | bool = ..., *, include_private: bool | None = None) -> tuple[hou.Attrib, ...]:
    """
pointAttribs(self, scope=hou.attribScope.Public) -> tuple of hou.Attrib

    Return a tuple of all the point attributes.


    scope
        A hou.attribScope value to specify whether the public or private
        attributes should be listed.

    Note that the point position attribute is named P and is 3 floats in
    size. Also, the point weight attribute is named Pw and is 1 float in
    size. P always exists, but Pw may not.

"""
def primAttribs(self: hou.Geometry, scope: hou.EnumValue[hou.attribScope] | bool = ..., *, include_private: bool | None = None) -> tuple[hou.Attrib, ...]:
    """
primAttribs(self, scope=hou.attribScope.Public) -> tuple of hou.Attrib

    Return a tuple of all the primitive attributes.


    scope
        A hou.attribScope value to specify whether the public or private
        attributes should be listed.

"""
def vertexAttribs(self: hou.Geometry, scope: hou.EnumValue[hou.attribScope] | bool = ..., *, include_private: bool | None = None) -> tuple[hou.Attrib, ...]:
    """
vertexAttribs(self, scope=hou.attribScope.Public) -> tuple of hou.Attrib

    Return a tuple of all the vertex attributes.


    scope
        A hou.attribScope value to specify whether the public or private
        attributes should be listed.

"""
def globalAttribs(self: hou.Geometry, scope: hou.EnumValue[hou.attribScope] | bool = ..., *, include_private: bool | None = None) -> tuple[hou.Attrib, ...]:
    """
globalAttribs(self, scope=hou.attribScope.Public) -> tuple of hou.Attrib

    Return a tuple of all the global (a.k.a. detail) attributes.


    scope
        A hou.attribScope value to specify whether the public or private
        attributes should be listed.

"""
def intrinsicValueDict(self: hou.Geometry) -> dict[str, hou.AttribReturnType]:
    """
intrinsicValueDict(self) -> dict of str to value

    Returns a dictionary mapping intrinsic names to their values.

"""
def execute(self: hou.Geometry, verb: hou.SopVerb, inputs: Sequence[hou.Geometry] | None = None) -> hou.Geometry:
    """
execute(self, verb, inputs=[]) -> HOM_Geometry

    Invokes verb.execute() with myself as the first input, and returns
    the resulting geometry. This allows one to chain a series of verbs
    invocations: geo.execute(subdivide).execute(subdivide).

    The optional inputs will have the geometry itself prepended.

"""
def createPackedGeometry(self: hou.Geometry, geo: hou.Geometry, point: hou.Point | None = None) -> hou.PackedGeometry:
    """
createPackedGeometry(self, geo, point=None) -> hou.PackedPrim

    Create a geometry packed primitive that uses the given embedded
    geometry.


    geo
        hou.Geometry object to create PackedGeometry primitive with

    point

    See hou.PackedPrim for more information.

"""
def generateGroupMenu(self: hou.Geometry, group_types: hou.EnumValue[hou.geometryType] | Sequence[hou.EnumValue[hou.geometryType]] | None = None, include_selection: bool = True, include_name_attrib: bool = True, case_sensitive: bool = True, pattern: str = '*', decode_tokens: bool = False, parm: hou.Parm | None = None) -> tuple[str, ...]:
    '''
generateGroupMenu(self, group_types=None, include_selection=True,
include_name_attrib=True, case_sensitive=True, pattern="*",
decode_tokens=False, parm=None) -> tuple of str

    Generates the tokens and labels for a parameter menu listing the
    geometry\'s groups.


    group_types
        A hou.geometryType value (or sequence of hou.geometryType)
        specifying the component types to list groups for. The default
        value of None will list all point, primitive, and edge groups.

    include_selection
        Includes the current component selection in the group menu, if
        this geometry is from a SOP.

    include_name_attrib
        If a primitive name attribute exists, includes the unique names
        in the menu (for example, @name=piece2).

    case_sensitive
        Specifies whether the menu labels are produced in a case-
        sensitive order. This also controls whether the pattern is
        treated as case-sensitive.

    pattern
        Specifies a pattern of group names that should be included.

    decode_tokens
        If enabled, the menu tokens will contain the decoded group names
        rather than the actual group names. This can be useful for
        parameters that support matching against decoded group names.

    parm
        Optionally specifies the hou.Parm for which the menu is being
        generated. The parameter\'s current group string is used to
        indicate which groups have already been toggled on.

'''
