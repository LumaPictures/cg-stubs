# mypy: disable-error-code="misc, override, no-redef"

import Boost.Python
import pxr.Ar
import pxr.Sdf
import pxr.Tf
import types
import typing
from _typeshed import Incomplete
from typing import Any, Callable, ClassVar, overload

ArcTypeInherit: ArcType
ArcTypePayload: ArcType
ArcTypeReference: ArcType
ArcTypeRelocate: ArcType
ArcTypeRoot: ArcType
ArcTypeSpecialize: ArcType
ArcTypeVariant: ArcType
DependencyTypeAncestral: DependencyType
DependencyTypeAnyIncludingVirtual: DependencyType
DependencyTypeAnyNonVirtual: DependencyType
DependencyTypeDirect: DependencyType
DependencyTypeNonVirtual: DependencyType
DependencyTypeNone: DependencyType
DependencyTypePartlyDirect: DependencyType
DependencyTypePurelyDirect: DependencyType
DependencyTypeRoot: DependencyType
DependencyTypeVirtual: DependencyType
ErrorType_ArcCapacityExceeded: ErrorType
ErrorType_ArcCycle: ErrorType
ErrorType_ArcNamespaceDepthCapacityExceeded: ErrorType
ErrorType_ArcPermissionDenied: ErrorType
ErrorType_InconsistentAttributeType: ErrorType
ErrorType_InconsistentAttributeVariability: ErrorType
ErrorType_InconsistentPropertyType: ErrorType
ErrorType_IndexCapacityExceeded: ErrorType
ErrorType_InternalAssetPath: ErrorType
ErrorType_InvalidAssetPath: ErrorType
ErrorType_InvalidAuthoredRelocation: ErrorType
ErrorType_InvalidConflictingRelocation: ErrorType
ErrorType_InvalidExternalTargetPath: ErrorType
ErrorType_InvalidInstanceTargetPath: ErrorType
ErrorType_InvalidPrimPath: ErrorType
ErrorType_InvalidReferenceOffset: ErrorType
ErrorType_InvalidSameTargetRelocations: ErrorType
ErrorType_InvalidSublayerOffset: ErrorType
ErrorType_InvalidSublayerOwnership: ErrorType
ErrorType_InvalidSublayerPath: ErrorType
ErrorType_InvalidTargetPath: ErrorType
ErrorType_InvalidVariantSelection: ErrorType
ErrorType_MutedAssetPath: ErrorType
ErrorType_OpinionAtRelocationSource: ErrorType
ErrorType_PrimPermissionDenied: ErrorType
ErrorType_PropertyPermissionDenied: ErrorType
ErrorType_SublayerCycle: ErrorType
ErrorType_TargetPermissionDenied: ErrorType
ErrorType_UnresolvedPrimPath: ErrorType
ErrorType_VariableExpressionError: ErrorType
_TestPrimIndex: Callable
__MFB_FULL_PACKAGE_NAME: str

class ArcType(pxr.Tf.Tf_PyEnumWrapper):
    _baseName: ClassVar[str] = ...
    allValues: ClassVar[tuple] = ...
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def GetValueFromName(name: object) -> Any: ...

