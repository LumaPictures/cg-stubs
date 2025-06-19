# mypy: disable-error-code="misc, override, no-redef"

import Boost.Python
import pxr.Ar
import pxr.Sdf
import pxr.Tf
import pxr.Usd
import pxr.UsdGeom
from _typeshed import Incomplete
from typing import Any, ClassVar, overload

__MFB_FULL_PACKAGE_NAME: str

class ArticulationRootAPI(pxr.Usd.APISchemaBase):
    """
    PhysicsArticulationRootAPI can be applied to a scene graph node, and
    marks the subtree rooted here for inclusion in one or more reduced
    coordinate articulations.


    For floating articulations, this should be on the root body. For fixed
    articulations (robotics jargon for e.g. a robot arm for welding that
    is bolted to the floor), this API can be on a direct or indirect
    parent of the root joint which is connected to the world, or on the
    joint itself..
    """
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None:
        """
        Construct a UsdPhysicsArticulationRootAPI on UsdPrim C{prim}.


        Equivalent to UsdPhysicsArticulationRootAPI::Get (prim.GetStage(),
        prim.GetPath()) for a *valid* C{prim}, but will not immediately throw
        an error for an invalid C{prim}
        """
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None:
        """
        Construct a UsdPhysicsArticulationRootAPI on the prim held by
        C{schemaObj}.


        Should be preferred over UsdPhysicsArticulationRootAPI
        (schemaObj.GetPrim()), as it preserves SchemaBase state.
        """
    @staticmethod
    def Apply(prim: pxr.Usd.Prim) -> ArticulationRootAPI:
        '''
        Applies this B{single-apply} API schema to the given C{prim}.


        This information is stored by adding"PhysicsArticulationRootAPI"to the
        token-valued, listOp metadata *apiSchemas* on the prim.

        A valid UsdPhysicsArticulationRootAPI object is returned upon success.
        An invalid (or empty) UsdPhysicsArticulationRootAPI object is returned
        upon failure. See UsdPrim::ApplyAPI() for conditions resulting in
        failure.

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
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> ArticulationRootAPI:
        """
        Return a UsdPhysicsArticulationRootAPI holding the prim adhering to
        this schema at C{path} on C{stage}.


        If no prim exists at C{path} on C{stage}, or if the prim at that path
        does not adhere to this schema, return an invalid schema object. This
        is shorthand for the following: ::

          UsdPhysicsArticulationRootAPI(stage->GetPrimAtPath(path));

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

class CollisionAPI(pxr.Usd.APISchemaBase):
    """
    Applies collision attributes to a UsdGeomXformable prim.


    If a simulation is running, this geometry will collide with other
    geometries that have PhysicsCollisionAPI applied. If a prim in the
    parent hierarchy has the RigidBodyAPI applied, this collider is a part
    of that body. If there is no body in the parent hierarchy, this
    collider is considered to be static.
    """
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None:
        """
        Construct a UsdPhysicsCollisionAPI on UsdPrim C{prim}.


        Equivalent to UsdPhysicsCollisionAPI::Get (prim.GetStage(),
        prim.GetPath()) for a *valid* C{prim}, but will not immediately throw
        an error for an invalid C{prim}
        """
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None:
        """
        Construct a UsdPhysicsCollisionAPI on the prim held by C{schemaObj}.


        Should be preferred over UsdPhysicsCollisionAPI (schemaObj.GetPrim()),
        as it preserves SchemaBase state.
        """
    @staticmethod
    def Apply(prim: pxr.Usd.Prim) -> CollisionAPI:
        '''
        Applies this B{single-apply} API schema to the given C{prim}.


        This information is stored by adding"PhysicsCollisionAPI"to the token-
        valued, listOp metadata *apiSchemas* on the prim.

        A valid UsdPhysicsCollisionAPI object is returned upon success. An
        invalid (or empty) UsdPhysicsCollisionAPI object is returned upon
        failure. See UsdPrim::ApplyAPI() for conditions resulting in failure.

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
    def CreateCollisionEnabledAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetCollisionEnabledAttr() , and also Create vs Get Property
        Methods for when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateSimulationOwnerRel(self) -> pxr.Usd.Relationship:
        """
        See GetSimulationOwnerRel() , and also Create vs Get Property Methods
        for when to use Get vs Create.
        """
    @staticmethod
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> CollisionAPI:
        """
        Return a UsdPhysicsCollisionAPI holding the prim adhering to this
        schema at C{path} on C{stage}.


        If no prim exists at C{path} on C{stage}, or if the prim at that path
        does not adhere to this schema, return an invalid schema object. This
        is shorthand for the following: ::

          UsdPhysicsCollisionAPI(stage->GetPrimAtPath(path));

        """
    def GetCollisionEnabledAttr(self) -> pxr.Usd.Attribute:
        """
        Determines if the PhysicsCollisionAPI is enabled.



        Declaration

        C{bool physics:collisionEnabled = 1}

        C++ Type

        bool

        Usd Type

        SdfValueTypeNames->Bool
        """
    @staticmethod
    def GetSchemaAttributeNames(includeInherited: bool = ...) -> list[str]:
        """
        Return a vector of names of all pre-declared attributes for this
        schema class and all its ancestor classes.


        Does not include attributes that may be authored by custom/extended
        methods of the schemas involved.
        """
    def GetSimulationOwnerRel(self) -> pxr.Usd.Relationship:
        """
        Single PhysicsScene that will simulate this collider.


        By default this object belongs to the first PhysicsScene. Note that if
        a RigidBodyAPI in the hierarchy above has a different simulationOwner
        then it has a precedence over this relationship.
        """
    @staticmethod
    def _GetStaticTfType() -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...

