"""Rules for turning SideFX's docs into the hou stub.

These are generic: they apply to every class and function the docs describe.  A signature or
type that is wrong for one member, or a member the docs lack, is fixed in annotations/hou.pyi
instead (see annotate/README.md).
"""

_TYPE_ALIAS_COMPONENTS = {
    "ATTRIB": ["int", "float", "str"],
    "PARM": ["bool", "int", "float", "str", "dict[str, str]", "'Ramp'", "'Geometry'"],
    "PARM_ARG_ONLY": ["'Parm'"],
    "PARM_RETURN_ONLY": ["'OpNode'"],
    "OPTION": [
        "bool",
        "int",
        "float",
        "str",
        "Vector2",
        "Vector3",
        "Vector4",
        "Quaternion",
        "Matrix3",
        "Matrix4",
    ],
    "OPTION_MULTI_ARG": [
        "bool",
        "int",
        "float",
        "str",
        "Vector2",
        "Vector3",
        "Vector4",
        "Quaternion",
        "Matrix3",
        "Matrix4",
        "Sequence[int]",
        "Sequence[float]",
    ],
    "OPTION_MULTI_RETURN": [
        "bool",
        "int",
        "float",
        "str",
        "Vector2",
        "Vector3",
        "Vector4",
        "Quaternion",
        "Matrix3",
        "Matrix4",
        "Tuple[int, ...]",
        "Tuple[float, ...]",
    ],
}


def get_type_aliases() -> dict[str, str]:
    attrib_arg_types = _TYPE_ALIAS_COMPONENTS["ATTRIB"] + [
        f"Sequence[{typ}]" for typ in _TYPE_ALIAS_COMPONENTS["ATTRIB"]
    ]
    attrib_return_types = _TYPE_ALIAS_COMPONENTS["ATTRIB"] + [
        f"Tuple[{typ}, ...]" for typ in _TYPE_ALIAS_COMPONENTS["ATTRIB"]
    ]

    parm_arg_types = (
        _TYPE_ALIAS_COMPONENTS["PARM"] + _TYPE_ALIAS_COMPONENTS["PARM_ARG_ONLY"]
    )
    parm_return_types = (
        _TYPE_ALIAS_COMPONENTS["PARM"] + _TYPE_ALIAS_COMPONENTS["PARM_RETURN_ONLY"]
    )

    result = {
        "AttribBasicType": " | ".join(_TYPE_ALIAS_COMPONENTS["ATTRIB"]),
        "AttribArgType": " | ".join(attrib_arg_types),
        "AttribDictArgType": " | ".join(
            f"dict[str, {typ}]" for typ in attrib_arg_types
        ),
        "AttribReturnType": " | ".join(attrib_return_types),
        "AttribDictReturnType": " | ".join(
            f"dict[str, {typ}]" for typ in attrib_return_types
        ),
        "ParmArgType": " | ".join(parm_arg_types),
        "ParmReturnType": " | ".join(parm_return_types),
        "ParmTupleArgType": " | ".join(f"Sequence[{typ}]" for typ in parm_arg_types),
        "ParmTupleReturnType": " | ".join(
            f"Tuple[{typ}, ...]" for typ in parm_return_types
        ),
        "OptionType": " | ".join(_TYPE_ALIAS_COMPONENTS["OPTION"]),
        "OptionSequenceType": " | ".join(
            f"Sequence[{typ}]" for typ in _TYPE_ALIAS_COMPONENTS["OPTION"]
        ),
        "OptionMultiArgType": " | ".join(_TYPE_ALIAS_COMPONENTS["OPTION_MULTI_ARG"]),
        "OptionMultiReturnType": " | ".join(
            _TYPE_ALIAS_COMPONENTS["OPTION_MULTI_RETURN"]
        ),
    }

    return result


TYPE_ALIASES = get_type_aliases()


ADDITIONAL_ENUM_NAMES = {
    "fbxMaterialMode": {
        "FBXShaderNodes",
        "PrincipledShaders",
        "VopNetworks",
    },
    "fbxCompatibilityMode": {
        "FBXStandard",
        "Maya",
    },
    "_ik_targetType": {
        "All",
        "Orientation",
        "Position",
    },
    "parmTemplateType": {
        "Folder",
        "Data",
    },
    "optionalBool": {
        "Yes",
        "No",
        "NoOpinion",
    },
}


# Functions that return these types are never optional.
NON_OPTIONAL_RETURN_TYPES = {
    "_AgentClipTupleGenerator",
    "_AgentGroupTupleGenerator",
    "_AgentLayerTupleGenerator",
    "_DopRecordTupleGenerator",
    "_EdgeTupleGenerator",
    "_IKJointTupleGenerator",
    "_LogEntryTupleGenerator",
    "_NetworkBoxTupleGenerator",
    "_PointTupleGenerator",
    "_PrimTupleGenerator",
    "_StickyNoteTupleGenerator",
    "_VertexTupleGenerator",
    "EnumValue",
    "Iterator",
    "Matrix2",
    "Matrix3",
    "Matrix4",
    "Quaternion",
    "Tuple",
    "Vector2",
    "Vector3",
    "Vector4",
    "std.vector",
    "tuple",
}


# Signatures of the special methods of every class: the docs give the comparison operators
# many inaccurate overloads.
SPECIAL_METHOD_SIGNATURES = {
    "__ne__": "(self, other: object) -> bool",
    "__eq__": "(self, other: object) -> bool",
    "__lt__": "(self, other: object) -> bool",
    "__le__": "(self, other: object) -> bool",
    "__gt__": "(self, other: object) -> bool",
    "__ge__": "(self, other: object) -> bool",
}
