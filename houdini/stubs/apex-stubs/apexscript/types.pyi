from _typeshed import Incomplete
from typing import NamedTuple

class NodeTypeComponents(NamedTuple):
    namespace: Incomplete
    name: Incomplete
    value_types: Incomplete
    version: Incomplete

def nodeTypeComponents(name: str) -> NodeTypeComponents:
    """Separates a node type name into its components.

    The components consist of the node type's namespace, name, value_types and
    version. They are returned as a NodeTypeComponents tuple, allowing the
    individual components to be accessed by name.

    For example, the node type name ns::name<Int,Float>::2.0' is returned as
    NodeTypeComponents('ns', 'name', ['Int', 'Float'], '2.0')
    """

BOOL: str
INT: str
FLOAT: str
STRING: str
VECTOR2: str
VECTOR3: str
VECTOR4: str
MATRIX3: str
MATRIX4: str
GEOMETRY: str
DICT: str
GRAPH: str
NODE: str
PORT: str
VOID: str
ARRAY_SUFFIX: str
BOOL_ARRAY: Incomplete
INT_ARRAY: Incomplete
FLOAT_ARRAY: Incomplete
STRING_ARRAY: Incomplete
VECTOR2_ARRAY: Incomplete
VECTOR3_ARRAY: Incomplete
VECTOR4_ARRAY: Incomplete
MATRIX3_ARRAY: Incomplete
MATRIX4_ARRAY: Incomplete
GEOMETRY_ARRAY: Incomplete
DICT_ARRAY: Incomplete
NODE_ARRAY: Incomplete
PORT_ARRAY: Incomplete
BASIC_TYPES: Incomplete
VECTOR_TYPES: Incomplete
MATRIX_TYPES: Incomplete
GRAPH_TYPES: Incomplete
SCALAR_TYPES: Incomplete
ARRAY_TYPES: Incomplete
start_idx: Incomplete
end_idx: Incomplete
value_type: Incomplete
APEX_TYPES = SCALAR_TYPES | ARRAY_TYPES
GENERIC_TYPES: Incomplete
TYPE_CONVERSIONS: Incomplete
value_types: Incomplete
src_type: Incomplete
dst_type: Incomplete

def construct(apex_type: str, *args, **kwargs):
    """Constructs a python object to hold a value of the requested apex type.

    This function is used to construct, copy, and/or convert its arguments into
    the requested apex type. When no arguments are provided, the type is
    default constructed into an appropriate python object representing the type.
    If passed a value of the same type, a copy of the type is made. When passed
    a value of another type, a conversion occurs.

    The conversions are more permissive than that which is currently
    represented by apex operations. For example, you may convert from an
    apex.IntArray() to an apex.FloatArray() (which is not currently
    implemented in apex). This behavior provides a number of conveniences for
    callers, and perhaps apex will support these additional conversions in the
    future, but for now the ability to construct a requested value from the
    arguments should not be used to do any type checking within apexscript.
    """
def typeFromValue(apex_value) -> str | None:
    """Returns the name of the apex type represented by the python object.

    The following categories of python objects have apex equivalents:
    Builtin python types: bool, int, float, str, dict
    Houdini HOM types: hou.Vector[234], hou.Matrix[34], hou.Geometry
    Apex Array Types:
        apex.[Bool,Int,Float,String]Array
        apex.[Vector[234]]Array
        apex.[Matrix[34]]
        apex.GeometryArray
        apex.DictArray

    Python tuples are shorthand for vector and matrix types.
    Python lists (of a single element type) are shorthand for apex arrays.
    """