class CollisionGroup(pxr.Usd.Typed):
    """
    Defines a collision group for coarse filtering.


    When a collision occurs between two objects that have a
    PhysicsCollisionGroup assigned, they will collide with each other
    unless this PhysicsCollisionGroup pair is filtered. See filteredGroups
    attribute.

    A CollectionAPI:colliders maintains a list of PhysicsCollisionAPI
    rel-s that defines the members of this Collisiongroup.
    """
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None:
        """
        Construct a UsdPhysicsCollisionGroup on UsdPrim C{prim}.


        Equivalent to UsdPhysicsCollisionGroup::Get (prim.GetStage(),
        prim.GetPath()) for a *valid* C{prim}, but will not immediately throw
        an error for an invalid C{prim}
        """
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None:
        """
        Construct a UsdPhysicsCollisionGroup on the prim held by C{schemaObj}.


        Should be preferred over UsdPhysicsCollisionGroup
        (schemaObj.GetPrim()), as it preserves SchemaBase state.
        """
    @staticmethod
    def ComputeCollisionGroupTable(stage: pxr.Usd.Stage) -> CollisionGroupTable:
        """
        Compute a table encoding all the collision groups filter rules for a
        stage.


        This can be used as a reference to validate an implementation of the
        collision groups filters. The returned table is diagonally symmetric.
        """
    def CreateFilteredGroupsRel(self) -> pxr.Usd.Relationship:
        """
        See GetFilteredGroupsRel() , and also Create vs Get Property Methods
        for when to use Get vs Create.
        """
    def CreateInvertFilteredGroupsAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetInvertFilteredGroupsAttr() , and also Create vs Get Property
        Methods for when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateMergeGroupNameAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetMergeGroupNameAttr() , and also Create vs Get Property Methods
        for when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    @staticmethod
    def Define(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> CollisionGroup:
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
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> CollisionGroup:
        """
        Return a UsdPhysicsCollisionGroup holding the prim adhering to this
        schema at C{path} on C{stage}.


        If no prim exists at C{path} on C{stage}, or if the prim at that path
        does not adhere to this schema, return an invalid schema object. This
        is shorthand for the following: ::

          UsdPhysicsCollisionGroup(stage->GetPrimAtPath(path));

        """
    def GetCollidersCollectionAPI(self) -> pxr.Usd.CollectionAPI:
        """
        Return the UsdCollectionAPI interface used for defining what colliders
        belong to the CollisionGroup.
        """
    def GetFilteredGroupsRel(self) -> pxr.Usd.Relationship:
        """
        References a list of PhysicsCollisionGroups with which collisions
        should be ignored.
        """
    def GetInvertFilteredGroupsAttr(self) -> pxr.Usd.Attribute:
        """
        Normally, the filter will disable collisions against the selected
        filter groups.


        However, if this option is set, the filter will disable collisions
        against all colliders except for those in the selected filter groups.

        Declaration

        C{bool physics:invertFilteredGroups}

        C++ Type

        bool

        Usd Type

        SdfValueTypeNames->Bool
        """
    def GetMergeGroupNameAttr(self) -> pxr.Usd.Attribute:
        """
        If non-empty, any collision groups in a stage with a matching
        mergeGroup should be considered to refer to the same collection.


        Matching collision groups should behave as if there were a single
        group containing referenced colliders and filter groups from both
        collections.

        Declaration

        C{string physics:mergeGroup}

        C++ Type

        std::string

        Usd Type

        SdfValueTypeNames->String
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

class CollisionGroupTable(Boost.Python.instance):
    __instance_size__: ClassVar[int] = ...
    def __init__(self) -> None: ...
    def GetGroups(self) -> list: ...
    def IsCollisionEnabled(self, arg2: object, arg3: object, /) -> bool: ...

class DistanceJoint(Joint):
    """
    Predefined distance joint type (Distance between rigid bodies may be
    limited to given minimum or maximum distance.)
    """
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None:
        """
        Construct a UsdPhysicsDistanceJoint on UsdPrim C{prim}.


        Equivalent to UsdPhysicsDistanceJoint::Get (prim.GetStage(),
        prim.GetPath()) for a *valid* C{prim}, but will not immediately throw
        an error for an invalid C{prim}
        """
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None:
        """
        Construct a UsdPhysicsDistanceJoint on the prim held by C{schemaObj}.


        Should be preferred over UsdPhysicsDistanceJoint
        (schemaObj.GetPrim()), as it preserves SchemaBase state.
        """
    def CreateMaxDistanceAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetMaxDistanceAttr() , and also Create vs Get Property Methods for
        when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateMinDistanceAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetMinDistanceAttr() , and also Create vs Get Property Methods for
        when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    @staticmethod
    def Define(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> DistanceJoint:
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
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> DistanceJoint:
        """
        Return a UsdPhysicsDistanceJoint holding the prim adhering to this
        schema at C{path} on C{stage}.


        If no prim exists at C{path} on C{stage}, or if the prim at that path
        does not adhere to this schema, return an invalid schema object. This
        is shorthand for the following: ::

          UsdPhysicsDistanceJoint(stage->GetPrimAtPath(path));

        """
    def GetMaxDistanceAttr(self) -> pxr.Usd.Attribute:
        """
        Maximum distance.


        If attribute is negative, the joint is not limited. Units: distance.

        Declaration

        C{float physics:maxDistance = -1}

        C++ Type

        float

        Usd Type

        SdfValueTypeNames->Float
        """
    def GetMinDistanceAttr(self) -> pxr.Usd.Attribute:
        """
        Minimum distance.


        If attribute is negative, the joint is not limited. Units: distance.

        Declaration

        C{float physics:minDistance = -1}

        C++ Type

        float

        Usd Type

        SdfValueTypeNames->Float
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

class DriveAPI(pxr.Usd.APISchemaBase):
    '''
    The PhysicsDriveAPI when applied to any joint primitive will drive the
    joint towards a given target.


    The PhysicsDriveAPI is a multipleApply schema: drive can be set per
    axis"transX","transY","transZ","rotX","rotY","rotZ"or its"linear"for
    prismatic joint or"angular"for revolute joints. Setting these as a
    multipleApply schema TfToken name will define the degree of freedom
    the DriveAPI is applied to. Each drive is an implicit force-limited
    damped spring: Force or acceleration = stiffness * (targetPosition -
    position)
       - damping * (targetVelocity - velocity)

    For any described attribute *Fallback* *Value* or *Allowed* *Values*
    below that are text/tokens, the actual token is published and defined
    in UsdPhysicsTokens. So to set an attribute to the value"rightHanded",
    use UsdPhysicsTokens->rightHanded as the value.
    '''
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim, name: str | pxr.Ar.ResolvedPath) -> None:
        '''
        Construct a UsdPhysicsDriveAPI on UsdPrim C{prim} with name C{name}.


        Equivalent to UsdPhysicsDriveAPI::Get ( prim.GetStage(),
        prim.GetPath().AppendProperty("drive:name"));

        for a *valid* C{prim}, but will not immediately throw an error for an
        invalid C{prim}
        '''
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase, name: str | pxr.Ar.ResolvedPath) -> None:
        """
        Construct a UsdPhysicsDriveAPI on the prim held by C{schemaObj} with
        name C{name}.


        Should be preferred over UsdPhysicsDriveAPI (schemaObj.GetPrim(),
        name), as it preserves SchemaBase state.
        """
    @overload
    def __init__(self) -> None: ...
    @staticmethod
    def Apply(prim: pxr.Usd.Prim, name: str | pxr.Ar.ResolvedPath) -> DriveAPI:
        '''
        Applies this B{multiple-apply} API schema to the given C{prim} along
        with the given instance name, C{name}.


        This information is stored by adding"PhysicsDriveAPI:<i>name</i>"to
        the token-valued, listOp metadata *apiSchemas* on the prim. For
        example, if C{name} is\'instance1\', the
        token\'PhysicsDriveAPI:instance1\'is added to\'apiSchemas\'.

        A valid UsdPhysicsDriveAPI object is returned upon success. An invalid
        (or empty) UsdPhysicsDriveAPI object is returned upon failure. See
        UsdPrim::ApplyAPI() for conditions resulting in failure.

        UsdPrim::GetAppliedSchemas()

        UsdPrim::HasAPI()

        UsdPrim::CanApplyAPI()

        UsdPrim::ApplyAPI()

        UsdPrim::RemoveAPI()
        '''
    @staticmethod
    def CanApply(prim: pxr.Usd.Prim, name: str | pxr.Ar.ResolvedPath) -> _CanApplyResult:
        """
        Returns true if this B{multiple-apply} API schema can be applied, with
        the given instance name, C{name}, to the given C{prim}.


        If this schema can not be a applied the prim, this returns false and,
        if provided, populates C{whyNot} with the reason it can not be
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
    def CreateDampingAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetDampingAttr() , and also Create vs Get Property Methods for
        when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateMaxForceAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetMaxForceAttr() , and also Create vs Get Property Methods for
        when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateStiffnessAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetStiffnessAttr() , and also Create vs Get Property Methods for
        when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateTargetPositionAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetTargetPositionAttr() , and also Create vs Get Property Methods
        for when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateTargetVelocityAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetTargetVelocityAttr() , and also Create vs Get Property Methods
        for when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateTypeAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetTypeAttr() , and also Create vs Get Property Methods for when
        to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    @overload
    @staticmethod
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> DriveAPI:
        """
        Return a UsdPhysicsDriveAPI holding the prim adhering to this schema
        at C{path} on C{stage}.


        If no prim exists at C{path} on C{stage}, or if the prim at that path
        does not adhere to this schema, return an invalid schema object.
        C{path} must be of the format<path>.drive:name.

        This is shorthand for the following: ::

          TfToken name = SdfPath::StripNamespace(path.GetToken());
          UsdPhysicsDriveAPI(
              stage->GetPrimAtPath(path.GetPrimPath()), name);

        """
    @overload
    @staticmethod
    def Get(prim: pxr.Usd.Prim, name: str | pxr.Ar.ResolvedPath) -> DriveAPI:
        """
        Return a UsdPhysicsDriveAPI with name C{name} holding the prim
        C{prim}.


        Shorthand for UsdPhysicsDriveAPI(prim, name);
        """
    @staticmethod
    def GetAll(prim: pxr.Usd.Prim) -> list[DriveAPI]:
        """
        Return a vector of all named instances of UsdPhysicsDriveAPI on the
        given C{prim}.
        """
    def GetDampingAttr(self) -> pxr.Usd.Attribute:
        """
        Damping of the drive.


        Units: if linear drive: mass/second If angular drive:
        mass*DIST_UNITS*DIST_UNITS/second/degrees.

        Declaration

        C{float physics:damping = 0}

        C++ Type

        float

        Usd Type

        SdfValueTypeNames->Float
        """
    def GetMaxForceAttr(self) -> pxr.Usd.Attribute:
        """
        Maximum force that can be applied to drive.


        Units: if linear drive: mass*DIST_UNITS/second/second if angular
        drive: mass*DIST_UNITS*DIST_UNITS/second/second inf means not limited.
        Must be non-negative.

        Declaration

        C{float physics:maxForce = inf}

        C++ Type

        float

        Usd Type

        SdfValueTypeNames->Float
        """
    @overload
    @staticmethod
    def GetSchemaAttributeNames(includeInherited: bool = ...) -> list[str]:
        """
        Return a vector of names of all pre-declared attributes for this
        schema class and all its ancestor classes.


        Does not include attributes that may be authored by custom/extended
        methods of the schemas involved.
        """
    @overload
    @staticmethod
    def GetSchemaAttributeNames(_includeInherited: bool, /, includeInherited: str | pxr.Ar.ResolvedPath) -> list[str]:
        """
        Return a vector of names of all pre-declared attributes for this
        schema class and all its ancestor classes for a given instance name.


        Does not include attributes that may be authored by custom/extended
        methods of the schemas involved. The names returned will have the
        proper namespace prefix.
        """
    def GetStiffnessAttr(self) -> pxr.Usd.Attribute:
        """
        Stiffness of the drive.


        Units: if linear drive: mass/second/second if angular drive:
        mass*DIST_UNITS*DIST_UNITS/degrees/second/second.

        Declaration

        C{float physics:stiffness = 0}

        C++ Type

        float

        Usd Type

        SdfValueTypeNames->Float
        """
    def GetTargetPositionAttr(self) -> pxr.Usd.Attribute:
        """
        Target value for position.


        Units: if linear drive: distance if angular drive: degrees.

        Declaration

        C{float physics:targetPosition = 0}

        C++ Type

        float

        Usd Type

        SdfValueTypeNames->Float
        """
    def GetTargetVelocityAttr(self) -> pxr.Usd.Attribute:
        """
        Target value for velocity.


        Units: if linear drive: distance/second if angular drive:
        degrees/second.

        Declaration

        C{float physics:targetVelocity = 0}

        C++ Type

        float

        Usd Type

        SdfValueTypeNames->Float
        """
    def GetTypeAttr(self) -> pxr.Usd.Attribute:
        '''
        Drive spring is for the acceleration at the joint (rather than the
        force).



        Declaration

        C{uniform token physics:type ="force"}

        C++ Type

        TfToken

        Usd Type

        SdfValueTypeNames->Token

        Variability

        SdfVariabilityUniform

        Allowed Values

        force, acceleration
        '''
    @staticmethod
    def IsPhysicsDriveAPIPath(_path: pxr.Sdf.Path | str, /) -> bool:
        """
        Checks if the given path C{path} is of an API schema of type
        PhysicsDriveAPI.


        If so, it stores the instance name of the schema in C{name} and
        returns true. Otherwise, it returns false.
        """
    @staticmethod
    def _GetStaticTfType() -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...

class FilteredPairsAPI(pxr.Usd.APISchemaBase):
    '''
    API to describe fine-grained filtering.


    If a collision between two objects occurs, this pair might be filtered
    if the pair is defined through this API. This API can be applied
    either to a body or collision or even articulation.
    The"filteredPairs"defines what objects it should not collide against.
    Note that FilteredPairsAPI filtering has precedence over
    CollisionGroup filtering.
    '''
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None:
        """
        Construct a UsdPhysicsFilteredPairsAPI on UsdPrim C{prim}.


        Equivalent to UsdPhysicsFilteredPairsAPI::Get (prim.GetStage(),
        prim.GetPath()) for a *valid* C{prim}, but will not immediately throw
        an error for an invalid C{prim}
        """
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None:
        """
        Construct a UsdPhysicsFilteredPairsAPI on the prim held by
        C{schemaObj}.


        Should be preferred over UsdPhysicsFilteredPairsAPI
        (schemaObj.GetPrim()), as it preserves SchemaBase state.
        """
    @staticmethod
    def Apply(prim: pxr.Usd.Prim) -> FilteredPairsAPI:
        '''
        Applies this B{single-apply} API schema to the given C{prim}.


        This information is stored by adding"PhysicsFilteredPairsAPI"to the
        token-valued, listOp metadata *apiSchemas* on the prim.

        A valid UsdPhysicsFilteredPairsAPI object is returned upon success. An
        invalid (or empty) UsdPhysicsFilteredPairsAPI object is returned upon
        failure. See UsdPrim::ApplyAPI() for conditions resulting in failure.

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
    def CreateFilteredPairsRel(self) -> pxr.Usd.Relationship:
        """
        See GetFilteredPairsRel() , and also Create vs Get Property Methods
        for when to use Get vs Create.
        """
    @staticmethod
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> FilteredPairsAPI:
        """
        Return a UsdPhysicsFilteredPairsAPI holding the prim adhering to this
        schema at C{path} on C{stage}.


        If no prim exists at C{path} on C{stage}, or if the prim at that path
        does not adhere to this schema, return an invalid schema object. This
        is shorthand for the following: ::

          UsdPhysicsFilteredPairsAPI(stage->GetPrimAtPath(path));

        """
    def GetFilteredPairsRel(self) -> pxr.Usd.Relationship:
        """
        Relationship to objects that should be filtered.
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

