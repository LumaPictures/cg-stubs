# mypy: disable-error-code="misc, override, no-redef"

import Boost.Python
import pxr.Ar
import pxr.Sdf
import pxr.Tf
import pxr.Usd
import pxr.UsdGeom
import pxr.UsdShade
from typing import Any, ClassVar, overload

__MFB_FULL_PACKAGE_NAME: str

class MaterialAPI(pxr.Usd.APISchemaBase):
    '''
    Deprecated

    Materials should use UsdShadeMaterial instead. This schema will be
    removed in a future release.

    This API provides outputs that connect a material prim to prman
    shaders and RIS objects.

    For any described attribute *Fallback* *Value* or *Allowed* *Values*
    below that are text/tokens, the actual token is published and defined
    in UsdRiTokens. So to set an attribute to the value"rightHanded", use
    UsdRiTokens->rightHanded as the value.
    '''
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None:
        """
        Construct a UsdRiMaterialAPI on UsdPrim C{prim}.


        Equivalent to UsdRiMaterialAPI::Get (prim.GetStage(), prim.GetPath())
        for a *valid* C{prim}, but will not immediately throw an error for an
        invalid C{prim}
        """
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None:
        """
        Construct a UsdRiMaterialAPI on the prim held by C{schemaObj}.


        Should be preferred over UsdRiMaterialAPI (schemaObj.GetPrim()), as it
        preserves SchemaBase state.
        """
    @overload
    def __init__(self, material: pxr.UsdShade.Material) -> None:
        """
        A constructor for creating a MaterialAPI object from a material prim.
        """
    @staticmethod
    def Apply(prim: pxr.Usd.Prim) -> MaterialAPI:
        '''
        Applies this B{single-apply} API schema to the given C{prim}.


        This information is stored by adding"RiMaterialAPI"to the token-
        valued, listOp metadata *apiSchemas* on the prim.

        A valid UsdRiMaterialAPI object is returned upon success. An invalid
        (or empty) UsdRiMaterialAPI object is returned upon failure. See
        UsdPrim::ApplyAPI() for conditions resulting in failure.

        UsdPrim::GetAppliedSchemas()

        UsdPrim::HasAPI()

        UsdPrim::CanApplyAPI()

        UsdPrim::ApplyAPI()

        UsdPrim::RemoveAPI()
        '''
    @staticmethod
    def CanApply(prim: pxr.Usd.Prim) -> _CanApplyResult:
        """
        Returns true if this B{single-apply} API schema can be applied to the
        given C{prim}.


        If this schema can not be a applied to the prim, this returns false
        and, if provided, populates C{whyNot} with the reason it can not be
        applied.

        Note that if CanApply returns false, that does not necessarily imply
        that calling Apply will fail. Callers are expected to call CanApply
        before calling Apply if they want to ensure that it is valid to apply
        a schema.

        UsdPrim::GetAppliedSchemas()

        UsdPrim::HasAPI()

        UsdPrim::CanApplyAPI()

        UsdPrim::ApplyAPI()

        UsdPrim::RemoveAPI()
        """
    def ComputeInterfaceInputConsumersMap(self, computeTransitiveConsumers: bool = ...) -> dict:
        """
        Walks the namespace subtree below the material and computes a map
        containing the list of all inputs on the material and the associated
        vector of consumers of their values.


        The consumers can be inputs on shaders within the material or on node-
        graphs under it.
        """
    def CreateDisplacementAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetDisplacementAttr() , and also Create vs Get Property Methods
        for when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateSurfaceAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetSurfaceAttr() , and also Create vs Get Property Methods for
        when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateVolumeAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetVolumeAttr() , and also Create vs Get Property Methods for when
        to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    @staticmethod
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> MaterialAPI:
        """
        Return a UsdRiMaterialAPI holding the prim adhering to this schema at
        C{path} on C{stage}.


        If no prim exists at C{path} on C{stage}, or if the prim at that path
        does not adhere to this schema, return an invalid schema object. This
        is shorthand for the following: ::

          UsdRiMaterialAPI(stage->GetPrimAtPath(path));

        """
    def GetDisplacement(self, ignoreBaseMaterial: bool = ...) -> pxr.UsdShade.Shader:
        '''
        Returns a valid shader object if the"displacement"output on the
        material is connected to one.


        If C{ignoreBaseMaterial} is true and if the"displacement"shader source
        is specified in the base-material of this material, then this returns
        an invalid shader object.
        '''
    def GetDisplacementAttr(self) -> pxr.Usd.Attribute:
        """

        Declaration

        C{token outputs:ri:displacement}

        C++ Type

        TfToken

        Usd Type

        SdfValueTypeNames->Token
        """
    def GetDisplacementOutput(self) -> pxr.UsdShade.Output:
        '''
        Returns the"displacement"output associated with the material.
        '''
    @staticmethod
    def GetSchemaAttributeNames(includeInherited: bool = ...) -> list[str]:
        """
        Return a vector of names of all pre-declared attributes for this
        schema class and all its ancestor classes.


        Does not include attributes that may be authored by custom/extended
        methods of the schemas involved.
        """
    def GetSurface(self, ignoreBaseMaterial: bool = ...) -> pxr.UsdShade.Shader:
        '''
        Returns a valid shader object if the"surface"output on the material is
        connected to one.


        If C{ignoreBaseMaterial} is true and if the"surface"shader source is
        specified in the base-material of this material, then this returns an
        invalid shader object.
        '''
    def GetSurfaceAttr(self) -> pxr.Usd.Attribute:
        """

        Declaration

        C{token outputs:ri:surface}

        C++ Type

        TfToken

        Usd Type

        SdfValueTypeNames->Token
        """
    def GetSurfaceOutput(self) -> pxr.UsdShade.Output:
        '''
        Returns the"surface"output associated with the material.
        '''
    def GetVolume(self, ignoreBaseMaterial: bool = ...) -> pxr.UsdShade.Shader:
        '''
        Returns a valid shader object if the"volume"output on the material is
        connected to one.


        If C{ignoreBaseMaterial} is true and if the"volume"shader source is
        specified in the base-material of this material, then this returns an
        invalid shader object.
        '''
    def GetVolumeAttr(self) -> pxr.Usd.Attribute:
        """

        Declaration

        C{token outputs:ri:volume}

        C++ Type

        TfToken

        Usd Type

        SdfValueTypeNames->Token
        """
    def GetVolumeOutput(self) -> pxr.UsdShade.Output:
        '''
        Returns the"volume"output associated with the material.
        '''
    def SetDisplacementSource(self, _displacementPath: pxr.Sdf.Path | str, /) -> bool: ...
    def SetSurfaceSource(self, _surfacePath: pxr.Sdf.Path | str, /) -> bool: ...
    def SetVolumeSource(self, _volumePath: pxr.Sdf.Path | str, /) -> bool: ...
    @staticmethod
    def _GetStaticTfType() -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...