class Cache(Boost.Python.instance):
    '''
    PcpCache is the context required to make requests of the Pcp
    composition algorithm and cache the results.


    Because the algorithms are recursive  making a request typically makes
    other internal requests to solve subproblems  caching subproblem
    results is required for reasonable performance, and so this cache is
    the only entrypoint to the algorithms.

    There is a set of parameters that affect the composition results:

       - variant fallbacks: per named variant set, an ordered list of
         fallback values to use when composing a prim that defines a variant
         set but does not specify a selection

       - payload inclusion set: an SdfPath set used to identify which
         prims should have their payloads included during composition; this is
         the basis for explicit control over the"working set"of composition

       - file format target: the file format target that Pcp will request
         when opening scene description layers

       - "USD mode"configures the Pcp composition algorithm to provide
         only a custom, lighter subset of the full feature set, as needed by
         the Universal Scene Description system
         There are a number of different computations that can be requested.
         These include computing a layer stack from a PcpLayerStackIdentifier,
         computing a prim index or prim stack, and computing a property index.
    '''
    __instance_size__: ClassVar[int] = ...
    def __init__(self, layerStackIdentifier: LayerStackIdentifier, fileFormatTarget: str | pxr.Ar.ResolvedPath = ..., usd: bool = ...) -> None:
        """
        Construct a PcpCache to compose results for the layer stack identified
        by *layerStackIdentifier*.


        If C{fileFormatTarget} is given, Pcp will specify C{fileFormatTarget}
        as the file format target when searching for or opening a layer.

        If C{usd} is true, computation of prim indices and composition of prim
        child names are performed without relocates, inherits, permissions,
        symmetry, or payloads, and without populating the prim stack and
        gathering its dependencies.
        """
    def ComputeAttributeConnectionPaths(self, relPath: pxr.Sdf.Path | str, localOnly: bool = ..., stopProperty: pxr.Sdf.Spec = ..., includeStopProperty: bool = ...) -> tuple:
        """
        Compute the attribute connection paths for the attribute at
        C{attributePath} into C{paths}.


        If C{localOnly} is C{true} then this will compose attribute
        connections from local nodes only. If C{stopProperty} is not C{None}
        then this will stop composing attribute connections at
        C{stopProperty}, including C{stopProperty} iff C{includeStopProperty}
        is C{true}. If not C{None}, C{deletedPaths} will be populated with
        connection paths whose deletion contributed to the computed result.
        C{allErrors} will contain any errors encountered while performing this
        operation.
        """
    def ComputeLayerStack(self, _identifier: LayerStackIdentifier, /) -> tuple:
        """
        Returns the layer stack for C{identifier} if it exists, otherwise
        creates a new layer stack for C{identifier}.


        This returns C{None} if C{identifier} is invalid (i.e. its root layer
        is C{None}). C{allErrors} will contain any errors encountered while
        creating a new layer stack. It'll be unchanged if the layer stack
        already existed.
        """
    def ComputePrimIndex(self, _primPath: pxr.Sdf.Path | str, /) -> tuple:
        """
        Compute and return a reference to the cached result for the prim index
        for the given path.


        C{allErrors} will contain any errors encountered while performing this
        operation.
        """
    def ComputePropertyIndex(self, _propPath: pxr.Sdf.Path | str, /) -> tuple:
        """
        Compute and return a reference to the cached result for the property
        index for the given path.


        C{allErrors} will contain any errors encountered while performing this
        operation.
        """
    def ComputeRelationshipTargetPaths(self, relPath: pxr.Sdf.Path | str, localOnly: bool = ..., stopProperty: pxr.Sdf.Spec = ..., includeStopProperty: bool = ...) -> tuple:
        """
        Compute the relationship target paths for the relationship at
        C{relationshipPath} into C{paths}.


        If C{localOnly} is C{true} then this will compose relationship targets
        from local nodes only. If C{stopProperty} is not C{None} then this
        will stop composing relationship targets at C{stopProperty}, including
        C{stopProperty} iff C{includeStopProperty} is C{true}. If not C{None},
        C{deletedPaths} will be populated with target paths whose deletion
        contributed to the computed result. C{allErrors} will contain any
        errors encountered while performing this operation.
        """
    def FindAllLayerStacksUsingLayer(self, _layer: pxr.Sdf.Layer, /) -> list[LayerStack]:
        """
        Returns every computed & cached layer stack that includes C{layer}.
        """
    def FindPrimIndex(self, _primPath: pxr.Sdf.Path | str, /) -> PrimIndex:
        """
        Returns a pointer to the cached computed prim index for the given
        path, or None if it has not been computed.
        """
    def FindPropertyIndex(self, _propPath: pxr.Sdf.Path | str, /) -> PropertyIndex:
        """
        Returns a pointer to the cached computed property index for the given
        path, or None if it has not been computed.
        """
    def FindSiteDependencies(self, siteLayerStack: LayerStack, sitePath: pxr.Sdf.Path | str, dependencyType: int = ..., recurseOnSite: bool = ..., recurseOnIndex: bool = ..., filterForExistingCachesOnly: bool = ...) -> list: ...
    def GetDynamicFileFormatArgumentDependencyData(self, _primIndexPath: pxr.Sdf.Path | str, /) -> DynamicFileFormatDependencyData:
        """
        Returns the dynamic file format dependency data object for the prim
        index with the given C{primIndexPath}.


        This will return an empty dependency data if either there is no cache
        prim index for the path or if the prim index has no dynamic file
        formats that it depends on.
        """
    def GetExpressionVariablesFromLayerStackUsedByPrim(self, layerStack: pxr.Sdf.Path | str, primIndexPath: LayerStack) -> list[str]:
        """
        Returns the set of expression variables in C{layerStack} that are used
        by the prim index at C{primIndexPath}.
        """
    def GetLayerStackIdentifier(self) -> LayerStackIdentifier:
        """
        Get the identifier of the layerStack used for composition.
        """
    def GetMutedLayers(self) -> list[str]:
        """
        Returns the list of canonical identifiers for muted layers in this
        cache.


        See documentation on RequestLayerMuting for more details.
        """
    def GetPrimsUsingExpressionVariablesFromLayerStack(self, layerStack: LayerStack) -> list[pxr.Sdf.Path]:
        """
        Returns the list of prim index paths that depend on one or more
        expression variables from C{layerStack}.
        """
    def GetUsedLayers(self) -> list[pxr.Sdf.Layer]:
        """
        Returns set of all layers used by this cache.
        """
    def GetUsedLayersRevision(self) -> int:
        """
        Return a number that can be used to determine whether or not the set
        of layers used by this cache may have changed or not.


        For example, if one calls GetUsedLayers() and saves the
        GetUsedLayersRevision() , and then later calls GetUsedLayersRevision()
        again, if the number is unchanged, then GetUsedLayers() is guaranteed
        to be unchanged as well.
        """
    def GetVariantFallbacks(self) -> dict:
        """
        Get the list of fallbacks to attempt to use when evaluating variant
        sets that lack an authored selection.
        """
    def HasAnyDynamicFileFormatArgumentAttributeDependencies(self) -> bool:
        """
        Returns true if any prim index in this cache has a dependency on a
        dynamic file format argument attribute's default value field.


        """
    def HasAnyDynamicFileFormatArgumentFieldDependencies(self) -> bool:
        """
        Returns true if any prim index in this cache has a dependency on a
        dynamic file format argument field.


        """
    def HasRootLayerStack(self, _layerStack: LayerStack, /) -> bool:
        """
        Return true if this cache's root layer stack is C{layerStack}, false
        otherwise.


        This is functionally equivalent to comparing against the result of
        GetLayerStack() , but does not require constructing a TfWeakPtr or any
        refcount operations.
        """
    def IsInvalidAssetPath(self, _resolvedAssetPath: str | pxr.Ar.ResolvedPath, /) -> bool:
        """
        Returns true if C{resolvedAssetPath} was used by a prim (e.g.


        in a reference) but did not resolve to a valid asset. This is
        functionally equivalent to examining the values in the map returned by
        GetInvalidAssetPaths, but more efficient.
        """
    def IsInvalidSublayerIdentifier(self, _identifier: str | pxr.Ar.ResolvedPath, /) -> bool:
        """
        Returns true if C{identifier} was used as a sublayer path in a layer
        stack but did not identify a valid layer.


        This is functionally equivalent to examining the values in the vector
        returned by GetInvalidSublayerIdentifiers, but more efficient.
        """
    def IsLayerMuted(self, layerIdentifier: str | pxr.Ar.ResolvedPath) -> bool:
        """
        Returns true if the layer specified by C{layerIdentifier} is muted in
        this cache, false otherwise.


        If C{layerIdentifier} is relative, it is assumed to be relative to
        this cache's root layer. See documentation on RequestLayerMuting for
        more details.
        """
    def IsPayloadIncluded(self, _path: pxr.Sdf.Path | str, /) -> bool:
        """
        Return true if the payload is included for the given path.
        """
    def IsPossibleDynamicFileFormatArgumentAttribute(self, _attributeName: str | pxr.Ar.ResolvedPath, /) -> bool:
        """
        Returns true if the given C{attributeName} is the name of an attribute
        whose default value field was composed while generating dynamic file
        format arguments for any prim index in this cache.


        """
    def IsPossibleDynamicFileFormatArgumentField(self, _field: str | pxr.Ar.ResolvedPath, /) -> bool:
        """
        Returns true if the given C{field} is the name of a field that was
        composed while generating dynamic file format arguments for any prim
        index in this cache.


        """
    def PrintStatistics(self) -> None:
        """
        Prints various statistics about the data stored in this cache.
        """
    def Reload(self) -> None:
        """
        Reload the layers of the layer stack, except session layers and
        sublayers of session layers.


        This will also try to load sublayers in this cache's layer stack that
        could not be loaded previously. It will also try to load any
        referenced or payloaded layer that could not be loaded previously.
        Clients should subsequently C{Apply()} C{changes} to use any now-valid
        layers.
        """
    def RequestLayerMuting(self, layersToMute: typing.Iterable[str | pxr.Ar.ResolvedPath], layersToUnmute: typing.Iterable[str | pxr.Ar.ResolvedPath]) -> None:
        """
        Request layers to be muted or unmuted in this cache.


        Muted layers are ignored during composition and do not appear in any
        layer stacks. The root layer of this stage may not be muted;
        attempting to do so will generate a coding error. If the root layer of
        a reference or payload layer stack is muted, the behavior is as if the
        muted layer did not exist, which means a composition error will be
        generated.

        A canonical identifier for each layer in C{layersToMute} will be
        computed using ArResolver::CreateIdentifier using the cache's root
        layer as the anchoring asset. If an identifier contains a file format
        target that matches this cache's file format target, that argument
        will be removed from the identifier. Any layer encountered during
        composition with the same canonical identifier will be considered
        muted and ignored.

        Note that muting a layer will cause this cache to release all
        references to that layer. If no other client is holding on to
        references to that layer, it will be unloaded. In this case, if there
        are unsaved edits to the muted layer, those edits are lost.  Since
        anonymous layers are not serialized, muting an anonymous layer will
        cause that layer and its contents to be lost in this case.

        If C{changes} is not C{nullptr}, it is adjusted to reflect the changes
        necessary to see the change in muted layers. Otherwise, those changes
        are applied immediately.

        C{newLayersMuted} and C{newLayersUnmuted} contains the pruned vector
        of layers which are muted or unmuted by this call to
        RequestLayerMuting.
        """
    def RequestPayloads(self, _pathsToInclude: typing.Iterable[pxr.Sdf.Path | str], _pathsToExclude: typing.Iterable[pxr.Sdf.Path | str], /) -> None:
        """
        Request payloads to be included or excluded from composition.


        pathsToInclude

        is a set of paths to add to the set for payload inclusion.
        pathsToExclude

        is a set of paths to remove from the set for payload inclusion.
        changes

        if not C{None}, is adjusted to reflect the changes necessary to see
        the change in payloads; otherwise those changes are applied
        immediately.

        If a path is listed in both pathsToInclude and pathsToExclude, it will
        be treated as an inclusion only.
        """
    def SetVariantFallbacks(self, _map: dict, /) -> None:
        """
        Set the list of fallbacks to attempt to use when evaluating variant
        sets that lack an authored selection.


        If C{changes} is not C{None} then it's adjusted to reflect the changes
        necessary to see the change in standin preferences, otherwise those
        changes are applied immediately.
        """
    def UsesLayerStack(self, _layerStack: LayerStack, /) -> bool:
        """
        Return true if C{layerStack} is used by this cache in its composition,
        false otherwise.
        """
    @property
    def fileFormatTarget(self) -> str:
        """
        Returns the file format target this cache is configured for.
        """
    @property
    def layerStack(self) -> LayerStack:
        """
        Get the layer stack for GetLayerStackIdentifier() .


        Note that this will neither compute the layer stack nor report errors.
        So if the layer stack has not been computed yet this will return
        C{None}. Use ComputeLayerStack() if you need to compute the layer
        stack if it hasn't been computed already and/or get errors caused by
        computing the layer stack.
        """

