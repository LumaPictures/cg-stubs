# mypy: disable-error-code="misc, override, no-redef"

import Boost.Python
import pxr.Ar
import pxr.Gf
import pxr.Sdf
import pxr.Tf
import pxr.Usd
import pxr.UsdGeom
import pxr.UsdShade
import pxr.Vt
import typing
from typing import Any, ClassVar, overload

__MFB_FULL_PACKAGE_NAME: str

class AnimMapper(Boost.Python.instance):
    @overload
    def __init__(self) -> None:
        """
        Construct a null mapper.
        """
    @overload
    def __init__(self, _size: int, /) -> None:
        """
        Construct an identity mapper for remapping a range of C{size} elems.


        An identity mapper is used to indicate that no remapping is required.
        """
    @overload
    def __init__(self, sourceOrder: pxr.Vt.TokenArray | typing.Iterable[pxr.Ar.ResolvedPath] | typing.Iterable[str], targetOrder: pxr.Vt.TokenArray | typing.Iterable[pxr.Ar.ResolvedPath] | typing.Iterable[str]) -> None:
        """
        Construct a mapper for mapping data from C{sourceOrder} to
        C{targetOrder}.
        """
    def IsIdentity(self) -> bool:
        """
        Returns true if this is an identity map.


        The source and target orders of an identity map are identical.
        """
    def IsNull(self) -> bool:
        """
        Returns true if this is a null mapping.


        No source elements of a null map are mapped to the target.
        """
    def IsSparse(self) -> bool:
        """
        Returns true if this is a sparse mapping.


        A sparse mapping means that not all target values will be overridden
        by source values, when mapped with Remap().
        """
    def Remap(self, source: object, target: object = ..., elementSize: int = ..., defaultValue: object = ...) -> Any: ...
    @overload
    def RemapTransforms(self, source: pxr.Vt.Matrix4fArray | typing.Iterable[pxr.Gf.Matrix4f], target: pxr.Vt.Matrix4fArray | typing.Iterable[pxr.Gf.Matrix4f], elementSize: int = ...) -> pxr.Vt.Matrix4fArray:
        """
        Convenience method for the common task of remapping transform arrays.


        This performs the same operation as Remap(), but sets the matrix
        identity as the default value.
        """
    @overload
    def RemapTransforms(self, source: pxr.Vt.Matrix4dArray | typing.Iterable[pxr.Gf.Matrix4d], target: pxr.Vt.Matrix4dArray | typing.Iterable[pxr.Gf.Matrix4d], elementSize: int = ...) -> pxr.Vt.Matrix4dArray: ...
    def __len__(self) -> int: ...