class FixedJoint(Joint):
    """
    Predefined fixed joint type (All degrees of freedom are removed.)
    """
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None:
        """
        Construct a UsdPhysicsFixedJoint on UsdPrim C{prim}.


        Equivalent to UsdPhysicsFixedJoint::Get (prim.GetStage(),
        prim.GetPath()) for a *valid* C{prim}, but will not immediately throw
        an error for an invalid C{prim}
        """
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None:
        """
        Construct a UsdPhysicsFixedJoint on the prim held by C{schemaObj}.


        Should be preferred over UsdPhysicsFixedJoint (schemaObj.GetPrim()),
        as it preserves SchemaBase state.
        """
    @staticmethod
    def Define(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> FixedJoint:
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
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> FixedJoint:
        """
        Return a UsdPhysicsFixedJoint holding the prim adhering to this schema
        at C{path} on C{stage}.


        If no prim exists at C{path} on C{stage}, or if the prim at that path
        does not adhere to this schema, return an invalid schema object. This
        is shorthand for the following: ::

          UsdPhysicsFixedJoint(stage->GetPrimAtPath(path));

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

class Joint(pxr.UsdGeom.Imageable):
    """
    A joint constrains the movement of rigid bodies.


    Joint can be created between two rigid bodies or between one rigid
    body and world. By default joint primitive defines a D6 joint where
    all degrees of freedom are free. Three linear and three angular
    degrees of freedom. Note that default behavior is to disable collision
    between jointed bodies.
    """
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None:
        """
        Construct a UsdPhysicsJoint on UsdPrim C{prim}.


        Equivalent to UsdPhysicsJoint::Get (prim.GetStage(), prim.GetPath())
        for a *valid* C{prim}, but will not immediately throw an error for an
        invalid C{prim}
        """
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None:
        """
        Construct a UsdPhysicsJoint on the prim held by C{schemaObj}.


        Should be preferred over UsdPhysicsJoint (schemaObj.GetPrim()), as it
        preserves SchemaBase state.
        """
    def CreateBody0Rel(self) -> pxr.Usd.Relationship:
        """
        See GetBody0Rel() , and also Create vs Get Property Methods for when
        to use Get vs Create.
        """
    def CreateBody1Rel(self) -> pxr.Usd.Relationship:
        """
        See GetBody1Rel() , and also Create vs Get Property Methods for when
        to use Get vs Create.
        """
    def CreateBreakForceAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetBreakForceAttr() , and also Create vs Get Property Methods for
        when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateBreakTorqueAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetBreakTorqueAttr() , and also Create vs Get Property Methods for
        when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateCollisionEnabledAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetCollisionEnabledAttr() , and also Create vs Get Property
        Methods for when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateExcludeFromArticulationAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetExcludeFromArticulationAttr() , and also Create vs Get Property
        Methods for when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateJointEnabledAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetJointEnabledAttr() , and also Create vs Get Property Methods
        for when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateLocalPos0Attr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetLocalPos0Attr() , and also Create vs Get Property Methods for
        when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateLocalPos1Attr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetLocalPos1Attr() , and also Create vs Get Property Methods for
        when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateLocalRot0Attr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetLocalRot0Attr() , and also Create vs Get Property Methods for
        when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateLocalRot1Attr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetLocalRot1Attr() , and also Create vs Get Property Methods for
        when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    @staticmethod
    def Define(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> Joint:
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
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> Joint:
        """
        Return a UsdPhysicsJoint holding the prim adhering to this schema at
        C{path} on C{stage}.


        If no prim exists at C{path} on C{stage}, or if the prim at that path
        does not adhere to this schema, return an invalid schema object. This
        is shorthand for the following: ::

          UsdPhysicsJoint(stage->GetPrimAtPath(path));

        """
    def GetBody0Rel(self) -> pxr.Usd.Relationship:
        """
        Relationship to any UsdGeomXformable.
        """
    def GetBody1Rel(self) -> pxr.Usd.Relationship:
        """
        Relationship to any UsdGeomXformable.
        """
    def GetBreakForceAttr(self) -> pxr.Usd.Attribute:
        """
        Joint break force.


        If set, joint is to break when this force limit is reached. (Used for
        linear DOFs.) Units: mass * distance / second / second

        Declaration

        C{float physics:breakForce = inf}

        C++ Type

        float

        Usd Type

        SdfValueTypeNames->Float
        """
    def GetBreakTorqueAttr(self) -> pxr.Usd.Attribute:
        """
        Joint break torque.


        If set, joint is to break when this torque limit is reached. (Used for
        angular DOFs.) Units: mass * distance * distance / second / second

        Declaration

        C{float physics:breakTorque = inf}

        C++ Type

        float

        Usd Type

        SdfValueTypeNames->Float
        """
    def GetCollisionEnabledAttr(self) -> pxr.Usd.Attribute:
        """
        Determines if the jointed subtrees should collide or not.



        Declaration

        C{bool physics:collisionEnabled = 0}

        C++ Type

        bool

        Usd Type

        SdfValueTypeNames->Bool
        """
    def GetExcludeFromArticulationAttr(self) -> pxr.Usd.Attribute:
        """
        Determines if the joint can be included in an Articulation.



        Declaration

        C{uniform bool physics:excludeFromArticulation = 0}

        C++ Type

        bool

        Usd Type

        SdfValueTypeNames->Bool

        Variability

        SdfVariabilityUniform
        """
    def GetJointEnabledAttr(self) -> pxr.Usd.Attribute:
        """
        Determines if the joint is enabled.



        Declaration

        C{bool physics:jointEnabled = 1}

        C++ Type

        bool

        Usd Type

        SdfValueTypeNames->Bool
        """
    def GetLocalPos0Attr(self) -> pxr.Usd.Attribute:
        """
        Relative position of the joint frame to body0's frame.



        Declaration

        C{point3f physics:localPos0 = (0, 0, 0)}

        C++ Type

        GfVec3f

        Usd Type

        SdfValueTypeNames->Point3f
        """
    def GetLocalPos1Attr(self) -> pxr.Usd.Attribute:
        """
        Relative position of the joint frame to body1's frame.



        Declaration

        C{point3f physics:localPos1 = (0, 0, 0)}

        C++ Type

        GfVec3f

        Usd Type

        SdfValueTypeNames->Point3f
        """
    def GetLocalRot0Attr(self) -> pxr.Usd.Attribute:
        """
        Relative orientation of the joint frame to body0's frame.



        Declaration

        C{quatf physics:localRot0 = (1, 0, 0, 0)}

        C++ Type

        GfQuatf

        Usd Type

        SdfValueTypeNames->Quatf
        """
    def GetLocalRot1Attr(self) -> pxr.Usd.Attribute:
        """
        Relative orientation of the joint frame to body1's frame.



        Declaration

        C{quatf physics:localRot1 = (1, 0, 0, 0)}

        C++ Type

        GfQuatf

        Usd Type

        SdfValueTypeNames->Quatf
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

class LimitAPI(pxr.Usd.APISchemaBase):
    '''
    The PhysicsLimitAPI can be applied to a PhysicsJoint and will restrict
    the movement along an axis.


    PhysicsLimitAPI is a multipleApply schema: The PhysicsJoint can be
    restricted
    along"transX","transY","transZ","rotX","rotY","rotZ","distance".
    Setting these as a multipleApply schema TfToken name will define the
    degree of freedom the PhysicsLimitAPI is applied to. Note that if the
    low limit is higher than the high limit, motion along this axis is
    considered locked.
    '''
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim, name: str | pxr.Ar.ResolvedPath) -> None:
        '''
        Construct a UsdPhysicsLimitAPI on UsdPrim C{prim} with name C{name}.


        Equivalent to UsdPhysicsLimitAPI::Get ( prim.GetStage(),
        prim.GetPath().AppendProperty("limit:name"));

        for a *valid* C{prim}, but will not immediately throw an error for an
        invalid C{prim}
        '''
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase, name: str | pxr.Ar.ResolvedPath) -> None:
        """
        Construct a UsdPhysicsLimitAPI on the prim held by C{schemaObj} with
        name C{name}.


        Should be preferred over UsdPhysicsLimitAPI (schemaObj.GetPrim(),
        name), as it preserves SchemaBase state.
        """
    @overload
    def __init__(self) -> None: ...
    @staticmethod
    def Apply(prim: pxr.Usd.Prim, name: str | pxr.Ar.ResolvedPath) -> LimitAPI:
        '''
        Applies this B{multiple-apply} API schema to the given C{prim} along
        with the given instance name, C{name}.


        This information is stored by adding"PhysicsLimitAPI:<i>name</i>"to
        the token-valued, listOp metadata *apiSchemas* on the prim. For
        example, if C{name} is\'instance1\', the
        token\'PhysicsLimitAPI:instance1\'is added to\'apiSchemas\'.

        A valid UsdPhysicsLimitAPI object is returned upon success. An invalid
        (or empty) UsdPhysicsLimitAPI object is returned upon failure. See
        UsdPrim::ApplyAPI() for conditions resulting in failure.

        UsdPrim::GetAppliedSchemas()

        UsdPrim::HasAPI()

        UsdPrim::CanApplyAPI()

        UsdPrim::ApplyAPI()

        UsdPrim::RemoveAPI()
        '''
    @staticmethod
    def CanApply(prim: pxr.Usd.Prim, name: str | pxr.Ar.ResolvedPath) -> _CanApplyResult:
        """
        Returns true if this B{multiple-apply} API schema can be applied, with
        the given instance name, C{name}, to the given C{prim}.


        If this schema can not be a applied the prim, this returns false and,
        if provided, populates C{whyNot} with the reason it can not be
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
    def CreateHighAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetHighAttr() , and also Create vs Get Property Methods for when
        to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateLowAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetLowAttr() , and also Create vs Get Property Methods for when to
        use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    @overload
    @staticmethod
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> LimitAPI:
        """
        Return a UsdPhysicsLimitAPI holding the prim adhering to this schema
        at C{path} on C{stage}.


        If no prim exists at C{path} on C{stage}, or if the prim at that path
        does not adhere to this schema, return an invalid schema object.
        C{path} must be of the format<path>.limit:name.

        This is shorthand for the following: ::

          TfToken name = SdfPath::StripNamespace(path.GetToken());
          UsdPhysicsLimitAPI(
              stage->GetPrimAtPath(path.GetPrimPath()), name);

        """
    @overload
    @staticmethod
    def Get(prim: pxr.Usd.Prim, name: str | pxr.Ar.ResolvedPath) -> LimitAPI:
        """
        Return a UsdPhysicsLimitAPI with name C{name} holding the prim
        C{prim}.


        Shorthand for UsdPhysicsLimitAPI(prim, name);
        """
    @staticmethod
    def GetAll(prim: pxr.Usd.Prim) -> list[LimitAPI]:
        """
        Return a vector of all named instances of UsdPhysicsLimitAPI on the
        given C{prim}.
        """
    def GetHighAttr(self) -> pxr.Usd.Attribute:
        """
        Upper limit.


        Units: degrees or distance depending on trans or rot axis applied to.
        inf means not limited in positive direction.

        Declaration

        C{float physics:high = inf}

        C++ Type

        float

        Usd Type

        SdfValueTypeNames->Float
        """
    def GetLowAttr(self) -> pxr.Usd.Attribute:
        """
        Lower limit.


        Units: degrees or distance depending on trans or rot axis applied to.
        -inf means not limited in negative direction.

        Declaration

        C{float physics:low = -inf}

        C++ Type

        float

        Usd Type

        SdfValueTypeNames->Float
        """
    @overload
    @staticmethod
    def GetSchemaAttributeNames(includeInherited: bool = ...) -> list[str]:
        """
        Return a vector of names of all pre-declared attributes for this
        schema class and all its ancestor classes.


        Does not include attributes that may be authored by custom/extended
        methods of the schemas involved.
        """
    @overload
    @staticmethod
    def GetSchemaAttributeNames(_includeInherited: bool, /, includeInherited: str | pxr.Ar.ResolvedPath) -> list[str]:
        """
        Return a vector of names of all pre-declared attributes for this
        schema class and all its ancestor classes for a given instance name.


        Does not include attributes that may be authored by custom/extended
        methods of the schemas involved. The names returned will have the
        proper namespace prefix.
        """
    @staticmethod
    def IsPhysicsLimitAPIPath(_path: pxr.Sdf.Path | str, /) -> bool:
        """
        Checks if the given path C{path} is of an API schema of type
        PhysicsLimitAPI.


        If so, it stores the instance name of the schema in C{name} and
        returns true. Otherwise, it returns false.
        """
    @staticmethod
    def _GetStaticTfType() -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...

class MassAPI(pxr.Usd.APISchemaBase):
    """
    Defines explicit mass properties (mass, density, inertia etc.).


    MassAPI can be applied to any object that has a PhysicsCollisionAPI or
    a PhysicsRigidBodyAPI.
    """
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None:
        """
        Construct a UsdPhysicsMassAPI on UsdPrim C{prim}.


        Equivalent to UsdPhysicsMassAPI::Get (prim.GetStage(), prim.GetPath())
        for a *valid* C{prim}, but will not immediately throw an error for an
        invalid C{prim}
        """
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None:
        """
        Construct a UsdPhysicsMassAPI on the prim held by C{schemaObj}.


        Should be preferred over UsdPhysicsMassAPI (schemaObj.GetPrim()), as
        it preserves SchemaBase state.
        """
    @staticmethod
    def Apply(prim: pxr.Usd.Prim) -> MassAPI:
        '''
        Applies this B{single-apply} API schema to the given C{prim}.


        This information is stored by adding"PhysicsMassAPI"to the token-
        valued, listOp metadata *apiSchemas* on the prim.

        A valid UsdPhysicsMassAPI object is returned upon success. An invalid
        (or empty) UsdPhysicsMassAPI object is returned upon failure. See
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
    def CreateCenterOfMassAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetCenterOfMassAttr() , and also Create vs Get Property Methods
        for when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateDensityAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetDensityAttr() , and also Create vs Get Property Methods for
        when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateDiagonalInertiaAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetDiagonalInertiaAttr() , and also Create vs Get Property Methods
        for when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateMassAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetMassAttr() , and also Create vs Get Property Methods for when
        to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreatePrincipalAxesAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetPrincipalAxesAttr() , and also Create vs Get Property Methods
        for when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    @staticmethod
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> MassAPI:
        """
        Return a UsdPhysicsMassAPI holding the prim adhering to this schema at
        C{path} on C{stage}.


        If no prim exists at C{path} on C{stage}, or if the prim at that path
        does not adhere to this schema, return an invalid schema object. This
        is shorthand for the following: ::

          UsdPhysicsMassAPI(stage->GetPrimAtPath(path));

        """
    def GetCenterOfMassAttr(self) -> pxr.Usd.Attribute:
        """
        Center of mass in the prim's local space.


        Units: distance.

        Declaration

        C{point3f physics:centerOfMass = (-inf, -inf, -inf)}

        C++ Type

        GfVec3f

        Usd Type

        SdfValueTypeNames->Point3f
        """
    def GetDensityAttr(self) -> pxr.Usd.Attribute:
        """
        If non-zero, specifies the density of the object.


        In the context of rigid body physics, density indirectly results in
        setting mass via (mass = density x volume of the object). How the
        volume is computed is up to implementation of the physics system. It
        is generally computed from the collision approximation rather than the
        graphical mesh. In the case where both density and mass are specified
        for the same object, mass has precedence over density. Unlike mass,
        child's prim's density overrides parent prim's density as it is
        accumulative. Note that density of a collisionAPI can be also
        alternatively set through a PhysicsMaterialAPI. The material density
        has the weakest precedence in density definition. Note if density is
        0.0 it is ignored. Units: mass/distance/distance/distance.

        Declaration

        C{float physics:density = 0}

        C++ Type

        float

        Usd Type

        SdfValueTypeNames->Float
        """
    def GetDiagonalInertiaAttr(self) -> pxr.Usd.Attribute:
        """
        If non-zero, specifies diagonalized inertia tensor along the principal
        axes.


        Note if diagonalInertial is (0.0, 0.0, 0.0) it is ignored. Units:
        mass*distance*distance.

        Declaration

        C{float3 physics:diagonalInertia = (0, 0, 0)}

        C++ Type

        GfVec3f

        Usd Type

        SdfValueTypeNames->Float3
        """
    def GetMassAttr(self) -> pxr.Usd.Attribute:
        """
        If non-zero, directly specifies the mass of the object.


        Note that any child prim can also have a mass when they apply massAPI.
        In this case, the precedence rule is'parent mass overrides the
        child's'. This may come as counter-intuitive, but mass is a computed
        quantity and in general not accumulative. For example, if a parent has
        mass of 10, and one of two children has mass of 20, allowing child's
        mass to override its parent results in a mass of -10 for the other
        child. Note if mass is 0.0 it is ignored. Units: mass.

        Declaration

        C{float physics:mass = 0}

        C++ Type

        float

        Usd Type

        SdfValueTypeNames->Float
        """
    def GetPrincipalAxesAttr(self) -> pxr.Usd.Attribute:
        """
        Orientation of the inertia tensor's principal axes in the prim's local
        space.



        Declaration

        C{quatf physics:principalAxes = (0, 0, 0, 0)}

        C++ Type

        GfQuatf

        Usd Type

        SdfValueTypeNames->Quatf
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