class Dependency(Boost.Python.instance):
    """
    Description of a dependency.
    """
    indexPath: Incomplete
    mapFunc: Incomplete
    sitePath: Incomplete
    def __init__(self, arg2: pxr.Sdf.Path | str, arg3: pxr.Sdf.Path | str, arg4: MapFunction, /) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...

class DependencyType(pxr.Tf.Tf_PyEnumWrapper):
    _baseName: ClassVar[str] = ...
    allValues: ClassVar[tuple] = ...
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def GetValueFromName(name: object) -> Any: ...

class DynamicFileFormatDependencyData(Boost.Python.instance):
    """
    Contains the necessary information for storing a prim index's
    dependency on dynamic file format arguments and determining if a field
    change affects the prim index.


    This data structure does not store the prim index or its path itself
    and is expected to be the data in some other data structure that maps
    prim indexes to its dependencies.
    """
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """
    def CanAttributeDefaultValueChangeAffectFileFormatArguments(self, _attributeName: str | pxr.Ar.ResolvedPath, _oldValue: Any, _newValue: Any, /) -> bool:
        """
        Given an C{attributeName} and the changed attribute default values in
        C{oldValue} and C{newValue}, this returns whether this default value
        change can affect any of the file format arguments generated by any of
        the contexts stored in this dependency.
        """
    def CanFieldChangeAffectFileFormatArguments(self, _fieldName: str | pxr.Ar.ResolvedPath, _oldValue: Any, _newValue: Any, /) -> bool:
        """
        Given a C{field} name and the changed field values in C{oldValue} and
        C{newValue}, this returns whether this change can affect any of the
        file format arguments generated by any of the contexts stored in this
        dependency.
        """
    def GetRelevantAttributeNames(self) -> list:
        """
        Returns a list of attribute names that were composed for any of the
        dependency contexts that were added to this dependency.
        """
    def GetRelevantFieldNames(self) -> list:
        """
        Returns a list of field names that were composed for any of the
        dependency contexts that were added to this dependency.
        """
    def IsEmpty(self) -> bool:
        """
        Returns whether this dependency data is empty.
        """

class ErrorArcCycle(ErrorBase):
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """

class ErrorArcPermissionDenied(ErrorBase):
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """

class ErrorBase(Boost.Python.instance):
    """
    Base class for all error types.
    """
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """
    @property
    def errorType(self): ...

class ErrorCapacityExceeded(ErrorBase):
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """

class ErrorInconsistentAttributeType(ErrorBase):
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """

class ErrorInconsistentAttributeVariability(ErrorBase):
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """

class ErrorInconsistentPropertyType(ErrorBase):
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """

class ErrorInvalidAssetPath(ErrorInvalidAssetPathBase):
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """

class ErrorInvalidAssetPathBase(ErrorBase):
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """

class ErrorInvalidAuthoredRelocation(ErrorRelocationBase):
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """

class ErrorInvalidConflictingRelocation(ErrorRelocationBase):
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """

class ErrorInvalidExternalTargetPath(ErrorTargetPathBase):
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """

class ErrorInvalidInstanceTargetPath(ErrorTargetPathBase):
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """

class ErrorInvalidPrimPath(ErrorBase):
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """

class ErrorInvalidReferenceOffset(ErrorBase):
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """

class ErrorInvalidSameTargetRelocations(ErrorRelocationBase):
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """

class ErrorInvalidSublayerOffset(ErrorBase):
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """

class ErrorInvalidSublayerOwnership(ErrorBase):
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """

class ErrorInvalidSublayerPath(ErrorBase):
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """

class ErrorInvalidTargetPath(ErrorTargetPathBase):
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """

class ErrorMutedAssetPath(ErrorInvalidAssetPathBase):
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """

class ErrorOpinionAtRelocationSource(ErrorBase):
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """

class ErrorPrimPermissionDenied(ErrorBase):
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """

class ErrorPropertyPermissionDenied(ErrorBase):
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """

class ErrorRelocationBase(ErrorBase):
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """

class ErrorSublayerCycle(ErrorBase):
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """

class ErrorTargetPathBase(ErrorBase):
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """

class ErrorTargetPermissionDenied(ErrorTargetPathBase):
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """

class ErrorType(pxr.Tf.Tf_PyEnumWrapper):
    _baseName: ClassVar[str] = ...
    allValues: ClassVar[tuple] = ...
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def GetValueFromName(name: object) -> Any: ...

class ErrorUnresolvedPrimPath(ErrorBase):
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """

class ErrorVariableExpressionError(ErrorBase):
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """

class ExpressionVariables(Boost.Python.instance):
    """
    Object containing composed expression variables associated with a
    given layer stack, identified by a PcpExpressionVariablesSource.
    """
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None:
        """
        Create a new object with no expression variables and the source set to
        the root layer stack.
        """
    @overload
    def __init__(self, _source: ExpressionVariablesSource, _expressionVariables: dict, /) -> None:
        """
        Creates a new object for C{source} with the given
        C{expressionVariables}.
        """
    @overload
    @staticmethod
    def Compute(sourceLayerStackId: LayerStackIdentifier, rootLayerStackId: LayerStackIdentifier, overrideExpressionVars: ExpressionVariables) -> ExpressionVariables:
        """
        Compute the composed expression variables for C{sourceLayerStackId},
        recursively computing and composing the overrides specified by its
        expressionVariableOverridesSource.


        If C{overrideExpressionVars} is provided, it will be used as the
        overrides instead of performing the recursive computation.
        """
    @overload
    @staticmethod
    def Compute(sourceLayerStackId: LayerStackIdentifier, rootLayerStackId: LayerStackIdentifier) -> ExpressionVariables:
        """
        Compute the composed expression variables for C{sourceLayerStackId},
        recursively computing and composing the overrides specified by its
        expressionVariableOverridesSource.


        If C{overrideExpressionVars} is provided, it will be used as the
        overrides instead of performing the recursive computation.
        """
    def GetSource(self) -> ExpressionVariablesSource:
        """
        Return the source of the composed expression variables.
        """
    def GetVariables(self) -> dict:
        """
        Returns the composed expression variables dictionary.
        """
    def __eq__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...

class ExpressionVariablesSource(Boost.Python.instance):
    """
    Represents the layer stack associated with a set of expression
    variables.


    This is typically a simple PcpLayerStackIdentifier.
    """
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None:
        """
        Create a PcpExpressionVariableSource representing the root layer stack
        of a prim index.
        """
    @overload
    def __init__(self, layerStackId: LayerStackIdentifier, rootLayerStackId: LayerStackIdentifier) -> None:
        """
        Create a PcpExpressionVariableSource representing the layer stack
        identified by C{layerStackIdentifier}.


        If C{layerStackIdentifier} is equal to C{rootLayerStackIdentifier},
        this is the same as the default constructor.
        """
    def GetLayerStackIdentifier(self) -> LayerStackIdentifier:
        """
        Return the identifier of the layer stack represented by this object if
        it is not the root layer stack.


        Return nullptr if this object represents the root layer stack (i.e.,
        IsRootLayerStack returns true).
        """
    def IsRootLayerStack(self) -> bool:
        """
        Return true if this object represents a prim index's root layer stack,
        false otherwise.


        If this function returns true, GetLayerStackIdentifier will return
        nullptr.
        """
    @overload
    def ResolveLayerStackIdentifier(self, arg2: LayerStackIdentifier, /) -> LayerStackIdentifier: ...
    @overload
    def ResolveLayerStackIdentifier(self, arg2: Cache, /) -> LayerStackIdentifier: ...
    def __eq__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...

class InstanceKey(Boost.Python.instance):
    """
    A PcpInstanceKey identifies instanceable prim indexes that share the
    same set of opinions.


    Instanceable prim indexes with equal instance keys are guaranteed to
    have the same opinions for name children and properties beneath those
    name children. They are NOT guaranteed to have the same opinions for
    direct properties of the prim indexes themselves.
    """
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, primIndex: PrimIndex) -> None:
        """
        Create an instance key for the given prim index.
        """
    def __eq__(self, other: object) -> bool:
        """
        Comparison operators.
        """
    def __hash__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...

class LayerStack(Boost.Python.instance):
    """
    Represents a stack of layers that contribute opinions to composition.


    Each PcpLayerStack is identified by a PcpLayerStackIdentifier. This
    identifier contains all of the parameters needed to construct a layer
    stack, such as the root layer, session layer, and path resolver
    context.

    PcpLayerStacks are constructed and managed by a
    Pcp_LayerStackRegistry.
    """
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """
    def __bool__(self) -> bool:
        """True if this object has not expired.  False otherwise."""
    def __eq__(self, other: object) -> bool:
        """Equality operator:  x == y"""
    def __lt__(self, other: object) -> bool:
        """Less than operator: x < y"""
    def __ne__(self, other: object) -> bool:
        """Non-equality operator: x != y"""
    @property
    def expired(self): ...
    @property
    def expressionVariableDependencies(self) -> list[str]:
        """
        Return the set of expression variables used during the computation of
        this layer stack.


        For example, this may include the variables used in expression
        variable expressions in sublayer asset paths.
        """
    @property
    def expressionVariables(self) -> ExpressionVariables:
        """
        Return the composed expression variables for this layer stack.
        """
    @property
    def identifier(self) -> LayerStackIdentifier:
        """
        Returns the identifier for this layer stack.
        """
    @property
    def incrementalRelocatesSourceToTarget(self) -> dict[pxr.Sdf.Path, pxr.Sdf.Path]:
        """
        Returns incremental relocation source-to-target mapping for this layer
        stack.


        This map contains the individual relocation entries found across all
        layers in this layer stack; it does not combine ancestral entries with
        descendant entries. For instance, if this layer stack contains
        relocations { /A: /B} and { /A/C: /A/D}, this map will contain { /A:
        /B} and { /A/C: /A/D}.
        """
    @property
    def incrementalRelocatesTargetToSource(self) -> dict[pxr.Sdf.Path, pxr.Sdf.Path]:
        """
        Returns incremental relocation target-to-source mapping for this layer
        stack.


        See GetIncrementalRelocatesTargetToSource for more details.
        """
    @property
    def layerOffsets(self): ...
    @property
    def layerTree(self) -> pxr.Sdf.LayerTree:
        """
        Returns the layer tree representing the structure of the non-session
        layers in the layer stack.
        """
    @property
    def layers(self) -> list[pxr.Sdf.Layer]:
        """
        Returns the layers in this layer stack in strong-to-weak order.


        Note that this is only the *local* layer stack  it does not include
        any layers brought in by references inside prims.
        """
    @property
    def localErrors(self) -> list[ErrorBase]:
        """
        Return the list of errors local to this layer stack.
        """
    @property
    def mutedLayers(self) -> list[str]:
        """
        Returns the set of layers that were muted in this layer stack.
        """
    @property
    def pathsToPrimsWithRelocates(self) -> list[pxr.Sdf.Path]:
        """
        Returns a list of paths to all prims across all layers in this layer
        stack that contained relocates.
        """
    @property
    def relocatesSourceToTarget(self) -> dict[pxr.Sdf.Path, pxr.Sdf.Path]:
        """
        Returns relocation source-to-target mapping for this layer stack.


        This map combines the individual relocation entries found across all
        layers in this layer stack; multiple entries that affect a single prim
        will be combined into a single entry. For instance, if this layer
        stack contains relocations { /A: /B} and { /A/C: /A/D}, this map will
        contain { /A: /B} and { /B/C: /B/D}. This allows consumers to go from
        unrelocated namespace to relocated namespace in a single step.
        """
    @property
    def relocatesTargetToSource(self) -> dict[pxr.Sdf.Path, pxr.Sdf.Path]:
        """
        Returns relocation target-to-source mapping for this layer stack.


        See GetRelocatesSourceToTarget for more details.
        """
    @property
    def sessionLayerTree(self) -> pxr.Sdf.LayerTree:
        """
        Returns the layer tree representing the structure of the session
        layers in the layer stack or null if there are no session layers.
        """

class LayerStackIdentifier(Boost.Python.instance):
    """
    Arguments used to identify a layer stack.


    Objects of this type are immutable.
    """
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None:
        """
        Construct with all empty pointers.
        """
    @overload
    def __init__(self, rootLayer: pxr.Sdf.Layer, sessionLayer: pxr.Sdf.Layer = ..., pathResolverContext: pxr.Ar.ResolverContext = ..., expressionVariablesOverrideSource: ExpressionVariablesSource = ...) -> None:
        """
        Construct with given pointers.


        If all arguments are C{TfNullPtr} then the result is identical to the
        default constructed object.
        """
    def __bool__(self) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    def __ge__(self, other: object) -> bool: ...
    def __gt__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    def __le__(self, other: object) -> bool: ...
    def __lt__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    @property
    def expressionVariablesOverrideSource(self): ...
    @property
    def pathResolverContext(self): ...
    @property
    def rootLayer(self): ...
    @property
    def sessionLayer(self): ...