class AnimQuery(Boost.Python.instance):
    """
    Class providing efficient queries of primitives that provide skel
    animation.
    """
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """
    def BlendShapeWeightsMightBeTimeVarying(self) -> bool:
        """
        Return true if it possible, but not certain, that the blend shape
        weights computed through this animation query change over time, false
        otherwise.



        UsdAttribute::ValueMightBeTimeVayring
        """
    def ComputeBlendShapeWeights(self, time: pxr.Usd.TimeCode | float | pxr.Sdf.TimeCode = ...) -> pxr.Vt.FloatArray: ...
    def ComputeJointLocalTransformComponents(self, time: pxr.Usd.TimeCode | float | pxr.Sdf.TimeCode = ...) -> tuple:
        """
        Compute translation,rotation,scale components of the joint transforms
        in joint-local space.


        This is provided to facilitate direct streaming of animation data in a
        form that can efficiently be processed for animation blending.
        """
    def ComputeJointLocalTransforms(self, time: pxr.Usd.TimeCode | float | pxr.Sdf.TimeCode = ...) -> pxr.Vt.Matrix4dArray:
        """
        Compute joint transforms in joint-local space.


        Transforms are returned in the order specified by the joint ordering
        of the animation primitive itself.
        """
    def GetBlendShapeOrder(self) -> pxr.Vt.TokenArray:
        """
        Returns an array of tokens describing the ordering of blend shape
        channels in the animation.
        """
    def GetBlendShapeWeightTimeSamples(self) -> list[float]:
        """
        Get the time samples at which values contributing to blend shape
        weights have been set.



        UsdAttribute::GetTimeSamples
        """
    def GetBlendShapeWeightTimeSamplesInInterval(self, interval: pxr.Gf.Interval) -> list[float]:
        """
        Get the time samples at which values contributing to blend shape
        weights are set, over C{interval}.



        UsdAttribute::GetTimeSamplesInInterval
        """
    def GetJointOrder(self) -> pxr.Vt.TokenArray:
        """
        Returns an array of tokens describing the ordering of joints in the
        animation.



        UsdSkelSkeleton::GetJointOrder
        """
    def GetJointTransformTimeSamples(self) -> list[float]:
        """
        Get the time samples at which values contributing to joint transforms
        are set.


        This only computes the time samples for sampling transforms in joint-
        local space, and does not include time samples affecting the root
        transformation.

        UsdAttribute::GetTimeSamples
        """
    def GetJointTransformTimeSamplesInInterval(self, interval: pxr.Gf.Interval) -> list[float]:
        """
        Get the time samples at which values contributing to joint transforms
        are set, over C{interval}.


        This only computes the time samples for sampling transforms in joint-
        local space, and does not include time samples affecting the root
        transformation.

        UsdAttribute::GetTimeSamplesInInterval
        """
    def GetPrim(self) -> pxr.Usd.Prim:
        """
        Return the primitive this anim query reads from.
        """
    def JointTransformsMightBeTimeVarying(self) -> bool:
        """
        Return true if it possible, but not certain, that joint transforms
        computed through this animation query change over time, false
        otherwise.



        UsdAttribute::ValueMightBeTimeVayring
        """
    def __bool__(self) -> bool:
        """
        Boolean conversion operator. Equivalent to IsValid() .
        """
    def __eq__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...

class Animation(pxr.Usd.Typed):
    """
    Describes a skel animation, where joint animation is stored in a
    vectorized form.


    See the extended Skel Animation documentation for more information.
    """
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None:
        """
        Construct a UsdSkelAnimation on UsdPrim C{prim}.


        Equivalent to UsdSkelAnimation::Get (prim.GetStage(), prim.GetPath())
        for a *valid* C{prim}, but will not immediately throw an error for an
        invalid C{prim}
        """
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None:
        """
        Construct a UsdSkelAnimation on the prim held by C{schemaObj}.


        Should be preferred over UsdSkelAnimation (schemaObj.GetPrim()), as it
        preserves SchemaBase state.
        """
    def CreateBlendShapeWeightsAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetBlendShapeWeightsAttr() , and also Create vs Get Property
        Methods for when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateBlendShapesAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetBlendShapesAttr() , and also Create vs Get Property Methods for
        when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateJointsAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetJointsAttr() , and also Create vs Get Property Methods for when
        to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateRotationsAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetRotationsAttr() , and also Create vs Get Property Methods for
        when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateScalesAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetScalesAttr() , and also Create vs Get Property Methods for when
        to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateTranslationsAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetTranslationsAttr() , and also Create vs Get Property Methods
        for when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    @staticmethod
    def Define(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> Animation:
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
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> Animation:
        """
        Return a UsdSkelAnimation holding the prim adhering to this schema at
        C{path} on C{stage}.


        If no prim exists at C{path} on C{stage}, or if the prim at that path
        does not adhere to this schema, return an invalid schema object. This
        is shorthand for the following: ::

          UsdSkelAnimation(stage->GetPrimAtPath(path));

        """
    def GetBlendShapeWeightsAttr(self) -> pxr.Usd.Attribute:
        """
        Array of weight values for each blend shape.


        Each weight value is associated with the corresponding blend shape
        identified within the *blendShapes* token array, and therefore must
        have the same length as *blendShapes.

        Declaration

        C{float[] blendShapeWeights}

        C++ Type

        VtArray<float>

        Usd Type

        SdfValueTypeNames->FloatArray
        """
    def GetBlendShapesAttr(self) -> pxr.Usd.Attribute:
        """
        Array of tokens identifying which blend shapes this animation's data
        applies to.


        The tokens for blendShapes correspond to the tokens set in the
        *skel:blendShapes* binding property of the UsdSkelBindingAPI.

        Declaration

        C{uniform token[] blendShapes}

        C++ Type

        VtArray<TfToken>

        Usd Type

        SdfValueTypeNames->TokenArray

        Variability

        SdfVariabilityUniform
        """
    def GetJointsAttr(self) -> pxr.Usd.Attribute:
        """
        Array of tokens identifying which joints this animation's data applies
        to.


        The tokens for joints correspond to the tokens of Skeleton primitives.
        The order of the joints as listed here may vary from the order of
        joints on the Skeleton itself.

        Declaration

        C{uniform token[] joints}

        C++ Type

        VtArray<TfToken>

        Usd Type

        SdfValueTypeNames->TokenArray

        Variability

        SdfVariabilityUniform
        """
    def GetRotationsAttr(self) -> pxr.Usd.Attribute:
        """
        Joint-local unit quaternion rotations of all affected joints, in
        32-bit precision.


        Array length should match the size of the *joints* attribute.

        Declaration

        C{quatf[] rotations}

        C++ Type

        VtArray<GfQuatf>

        Usd Type

        SdfValueTypeNames->QuatfArray
        """
    def GetScalesAttr(self) -> pxr.Usd.Attribute:
        """
        Joint-local scales of all affected joints, in 16 bit precision.


        Array length should match the size of the *joints* attribute.

        Declaration

        C{half3[] scales}

        C++ Type

        VtArray<GfVec3h>

        Usd Type

        SdfValueTypeNames->Half3Array
        """
    @staticmethod
    def GetSchemaAttributeNames(includeInherited: bool = ...) -> list[str]:
        """
        Return a vector of names of all pre-declared attributes for this
        schema class and all its ancestor classes.


        Does not include attributes that may be authored by custom/extended
        methods of the schemas involved.
        """
    def GetTransforms(self, time: pxr.Usd.TimeCode | float | pxr.Sdf.TimeCode = ...) -> pxr.Vt.Matrix4dArray:
        """
        Convenience method for querying resolved transforms at C{time}.


        Note that it is more efficient to query transforms through
        UsdSkelAnimQuery or UsdSkelSkeletonQuery.
        """
    def GetTranslationsAttr(self) -> pxr.Usd.Attribute:
        """
        Joint-local translations of all affected joints.


        Array length should match the size of the *joints* attribute.

        Declaration

        C{float3[] translations}

        C++ Type

        VtArray<GfVec3f>

        Usd Type

        SdfValueTypeNames->Float3Array
        """
    def SetTransforms(self, xforms: pxr.Vt.Matrix4dArray | typing.Iterable[pxr.Gf.Matrix4d], time: pxr.Usd.TimeCode | float | pxr.Sdf.TimeCode = ...) -> bool:
        """
        Convenience method for setting an array of transforms.


        The given transforms must be *orthogonal*.
        """
    @staticmethod
    def _GetStaticTfType() -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...

class Binding(Boost.Python.instance):
    """
    Helper object that describes the binding of a skeleton to a set of
    skinnable objects.


    The set of skinnable objects is given as UsdSkelSkinningQuery prims,
    which can be used both to identify the skinned prim as well compute
    skinning properties of the prim.
    """
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, _skel: Skeleton, _skinningQueries: list[SkinningQuery], /) -> None: ...
    def GetSkeleton(self) -> Skeleton:
        """
        Returns the bound skeleton.
        """
    def GetSkinningTargets(self) -> list[SkinningQuery]:
        """
        Returns the set skinning targets.
        """

class BindingAPI(pxr.Usd.APISchemaBase):
    '''
    Provides API for authoring and extracting all the skinning-related
    data that lives in the"geometry hierarchy"of prims and models that
    want to be skeletally deformed.


    See the extended UsdSkelBindingAPI schema documentation for more about
    bindings and how they apply in a scene graph.

    For any described attribute *Fallback* *Value* or *Allowed* *Values*
    below that are text/tokens, the actual token is published and defined
    in UsdSkelTokens. So to set an attribute to the value"rightHanded",
    use UsdSkelTokens->rightHanded as the value.
    '''
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None:
        """
        Construct a UsdSkelBindingAPI on UsdPrim C{prim}.


        Equivalent to UsdSkelBindingAPI::Get (prim.GetStage(), prim.GetPath())
        for a *valid* C{prim}, but will not immediately throw an error for an
        invalid C{prim}
        """
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None:
        """
        Construct a UsdSkelBindingAPI on the prim held by C{schemaObj}.


        Should be preferred over UsdSkelBindingAPI (schemaObj.GetPrim()), as
        it preserves SchemaBase state.
        """
    @staticmethod
    def Apply(prim: pxr.Usd.Prim) -> BindingAPI:
        '''
        Applies this B{single-apply} API schema to the given C{prim}.


        This information is stored by adding"SkelBindingAPI"to the token-
        valued, listOp metadata *apiSchemas* on the prim.

        A valid UsdSkelBindingAPI object is returned upon success. An invalid
        (or empty) UsdSkelBindingAPI object is returned upon failure. See
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
    def CreateAnimationSourceRel(self) -> pxr.Usd.Relationship:
        """
        See GetAnimationSourceRel() , and also Create vs Get Property Methods
        for when to use Get vs Create.
        """
    def CreateBlendShapeTargetsRel(self) -> pxr.Usd.Relationship:
        """
        See GetBlendShapeTargetsRel() , and also Create vs Get Property
        Methods for when to use Get vs Create.
        """
    def CreateBlendShapesAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetBlendShapesAttr() , and also Create vs Get Property Methods for
        when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateGeomBindTransformAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetGeomBindTransformAttr() , and also Create vs Get Property
        Methods for when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateJointIndicesAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetJointIndicesAttr() , and also Create vs Get Property Methods
        for when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateJointIndicesPrimvar(self, constant: bool, elementSize: int = ...) -> pxr.UsdGeom.Primvar:
        """
        Convenience function to create the jointIndices primvar, optionally
        specifying elementSize.


        If C{constant} is true, the resulting primvar is configured
        with'constant'interpolation, and describes a rigid deformation.
        Otherwise, the primvar is configured with'vertex'interpolation, and
        describes joint influences that vary per point.

        CreateJointIndicesAttr() , GetJointIndicesPrimvar()
        """
    def CreateJointWeightsAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetJointWeightsAttr() , and also Create vs Get Property Methods
        for when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateJointWeightsPrimvar(self, constant: bool, elementSize: int = ...) -> pxr.UsdGeom.Primvar:
        """
        Convenience function to create the jointWeights primvar, optionally
        specifying elementSize.


        If C{constant} is true, the resulting primvar is configured
        with'constant'interpolation, and describes a rigid deformation.
        Otherwise, the primvar is configured with'vertex'interpolation, and
        describes joint influences that vary per point.

        CreateJointWeightsAttr() , GetJointWeightsPrimvar()
        """
    def CreateJointsAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetJointsAttr() , and also Create vs Get Property Methods for when
        to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateSkeletonRel(self) -> pxr.Usd.Relationship:
        """
        See GetSkeletonRel() , and also Create vs Get Property Methods for
        when to use Get vs Create.
        """
    def CreateSkinningMethodAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetSkinningMethodAttr() , and also Create vs Get Property Methods
        for when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    @staticmethod
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> BindingAPI:
        """
        Return a UsdSkelBindingAPI holding the prim adhering to this schema at
        C{path} on C{stage}.


        If no prim exists at C{path} on C{stage}, or if the prim at that path
        does not adhere to this schema, return an invalid schema object. This
        is shorthand for the following: ::

          UsdSkelBindingAPI(stage->GetPrimAtPath(path));

        """
    def GetAnimationSource(self) -> pxr.Usd.Prim:
        """
        Convenience method to query the animation source bound on this prim.


        Returns true if an animation source binding is defined, and sets
        C{prim} to the target prim. The resulting primitive may still be
        invalid, if the prim has been explicitly *unbound*.

        This does not resolved inherited animation source bindings.
        """
    def GetAnimationSourceRel(self) -> pxr.Usd.Relationship:
        """
        Animation source to be bound to Skeleton primitives at or beneath the
        location at which this property is defined.
        """
    def GetBlendShapeTargetsRel(self) -> pxr.Usd.Relationship:
        """
        Ordered list of all target blend shapes.


        This property is not inherited hierarchically, and is expected to be
        authored directly on the skinnable primitive to which the the blend
        shapes apply.
        """
    def GetBlendShapesAttr(self) -> pxr.Usd.Attribute:
        """
        An array of tokens defining the order onto which blend shape weights
        from an animation source map onto the *skel:blendShapeTargets* rel of
        a binding site.


        If authored, the number of elements must be equal to the number of
        targets in the *blendShapeTargets* rel. This property is not inherited
        hierarchically, and is expected to be authored directly on the
        skinnable primitive to which the blend shapes apply.

        Declaration

        C{uniform token[] skel:blendShapes}

        C++ Type

        VtArray<TfToken>

        Usd Type

        SdfValueTypeNames->TokenArray

        Variability

        SdfVariabilityUniform
        """
    def GetGeomBindTransformAttr(self) -> pxr.Usd.Attribute:
        '''
        Encodes the bind-time world space transforms of the prim.


        If the transform is identical for a group of gprims that share a
        common ancestor, the transform may be authored on the ancestor,
        to"inherit"down to all the leaf gprims. If this transform is unset, an
        identity transform is used instead.

        Declaration

        C{matrix4d primvars:skel:geomBindTransform}

        C++ Type

        GfMatrix4d

        Usd Type

        SdfValueTypeNames->Matrix4d
        '''
    def GetInheritedAnimationSource(self) -> pxr.Usd.Prim:
        """
        Returns the animation source bound at this prim, or one of its
        ancestors.
        """
    def GetInheritedSkeleton(self) -> Skeleton:
        """
        Returns the skeleton bound at this prim, or one of its ancestors.
        """
    def GetJointIndicesAttr(self) -> pxr.Usd.Attribute:
        """
        Indices into the *joints* attribute of the closest (in namespace)
        bound Skeleton that affect each point of a PointBased gprim.


        The primvar can have either *constant* or *vertex* interpolation. This
        primvar's *elementSize* will determine how many joint influences apply
        to each point. Indices must point be valid. Null influences should be
        defined by setting values in jointWeights to zero. See UsdGeomPrimvar
        for more information on interpolation and elementSize.

        Declaration

        C{int[] primvars:skel:jointIndices}

        C++ Type

        VtArray<int>

        Usd Type

        SdfValueTypeNames->IntArray
        """
    def GetJointIndicesPrimvar(self) -> pxr.UsdGeom.Primvar:
        """
        Convenience function to get the jointIndices attribute as a primvar.



        GetJointIndicesAttr, GetInheritedJointWeightsPrimvar
        """
    def GetJointWeightsAttr(self) -> pxr.Usd.Attribute:
        """
        Weights for the joints that affect each point of a PointBased gprim.


        The primvar can have either *constant* or *vertex* interpolation. This
        primvar's *elementSize* will determine how many joints influences
        apply to each point. The length, interpolation, and elementSize of
        *jointWeights* must match that of *jointIndices*. See UsdGeomPrimvar
        for more information on interpolation and elementSize.

        Declaration

        C{float[] primvars:skel:jointWeights}

        C++ Type

        VtArray<float>

        Usd Type

        SdfValueTypeNames->FloatArray
        """
    def GetJointWeightsPrimvar(self) -> pxr.UsdGeom.Primvar:
        """
        Convenience function to get the jointWeights attribute as a primvar.



        GetJointWeightsAttr, GetInheritedJointWeightsPrimvar
        """
    def GetJointsAttr(self) -> pxr.Usd.Attribute:
        """
        An (optional) array of tokens defining the list of joints to which
        jointIndices apply.


        If not defined, jointIndices applies to the ordered list of joints
        defined in the bound Skeleton's *joints* attribute. If undefined on a
        primitive, the primitive inherits the value of the nearest ancestor
        prim, if any.

        Declaration

        C{uniform token[] skel:joints}

        C++ Type

        VtArray<TfToken>

        Usd Type

        SdfValueTypeNames->TokenArray

        Variability

        SdfVariabilityUniform
        """
    @staticmethod
    def GetSchemaAttributeNames(includeInherited: bool = ...) -> list[str]:
        """
        Return a vector of names of all pre-declared attributes for this
        schema class and all its ancestor classes.


        Does not include attributes that may be authored by custom/extended
        methods of the schemas involved.
        """
    def GetSkeleton(self) -> Skeleton:
        """
        Convenience method to query the Skeleton bound on this prim.


        Returns true if a Skeleton binding is defined, and sets C{skel} to the
        target skel. The resulting Skeleton may still be invalid, if the
        Skeleton has been explicitly *unbound*.

        This does not resolved inherited skeleton bindings.
        """
    def GetSkeletonRel(self) -> pxr.Usd.Relationship:
        """
        Skeleton to be bound to this prim and its descendents that possess a
        mapping and weighting to the joints of the identified Skeleton.
        """
    def GetSkinningMethodAttr(self) -> pxr.Usd.Attribute:
        '''
        The skinningMethod specifies the skinning method for the prim.



        Declaration

        C{uniform token primvars:skel:skinningMethod ="classicLinear"}

        C++ Type

        TfToken

        Usd Type

        SdfValueTypeNames->Token

        Variability

        SdfVariabilityUniform

        Allowed Values

        classicLinear, dualQuaternion
        '''
    def SetRigidJointInfluence(self, jointIndex: int, weight: float = ...) -> bool:
        """
        Convenience method for defining joints influences that make a
        primitive rigidly deformed by a single joint.
        """
    @staticmethod
    def ValidateJointIndices(jointIndices: pxr.Vt.IntArray | typing.Iterable[int], numJoints: int) -> tuple:
        """
        Validate an array of joint indices.


        This ensures that all indices are the in the range [0, numJoints).
        Returns true if the indices are valid, or false otherwise. If invalid
        and C{reason} is non-null, an error message describing the first
        validation error will be set.
        """
    @staticmethod
    def _GetStaticTfType() -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...

class BlendShape(pxr.Usd.Typed):
    """
    Describes a target blend shape, possibly containing inbetween shapes.


    See the extended Blend Shape Schema documentation for information.
    """
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None:
        """
        Construct a UsdSkelBlendShape on UsdPrim C{prim}.


        Equivalent to UsdSkelBlendShape::Get (prim.GetStage(), prim.GetPath())
        for a *valid* C{prim}, but will not immediately throw an error for an
        invalid C{prim}
        """
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None:
        """
        Construct a UsdSkelBlendShape on the prim held by C{schemaObj}.


        Should be preferred over UsdSkelBlendShape (schemaObj.GetPrim()), as
        it preserves SchemaBase state.
        """
    def CreateInbetween(self, name: str | pxr.Ar.ResolvedPath) -> InbetweenShape:
        """
        Author scene description to create an attribute on this prim that will
        be recognized as an Inbetween (i.e.


        will present as a valid UsdSkelInbetweenShape).

        The name of the created attribute or may or may not be the specified
        C{attrName}, due to the possible need to apply property namespacing.
        Creation may fail and return an invalid Inbetwen if C{attrName}
        contains a reserved keyword.

        an invalid UsdSkelInbetweenShape if we failed to create a valid
        attribute, a valid UsdSkelInbetweenShape otherwise. It is not an error
        to create over an existing, compatible attribute.

        UsdSkelInbetweenShape::IsInbetween()
        """
    def CreateNormalOffsetsAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetNormalOffsetsAttr() , and also Create vs Get Property Methods
        for when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateOffsetsAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetOffsetsAttr() , and also Create vs Get Property Methods for
        when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreatePointIndicesAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetPointIndicesAttr() , and also Create vs Get Property Methods
        for when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    @staticmethod
    def Define(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> BlendShape:
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
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> BlendShape:
        """
        Return a UsdSkelBlendShape holding the prim adhering to this schema at
        C{path} on C{stage}.


        If no prim exists at C{path} on C{stage}, or if the prim at that path
        does not adhere to this schema, return an invalid schema object. This
        is shorthand for the following: ::

          UsdSkelBlendShape(stage->GetPrimAtPath(path));

        """
    def GetAuthoredInbetweens(self) -> list[InbetweenShape]:
        """
        Like GetInbetweens() , but exclude inbetwens that have no authored
        scene / description.
        """
    def GetInbetween(self, name: str | pxr.Ar.ResolvedPath) -> InbetweenShape:
        """
        Return the Inbetween corresponding to the attribute named C{name},
        which will be valid if an Inbetween attribute definition already
        exists.


        Name lookup will account for Inbetween namespacing, which means that
        this method will succeed in some cases where C{UsdSkelInbetweenShape
        (prim->GetAttribute(name))} will not, unless C{name} has the proper
        namespace prefix.

        HasInbetween()
        """
    def GetInbetweens(self) -> list[InbetweenShape]:
        """
        Return valid UsdSkelInbetweenShape objects for all defined Inbetweens
        on this prim.
        """
    def GetNormalOffsetsAttr(self) -> pxr.Usd.Attribute:
        """
        B{Required property}.


        Normal offsets which, when added to the base pose, provides the
        normals of the target shape.

        Declaration

        C{uniform vector3f[] normalOffsets}

        C++ Type

        VtArray<GfVec3f>

        Usd Type

        SdfValueTypeNames->Vector3fArray

        Variability

        SdfVariabilityUniform
        """
    def GetOffsetsAttr(self) -> pxr.Usd.Attribute:
        """
        B{Required property}.


        Position offsets which, when added to the base pose, provides the
        target shape.

        Declaration

        C{uniform vector3f[] offsets}

        C++ Type

        VtArray<GfVec3f>

        Usd Type

        SdfValueTypeNames->Vector3fArray

        Variability

        SdfVariabilityUniform
        """
    def GetPointIndicesAttr(self) -> pxr.Usd.Attribute:
        """
        B{Optional property}.


        Indices into the original mesh that correspond to the values in
        *offsets* and of any inbetween shapes. If authored, the number of
        elements must be equal to the number of elements in the *offsets*
        array.

        Declaration

        C{uniform int[] pointIndices}

        C++ Type

        VtArray<int>

        Usd Type

        SdfValueTypeNames->IntArray

        Variability

        SdfVariabilityUniform
        """
    @staticmethod
    def GetSchemaAttributeNames(includeInherited: bool = ...) -> list[str]:
        """
        Return a vector of names of all pre-declared attributes for this
        schema class and all its ancestor classes.


        Does not include attributes that may be authored by custom/extended
        methods of the schemas involved.
        """
    def HasInbetween(self, name: str | pxr.Ar.ResolvedPath) -> bool:
        """
        Return true if there is a defined Inbetween named C{name} on this
        prim.


        Name lookup will account for Inbetween namespacing.

        GetInbetween()
        """
    @staticmethod
    def ValidatePointIndices(pointIndices: pxr.Vt.IntArray | typing.Iterable[int], numPoints: int) -> tuple:
        """
        Validates a set of point indices for a given point count.


        This ensures that all point indices are in the range [0, numPoints).
        Returns true if the indices are valid, or false otherwise. If invalid
        and C{reason} is non-null, an error message describing the first
        validation error will be set.
        """
    @staticmethod
    def _GetStaticTfType() -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...

class BlendShapeQuery(Boost.Python.instance):
    """
    Helper class used to resolve blend shape weights, including
    inbetweens.
    """
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, _binding: BindingAPI, /) -> None: ...
    def ComputeBlendShapePointIndices(self) -> list[pxr.Vt.IntArray]:
        """
        Compute an array holding the point indices of all shapes.


        This is indexed by the *blendShapeIndices* returned by
        ComputeSubShapes(). Since the *pointIndices* property of blend shapes
        is optional, some of the arrays may be empty.
        """
    def ComputeDeformedPoints(self, subShapeWeights: pxr.Vt.FloatArray | typing.Iterable[float], blendShapeIndices: pxr.Vt.UIntArray | typing.Iterable[int], subShapeIndices: pxr.Vt.UIntArray | typing.Iterable[int], blendShapePointIndices: typing.Iterable[pxr.Vt.IntArray | typing.Iterable[int]], subShapePointOffset: typing.Iterable[pxr.Vt.Vec3fArray | typing.Iterable[list[float]] | typing.Iterable[pxr.Gf.Vec3f] | typing.Iterable[tuple[float, float, float]]], points: pxr.Vt.Vec3fArray | typing.Iterable[list[float]] | typing.Iterable[pxr.Gf.Vec3f] | typing.Iterable[tuple[float, float, float]]) -> bool:
        """
        Deform C{points} using the resolved sub-shapes given by
        C{subShapeWeights}, C{blendShapeIndices} and C{subShapeIndices}.


        The C{blendShapePointIndices} and C{blendShapePointOffsets} arrays
        both provide the pre-computed point offsets and indices of each sub-
        shape, as computed by ComputeBlendShapePointIndices() and
        ComputeSubShapePointOffsets() .
        """
    def ComputeSubShapePointOffsets(self) -> list[pxr.Vt.Vec3fArray]:
        """
        Compute an array holding the point offsets of all sub-shapes.


        This includes offsets of both primary shapes  those stored directly on
        a BlendShape primitive  as well as those of inbetween shapes. This is
        indexed by the *subShapeIndices* returned by ComputeSubShapeWeights()
        .
        """
    def ComputeSubShapeWeights(self, _weights: pxr.Vt.FloatArray | typing.Iterable[float], /) -> tuple:
        """
        Compute the resolved weights for all sub-shapes bound to this prim.


        The C{weights} values are initial weight values, ordered according to
        the *skel:blendShapeTargets* relationship of the prim this query is
        associated with. If there are any inbetween shapes, a new set of
        weights is computed, providing weighting of the relevant inbetweens.

        All computed arrays shared the same size. Elements of the same index
        identify which sub-shape of which blend shape a given weight value is
        mapped to.
        """
    def GetBlendShape(self, _blendShapeIndex: int, /) -> BlendShape:
        """
        Returns the blend shape corresponding to C{blendShapeIndex}.
        """
    def GetBlendShapeIndex(self, _subShapeIndex: int, /) -> int:
        """
        Returns the blend shape index corresponding to the C{i'th} sub-shape.
        """
    def GetInbetween(self, _subShapeIndex: int, /) -> InbetweenShape:
        """
        Returns the inbetween shape corresponding to sub-shape C{i}, if any.
        """
    def GetNumBlendShapes(self) -> int: ...
    def GetNumSubShapes(self) -> int: ...

class Cache(Boost.Python.instance):
    """
    Thread-safe cache for accessing query objects for evaluating skeletal
    data.


    This provides caching of major structural components, such as skeletal
    topology. In a streaming context, this cache is intended to persist.
    """
    __instance_size__: ClassVar[int] = ...
    def __init__(self) -> None: ...
    def Clear(self) -> None: ...
    def ComputeSkelBinding(self, skelRoot: Root, skel: Skeleton, predicate: pxr.Usd._PrimFlagsPredicate | pxr.Usd._Term) -> Binding:
        """
        Compute the bindings corresponding to a single skeleton, bound beneath
        C{skelRoot}, as discovered through a traversal using C{predicate}.


        Skinnable prims are only discoverable by this method if Populate() has
        already been called for C{skelRoot}, with an equivalent predicate.
        """
    def ComputeSkelBindings(self, skelRoot: Root, predicate: pxr.Usd._PrimFlagsPredicate | pxr.Usd._Term) -> list[Binding]:
        """
        Compute the set of skeleton bindings beneath C{skelRoot}, as
        discovered through a traversal using C{predicate}.


        Skinnable prims are only discoverable by this method if Populate() has
        already been called for C{skelRoot}, with an equivalent predicate.
        """
    @overload
    def GetAnimQuery(self, anim: Animation) -> AnimQuery:
        """
        Get an anim query corresponding to C{anim}.


        This does not require Populate() to be called on the cache.
        """
    @overload
    def GetAnimQuery(self, prim: pxr.Usd.Prim) -> AnimQuery:
        """
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.


        Deprecated
        """
    def GetSkelQuery(self, _skel: Skeleton, /) -> SkeletonQuery:
        """
        Get a skel query for computing properties of C{skel}.


        This does not require Populate() to be called on the cache.
        """
    def GetSkinningQuery(self, _prim: pxr.Usd.Prim, /) -> SkinningQuery:
        """
        Get a skinning query at C{prim}.


        Skinning queries are defined at any skinnable prims (I.e., boundable
        prims with fully defined joint influences).

        The caller must first Populate() the cache with the skel root
        containing C{prim}, with a predicate that will visit C{prim}, in order
        for a skinning query to be discoverable.
        """
    def Populate(self, skelRoot: Root, predicate: pxr.Usd._PrimFlagsPredicate | pxr.Usd._Term) -> bool:
        """
        Populate the cache for the skeletal data beneath prim C{root}, as
        traversed using C{predicate}.


        Population resolves inherited skel bindings set using the
        UsdSkelBindingAPI, making resolved bindings available through
        GetSkinningQuery() , ComputeSkelBinding() and ComputeSkelBindings() .
        """

class InbetweenShape(Boost.Python.instance):
    """
    Schema wrapper for UsdAttribute for authoring and introspecting
    attributes that serve as inbetween shapes of a UsdSkelBlendShape.


    Inbetween shapes allow an explicit shape to be specified when the
    blendshape to which it's bound is evaluated at a certain weight. For
    example, rather than performing piecewise linear interpolation between
    a primary shape and the rest shape at weight 0.5, an inbetween shape
    could be defined at the weight. For weight values greater than 0.5, a
    shape would then be resolved by linearly interpolating between the
    inbetween shape and the primary shape, while for weight values less
    than or equal to 0.5, the shape is resolved by linearly interpolating
    between the inbetween shape and the primary shape.
    """
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None:
        """
        Default constructor returns an invalid inbetween shape.
        """
    @overload
    def __init__(self, attr: pxr.Usd.Attribute | pxr.UsdGeom.ConstraintTarget | pxr.UsdGeom.Primvar | pxr.UsdGeom.XformOp | pxr.UsdShade.Input | pxr.UsdShade.Output) -> None:
        """
        Speculative constructor that will produce a valid
        UsdSkelInbetweenShape when C{attr} already represents an attribute
        that is an Inbetween, and produces an *invalid* Inbetween otherwise
        (i.e.


        operator bool() will return false).

        Calling C{UsdSkelInbetweenShape::IsInbetween(attr)} will return the
        same truth value as this constructor, but if you plan to subsequently
        use the Inbetween anyways, just use this constructor.
        """
    def CreateNormalOffsetsAttr(self, _defaultValue: Any, /) -> pxr.Usd.Attribute:
        """
        Returns the existing normal offsets attribute if the shape has normal
        offsets, or creates a new one.
        """
    def GetAttr(self) -> pxr.Usd.Attribute:
        """
        Explicit UsdAttribute extractor.
        """
    def GetNormalOffsets(self) -> pxr.Vt.Vec3fArray:
        """
        Get the normal offsets authored for this shape.


        Normal offsets are optional, and may be left unspecified.
        """
    def GetNormalOffsetsAttr(self) -> pxr.Usd.Attribute:
        """
        Returns a valid normal offsets attribute if the shape has normal
        offsets.


        Returns an invalid attribute otherwise.
        """
    def GetOffsets(self) -> pxr.Vt.Vec3fArray:
        """
        Get the point offsets corresponding to this shape.
        """
    def GetWeight(self) -> float:
        """
        Return the location at which the shape is applied.
        """
    def HasAuthoredWeight(self) -> bool:
        """
        Has a weight value been explicitly authored on this shape?



        GetWeight()
        """
    def IsDefined(self) -> bool:
        """
        Return true if the wrapped UsdAttribute::IsDefined() , and in addition
        the attribute is identified as an Inbetween.
        """
    @staticmethod
    def IsInbetween(attr: pxr.Usd.Attribute | pxr.UsdGeom.ConstraintTarget | pxr.UsdGeom.Primvar | pxr.UsdGeom.XformOp | pxr.UsdShade.Input | pxr.UsdShade.Output) -> bool:
        """
        Test whether a given UsdAttribute represents a valid Inbetween, which
        implies that creating a UsdSkelInbetweenShape from the attribute will
        succeed.


        Succes implies that C{attr.IsDefined()} is true.
        """
    def SetNormalOffsets(self, offsets: pxr.Vt.Vec3fArray | typing.Iterable[list[float]] | typing.Iterable[pxr.Gf.Vec3f] | typing.Iterable[tuple[float, float, float]]) -> bool:
        """
        Set the normal offsets authored for this shape.
        """
    def SetOffsets(self, offsets: pxr.Vt.Vec3fArray | typing.Iterable[list[float]] | typing.Iterable[pxr.Gf.Vec3f] | typing.Iterable[tuple[float, float, float]]) -> bool:
        """
        Set the point offsets corresponding to this shape.
        """
    def SetWeight(self, weight: float) -> bool:
        """
        Set the location at which the shape is applied.
        """
    def __bool__(self) -> bool:
        """
        Return true if this Inbetween is valid for querying and authoring
        values and metadata, which is identically equivalent to IsDefined() .
        """
    def __eq__(self, other: object) -> bool: ...

class Root(pxr.UsdGeom.Boundable):
    """
    Boundable prim type used to identify a scope beneath which skeletally-
    posed primitives are defined.


    A SkelRoot must be defined at or above a skinned primitive for any
    skinning behaviors in UsdSkel.

    See the extended Skel Root Schema documentation for more information.
    """
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None:
        """
        Construct a UsdSkelRoot on UsdPrim C{prim}.


        Equivalent to UsdSkelRoot::Get (prim.GetStage(), prim.GetPath()) for a
        *valid* C{prim}, but will not immediately throw an error for an
        invalid C{prim}
        """
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None:
        """
        Construct a UsdSkelRoot on the prim held by C{schemaObj}.


        Should be preferred over UsdSkelRoot (schemaObj.GetPrim()), as it
        preserves SchemaBase state.
        """
    @staticmethod
    def Define(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> Root:
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
    def Find(_prim: pxr.Usd.Prim, /) -> Root:
        """
        Returns the skel root at or above C{prim}, or an invalid schema object
        if no ancestor prim is defined as a skel root.
        """
    @staticmethod
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> Root:
        """
        Return a UsdSkelRoot holding the prim adhering to this schema at
        C{path} on C{stage}.


        If no prim exists at C{path} on C{stage}, or if the prim at that path
        does not adhere to this schema, return an invalid schema object. This
        is shorthand for the following: ::

          UsdSkelRoot(stage->GetPrimAtPath(path));

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

class Skeleton(pxr.UsdGeom.Boundable):
    """
    Describes a skeleton.


    See the extended Skeleton Schema documentation for more information.
    """
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None:
        """
        Construct a UsdSkelSkeleton on UsdPrim C{prim}.


        Equivalent to UsdSkelSkeleton::Get (prim.GetStage(), prim.GetPath())
        for a *valid* C{prim}, but will not immediately throw an error for an
        invalid C{prim}
        """
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None:
        """
        Construct a UsdSkelSkeleton on the prim held by C{schemaObj}.


        Should be preferred over UsdSkelSkeleton (schemaObj.GetPrim()), as it
        preserves SchemaBase state.
        """
    def CreateBindTransformsAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetBindTransformsAttr() , and also Create vs Get Property Methods
        for when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateJointNamesAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetJointNamesAttr() , and also Create vs Get Property Methods for
        when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateJointsAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetJointsAttr() , and also Create vs Get Property Methods for when
        to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateRestTransformsAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetRestTransformsAttr() , and also Create vs Get Property Methods
        for when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    @staticmethod
    def Define(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> Skeleton:
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
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> Skeleton:
        """
        Return a UsdSkelSkeleton holding the prim adhering to this schema at
        C{path} on C{stage}.


        If no prim exists at C{path} on C{stage}, or if the prim at that path
        does not adhere to this schema, return an invalid schema object. This
        is shorthand for the following: ::

          UsdSkelSkeleton(stage->GetPrimAtPath(path));

        """
    def GetBindTransformsAttr(self) -> pxr.Usd.Attribute:
        """
        Specifies the bind-pose transforms of each joint in B{world space}, in
        the ordering imposed by *joints*.



        Declaration

        C{uniform matrix4d[] bindTransforms}

        C++ Type

        VtArray<GfMatrix4d>

        Usd Type

        SdfValueTypeNames->Matrix4dArray

        Variability

        SdfVariabilityUniform
        """
    def GetJointNamesAttr(self) -> pxr.Usd.Attribute:
        """
        If authored, provides a unique name per joint.


        This may be optionally set to provide better names when translating to
        DCC apps that require unique joint names.

        Declaration

        C{uniform token[] jointNames}

        C++ Type

        VtArray<TfToken>

        Usd Type

        SdfValueTypeNames->TokenArray

        Variability

        SdfVariabilityUniform
        """
    def GetJointsAttr(self) -> pxr.Usd.Attribute:
        """
        An array of path tokens identifying the set of joints that make up the
        skeleton, and their order.


        Each token in the array must be valid when parsed as an SdfPath. The
        parent-child relationships of the corresponding paths determine the
        parent-child relationships of each joint. It is not required that the
        name at the end of each path be unique, but rather only that the paths
        themselves be unique.

        Declaration

        C{uniform token[] joints}

        C++ Type

        VtArray<TfToken>

        Usd Type

        SdfValueTypeNames->TokenArray

        Variability

        SdfVariabilityUniform
        """
    def GetRestTransformsAttr(self) -> pxr.Usd.Attribute:
        """
        Specifies the rest-pose transforms of each joint in B{local space}, in
        the ordering imposed by *joints*.


        This provides fallback values for joint transforms when a Skeleton
        either has no bound animation source, or when that animation source
        only contains animation for a subset of a Skeleton's joints.

        Declaration

        C{uniform matrix4d[] restTransforms}

        C++ Type

        VtArray<GfMatrix4d>

        Usd Type

        SdfValueTypeNames->Matrix4dArray

        Variability

        SdfVariabilityUniform
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

class SkeletonQuery(Boost.Python.instance):
    """
    Primary interface to reading *bound* skeleton data.


    This is used to query properties such as resolved transforms and
    animation bindings, as bound through the UsdSkelBindingAPI.

    A UsdSkelSkeletonQuery can not be constructed directly, and instead
    must be constructed through a UsdSkelCache instance. This is done as
    follows: ::

      // Global cache, intended to persist.
      UsdSkelCache skelCache;
      // Populate the cache for a skel root.
      skelCache.Populate(UsdSkelRoot(skelRootPrim));
  
      if (UsdSkelSkeletonQuery skelQuery = skelCache.GetSkelQuery(skelPrim)) {
          ...
      }

    """
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """
    def ComputeJointLocalTransforms(self, time: pxr.Usd.TimeCode | float | pxr.Sdf.TimeCode = ..., atRest: bool = ...) -> pxr.Vt.Matrix4dArray:
        """
        Compute joint transforms in joint-local space, at C{time}.


        This returns transforms in joint order of the skeleton. If C{atRest}
        is false and an animation source is bound, local transforms defined by
        the animation are mapped into the skeleton's joint order. Any
        transforms not defined by the animation source use the transforms from
        the rest pose as a fallback value. If valid transforms cannot be
        computed for the animation source, the C{xforms} are instead set to
        the rest transforms.
        """
    def ComputeJointRestRelativeTransforms(self, time: pxr.Usd.TimeCode | float | pxr.Sdf.TimeCode = ...) -> pxr.Vt.Matrix4dArray:
        """
        Compute joint transforms which, when concatenated against the rest
        pose, produce joint transforms in joint-local space.


        More specifically, this computes *restRelativeTransform* in: ::

          restRelativeTransform * restTransform = jointLocalTransform

        """
    def ComputeJointSkelTransforms(self, time: pxr.Usd.TimeCode | float | pxr.Sdf.TimeCode = ..., atRest: bool = ...) -> pxr.Vt.Matrix4dArray:
        """
        Compute joint transforms in skeleton space, at C{time}.


        This concatenates joint transforms as computed from
        ComputeJointLocalTransforms() . If C{atRest} is true, any bound
        animation source is ignored, and transforms are computed from the rest
        pose. The skeleton-space transforms of the rest pose are cached
        internally.
        """
    def ComputeJointWorldTransforms(self, time: pxr.UsdGeom.XformCache = ..., atRest: bool = ...) -> pxr.Vt.Matrix4dArray:
        """
        Compute joint transforms in world space, at whatever time is
        configured on C{xfCache}.


        This is equivalent to computing skel-space joint transforms with
        CmoputeJointSkelTransforms(), and then concatenating all transforms by
        the local-to-world transform of the Skeleton prim. If C{atRest} is
        true, any bound animation source is ignored, and transforms are
        computed from the rest pose.
        """
    def ComputeSkinningTransforms(self, time: pxr.Usd.TimeCode | float | pxr.Sdf.TimeCode = ...) -> pxr.Vt.Matrix4dArray:
        """
        Compute transforms representing the change in transformation of a
        joint from its rest pose, in skeleton space.


        I.e., ::

          inverse(bindTransform)*jointTransform

        These are the transforms usually required for skinning.
        """
    def GetAnimQuery(self) -> AnimQuery:
        """
        Returns the animation query that provides animation for the bound
        skeleton instance, if any.
        """
    def GetJointOrder(self) -> pxr.Vt.TokenArray:
        """
        Returns an array of joint paths, given as tokens, describing the order
        and parent-child relationships of joints in the skeleton.



        UsdSkelSkeleton::GetJointOrder
        """
    def GetJointWorldBindTransforms(self) -> pxr.Vt.Matrix4dArray:
        """
        Returns the world space joint transforms at bind time.
        """
    def GetMapper(self) -> AnimMapper:
        """
        Returns a mapper for remapping from the bound animation, if any, to
        the Skeleton.
        """
    def GetPrim(self) -> pxr.Usd.Prim:
        """
        Returns the underlying Skeleton primitive corresponding to the bound
        skeleton instance, if any.
        """
    def GetSkeleton(self) -> Skeleton:
        """
        Returns the bound skeleton instance, if any.
        """
    def GetTopology(self) -> Topology:
        """
        Returns the topology of the bound skeleton instance, if any.
        """
    def HasBindPose(self) -> bool:
        """
        Returns C{true} if the size of the array returned by
        skeleton::GetBindTransformsAttr() matches the number of joints in the
        skeleton.
        """
    def HasRestPose(self) -> bool:
        """
        Returns C{true} if the size of the array returned by
        skeleton::GetRestTransformsAttr() matches the number of joints in the
        skeleton.
        """
    def __bool__(self) -> bool:
        """
        Boolean conversion operator. Equivalent to IsValid() .
        """
    def __eq__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...

class SkinningQuery(Boost.Python.instance):
    """
    Object used for querying resolved bindings for skinning.
    """
    __instance_size__: ClassVar[int] = ...
    def __init__(self) -> None: ...
    @overload
    def ComputeExtentsPadding(self, skelRestXforms: SkinningQuery, boundable: pxr.Vt.Matrix4dArray | typing.Iterable[pxr.Gf.Matrix4d], time: pxr.UsdGeom.Boundable = ...) -> float: ...
    @overload
    def ComputeExtentsPadding(self, skelRestXforms: SkinningQuery, boundable: pxr.Vt.Matrix4fArray | typing.Iterable[pxr.Gf.Matrix4f], time: pxr.UsdGeom.Boundable = ...) -> float: ...
    def ComputeJointInfluences(self, time: pxr.Usd.TimeCode | float | pxr.Sdf.TimeCode = ...) -> tuple[pxr.Vt.IntArray, pxr.Vt.FloatArray]:
        """
        Convenience method for computing joint influences.


        In addition to querying influences, this will also perform validation
        of the basic form of the weight data  although the array contents is
        not validated.
        """
    @overload
    def ComputeSkinnedPoints(self, xforms: pxr.Vt.Matrix4fArray | typing.Iterable[pxr.Gf.Matrix4f], points: pxr.Vt.Vec3fArray | typing.Iterable[list[float]] | typing.Iterable[pxr.Gf.Vec3f] | typing.Iterable[tuple[float, float, float]], time: pxr.Usd.TimeCode | float | pxr.Sdf.TimeCode = ...) -> bool:
        """
        Compute skinned points using specified skinning method attr (fallback
        to linear blend skinning if not specified) Both C{xforms} and
        C{points} are given in *skeleton space*, using the joint order of the
        bound skeleton.


        Joint influences and the (optional) binding transform are computed at
        time C{time} (which will typically be unvarying).

        UsdSkelSkeletonQuery::ComputeSkinningTransforms
        """
    @overload
    def ComputeSkinnedPoints(self, xforms: pxr.Vt.Matrix4dArray | typing.Iterable[pxr.Gf.Matrix4d], points: pxr.Vt.Vec3fArray | typing.Iterable[list[float]] | typing.Iterable[pxr.Gf.Vec3f] | typing.Iterable[tuple[float, float, float]], time: pxr.Usd.TimeCode | float | pxr.Sdf.TimeCode = ...) -> bool: ...
    @overload
    def ComputeSkinnedTransform(self, xforms: pxr.Vt.Matrix4fArray | typing.Iterable[pxr.Gf.Matrix4f], time: pxr.Usd.TimeCode | float | pxr.Sdf.TimeCode = ...) -> pxr.Gf.Matrix4f:
        """
        Compute a skinning transform using specified skinning method attr
        (fallback to linear blend skinning if not specified) The C{xforms} are
        given in *skeleton space*, using the joint order of the bound
        skeleton.


        Joint influences and the (optional) binding transform are computed at
        time C{time} (which will typically be unvarying). If this skinning
        query holds non-constant joint influences, no transform will be
        computed, and the function will return false.

        UsdSkelSkeletonQuery::ComputeSkinningTransforms
        """
    @overload
    def ComputeSkinnedTransform(self, xforms: pxr.Vt.Matrix4dArray | typing.Iterable[pxr.Gf.Matrix4d], time: pxr.Usd.TimeCode | float | pxr.Sdf.TimeCode = ...) -> pxr.Gf.Matrix4d: ...
    def ComputeVaryingJointInfluences(self, numPoints: int, time: pxr.Usd.TimeCode | float | pxr.Sdf.TimeCode = ...) -> tuple[pxr.Vt.IntArray, pxr.Vt.FloatArray]:
        """
        Convenience method for computing joint influence, where constant
        influences are expanded to hold values per point.


        In addition to querying influences, this will also perform validation
        of the basic form of the weight data  although the array contents is
        not validated.
        """
    def GetBlendShapeMapper(self) -> AnimMapper:
        """
        Return the mapper for remapping blend shapes from the order of the
        bound SkelAnimation to the local blend shape order of this prim.


        Returns a null reference if the underlying prim has no blend shapes.
        The mapper maps data from the order given by the *blendShapes* order
        on the SkelAnimation to the order given by the *skel:blendShapes*
        property, as set through the UsdSkelBindingAPI.
        """
    def GetBlendShapeOrder(self) -> pxr.Vt.TokenArray:
        """
        Get the blend shapes for this skinning site, if any.
        """
    def GetBlendShapeTargetsRel(self) -> pxr.Usd.Relationship: ...
    def GetBlendShapesAttr(self) -> pxr.Usd.Attribute: ...
    def GetGeomBindTransform(self, time: pxr.Usd.TimeCode | float | pxr.Sdf.TimeCode = ...) -> pxr.Gf.Matrix4d: ...
    def GetGeomBindTransformAttr(self) -> pxr.Usd.Attribute: ...
    def GetInterpolation(self) -> str: ...
    def GetJointIndicesPrimvar(self) -> pxr.UsdGeom.Primvar: ...
    def GetJointMapper(self) -> AnimMapper:
        """
        Return a mapper for remapping from the joint order of the skeleton to
        the local joint order of this prim, if any.


        Returns a null pointer if the prim has no custom joint orer. The
        mapper maps data from the order given by the *joints* order on the
        Skeleton to the order given by the *skel:joints* property, as
        optionally set through the UsdSkelBindingAPI.
        """
    def GetJointOrder(self) -> pxr.Vt.TokenArray:
        """
        Get the custom joint order for this skinning site, if any.
        """
    def GetJointWeightsPrimvar(self) -> pxr.UsdGeom.Primvar: ...
    def GetMapper(self) -> AnimMapper:
        """
        Deprecated

        Use GetJointMapper.
        """
    def GetNumInfluencesPerComponent(self) -> int:
        """
        Returns the number of influences encoded for each component.


        If the prim defines rigid joint influences, then this returns the
        number of influences that map to every point. Otherwise, this provides
        the number of influences per point.

        IsRigidlyDeformed
        """
    def GetPrim(self) -> pxr.Usd.Prim: ...
    def GetSkinningMethod(self) -> str: ...
    def GetSkinningMethodAttr(self) -> pxr.Usd.Attribute: ...
    def GetTimeSamples(self) -> list[float]:
        """
        Populate C{times} with the union of time samples for all properties
        that affect skinning, independent of joint transforms and any other
        prim-specific properties (such as points).



        UsdAttribute::GetTimeSamples
        """
    def GetTimeSamplesInInterval(self, _interval: pxr.Gf.Interval, /) -> list[float]:
        """
        Populate C{times} with the union of time samples within C{interval},
        for all properties that affect skinning, independent of joint
        transforms and any other prim-specific properties (such as points).



        UsdAttribute::GetTimeSamplesInInterval
        """
    def HasBlendShapes(self) -> bool:
        """
        Returns true if there are blend shapes associated with this prim.
        """
    def HasJointInfluences(self) -> bool:
        """
        Returns true if joint influence data is associated with this prim.
        """
    def IsRigidlyDeformed(self) -> bool:
        """
        Returns true if the held prim has the same joint influences across all
        points, or false otherwise.
        """
    def __bool__(self) -> bool:
        """
        Boolean conversion operator. Equivalent to IsValid() .
        """

class Tokens(Boost.Python.instance):
    BlendShape: ClassVar[str] = ...  # read-only
    SkelAnimation: ClassVar[str] = ...  # read-only
    SkelBindingAPI: ClassVar[str] = ...  # read-only
    SkelRoot: ClassVar[str] = ...  # read-only
    Skeleton: ClassVar[str] = ...  # read-only
    bindTransforms: ClassVar[str] = ...  # read-only
    blendShapeWeights: ClassVar[str] = ...  # read-only
    blendShapes: ClassVar[str] = ...  # read-only
    classicLinear: ClassVar[str] = ...  # read-only
    dualQuaternion: ClassVar[str] = ...  # read-only
    jointNames: ClassVar[str] = ...  # read-only
    joints: ClassVar[str] = ...  # read-only
    normalOffsets: ClassVar[str] = ...  # read-only
    offsets: ClassVar[str] = ...  # read-only
    pointIndices: ClassVar[str] = ...  # read-only
    primvarsSkelGeomBindTransform: ClassVar[str] = ...  # read-only
    primvarsSkelJointIndices: ClassVar[str] = ...  # read-only
    primvarsSkelJointWeights: ClassVar[str] = ...  # read-only
    primvarsSkelSkinningMethod: ClassVar[str] = ...  # read-only
    restTransforms: ClassVar[str] = ...  # read-only
    rotations: ClassVar[str] = ...  # read-only
    scales: ClassVar[str] = ...  # read-only
    skelAnimationSource: ClassVar[str] = ...  # read-only
    skelBlendShapeTargets: ClassVar[str] = ...  # read-only
    skelBlendShapes: ClassVar[str] = ...  # read-only
    skelJoints: ClassVar[str] = ...  # read-only
    skelSkeleton: ClassVar[str] = ...  # read-only
    translations: ClassVar[str] = ...  # read-only
    weight: ClassVar[str] = ...  # read-only
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """

class Topology(Boost.Python.instance):
    """
    Object holding information describing skeleton topology.


    This provides the hierarchical information needed to reason about
    joint relationships in a manner suitable to computations.
    """
    @overload
    def __init__(self, _parentIndices: pxr.Vt.IntArray | typing.Iterable[int], /) -> None:
        """
        Construct a skel topology from an array of parent indices.


        For each joint, this provides the parent index of that joint, or -1 if
        none.
        """
    @overload
    def __init__(self, arg2: object, /) -> None: ...
    @overload
    def __init__(self, arg2: pxr.Vt.TokenArray | typing.Iterable[pxr.Ar.ResolvedPath] | typing.Iterable[str], /) -> None: ...
    def GetNumJoints(self) -> int: ...
    def GetParent(self, _index: int, /) -> int:
        """
        Returns the parent joint of the C{index'th} joint, Returns -1 for
        joints with no parent (roots).
        """
    def GetParentIndices(self) -> pxr.Vt.IntArray: ...
    def IsRoot(self, _index: int, /) -> bool:
        """
        Returns true if the C{index'th} joint is a root joint.
        """
    def Validate(self) -> tuple:
        """
        Validate the topology.


        If validation is unsuccessful, a reason why will be written to
        C{reason}, if provided.
        """
    def __len__(self) -> int: ...

class _CanApplyResult(Boost.Python.instance):
    __instance_size__: ClassVar[int] = ...
    def __init__(self, arg2: bool, arg3: object, /) -> None: ...
    def __bool__(self) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    def __getitem__(self, arg2: int, /) -> Any: ...
    def __ne__(self, other: object) -> bool: ...
    @property
    def whyNot(self): ...

def ApplyBlendShape(weight: float, offsets: pxr.Vt.Vec3fArray | typing.Iterable[list[float]] | typing.Iterable[pxr.Gf.Vec3f] | typing.Iterable[tuple[float, float, float]], indices: pxr.Vt.IntArray | typing.Iterable[int], points: pxr.Vt.Vec3fArray | typing.Iterable[list[float]] | typing.Iterable[pxr.Gf.Vec3f] | typing.Iterable[tuple[float, float, float]]) -> bool:
    """
    Apply a single blend shape to C{points}.


    The shape is given as a span of C{offsets}. If the C{indices} span is
    not empty, it provides the index into the C{points} span at which each
    offset should be mapped. Otherwise, the C{offsets} span must be the
    same size as the C{points} span.
    """
@overload
def BakeSkinning(root: Root, interval: pxr.Gf.Interval = ...) -> bool:
    """
    Overload of UsdSkelBakeSkinning, which bakes the effect of skinning
    prims directly into points and transforms, for all skels bound beneath
    C{root}, over C{interval}.


    Skinning is baked into the current edit target. The edit target is
    *not* saved during skinning: the caller should Save() or Export() the
    result.
    """
@overload
def BakeSkinning(range: pxr.Usd.PrimRange, interval: pxr.Gf.Interval = ...) -> bool:
    """
    Overload of UsdSkelBakeSkinning, which bakes the effect of skinning
    prims directly into points and transforms, for all SkelRoot prims in
    C{range}, over C{interval}.


    Skinning is baked into the current edit target. The edit target is
    *not* saved during skinning: the caller should Save() or Export() the
    result.
    """
@overload
def ComputeJointLocalTransforms(topology: Topology, xforms: pxr.Vt.Matrix4dArray | typing.Iterable[pxr.Gf.Matrix4d], inverseXforms: pxr.Vt.Matrix4dArray | typing.Iterable[pxr.Gf.Matrix4d], jointLocalXforms: pxr.Vt.Matrix4dArray | typing.Iterable[pxr.Gf.Matrix4d], rootInverseXform: pxr.Gf.Matrix4d = ...) -> bool:
    """
    This is an overloaded member function, provided for convenience. It
    differs from the above function only in what argument(s) it accepts.


    Deprecated

    Use form that takes TfSpan arguments.
    """
@overload
def ComputeJointLocalTransforms(topology: Topology, xforms: pxr.Vt.Matrix4dArray | typing.Iterable[pxr.Gf.Matrix4d], inverseXforms: pxr.Vt.Matrix4dArray | typing.Iterable[pxr.Gf.Matrix4d], rootInverseXform: pxr.Gf.Matrix4d = ...) -> pxr.Vt.Matrix4dArray:
    """
    This is an overloaded member function, provided for convenience. It
    differs from the above function only in what argument(s) it accepts.


    Deprecated

    Use form that takes TfSpan arguments.
    """
@overload
def ComputeJointLocalTransforms(topology: Topology, xforms: pxr.Vt.Matrix4dArray | typing.Iterable[pxr.Gf.Matrix4d], jointLocalXforms: pxr.Vt.Matrix4dArray | typing.Iterable[pxr.Gf.Matrix4d], rootInverseXform: pxr.Gf.Matrix4d = ...) -> bool: ...
@overload
def ComputeJointLocalTransforms(topology: Topology, xforms: pxr.Vt.Matrix4fArray | typing.Iterable[pxr.Gf.Matrix4f], inverseXforms: pxr.Vt.Matrix4fArray | typing.Iterable[pxr.Gf.Matrix4f], jointLocalXforms: pxr.Vt.Matrix4fArray | typing.Iterable[pxr.Gf.Matrix4f], rootInverseXform: pxr.Gf.Matrix4f = ...) -> bool: ...
@overload
def ComputeJointLocalTransforms(topology: Topology, xforms: pxr.Vt.Matrix4fArray | typing.Iterable[pxr.Gf.Matrix4f], jointLocalXforms: pxr.Vt.Matrix4fArray | typing.Iterable[pxr.Gf.Matrix4f], rootInverseXform: pxr.Gf.Matrix4f = ...) -> bool: ...
@overload
def ComputeJointLocalTransforms(topology: Topology, xforms: pxr.Vt.Matrix4dArray | typing.Iterable[pxr.Gf.Matrix4d], rootInverseXform: pxr.Gf.Matrix4d = ...) -> pxr.Vt.Matrix4dArray: ...
@overload
def ComputeJointsExtent(xforms: pxr.Vt.Matrix4dArray | typing.Iterable[pxr.Gf.Matrix4d], pad: float = ..., rootXform: pxr.Gf.Matrix4d = ...) -> pxr.Gf.Range3f: ...
@overload
def ComputeJointsExtent(xforms: pxr.Vt.Matrix4fArray | typing.Iterable[pxr.Gf.Matrix4f], pad: float = ..., rootXform: pxr.Gf.Matrix4f = ...) -> pxr.Gf.Range3f: ...
@overload
def ConcatJointTransforms(_topology: Topology, /, topology: pxr.Vt.Matrix4dArray | typing.Iterable[pxr.Gf.Matrix4d], jointLocalXforms: pxr.Vt.Matrix4dArray | typing.Iterable[pxr.Gf.Matrix4d], rootXform: pxr.Gf.Matrix4d = ...) -> bool:
    """
    This is an overloaded member function, provided for convenience. It
    differs from the above function only in what argument(s) it accepts.


    Deprecated

    Use the function form that takes TfSpan arguments.
    """
@overload
def ConcatJointTransforms(arg1: Topology, /, topology: pxr.Vt.Matrix4fArray | typing.Iterable[pxr.Gf.Matrix4f], jointLocalXforms: pxr.Vt.Matrix4fArray | typing.Iterable[pxr.Gf.Matrix4f], rootXform: pxr.Gf.Matrix4f = ...) -> bool: ...
@overload
def ConcatJointTransforms(topology: Topology, jointLocalXforms: pxr.Vt.Matrix4dArray | typing.Iterable[pxr.Gf.Matrix4d], rootXform: pxr.Gf.Matrix4d = ...) -> pxr.Vt.Matrix4dArray: ...
@overload
def DecomposeTransform(_xform: pxr.Gf.Matrix4d, /) -> tuple:
    """
    Decompose a transform into translate/rotate/scale components.


    The transform order for decomposition is scale, rotate, translate.
    """
@overload
def DecomposeTransform(_xform: pxr.Gf.Matrix4f, /) -> tuple:
    """
    This is an overloaded member function, provided for convenience. It
    differs from the above function only in what argument(s) it accepts.
    """
@overload
def DecomposeTransforms(_xforms: pxr.Vt.Matrix4dArray | typing.Iterable[pxr.Gf.Matrix4d], /) -> tuple:
    """
    This is an overloaded member function, provided for convenience. It
    differs from the above function only in what argument(s) it accepts.


    Deprecated

    Use form that takes TfSpan arguments.
    """
@overload
def DecomposeTransforms(_count: pxr.Vt.Matrix4fArray | typing.Iterable[pxr.Gf.Matrix4f], /) -> tuple:
    """
    This is an overloaded member function, provided for convenience. It
    differs from the above function only in what argument(s) it accepts.


    Deprecated

    Use form that takes TfSpan arguments.
    """
@overload
def ExpandConstantInfluencesToVarying(array: pxr.Vt.IntArray | typing.Iterable[int], size: int) -> bool:
    """
    Convert an array of constant influences (joint weights or indices) to
    an array of varying influences.


    The C{size} should match the size of required for'vertex'interpolation
    on the type geometry primitive. Typically, this is the number of
    points. This is a convenience function for clients that don't
    understand constant (rigid) weighting.
    """
@overload
def ExpandConstantInfluencesToVarying(array: pxr.Vt.FloatArray | typing.Iterable[float], size: int) -> bool:
    """
    This is an overloaded member function, provided for convenience. It
    differs from the above function only in what argument(s) it accepts.
    """
def InterleaveInfluences(indices: pxr.Vt.IntArray | typing.Iterable[int], weights: pxr.Vt.FloatArray | typing.Iterable[float], interleavedInfluences: pxr.Vt.Vec2fArray | typing.Iterable[list[float]] | typing.Iterable[pxr.Gf.Vec2f] | typing.Iterable[tuple[float, float]]) -> bool:
    """
    Combine arrays of joint indices and weights into interleaved
    (index,weight) vectors.
    """
def IsSkelAnimationPrim(prim: pxr.Usd.Prim) -> bool:
    """
    Returns true if C{prim} is a valid skel animation source.
    """
def IsSkinnablePrim(prim: pxr.Usd.Prim) -> bool:
    """
    Returns true if C{prim} is considered to be a skinnable primitive.


    Whether or not the prim is actually skinned additionally depends on
    whether or not the prim has a bound skeleton, and prop joint
    influences.
    """
def MakeTransform(translate: pxr.Gf.Vec3f | list[float] | tuple[float, float, float], rotate: pxr.Gf.Quatf | pxr.Gf.Quath, scale: pxr.Gf.Vec3h | list[float] | tuple[float, float, float]) -> pxr.Gf.Matrix4d:
    """
    This is an overloaded member function, provided for convenience. It
    differs from the above function only in what argument(s) it accepts.
    """
def MakeTransforms(translations: pxr.Vt.Vec3fArray | typing.Iterable[list[float]] | typing.Iterable[pxr.Gf.Vec3f] | typing.Iterable[tuple[float, float, float]], rotations: pxr.Vt.QuatfArray | typing.Iterable[pxr.Gf.Quatf] | typing.Iterable[pxr.Gf.Quath], scales: pxr.Vt.Vec3hArray | typing.Iterable[list[float]] | typing.Iterable[pxr.Gf.Vec3h] | typing.Iterable[tuple[float, float, float]]) -> pxr.Vt.Matrix4dArray:
    """
    This is an overloaded member function, provided for convenience. It
    differs from the above function only in what argument(s) it accepts.


    Deprecated

    Use form that takes TfSpan arguments.
    """
def NormalizeWeights(weights: pxr.Vt.FloatArray | typing.Iterable[float], numInfluencesPerComponent: int, eps: float = ...) -> bool:
    """
    Helper method to normalize weight values across each consecutive run
    of C{numInfluencesPerComponent} elements.


    If the total weight for a run of elements is smaller than C{eps}, the
    elements'weights are set to zero.
    """
@overload
def ResizeInfluences(array: pxr.Vt.IntArray | typing.Iterable[int], srcNumInfluencesPerComponent: int, newNumInfluencesPerComponent: int) -> bool:
    """
    Resize the number of influences per component in a weight or indices
    array, which initially has C{srcNumInfluencesPerComponent} influences
    to have no more than C{newNumInfluencesPerComponent} influences per
    component.


    If the size decreases, influences are additionally re-normalized. This
    is a convenience method for clients that require a fixed number of of
    influences.
    """
@overload
def ResizeInfluences(array: pxr.Vt.FloatArray | typing.Iterable[float], srcNumInfluencesPerComponent: int, newNumInfluencesPerComponent: int) -> bool:
    """
    This is an overloaded member function, provided for convenience. It
    differs from the above function only in what argument(s) it accepts.
    """
@overload
def SkinNormals(skinningMethod: str | pxr.Ar.ResolvedPath, geomBindTransform: pxr.Gf.Matrix3d, jointXforms: pxr.Vt.Matrix3dArray | typing.Iterable[pxr.Gf.Matrix3d], influences: pxr.Vt.Vec2fArray | typing.Iterable[list[float]] | typing.Iterable[pxr.Gf.Vec2f] | typing.Iterable[tuple[float, float]], numInfluencesPerPoint: int, normals: pxr.Vt.Vec3fArray | typing.Iterable[list[float]] | typing.Iterable[pxr.Gf.Vec3f] | typing.Iterable[tuple[float, float, float]], inSerial: bool = ...) -> bool:
    """
    This is an overloaded member function, provided for convenience. It
    differs from the above function only in what argument(s) it accepts.
    """
@overload
def SkinNormals(skinningMethod: str | pxr.Ar.ResolvedPath, geomBindTransform: pxr.Gf.Matrix3f, jointXforms: pxr.Vt.Matrix3fArray | typing.Iterable[pxr.Gf.Matrix3f], influences: pxr.Vt.Vec2fArray | typing.Iterable[list[float]] | typing.Iterable[pxr.Gf.Vec2f] | typing.Iterable[tuple[float, float]], numInfluencesPerPoint: int, normals: pxr.Vt.Vec3fArray | typing.Iterable[list[float]] | typing.Iterable[pxr.Gf.Vec3f] | typing.Iterable[tuple[float, float, float]], inSerial: bool = ...) -> bool:
    """
    This is an overloaded member function, provided for convenience. It
    differs from the above function only in what argument(s) it accepts.
    """
@overload
def SkinNormals(skinningMethod: str | pxr.Ar.ResolvedPath, geomBindTransform: pxr.Gf.Matrix3d, jointXforms: pxr.Vt.Matrix3dArray | typing.Iterable[pxr.Gf.Matrix3d], jointIndices: pxr.Vt.IntArray | typing.Iterable[int], jointWeights: pxr.Vt.FloatArray | typing.Iterable[float], numInfluencesPerPoint: int, normals: pxr.Vt.Vec3fArray | typing.Iterable[list[float]] | typing.Iterable[pxr.Gf.Vec3f] | typing.Iterable[tuple[float, float, float]], inSerial: bool = ...) -> bool:
    '''
    Skin normals using linear blend skinning (LBS) or dual quaternion
    skinning (DQS), for normals with *vertex* or *varying* interpolation.


    Use UsdSkelSkinFaceVaryingNormals() for normals with _faceVarying__
    interpolation. The C{jointXforms} are the *inverse transposes* of the
    3x3 component of the UsdSkel_Term_SkinningTransforms""skinning
    transforms", given in *skeleton space*. The C{geomBindTransform} is
    the *inverse transpose* of the matrix that transforms points from a
    bind pose ino the same *skeleton space* that the skinning tranforms
    were computed in.
    '''
@overload
def SkinNormals(skinningMethod: str | pxr.Ar.ResolvedPath, geomBindTransform: pxr.Gf.Matrix3f, jointXforms: pxr.Vt.Matrix3fArray | typing.Iterable[pxr.Gf.Matrix3f], jointIndices: pxr.Vt.IntArray | typing.Iterable[int], jointWeights: pxr.Vt.FloatArray | typing.Iterable[float], numInfluencesPerPoint: int, normals: pxr.Vt.Vec3fArray | typing.Iterable[list[float]] | typing.Iterable[pxr.Gf.Vec3f] | typing.Iterable[tuple[float, float, float]], inSerial: bool = ...) -> bool:
    """
    This is an overloaded member function, provided for convenience. It
    differs from the above function only in what argument(s) it accepts.
    """
@overload
def SkinNormalsLBS(geomBindTransform: pxr.Gf.Matrix3d, jointXforms: pxr.Vt.Matrix3dArray | typing.Iterable[pxr.Gf.Matrix3d], influences: pxr.Vt.Vec2fArray | typing.Iterable[list[float]] | typing.Iterable[pxr.Gf.Vec2f] | typing.Iterable[tuple[float, float]], numInfluencesPerPoint: int, normals: pxr.Vt.Vec3fArray | typing.Iterable[list[float]] | typing.Iterable[pxr.Gf.Vec3f] | typing.Iterable[tuple[float, float, float]], inSerial: bool = ...) -> bool:
    """
    This is an overloaded member function, provided for convenience. It
    differs from the above function only in what argument(s) it accepts.
    """
@overload
def SkinNormalsLBS(geomBindTransform: pxr.Gf.Matrix3f, jointXforms: pxr.Vt.Matrix3fArray | typing.Iterable[pxr.Gf.Matrix3f], influences: pxr.Vt.Vec2fArray | typing.Iterable[list[float]] | typing.Iterable[pxr.Gf.Vec2f] | typing.Iterable[tuple[float, float]], numInfluencesPerPoint: int, normals: pxr.Vt.Vec3fArray | typing.Iterable[list[float]] | typing.Iterable[pxr.Gf.Vec3f] | typing.Iterable[tuple[float, float, float]], inSerial: bool = ...) -> bool:
    """
    This is an overloaded member function, provided for convenience. It
    differs from the above function only in what argument(s) it accepts.
    """
@overload
def SkinNormalsLBS(geomBindTransform: pxr.Gf.Matrix3d, jointXforms: pxr.Vt.Matrix3dArray | typing.Iterable[pxr.Gf.Matrix3d], jointIndices: pxr.Vt.IntArray | typing.Iterable[int], jointWeights: pxr.Vt.FloatArray | typing.Iterable[float], numInfluencesPerPoint: int, normals: pxr.Vt.Vec3fArray | typing.Iterable[list[float]] | typing.Iterable[pxr.Gf.Vec3f] | typing.Iterable[tuple[float, float, float]], inSerial: bool = ...) -> bool: ...
@overload
def SkinNormalsLBS(geomBindTransform: pxr.Gf.Matrix3f, jointXforms: pxr.Vt.Matrix3fArray | typing.Iterable[pxr.Gf.Matrix3f], jointIndices: pxr.Vt.IntArray | typing.Iterable[int], jointWeights: pxr.Vt.FloatArray | typing.Iterable[float], numInfluencesPerPoint: int, normals: pxr.Vt.Vec3fArray | typing.Iterable[list[float]] | typing.Iterable[pxr.Gf.Vec3f] | typing.Iterable[tuple[float, float, float]], inSerial: bool = ...) -> bool:
    """
    This is an overloaded member function, provided for convenience. It
    differs from the above function only in what argument(s) it accepts.
    """
@overload
def SkinPoints(skinningMethod: object, geomBindTransform: pxr.Gf.Matrix4d, jointXforms: pxr.Vt.Matrix4dArray | typing.Iterable[pxr.Gf.Matrix4d], jointIndices: pxr.Vt.IntArray | typing.Iterable[int], jointWeights: pxr.Vt.FloatArray | typing.Iterable[float], numInfluencesPerPoint: int, points: pxr.Vt.Vec3fArray | typing.Iterable[list[float]] | typing.Iterable[pxr.Gf.Vec3f] | typing.Iterable[tuple[float, float, float]], inSerial: bool = ...) -> bool: ...
@overload
def SkinPoints(skinningMethod: object, geomBindTransform: pxr.Gf.Matrix4d, jointXforms: pxr.Vt.Matrix4dArray | typing.Iterable[pxr.Gf.Matrix4d], influences: pxr.Vt.Vec2fArray | typing.Iterable[list[float]] | typing.Iterable[pxr.Gf.Vec2f] | typing.Iterable[tuple[float, float]], numInfluencesPerPoint: int, points: pxr.Vt.Vec3fArray | typing.Iterable[list[float]] | typing.Iterable[pxr.Gf.Vec3f] | typing.Iterable[tuple[float, float, float]], inSerial: bool = ...) -> bool: ...
@overload
def SkinPoints(skinningMethod: object, geomBindTransform: pxr.Gf.Matrix4f, jointXforms: pxr.Vt.Matrix4fArray | typing.Iterable[pxr.Gf.Matrix4f], jointIndices: pxr.Vt.IntArray | typing.Iterable[int], jointWeights: pxr.Vt.FloatArray | typing.Iterable[float], numInfluencesPerPoint: int, points: pxr.Vt.Vec3fArray | typing.Iterable[list[float]] | typing.Iterable[pxr.Gf.Vec3f] | typing.Iterable[tuple[float, float, float]], inSerial: bool = ...) -> bool: ...
@overload
def SkinPoints(skinningMethod: object, geomBindTransform: pxr.Gf.Matrix4f, jointXforms: pxr.Vt.Matrix4fArray | typing.Iterable[pxr.Gf.Matrix4f], influences: pxr.Vt.Vec2fArray | typing.Iterable[list[float]] | typing.Iterable[pxr.Gf.Vec2f] | typing.Iterable[tuple[float, float]], numInfluencesPerPoint: int, points: pxr.Vt.Vec3fArray | typing.Iterable[list[float]] | typing.Iterable[pxr.Gf.Vec3f] | typing.Iterable[tuple[float, float, float]], inSerial: bool = ...) -> bool: ...
@overload
def SkinPointsLBS(geomBindTransform: pxr.Gf.Matrix4d, jointXforms: pxr.Vt.Matrix4dArray | typing.Iterable[pxr.Gf.Matrix4d], jointIndices: pxr.Vt.IntArray | typing.Iterable[int], jointWeights: pxr.Vt.FloatArray | typing.Iterable[float], numInfluencesPerPoint: int, points: pxr.Vt.Vec3fArray | typing.Iterable[list[float]] | typing.Iterable[pxr.Gf.Vec3f] | typing.Iterable[tuple[float, float, float]], inSerial: bool = ...) -> bool: ...
@overload
def SkinPointsLBS(geomBindTransform: pxr.Gf.Matrix4d, jointXforms: pxr.Vt.Matrix4dArray | typing.Iterable[pxr.Gf.Matrix4d], influences: pxr.Vt.Vec2fArray | typing.Iterable[list[float]] | typing.Iterable[pxr.Gf.Vec2f] | typing.Iterable[tuple[float, float]], numInfluencesPerPoint: int, points: pxr.Vt.Vec3fArray | typing.Iterable[list[float]] | typing.Iterable[pxr.Gf.Vec3f] | typing.Iterable[tuple[float, float, float]], inSerial: bool = ...) -> bool: ...
@overload
def SkinPointsLBS(geomBindTransform: pxr.Gf.Matrix4f, jointXforms: pxr.Vt.Matrix4fArray | typing.Iterable[pxr.Gf.Matrix4f], jointIndices: pxr.Vt.IntArray | typing.Iterable[int], jointWeights: pxr.Vt.FloatArray | typing.Iterable[float], numInfluencesPerPoint: int, points: pxr.Vt.Vec3fArray | typing.Iterable[list[float]] | typing.Iterable[pxr.Gf.Vec3f] | typing.Iterable[tuple[float, float, float]], inSerial: bool = ...) -> bool: ...
@overload
def SkinPointsLBS(geomBindTransform: pxr.Gf.Matrix4f, jointXforms: pxr.Vt.Matrix4fArray | typing.Iterable[pxr.Gf.Matrix4f], influences: pxr.Vt.Vec2fArray | typing.Iterable[list[float]] | typing.Iterable[pxr.Gf.Vec2f] | typing.Iterable[tuple[float, float]], numInfluencesPerPoint: int, points: pxr.Vt.Vec3fArray | typing.Iterable[list[float]] | typing.Iterable[pxr.Gf.Vec3f] | typing.Iterable[tuple[float, float, float]], inSerial: bool = ...) -> bool: ...
@overload
def SkinTransform(skinningMethod: object, geomBindTransform: pxr.Gf.Matrix4d, jointXforms: pxr.Vt.Matrix4dArray | typing.Iterable[pxr.Gf.Matrix4d], influences: pxr.Vt.Vec2fArray | typing.Iterable[list[float]] | typing.Iterable[pxr.Gf.Vec2f] | typing.Iterable[tuple[float, float]]) -> pxr.Gf.Matrix4d: ...
@overload
def SkinTransform(skinningMethod: object, geomBindTransform: pxr.Gf.Matrix4d, jointXforms: pxr.Vt.Matrix4dArray | typing.Iterable[pxr.Gf.Matrix4d], jointIndices: pxr.Vt.IntArray | typing.Iterable[int], jointWeights: pxr.Vt.FloatArray | typing.Iterable[float]) -> pxr.Gf.Matrix4d: ...
@overload
def SkinTransform(skinningMethod: object, geomBindTransform: pxr.Gf.Matrix4f, jointXforms: pxr.Vt.Matrix4fArray | typing.Iterable[pxr.Gf.Matrix4f], influences: pxr.Vt.Vec2fArray | typing.Iterable[list[float]] | typing.Iterable[pxr.Gf.Vec2f] | typing.Iterable[tuple[float, float]]) -> pxr.Gf.Matrix4f: ...
@overload
def SkinTransform(skinningMethod: object, geomBindTransform: pxr.Gf.Matrix4f, jointXforms: pxr.Vt.Matrix4fArray | typing.Iterable[pxr.Gf.Matrix4f], jointIndices: pxr.Vt.IntArray | typing.Iterable[int], jointWeights: pxr.Vt.FloatArray | typing.Iterable[float]) -> pxr.Gf.Matrix4f: ...
@overload
def SkinTransformLBS(geomBindTransform: pxr.Gf.Matrix4d, jointXforms: pxr.Vt.Matrix4dArray | typing.Iterable[pxr.Gf.Matrix4d], influences: pxr.Vt.Vec2fArray | typing.Iterable[list[float]] | typing.Iterable[pxr.Gf.Vec2f] | typing.Iterable[tuple[float, float]]) -> pxr.Gf.Matrix4d: ...
@overload
def SkinTransformLBS(geomBindTransform: pxr.Gf.Matrix4d, jointXforms: pxr.Vt.Matrix4dArray | typing.Iterable[pxr.Gf.Matrix4d], jointIndices: pxr.Vt.IntArray | typing.Iterable[int], jointWeights: pxr.Vt.FloatArray | typing.Iterable[float]) -> pxr.Gf.Matrix4d: ...
@overload
def SkinTransformLBS(geomBindTransform: pxr.Gf.Matrix4f, jointXforms: pxr.Vt.Matrix4fArray | typing.Iterable[pxr.Gf.Matrix4f], influences: pxr.Vt.Vec2fArray | typing.Iterable[list[float]] | typing.Iterable[pxr.Gf.Vec2f] | typing.Iterable[tuple[float, float]]) -> pxr.Gf.Matrix4f: ...
@overload
def SkinTransformLBS(geomBindTransform: pxr.Gf.Matrix4f, jointXforms: pxr.Vt.Matrix4fArray | typing.Iterable[pxr.Gf.Matrix4f], jointIndices: pxr.Vt.IntArray | typing.Iterable[int], jointWeights: pxr.Vt.FloatArray | typing.Iterable[float]) -> pxr.Gf.Matrix4f: ...
def SortInfluences(indices: pxr.Vt.IntArray | typing.Iterable[int], weights: pxr.Vt.FloatArray | typing.Iterable[float], numInfluencesPerComponent: int) -> bool:
    """
    This is an overloaded member function, provided for convenience. It
    differs from the above function only in what argument(s) it accepts.


    Deprecated

    Use form that takes TfSpan arguments.
    """