class MassUnits(Boost.Python.instance):
    """
    Container class for static double-precision symbols representing
    common mass units of measure expressed in kilograms.
    """
    grams: ClassVar[float] = ...  # read-only
    kilograms: ClassVar[float] = ...  # read-only
    slugs: ClassVar[float] = ...  # read-only
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """

class MaterialAPI(pxr.Usd.APISchemaBase):
    """
    Adds simulation material properties to a Material.


    All collisions that have a relationship to this material will have
    their collision response defined through this material.
    """
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None:
        """
        Construct a UsdPhysicsMaterialAPI on UsdPrim C{prim}.


        Equivalent to UsdPhysicsMaterialAPI::Get (prim.GetStage(),
        prim.GetPath()) for a *valid* C{prim}, but will not immediately throw
        an error for an invalid C{prim}
        """
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None:
        """
        Construct a UsdPhysicsMaterialAPI on the prim held by C{schemaObj}.


        Should be preferred over UsdPhysicsMaterialAPI (schemaObj.GetPrim()),
        as it preserves SchemaBase state.
        """
    @staticmethod
    def Apply(prim: pxr.Usd.Prim) -> MaterialAPI:
        '''
        Applies this B{single-apply} API schema to the given C{prim}.


        This information is stored by adding"PhysicsMaterialAPI"to the token-
        valued, listOp metadata *apiSchemas* on the prim.

        A valid UsdPhysicsMaterialAPI object is returned upon success. An
        invalid (or empty) UsdPhysicsMaterialAPI object is returned upon
        failure. See UsdPrim::ApplyAPI() for conditions resulting in failure.

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
    def CreateDensityAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetDensityAttr() , and also Create vs Get Property Methods for
        when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateDynamicFrictionAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetDynamicFrictionAttr() , and also Create vs Get Property Methods
        for when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateRestitutionAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetRestitutionAttr() , and also Create vs Get Property Methods for
        when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateStaticFrictionAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetStaticFrictionAttr() , and also Create vs Get Property Methods
        for when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    @staticmethod
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> MaterialAPI:
        """
        Return a UsdPhysicsMaterialAPI holding the prim adhering to this
        schema at C{path} on C{stage}.


        If no prim exists at C{path} on C{stage}, or if the prim at that path
        does not adhere to this schema, return an invalid schema object. This
        is shorthand for the following: ::

          UsdPhysicsMaterialAPI(stage->GetPrimAtPath(path));

        """
    def GetDensityAttr(self) -> pxr.Usd.Attribute:
        """
        If non-zero, defines the density of the material.


        This can be used for body mass computation, see PhysicsMassAPI. Note
        that if the density is 0.0 it is ignored. Units:
        mass/distance/distance/distance.

        Declaration

        C{float physics:density = 0}

        C++ Type

        float

        Usd Type

        SdfValueTypeNames->Float
        """
    def GetDynamicFrictionAttr(self) -> pxr.Usd.Attribute:
        """
        Dynamic friction coefficient.


        Unitless.

        Declaration

        C{float physics:dynamicFriction = 0}

        C++ Type

        float

        Usd Type

        SdfValueTypeNames->Float
        """
    def GetRestitutionAttr(self) -> pxr.Usd.Attribute:
        """
        Restitution coefficient.


        Unitless.

        Declaration

        C{float physics:restitution = 0}

        C++ Type

        float

        Usd Type

        SdfValueTypeNames->Float
        """
    @staticmethod
    def GetSchemaAttributeNames(includeInherited: bool = ...) -> list[str]:
        """
        Return a vector of names of all pre-declared attributes for this
        schema class and all its ancestor classes.


        Does not include attributes that may be authored by custom/extended
        methods of the schemas involved.
        """
    def GetStaticFrictionAttr(self) -> pxr.Usd.Attribute:
        """
        Static friction coefficient.


        Unitless.

        Declaration

        C{float physics:staticFriction = 0}

        C++ Type

        float

        Usd Type

        SdfValueTypeNames->Float
        """
    @staticmethod
    def _GetStaticTfType() -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...

class MeshCollisionAPI(pxr.Usd.APISchemaBase):
    '''
    Attributes to control how a Mesh is made into a collider.


    Can be applied to only a USDGeomMesh in addition to its
    PhysicsCollisionAPI.

    For any described attribute *Fallback* *Value* or *Allowed* *Values*
    below that are text/tokens, the actual token is published and defined
    in UsdPhysicsTokens. So to set an attribute to the value"rightHanded",
    use UsdPhysicsTokens->rightHanded as the value.
    '''
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None:
        """
        Construct a UsdPhysicsMeshCollisionAPI on UsdPrim C{prim}.


        Equivalent to UsdPhysicsMeshCollisionAPI::Get (prim.GetStage(),
        prim.GetPath()) for a *valid* C{prim}, but will not immediately throw
        an error for an invalid C{prim}
        """
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None:
        """
        Construct a UsdPhysicsMeshCollisionAPI on the prim held by
        C{schemaObj}.


        Should be preferred over UsdPhysicsMeshCollisionAPI
        (schemaObj.GetPrim()), as it preserves SchemaBase state.
        """
    @staticmethod
    def Apply(prim: pxr.Usd.Prim) -> MeshCollisionAPI:
        '''
        Applies this B{single-apply} API schema to the given C{prim}.


        This information is stored by adding"PhysicsMeshCollisionAPI"to the
        token-valued, listOp metadata *apiSchemas* on the prim.

        A valid UsdPhysicsMeshCollisionAPI object is returned upon success. An
        invalid (or empty) UsdPhysicsMeshCollisionAPI object is returned upon
        failure. See UsdPrim::ApplyAPI() for conditions resulting in failure.

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
    def CreateApproximationAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetApproximationAttr() , and also Create vs Get Property Methods
        for when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    @staticmethod
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> MeshCollisionAPI:
        """
        Return a UsdPhysicsMeshCollisionAPI holding the prim adhering to this
        schema at C{path} on C{stage}.


        If no prim exists at C{path} on C{stage}, or if the prim at that path
        does not adhere to this schema, return an invalid schema object. This
        is shorthand for the following: ::

          UsdPhysicsMeshCollisionAPI(stage->GetPrimAtPath(path));

        """
    def GetApproximationAttr(self) -> pxr.Usd.Attribute:
        '''
        Determines the mesh\'s collision approximation:"none"- The mesh
        geometry is used directly as a collider without any approximation.


        "convexDecomposition"- A convex mesh decomposition is performed. This
        results in a set of convex mesh colliders."convexHull"- A convex hull
        of the mesh is generated and used as the collider."boundingSphere"- A
        bounding sphere is computed around the mesh and used as a
        collider."boundingCube"- An optimally fitting box collider is computed
        around the mesh."meshSimplification"- A mesh simplification step is
        performed, resulting in a simplified triangle mesh collider.

        Declaration

        C{uniform token physics:approximation ="none"}

        C++ Type

        TfToken

        Usd Type

        SdfValueTypeNames->Token

        Variability

        SdfVariabilityUniform

        Allowed Values

        none, convexDecomposition, convexHull, boundingSphere, boundingCube,
        meshSimplification
        '''
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

class PrismaticJoint(Joint):
    '''
    Predefined prismatic joint type (translation along prismatic joint
    axis is permitted.)


    For any described attribute *Fallback* *Value* or *Allowed* *Values*
    below that are text/tokens, the actual token is published and defined
    in UsdPhysicsTokens. So to set an attribute to the value"rightHanded",
    use UsdPhysicsTokens->rightHanded as the value.
    '''
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None:
        """
        Construct a UsdPhysicsPrismaticJoint on UsdPrim C{prim}.


        Equivalent to UsdPhysicsPrismaticJoint::Get (prim.GetStage(),
        prim.GetPath()) for a *valid* C{prim}, but will not immediately throw
        an error for an invalid C{prim}
        """
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None:
        """
        Construct a UsdPhysicsPrismaticJoint on the prim held by C{schemaObj}.


        Should be preferred over UsdPhysicsPrismaticJoint
        (schemaObj.GetPrim()), as it preserves SchemaBase state.
        """
    def CreateAxisAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetAxisAttr() , and also Create vs Get Property Methods for when
        to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateLowerLimitAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetLowerLimitAttr() , and also Create vs Get Property Methods for
        when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateUpperLimitAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetUpperLimitAttr() , and also Create vs Get Property Methods for
        when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    @staticmethod
    def Define(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> PrismaticJoint:
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
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> PrismaticJoint:
        """
        Return a UsdPhysicsPrismaticJoint holding the prim adhering to this
        schema at C{path} on C{stage}.


        If no prim exists at C{path} on C{stage}, or if the prim at that path
        does not adhere to this schema, return an invalid schema object. This
        is shorthand for the following: ::

          UsdPhysicsPrismaticJoint(stage->GetPrimAtPath(path));

        """
    def GetAxisAttr(self) -> pxr.Usd.Attribute:
        '''
        Joint axis.



        Declaration

        C{uniform token physics:axis ="X"}

        C++ Type

        TfToken

        Usd Type

        SdfValueTypeNames->Token

        Variability

        SdfVariabilityUniform

        Allowed Values

        X, Y, Z
        '''
    def GetLowerLimitAttr(self) -> pxr.Usd.Attribute:
        """
        Lower limit.


        Units: distance. -inf means not limited in negative direction.

        Declaration

        C{float physics:lowerLimit = -inf}

        C++ Type

        float

        Usd Type

        SdfValueTypeNames->Float
        """
    @staticmethod
    def GetSchemaAttributeNames(includeInherited: bool = ...) -> list[str]:
        """
        Return a vector of names of all pre-declared attributes for this
        schema class and all its ancestor classes.


        Does not include attributes that may be authored by custom/extended
        methods of the schemas involved.
        """
    def GetUpperLimitAttr(self) -> pxr.Usd.Attribute:
        """
        Upper limit.


        Units: distance. inf means not limited in positive direction.

        Declaration

        C{float physics:upperLimit = inf}

        C++ Type

        float

        Usd Type

        SdfValueTypeNames->Float
        """
    @staticmethod
    def _GetStaticTfType() -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...

class RevoluteJoint(Joint):
    '''
    Predefined revolute joint type (rotation along revolute joint axis is
    permitted.)


    For any described attribute *Fallback* *Value* or *Allowed* *Values*
    below that are text/tokens, the actual token is published and defined
    in UsdPhysicsTokens. So to set an attribute to the value"rightHanded",
    use UsdPhysicsTokens->rightHanded as the value.
    '''
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None:
        """
        Construct a UsdPhysicsRevoluteJoint on UsdPrim C{prim}.


        Equivalent to UsdPhysicsRevoluteJoint::Get (prim.GetStage(),
        prim.GetPath()) for a *valid* C{prim}, but will not immediately throw
        an error for an invalid C{prim}
        """
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None:
        """
        Construct a UsdPhysicsRevoluteJoint on the prim held by C{schemaObj}.


        Should be preferred over UsdPhysicsRevoluteJoint
        (schemaObj.GetPrim()), as it preserves SchemaBase state.
        """
    def CreateAxisAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetAxisAttr() , and also Create vs Get Property Methods for when
        to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateLowerLimitAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetLowerLimitAttr() , and also Create vs Get Property Methods for
        when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateUpperLimitAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetUpperLimitAttr() , and also Create vs Get Property Methods for
        when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    @staticmethod
    def Define(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> RevoluteJoint:
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
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> RevoluteJoint:
        """
        Return a UsdPhysicsRevoluteJoint holding the prim adhering to this
        schema at C{path} on C{stage}.


        If no prim exists at C{path} on C{stage}, or if the prim at that path
        does not adhere to this schema, return an invalid schema object. This
        is shorthand for the following: ::

          UsdPhysicsRevoluteJoint(stage->GetPrimAtPath(path));

        """
    def GetAxisAttr(self) -> pxr.Usd.Attribute:
        '''
        Joint axis.



        Declaration

        C{uniform token physics:axis ="X"}

        C++ Type

        TfToken

        Usd Type

        SdfValueTypeNames->Token

        Variability

        SdfVariabilityUniform

        Allowed Values

        X, Y, Z
        '''
    def GetLowerLimitAttr(self) -> pxr.Usd.Attribute:
        """
        Lower limit.


        Units: degrees. -inf means not limited in negative direction.

        Declaration

        C{float physics:lowerLimit = -inf}

        C++ Type

        float

        Usd Type

        SdfValueTypeNames->Float
        """
    @staticmethod
    def GetSchemaAttributeNames(includeInherited: bool = ...) -> list[str]:
        """
        Return a vector of names of all pre-declared attributes for this
        schema class and all its ancestor classes.


        Does not include attributes that may be authored by custom/extended
        methods of the schemas involved.
        """
    def GetUpperLimitAttr(self) -> pxr.Usd.Attribute:
        """
        Upper limit.


        Units: degrees. inf means not limited in positive direction.

        Declaration

        C{float physics:upperLimit = inf}

        C++ Type

        float

        Usd Type

        SdfValueTypeNames->Float
        """
    @staticmethod
    def _GetStaticTfType() -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...

class RigidBodyAPI(pxr.Usd.APISchemaBase):
    """
    Applies physics body attributes to any UsdGeomXformable prim and marks
    that prim to be driven by a simulation.


    If a simulation is running it will update this prim's pose. All prims
    in the hierarchy below this prim should move accordingly.
    """

    class MassInformation(Boost.Python.instance):
        """
        Mass information for a collision, used in ComputeMassProperties
        MassInformationFn callback.
        """
        __instance_size__: ClassVar[int] = ...
        centerOfMass: Incomplete
        inertia: Incomplete
        localPos: Incomplete
        localRot: Incomplete
        volume: Incomplete
        def __init__(self) -> None: ...
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None:
        """
        Construct a UsdPhysicsRigidBodyAPI on UsdPrim C{prim}.


        Equivalent to UsdPhysicsRigidBodyAPI::Get (prim.GetStage(),
        prim.GetPath()) for a *valid* C{prim}, but will not immediately throw
        an error for an invalid C{prim}
        """
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None:
        """
        Construct a UsdPhysicsRigidBodyAPI on the prim held by C{schemaObj}.


        Should be preferred over UsdPhysicsRigidBodyAPI (schemaObj.GetPrim()),
        as it preserves SchemaBase state.
        """
    @staticmethod
    def Apply(prim: pxr.Usd.Prim) -> RigidBodyAPI:
        '''
        Applies this B{single-apply} API schema to the given C{prim}.


        This information is stored by adding"PhysicsRigidBodyAPI"to the token-
        valued, listOp metadata *apiSchemas* on the prim.

        A valid UsdPhysicsRigidBodyAPI object is returned upon success. An
        invalid (or empty) UsdPhysicsRigidBodyAPI object is returned upon
        failure. See UsdPrim::ApplyAPI() for conditions resulting in failure.

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
    def ComputeMassProperties(self, _massInfoFn: MassInformationFn, /) -> tuple:
        """
        Compute mass properties of the rigid body C{diagonalInertia} Computed
        diagonal of the inertial tensor for the rigid body.


        C{com} Computed center of mass for the rigid body. C{principalAxes}
        Inertia tensor's principal axes orienttion for the rigid body.
        C{massInfoFn} Callback function to get collision mass information.

        Computed mass of the rigid body
        """
    def CreateAngularVelocityAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetAngularVelocityAttr() , and also Create vs Get Property Methods
        for when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateKinematicEnabledAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetKinematicEnabledAttr() , and also Create vs Get Property
        Methods for when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateRigidBodyEnabledAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetRigidBodyEnabledAttr() , and also Create vs Get Property
        Methods for when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateSimulationOwnerRel(self) -> pxr.Usd.Relationship:
        """
        See GetSimulationOwnerRel() , and also Create vs Get Property Methods
        for when to use Get vs Create.
        """
    def CreateStartsAsleepAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetStartsAsleepAttr() , and also Create vs Get Property Methods
        for when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateVelocityAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetVelocityAttr() , and also Create vs Get Property Methods for
        when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    @staticmethod
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> RigidBodyAPI:
        """
        Return a UsdPhysicsRigidBodyAPI holding the prim adhering to this
        schema at C{path} on C{stage}.


        If no prim exists at C{path} on C{stage}, or if the prim at that path
        does not adhere to this schema, return an invalid schema object. This
        is shorthand for the following: ::

          UsdPhysicsRigidBodyAPI(stage->GetPrimAtPath(path));

        """
    def GetAngularVelocityAttr(self) -> pxr.Usd.Attribute:
        """
        Angular velocity in the same space as the node's xform.


        Units: degrees/second.

        Declaration

        C{vector3f physics:angularVelocity = (0, 0, 0)}

        C++ Type

        GfVec3f

        Usd Type

        SdfValueTypeNames->Vector3f
        """
    def GetKinematicEnabledAttr(self) -> pxr.Usd.Attribute:
        """
        Determines whether the body is kinematic or not.


        A kinematic body is a body that is moved through animated poses or
        through user defined poses. The simulation derives velocities for the
        kinematic body based on the external motion. When a continuous motion
        is not desired, this kinematic flag should be set to false.

        Declaration

        C{bool physics:kinematicEnabled = 0}

        C++ Type

        bool

        Usd Type

        SdfValueTypeNames->Bool
        """
    def GetRigidBodyEnabledAttr(self) -> pxr.Usd.Attribute:
        """
        Determines if this PhysicsRigidBodyAPI is enabled.



        Declaration

        C{bool physics:rigidBodyEnabled = 1}

        C++ Type

        bool

        Usd Type

        SdfValueTypeNames->Bool
        """
    @staticmethod
    def GetSchemaAttributeNames(includeInherited: bool = ...) -> list[str]:
        """
        Return a vector of names of all pre-declared attributes for this
        schema class and all its ancestor classes.


        Does not include attributes that may be authored by custom/extended
        methods of the schemas involved.
        """
    def GetSimulationOwnerRel(self) -> pxr.Usd.Relationship:
        """
        Single PhysicsScene that will simulate this body.


        By default this is the first PhysicsScene found in the stage using
        UsdStage::Traverse() .
        """
    def GetStartsAsleepAttr(self) -> pxr.Usd.Attribute:
        """
        Determines if the body is asleep when the simulation starts.



        Declaration

        C{uniform bool physics:startsAsleep = 0}

        C++ Type

        bool

        Usd Type

        SdfValueTypeNames->Bool

        Variability

        SdfVariabilityUniform
        """
    def GetVelocityAttr(self) -> pxr.Usd.Attribute:
        """
        Linear velocity in the same space as the node's xform.


        Units: distance/second.

        Declaration

        C{vector3f physics:velocity = (0, 0, 0)}

        C++ Type

        GfVec3f

        Usd Type

        SdfValueTypeNames->Vector3f
        """
    @staticmethod
    def _GetStaticTfType() -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...

class Scene(pxr.Usd.Typed):
    """
    General physics simulation properties, required for simulation.
    """
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None:
        """
        Construct a UsdPhysicsScene on UsdPrim C{prim}.


        Equivalent to UsdPhysicsScene::Get (prim.GetStage(), prim.GetPath())
        for a *valid* C{prim}, but will not immediately throw an error for an
        invalid C{prim}
        """
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None:
        """
        Construct a UsdPhysicsScene on the prim held by C{schemaObj}.


        Should be preferred over UsdPhysicsScene (schemaObj.GetPrim()), as it
        preserves SchemaBase state.
        """
    def CreateGravityDirectionAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetGravityDirectionAttr() , and also Create vs Get Property
        Methods for when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateGravityMagnitudeAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetGravityMagnitudeAttr() , and also Create vs Get Property
        Methods for when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    @staticmethod
    def Define(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> Scene:
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
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> Scene:
        """
        Return a UsdPhysicsScene holding the prim adhering to this schema at
        C{path} on C{stage}.


        If no prim exists at C{path} on C{stage}, or if the prim at that path
        does not adhere to this schema, return an invalid schema object. This
        is shorthand for the following: ::

          UsdPhysicsScene(stage->GetPrimAtPath(path));

        """
    def GetGravityDirectionAttr(self) -> pxr.Usd.Attribute:
        """
        Gravity direction vector in simulation world space.


        Will be normalized before use. A zero vector is a request to use the
        negative upAxis. Unitless.

        Declaration

        C{vector3f physics:gravityDirection = (0, 0, 0)}

        C++ Type

        GfVec3f

        Usd Type

        SdfValueTypeNames->Vector3f
        """
    def GetGravityMagnitudeAttr(self) -> pxr.Usd.Attribute:
        """
        Gravity acceleration magnitude in simulation world space.


        A negative value is a request to use a value equivalent to earth
        gravity regardless of the metersPerUnit scaling used by this scene.
        Units: distance/second/second.

        Declaration

        C{float physics:gravityMagnitude = -inf}

        C++ Type

        float

        Usd Type

        SdfValueTypeNames->Float
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