class LayerStackSite(Boost.Python.instance):
    """
    A site specifies a path in a layer stack of scene description.
    """
    layerStack: Incomplete
    path: Incomplete
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """

class MapExpression(Boost.Python.instance):
    """
    An expression that yields a PcpMapFunction value.


    Expressions comprise constant values, variables, and operators applied
    to sub-expressions. Expressions cache their computed values
    internally. Assigning a new value to a variable automatically
    invalidates the cached values of dependent expressions. Common
    (sub-)expressions are automatically detected and shared.

    PcpMapExpression exists solely to support efficient incremental
    handling of relocates edits. It represents a tree of the namespace
    mapping operations and their inputs, so we can narrowly redo the
    computation when one of the inputs changes.
    """
    __instance_size__: ClassVar[int] = ...
    def __init__(self) -> None:
        """
        Default-construct a None expression.
        """
    def AddRootIdentity(self) -> MapExpression:
        """
        Return a new expression representing this expression with an added (if
        necessary) mapping from</>to</>.
        """
    def Compose(self, _f: MapExpression, /) -> MapExpression:
        """
        Create a new PcpMapExpression representing the application of f's
        value, followed by the application of this expression's value.
        """
    @staticmethod
    def Constant(_constValue: MapFunction, /) -> MapExpression:
        """
        Create a new constant.
        """
    def Evaluate(self) -> MapFunction:
        """
        Evaluate this expression, yielding a PcpMapFunction value.


        The computed result is cached. The return value is a reference to the
        internal cached value. The cache is automatically invalidated as
        needed.
        """
    @staticmethod
    def Identity() -> MapExpression:
        """
        Return an expression representing PcpMapFunction::Identity() .
        """
    @staticmethod
    def Inverse() -> MapExpression:
        """
        Create a new PcpMapExpression representing the inverse of f.
        """
    def MapSourceToTarget(self, path: pxr.Sdf.Path | str) -> pxr.Sdf.Path:
        """
        Map a path in the source namespace to the target.


        If the path is not in the domain, returns an empty path.
        """
    def MapTargetToSource(self, path: pxr.Sdf.Path | str) -> pxr.Sdf.Path:
        """
        Map a path in the target namespace to the source.


        If the path is not in the co-domain, returns an empty path.
        """
    @property
    def isIdentity(self) -> bool:
        """
        Return true if the evaluated map function is the identity function.


        For identity, MapSourceToTarget() always returns the path unchanged.
        """
    @property
    def isNull(self) -> bool:
        """
        Return true if this is a null expression.
        """
    @property
    def timeOffset(self) -> pxr.Sdf.LayerOffset:
        """
        The time offset of the mapping.
        """

class MapFunction(Boost.Python.instance):
    """
    A function that maps values from one namespace (and time domain) to
    another.


    It represents the transformation that an arc such as a reference arc
    applies as it incorporates values across the arc.

    Take the example of a reference arc, where a source path</Model>is
    referenced as a target path,</Model_1>. The source path</Model>is the
    source of the opinions; the target path</Model_1>is where they are
    incorporated in the scene. Values in the model that refer to paths
    relative to</Model>must be transformed to be relative
    to</Model_1>instead. The PcpMapFunction for the arc provides this
    service.

    Map functions have a specific *domain*, or set of values they can
    operate on. Any values outside the domain cannot be mapped. The domain
    precisely tracks what areas of namespace can be referred to across
    various forms of arcs.

    Map functions can be chained to represent a series of map operations
    applied in sequence. The map function represent the cumulative effect
    as efficiently as possible. For example, in the case of a chained
    reference from</Model>to</Model>to</Model>to</Model_1>, this is
    effectively the same as a mapping directly from</Model>to</Model_1>.
    Representing the cumulative effect of arcs in this way is important
    for handling larger scenes efficiently.

    Map functions can be *inverted*. Formally, map functions are
    bijections (one-to-one and onto), which ensures that they can be
    inverted. Put differently, no information is lost by applying a map
    function to set of values within its domain; they retain their
    distinct identities and can always be mapped back.

    One analogy that may or may not be helpful: In the same way a
    geometric transform maps a model's points in its rest space into the
    world coordinates for a particular instance, a PcpMapFunction maps
    values about a referenced model into the composed scene for a
    particular instance of that model. But rather than translating and
    rotating points, the map function shifts the values in namespace (and
    time).
    """
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None:
        """
        Construct a null function.
        """
    @overload
    def __init__(self, sourceToTargetMap: dict, timeOffset: pxr.Sdf.LayerOffset = ...) -> None: ...
    @overload
    def __init__(self, arg2: MapFunction, /) -> None: ...
    def Compose(self, _f: MapFunction, /) -> MapFunction:
        """
        Compose this map over the given map function.


        The result will represent the application of f followed by the
        application of this function.
        """
    def ComposeOffset(self, offset: pxr.Sdf.LayerOffset) -> MapFunction:
        """
        Compose this map function over a hypothetical map function that has an
        identity path mapping and C{offset}.


        This is equivalent to building such a map function and invoking
        Compose() , but is faster.
        """
    def GetInverse(self) -> MapFunction:
        """
        Return the inverse of this map function.


        This returns a true inverse C{inv:} for any path p in this function's
        domain that it maps to p', inv(p') ->p.
        """
    @staticmethod
    def Identity() -> MapFunction:
        """
        Construct an identity map function.
        """
    @staticmethod
    def IdentityPathMap() -> dict:
        """
        Returns an identity path mapping.
        """
    @overload
    def MapSourceToTarget(self, path: pxr.Sdf.Path | str) -> pxr.Sdf.Path:
        """
        Map a path in the source namespace to the target.


        If the path is not in the domain, returns an empty path.
        """
    @overload
    def MapSourceToTarget(self, pathExpr: pxr.Sdf.PathExpression) -> pxr.Sdf.PathExpression:
        """
        Map all path pattern prefix paths and expression reference paths in
        the source namespace to the target.


        For any references or patterns with prefix paths that are not in the
        domain, replace with an SdfPathPattern::Nothing() subexpression, to be
        simplified.

        For example, if the mapping specifies /Foo ->/World/Foo_1, and the
        expression is'/Foo/Bar//Baz + /Something/Else//Entirely', the
        resulting expression will be'/World/Foo_1/Bar//Baz', since the
        /Something/Else prefix is outside the domain.

        If C{excludedPatterns} and/or C{excludedReferences} are supplied, they
        are populated with those patterns & references that could not be
        translated and were replaced with SdfPathPattern::Nothing().
        """
    @overload
    def MapTargetToSource(self, path: pxr.Sdf.Path | str) -> pxr.Sdf.Path:
        """
        Map a path in the target namespace to the source.


        If the path is not in the co-domain, returns an empty path.
        """
    @overload
    def MapTargetToSource(self, pathExpr: pxr.Sdf.PathExpression) -> pxr.Sdf.PathExpression:
        """
        Map all path pattern prefix paths and expression reference paths in
        the target namespace to the source.


        For any references or patterns with prefix paths that are not in the
        co-domain, replace with an SdfPathPattern::Nothing() subexpression, to
        be simplified.

        For example, if the mapping specifies /World/Foo_1 ->/Foo, and the
        expression is'/World/Foo_1/Bar//Baz + /World/Bar//', the resulting
        expression will be'/Foo/Bar//Baz', since the /World/Bar prefix is
        outside the co-domain.

        If C{excludedPatterns} and/or C{excludedReferences} are supplied, they
        are populated with those patterns & references that could not be
        translated and were replaced with SdfPathPattern::Nothing().
        """
    def __eq__(self, other: object) -> bool:
        """
        Equality.
        """
    def __ne__(self, other: object) -> bool: ...
    @property
    def isIdentity(self) -> bool:
        """
        Return true if the map function is the identity function.


        The identity function has an identity path mapping and time offset.
        """
    @property
    def isIdentityPathMapping(self) -> bool:
        """
        Return true if the map function uses the identity path mapping.


        If true, MapSourceToTarget() always returns the path unchanged.
        However, this map function may have a non-identity time offset.
        """
    @property
    def isNull(self) -> bool:
        """
        Return true if this map function is the null function.


        For a null function, MapSourceToTarget() always returns an empty path.
        """
    @property
    def sourceToTargetMap(self) -> PathMap:
        """
        The set of path mappings, from source to target.
        """
    @property
    def timeOffset(self) -> pxr.Sdf.LayerOffset:
        """
        The time offset of the mapping.
        """

class NodeRef(Boost.Python.instance):
    """
    PcpNode represents a node in an expression tree for compositing scene
    description.


    A node represents the opinions from a particular site. In addition, it
    may have child nodes, representing nested expressions that are
    composited over/under this node.

    Child nodes are stored and composited in strength order.

    Each node holds information about the arc to its parent. This captures
    both the relative strength of the sub-expression as well as any value-
    mapping needed, such as to rename opinions from a model to use in a
    particular instance.
    """
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """
    def CanContributeSpecs(self) -> bool:
        """
        Returns true if this node is allowed to contribute opinions for
        composition, false otherwise.
        """
    def GetDepthBelowIntroduction(self) -> int:
        """
        Return the number of levels of namespace this node's site is below the
        level at which it was introduced by an arc.
        """
    def GetIntroPath(self) -> pxr.Sdf.Path:
        """
        Get the path that introduced this node.


        Specifically, this is the path the parent node had at the level of
        namespace where this node was added as a child. For a root node, this
        returns the absolute root path. See also GetDepthBelowIntroduction() .
        """
    def GetOriginRootNode(self) -> NodeRef:
        """
        Walk up to the root origin node for this node.


        This is the very first node that caused this node to be added to the
        graph. For instance, the root origin node of an implied inherit is the
        original inherit node.
        """
    def GetPathAtIntroduction(self) -> pxr.Sdf.Path:
        """
        Returns the path for this node's site when it was introduced.
        """
    def GetRootNode(self) -> NodeRef:
        """
        Walk up to the root node of this expression.
        """
    def GetSpecContributionRestrictedDepth(self) -> int:
        """
        Returns the namespace depth (i.e., the path element count) of this
        node's path when it was restricted from contributing opinions for
        composition.


        If this spec has no such restriction, returns 0.

        Note that unlike the value returned by GetNamespaceDepth, this value
        *does* include variant selections.
        """
    def IsDueToAncestor(self) -> bool: ...
    def IsRootNode(self) -> bool:
        """
        Returns true if this node is the root node of the prim index graph.
        """
    def __bool__(self) -> bool: ...
    def __eq__(self, other: object) -> bool:
        """
        Returns true if this references the same node as C{rhs}.
        """
    def __ne__(self, other: object) -> bool: ...
    @property
    def arcType(self) -> ArcType:
        """
        Returns the type of arc connecting this node to its parent node.
        """
    @property
    def children(self): ...
    @property
    def hasSpecs(self): ...
    @property
    def hasSymmetry(self): ...
    @property
    def isCulled(self) -> bool: ...
    @property
    def isInert(self) -> bool: ...
    @property
    def isRestricted(self) -> bool: ...
    @property
    def layerStack(self) -> LayerStack:
        """
        Returns the layer stack for the site this node represents.
        """
    @property
    def mapToParent(self) -> MapExpression:
        """
        Returns mapping function used to translate paths and values from this
        node to its parent node.
        """
    @property
    def mapToRoot(self) -> MapExpression:
        """
        Returns mapping function used to translate paths and values from this
        node directly to the root node.
        """
    @property
    def namespaceDepth(self) -> int:
        """
        Returns the absolute namespace depth of the node that introduced this
        node.


        Note that this does *not* count any variant selections.
        """
    @property
    def origin(self): ...
    @property
    def parent(self): ...
    @property
    def path(self) -> pxr.Sdf.Path:
        """
        Returns the path for the site this node represents.
        """
    @property
    def permission(self) -> pxr.Sdf.Permission: ...
    @property
    def siblingNumAtOrigin(self) -> int:
        """
        Returns this node's index among siblings with the same arc type at
        this node's origin.
        """
    @property
    def site(self) -> LayerStackSite:
        """
        Get the site this node represents.
        """

