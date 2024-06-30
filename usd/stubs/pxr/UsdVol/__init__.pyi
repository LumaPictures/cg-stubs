# mypy: disable-error-code="misc, override, no-redef"

import Boost.Python
import pxr.Ar
import pxr.Sdf
import pxr.Tf
import pxr.Usd
import pxr.UsdGeom
from typing import Any, ClassVar, overload

__MFB_FULL_PACKAGE_NAME: str

class Field3DAsset(FieldAsset):
    '''
    Field3D field primitive.


    The FieldAsset filePath attribute must specify a file in the Field3D
    format on disk.

    For any described attribute *Fallback* *Value* or *Allowed* *Values*
    below that are text/tokens, the actual token is published and defined
    in UsdVolTokens. So to set an attribute to the value"rightHanded", use
    UsdVolTokens->rightHanded as the value.
    '''
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None:
        """
        Construct a UsdVolField3DAsset on UsdPrim C{prim}.


        Equivalent to UsdVolField3DAsset::Get (prim.GetStage(),
        prim.GetPath()) for a *valid* C{prim}, but will not immediately throw
        an error for an invalid C{prim}
        """
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None:
        """
        Construct a UsdVolField3DAsset on the prim held by C{schemaObj}.


        Should be preferred over UsdVolField3DAsset (schemaObj.GetPrim()), as
        it preserves SchemaBase state.
        """
    def CreateFieldDataTypeAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetFieldDataTypeAttr() , and also Create vs Get Property Methods
        for when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateFieldPurposeAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetFieldPurposeAttr() , and also Create vs Get Property Methods
        for when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    @staticmethod
    def Define(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> Field3DAsset:
        """
        Attempt to ensure a *UsdPrim* adhering to this schema at C{path} is
        defined (according to UsdPrim::IsDefined() ) on this stage.


        If a prim adhering to this schema at C{path} is already defined on
        this stage, return that prim. Otherwise author an *SdfPrimSpec* with
        *specifier* == *SdfSpecifierDef* and this schema's prim type name for
        the prim at C{path} at the current EditTarget. Author *SdfPrimSpec* s
        with C{specifier} == *SdfSpecifierDef* and empty typeName at the
        current EditTarget for any nonexistent, or existing but not *Defined*
        ancestors.

        The given *path* must be an absolute prim path that does not contain
        any variant selections.

        If it is impossible to author any of the necessary PrimSpecs, (for
        example, in case *path* cannot map to the current UsdEditTarget 's
        namespace) issue an error and return an invalid *UsdPrim*.

        Note that this method may return a defined prim whose typeName does
        not specify this schema class, in case a stronger typeName opinion
        overrides the opinion at the current EditTarget.
        """
    @staticmethod
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> Field3DAsset:
        """
        Return a UsdVolField3DAsset holding the prim adhering to this schema
        at C{path} on C{stage}.


        If no prim exists at C{path} on C{stage}, or if the prim at that path
        does not adhere to this schema, return an invalid schema object. This
        is shorthand for the following: ::

          UsdVolField3DAsset(stage->GetPrimAtPath(path));

        """
    def GetFieldDataTypeAttr(self) -> pxr.Usd.Attribute:
        """
        Token which is used to indicate the data type of an individual field.


        Authors use this to tell consumers more about the field without
        opening the file on disk. The list of allowed tokens reflects the
        available choices for Field3d volumes.

        Declaration

        C{token fieldDataType}

        C++ Type

        TfToken

        Usd Type

        SdfValueTypeNames->Token

        Allowed Values

        half, float, double, half3, float3, double3
        """
    def GetFieldPurposeAttr(self) -> pxr.Usd.Attribute:
        """
        Optional token which can be used to indicate the purpose or grouping
        of an individual field.


        Clients which consume Field3D files should treat this as the Field3D
        field *name*.

        Declaration

        C{token fieldPurpose}

        C++ Type

        TfToken

        Usd Type

        SdfValueTypeNames->Token
        """
    @staticmethod
    def GetSchemaAttributeNames(includeInherited: bool = ...) -> list[str]:
        """
        Return a vector of names of all pre-declared attributes for this
        schema class and all its ancestor classes.


        Does not include attributes that may be authored by custom/extended
        methods of the schemas involved.
        """
    @staticmethod
    def _GetStaticTfType() -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...

class FieldAsset(FieldBase):
    '''
    Base class for field primitives defined by an external file.


    For any described attribute *Fallback* *Value* or *Allowed* *Values*
    below that are text/tokens, the actual token is published and defined
    in UsdVolTokens. So to set an attribute to the value"rightHanded", use
    UsdVolTokens->rightHanded as the value.
    '''
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None:
        """
        Construct a UsdVolFieldAsset on UsdPrim C{prim}.


        Equivalent to UsdVolFieldAsset::Get (prim.GetStage(), prim.GetPath())
        for a *valid* C{prim}, but will not immediately throw an error for an
        invalid C{prim}
        """
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None:
        """
        Construct a UsdVolFieldAsset on the prim held by C{schemaObj}.


        Should be preferred over UsdVolFieldAsset (schemaObj.GetPrim()), as it
        preserves SchemaBase state.
        """
    def CreateFieldDataTypeAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetFieldDataTypeAttr() , and also Create vs Get Property Methods
        for when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateFieldIndexAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetFieldIndexAttr() , and also Create vs Get Property Methods for
        when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateFieldNameAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetFieldNameAttr() , and also Create vs Get Property Methods for
        when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateFilePathAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetFilePathAttr() , and also Create vs Get Property Methods for
        when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateVectorDataRoleHintAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetVectorDataRoleHintAttr() , and also Create vs Get Property
        Methods for when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    @staticmethod
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> FieldAsset:
        """
        Return a UsdVolFieldAsset holding the prim adhering to this schema at
        C{path} on C{stage}.


        If no prim exists at C{path} on C{stage}, or if the prim at that path
        does not adhere to this schema, return an invalid schema object. This
        is shorthand for the following: ::

          UsdVolFieldAsset(stage->GetPrimAtPath(path));

        """
    def GetFieldDataTypeAttr(self) -> pxr.Usd.Attribute:
        """
        Token which is used to indicate the data type of an individual field.


        Authors use this to tell consumers more about the field without
        opening the file on disk. The list of allowed tokens is specified with
        the specific asset type. A missing value is considered an error.

        Declaration

        C{token fieldDataType}

        C++ Type

        TfToken

        Usd Type

        SdfValueTypeNames->Token
        """
    def GetFieldIndexAttr(self) -> pxr.Usd.Attribute:
        """
        A file can contain multiple fields with the same name.


        This optional attribute is an index used to disambiguate between these
        multiple fields with the same name.

        Declaration

        C{int fieldIndex}

        C++ Type

        int

        Usd Type

        SdfValueTypeNames->Int
        """
    def GetFieldNameAttr(self) -> pxr.Usd.Attribute:
        """
        Name of an individual field within the file specified by the filePath
        attribute.



        Declaration

        C{token fieldName}

        C++ Type

        TfToken

        Usd Type

        SdfValueTypeNames->Token
        """
    def GetFilePathAttr(self) -> pxr.Usd.Attribute:
        '''
        An asset path attribute that points to a file on disk.


        For each supported file format, a separate FieldAsset subclass is
        required.

        This attribute\'s value can be animated over time, as most volume asset
        formats represent just a single timeSample of a volume. However, it
        does not, at this time, support any pattern substitutions like"$F".

        Declaration

        C{asset filePath}

        C++ Type

        SdfAssetPath

        Usd Type

        SdfValueTypeNames->Asset
        '''
    @staticmethod
    def GetSchemaAttributeNames(includeInherited: bool = ...) -> list[str]:
        """
        Return a vector of names of all pre-declared attributes for this
        schema class and all its ancestor classes.


        Does not include attributes that may be authored by custom/extended
        methods of the schemas involved.
        """
    def GetVectorDataRoleHintAttr(self) -> pxr.Usd.Attribute:
        '''
        Optional token which is used to indicate the role of a vector valued
        field.


        This can drive the data type in which fields are made available in a
        renderer or whether the vector values are to be transformed.

        Declaration

        C{token vectorDataRoleHint ="None"}

        C++ Type

        TfToken

        Usd Type

        SdfValueTypeNames->Token

        Allowed Values

        None, Point, Normal, Vector, Color
        '''
    @staticmethod
    def _GetStaticTfType() -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...

class FieldBase(pxr.UsdGeom.Xformable):
    """
    Base class for field primitives.
    """
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None:
        """
        Construct a UsdVolFieldBase on UsdPrim C{prim}.


        Equivalent to UsdVolFieldBase::Get (prim.GetStage(), prim.GetPath())
        for a *valid* C{prim}, but will not immediately throw an error for an
        invalid C{prim}
        """
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None:
        """
        Construct a UsdVolFieldBase on the prim held by C{schemaObj}.


        Should be preferred over UsdVolFieldBase (schemaObj.GetPrim()), as it
        preserves SchemaBase state.
        """
    @staticmethod
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> FieldBase:
        """
        Return a UsdVolFieldBase holding the prim adhering to this schema at
        C{path} on C{stage}.


        If no prim exists at C{path} on C{stage}, or if the prim at that path
        does not adhere to this schema, return an invalid schema object. This
        is shorthand for the following: ::

          UsdVolFieldBase(stage->GetPrimAtPath(path));

        """
    @staticmethod
    def GetSchemaAttributeNames(includeInherited: bool = ...) -> list[str]:
        """
        Return a vector of names of all pre-declared attributes for this
        schema class and all its ancestor classes.


        Does not include attributes that may be authored by custom/extended
        methods of the schemas involved.
        """
    @staticmethod
    def _GetStaticTfType() -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...

class OpenVDBAsset(FieldAsset):
    '''
    OpenVDB field primitive.


    The FieldAsset filePath attribute must specify a file in the OpenVDB
    format on disk.

    For any described attribute *Fallback* *Value* or *Allowed* *Values*
    below that are text/tokens, the actual token is published and defined
    in UsdVolTokens. So to set an attribute to the value"rightHanded", use
    UsdVolTokens->rightHanded as the value.
    '''
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None:
        """
        Construct a UsdVolOpenVDBAsset on UsdPrim C{prim}.


        Equivalent to UsdVolOpenVDBAsset::Get (prim.GetStage(),
        prim.GetPath()) for a *valid* C{prim}, but will not immediately throw
        an error for an invalid C{prim}
        """
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None:
        """
        Construct a UsdVolOpenVDBAsset on the prim held by C{schemaObj}.


        Should be preferred over UsdVolOpenVDBAsset (schemaObj.GetPrim()), as
        it preserves SchemaBase state.
        """
    def CreateFieldClassAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetFieldClassAttr() , and also Create vs Get Property Methods for
        when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateFieldDataTypeAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetFieldDataTypeAttr() , and also Create vs Get Property Methods
        for when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    @staticmethod
    def Define(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> OpenVDBAsset:
        """
        Attempt to ensure a *UsdPrim* adhering to this schema at C{path} is
        defined (according to UsdPrim::IsDefined() ) on this stage.


        If a prim adhering to this schema at C{path} is already defined on
        this stage, return that prim. Otherwise author an *SdfPrimSpec* with
        *specifier* == *SdfSpecifierDef* and this schema's prim type name for
        the prim at C{path} at the current EditTarget. Author *SdfPrimSpec* s
        with C{specifier} == *SdfSpecifierDef* and empty typeName at the
        current EditTarget for any nonexistent, or existing but not *Defined*
        ancestors.

        The given *path* must be an absolute prim path that does not contain
        any variant selections.

        If it is impossible to author any of the necessary PrimSpecs, (for
        example, in case *path* cannot map to the current UsdEditTarget 's
        namespace) issue an error and return an invalid *UsdPrim*.

        Note that this method may return a defined prim whose typeName does
        not specify this schema class, in case a stronger typeName opinion
        overrides the opinion at the current EditTarget.
        """
    @staticmethod
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> OpenVDBAsset:
        """
        Return a UsdVolOpenVDBAsset holding the prim adhering to this schema
        at C{path} on C{stage}.


        If no prim exists at C{path} on C{stage}, or if the prim at that path
        does not adhere to this schema, return an invalid schema object. This
        is shorthand for the following: ::

          UsdVolOpenVDBAsset(stage->GetPrimAtPath(path));

        """
    def GetFieldClassAttr(self) -> pxr.Usd.Attribute:
        """
        Optional token which can be used to indicate the class of an
        individual grid.


        This is a mapping to openvdb::GridClass where the values are
        GRID_LEVEL_SET, GRID_FOG_VOLUME, GRID_STAGGERED, and GRID_UNKNOWN.

        Declaration

        C{token fieldClass}

        C++ Type

        TfToken

        Usd Type

        SdfValueTypeNames->Token

        Allowed Values

        levelSet, fogVolume, staggered, unknown
        """
    def GetFieldDataTypeAttr(self) -> pxr.Usd.Attribute:
        """
        Token which is used to indicate the data type of an individual field.


        Authors use this to tell consumers more about the field without
        opening the file on disk. The list of allowed tokens reflects the
        available choices for OpenVDB volumes.

        Declaration

        C{token fieldDataType}

        C++ Type

        TfToken

        Usd Type

        SdfValueTypeNames->Token

        Allowed Values

        half, float, double, int, uint, int64, half2, float2, double2, int2,
        half3, float3, double3, int3, matrix3d, matrix4d, quatd, bool, mask,
        string
        """
    @staticmethod
    def GetSchemaAttributeNames(includeInherited: bool = ...) -> list[str]:
        """
        Return a vector of names of all pre-declared attributes for this
        schema class and all its ancestor classes.


        Does not include attributes that may be authored by custom/extended
        methods of the schemas involved.
        """
    @staticmethod
    def _GetStaticTfType() -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...

class Tokens(Boost.Python.instance):
    Color: ClassVar[str] = ...  # read-only
    Field3DAsset: ClassVar[str] = ...  # read-only
    FieldAsset: ClassVar[str] = ...  # read-only
    FieldBase: ClassVar[str] = ...  # read-only
    None_: ClassVar[str] = ...  # read-only
    Normal: ClassVar[str] = ...  # read-only
    OpenVDBAsset: ClassVar[str] = ...  # read-only
    Point: ClassVar[str] = ...  # read-only
    Vector: ClassVar[str] = ...  # read-only
    Volume: ClassVar[str] = ...  # read-only
    bool_: ClassVar[str] = ...  # read-only
    double2: ClassVar[str] = ...  # read-only
    double3: ClassVar[str] = ...  # read-only
    double_: ClassVar[str] = ...  # read-only
    field: ClassVar[str] = ...  # read-only
    fieldClass: ClassVar[str] = ...  # read-only
    fieldDataType: ClassVar[str] = ...  # read-only
    fieldIndex: ClassVar[str] = ...  # read-only
    fieldName: ClassVar[str] = ...  # read-only
    fieldPurpose: ClassVar[str] = ...  # read-only
    filePath: ClassVar[str] = ...  # read-only
    float2: ClassVar[str] = ...  # read-only
    float3: ClassVar[str] = ...  # read-only
    float_: ClassVar[str] = ...  # read-only
    fogVolume: ClassVar[str] = ...  # read-only
    half: ClassVar[str] = ...  # read-only
    half2: ClassVar[str] = ...  # read-only
    half3: ClassVar[str] = ...  # read-only
    int2: ClassVar[str] = ...  # read-only
    int3: ClassVar[str] = ...  # read-only
    int64: ClassVar[str] = ...  # read-only
    int_: ClassVar[str] = ...  # read-only
    levelSet: ClassVar[str] = ...  # read-only
    mask: ClassVar[str] = ...  # read-only
    matrix3d: ClassVar[str] = ...  # read-only
    matrix4d: ClassVar[str] = ...  # read-only
    quatd: ClassVar[str] = ...  # read-only
    staggered: ClassVar[str] = ...  # read-only
    string: ClassVar[str] = ...  # read-only
    uint: ClassVar[str] = ...  # read-only
    unknown: ClassVar[str] = ...  # read-only
    vectorDataRoleHint: ClassVar[str] = ...  # read-only
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """

class Volume(pxr.UsdGeom.Gprim):
    '''
    A renderable volume primitive.


    A volume is made up of any number of FieldBase primitives bound
    together in this volume. Each FieldBase primitive is specified as a
    relationship with a namespace prefix of"field".

    The relationship name is used by the renderer to associate individual
    fields with the named input parameters on the volume shader. Using
    this indirect approach to connecting fields to shader parameters
    (rather than using the field prim\'s name) allows a single field to be
    reused for different shader inputs, or to be used as different shader
    parameters when rendering different Volumes. This means that the name
    of the field prim is not relevant to its contribution to the volume
    prims which refer to it. Nor does the field prim\'s location in the
    scene graph have any relevance, and Volumes may refer to fields
    anywhere in the scene graph. B{However}, unless Field prims need to be
    shared by multiple Volumes, a Volume\'s Field prims should be located
    under the Volume in namespace, for enhanced organization.
    '''
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None:
        """
        Construct a UsdVolVolume on UsdPrim C{prim}.


        Equivalent to UsdVolVolume::Get (prim.GetStage(), prim.GetPath()) for
        a *valid* C{prim}, but will not immediately throw an error for an
        invalid C{prim}
        """
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None:
        """
        Construct a UsdVolVolume on the prim held by C{schemaObj}.


        Should be preferred over UsdVolVolume (schemaObj.GetPrim()), as it
        preserves SchemaBase state.
        """
    def BlockFieldRelationship(self, name: str | pxr.Ar.ResolvedPath) -> bool:
        """
        Blocks an existing field relationship on this volume, ensuring it will
        not be enumerated by GetFieldPaths() .


        Returns true if the relationship existed, false if it did not. In
        other words the return value indicates whether the volume prim was
        changed.

        The name lookup automatically applies the field relationship
        namespacing, if it isn't specified in the name token.
        """
    def CreateFieldRelationship(self, name: str | pxr.Ar.ResolvedPath, fieldPath: pxr.Sdf.Path | str) -> bool:
        '''
        Creates a relationship on this volume that targets the specified
        field.


        If an existing relationship exists with the same name, it is replaced
        (since only one target is allowed for each named relationship).

        Returns C{true} if the relationship was successfully created and set -
        it is legal to call this method for a field relationship that
        already"exists", i.e. already posesses scene description, as this is
        the only method we provide for setting a field relatioonship\'s value,
        to help enforce that field relationships can have only a single (or
        no) target.

        fieldPath

        - can be a prim path, or the path of another relationship, to effect
        Relationship Forwarding The name lookup automatically applies the
        field relationship namespacing, if it isn\'t specified in the name
        token.
        '''
    @staticmethod
    def Define(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> Volume:
        """
        Attempt to ensure a *UsdPrim* adhering to this schema at C{path} is
        defined (according to UsdPrim::IsDefined() ) on this stage.


        If a prim adhering to this schema at C{path} is already defined on
        this stage, return that prim. Otherwise author an *SdfPrimSpec* with
        *specifier* == *SdfSpecifierDef* and this schema's prim type name for
        the prim at C{path} at the current EditTarget. Author *SdfPrimSpec* s
        with C{specifier} == *SdfSpecifierDef* and empty typeName at the
        current EditTarget for any nonexistent, or existing but not *Defined*
        ancestors.

        The given *path* must be an absolute prim path that does not contain
        any variant selections.

        If it is impossible to author any of the necessary PrimSpecs, (for
        example, in case *path* cannot map to the current UsdEditTarget 's
        namespace) issue an error and return an invalid *UsdPrim*.

        Note that this method may return a defined prim whose typeName does
        not specify this schema class, in case a stronger typeName opinion
        overrides the opinion at the current EditTarget.
        """
    @staticmethod
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> Volume:
        """
        Return a UsdVolVolume holding the prim adhering to this schema at
        C{path} on C{stage}.


        If no prim exists at C{path} on C{stage}, or if the prim at that path
        does not adhere to this schema, return an invalid schema object. This
        is shorthand for the following: ::

          UsdVolVolume(stage->GetPrimAtPath(path));

        """
    def GetFieldPath(self, name: str | pxr.Ar.ResolvedPath) -> pxr.Sdf.Path:
        """
        Checks if there is an existing field relationship with a given name,
        and if so, returns the path to the Field prim it targets, or else the
        empty path.


        The name lookup automatically applies the field relationship
        namespacing, if it isn't specified in the name token.
        """
    def GetFieldPaths(self) -> dict:
        """
        Return a map of field relationship names to the fields themselves,
        represented as prim paths.


        This map provides all the information that should be needed to tie
        fields to shader parameters and render this volume.

        The field relationship names that server as the map keys will have the
        field namespace stripped from them.
        """
    @staticmethod
    def GetSchemaAttributeNames(includeInherited: bool = ...) -> list[str]:
        """
        Return a vector of names of all pre-declared attributes for this
        schema class and all its ancestor classes.


        Does not include attributes that may be authored by custom/extended
        methods of the schemas involved.
        """
    def HasFieldRelationship(self, name: str | pxr.Ar.ResolvedPath) -> bool:
        """
        Checks if there is an existing field relationship with a given name.


        This query will return C{true} even for a field relationship that has
        been blocked and therefore will not contribute to the map returned by
        GetFieldRelationships()

        The name lookup automatically applies the field relationship
        namespacing, if it isn't specified in the name token.
        """
    @staticmethod
    def _GetStaticTfType() -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...
