# mypy: disable-error-code="misc, override, no-redef"

import Boost.Python
import pxr.Ar
import pxr.Ndr
import pxr.Sdf
import pxr.Sdr
import pxr.Tf
import pxr.Usd
import pxr.UsdGeom
import pxr.UsdSkel
import pxr.Vt
import typing
from _typeshed import Incomplete
from typing import Any, ClassVar, overload

__MFB_FULL_PACKAGE_NAME: str

class AttributeType(Boost.Python.enum):
    Input: ClassVar[AttributeType] = ...
    Invalid: ClassVar[AttributeType] = ...
    Output: ClassVar[AttributeType] = ...
    names: ClassVar[dict] = ...
    values: ClassVar[dict] = ...

class ConnectableAPI(pxr.Usd.APISchemaBase):
    """
    UsdShadeConnectableAPI is an API schema that provides a common
    interface for creating outputs and making connections between shading
    parameters and outputs.


    The interface is common to all UsdShade schemas that support Inputs
    and Outputs, which currently includes UsdShadeShader,
    UsdShadeNodeGraph, and UsdShadeMaterial.

    One can construct a UsdShadeConnectableAPI directly from a UsdPrim, or
    from objects of any of the schema classes listed above. If it seems
    onerous to need to construct a secondary schema object to interact
    with Inputs and Outputs, keep in mind that any function whose purpose
    is either to walk material/shader networks via their connections, or
    to create such networks, can typically be written entirely in terms of
    UsdShadeConnectableAPI objects, without needing to care what the
    underlying prim type is.

    Additionally, the most common UsdShadeConnectableAPI behaviors
    (creating Inputs and Outputs, and making connections) are wrapped as
    convenience methods on the prim schema classes (creation) and
    UsdShadeInput and UsdShadeOutput.
    """
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None:
        """
        Construct a UsdShadeConnectableAPI on UsdPrim C{prim}.


        Equivalent to UsdShadeConnectableAPI::Get (prim.GetStage(),
        prim.GetPath()) for a *valid* C{prim}, but will not immediately throw
        an error for an invalid C{prim}
        """
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None:
        """
        Construct a UsdShadeConnectableAPI on the prim held by C{schemaObj}.


        Should be preferred over UsdShadeConnectableAPI (schemaObj.GetPrim()),
        as it preserves SchemaBase state.
        """
    @overload
    @staticmethod
    def CanConnect(input: Input, source: pxr.Usd.Attribute | pxr.UsdGeom.ConstraintTarget | pxr.UsdGeom.Primvar | pxr.UsdGeom.XformOp | Input | Output) -> bool:
        '''
        Determines whether the given input can be connected to the given
        source attribute, which can be an input or an output.


        The result depends on the"connectability"of the input and the source
        attributes. Depending on the prim type, this may require the plugin
        that defines connectability behavior for that prim type be loaded.

        UsdShadeInput::SetConnectability

        UsdShadeInput::GetConnectability
        '''
    @overload
    @staticmethod
    def CanConnect(output: Output, source: pxr.Usd.Attribute | pxr.UsdGeom.ConstraintTarget | pxr.UsdGeom.Primvar | pxr.UsdGeom.XformOp | Input | Output = ...) -> bool:
        """
        Determines whether the given output can be connected to the given
        source attribute, which can be an input or an output.


        An output is considered to be connectable only if it belongs to a
        node-graph. Shader outputs are not connectable.

        C{source} is an optional argument. If a valid UsdAttribute is supplied
        for it, this method will return true only if the source attribute is
        owned by a descendant of the node-graph owning the output.
        """
    @staticmethod
    def ClearSource(shadingAttr: pxr.Usd.Attribute | pxr.UsdGeom.ConstraintTarget | pxr.UsdGeom.Primvar | pxr.UsdGeom.XformOp | Input | Output) -> bool:
        """
        Deprecated

        This is the older version that only referenced a single source. Please
        use ClearSources instead.
        """
    @staticmethod
    def ClearSources(shadingAttr: pxr.Usd.Attribute | pxr.UsdGeom.ConstraintTarget | pxr.UsdGeom.Primvar | pxr.UsdGeom.XformOp | Input | Output) -> bool:
        """
        Clears sources for this shading attribute in the current
        UsdEditTarget.


        Most of the time, what you probably want is DisconnectSource() rather
        than this function.

        DisconnectSource()
        """
    @overload
    @staticmethod
    def ConnectToSource(shadingAttr: pxr.Usd.Attribute | pxr.UsdGeom.ConstraintTarget | pxr.UsdGeom.Primvar | pxr.UsdGeom.XformOp | Input | Output, source: ConnectionSourceInfo, mod: ConnectionModification = ...) -> bool:
        """
        Authors a connection for a given shading attribute C{shadingAttr}.


        C{shadingAttr} can represent a parameter, an input or an output.
        C{source} is a struct that describes the upstream source attribute
        with all the information necessary to make a connection. See the
        documentation for UsdShadeConnectionSourceInfo. C{mod} describes the
        operation that should be applied to the list of connections. By
        default the new connection will replace any existing connections, but
        it can add to the list of connections to represent multiple input
        connections.

        C{true} if a connection was created successfully. C{false} if
        C{shadingAttr} or C{source} is invalid.

        This method does not verify the connectability of the shading
        attribute to the source. Clients must invoke CanConnect() themselves
        to ensure compatibility.

        The source shading attribute is created if it doesn't exist already.
        """
    @overload
    @staticmethod
    def ConnectToSource(shadingAttr: pxr.Usd.Attribute | pxr.UsdGeom.ConstraintTarget | pxr.UsdGeom.Primvar | pxr.UsdGeom.XformOp | Input | Output, source: ConnectableAPI, sourceName: str | pxr.Ar.ResolvedPath, sourceType: AttributeType = ..., typeName: pxr.Sdf.ValueTypeName = ...) -> bool:
        """
        Deprecated

        Please use the versions that take a UsdShadeConnectionSourceInfo to
        describe the upstream source This is an overloaded member function,
        provided for convenience. It differs from the above function only in
        what argument(s) it accepts.
        """
    @overload
    @staticmethod
    def ConnectToSource(shadingAttr: pxr.Usd.Attribute | pxr.UsdGeom.ConstraintTarget | pxr.UsdGeom.Primvar | pxr.UsdGeom.XformOp | Input | Output, sourcePath: pxr.Sdf.Path | str) -> bool:
        """
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.

        Connect the given shading attribute to the source at path,
        C{sourcePath}.


        C{sourcePath} should be the fully namespaced property path.

        This overload is provided for convenience, for use in contexts where
        the prim types are unknown or unavailable.
        """
    @overload
    @staticmethod
    def ConnectToSource(shadingAttr: pxr.Usd.Attribute | pxr.UsdGeom.ConstraintTarget | pxr.UsdGeom.Primvar | pxr.UsdGeom.XformOp | Input | Output, input: Input) -> bool:
        """
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.

        Connect the given shading attribute to the given source input.
        """
    @overload
    @staticmethod
    def ConnectToSource(shadingAttr: pxr.Usd.Attribute | pxr.UsdGeom.ConstraintTarget | pxr.UsdGeom.Primvar | pxr.UsdGeom.XformOp | Input | Output, output: Output) -> bool:
        """
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.

        Connect the given shading attribute to the given source output.
        """
    def CreateInput(self, name: str | pxr.Ar.ResolvedPath, type: pxr.Sdf.ValueTypeName) -> Input:
        '''
        Create an input which can both have a value and be connected.


        The attribute representing the input is created in
        the"inputs:"namespace.
        '''
    def CreateOutput(self, name: str | pxr.Ar.ResolvedPath, type: pxr.Sdf.ValueTypeName) -> Output:
        '''
        Create an output, which represents and externally computed, typed
        value.


        Outputs on node-graphs can be connected.

        The attribute representing an output is created in
        the"outputs:"namespace.
        '''
    @staticmethod
    def DisconnectSource(shadingAttr: pxr.Usd.Attribute | pxr.UsdGeom.ConstraintTarget | pxr.UsdGeom.Primvar | pxr.UsdGeom.XformOp | Input | Output, sourceAttr: pxr.Usd.Attribute | pxr.UsdGeom.ConstraintTarget | pxr.UsdGeom.Primvar | pxr.UsdGeom.XformOp | Input | Output = ...) -> bool:
        '''
        Disconnect source for this shading attribute.


        If C{sourceAttr} is valid it will disconnect the connection to this
        upstream attribute. Otherwise it will disconnect all connections by
        authoring an empty list of connections for the attribute
        C{shadingAttr}.

        This may author more scene description than you might expect - we
        define the behavior of disconnect to be that, even if a shading
        attribute becomes connected in a weaker layer than the current
        UsdEditTarget, the attribute will *still* be disconnected in the
        composition, therefore we must"block"it in the current UsdEditTarget.

        ConnectToSource() .
        '''
    @staticmethod
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> ConnectableAPI:
        """
        Return a UsdShadeConnectableAPI holding the prim adhering to this
        schema at C{path} on C{stage}.


        If no prim exists at C{path} on C{stage}, or if the prim at that path
        does not adhere to this schema, return an invalid schema object. This
        is shorthand for the following: ::

          UsdShadeConnectableAPI(stage->GetPrimAtPath(path));

        """
    @staticmethod
    def GetConnectedSource(shadingAttr: pxr.Usd.Attribute | pxr.UsdGeom.ConstraintTarget | pxr.UsdGeom.Primvar | pxr.UsdGeom.XformOp | Input | Output) -> tuple[ConnectableAPI, str, AttributeType]:
        """
        Deprecated

        Shading attributes can have multiple connections and so using
        GetConnectedSources is needed in general

        Finds the source of a connection for the given shading attribute.

        C{shadingAttr} is the shading attribute whose connection we want to
        interrogate. C{source} is an output parameter which will be set to the
        source connectable prim. C{sourceName} will be set to the name of the
        source shading attribute, which may be an input or an output, as
        specified by C{sourceType} C{sourceType} will have the type of the
        source shading attribute, i.e. whether it is an C{Input} or C{Output}

        C{true} if the shading attribute is connected to a valid, defined
        source attribute. C{false} if the shading attribute is not connected
        to a single, defined source attribute.

        Previously this method would silently return false for multiple
        connections. We are changing the behavior of this method to return the
        result for the first connection and issue a TfWarn about it. We want
        to encourage clients to use GetConnectedSources going forward.

        The python wrapping for this method returns a (source, sourceName,
        sourceType) tuple if the parameter is connected, else C{None}
        """
    @staticmethod
    def GetConnectedSources(shadingAttr: pxr.Usd.Attribute | pxr.UsdGeom.ConstraintTarget | pxr.UsdGeom.Primvar | pxr.UsdGeom.XformOp | Input | Output) -> tuple[list[ConnectionSourceInfo], list[pxr.Sdf.Path]]:
        """
        Finds the valid sources of connections for the given shading
        attribute.


        C{shadingAttr} is the shading attribute whose connections we want to
        interrogate. C{invalidSourcePaths} is an optional output parameter to
        collect the invalid source paths that have not been reported in the
        returned vector.

        Returns a vector of C{UsdShadeConnectionSourceInfo} structs with
        information about each upsteam attribute. If the vector is empty,
        there have been no connections.

        A valid connection requires the existence of the source attribute and
        also requires that the source prim is UsdShadeConnectableAPI
        compatible.

        The python wrapping returns a tuple with the valid connections first,
        followed by the invalid source paths.
        """
    def GetInput(self, name: str | pxr.Ar.ResolvedPath) -> Input:
        """
        Return the requested input if it exists.


        C{name} is the unnamespaced base name.
        """
    def GetInputs(self, onlyAuthored: bool = ...) -> list[Input]:
        '''
        Returns all inputs on the connectable prim (i.e.


        shader or node-graph). Inputs are represented by attributes in
        the"inputs:"namespace. If C{onlyAuthored} is true (the default), then
        only return authored attributes; otherwise, this also returns un-
        authored builtins.
        '''
    def GetOutput(self, name: str | pxr.Ar.ResolvedPath) -> Output:
        """
        Return the requested output if it exists.


        C{name} is the unnamespaced base name.
        """
    def GetOutputs(self, onlyAuthored: bool = ...) -> list[Output]:
        '''
        Returns all outputs on the connectable prim (i.e.


        shader or node-graph). Outputs are represented by attributes in
        the"outputs:"namespace. If C{onlyAuthored} is true (the default), then
        only return authored attributes; otherwise, this also returns un-
        authored builtins.
        '''
    @staticmethod
    def GetRawConnectedSourcePaths(shadingAttr: pxr.Usd.Attribute | pxr.UsdGeom.ConstraintTarget | pxr.UsdGeom.Primvar | pxr.UsdGeom.XformOp | Input | Output) -> list[pxr.Sdf.Path]:
        '''
        Deprecated

        Please us GetConnectedSources to retrieve multiple connections

        Returns the"raw"(authored) connected source paths for the given
        shading attribute.
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
    def HasConnectableAPI(schemaType: pxr.Tf.Type) -> bool:
        """
        Return true if the C{schemaType} has a valid connectableAPIBehavior
        registered, false otherwise.


        To check if a prim's connectableAPI has a behavior defined, use
        UsdSchemaBase::operator bool() .
        """
    @staticmethod
    def HasConnectedSource(shadingAttr: pxr.Usd.Attribute | pxr.UsdGeom.ConstraintTarget | pxr.UsdGeom.Primvar | pxr.UsdGeom.XformOp | Input | Output) -> bool:
        """
        Returns true if and only if the shading attribute is currently
        connected to at least one valid (defined) source.


        If you will be calling GetConnectedSources() afterwards anyways, it
        will be *much* faster to instead check if the returned vector is
        empty: ::

          UsdShadeSourceInfoVector connections =
              UsdShadeConnectableAPI::GetConnectedSources(attribute);
          if (!connections.empty()){
               // process connected attribute
          } else {
               // process unconnected attribute
          }

        """
    def IsContainer(self) -> bool:
        """
        Returns true if the prim is a container.


        The underlying prim type may provide runtime behavior that defines
        whether it is a container.
        """
    @staticmethod
    def IsSourceConnectionFromBaseMaterial(shadingAttr: pxr.Usd.Attribute | pxr.UsdGeom.ConstraintTarget | pxr.UsdGeom.Primvar | pxr.UsdGeom.XformOp | Input | Output) -> bool:
        """
        Returns true if the connection to the given shading attribute's
        source, as returned by UsdShadeConnectableAPI::GetConnectedSource() ,
        is authored across a specializes arc, which is used to denote a base
        material.
        """
    def RequiresEncapsulation(self) -> bool:
        """
        Returns true if container encapsulation rules should be respected when
        evaluating connectibility behavior, false otherwise.


        The underlying prim type may provide runtime behavior that defines if
        encapsulation rules are respected or not.
        """
    @staticmethod
    def SetConnectedSources(_shadingAttr: pxr.Usd.Attribute | pxr.UsdGeom.ConstraintTarget | pxr.UsdGeom.Primvar | pxr.UsdGeom.XformOp | Input | Output, _sourceInfos: typing.Iterable[ConnectionSourceInfo], /) -> bool:
        """
        Authors a list of connections for a given shading attribute
        C{shadingAttr}.


        C{shadingAttr} can represent a parameter, an input or an output.
        C{sourceInfos} is a vector of structs that describes the upstream
        source attributes with all the information necessary to make all the
        connections. See the documentation for UsdShadeConnectionSourceInfo.

        C{true} if all connection were created successfully. C{false} if the
        C{shadingAttr} or one of the sources are invalid.

        A valid connection is one that has a valid
        C{UsdShadeConnectionSourceInfo}, which requires the existence of the
        upstream source prim. It does not require the existence of the source
        attribute as it will be create if necessary.
        """
    @staticmethod
    def _GetStaticTfType() -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...

class ConnectionModification(Boost.Python.enum):
    Append: ClassVar[ConnectionModification] = ...
    Prepend: ClassVar[ConnectionModification] = ...
    Replace: ClassVar[ConnectionModification] = ...
    names: ClassVar[dict] = ...
    values: ClassVar[dict] = ...

class ConnectionSourceInfo(Boost.Python.instance):
    """
    A compact struct to represent a bundle of information about an
    upstream source attribute.
    """
    __instance_size__: ClassVar[int] = ...
    source: Incomplete
    sourceName: Incomplete
    sourceType: Incomplete
    typeName: Incomplete
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, source: ConnectableAPI, sourceName: str | pxr.Ar.ResolvedPath, sourceType: AttributeType, typeName: pxr.Sdf.ValueTypeName = ...) -> None: ...
    @overload
    def __init__(self, input: Input) -> None: ...
    @overload
    def __init__(self, output: Output) -> None: ...
    @overload
    def __init__(self, _stage: pxr.Usd.Stage, _sourcePath: pxr.Sdf.Path | str, /) -> None:
        """
        Construct the information for this struct from a property path.


        The source attribute does not have to exist, but the C{sourcePath}
        needs to have a valid prefix to identify the sourceType. The source
        prim needs to exist and be UsdShadeConnectableAPI compatible
        """
    def IsValid(self) -> bool:
        """
        Return true if this source info is valid for setting up a connection.
        """
    def __bool__(self) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...

class CoordSysAPI(pxr.Usd.APISchemaBase):
    '''
    UsdShadeCoordSysAPI provides a way to designate, name, and discover
    coordinate systems.


    Coordinate systems are implicitly established by UsdGeomXformable
    prims, using their local space. That coordinate system may be bound
    (i.e., named) from another prim. The binding is encoded as a single-
    target relationship. Coordinate system bindings apply to descendants
    of the prim where the binding is expressed, but names may be re-bound
    by descendant prims.

    CoordSysAPI is a multi-apply API schema, where instance names signify
    the named coordinate systems. The instance names are used with
    the"coordSys:"namespace to determine the binding to the
    UsdGeomXformable prim.

    Named coordinate systems are useful in shading (and other) workflows.
    An example is projection paint, which projects a texture from a
    certain view (the paint coordinate system), encoded as (e.g.)"rel
    coordSys:paint:binding". Using the paint coordinate frame avoids the
    need to assign a UV set to the object, and can be a concise way to
    project paint across a collection of objects with a single shared
    paint coordinate system.
    '''
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim, name: str | pxr.Ar.ResolvedPath) -> None:
        '''
        Construct a UsdShadeCoordSysAPI on UsdPrim C{prim} with name C{name}.


        Equivalent to UsdShadeCoordSysAPI::Get ( prim.GetStage(),
        prim.GetPath().AppendProperty("coordSys:name"));

        for a *valid* C{prim}, but will not immediately throw an error for an
        invalid C{prim}
        '''
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase, name: str | pxr.Ar.ResolvedPath) -> None:
        """
        Construct a UsdShadeCoordSysAPI on the prim held by C{schemaObj} with
        name C{name}.


        Should be preferred over UsdShadeCoordSysAPI (schemaObj.GetPrim(),
        name), as it preserves SchemaBase state.
        """
    @overload
    def __init__(self) -> None: ...
    @staticmethod
    def Apply(prim: pxr.Usd.Prim, name: str | pxr.Ar.ResolvedPath) -> CoordSysAPI:
        '''
        Applies this B{multiple-apply} API schema to the given C{prim} along
        with the given instance name, C{name}.


        This information is stored by adding"CoordSysAPI:<i>name</i>"to the
        token-valued, listOp metadata *apiSchemas* on the prim. For example,
        if C{name} is\'instance1\', the token\'CoordSysAPI:instance1\'is added
        to\'apiSchemas\'.

        A valid UsdShadeCoordSysAPI object is returned upon success. An
        invalid (or empty) UsdShadeCoordSysAPI object is returned upon
        failure. See UsdPrim::ApplyAPI() for conditions resulting in failure.

        UsdPrim::GetAppliedSchemas()

        UsdPrim::HasAPI()

        UsdPrim::CanApplyAPI()

        UsdPrim::ApplyAPI()

        UsdPrim::RemoveAPI()
        '''
    def ApplyAndBind(self, name: str | pxr.Ar.ResolvedPath, path: pxr.Sdf.Path | str) -> bool:
        """
        A convinience API for clients to use to Apply schema in accordance
        with new UsdShadeCoordSysAPI schema constructs and appropriate Bind
        the target.


        Note that this is only for clients using old behavior.

        Deprecated
        """
    @overload
    def Bind(self, name: str | pxr.Ar.ResolvedPath, path: pxr.Sdf.Path | str) -> bool:
        """
        Bind the name to the given path.


        The prim at the given path is expected to be UsdGeomXformable, in
        order for the binding to be succesfully resolved.

        Deprecated

        This method is deprecated as it operates on the old non-applied
        UsdShadeCoordSysAPI If USD_SHADE_COORD_SYS_IS_MULTI_APPLY is set to
        True, adds a binding conforming to the new multi-apply
        UsdShadeCoordSysAPI schema. If USD_SHADE_COORD_SYS_IS_MULTI_APPLY is
        set to Warn, try to also bind to multi-apply API compliant
        relationship for the prim, along with backward compatible deprecated
        behavior.
        """
    @overload
    def Bind(self, path: pxr.Sdf.Path | str) -> bool:
        """
        Bind the name to the given path.


        The prim at the given path is expected to be UsdGeomXformable, in
        order for the binding to be succesfully resolved.
        """
    def BlockBinding(self, name: str | pxr.Ar.ResolvedPath = ...) -> bool:
        """
        Block the indicated coordinate system binding on this prim by blocking
        targets on the underlying relationship.


        Deprecated

        This method is deprecated as it operates on the old non-applied
        UsdShadeCoordSysAPI If USD_SHADE_COORD_SYS_IS_MULTI_APPLY is set to
        True, blocks binding conforming to the new multi-apply
        UsdShadeCoordSysAPI schema. If USD_SHADE_COORD_SYS_IS_MULTI_APPLY is
        set to Warn, try to also block binding for multi-apply API compliant
        relationship for the prim, along with backward compatible deprecated
        behavior.
        """
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
    @staticmethod
    def CanContainPropertyName(name: str | pxr.Ar.ResolvedPath) -> bool:
        '''
        Test whether a given C{name} contains the"coordSys:"prefix.
        '''
    @overload
    def ClearBinding(self, name: str | pxr.Ar.ResolvedPath, removeSpec: bool) -> bool:
        """
        Clear the indicated coordinate system binding on this prim from the
        current edit target.


        Only remove the spec if C{removeSpec} is true (leave the spec to
        preserve meta-data we may have intentionally authored on the
        relationship)

        Deprecated

        This method is deprecated as it operates on the old non-applied
        UsdShadeCoordSysAPI If USD_SHADE_COORD_SYS_IS_MULTI_APPLY is set to
        True, clears a binding conforming to the new multi-apply
        UsdShadeCoordSysAPI schema. If USD_SHADE_COORD_SYS_IS_MULTI_APPLY is
        set to Warn, try to also clear binding for multi-apply API compliant
        relationship for the prim, along with backward compatible deprecated
        behavior.
        """
    @overload
    def ClearBinding(self, removeSpec: bool) -> bool:
        """
        Clear the coordinate system binding on the prim corresponding to the
        instanceName of this UsdShadeCoordSysAPI, from the current edit
        target.


        Only remove the spec if C{removeSpec} is true (leave the spec to
        preserve meta-data we may have intentionally authored on the
        relationship)
        """
    def CreateBindingRel(self) -> pxr.Usd.Relationship:
        """
        See GetBindingRel() , and also Create vs Get Property Methods for when
        to use Get vs Create.
        """
    def FindBindingWithInheritance(self) -> pxr.UsdSkel.Binding:
        """
        Find the coordinate system bindings that apply to this prim, including
        inherited bindings.


        This computation examines this prim and ancestors for the strongest
        binding for the specific instanceName. A binding expressed by a child
        prim supercedes bindings on ancestors. Only ancestor prims which have
        the UsdShadeCoordSysAPI :instanceName applied are considered.

        Note that this API does not validate the prims at the target paths;
        they may be of incorrect type, or missing entirely.

        Binding relationships with no resolved targets are skipped.
        """
    def FindBindingsWithInheritance(self) -> list[pxr.UsdSkel.Binding]:
        """
        Find the list of coordinate system bindings that apply to this prim,
        including inherited bindings.


        This computation examines this prim and ancestors for the strongest
        binding for each name. A binding expressed by a child prim supercedes
        bindings on ancestors.

        Note that this API does not validate the prims at the target paths;
        they may be of incorrect type, or missing entirely.

        Binding relationships with no resolved targets are skipped.

        Deprecated

        This method is deprecated as it operates on the old non-applied
        UsdShadeCoordSysAPI If USD_SHADE_COORD_SYS_IS_MULTI_APPLY is set to
        True, returns bindings conforming to the new multi-apply
        UsdShadeCoordSysAPI schema. If USD_SHADE_COORD_SYS_IS_MULTI_APPLY is
        set to Warn, try to get multi-apply API compliant local bindings for
        the prim, if none fallback to backward compatible deprecated behavior.
        """
    @staticmethod
    def FindBindingsWithInheritanceForPrim(_prim: pxr.Usd.Prim, /) -> list[pxr.UsdSkel.Binding]:
        """
        Find the list of coordinate system bindings that apply to this prim,
        including inherited bindings.


        This computation examines this prim and ancestors for the strongest
        binding for each name. A binding expressed by a child prim supercedes
        bindings on ancestors. Only prims which have the UsdShadeCoordSysAPI
        applied are considered and queried for a binding.

        Note that this API does not validate the prims at the target paths;
        they may be of incorrect type, or missing entirely.

        Binding relationships with no resolved targets are skipped.
        """
    @overload
    @staticmethod
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> CoordSysAPI:
        """
        Return a UsdShadeCoordSysAPI holding the prim adhering to this schema
        at C{path} on C{stage}.


        If no prim exists at C{path} on C{stage}, or if the prim at that path
        does not adhere to this schema, return an invalid schema object.
        C{path} must be of the format<path>.coordSys:name.

        This is shorthand for the following: ::

          TfToken name = SdfPath::StripNamespace(path.GetToken());
          UsdShadeCoordSysAPI(
              stage->GetPrimAtPath(path.GetPrimPath()), name);

        """
    @overload
    @staticmethod
    def Get(prim: pxr.Usd.Prim, name: str | pxr.Ar.ResolvedPath) -> CoordSysAPI:
        """
        Return a UsdShadeCoordSysAPI with name C{name} holding the prim
        C{prim}.


        Shorthand for UsdShadeCoordSysAPI(prim, name);
        """
    @staticmethod
    def GetAll(prim: pxr.Usd.Prim) -> list[CoordSysAPI]:
        """
        Return a vector of all named instances of UsdShadeCoordSysAPI on the
        given C{prim}.
        """
    def GetBindingRel(self) -> pxr.Usd.Relationship:
        """
        Prim binding expressing the appropriate coordinate systems.
        """
    @staticmethod
    def GetCoordSysRelationshipName(coordSysName: str | pxr.Ar.ResolvedPath) -> str:
        """
        Returns the fully namespaced coordinate system relationship name,
        given the coordinate system name.


        Deprecated

        This method is deprecated as it operates on the old non-applied
        UsdShadeCoordSysAPI
        """
    def GetLocalBinding(self) -> pxr.UsdSkel.Binding:
        """
        Get the coordinate system bindings local to this prim corresponding to
        this instance name.


        This does not process inherited bindings. It does not validate that a
        prim exists at the indicated path. If the binding relationship has
        multiple targets, only the first is used.
        """
    def GetLocalBindings(self) -> list[pxr.UsdSkel.Binding]:
        """
        Get the list of coordinate system bindings local to this prim.


        This does not process inherited bindings. It does not validate that a
        prim exists at the indicated path. If the binding relationship has
        multiple targets, only the first is used.

        Deprecated

        This method is deprecated as it operates on the old non-applied
        UsdShadeCoordSysAPI If USD_SHADE_COORD_SYS_IS_MULTI_APPLY is set to
        True, returns bindings conforming to the new multi-apply
        UsdShadeCoordSysAPI schema. If USD_SHADE_COORD_SYS_IS_MULTI_APPLY is
        set to Warn, try to get multi-apply API compliant local bindings for
        the prim, if none fallback to backward compatible deprecated behavior.
        """
    @staticmethod
    def GetLocalBindingsForPrim(prim: pxr.Usd.Prim) -> list[pxr.UsdSkel.Binding]:
        """
        Get the list of coordinate system bindings local to this prim, across
        all multi-apply instanceNames.


        This does not process inherited bindings. It does not validate that a
        prim exists at the indicated path. If the binding relationship has
        multiple targets, only the first is used.

        Note that this will always return empty vector of bindings if the
        C{prim} being queried does not have UsdShadeCoordSysAPI applied.
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
    def HasLocalBindings(self) -> bool:
        """
        Returns true if the prim has local coordinate system relationship
        exists.


        Deprecated

        This method is deprecated as it operates on the old non-applied
        UsdShadeCoordSysAPI If USD_SHADE_COORD_SYS_IS_MULTI_APPLY is set to
        True, if prim has appropriate API applied, that is conforming to the
        new behavior. If USD_SHADE_COORD_SYS_IS_MULTI_APPLY is set to Warn,
        try to see if multi-apply API compliant local bindings are present for
        the prim, if not fallback to backward compatible deprecated behavior.
        """
    @staticmethod
    def HasLocalBindingsForPrim(prim: pxr.Usd.Prim) -> bool:
        """
        Returns true if the prim has UsdShadeCoordSysAPI applied.


        Which implies it has the appropriate binding relationship(s).
        """
    @staticmethod
    def IsCoordSysAPIPath(_path: pxr.Sdf.Path | str, /) -> bool:
        """
        Checks if the given path C{path} is of an API schema of type
        CoordSysAPI.


        If so, it stores the instance name of the schema in C{name} and
        returns true. Otherwise, it returns false.
        """
    @staticmethod
    def _GetStaticTfType() -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...

class Input(Boost.Python.instance):
    """
    This class encapsulates a shader or node-graph input, which is a
    connectable attribute representing a typed value.
    """
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self, attr: pxr.Usd.Attribute | pxr.UsdGeom.ConstraintTarget | pxr.UsdGeom.Primvar | pxr.UsdGeom.XformOp | Input | Output) -> None:
        """
        Speculative constructor that will produce a valid UsdShadeInput when
        C{attr} already represents a shade Input, and produces an *invalid*
        UsdShadeInput otherwise (i.e.


        the explicit bool conversion operator will return false).
        """
    @overload
    def __init__(self) -> None:
        """
        Default constructor returns an invalid Input.


        Exists for the sake of container classes
        """
    def CanConnect(self, source: pxr.Usd.Attribute | pxr.UsdGeom.ConstraintTarget | pxr.UsdGeom.Primvar | pxr.UsdGeom.XformOp | Input | Output) -> bool:
        """
        Determines whether this Input can be connected to the given source
        attribute, which can be an input or an output.



        UsdShadeConnectableAPI::CanConnect
        """
    def ClearConnectability(self) -> bool:
        """
        Clears any authored connectability on the Input.
        """
    def ClearSdrMetadata(self) -> None:
        '''
        Clears any"sdrMetadata"value authored on the Input in the current
        EditTarget.
        '''
    def ClearSdrMetadataByKey(self, key: str | pxr.Ar.ResolvedPath) -> None:
        '''
        Clears the entry corresponding to the given C{key} in
        the"sdrMetadata"dictionary authored in the current EditTarget.
        '''
    def ClearSource(self) -> bool:
        """
        Deprecated
        """
    def ClearSources(self) -> bool:
        """
        Clears sources for this Input in the current UsdEditTarget.


        Most of the time, what you probably want is DisconnectSource() rather
        than this function.

        UsdShadeConnectableAPI::ClearSources
        """
    @overload
    def ConnectToSource(self, source: ConnectionSourceInfo, mod: ConnectionModification = ...) -> bool:
        """
        Authors a connection for this Input.


        C{source} is a struct that describes the upstream source attribute
        with all the information necessary to make a connection. See the
        documentation for UsdShadeConnectionSourceInfo. C{mod} describes the
        operation that should be applied to the list of connections. By
        default the new connection will replace any existing connections, but
        it can add to the list of connections to represent multiple input
        connections.

        C{true} if a connection was created successfully. C{false} if this
        input or C{source} is invalid.

        This method does not verify the connectability of the shading
        attribute to the source. Clients must invoke CanConnect() themselves
        to ensure compatibility.

        The source shading attribute is created if it doesn't exist already.

        UsdShadeConnectableAPI::ConnectToSource
        """
    @overload
    def ConnectToSource(self, source: ConnectableAPI, sourceName: str | pxr.Ar.ResolvedPath, sourceType: AttributeType = ..., typeName: pxr.Sdf.ValueTypeName = ...) -> bool:
        """
        Deprecated

        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        """
    @overload
    def ConnectToSource(self, sourcePath: pxr.Sdf.Path | str) -> bool:
        """
        Authors a connection for this Input to the source at the given path.



        UsdShadeConnectableAPI::ConnectToSource
        """
    @overload
    def ConnectToSource(self, input: Input) -> bool:
        """
        Connects this Input to the given input, C{sourceInput}.



        UsdShadeConnectableAPI::ConnectToSource
        """
    @overload
    def ConnectToSource(self, output: Output) -> bool:
        """
        Connects this Input to the given output, C{sourceOutput}.



        UsdShadeConnectableAPI::ConnectToSource
        """
    def DisconnectSource(self, sourceAttr: pxr.Usd.Attribute | pxr.UsdGeom.ConstraintTarget | pxr.UsdGeom.Primvar | pxr.UsdGeom.XformOp | Input | Output = ...) -> bool:
        """
        Disconnect source for this Input.


        If C{sourceAttr} is valid, only a connection to the specified
        attribute is disconnected, otherwise all connections are removed.

        UsdShadeConnectableAPI::DisconnectSource
        """
    def Get(self, time: pxr.Usd.TimeCode | float | pxr.Sdf.TimeCode = ...) -> Any:
        """
        Convenience wrapper for the templated UsdAttribute::Get() .
        """
    def GetAttr(self) -> pxr.Usd.Attribute:
        """
        Explicit UsdAttribute extractor.
        """
    def GetBaseName(self) -> str:
        '''
        Returns the name of the input.


        We call this the base name since it strips off the"inputs:"namespace
        prefix from the attribute name, and returns it.
        '''
    def GetConnectability(self) -> str:
        """
        Returns the connectability of the Input.



        SetConnectability()
        """
    def GetConnectedSource(self) -> tuple[ConnectableAPI, str, AttributeType]:
        """
        Deprecated
        """
    def GetConnectedSources(self) -> tuple[list[ConnectionSourceInfo], list[pxr.Sdf.Path]]:
        """
        Finds the valid sources of connections for the Input.


        C{invalidSourcePaths} is an optional output parameter to collect the
        invalid source paths that have not been reported in the returned
        vector.

        Returns a vector of C{UsdShadeConnectionSourceInfo} structs with
        information about each upsteam attribute. If the vector is empty,
        there have been no valid connections.

        A valid connection requires the existence of the source attribute and
        also requires that the source prim is UsdShadeConnectableAPI
        compatible.

        The python wrapping returns a tuple with the valid connections first,
        followed by the invalid source paths.

        UsdShadeConnectableAPI::GetConnectedSources
        """
    def GetDisplayGroup(self) -> str:
        """
        Get the displayGroup metadata for this Input, i.e.


        hint for the location and nesting of the attribute.

        UsdProperty::GetDisplayGroup() , UsdProperty::GetNestedDisplayGroup()
        """
    def GetDocumentation(self) -> str:
        """
        Get documentation string for this Input.



        UsdObject::GetDocumentation()
        """
    def GetFullName(self) -> str:
        """
        Get the name of the attribute associated with the Input.
        """
    def GetPrim(self) -> pxr.Usd.Prim:
        """
        Get the prim that the input belongs to.
        """
    def GetRawConnectedSourcePaths(self) -> list[pxr.Sdf.Path]:
        '''
        Deprecated

        Returns the"raw"(authored) connected source paths for this Input.

        UsdShadeConnectableAPI::GetRawConnectedSourcePaths
        '''
    def GetRenderType(self) -> str:
        """
        Return this Input's specialized renderType, or an empty token if none
        was authored.



        SetRenderType()
        """
    def GetSdrMetadata(self) -> dict[str, str]:
        '''
        Returns this Input\'s composed"sdrMetadata"dictionary as a NdrTokenMap.
        '''
    def GetSdrMetadataByKey(self, key: str | pxr.Ar.ResolvedPath) -> str:
        """
        Returns the value corresponding to C{key} in the composed
        B{sdrMetadata} dictionary.
        """
    def GetTypeName(self) -> pxr.Sdf.ValueTypeName:
        '''
        Get the"scene description"value type name of the attribute associated
        with the Input.
        '''
    def GetValueProducingAttribute(self) -> tuple[pxr.Usd.Attribute, AttributeType]:
        """
        Deprecated

        in favor of calling GetValueProducingAttributes
        """
    def GetValueProducingAttributes(self, shaderOutputsOnly: bool = ...) -> list[Attribute]:
        """
        Find what is connected to this Input recursively.



        UsdShadeUtils::GetValueProducingAttributes
        """
    def HasConnectedSource(self) -> bool:
        """
        Returns true if and only if this Input is currently connected to a
        valid (defined) source.



        UsdShadeConnectableAPI::HasConnectedSource
        """
    def HasRenderType(self) -> bool:
        """
        Return true if a renderType has been specified for this Input.



        SetRenderType()
        """
    def HasSdrMetadata(self) -> bool:
        '''
        Returns true if the Input has a non-empty
        composed"sdrMetadata"dictionary value.
        '''
    def HasSdrMetadataByKey(self, key: str | pxr.Ar.ResolvedPath) -> bool:
        '''
        Returns true if there is a value corresponding to the given C{key} in
        the composed"sdrMetadata"dictionary.
        '''
    @staticmethod
    def IsInput(_attr: pxr.Usd.Attribute | pxr.UsdGeom.ConstraintTarget | pxr.UsdGeom.Primvar | pxr.UsdGeom.XformOp | Input | Output, /) -> bool:
        """
        Test whether a given UsdAttribute represents a valid Input, which
        implies that creating a UsdShadeInput from the attribute will succeed.


        Success implies that C{attr.IsDefined()} is true.
        """
    @staticmethod
    def IsInterfaceInputName(_name: str | pxr.Ar.ResolvedPath, /) -> bool:
        """
        Test if this name has a namespace that indicates it could be an input.
        """
    def IsSourceConnectionFromBaseMaterial(self) -> bool:
        """
        Returns true if the connection to this Input's source, as returned by
        GetConnectedSource() , is authored across a specializes arc, which is
        used to denote a base material.



        UsdShadeConnectableAPI::IsSourceConnectionFromBaseMaterial
        """
    def Set(self, value: Any, time: pxr.Usd.TimeCode | float | pxr.Sdf.TimeCode = ...) -> bool:
        """
        Set a value for the Input at C{time}.
        """
    def SetConnectability(self, _connectability: str | pxr.Ar.ResolvedPath, /) -> bool:
        '''
        Set the connectability of the Input.


        In certain shading data models, there is a need to distinguish which
        inputs B{can} vary over a surface from those that must be B{uniform}.
        This is accomplished in UsdShade by limiting the connectability of the
        input. This is done by setting the"connectability"metadata on the
        associated attribute.

        Connectability of an Input can be set to UsdShadeTokens->full or
        UsdShadeTokens->interfaceOnly.

           - B{full} implies that the Input can be connected to any other
             Input or Output.

           - B{interfaceOnly} implies that the Input can only be connected to
             a NodeGraph Input (which represents an interface override, not a
             render-time dataflow connection), or another Input whose
             connectability is also"interfaceOnly".
             The default connectability of an input is UsdShadeTokens->full.

        SetConnectability()
        '''
    def SetConnectedSources(self, _sourceInfos: typing.Iterable[ConnectionSourceInfo], /) -> bool:
        """
        Connects this Input to the given sources, C{sourceInfos}.



        UsdShadeConnectableAPI::SetConnectedSources
        """
    def SetDisplayGroup(self, _displayGroup: str | pxr.Ar.ResolvedPath, /) -> bool:
        '''
        Set the displayGroup metadata for this Input, i.e.


        hinting for the location and nesting of the attribute.

        Note for an input representing a nested SdrShaderProperty, its
        expected to have the scope delimited by a":".

        UsdProperty::SetDisplayGroup() , UsdProperty::SetNestedDisplayGroup()

        SdrShaderProperty::GetPage()
        '''
    def SetDocumentation(self, _docs: str | pxr.Ar.ResolvedPath, /) -> bool:
        """
        Set documentation string for this Input.



        UsdObject::SetDocumentation()
        """
    def SetRenderType(self, renderType: str | pxr.Ar.ResolvedPath) -> bool:
        '''
        Specify an alternative, renderer-specific type to use when
        emitting/translating this Input, rather than translating based on its
        GetTypeName()


        For example, we set the renderType to"struct"for Inputs that are of
        renderman custom struct types.

        true on success.
        '''
    def SetSdrMetadata(self, sdrMetadata: dict[str | pxr.Ar.ResolvedPath, str | pxr.Ar.ResolvedPath]) -> None:
        """
        Authors the given C{sdrMetadata} value on this Input at the current
        EditTarget.
        """
    def SetSdrMetadataByKey(self, key: str | pxr.Ar.ResolvedPath, value: str | pxr.Ar.ResolvedPath) -> None:
        '''
        Sets the value corresponding to C{key} to the given string C{value},
        in the Input\'s"sdrMetadata"dictionary at the current EditTarget.
        '''
    def __bool__(self) -> bool:
        """
        Return true if this Input is valid for querying and authoring values
        and metadata, which is identically equivalent to IsDefined() .
        """
    def __eq__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...

class Material(NodeGraph):
    '''
    A Material provides a container into which multiple"render
    contexts"can add data that defines a"shading material"for a renderer.


    Typically this consists of one or more UsdShadeOutput properties
    connected to outputs of nested Shader prims - though a context/client
    is free to add any data that is suitable. We B{strongly advise} that
    all contexts adopt the convention that all properties be prefixed with
    a namespace that identifies the context e.g."token
    outputs:ri:surface.connect
    =</MyselfMaterial/previewSurface.outputs:surface".

    In the UsdShading model, geometry expresses a binding to a single
    Material or to a set of Materials partitioned by UsdGeomSubsets
    defined beneath the geometry; it is legal to bind a Material at the
    root (or other sub-prim) of a model, and then bind a different
    Material to individual gprims, but the meaning of inheritance
    and"ancestral overriding"of Material bindings is left to each render-
    target to determine. Since UsdGeom has no concept of shading, we
    provide the API for binding and unbinding geometry on the API schema
    UsdShadeMaterialBindingAPI.

    The entire power of USD VariantSets and all the other composition
    operators can leveraged when encoding shading variation.
    UsdShadeMaterial provides facilities for a particular way of
    building"Material variants"in which neither the identity of the
    Materials themselves nor the geometry Material-bindings need to change
    - instead we vary the targeted networks, interface values, and even
    parameter values within a single variantSet.  See Authoring Material
    Variations for more details.

    UsdShade requires that all of the shaders that"belong"to the Material
    live under the Material in namespace. This supports powerful, easy
    reuse of Materials, because it allows us to *reference* a Material
    from one asset (the asset might be a module of Materials) into
    another asset: USD references compose all descendant prims of the
    reference target into the referencer\'s namespace, which means that all
    of the referenced Material\'s shader networks will come along with the
    Material. When referenced in this way, Materials can also be
    instanced, for ease of deduplication and compactness. Finally,
    Material encapsulation also allows us to specialize child materials
    from parent materials.

    For any described attribute *Fallback* *Value* or *Allowed* *Values*
    below that are text/tokens, the actual token is published and defined
    in UsdShadeTokens. So to set an attribute to the value"rightHanded",
    use UsdShadeTokens->rightHanded as the value.
    '''
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None:
        """
        Construct a UsdShadeMaterial on UsdPrim C{prim}.


        Equivalent to UsdShadeMaterial::Get (prim.GetStage(), prim.GetPath())
        for a *valid* C{prim}, but will not immediately throw an error for an
        invalid C{prim}
        """
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None:
        """
        Construct a UsdShadeMaterial on the prim held by C{schemaObj}.


        Should be preferred over UsdShadeMaterial (schemaObj.GetPrim()), as it
        preserves SchemaBase state.
        """
    def ClearBaseMaterial(self) -> None:
        """
        Clear the base Material of this Material.
        """
    def ComputeDisplacementSource(self, renderContext: str | pxr.Ar.ResolvedPath = ...) -> tuple[Shader, str, AttributeType]:
        """
        Deprecated

        Use the form that takes a TfTokenVector or renderContexts
        """
    def ComputeSurfaceSource(self, renderContext: str | pxr.Ar.ResolvedPath = ...) -> tuple[Shader, str, AttributeType]:
        """
        Deprecated

        Use the form that takes a TfTokenVector or renderContexts.
        """
    def ComputeVolumeSource(self, renderContext: str | pxr.Ar.ResolvedPath = ...) -> tuple[Shader, str, AttributeType]:
        """
        Deprecated

        Use the form that takes a TfTokenVector or renderContexts
        """
    def CreateDisplacementAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetDisplacementAttr() , and also Create vs Get Property Methods
        for when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateDisplacementOutput(self, renderContext: str | pxr.Ar.ResolvedPath = ...) -> Output:
        '''
        Creates and returns the"displacement"output on this material for the
        specified C{renderContext}.


        If the output already exists on the material, it is returned and no
        authoring is performed. The returned output will always have the
        requested renderContext.
        '''
    @staticmethod
    def CreateMasterMaterialVariant(masterPrim: pxr.Usd.Prim, materialPrims: typing.Iterable[pxr.Usd.Prim], masterVariantSetName: str | pxr.Ar.ResolvedPath = ...) -> bool:
        '''
        Create a variantSet on C{masterPrim} that will set the MaterialVariant
        on each of the given *MaterialPrims*.


        The variantSet, whose name can be specified with
        C{masterVariantSetName} and defaults to the same MaterialVariant name
        created on Materials by GetEditContextForVariant() , will have the
        same variants as the Materials, and each Master variant will set every
        C{MaterialPrims\'} MaterialVariant selection to the same variant as the
        master. Thus, it allows all Materials to be switched with a single
        variant selection, on C{masterPrim}.

        If C{masterPrim} is an ancestor of any given member of
        C{MaterialPrims}, then we will author variant selections directly on
        the MaterialPrims. However, it is often preferable to create a master
        MaterialVariant in a separately rooted tree from the MaterialPrims, so
        that it can be layered more strongly on top of the Materials.
        Therefore, for any MaterialPrim in a different tree than masterPrim,
        we will create"overs"as children of masterPrim that recreate the path
        to the MaterialPrim, substituting masterPrim\'s full path for the
        MaterialPrim\'s root path component.

        Upon successful completion, the new variantSet we created on
        C{masterPrim} will have its variant selection authored to
        the"last"variant (determined lexicographically). It is up to the
        calling client to either UsdVariantSet::ClearVariantSelection() on
        C{masterPrim}, or set the selection to the desired default setting.

        Return C{true} on success. It is an error if any of C{Materials} have
        a different set of variants for the MaterialVariant than the others.
        '''
    def CreateSurfaceAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetSurfaceAttr() , and also Create vs Get Property Methods for
        when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateSurfaceOutput(self, renderContext: str | pxr.Ar.ResolvedPath = ...) -> Output:
        '''
        Creates and returns the"surface"output on this material for the
        specified C{renderContext}.


        If the output already exists on the material, it is returned and no
        authoring is performed. The returned output will always have the
        requested renderContext.
        '''
    def CreateVolumeAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetVolumeAttr() , and also Create vs Get Property Methods for when
        to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateVolumeOutput(self, renderContext: str | pxr.Ar.ResolvedPath = ...) -> Output:
        '''
        Creates and returns the"volume"output on this material for the
        specified C{renderContext}.


        If the output already exists on the material, it is returned and no
        authoring is performed. The returned output will always have the
        requested renderContext.
        '''
    @staticmethod
    def Define(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> Material:
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
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> Material:
        """
        Return a UsdShadeMaterial holding the prim adhering to this schema at
        C{path} on C{stage}.


        If no prim exists at C{path} on C{stage}, or if the prim at that path
        does not adhere to this schema, return an invalid schema object. This
        is shorthand for the following: ::

          UsdShadeMaterial(stage->GetPrimAtPath(path));

        """
    def GetBaseMaterial(self) -> Material:
        """
        Get the path to the base Material of this Material.


        If there is no base Material, an empty Material is returned
        """
    def GetBaseMaterialPath(self) -> pxr.Sdf.Path:
        """
        Get the base Material of this Material.


        If there is no base Material, an empty path is returned
        """
    def GetDisplacementAttr(self) -> pxr.Usd.Attribute:
        '''
        Represents the universal"displacement"output terminal of a material.



        Declaration

        C{token outputs:displacement}

        C++ Type

        TfToken

        Usd Type

        SdfValueTypeNames->Token
        '''
    def GetDisplacementOutput(self, renderContext: str | pxr.Ar.ResolvedPath = ...) -> Output:
        '''
        Returns the"displacement"output of this material for the specified
        renderContext.


        The returned output will always have the requested renderContext.

        An invalid output is returned if an output corresponding to the
        requested specific-renderContext does not exist.

        UsdShadeMaterial::ComputeDisplacementSource()
        '''
    def GetDisplacementOutputs(self) -> list[Output]:
        '''
        Returns the"displacement"outputs of this material for all available
        renderContexts.


        The returned vector will include all authored"displacement"outputs
        with the *universal* renderContext output first, if present. Outputs
        are returned regardless of whether they are connected to a valid
        source.
        '''
    def GetEditContextForVariant(self, materialVariantName: str | pxr.Ar.ResolvedPath, layer: pxr.Sdf.Layer = ...) -> pxr.Usd.EditContext:
        '''
        Helper function for configuring a UsdStage \'s UsdEditTarget to author
        Material variations.


        Takes care of creating the Material variantSet and specified variant,
        if necessary.

        Let\'s assume that we are authoring Materials into the Stage\'s current
        UsdEditTarget, and that we are iterating over the variations of a
        UsdShadeMaterial *clothMaterial*, and *currVariant* is the variant we
        are processing (e.g."denim").

        In C++, then, we would use the following pattern: ::

          {
              UsdEditContext ctxt(clothMaterial.GetEditContextForVariant(currVariant));
  
              // All USD mutation of the UsdStage on which clothMaterial sits will
              // now go "inside" the currVariant of the "MaterialVariant" variantSet
          }

        In python, the pattern is: ::

          with clothMaterial.GetEditContextForVariant(currVariant):
              # Now sending mutations to currVariant

        If C{layer} is specified, then we will use it, rather than the stage\'s
        current UsdEditTarget \'s layer as the destination layer for the edit
        context we are building. If C{layer} does not actually contribute to
        the Material prim\'s definition, any editing will have no effect on
        this Material.

        B{Note:} As just stated, using this method involves authoring a
        selection for the MaterialVariant in the stage\'s current EditTarget.
        When client is done authoring variations on this prim, they will
        likely want to either UsdVariantSet::SetVariantSelection() to the
        appropriate default selection, or possibly
        UsdVariantSet::ClearVariantSelection() on the
        UsdShadeMaterial::GetMaterialVariant() UsdVariantSet.

        UsdVariantSet::GetVariantEditContext()
        '''
    def GetMaterialVariant(self) -> pxr.Usd.VariantSet:
        """
        Return a UsdVariantSet object for interacting with the Material
        variant variantSet.
        """
    @staticmethod
    def GetSchemaAttributeNames(includeInherited: bool = ...) -> list[str]:
        """
        Return a vector of names of all pre-declared attributes for this
        schema class and all its ancestor classes.


        Does not include attributes that may be authored by custom/extended
        methods of the schemas involved.
        """
    def GetSurfaceAttr(self) -> pxr.Usd.Attribute:
        '''
        Represents the universal"surface"output terminal of a material.



        Declaration

        C{token outputs:surface}

        C++ Type

        TfToken

        Usd Type

        SdfValueTypeNames->Token
        '''
    def GetSurfaceOutput(self, renderContext: str | pxr.Ar.ResolvedPath = ...) -> Output:
        '''
        Returns the"surface"output of this material for the specified
        C{renderContext}.


        The returned output will always have the requested renderContext.

        An invalid output is returned if an output corresponding to the
        requested specific-renderContext does not exist.

        UsdShadeMaterial::ComputeSurfaceSource()
        '''
    def GetSurfaceOutputs(self) -> list[Output]:
        '''
        Returns the"surface"outputs of this material for all available
        renderContexts.


        The returned vector will include all authored"surface"outputs with the
        *universal* renderContext output first, if present. Outputs are
        returned regardless of whether they are connected to a valid source.
        '''
    def GetVolumeAttr(self) -> pxr.Usd.Attribute:
        '''
        Represents the universal"volume"output terminal of a material.



        Declaration

        C{token outputs:volume}

        C++ Type

        TfToken

        Usd Type

        SdfValueTypeNames->Token
        '''
    def GetVolumeOutput(self, renderContext: str | pxr.Ar.ResolvedPath = ...) -> Output:
        '''
        Returns the"volume"output of this material for the specified
        renderContext.


        The returned output will always have the requested renderContext.

        An invalid output is returned if an output corresponding to the
        requested specific-renderContext does not exist.

        UsdShadeMaterial::ComputeVolumeSource()
        '''
    def GetVolumeOutputs(self) -> list[Output]:
        '''
        Returns the"volume"outputs of this material for all available
        renderContexts.


        The returned vector will include all authored"volume"outputs with the
        *universal* renderContext output first, if present. Outputs are
        returned regardless of whether they are connected to a valid source.
        '''
    def HasBaseMaterial(self) -> bool: ...
    def SetBaseMaterial(self, baseMaterial: Material) -> None:
        """
        Set the base Material of this Material.


        An empty Material is equivalent to clearing the base Material.
        """
    def SetBaseMaterialPath(self, baseLookPath: pxr.Sdf.Path | str) -> None:
        """
        Set the path to the base Material of this Material.


        An empty path is equivalent to clearing the base Material.
        """
    @staticmethod
    def _GetStaticTfType() -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...

class MaterialBindingAPI(pxr.Usd.APISchemaBase):
    '''
    UsdShadeMaterialBindingAPI is an API schema that provides an interface
    for binding materials to prims or collections of prims (represented by
    UsdCollectionAPI objects).


    In the USD shading model, each renderable gprim computes a single
    B{resolved Material} that will be used to shade the gprim (exceptions,
    of course, for gprims that possess UsdGeomSubsets, as each subset can
    be shaded by a different Material). A gprim B{and each of its ancestor
    prims} can possess, through the MaterialBindingAPI, both a B{direct}
    binding to a Material, and any number of B{collection-based} bindings
    to Materials; each binding can be generic or declared for a particular
    B{purpose}, and given a specific B{binding strength}. It is the
    process of"material resolution"(see
    UsdShadeMaterialBindingAPI_MaterialResolution) that examines all of
    these bindings, and selects the one Material that best matches the
    client\'s needs.

    The intent of B{purpose} is that each gprim should be able to resolve
    a Material for any given purpose, which implies it can have
    differently bound materials for different purposes. There are two
    *special* values of B{purpose} defined in UsdShade, although the API
    fully supports specifying arbitrary values for it, for the sake of
    extensibility:
       - B{UsdShadeTokens->full} : to be used when the purpose of the
         render is entirely to visualize the truest representation of a scene,
         considering all lighting and material information, at highest
         fidelity.

       - B{UsdShadeTokens->preview} : to be used when the render is in
         service of a goal other than a high fidelity"full"render (such as
         scene manipulation, modeling, or realtime playback). Latency and speed
         are generally of greater concern for preview renders, therefore
         preview materials are generally designed to be"lighterweight"compared
         to full materials.
         A binding can also have no specific purpose at all, in which case, it
         is considered to be the fallback or all-purpose binding (denoted by
         the empty-valued token B{UsdShadeTokens->allPurpose}).

    The B{purpose} of a material binding is encoded in the name of the
    binding relationship.
       - In the case of a direct binding, the *allPurpose* binding is
         represented by the relationship named B{material:binding}. Special-
         purpose direct bindings are represented by relationships named
         B{material:binding: *purpose*}. A direct binding relationship must
         have a single target path that points to a B{UsdShadeMaterial}.

       - In the case of a collection-based binding, the *allPurpose*
         binding is represented by a relationship named
         B{material:binding:collection: *bindingName*}, where B{bindingName}
         establishes an identity for the binding that is unique on the prim.
         Attempting to establish two collection bindings of the same name on
         the same prim will result in the first binding simply being
         overridden. A special-purpose collection-based binding is represented
         by a relationship named B{material:binding:collection:
         *purpose:bindingName*}. A collection-based binding relationship must
         have exacly two targets, one of which should be a collection-path (see
         ef UsdCollectionAPI::GetCollectionPath() ) and the other should point
         to a B{UsdShadeMaterial}. In the future, we may allow a single
         collection binding to target multiple collections, if we can establish
         a reasonable round-tripping pattern for applications that only allow a
         single collection to be associated with each Material.

    B{Note:} Both B{bindingName} and B{purpose} must be non-namespaced
    tokens. This allows us to know the role of a binding relationship
    simply from the number of tokens in it.
       - B{Two tokens} : the fallback,"all purpose", direct binding,
         *material:binding*

       - B{Three tokens} : a purpose-restricted, direct, fallback binding,
         e.g. material:binding:preview

       - B{Four tokens} : an all-purpose, collection-based binding, e.g.
         material:binding:collection:metalBits

       - B{Five tokens} : a purpose-restricted, collection-based binding,
         e.g. material:binding:collection:full:metalBits

    A B{binding-strength} value is used to specify whether a binding
    authored on a prim should be weaker or stronger than bindings that
    appear lower in namespace. We encode the binding strength with as
    token-valued metadata B{\'bindMaterialAs\'} for future flexibility, even
    though for now, there are only two possible values:
    *UsdShadeTokens->weakerThanDescendants* and
    *UsdShadeTokens->strongerThanDescendants*. When binding-strength is
    not authored (i.e. empty) on a binding-relationship, the default
    behavior matches UsdShadeTokens->weakerThanDescendants.

    If a material binding relationship is a built-in property defined as
    part of a typed prim\'s schema, a fallback value should not be provided
    for it. This is because the"material resolution"algorithm only
    conisders *authored* properties.
    '''

    class CollectionBinding(Boost.Python.instance):
        """
        This struct is used to represent a collection-based material binding,
        which contains two objects - a collection and a bound material.
        """
        __instance_size__: ClassVar[int] = ...
        @overload
        def __init__(self) -> None:
            """
            Default constructor initializes a CollectionBinding object with
            invalid collection, material and bindingRel data members.
            """
        @overload
        def __init__(self, collBindingRel: pxr.Usd.Relationship) -> None:
            """
            Constructs a CollectionBinding object from the given collection-
            binding relationship.


            This inspects the targets of the relationship and determines the bound
            collection and the target material that the collection is bound to.
            """
        def GetBindingRel(self) -> pxr.Usd.Relationship:
            """
            Returns the binding-relationship that represents this collection-
            based binding.
            """
        def GetCollection(self) -> pxr.Usd.CollectionAPI:
            """
            Constructs and returns the CollectionAPI object for the collection
            that is bound by this collection-binding.
            """
        def GetCollectionPath(self) -> pxr.Sdf.Path:
            """
            Returns the path to the collection that is bound by this binding.
            """
        def GetMaterial(self) -> Material:
            """
            Constructs and returns the material object that this collection-based
            binding binds to.
            """
        def GetMaterialPath(self) -> pxr.Sdf.Path:
            """
            Returns the path to the material that is bound to by this binding.
            """
        @staticmethod
        def IsCollectionBindingRel(bindingRel: pxr.Usd.Relationship) -> bool:
            """
            Checks if the C{bindingRel} identifies a collection.
            """
        def IsValid(self) -> bool:
            """
            Returns true if the CollectionBinding points to a non-empty material
            path and collection.
            """

    class DirectBinding(Boost.Python.instance):
        """
        This class represents a direct material binding.
        """
        __instance_size__: ClassVar[int] = ...
        @overload
        def __init__(self) -> None:
            """
            Default constructor initializes a DirectBinding object with invalid
            material and bindingRel data members.
            """
        @overload
        def __init__(self, bindingRel: pxr.Usd.Relationship) -> None: ...
        def GetBindingRel(self) -> pxr.Usd.Relationship:
            """
            Returns the binding-relationship that represents this direct binding.
            """
        def GetMaterial(self) -> Material:
            """
            Gets the material object that this direct binding binds to.
            """
        def GetMaterialPath(self) -> pxr.Sdf.Path:
            """
            Returns the path to the material that is bound to by this direct
            binding.
            """
        def GetMaterialPurpose(self) -> str:
            """
            Returns the purpose of the direct binding.
            """
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None:
        """
        Construct a UsdShadeMaterialBindingAPI on UsdPrim C{prim}.


        Equivalent to UsdShadeMaterialBindingAPI::Get (prim.GetStage(),
        prim.GetPath()) for a *valid* C{prim}, but will not immediately throw
        an error for an invalid C{prim}
        """
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None:
        """
        Construct a UsdShadeMaterialBindingAPI on the prim held by
        C{schemaObj}.


        Should be preferred over UsdShadeMaterialBindingAPI
        (schemaObj.GetPrim()), as it preserves SchemaBase state.
        """
    def AddPrimToBindingCollection(self, prim: pxr.Usd.Prim, bindingName: str | pxr.Ar.ResolvedPath, materialPurpose: str | pxr.Ar.ResolvedPath = ...) -> bool:
        """
        Adds the specified C{prim} to the collection targeted by the binding
        relationship corresponding to given C{bindingName} and
        C{materialPurpose}.


        If the collection-binding relationship doesn't exist or if the
        targeted collection already includes the C{prim}, then this does
        nothing and returns true.

        If the targeted collection does not include C{prim} (or excludes it
        explicitly), then this modifies the collection by adding the prim to
        it (by invoking UsdCollectionAPI::AddPrim()).
        """
    @staticmethod
    def Apply(prim: pxr.Usd.Prim) -> MaterialBindingAPI:
        '''
        Applies this B{single-apply} API schema to the given C{prim}.


        This information is stored by adding"MaterialBindingAPI"to the token-
        valued, listOp metadata *apiSchemas* on the prim.

        A valid UsdShadeMaterialBindingAPI object is returned upon success. An
        invalid (or empty) UsdShadeMaterialBindingAPI object is returned upon
        failure. See UsdPrim::ApplyAPI() for conditions resulting in failure.

        UsdPrim::GetAppliedSchemas()

        UsdPrim::HasAPI()

        UsdPrim::CanApplyAPI()

        UsdPrim::ApplyAPI()

        UsdPrim::RemoveAPI()
        '''
    @overload
    def Bind(self, material: Material, bindingStrength: str | pxr.Ar.ResolvedPath = ..., materialPurpose: str | pxr.Ar.ResolvedPath = ...) -> bool:
        """
        Authors a direct binding to the given C{material} on this prim.


        If C{bindingStrength} is UsdShadeTokens->fallbackStrength, the value
        UsdShadeTokens->weakerThanDescendants is authored sparsely. To stamp
        out the bindingStrength value explicitly, clients can pass in
        UsdShadeTokens->weakerThanDescendants or
        UsdShadeTokens->strongerThanDescendants directly.

        If C{materialPurpose} is specified and isn't equal to
        UsdShadeTokens->allPurpose, the binding only applies to the specified
        material purpose.

        Note that UsdShadeMaterialBindingAPI is a SingleAppliedAPI schema
        which when applied updates the prim definition accordingly. This
        information on the prim definition is helpful in multiple queries and
        more performant. Hence its recommended to call
        UsdShadeMaterialBindingAPI::Apply() when Binding a material.

        Returns true on success, false otherwise.
        """
    @overload
    def Bind(self, collection: pxr.Usd.CollectionAPI, material: Material, bindingName: str | pxr.Ar.ResolvedPath = ..., bindingStrength: str | pxr.Ar.ResolvedPath = ..., materialPurpose: str | pxr.Ar.ResolvedPath = ...) -> bool:
        """
        Authors a collection-based binding, which binds the given C{material}
        to the given C{collection} on this prim.


        C{bindingName} establishes an identity for the binding that is unique
        on the prim. Attempting to establish two collection bindings of the
        same name on the same prim will result in the first binding simply
        being overridden. If C{bindingName} is empty, it is set to the base-
        name of the collection being bound (which is the collection-name with
        any namespaces stripped out). If there are multiple collections with
        the same base-name being bound at the same prim, clients should pass
        in a unique binding name per binding, in order to preserve all
        bindings. The binding name used in constructing the collection-binding
        relationship name shoud not contain namespaces. Hence, a coding error
        is issued and no binding is authored if the provided value of
        C{bindingName} is non-empty and contains namespaces.

        If C{bindingStrength} is *UsdShadeTokens->fallbackStrength*, the value
        UsdShadeTokens->weakerThanDescendants is authored sparsely, i.e. only
        when there is an existing binding with a different bindingStrength. To
        stamp out the bindingStrength value explicitly, clients can pass in
        UsdShadeTokens->weakerThanDescendants or
        UsdShadeTokens->strongerThanDescendants directly.

        If C{materialPurpose} is specified and isn't equal to
        UsdShadeTokens->allPurpose, the binding only applies to the specified
        material purpose.

        Note that UsdShadeMaterialBindingAPI is a SingleAppliedAPI schema
        which when applied updates the prim definition accordingly. This
        information on the prim definition is helpful in multiple queries and
        more performant. Hence its recommended to call
        UsdShadeMaterialBindingAPI::Apply() when Binding a material.

        Returns true on success, false otherwise.
        """
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
    def CanContainPropertyName(name: str | pxr.Ar.ResolvedPath) -> bool:
        '''
        Test whether a given C{name} contains the"material:binding:"prefix.
        '''
    def ComputeBoundMaterial(self, materialPurpose: object = ..., supportLegacyBindings: bool = ...) -> Any: ...
    @staticmethod
    def ComputeBoundMaterials(prims: typing.Iterable[pxr.Usd.Prim], materialPurpose: str | pxr.Ar.ResolvedPath = ..., supportLegacyBindings: bool = ...) -> tuple[list[Material], list[pxr.Usd.Relationship]]:
        '''
        Static API for efficiently and concurrently computing the resolved
        material bindings for a vector of UsdPrims, C{prims} for the given
        C{materialPurpose}.


        The size of the returned vector always matches the size of the input
        vector, C{prims}. If a prim is not bound to any material, an invalid
        or empty UsdShadeMaterial is returned at the index corresponding to
        it.

        If the pointer C{bindingRels} points to a valid vector, then it is
        populated with the set of all"winning"binding relationships.

        In order for backward compatibility with old assets not having
        MaterialBindingAPI applied, C{supportLegacyBindings} defaults to true.
        Though its recommended for clients to update the assets to have
        MaterialBindingAPI applied for optimized computation of bound
        material.

        Note: In a future release the default for C{supportLegacyBindings}
        will be updated to"false".

        The python version of this method returns a tuple containing two lists
        - the bound materials and the corresponding"winning"binding
        relationships.
        '''
    def CreateMaterialBindSubset(self, subsetName: str | pxr.Ar.ResolvedPath, indices: pxr.Vt.IntArray | typing.Iterable[int], elementType: str | pxr.Ar.ResolvedPath = ...) -> pxr.UsdGeom.Subset:
        '''
        Creates a GeomSubset named C{subsetName} with element type,
        C{elementType} and familyName B{materialBind B{below this prim.}}


        If a GeomSubset named C{subsetName} already exists, then
        its"familyName"is updated to be UsdShadeTokens->materialBind and its
        indices (at *default* timeCode) are updated with the provided
        C{indices} value before returning.

        This method forces the familyType of the"materialBind"family of
        subsets to UsdGeomTokens->nonOverlapping if it\'s unset or explicitly
        set to UsdGeomTokens->unrestricted.

        The default value C{elementType} is UsdGeomTokens->face, as we expect
        materials to be bound most often to subsets of faces on meshes.
        '''
    @staticmethod
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> MaterialBindingAPI:
        """
        Return a UsdShadeMaterialBindingAPI holding the prim adhering to this
        schema at C{path} on C{stage}.


        If no prim exists at C{path} on C{stage}, or if the prim at that path
        does not adhere to this schema, return an invalid schema object. This
        is shorthand for the following: ::

          UsdShadeMaterialBindingAPI(stage->GetPrimAtPath(path));

        """
    def GetCollectionBindingRel(self, bindingName: str | pxr.Ar.ResolvedPath, materialPurpose: str | pxr.Ar.ResolvedPath = ...) -> pxr.Usd.Relationship:
        """
        Returns the collection-based material-binding relationship with the
        given C{bindingName} and C{materialPurpose} on this prim.


        For info on C{bindingName}, see UsdShadeMaterialBindingAPI::Bind() .
        The material purpose of the relationship that's returned will match
        the specified C{materialPurpose}.
        """
    def GetCollectionBindingRels(self, materialPurpose: str | pxr.Ar.ResolvedPath = ...) -> list[pxr.Usd.Relationship]:
        """
        Returns the list of collection-based material binding relationships on
        this prim for the given material purpose, C{materialPurpose}.


        The returned list of binding relationships will be in native property
        order. See UsdPrim::GetPropertyOrder() , UsdPrim::SetPropertyOrder() .
        Bindings that appear earlier in the property order are considered to
        be stronger than the ones that come later. See rule #6 in
        UsdShadeMaterialBindingAPI_MaterialResolution.
        """
    def GetCollectionBindings(self, materialPurpose: str | pxr.Ar.ResolvedPath = ...) -> list[MaterialBindingAPI.CollectionBinding]:
        """
        Returns all the collection-based bindings on this prim for the given
        material purpose.


        The returned CollectionBinding objects always have the specified
        C{materialPurpose} (i.e. the all-purpose binding is not returned if a
        special purpose binding is requested).

        If one or more collection based bindings are to prims that are not
        Materials, this does not generate an error, but the corresponding
        Material(s) will be invalid (i.e. evaluate to false).

        The python version of this API returns a tuple containing the vector
        of CollectionBinding objects and the corresponding vector of binding
        relationships.

        The returned list of collection-bindings will be in native property
        order of the associated binding relationships. See
        UsdPrim::GetPropertyOrder() , UsdPrim::SetPropertyOrder() . Binding
        relationships that come earlier in the list are considered to be
        stronger than the ones that come later. See rule #6 in
        UsdShadeMaterialBindingAPI_MaterialResolution.
        """
    def GetDirectBinding(self, materialPurpose: str | pxr.Ar.ResolvedPath = ...) -> MaterialBindingAPI.DirectBinding:
        """
        Computes and returns the direct binding for the given material purpose
        on this prim.


        The returned binding always has the specified C{materialPurpose} (i.e.
        the all-purpose binding is not returned if a special purpose binding
        is requested).

        If the direct binding is to a prim that is not a Material, this does
        not generate an error, but the returned Material will be invalid (i.e.
        evaluate to false).
        """
    def GetDirectBindingRel(self, materialPurpose: str | pxr.Ar.ResolvedPath = ...) -> pxr.Usd.Relationship:
        """
        Returns the direct material-binding relationship on this prim for the
        given material purpose.


        The material purpose of the relationship that's returned will match
        the specified C{materialPurpose}.
        """
    def GetMaterialBindSubsets(self) -> list[pxr.UsdGeom.Subset]:
        """
        Returns all the existing GeomSubsets with
        familyName=UsdShadeTokens->materialBind below this prim.
        """
    def GetMaterialBindSubsetsFamilyType(self) -> str:
        '''
        Returns the familyType of the family of"materialBind"GeomSubsets on
        this prim.


        By default, materialBind subsets have familyType="nonOverlapping", but
        they can also be tagged as a"partition", using
        SetMaterialBindFaceSubsetsFamilyType().

        UsdGeomSubset::GetFamilyNameAttr
        '''
    @staticmethod
    def GetMaterialBindingStrength(bindingRel: pxr.Usd.Relationship) -> str:
        """
        Resolves the'bindMaterialAs'token-valued metadata on the given binding
        relationship and returns it.


        If the resolved value is empty, this returns the fallback value
        UsdShadeTokens->weakerThanDescendants.

        UsdShadeMaterialBindingAPI::SetMaterialBindingStrength()
        """
    @staticmethod
    def GetMaterialPurposes() -> list[str]:
        """
        Returns a vector of the possible values for the'material purpose'.
        """
    @staticmethod
    def GetResolvedTargetPathFromBindingRel(bindingRel: pxr.Usd.Relationship) -> pxr.Sdf.Path:
        """
        returns the path of the resolved target identified by C{bindingRel}.
        """
    @staticmethod
    def GetSchemaAttributeNames(includeInherited: bool = ...) -> list[str]:
        """
        Return a vector of names of all pre-declared attributes for this
        schema class and all its ancestor classes.


        Does not include attributes that may be authored by custom/extended
        methods of the schemas involved.
        """
    def RemovePrimFromBindingCollection(self, prim: pxr.Usd.Prim, bindingName: str | pxr.Ar.ResolvedPath, materialPurpose: str | pxr.Ar.ResolvedPath = ...) -> bool:
        """
        Removes the specified C{prim} from the collection targeted by the
        binding relationship corresponding to given C{bindingName} and
        C{materialPurpose}.


        If the collection-binding relationship doesn't exist or if the
        targeted collection does not include the C{prim}, then this does
        nothing and returns true.

        If the targeted collection includes C{prim}, then this modifies the
        collection by removing the prim from it (by invoking
        UsdCollectionAPI::RemovePrim()). This method can be used in
        conjunction with the Unbind*() methods (if desired) to guarantee that
        a prim has no resolved material binding.
        """
    def SetMaterialBindSubsetsFamilyType(self, familyType: str | pxr.Ar.ResolvedPath) -> bool:
        '''
        Author the *familyType* of the"materialBind"family of GeomSubsets on
        this prim.


        The default C{familyType} is *UsdGeomTokens->nonOverlapping *. It can
        be set to *UsdGeomTokens->partition* to indicate that the entire
        imageable prim is included in the union of all
        the"materialBind"subsets. The family type should never be set to
        UsdGeomTokens->unrestricted, since it is invalid for a single piece of
        geometry (in this case, a subset) to be bound to more than one
        material. Hence, a coding error is issued if C{familyType} is
        UsdGeomTokens->unrestricted.**

        **

        UsdGeomSubset::SetFamilyType**
        '''
    @staticmethod
    def SetMaterialBindingStrength(_bindingRel: pxr.Usd.Relationship, /, bindingRel: str | pxr.Ar.ResolvedPath) -> bool:
        """
        Sets the'bindMaterialAs'token-valued metadata on the given binding
        relationship.


        If C{bindingStrength} is *UsdShadeTokens->fallbackStrength*, the value
        UsdShadeTokens->weakerThanDescendants is authored sparsely, i.e. only
        when there is a different existing bindingStrength value. To stamp out
        the bindingStrength value explicitly, clients can pass in
        UsdShadeTokens->weakerThanDescendants or
        UsdShadeTokens->strongerThanDescendants directly. Returns true on
        success, false otherwise.

        UsdShadeMaterialBindingAPI::GetMaterialBindingStrength()
        """
    def UnbindAllBindings(self) -> bool:
        """
        Unbinds all direct and collection-based bindings on this prim.
        """
    def UnbindCollectionBinding(self, bindingName: str | pxr.Ar.ResolvedPath, materialPurpose: str | pxr.Ar.ResolvedPath = ...) -> bool:
        """
        Unbinds the collection-based binding with the given C{bindingName},
        for the given C{materialPurpose} on this prim.


        It accomplishes this by blocking the targets of the associated binding
        relationship in the current edit target.

        If a binding was created without specifying a C{bindingName}, then the
        correct C{bindingName} to use for unbinding is the instance name of
        the targetted collection.

        This does not remove the UsdShadeMaterialBindingAPI schema
        application.
        """
    def UnbindDirectBinding(self, materialPurpose: str | pxr.Ar.ResolvedPath = ...) -> bool:
        """
        Unbinds the direct binding for the given material purpose (
        C{materialPurpose}) on this prim.


        It accomplishes this by blocking the targets of the binding
        relationship in the current edit target.

        This does not remove the UsdShadeMaterialBindingAPI schema
        application.
        """
    @staticmethod
    def _GetStaticTfType() -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...

class NodeDefAPI(pxr.Usd.APISchemaBase):
    '''
    UsdShadeNodeDefAPI is an API schema that provides attributes for a
    prim to select a corresponding Shader Node Definition ("Sdr Node"), as
    well as to look up a runtime entry for that shader node in the form of
    an SdrShaderNode.


    UsdShadeNodeDefAPI is intended to be a pre-applied API schema for any
    prim type that wants to refer to the SdrRegistry for further
    implementation details about the behavior of that prim. The primary
    use in UsdShade itself is as UsdShadeShader, which is a basis for
    material shading networks (UsdShadeMaterial), but this is intended to
    be used in other domains that also use the Sdr node mechanism.

    This schema provides properties that allow a prim to identify an
    external node definition, either by a direct identifier key into the
    SdrRegistry (info:id), an asset to be parsed by a suitable
    NdrParserPlugin (info:sourceAsset), or an inline source code that must
    also be parsed (info:sourceCode); as well as a selector attribute to
    determine which specifier is active (info:implementationSource).

    For any described attribute *Fallback* *Value* or *Allowed* *Values*
    below that are text/tokens, the actual token is published and defined
    in UsdShadeTokens. So to set an attribute to the value"rightHanded",
    use UsdShadeTokens->rightHanded as the value.
    '''
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None:
        """
        Construct a UsdShadeNodeDefAPI on UsdPrim C{prim}.


        Equivalent to UsdShadeNodeDefAPI::Get (prim.GetStage(),
        prim.GetPath()) for a *valid* C{prim}, but will not immediately throw
        an error for an invalid C{prim}
        """
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None:
        """
        Construct a UsdShadeNodeDefAPI on the prim held by C{schemaObj}.


        Should be preferred over UsdShadeNodeDefAPI (schemaObj.GetPrim()), as
        it preserves SchemaBase state.
        """
    @staticmethod
    def Apply(prim: pxr.Usd.Prim) -> NodeDefAPI:
        '''
        Applies this B{single-apply} API schema to the given C{prim}.


        This information is stored by adding"NodeDefAPI"to the token-valued,
        listOp metadata *apiSchemas* on the prim.

        A valid UsdShadeNodeDefAPI object is returned upon success. An invalid
        (or empty) UsdShadeNodeDefAPI object is returned upon failure. See
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
    def CreateIdAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetIdAttr() , and also Create vs Get Property Methods for when to
        use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateImplementationSourceAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetImplementationSourceAttr() , and also Create vs Get Property
        Methods for when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    @staticmethod
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> NodeDefAPI:
        """
        Return a UsdShadeNodeDefAPI holding the prim adhering to this schema
        at C{path} on C{stage}.


        If no prim exists at C{path} on C{stage}, or if the prim at that path
        does not adhere to this schema, return an invalid schema object. This
        is shorthand for the following: ::

          UsdShadeNodeDefAPI(stage->GetPrimAtPath(path));

        """
    def GetIdAttr(self) -> pxr.Usd.Attribute:
        """
        The id is an identifier for the type or purpose of the shader.


        E.g.: Texture or FractalFloat. The use of this id will depend on the
        render context: some will turn it into an actual shader path, some
        will use it to generate shader source code dynamically.

        SetShaderId()

        Declaration

        C{uniform token info:id}

        C++ Type

        TfToken

        Usd Type

        SdfValueTypeNames->Token

        Variability

        SdfVariabilityUniform
        """
    def GetImplementationSource(self) -> str:
        '''
        Reads the value of info:implementationSource attribute and returns a
        token identifying the attribute that must be consulted to identify the
        shader\'s source program.


        This returns
           - B{id}, to indicate that the"info:id"attribute must be consulted.

           - B{sourceAsset} to indicate that the asset-
             valued"info:{sourceType}:sourceAsset"attribute associated with the
             desired B{sourceType} should be consulted to locate the asset with the
             shader\'s source.

           - B{sourceCode} to indicate that the string-
             valued"info:{sourceType}:sourceCode"attribute associated with the
             desired B{sourceType} should be read to get shader\'s source.

        This issues a warning and returns B{id} if the
        *info:implementationSource* attribute has an invalid value.

        *{sourceType}* above is a place holder for a token that identifies the
        type of shader source or its implementation. For example: osl, glslfx,
        riCpp etc. This allows a shader to specify different sourceAsset (or
        sourceCode) values for different sourceTypes. The sourceType tokens
        usually correspond to the sourceType value of the NdrParserPlugin
        that\'s used to parse the shader source (NdrParserPlugin::SourceType).

        When sourceType is empty, the corresponding sourceAsset or sourceCode
        is considered to be"universal"(or fallback), which is represented by
        the empty-valued token UsdShadeTokens->universalSourceType. When the
        sourceAsset (or sourceCode) corresponding to a specific, requested
        sourceType is unavailable, the universal sourceAsset (or sourceCode)
        is returned by GetSourceAsset (and GetSourceCode} API, if present.

        GetShaderId()

        GetSourceAsset()

        GetSourceCode()
        '''
    def GetImplementationSourceAttr(self) -> pxr.Usd.Attribute:
        '''
        Specifies the attribute that should be consulted to get the shader\'s
        implementation or its source code.



           - If set to"id", the"info:id"attribute\'s value is used to determine
             the shader source from the shader registry.

           - If set to"sourceAsset", the resolved value of
             the"info:sourceAsset"attribute corresponding to the desired
             implementation (or source-type) is used to locate the shader source. A
             source asset file may also specify multiple shader definitions, so
             there is an optional attribute"info:sourceAsset:subIdentifier"whose
             value should be used to indicate a particular shader definition from a
             source asset file.

           - If set to"sourceCode", the value of"info:sourceCode"attribute
             corresponding to the desired implementation (or source type) is used
             as the shader source.

        Declaration

        C{uniform token info:implementationSource ="id"}

        C++ Type

        TfToken

        Usd Type

        SdfValueTypeNames->Token

        Variability

        SdfVariabilityUniform

        Allowed Values

        id, sourceAsset, sourceCode
        '''
    @staticmethod
    def GetSchemaAttributeNames(includeInherited: bool = ...) -> list[str]:
        """
        Return a vector of names of all pre-declared attributes for this
        schema class and all its ancestor classes.


        Does not include attributes that may be authored by custom/extended
        methods of the schemas involved.
        """
    def GetShaderId(self) -> str:
        """
        Fetches the shader's ID value from the *info:id* attribute, if the
        shader's *info:implementationSource* is B{id}.


        Returns B{true} if the shader's implementation source is B{id} and the
        value was fetched properly into C{id}. Returns false otherwise.

        GetImplementationSource()
        """
    def GetShaderNodeForSourceType(self, sourceType: str | pxr.Ar.ResolvedPath) -> pxr.Sdr.ShaderNode:
        """
        This method attempts to ensure that there is a ShaderNode in the
        shader registry (i.e.


        SdrRegistry) representing this shader for the given C{sourceType}. It
        may return a null pointer if none could be found or created.
        """
    def GetSourceAsset(self, sourceType: str | pxr.Ar.ResolvedPath = ...) -> pxr.Sdf.AssetPath:
        """
        Fetches the shader's source asset value for the specified
        C{sourceType} value from the B{info: *sourceType*: sourceAsset}
        attribute, if the shader's *info:implementationSource* is
        B{sourceAsset}.


        If the *sourceAsset* attribute corresponding to the requested
        *sourceType* isn't present on the shader, then the *universal*
        *fallback* sourceAsset attribute, i.e. *info:sourceAsset* is
        consulted, if present, to get the source asset path.

        Returns B{true} if the shader's implementation source is
        B{sourceAsset} and the source asset path value was fetched
        successfully into C{sourceAsset}. Returns false otherwise.

        GetImplementationSource()
        """
    def GetSourceAssetSubIdentifier(self, sourceType: str | pxr.Ar.ResolvedPath = ...) -> str:
        """
        Fetches the shader's sub-identifier for the source asset with the
        specified C{sourceType} value from the B{info: *sourceType*:
        sourceAsset:subIdentifier} attribute, if the shader's *info:
        implementationSource* is B{sourceAsset}.


        If the *subIdentifier* attribute corresponding to the requested
        *sourceType* isn't present on the shader, then the *universal*
        *fallback* sub-identifier attribute, i.e. *info:sourceAsset:
        subIdentifier* is consulted, if present, to get the sub-identifier
        name.

        Returns B{true} if the shader's implementation source is
        B{sourceAsset} and the sub-identifier for the given source type was
        fetched successfully into C{subIdentifier}. Returns false otherwise.
        """
    def GetSourceCode(self, sourceType: str | pxr.Ar.ResolvedPath = ...) -> str:
        """
        Fetches the shader's source code for the specified C{sourceType} value
        by reading the B{info: *sourceType*: sourceCode} attribute, if the
        shader's *info:implementationSource* is B{sourceCode}.


        If the *sourceCode* attribute corresponding to the requested
        *sourceType* isn't present on the shader, then the *universal* or
        *fallback* sourceCode attribute (i.e. *info:sourceCode*) is consulted,
        if present, to get the source code.

        Returns B{true} if the shader's implementation source is B{sourceCode}
        and the source code string was fetched successfully into
        C{sourceCode}. Returns false otherwise.

        GetImplementationSource()
        """
    def GetSourceTypes(self) -> list[str]:
        """
        Fetches the source types for the specified C{prim} value by reading
        the B{info: *sourceType* :<implementationSource>} attribute, if the
        shader's *info:implementationSource* is B{sourceCode} or
        B{sourceAsset}.


        If there are no source types listed then this returns an empty list

        GetImplementationSource()
        """
    def SetShaderId(self, _id: str | pxr.Ar.ResolvedPath, /) -> bool:
        """
        Sets the shader's ID value.


        This also sets the *info:implementationSource* attribute on the shader
        to B{UsdShadeTokens->id}, if the existing value is different.
        """
    def SetSourceAsset(self, sourceAsset: pxr.Sdf.AssetPath | str, sourceType: str | pxr.Ar.ResolvedPath = ...) -> bool:
        """
        Sets the shader's source-asset path value to C{sourceAsset} for the
        given source type, C{sourceType}.


        This also sets the *info:implementationSource* attribute on the shader
        to B{UsdShadeTokens->sourceAsset}.
        """
    def SetSourceAssetSubIdentifier(self, subIdentifier: str | pxr.Ar.ResolvedPath, sourceType: str | pxr.Ar.ResolvedPath = ...) -> bool:
        """
        Set a sub-identifier to be used with a source asset of the given
        source type.


        This sets the B{info: *sourceType*: sourceAsset:subIdentifier}.

        This also sets the *info:implementationSource* attribute on the shader
        to B{UsdShadeTokens->sourceAsset}
        """
    def SetSourceCode(self, sourceCode: str | pxr.Ar.ResolvedPath, sourceType: str | pxr.Ar.ResolvedPath = ...) -> bool:
        """
        Sets the shader's source-code value to C{sourceCode} for the given
        source type, C{sourceType}.


        This also sets the *info:implementationSource* attribute on the shader
        to B{UsdShadeTokens->sourceCode}.
        """
    @staticmethod
    def _GetStaticTfType() -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...

class NodeGraph(pxr.Usd.Typed):
    '''
    A node-graph is a container for shading nodes, as well as other node-
    graphs.


    It has a public input interface and provides a list of public outputs.

    B{Node Graph Interfaces}

    One of the most important functions of a node-graph is to host
    the"interface"with which clients of already-built shading networks
    will interact. Please see Interface Inputs for a detailed explanation
    of what the interface provides, and how to construct and use it, to
    effectively share/instance shader networks.

    B{Node Graph Outputs}

    These behave like outputs on a shader and are typically connected to
    an output on a shader inside the node-graph.
    '''
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None:
        """
        Construct a UsdShadeNodeGraph on UsdPrim C{prim}.


        Equivalent to UsdShadeNodeGraph::Get (prim.GetStage(), prim.GetPath())
        for a *valid* C{prim}, but will not immediately throw an error for an
        invalid C{prim}
        """
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None:
        """
        Construct a UsdShadeNodeGraph on the prim held by C{schemaObj}.


        Should be preferred over UsdShadeNodeGraph (schemaObj.GetPrim()), as
        it preserves SchemaBase state.
        """
    @overload
    def __init__(self, connectable: ConnectableAPI) -> None:
        """
        Constructor that takes a ConnectableAPI object.


        Allow implicit (auto) conversion of UsdShadeConnectableAPI to
        UsdShadeNodeGraph, so that a ConnectableAPI can be passed into any
        function that accepts a NodeGraph.

        that the conversion may produce an invalid NodeGraph object, because
        not all UsdShadeConnectableAPI s are UsdShadeNodeGraph s
        """
    def ComputeInterfaceInputConsumersMap(self, computeTransitiveConsumers: bool = ...) -> dict:
        """
        Walks the namespace subtree below the node-graph and computes a map
        containing the list of all inputs on the node-graph and the associated
        vector of consumers of their values.


        The consumers can be inputs on shaders within the node-graph or on
        nested node-graphs).

        If C{computeTransitiveConsumers} is true, then value consumers
        belonging to B{node-graphs} are resolved transitively to compute the
        transitive mapping from inputs on the node-graph to inputs on shaders
        inside the material. Note that inputs on node-graphs that don't have
        value consumers will continue to be included in the result.

        This API is provided for use by DCC's that want to present node-graph
        interface / shader connections in the opposite direction than they are
        encoded in USD.
        """
    def ComputeOutputSource(self, outputName: str | pxr.Ar.ResolvedPath) -> tuple[Shader, str, AttributeType]:
        """
        Deprecated

        in favor of GetValueProducingAttributes on UsdShadeOutput Resolves the
        connection source of the requested output, identified by C{outputName}
        to a shader output.

        C{sourceName} is an output parameter that is set to the name of the
        resolved output, if the node-graph output is connected to a valid
        shader source.

        C{sourceType} is an output parameter that is set to the type of the
        resolved output, if the node-graph output is connected to a valid
        shader source.

        Returns a valid shader object if the specified output exists and is
        connected to one. Return an empty shader object otherwise. The python
        version of this method returns a tuple containing three elements (the
        source shader, sourceName, sourceType).
        """
    def ConnectableAPI(self) -> ConnectableAPI:
        """
        Contructs and returns a UsdShadeConnectableAPI object with this node-
        graph.


        Note that most tasks can be accomplished without explicitly
        constructing a UsdShadeConnectable API, since connection-related API
        such as UsdShadeConnectableAPI::ConnectToSource() are static methods,
        and UsdShadeNodeGraph will auto-convert to a UsdShadeConnectableAPI
        when passed to functions that want to act generically on a connectable
        UsdShadeConnectableAPI object.
        """
    def CreateInput(self, name: str | pxr.Ar.ResolvedPath, type: pxr.Sdf.ValueTypeName) -> Input:
        '''
        Create an Input which can either have a value or can be connected.


        The attribute representing the input is created in
        the"inputs:"namespace.
        '''
    def CreateOutput(self, name: str | pxr.Ar.ResolvedPath, typeName: pxr.Sdf.ValueTypeName) -> Output:
        '''
        Create an output which can either have a value or can be connected.


        The attribute representing the output is created in
        the"outputs:"namespace.
        '''
    @staticmethod
    def Define(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> NodeGraph:
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
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> NodeGraph:
        """
        Return a UsdShadeNodeGraph holding the prim adhering to this schema at
        C{path} on C{stage}.


        If no prim exists at C{path} on C{stage}, or if the prim at that path
        does not adhere to this schema, return an invalid schema object. This
        is shorthand for the following: ::

          UsdShadeNodeGraph(stage->GetPrimAtPath(path));

        """
    def GetInput(self, name: str | pxr.Ar.ResolvedPath) -> Input:
        """
        Return the requested input if it exists.
        """
    def GetInputs(self, onlyAuthored: bool = ...) -> list[Input]:
        '''
        Returns all inputs present on the node-graph.


        These are represented by attributes in the"inputs:"namespace. If
        C{onlyAuthored} is true (the default), then only return authored
        attributes; otherwise, this also returns un-authored builtins.
        '''
    def GetInterfaceInputs(self) -> list[Input]:
        '''
        Returns all the"Interface Inputs"of the node-graph.


        This is the same as GetInputs() , but is provided as a convenience, to
        allow clients to distinguish between inputs on shaders vs. interface-
        inputs on node-graphs.
        '''
    def GetOutput(self, name: str | pxr.Ar.ResolvedPath) -> Output:
        """
        Return the requested output if it exists.
        """
    def GetOutputs(self, onlyAuthored: bool = ...) -> list[Output]:
        '''
        Outputs are represented by attributes in the"outputs:"namespace.


        If C{onlyAuthored} is true (the default), then only return authored
        attributes; otherwise, this also returns un-authored builtins.
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

class Output(Boost.Python.instance):
    """
    This class encapsulates a shader or node-graph output, which is a
    connectable attribute representing a typed, externally computed value.
    """
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self, attr: pxr.Usd.Attribute | pxr.UsdGeom.ConstraintTarget | pxr.UsdGeom.Primvar | pxr.UsdGeom.XformOp | Input | Output) -> None:
        """
        Speculative constructor that will produce a valid UsdShadeOutput when
        C{attr} already represents a shade Output, and produces an *invalid*
        UsdShadeOutput otherwise (i.e.


        the explicit bool conversion operator will return false).
        """
    @overload
    def __init__(self) -> None:
        """
        Default constructor returns an invalid Output.


        Exists for container classes
        """
    def CanConnect(self, source: pxr.Usd.Attribute | pxr.UsdGeom.ConstraintTarget | pxr.UsdGeom.Primvar | pxr.UsdGeom.XformOp | Input | Output) -> bool:
        """
        Determines whether this Output can be connected to the given source
        attribute, which can be an input or an output.


        An output is considered to be connectable only if it belongs to a
        node-graph. Shader outputs are not connectable.

        UsdShadeConnectableAPI::CanConnect
        """
    def ClearSdrMetadata(self) -> None:
        '''
        Clears any"sdrMetadata"value authored on the Output in the current
        EditTarget.
        '''
    def ClearSdrMetadataByKey(self, key: str | pxr.Ar.ResolvedPath) -> None:
        '''
        Clears the entry corresponding to the given C{key} in
        the"sdrMetadata"dictionary authored in the current EditTarget.
        '''
    def ClearSource(self) -> bool:
        """
        Deprecated
        """
    def ClearSources(self) -> bool:
        """
        Clears sources for this Output in the current UsdEditTarget.


        Most of the time, what you probably want is DisconnectSource() rather
        than this function.

        UsdShadeConnectableAPI::ClearSources
        """
    @overload
    def ConnectToSource(self, source: ConnectionSourceInfo, mod: ConnectionModification = ...) -> bool:
        """
        Authors a connection for this Output.


        C{source} is a struct that describes the upstream source attribute
        with all the information necessary to make a connection. See the
        documentation for UsdShadeConnectionSourceInfo. C{mod} describes the
        operation that should be applied to the list of connections. By
        default the new connection will replace any existing connections, but
        it can add to the list of connections to represent multiple input
        connections.

        C{true} if a connection was created successfully. C{false} if
        C{shadingAttr} or C{source} is invalid.

        This method does not verify the connectability of the shading
        attribute to the source. Clients must invoke CanConnect() themselves
        to ensure compatibility.

        The source shading attribute is created if it doesn't exist already.

        UsdShadeConnectableAPI::ConnectToSource
        """
    @overload
    def ConnectToSource(self, source: ConnectableAPI, sourceName: str | pxr.Ar.ResolvedPath, sourceType: AttributeType = ..., typeName: pxr.Sdf.ValueTypeName = ...) -> bool:
        """
        Deprecated

        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        """
    @overload
    def ConnectToSource(self, sourcePath: pxr.Sdf.Path | str) -> bool:
        """
        Authors a connection for this Output to the source at the given path.



        UsdShadeConnectableAPI::ConnectToSource
        """
    @overload
    def ConnectToSource(self, sourceInput: Input) -> bool:
        """
        Connects this Output to the given input, C{sourceInput}.



        UsdShadeConnectableAPI::ConnectToSource
        """
    @overload
    def ConnectToSource(self, sourceOutput: Output) -> bool:
        """
        Connects this Output to the given output, C{sourceOutput}.



        UsdShadeConnectableAPI::ConnectToSource
        """
    def DisconnectSource(self, sourceAttr: pxr.Usd.Attribute | pxr.UsdGeom.ConstraintTarget | pxr.UsdGeom.Primvar | pxr.UsdGeom.XformOp | Input | Output = ...) -> bool:
        """
        Disconnect source for this Output.


        If C{sourceAttr} is valid, only a connection to the specified
        attribute is disconnected, otherwise all connections are removed.

        UsdShadeConnectableAPI::DisconnectSource
        """
    def GetAttr(self) -> pxr.Usd.Attribute:
        """
        Explicit UsdAttribute extractor.
        """
    def GetBaseName(self) -> str:
        '''
        Returns the name of the output.


        We call this the base name since it strips off the"outputs:"namespace
        prefix from the attribute name, and returns it.
        '''
    def GetConnectedSource(self) -> tuple[ConnectableAPI, str, AttributeType]:
        """
        Deprecated

        Please use GetConnectedSources instead
        """
    def GetConnectedSources(self) -> tuple[list[ConnectionSourceInfo], list[pxr.Sdf.Path]]:
        """
        Finds the valid sources of connections for the Output.


        C{invalidSourcePaths} is an optional output parameter to collect the
        invalid source paths that have not been reported in the returned
        vector.

        Returns a vector of C{UsdShadeConnectionSourceInfo} structs with
        information about each upsteam attribute. If the vector is empty,
        there have been no valid connections.

        A valid connection requires the existence of the source attribute and
        also requires that the source prim is UsdShadeConnectableAPI
        compatible.

        The python wrapping returns a tuple with the valid connections first,
        followed by the invalid source paths.

        UsdShadeConnectableAPI::GetConnectedSources
        """
    def GetFullName(self) -> str:
        """
        Get the name of the attribute associated with the output.
        """
    def GetPrim(self) -> pxr.Usd.Prim:
        """
        Get the prim that the output belongs to.
        """
    def GetRawConnectedSourcePaths(self) -> list[pxr.Sdf.Path]:
        '''
        Deprecated

        Returns the"raw"(authored) connected source paths for this Output.

        UsdShadeConnectableAPI::GetRawConnectedSourcePaths
        '''
    def GetRenderType(self) -> str:
        """
        Return this output's specialized renderType, or an empty token if none
        was authored.



        SetRenderType()
        """
    def GetSdrMetadata(self) -> dict[str, str]:
        '''
        Returns this Output\'s composed"sdrMetadata"dictionary as a
        NdrTokenMap.
        '''
    def GetSdrMetadataByKey(self, key: str | pxr.Ar.ResolvedPath) -> str:
        """
        Returns the value corresponding to C{key} in the composed
        B{sdrMetadata} dictionary.
        """
    def GetTypeName(self) -> pxr.Sdf.ValueTypeName:
        '''
        Get the"scene description"value type name of the attribute associated
        with the output.
        '''
    def GetValueProducingAttributes(self, shaderOutputsOnly: bool = ...) -> list[Attribute]:
        """
        Find what is connected to this Output recursively.



        UsdShadeUtils::GetValueProducingAttributes
        """
    def HasConnectedSource(self) -> bool:
        """
        Returns true if and only if this Output is currently connected to a
        valid (defined) source.



        UsdShadeConnectableAPI::HasConnectedSource
        """
    def HasRenderType(self) -> bool:
        """
        Return true if a renderType has been specified for this output.



        SetRenderType()
        """
    def HasSdrMetadata(self) -> bool:
        '''
        Returns true if the Output has a non-empty
        composed"sdrMetadata"dictionary value.
        '''
    def HasSdrMetadataByKey(self, key: str | pxr.Ar.ResolvedPath) -> bool:
        '''
        Returns true if there is a value corresponding to the given C{key} in
        the composed"sdrMetadata"dictionary.
        '''
    @staticmethod
    def IsOutput(_attr: pxr.Usd.Attribute | pxr.UsdGeom.ConstraintTarget | pxr.UsdGeom.Primvar | pxr.UsdGeom.XformOp | Input | Output, /) -> bool:
        """
        Test whether a given UsdAttribute represents a valid Output, which
        implies that creating a UsdShadeOutput from the attribute will
        succeed.


        Success implies that C{attr.IsDefined()} is true.
        """
    def IsSourceConnectionFromBaseMaterial(self) -> bool:
        """
        Returns true if the connection to this Output's source, as returned by
        GetConnectedSource() , is authored across a specializes arc, which is
        used to denote a base material.



        UsdShadeConnectableAPI::IsSourceConnectionFromBaseMaterial
        """
    def Set(self, value: Any, time: pxr.Usd.TimeCode | float | pxr.Sdf.TimeCode = ...) -> bool:
        """
        Set a value for the output.


        It's unusual to be setting a value on an output since it represents an
        externally computed value. The Set API is provided here just for the
        sake of completeness and uniformity with other property schema.
        """
    def SetConnectedSources(self, _sourceInfos: typing.Iterable[ConnectionSourceInfo], /) -> bool:
        """
        Connects this Output to the given sources, C{sourceInfos}.



        UsdShadeConnectableAPI::SetConnectedSources
        """
    def SetRenderType(self, renderType: str | pxr.Ar.ResolvedPath) -> bool:
        '''
        Specify an alternative, renderer-specific type to use when
        emitting/translating this output, rather than translating based on its
        GetTypeName()


        For example, we set the renderType to"struct"for outputs that are of
        renderman custom struct types.

        true on success
        '''
    def SetSdrMetadata(self, sdrMetadata: dict[str | pxr.Ar.ResolvedPath, str | pxr.Ar.ResolvedPath]) -> None:
        """
        Authors the given C{sdrMetadata} value on this Output at the current
        EditTarget.
        """
    def SetSdrMetadataByKey(self, key: str | pxr.Ar.ResolvedPath, value: str | pxr.Ar.ResolvedPath) -> None:
        '''
        Sets the value corresponding to C{key} to the given string C{value},
        in the Output\'s"sdrMetadata"dictionary at the current EditTarget.
        '''
    def __bool__(self) -> bool:
        """
        Return true if this Output is valid for querying and authoring values
        and metadata, which is identically equivalent to IsDefined() .
        """
    def __eq__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...

class Shader(pxr.Usd.Typed):
    '''
    Base class for all USD shaders.


    Shaders are the building blocks of shading networks. While
    UsdShadeShader objects are not target specific, each renderer or
    application target may derive its own renderer-specific shader object
    types from this base, if needed.

    Objects of this class generally represent a single shading object,
    whether it exists in the target renderer or not. For example, a
    texture, a fractal, or a mix node.

    The UsdShadeNodeDefAPI provides attributes to uniquely identify the
    type of this node. The id resolution into a renderable shader target
    type of this node. The id resolution into a renderable shader target
    is deferred to the consuming application.

    The purpose of representing them in Usd is two-fold:
       - To represent, via"connections"the topology of the shading network
         that must be reconstructed in the renderer. Facilities for authoring
         and manipulating connections are encapsulated in the API schema
         UsdShadeConnectableAPI.

       - To present a (partial or full) interface of typed input
         parameters whose values can be set and overridden in Usd, to be
         provided later at render-time as parameter values to the actual render
         shader objects. Shader input parameters are encapsulated in the
         property schema UsdShadeInput.

    '''
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, connectable: ConnectableAPI) -> None:
        """
        Constructor that takes a ConnectableAPI object.


        Allow implicit (auto) conversion of UsdShadeConnectableAPI to
        UsdShadeShader, so that a ConnectableAPI can be passed into any
        function that accepts a Shader.

        that the conversion may produce an invalid Shader object, because not
        all UsdShadeConnectableAPI s are Shaders
        """
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None:
        """
        Construct a UsdShadeShader on UsdPrim C{prim}.


        Equivalent to UsdShadeShader::Get (prim.GetStage(), prim.GetPath())
        for a *valid* C{prim}, but will not immediately throw an error for an
        invalid C{prim}
        """
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None:
        """
        Construct a UsdShadeShader on the prim held by C{schemaObj}.


        Should be preferred over UsdShadeShader (schemaObj.GetPrim()), as it
        preserves SchemaBase state.
        """
    def ClearSdrMetadata(self) -> None:
        '''
        Clears any"sdrMetadata"value authored on the shader in the current
        EditTarget.
        '''
    def ClearSdrMetadataByKey(self, key: str | pxr.Ar.ResolvedPath) -> None:
        '''
        Clears the entry corresponding to the given C{key} in
        the"sdrMetadata"dictionary authored in the current EditTarget.
        '''
    def ConnectableAPI(self) -> ConnectableAPI:
        """
        Contructs and returns a UsdShadeConnectableAPI object with this
        shader.


        Note that most tasks can be accomplished without explicitly
        constructing a UsdShadeConnectable API, since connection-related API
        such as UsdShadeConnectableAPI::ConnectToSource() are static methods,
        and UsdShadeShader will auto-convert to a UsdShadeConnectableAPI when
        passed to functions that want to act generically on a connectable
        UsdShadeConnectableAPI object.
        """
    def CreateIdAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        Forwards to UsdShadeNodeDefAPI(prim).
        """
    def CreateImplementationSourceAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        Forwards to UsdShadeNodeDefAPI(prim).
        """
    def CreateInput(self, name: str | pxr.Ar.ResolvedPath, type: pxr.Sdf.ValueTypeName) -> Input:
        '''
        Create an input which can either have a value or can be connected.


        The attribute representing the input is created in
        the"inputs:"namespace. Inputs on both shaders and node-graphs are
        connectable.
        '''
    def CreateOutput(self, name: str | pxr.Ar.ResolvedPath, type: pxr.Sdf.ValueTypeName) -> Output:
        '''
        Create an output which can either have a value or can be connected.


        The attribute representing the output is created in
        the"outputs:"namespace. Outputs on a shader cannot be connected, as
        their value is assumed to be computed externally.
        '''
    @staticmethod
    def Define(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> Shader:
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
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> Shader:
        """
        Return a UsdShadeShader holding the prim adhering to this schema at
        C{path} on C{stage}.


        If no prim exists at C{path} on C{stage}, or if the prim at that path
        does not adhere to this schema, return an invalid schema object. This
        is shorthand for the following: ::

          UsdShadeShader(stage->GetPrimAtPath(path));

        """
    def GetIdAttr(self) -> pxr.Usd.Attribute:
        """
        Forwards to UsdShadeNodeDefAPI(prim).
        """
    def GetImplementationSource(self) -> str:
        """
        Forwards to UsdShadeNodeDefAPI(prim).
        """
    def GetImplementationSourceAttr(self) -> pxr.Usd.Attribute:
        """
        Forwards to UsdShadeNodeDefAPI(prim).
        """
    def GetInput(self, name: str | pxr.Ar.ResolvedPath) -> Input:
        """
        Return the requested input if it exists.
        """
    def GetInputs(self, onlyAuthored: bool = ...) -> list[Input]:
        '''
        Inputs are represented by attributes in the"inputs:"namespace.


        If C{onlyAuthored} is true (the default), then only return authored
        attributes; otherwise, this also returns un-authored builtins.
        '''
    def GetOutput(self, name: str | pxr.Ar.ResolvedPath) -> Output:
        """
        Return the requested output if it exists.
        """
    def GetOutputs(self, onlyAuthored: bool = ...) -> list[Output]:
        '''
        Outputs are represented by attributes in the"outputs:"namespace.


        If C{onlyAuthored} is true (the default), then only return authored
        attributes; otherwise, this also returns un-authored builtins.
        '''
    @staticmethod
    def GetSchemaAttributeNames(includeInherited: bool = ...) -> list[str]:
        """
        Return a vector of names of all pre-declared attributes for this
        schema class and all its ancestor classes.


        Does not include attributes that may be authored by custom/extended
        methods of the schemas involved.
        """
    def GetSdrMetadata(self) -> dict[str, str]:
        '''
        Returns this shader\'s composed"sdrMetadata"dictionary as a
        NdrTokenMap.
        '''
    def GetSdrMetadataByKey(self, key: str | pxr.Ar.ResolvedPath) -> str:
        """
        Returns the value corresponding to C{key} in the composed
        B{sdrMetadata} dictionary.
        """
    def GetShaderId(self) -> str:
        """
        Forwards to UsdShadeNodeDefAPI(prim).
        """
    def GetShaderNodeForSourceType(self, sourceType: str | pxr.Ar.ResolvedPath) -> pxr.Sdr.ShaderNode:
        """
        Forwards to UsdShadeNodeDefAPI(prim).
        """
    def GetSourceAsset(self, sourceType: str | pxr.Ar.ResolvedPath = ...) -> pxr.Sdf.AssetPath:
        """
        Forwards to UsdShadeNodeDefAPI(prim).
        """
    def GetSourceAssetSubIdentifier(self, sourceType: str | pxr.Ar.ResolvedPath = ...) -> str:
        """
        Forwards to UsdShadeNodeDefAPI(prim).
        """
    def GetSourceCode(self, sourceType: str | pxr.Ar.ResolvedPath = ...) -> str:
        """
        Forwards to UsdShadeNodeDefAPI(prim).
        """
    def GetSourceTypes(self) -> list[str]:
        """
        Forwards to UsdShadeNodeDefAPI(prim).
        """
    def HasSdrMetadata(self) -> bool:
        '''
        Returns true if the shader has a non-empty
        composed"sdrMetadata"dictionary value.
        '''
    def HasSdrMetadataByKey(self, key: str | pxr.Ar.ResolvedPath) -> bool:
        '''
        Returns true if there is a value corresponding to the given C{key} in
        the composed"sdrMetadata"dictionary.
        '''
    def SetSdrMetadata(self, sdrMetadata: dict[str | pxr.Ar.ResolvedPath, str | pxr.Ar.ResolvedPath]) -> None:
        """
        Authors the given C{sdrMetadata} on this shader at the current
        EditTarget.
        """
    def SetSdrMetadataByKey(self, key: str | pxr.Ar.ResolvedPath, value: str | pxr.Ar.ResolvedPath) -> None:
        '''
        Sets the value corresponding to C{key} to the given string C{value},
        in the shader\'s"sdrMetadata"dictionary at the current EditTarget.
        '''
    def SetShaderId(self, _id: str | pxr.Ar.ResolvedPath, /) -> bool:
        """
        Forwards to UsdShadeNodeDefAPI(prim).
        """
    def SetSourceAsset(self, sourceAsset: pxr.Sdf.AssetPath | str, sourceType: str | pxr.Ar.ResolvedPath = ...) -> bool:
        """
        Forwards to UsdShadeNodeDefAPI(prim).
        """
    def SetSourceAssetSubIdentifier(self, subIdentifier: str | pxr.Ar.ResolvedPath, sourceType: str | pxr.Ar.ResolvedPath = ...) -> bool:
        """
        Forwards to UsdShadeNodeDefAPI(prim).
        """
    def SetSourceCode(self, sourceCode: str | pxr.Ar.ResolvedPath, sourceType: str | pxr.Ar.ResolvedPath = ...) -> bool:
        """
        Forwards to UsdShadeNodeDefAPI(prim).
        """
    @staticmethod
    def _GetStaticTfType() -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...

class ShaderDefParserPlugin(Boost.Python.instance):
    """
    Parses shader definitions represented using USD scene description
    using the schemas provided by UsdShade.
    """
    __instance_size__: ClassVar[int] = ...
    def __init__(self) -> None: ...
    def GetDiscoveryTypes(self) -> list[str]:
        '''
        Returns the types of nodes that this plugin can parse.


        "Type"here is the discovery type (in the case of files, this will
        probably be the file extension, but in other systems will be data that
        can be determined during discovery). This type should only be used to
        match up a C{NdrNodeDiscoveryResult} to its parser plugin; this value
        is not exposed in the node\'s API.
        '''
    def GetSourceType(self) -> str:
        '''
        Returns the source type that this parser operates on.


        A source type is the most general type for a node. The parser plugin
        is responsible for parsing all discovery results that have the types
        declared under C{GetDiscoveryTypes()} , and those types are
        collectively identified as one"source type".
        '''
    def Parse(self, _discoveryResult: pxr.Ndr.NodeDiscoveryResult, /) -> pxr.Sdr.ShaderNode:
        """
        Takes the specified C{NdrNodeDiscoveryResult} instance, which was a
        result of the discovery process, and generates a new C{NdrNode}.


        The node's name, source type, and family must match.
        """

class ShaderDefUtils(Boost.Python.instance):
    """
    This class contains a set of utility functions used for populating the
    shader registry with shaders definitions specified using UsdShade
    schemas.
    """
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def GetNodeDiscoveryResults(shaderDef: Shader, sourceUri: str | pxr.Ar.ResolvedPath) -> list:
        """
        Returns the list of NdrNodeDiscoveryResult objects that must be added
        to the shader registry for the given shader C{shaderDef}, assuming it
        is found in a shader definition file found by an Ndr discovery plugin.


        To enable the shaderDef parser to find and parse this shader,
        C{sourceUri} should have the resolved path to the usd file containing
        this shader prim.
        """
    @staticmethod
    def GetPrimvarNamesMetadataString(metadata: dict[str | pxr.Ar.ResolvedPath, str | pxr.Ar.ResolvedPath], shaderDef: ConnectableAPI) -> str:
        """
        Collects all the names of valid primvar inputs of the given
        C{metadata} and the given C{shaderDef} and returns the string used to
        represent them in SdrShaderNode metadata.
        """
    @staticmethod
    def GetShaderProperties(shaderDef: ConnectableAPI) -> list[[pxr.Ndr.Property]]:
        """
        Gets all input and output properties of the given C{shaderDef} and
        translates them into NdrProperties that can be used as the properties
        for an SdrShaderNode.
        """

class Tokens(Boost.Python.instance):
    ConnectableAPI: ClassVar[str] = ...  # read-only
    CoordSysAPI: ClassVar[str] = ...  # read-only
    Material: ClassVar[str] = ...  # read-only
    MaterialBindingAPI: ClassVar[str] = ...  # read-only
    NodeDefAPI: ClassVar[str] = ...  # read-only
    NodeGraph: ClassVar[str] = ...  # read-only
    Shader: ClassVar[str] = ...  # read-only
    allPurpose: ClassVar[str] = ...  # read-only
    bindMaterialAs: ClassVar[str] = ...  # read-only
    coordSys: ClassVar[str] = ...  # read-only
    coordSys_MultipleApplyTemplate_Binding: ClassVar[str] = ...  # read-only
    displacement: ClassVar[str] = ...  # read-only
    fallbackStrength: ClassVar[str] = ...  # read-only
    full: ClassVar[str] = ...  # read-only
    id: ClassVar[str] = ...  # read-only
    infoId: ClassVar[str] = ...  # read-only
    infoImplementationSource: ClassVar[str] = ...  # read-only
    inputs: ClassVar[str] = ...  # read-only
    interfaceOnly: ClassVar[str] = ...  # read-only
    materialBind: ClassVar[str] = ...  # read-only
    materialBinding: ClassVar[str] = ...  # read-only
    materialBindingCollection: ClassVar[str] = ...  # read-only
    materialVariant: ClassVar[str] = ...  # read-only
    outputs: ClassVar[str] = ...  # read-only
    outputsDisplacement: ClassVar[str] = ...  # read-only
    outputsSurface: ClassVar[str] = ...  # read-only
    outputsVolume: ClassVar[str] = ...  # read-only
    preview: ClassVar[str] = ...  # read-only
    sdrMetadata: ClassVar[str] = ...  # read-only
    sourceAsset: ClassVar[str] = ...  # read-only
    sourceCode: ClassVar[str] = ...  # read-only
    strongerThanDescendants: ClassVar[str] = ...  # read-only
    subIdentifier: ClassVar[str] = ...  # read-only
    surface: ClassVar[str] = ...  # read-only
    universalRenderContext: ClassVar[str] = ...  # read-only
    universalSourceType: ClassVar[str] = ...  # read-only
    volume: ClassVar[str] = ...  # read-only
    weakerThanDescendants: ClassVar[str] = ...  # read-only
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """

class UdimUtils(Boost.Python.instance):
    """
    This class contains a set of utility functions used for working with
    Udim texture paths.
    """
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def IsUdimIdentifier(identifier: str | pxr.Ar.ResolvedPath) -> bool:
        '''
        Checks if C{identifier} contains a UDIM token.


        Currently only"<UDIM>"is supported, but other patterns such
        as"_MAPID_"may be supported in the future.
        '''
    @staticmethod
    def ReplaceUdimPattern(identifierWithPattern: str | pxr.Ar.ResolvedPath, replacement: str | pxr.Ar.ResolvedPath) -> str:
        """
        Replaces the UDIM pattern contained in C{identifierWithPattern} with
        C{replacement}.
        """
    @staticmethod
    def ResolveUdimPath(udimPath: str | pxr.Ar.ResolvedPath, layer: pxr.Sdf.Layer) -> str:
        '''
        Resolves a C{udimPath} containing a UDIM token.


        The path is first anchored with the passed C{layer} if needed, then
        the function attempts to resolve any possible UDIM tiles. If any
        exist, the resolved path is returned with"<UDIM>"substituted back in.
        If no resolves succeed or C{udimPath} does not contain a UDIM token,
        an empty string is returned.
        '''
    @staticmethod
    def ResolveUdimTilePaths(udimPath: str | pxr.Ar.ResolvedPath, layer: pxr.Sdf.Layer) -> list[tuple[str, str]]:
        """
        Attempts to resolve all paths which match a path containing a UDIM
        pattern.


        The path is first anchored with the passed C{layer} if needed, then
        the function attempts to resolve all possible UDIM numbers in the
        path.
        """

class Utils(Boost.Python.instance):
    """
    This class contains a set of utility functions used when authoring and
    querying shading networks.
    """
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def GetBaseNameAndType(_fullName: str | pxr.Ar.ResolvedPath, /) -> tuple[str, AttributeType]:
        """
        Given the full name of a shading attribute, returns it's base name and
        shading attribute type.
        """
    @staticmethod
    def GetConnectedSourcePath(connectionSourceInfo: ConnectionSourceInfo) -> pxr.Sdf.Path:
        """
        For a valid UsdShadeConnectionSourceInfo, return the complete path to
        the source property; otherwise the empty path.
        """
    @staticmethod
    def GetFullName(_baseName: str | pxr.Ar.ResolvedPath, _type: AttributeType, /) -> str:
        """
        Returns the full shading attribute name given the basename and the
        shading attribute type.


        C{baseName} is the name of the input or output on the shading node.
        C{type} is the UsdShadeAttributeType of the shading attribute.
        """
    @staticmethod
    def GetPrefixForAttributeType(_sourceType: AttributeType, /) -> str:
        """
        Returns the namespace prefix of the USD attribute associated with the
        given shading attribute type.
        """
    @staticmethod
    def GetType(_fullName: str | pxr.Ar.ResolvedPath, /) -> AttributeType:
        """
        Given the full name of a shading attribute, returns its shading
        attribute type.
        """
    @overload
    @staticmethod
    def GetValueProducingAttributes(input: Input, shaderOutputsOnly: bool = ...) -> list[Attribute]:
        """
        Find what is connected to an Input or Output recursively.


        GetValueProducingAttributes implements the UsdShade connectivity rules
        described in Connection Resolution Utilities.

        When tracing connections within networks that contain containers like
        UsdShadeNodeGraph nodes, the actual output(s) or value(s) at the end
        of an input or output might be multiple connections removed. The
        methods below resolves this across multiple physical connections.

        An UsdShadeInput is getting its value from one of these sources:
           - If the input is not connected the UsdAttribute for this input is
             returned, but only if it has an authored value. The input attribute
             itself carries the value for this input.

           - If the input is connected we follow the connection(s) until we
             reach a valid output of a UsdShadeShader node or if we reach a valid
             UsdShadeInput attribute of a UsdShadeNodeGraph or UsdShadeMaterial
             that has an authored value.

        An UsdShadeOutput on a container can get its value from the same type
        of sources as a UsdShadeInput on either a UsdShadeShader or
        UsdShadeNodeGraph. Outputs on non-containers (UsdShadeShaders) cannot
        be connected.

        This function returns a vector of UsdAttributes. The vector is empty
        if no valid attribute was found. The type of each attribute can be
        determined with the C{UsdShadeUtils::GetType} function.

        If C{shaderOutputsOnly} is true, it will only report attributes that
        are outputs of non-containers (UsdShadeShaders). This is a bit faster
        and what is need when determining the connections for Material
        terminals.

        This will return the last attribute along the connection chain that
        has an authored value, which might not be the last attribute in the
        chain itself.

        When the network contains multi-connections, this function can return
        multiple attributes for a single input or output. The list of
        attributes is build by a depth-first search, following the underlying
        connection paths in order. The list can contain both UsdShadeOutput
        and UsdShadeInput attributes. It is up to the caller to decide how to
        process such a mixture.
        """
    @overload
    @staticmethod
    def GetValueProducingAttributes(output: Output, shaderOutputsOnly: bool = ...) -> list[Attribute]:
        """
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
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