class PrimIndex(Boost.Python.instance):
    '''
    PcpPrimIndex is an index of the all sites of scene description that
    contribute opinions to a specific prim, under composition semantics.


    PcpComputePrimIndex() builds an index ("indexes") the given prim site.
    At any site there may be scene description values expressing arcs that
    represent instructions to pull in further scene description.
    PcpComputePrimIndex() recursively follows these arcs, building and
    ordering the results.
    '''
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """
    def ComposeAuthoredVariantSelections(self) -> dict:
        """
        Compose the authored prim variant selections.


        These are the variant selections expressed in scene description. Note
        that these selections may not have actually been applied, if they are
        invalid.

        This result is not cached, but computed each time.
        """
    def ComputePrimChildNames(self) -> tuple:
        """
        Compute the prim child names for the given path.


        C{errors} will contain any errors encountered while performing this
        operation.
        """
    def ComputePrimPropertyNames(self) -> list:
        """
        Compute the prim property names for the given path.


        C{errors} will contain any errors encountered while performing this
        operation. The C{nameOrder} vector must not contain any duplicate
        entries.
        """
    def DumpToDotGraph(self, filename: str | pxr.Ar.ResolvedPath, includeInheritOriginInfo: bool = ..., includeMaps: bool = ...) -> None:
        """
        Dump the prim index in dot format to the file named C{filename}.


        See Dump(...) for information regarding arguments.
        """
    def DumpToString(self, includeInheritOriginInfo: bool = ..., includeMaps: bool = ...) -> str:
        """
        Dump the prim index contents to a string.


        If C{includeInheritOriginInfo} is C{true}, output for implied inherit
        nodes will include information about the originating inherit node. If
        C{includeMaps} is C{true}, output for each node will include the
        mappings to the parent and root node.
        """
    @overload
    def GetNodeProvidingSpec(self, primSpec: pxr.Sdf.PrimSpec) -> NodeRef:
        """
        Returns the node that brings opinions from C{primSpec} into this prim
        index.


        If no such node exists, returns an invalid PcpNodeRef.
        """
    @overload
    def GetNodeProvidingSpec(self, layer: pxr.Sdf.Layer, path: pxr.Sdf.Path | str) -> NodeRef:
        """
        Returns the node that brings opinions from the Sd prim spec at
        C{layer} and C{path} into this prim index.


        If no such node exists, returns an invalid PcpNodeRef.
        """
    def GetSelectionAppliedForVariantSet(self, _variantSet: str | pxr.Ar.ResolvedPath, /) -> str:
        """
        Return the variant selection applied for the named variant set.


        If none was applied, this returns an empty string. This can be
        different from the authored variant selection; for example, if the
        authored selection is invalid.
        """
    def IsInstanceable(self) -> bool:
        """
        Returns true if this prim index is instanceable.


        Instanceable prim indexes with the same instance key are guaranteed to
        have the same set of opinions, but may not have local opinions about
        name children.

        PcpInstanceKey
        """
    def IsValid(self) -> bool:
        """
        Return true if this index is valid.


        A default-constructed index is invalid.
        """
    def PrintStatistics(self) -> None:
        """
        Prints various statistics about this prim index.
        """
    @property
    def hasAnyPayloads(self): ...
    @property
    def localErrors(self) -> list[ErrorBase]:
        """
        Return the list of errors local to this prim.
        """
    @property
    def primStack(self): ...
    @property
    def rootNode(self) -> NodeRef:
        """
        Returns the root node of the prim index graph.
        """

class PropertyIndex(Boost.Python.instance):
    """
    PcpPropertyIndex is an index of all sites in scene description that
    contribute opinions to a specific property, under composition
    semantics.
    """
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """
    @property
    def localErrors(self) -> list[ErrorBase]:
        """
        Return the list of errors local to this property.
        """
    @property
    def localPropertyStack(self): ...
    @property
    def propertyStack(self): ...