class RenderPassAPI(pxr.Usd.APISchemaBase):
    """
    RiRenderPassAPI is an API schema that provides a mechanism to set
    certain Ri statements on each prim in a collection, for a given
    RenderPass prim.


    The objects that are relevant to the render is specified via the
    cameraVisibility collection (UsdCollectionAPI) and can be accessed via
    GetCameraVisibilityCollectionAPI() . Each prim in the collection will
    have ri:visible:camera set to 1. By default everything in the scene
    should be visible to camera, so this collection sets includeRoot to 1.

    The objects that are relevant to the render is specified via the matte
    collection (UsdCollectionAPI) and can be accessed via
    GetMatteCollectionAPI() . Each prim in the collection will have
    ri:matte set to 1. By default everything in the scene should render
    normally, so this collection sets includeRoot to 0.
    """
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None:
        """
        Construct a UsdRiRenderPassAPI on UsdPrim C{prim}.


        Equivalent to UsdRiRenderPassAPI::Get (prim.GetStage(),
        prim.GetPath()) for a *valid* C{prim}, but will not immediately throw
        an error for an invalid C{prim}
        """
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None:
        """
        Construct a UsdRiRenderPassAPI on the prim held by C{schemaObj}.


        Should be preferred over UsdRiRenderPassAPI (schemaObj.GetPrim()), as
        it preserves SchemaBase state.
        """
    @staticmethod
    def Apply(prim: pxr.Usd.Prim) -> RenderPassAPI:
        '''
        Applies this B{single-apply} API schema to the given C{prim}.


        This information is stored by adding"RiRenderPassAPI"to the token-
        valued, listOp metadata *apiSchemas* on the prim.

        A valid UsdRiRenderPassAPI object is returned upon success. An invalid
        (or empty) UsdRiRenderPassAPI object is returned upon failure. See
        UsdPrim::ApplyAPI() for conditions resulting in failure.

        UsdPrim::GetAppliedSchemas()

        UsdPrim::HasAPI()

        UsdPrim::CanApplyAPI()

        UsdPrim::ApplyAPI()

        UsdPrim::RemoveAPI()
        '''
    @staticmethod
    def CanApply(prim: pxr.Usd.Prim) -> _CanApplyResult:
        """
        Returns true if this B{single-apply} API schema can be applied to the
        given C{prim}.


        If this schema can not be a applied to the prim, this returns false
        and, if provided, populates C{whyNot} with the reason it can not be
        applied.

        Note that if CanApply returns false, that does not necessarily imply
        that calling Apply will fail. Callers are expected to call CanApply
        before calling Apply if they want to ensure that it is valid to apply
        a schema.

        UsdPrim::GetAppliedSchemas()

        UsdPrim::HasAPI()

        UsdPrim::CanApplyAPI()

        UsdPrim::ApplyAPI()

        UsdPrim::RemoveAPI()
        """
    @staticmethod
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> RenderPassAPI:
        """
        Return a UsdRiRenderPassAPI holding the prim adhering to this schema
        at C{path} on C{stage}.


        If no prim exists at C{path} on C{stage}, or if the prim at that path
        does not adhere to this schema, return an invalid schema object. This
        is shorthand for the following: ::

          UsdRiRenderPassAPI(stage->GetPrimAtPath(path));

        """
    def GetCameraVisibilityCollectionAPI(self) -> pxr.Usd.CollectionAPI:
        """
        Return the UsdCollectionAPI interface used for examining and modifying
        the camera visibility collection of this prim.
        """
    def GetMatteCollectionAPI(self) -> pxr.Usd.CollectionAPI:
        """
        Return the UsdCollectionAPI interface used for examining and modifying
        the matte collection of this prim.
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

class SplineAPI(pxr.Usd.APISchemaBase):
    '''
    Deprecated

    This API schema will be removed in a future release.

    RiSplineAPI is a general purpose API schema used to describe a named
    spline stored as a set of attributes on a prim.

    It is an add-on schema that can be applied many times to a prim with
    different spline names. All the attributes authored by the schema are
    namespaced under"$NAME:spline:", with the name of the spline providing
    a namespace for the attributes.

    The spline describes a 2D piecewise cubic curve with a position and
    value for each knot. This is chosen to give straightforward artistic
    control over the shape. The supported basis types are:

       - linear (UsdRiTokens->linear)

       - bspline (UsdRiTokens->bspline)

       - Catmull-Rom (UsdRiTokens->catmullRom)

    '''
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None:
        """
        Construct a UsdRiSplineAPI on UsdPrim C{prim}.


        Equivalent to UsdRiSplineAPI::Get (prim.GetStage(), prim.GetPath())
        for a *valid* C{prim}, but will not immediately throw an error for an
        invalid C{prim}
        """
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None:
        """
        Construct a UsdRiSplineAPI on the prim held by C{schemaObj}.


        Should be preferred over UsdRiSplineAPI (schemaObj.GetPrim()), as it
        preserves SchemaBase state.
        """
    @overload
    def __init__(self, arg2: pxr.Usd.Prim, arg3: object, arg4: pxr.Sdf.ValueTypeName, arg5: bool, /) -> None: ...
    @overload
    def __init__(self, arg2: pxr.Usd.SchemaBase, arg3: object, arg4: pxr.Sdf.ValueTypeName, arg5: bool, /) -> None: ...
    @staticmethod
    def Apply(prim: pxr.Usd.Prim) -> SplineAPI:
        '''
        Applies this B{single-apply} API schema to the given C{prim}.


        This information is stored by adding"RiSplineAPI"to the token-valued,
        listOp metadata *apiSchemas* on the prim.

        A valid UsdRiSplineAPI object is returned upon success. An invalid (or
        empty) UsdRiSplineAPI object is returned upon failure. See
        UsdPrim::ApplyAPI() for conditions resulting in failure.

        UsdPrim::GetAppliedSchemas()

        UsdPrim::HasAPI()

        UsdPrim::CanApplyAPI()

        UsdPrim::ApplyAPI()

        UsdPrim::RemoveAPI()
        '''
    @staticmethod
    def CanApply(prim: pxr.Usd.Prim) -> _CanApplyResult:
        """
        Returns true if this B{single-apply} API schema can be applied to the
        given C{prim}.


        If this schema can not be a applied to the prim, this returns false
        and, if provided, populates C{whyNot} with the reason it can not be
        applied.

        Note that if CanApply returns false, that does not necessarily imply
        that calling Apply will fail. Callers are expected to call CanApply
        before calling Apply if they want to ensure that it is valid to apply
        a schema.

        UsdPrim::GetAppliedSchemas()

        UsdPrim::HasAPI()

        UsdPrim::CanApplyAPI()

        UsdPrim::ApplyAPI()

        UsdPrim::RemoveAPI()
        """
    def CreateInterpolationAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetInterpolationAttr() , and also Create vs Get Property Methods
        for when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreatePositionsAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetPositionsAttr() , and also Create vs Get Property Methods for
        when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateValuesAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetValuesAttr() , and also Create vs Get Property Methods for when
        to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    @staticmethod
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> SplineAPI:
        """
        Return a UsdRiSplineAPI holding the prim adhering to this schema at
        C{path} on C{stage}.


        If no prim exists at C{path} on C{stage}, or if the prim at that path
        does not adhere to this schema, return an invalid schema object. This
        is shorthand for the following: ::

          UsdRiSplineAPI(stage->GetPrimAtPath(path));

        """
    def GetInterpolationAttr(self) -> pxr.Usd.Attribute:
        """
        Interpolation method for the spline.


        C++ Type: TfToken  Usd Type: SdfValueTypeNames->Token  Variability:
        SdfVariabilityUniform  Fallback Value: linear  Allowed Values :
        [linear, constant, bspline, catmullRom]
        """
    def GetPositionsAttr(self) -> pxr.Usd.Attribute:
        """
        Positions of the knots.


        C++ Type: VtArray<float>  Usd Type: SdfValueTypeNames->FloatArray
        Variability: SdfVariabilityUniform  Fallback Value: No Fallback
        """
    @staticmethod
    def GetSchemaAttributeNames(includeInherited: bool = ...) -> list[str]:
        """
        Return a vector of names of all pre-declared attributes for this
        schema class and all its ancestor classes.


        Does not include attributes that may be authored by custom/extended
        methods of the schemas involved.
        """
    def GetValuesAttr(self) -> pxr.Usd.Attribute:
        """
        Values of the knots.


        C++ Type: See GetValuesTypeName()  Usd Type: See GetValuesTypeName()
        Variability: SdfVariabilityUniform  Fallback Value: No Fallback
        """
    def GetValuesTypeName(self) -> pxr.Sdf.ValueTypeName:
        """
        Returns the intended typename of the values attribute of the spline.
        """
    def Validate(self) -> tuple:
        """
        Validates the attribute values belonging to the spline.


        Returns true if the spline has all valid attribute values. Returns
        false and populates the C{reason} output argument if the spline has
        invalid attribute values.

        Here's the list of validations performed by this method:
           - the SplineAPI must be fully initialized

           - interpolation attribute must exist and use an allowed value

           - the positions array must be a float array

           - the positions array must be sorted by increasing value

           - the values array must use the correct value type

           - the positions and values array must have the same size

        """
    @staticmethod
    def _GetStaticTfType() -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...

class StatementsAPI(pxr.Usd.APISchemaBase):
    '''
    Container namespace schema for all renderman statements.



    The longer term goal is for clients to go directly to primvar or
    render-attribute API\'s, instead of using UsdRi StatementsAPI for
    inherited attributes. Anticpating this, StatementsAPI can smooth the
    way via a few environment variables:
       - USDRI_STATEMENTS_READ_OLD_ENCODING: Causes StatementsAPI to read
         old-style attributes instead of primvars in the"ri:"namespace.

    '''
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None:
        """
        Construct a UsdRiStatementsAPI on UsdPrim C{prim}.


        Equivalent to UsdRiStatementsAPI::Get (prim.GetStage(),
        prim.GetPath()) for a *valid* C{prim}, but will not immediately throw
        an error for an invalid C{prim}
        """
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None:
        """
        Construct a UsdRiStatementsAPI on the prim held by C{schemaObj}.


        Should be preferred over UsdRiStatementsAPI (schemaObj.GetPrim()), as
        it preserves SchemaBase state.
        """
    @staticmethod
    def Apply(prim: pxr.Usd.Prim) -> StatementsAPI:
        '''
        Applies this B{single-apply} API schema to the given C{prim}.


        This information is stored by adding"StatementsAPI"to the token-
        valued, listOp metadata *apiSchemas* on the prim.

        A valid UsdRiStatementsAPI object is returned upon success. An invalid
        (or empty) UsdRiStatementsAPI object is returned upon failure. See
        UsdPrim::ApplyAPI() for conditions resulting in failure.

        UsdPrim::GetAppliedSchemas()

        UsdPrim::HasAPI()

        UsdPrim::CanApplyAPI()

        UsdPrim::ApplyAPI()

        UsdPrim::RemoveAPI()
        '''
    @staticmethod
    def CanApply(prim: pxr.Usd.Prim) -> _CanApplyResult:
        """
        Returns true if this B{single-apply} API schema can be applied to the
        given C{prim}.


        If this schema can not be a applied to the prim, this returns false
        and, if provided, populates C{whyNot} with the reason it can not be
        applied.

        Note that if CanApply returns false, that does not necessarily imply
        that calling Apply will fail. Callers are expected to call CanApply
        before calling Apply if they want to ensure that it is valid to apply
        a schema.

        UsdPrim::GetAppliedSchemas()

        UsdPrim::HasAPI()

        UsdPrim::CanApplyAPI()

        UsdPrim::ApplyAPI()

        UsdPrim::RemoveAPI()
        """
    @overload
    def CreateRiAttribute(self, name: str | pxr.Ar.ResolvedPath, riType: str | pxr.Ar.ResolvedPath, nameSpace: str | pxr.Ar.ResolvedPath = ...) -> pxr.Usd.Attribute:
        '''
        Create a rib attribute on the prim to which this schema is attached.


        A rib attribute consists of an attribute *"nameSpace"* and an
        attribute *"name"*. For example, the namespace"cull"may define
        attributes"backfacing"and"hidden", and user-defined attributes belong
        to the namespace"user".

        This method makes no attempt to validate that the given C{nameSpace}
        and *name* are actually meaningful to prman or any other renderer.

        riType

        should be a known RenderMan type definition, which can be array-
        valued. For instance, both"color"and"float[3]"are valid values for
        C{riType}.
        '''
    @overload
    def CreateRiAttribute(self, name: str | pxr.Ar.ResolvedPath, tfType: pxr.Tf.Type, nameSpace: str | pxr.Ar.ResolvedPath = ...) -> pxr.Usd.Attribute:
        """
        Creates an attribute of the given C{tfType}.


        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        """
    @staticmethod
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> StatementsAPI:
        """
        Return a UsdRiStatementsAPI holding the prim adhering to this schema
        at C{path} on C{stage}.


        If no prim exists at C{path} on C{stage}, or if the prim at that path
        does not adhere to this schema, return an invalid schema object. This
        is shorthand for the following: ::

          UsdRiStatementsAPI(stage->GetPrimAtPath(path));

        """
    def GetCoordinateSystem(self) -> str:
        '''
        Returns the value in the"ri:coordinateSystem"attribute if it exists.
        '''
    def GetModelCoordinateSystems(self) -> list[pxr.Sdf.Path]:
        """
        Populates the output C{targets} with the authored
        ri:modelCoordinateSystems, if any.


        Returns true if the query was successful.
        """
    def GetModelScopedCoordinateSystems(self) -> list[pxr.Sdf.Path]:
        """
        Populates the output C{targets} with the authored
        ri:modelScopedCoordinateSystems, if any.


        Returns true if the query was successful.
        """
    def GetRiAttribute(self, name: str | pxr.Ar.ResolvedPath, nameSpace: str | pxr.Ar.ResolvedPath = ...) -> pxr.Usd.Attribute:
        """
        Return a UsdAttribute representing the Ri attribute with the name
        *name*, in the namespace *nameSpace*.


        The attribute returned may or may not B{actually} exist so it must be
        checked for validity.
        """
    @staticmethod
    def GetRiAttributeName(prop: pxr.Usd.Property | pxr.UsdGeom.XformOp) -> str:
        '''
        Return the base, most-specific name of the rib attribute.


        For example, the *name* of the rib
        attribute"cull:backfacing"is"backfacing"
        '''
    @staticmethod
    def GetRiAttributeNameSpace(prop: pxr.Usd.Property | pxr.UsdGeom.XformOp) -> str:
        '''
        Return the containing namespace of the rib attribute (e.g."user").
        '''
    def GetRiAttributes(self, nameSpace: str | pxr.Ar.ResolvedPath = ...) -> list[pxr.Usd.Property]:
        '''
        Return all rib attributes on this prim, or under a specific namespace
        (e.g."user").


        As noted above, rib attributes can be either UsdAttribute or
        UsdRelationship, and like all UsdProperties, need not have a defined
        value.
        '''
    @staticmethod
    def GetSchemaAttributeNames(includeInherited: bool = ...) -> list[str]:
        """
        Return a vector of names of all pre-declared attributes for this
        schema class and all its ancestor classes.


        Does not include attributes that may be authored by custom/extended
        methods of the schemas involved.
        """
    def GetScopedCoordinateSystem(self) -> str:
        '''
        Returns the value in the"ri:scopedCoordinateSystem"attribute if it
        exists.
        '''
    def HasCoordinateSystem(self) -> bool:
        """
        Returns true if the underlying prim has a ri:coordinateSystem opinion.
        """
    def HasScopedCoordinateSystem(self) -> bool:
        """
        Returns true if the underlying prim has a ri:scopedCoordinateSystem
        opinion.
        """
    @staticmethod
    def IsRiAttribute(prop: pxr.Usd.Property | pxr.UsdGeom.XformOp) -> bool:
        '''
        Return true if the property is in the"ri:attributes"namespace.
        '''
    @staticmethod
    def MakeRiAttributePropertyName(attrName: str | pxr.Ar.ResolvedPath) -> str:
        '''
        Returns the given C{attrName} prefixed with the full Ri attribute
        namespace, creating a name suitable for an RiAttribute UsdProperty.


        This handles conversion of common separator characters used in other
        packages, such as periods and underscores.

        Will return empty string if attrName is not a valid property
        identifier; otherwise, will return a valid property name that
        identifies the property as an RiAttribute, according to the following
        rules:
           - If C{attrName} is already a properly constructed RiAttribute
             property name, return it unchanged.

           - If C{attrName} contains two or more tokens separated by a
             *colon*, consider the first to be the namespace, and the rest the
             name, joined by underscores

           - If C{attrName} contains two or more tokens separated by a
             *period*, consider the first to be the namespace, and the rest the
             name, joined by underscores

           - If C{attrName} contains two or more tokens separated by an,
             *underscore* consider the first to be the namespace, and the rest the
             name, joined by underscores

           - else, assume C{attrName} is the name, and"user"is the namespace

        '''
    def SetCoordinateSystem(self, coordSysName: str | pxr.Ar.ResolvedPath) -> None:
        '''
        Sets the"ri:coordinateSystem"attribute to the given string value,
        creating the attribute if needed.


        That identifies this prim as providing a coordinate system, which can
        be retrieved via UsdGeomXformable::GetTransformAttr(). Also adds the
        owning prim to the ri:modelCoordinateSystems relationship targets on
        its parent leaf model prim, if it exists. If this prim is not under a
        leaf model, no relationship targets will be authored.
        '''
    def SetScopedCoordinateSystem(self, coordSysName: str | pxr.Ar.ResolvedPath) -> None:
        '''
        Sets the"ri:scopedCoordinateSystem"attribute to the given string
        value, creating the attribute if needed.


        That identifies this prim as providing a coordinate system, which can
        be retrieved via UsdGeomXformable::GetTransformAttr(). Such coordinate
        systems are local to the RI attribute stack state, but does get
        updated properly for instances when defined inside an object master.
        Also adds the owning prim to the ri:modelScopedCoordinateSystems
        relationship targets on its parent leaf model prim, if it exists. If
        this prim is not under a leaf model, no relationship targets will be
        authored.
        '''
    @staticmethod
    def _GetStaticTfType() -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...

class Tokens(Boost.Python.instance):
    RiMaterialAPI: ClassVar[str] = ...  # read-only
    RiRenderPassAPI: ClassVar[str] = ...  # read-only
    RiSplineAPI: ClassVar[str] = ...  # read-only
    StatementsAPI: ClassVar[str] = ...  # read-only
    bspline: ClassVar[str] = ...  # read-only
    cameraVisibility: ClassVar[str] = ...  # read-only
    catmullRom: ClassVar[str] = ...  # read-only
    collectionCameraVisibilityIncludeRoot: ClassVar[str] = ...  # read-only
    constant: ClassVar[str] = ...  # read-only
    interpolation: ClassVar[str] = ...  # read-only
    linear: ClassVar[str] = ...  # read-only
    matte: ClassVar[str] = ...  # read-only
    outputsRiDisplacement: ClassVar[str] = ...  # read-only
    outputsRiSurface: ClassVar[str] = ...  # read-only
    outputsRiVolume: ClassVar[str] = ...  # read-only
    positions: ClassVar[str] = ...  # read-only
    renderContext: ClassVar[str] = ...  # read-only
    spline: ClassVar[str] = ...  # read-only
    values: ClassVar[str] = ...  # read-only
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """

class _CanApplyResult(Boost.Python.instance):
    __instance_size__: ClassVar[int] = ...
    def __init__(self, arg2: bool, arg3: object, /) -> None: ...
    def __bool__(self) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    def __getitem__(self, arg2: int, /) -> Any: ...
    def __ne__(self, other: object) -> bool: ...
    @property
    def whyNot(self): ...

def ConvertFromRManFaceVaryingLinearInterpolation(_i: int, /) -> str:
    """
    Given the integer C{i} that corresponds to an rman enum for face-
    varying interpolate boundary condition, returns the equivalent UsdGeom
    token.
    """
def ConvertFromRManInterpolateBoundary(_i: int, /) -> str:
    """
    Given the integer C{i} that corresponds to an rman enum for
    interpolate boundary condition, returns the equivalent UsdGeom token.
    """
def ConvertToRManFaceVaryingLinearInterpolation(_token: str | pxr.Ar.ResolvedPath, /) -> int:
    """
    Given a C{token} representing a UsdGeom face-varying interpolate
    boundary value, returns corresponding rman enum (converted to int).
    """
def ConvertToRManInterpolateBoundary(_token: str | pxr.Ar.ResolvedPath, /) -> int:
    """
    Given a C{token} representing a UsdGeom interpolate boundary value,
    returns corresponding rman enum (converted to int).
    """