class SphericalJoint(Joint):
    '''
    Predefined spherical joint type (Removes linear degrees of freedom,
    cone limit may restrict the motion in a given range.) It allows two
    limit values, which when equal create a circular, else an elliptic
    cone limit around the limit axis.


    For any described attribute *Fallback* *Value* or *Allowed* *Values*
    below that are text/tokens, the actual token is published and defined
    in UsdPhysicsTokens. So to set an attribute to the value"rightHanded",
    use UsdPhysicsTokens->rightHanded as the value.
    '''
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None:
        """
        Construct a UsdPhysicsSphericalJoint on UsdPrim C{prim}.


        Equivalent to UsdPhysicsSphericalJoint::Get (prim.GetStage(),
        prim.GetPath()) for a *valid* C{prim}, but will not immediately throw
        an error for an invalid C{prim}
        """
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None:
        """
        Construct a UsdPhysicsSphericalJoint on the prim held by C{schemaObj}.


        Should be preferred over UsdPhysicsSphericalJoint
        (schemaObj.GetPrim()), as it preserves SchemaBase state.
        """
    def CreateAxisAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetAxisAttr() , and also Create vs Get Property Methods for when
        to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateConeAngle0LimitAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetConeAngle0LimitAttr() , and also Create vs Get Property Methods
        for when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateConeAngle1LimitAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetConeAngle1LimitAttr() , and also Create vs Get Property Methods
        for when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    @staticmethod
    def Define(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> SphericalJoint:
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
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> SphericalJoint:
        """
        Return a UsdPhysicsSphericalJoint holding the prim adhering to this
        schema at C{path} on C{stage}.


        If no prim exists at C{path} on C{stage}, or if the prim at that path
        does not adhere to this schema, return an invalid schema object. This
        is shorthand for the following: ::

          UsdPhysicsSphericalJoint(stage->GetPrimAtPath(path));

        """
    def GetAxisAttr(self) -> pxr.Usd.Attribute:
        '''
        Cone limit axis.



        Declaration

        C{uniform token physics:axis ="X"}

        C++ Type

        TfToken

        Usd Type

        SdfValueTypeNames->Token

        Variability

        SdfVariabilityUniform

        Allowed Values

        X, Y, Z
        '''
    def GetConeAngle0LimitAttr(self) -> pxr.Usd.Attribute:
        """
        Cone limit from the primary joint axis in the local0 frame toward the
        next axis.


        (Next axis of X is Y, and of Z is X.) A negative value means not
        limited. Units: degrees.

        Declaration

        C{float physics:coneAngle0Limit = -1}

        C++ Type

        float

        Usd Type

        SdfValueTypeNames->Float
        """
    def GetConeAngle1LimitAttr(self) -> pxr.Usd.Attribute:
        """
        Cone limit from the primary joint axis in the local0 frame toward the
        second to next axis.


        A negative value means not limited. Units: degrees.

        Declaration

        C{float physics:coneAngle1Limit = -1}

        C++ Type

        float

        Usd Type

        SdfValueTypeNames->Float
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
    PhysicsArticulationRootAPI: ClassVar[str] = ...  # read-only
    PhysicsCollisionAPI: ClassVar[str] = ...  # read-only
    PhysicsCollisionGroup: ClassVar[str] = ...  # read-only
    PhysicsDistanceJoint: ClassVar[str] = ...  # read-only
    PhysicsDriveAPI: ClassVar[str] = ...  # read-only
    PhysicsFilteredPairsAPI: ClassVar[str] = ...  # read-only
    PhysicsFixedJoint: ClassVar[str] = ...  # read-only
    PhysicsJoint: ClassVar[str] = ...  # read-only
    PhysicsLimitAPI: ClassVar[str] = ...  # read-only
    PhysicsMassAPI: ClassVar[str] = ...  # read-only
    PhysicsMaterialAPI: ClassVar[str] = ...  # read-only
    PhysicsMeshCollisionAPI: ClassVar[str] = ...  # read-only
    PhysicsPrismaticJoint: ClassVar[str] = ...  # read-only
    PhysicsRevoluteJoint: ClassVar[str] = ...  # read-only
    PhysicsRigidBodyAPI: ClassVar[str] = ...  # read-only
    PhysicsScene: ClassVar[str] = ...  # read-only
    PhysicsSphericalJoint: ClassVar[str] = ...  # read-only
    acceleration: ClassVar[str] = ...  # read-only
    angular: ClassVar[str] = ...  # read-only
    boundingCube: ClassVar[str] = ...  # read-only
    boundingSphere: ClassVar[str] = ...  # read-only
    colliders: ClassVar[str] = ...  # read-only
    convexDecomposition: ClassVar[str] = ...  # read-only
    convexHull: ClassVar[str] = ...  # read-only
    distance: ClassVar[str] = ...  # read-only
    drive: ClassVar[str] = ...  # read-only
    drive_MultipleApplyTemplate_PhysicsDamping: ClassVar[str] = ...  # read-only
    drive_MultipleApplyTemplate_PhysicsMaxForce: ClassVar[str] = ...  # read-only
    drive_MultipleApplyTemplate_PhysicsStiffness: ClassVar[str] = ...  # read-only
    drive_MultipleApplyTemplate_PhysicsTargetPosition: ClassVar[str] = ...  # read-only
    drive_MultipleApplyTemplate_PhysicsTargetVelocity: ClassVar[str] = ...  # read-only
    drive_MultipleApplyTemplate_PhysicsType: ClassVar[str] = ...  # read-only
    force: ClassVar[str] = ...  # read-only
    kilogramsPerUnit: ClassVar[str] = ...  # read-only
    limit: ClassVar[str] = ...  # read-only
    limit_MultipleApplyTemplate_PhysicsHigh: ClassVar[str] = ...  # read-only
    limit_MultipleApplyTemplate_PhysicsLow: ClassVar[str] = ...  # read-only
    linear: ClassVar[str] = ...  # read-only
    meshSimplification: ClassVar[str] = ...  # read-only
    none: ClassVar[str] = ...  # read-only
    physicsAngularVelocity: ClassVar[str] = ...  # read-only
    physicsApproximation: ClassVar[str] = ...  # read-only
    physicsAxis: ClassVar[str] = ...  # read-only
    physicsBody0: ClassVar[str] = ...  # read-only
    physicsBody1: ClassVar[str] = ...  # read-only
    physicsBreakForce: ClassVar[str] = ...  # read-only
    physicsBreakTorque: ClassVar[str] = ...  # read-only
    physicsCenterOfMass: ClassVar[str] = ...  # read-only
    physicsCollisionEnabled: ClassVar[str] = ...  # read-only
    physicsConeAngle0Limit: ClassVar[str] = ...  # read-only
    physicsConeAngle1Limit: ClassVar[str] = ...  # read-only
    physicsDensity: ClassVar[str] = ...  # read-only
    physicsDiagonalInertia: ClassVar[str] = ...  # read-only
    physicsDynamicFriction: ClassVar[str] = ...  # read-only
    physicsExcludeFromArticulation: ClassVar[str] = ...  # read-only
    physicsFilteredGroups: ClassVar[str] = ...  # read-only
    physicsFilteredPairs: ClassVar[str] = ...  # read-only
    physicsGravityDirection: ClassVar[str] = ...  # read-only
    physicsGravityMagnitude: ClassVar[str] = ...  # read-only
    physicsInvertFilteredGroups: ClassVar[str] = ...  # read-only
    physicsJointEnabled: ClassVar[str] = ...  # read-only
    physicsKinematicEnabled: ClassVar[str] = ...  # read-only
    physicsLocalPos0: ClassVar[str] = ...  # read-only
    physicsLocalPos1: ClassVar[str] = ...  # read-only
    physicsLocalRot0: ClassVar[str] = ...  # read-only
    physicsLocalRot1: ClassVar[str] = ...  # read-only
    physicsLowerLimit: ClassVar[str] = ...  # read-only
    physicsMass: ClassVar[str] = ...  # read-only
    physicsMaxDistance: ClassVar[str] = ...  # read-only
    physicsMergeGroup: ClassVar[str] = ...  # read-only
    physicsMinDistance: ClassVar[str] = ...  # read-only
    physicsPrincipalAxes: ClassVar[str] = ...  # read-only
    physicsRestitution: ClassVar[str] = ...  # read-only
    physicsRigidBodyEnabled: ClassVar[str] = ...  # read-only
    physicsSimulationOwner: ClassVar[str] = ...  # read-only
    physicsStartsAsleep: ClassVar[str] = ...  # read-only
    physicsStaticFriction: ClassVar[str] = ...  # read-only
    physicsUpperLimit: ClassVar[str] = ...  # read-only
    physicsVelocity: ClassVar[str] = ...  # read-only
    rotX: ClassVar[str] = ...  # read-only
    rotY: ClassVar[str] = ...  # read-only
    rotZ: ClassVar[str] = ...  # read-only
    transX: ClassVar[str] = ...  # read-only
    transY: ClassVar[str] = ...  # read-only
    transZ: ClassVar[str] = ...  # read-only
    x: ClassVar[str] = ...  # read-only
    y: ClassVar[str] = ...  # read-only
    z: ClassVar[str] = ...  # read-only
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

def GetStageKilogramsPerUnit(stage: pxr.Usd.Stage) -> float:
    """
    Return *stage* 's authored *kilogramsPerUnit*, or 1.0 if unauthored.
    """
def MassUnitsAre(authoredUnits: float, standardUnits: float, epsilon: float = ...) -> bool:
    """
    Return *true* if the two given metrics are within the provided
    relative *epsilon* of each other, when you need to know an absolute
    metric rather than a scaling factor.



    Use like so: ::

      double stageUnits = UsdPhysicsGetStageKilogramsPerUnit(stage);
  
      if (UsdPhysicsMassUnitsAre(stageUnits, UsdPhysicsMassUnits::kilograms))
          // do something for kilograms
      else if (UsdPhysicsMassUnitsAre(stageUnits, UsdPhysicsMassUnits::grams))
          // do something for grams

    *false* if either input is zero or negative, otherwise relative
    floating-point comparison between the two inputs.
    """
def SetStageKilogramsPerUnit(stage: pxr.Usd.Stage, metersPerUnit: float) -> bool:
    """
    Author *stage* 's *kilogramsPerUnit*.



    true if kilogramsPerUnit was successfully set. The stage's
    UsdEditTarget must be either its root layer or session layer.
    """
def StageHasAuthoredKilogramsPerUnit(stage: pxr.Usd.Stage) -> bool:
    """
    Return whether *stage* has an authored *kilogramsPerUnit*.
    """