class Site(Boost.Python.instance):
    """
    A site specifies a path in a layer stack of scene description.
    """
    layerStack: Incomplete
    path: Incomplete
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """

class _TestChangeProcessor(Boost.Python.instance):
    __instance_size__: ClassVar[int] = ...
    def __init__(self, arg2: Cache, /) -> None: ...
    def GetPrimChanges(self) -> list: ...
    def GetSignificantChanges(self) -> list: ...
    def GetSpecChanges(self) -> list: ...
    def __enter__(self) -> _TestChangeProcessor: ...
    def __exit__(self, type: type[BaseException] | None, value: BaseException | None, traceback: types.TracebackType | None) -> None: ...

def BuildPrimPropertyIndex(_propertyPath: pxr.Sdf.Path | str, _cache: Cache, _owningPrimIndex: PrimIndex, /) -> tuple:
    """
    Builds a prim property index for the property at C{propertyPath}.


    C{allErrors} will contain any errors encountered.
    """
def TranslatePathFromNodeToRoot(_sourceNode: NodeRef, /, sourceNode: pxr.Sdf.Path | str) -> pxr.Sdf.Path:
    """
    Translates C{pathInNodeNamespace} from the namespace of the prim index
    node C{sourceNode} to the namespace of the prim index's root node.


    This applies all necessary namespace translations.

    If the path is successfully translated and C{pathWasTranslated} is
    supplied, it will be set to C{true}. In some cases, paths may fail to
    translate because they fall outside the set of paths that are allowed
    by nodes in the prim index. For instance, for a referenced model,
    paths referring to locations outside that model will not be
    translated. In these cases, this function will return an empty SdfPath
    and C{pathWasTranslated} will be set to C{false}.

    In Sd/Csd terminology, this is forward path translation from the
    namespace of the prim spec represented by C{sourceNode} to the
    composed scene namespace.
    """
def TranslatePathFromRootToNode(_destNode: NodeRef, /, destNode: pxr.Sdf.Path | str) -> pxr.Sdf.Path:
    """
    Translates C{pathInRootNamespace} from the namespace of the root of
    the prim index that C{destNode} belongs to to the namespace of
    C{destNode} itself.


    This applies all necessary namespace translations.

    If the path is successfully translated and C{pathWasTranslated} is
    supplied, it will be set to C{true}. In some cases, paths may fail to
    translate because they fall outside the set of paths that are allowed
    by nodes in the prim index. For instance, for a referenced model,
    paths referring to locations outside that model will not be
    translated. In these cases, this function will return an empty SdfPath
    and C{pathWasTranslated} will be set to C{false}.

    In Sd/Csd terminology, this is reverse path translation from the
    namespace of the composed scene to the namespace of the prim spec
    represented by C{destNode}.
    """
def _GetInvalidPcpNode() -> NodeRef: ...
