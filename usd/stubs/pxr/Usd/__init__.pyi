# mypy: disable-error-code="misc, override, no-redef"

import Boost.Python
import pxr.Ar
import pxr.Gf
import pxr.Kind
import pxr.Pcp
import pxr.Sdf
import pxr.Tf
import pxr.UsdGeom
import pxr.UsdShade
import pxr.Vt
import types
import typing
import typing_extensions
from _typeshed import Incomplete
from typing import Any, ClassVar, overload

BlockStageCachePopulation: StageCacheContextBlockType
BlockStageCaches: StageCacheContextBlockType
InterpolationTypeHeld: InterpolationType
InterpolationTypeLinear: InterpolationType
ListPositionBackOfAppendList: ListPosition
ListPositionBackOfPrependList: ListPosition
ListPositionFrontOfAppendList: ListPosition
ListPositionFrontOfPrependList: ListPosition
LoadWithDescendants: LoadPolicy
LoadWithoutDescendants: LoadPolicy
PrimAllPrimsPredicate: _PrimFlagsPredicate
PrimDefaultPredicate: _PrimFlagsConjunction
PrimHasDefiningSpecifier: _Term
PrimIsAbstract: _Term
PrimIsActive: _Term
PrimIsDefined: _Term
PrimIsGroup: _Term
PrimIsInstance: _Term
PrimIsLoaded: _Term
PrimIsModel: _Term
ResolveInfoSourceDefault: ResolveInfoSource
ResolveInfoSourceFallback: ResolveInfoSource
ResolveInfoSourceNone: ResolveInfoSource
ResolveInfoSourceTimeSamples: ResolveInfoSource
ResolveInfoSourceValueClips: ResolveInfoSource
_NoBlock: StageCacheContextBlockType
__MFB_FULL_PACKAGE_NAME: str

class APISchemaBase(SchemaBase):
    '''
    The base class for all *API* schemas.


    An API schema provides an interface to a prim\'s qualities, but does
    not specify a typeName for the underlying prim. The prim\'s qualities
    include its inheritance structure, attributes, relationships etc.
    Since it cannot provide a typeName, an API schema is considered to be
    non-concrete.

    To auto-generate an API schema using usdGenSchema, simply leave the
    typeName empty and make it inherit from"/APISchemaBase"or from another
    API schema. See UsdModelAPI, UsdClipsAPI and UsdCollectionAPI for
    examples.

    API schemas are classified into applied and non-applied API schemas.
    The author of an API schema has to decide on the type of API schema at
    the time of its creation by setting customData[\'apiSchemaType\'] in the
    schema definition (i.e. in the associated primSpec inside the
    schema.usda file). UsdAPISchemaBase implements methods that are used
    to record the application of an API schema on a USD prim.

    If an API schema only provides an interface to set certain core bits
    of metadata (like UsdModelAPI, which sets model kind and UsdClipsAPI,
    which sets clips-related metadata) OR if the API schema can apply to
    any type of prim or only to a known fixed set of prim types OR if
    there is no use of recording the application of the API schema, in
    such cases, it would be better to make it a non-applied API schema.
    Examples of non-applied API schemas include UsdModelAPI, UsdClipsAPI,
    UsdShadeConnectableAPI and UsdGeomPrimvarsAPI.

    If there is a need to discover (or record) whether a prim contains or
    subscribes to a given API schema, it would be advantageous to make the
    API schema be"applied". In general, API schemas that add one or more
    properties to a prim should be tagged as applied API schemas. A public
    Apply() method is generated for applied API schemas by usdGenSchema.
    An applied API schema must be applied to a prim via a call to the
    generated Apply() method, for the schema object to evaluate to true
    when converted to a bool using the explicit bool conversion operator.
    Examples of applied API schemas include UsdCollectionAPI,
    UsdGeomModelAPI and UsdGeomMotionAPI

    '''
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
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

class AssetInfoKeys(Boost.Python.instance):
    identifier: ClassVar[str] = ...  # read-only
    name: ClassVar[str] = ...  # read-only
    payloadAssetDependencies: ClassVar[str] = ...  # read-only
    version: ClassVar[str] = ...  # read-only
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """

class Attribute(Property):
    '''
    Scenegraph object for authoring and retrieving numeric, string, and
    array valued data, sampled over time.


    The allowed value types for UsdAttribute are dictated by the Sdf
    ("Scene Description Foundations") core\'s data model, which we
    summarize in Basic Datatypes for Scene Description Provided by Sdf.

    Attribute Defining Qualities
    ============================

    In addition to its value type, an Attribute has two other defining
    qualities:
       - B{Variability} Expresses whether an attribute is intended to have
         time samples ( GetVariability() == C{SdfVariabilityVarying}), or only
         a default ( GetVariability() == C{SdfVariabilityUniform}). For more on
         reasoning about time samples, see Value & Time-Sample Accessors.

       - B{Custom} Determines whether an attribute belongs to a schema (
         IsCustom() == C{false}), or is a user-defined, custom attribute.
         schema attributes will always be defined on a prim of the schema type,
         ans may possess fallback values from the schema, whereas custom
         attributes must always first be authored in order to be defined. Note
         that *custom* is actually an aspect of UsdProperty, as UsdRelationship
         can also be custom or provided by a schema.

    Attribute Creation and Existence
    ================================

    One can always create an attribute generically via
    UsdPrim::CreateAttribute() , which ensures that an attribute"is
    defined"in the current UsdEditTarget. In order to author any metadata
    or a default or timesample for an attribute, *it must first be
    defined*. It is sufficient that the attribute be defined in any one of
    the layers participating in the stage\'s current composition; for
    *builtin* attributes (those belonging to the owning prim\'s defining
    schema, i.e. the most specific subclass of UsdTypedSchema for which
    prim.IsA<schema>() will evaluate to true) there need be no authored
    scene description, because a definition is provided by the prim\'s
    schema definition.

    B{Creating} an attribute does not imply that the attribute has a
    value. More broadly, in the following code: ::

      if (UsdAttribute attr = prim.GetAttribute(TfToken("myAttr"))){
         ...
      }

    The UsdAttribute passes the bool test, because it is defined; however,
    inside the clause, we have no guarantee that attr has a value.

    Attribute Value Interpolation
    =============================

    UsdAttribute supports two interpolation behaviors when retrieving
    attribute values at times where no value is explicitly authored. The
    desired behavior may be specified via UsdStage::SetInterpolationType.
    That behavior will be used for all calls to UsdAttribute::Get.

    The supported interpolation types are:

       - B{Held} Attribute values are held constant between authored
         values. An attribute\'s value will be equal to the nearest preceding
         authored value. If there is no preceding authored value, the value
         will be equal to the nearest subsequent value.

       - B{Linear} Attribute values are linearly interpolated between
         authored values.
         Linear interpolation is only supported for certain data types. See
         USD_LINEAR_INTERPOLATION_TYPES for the list of these types. Types that
         do not support linear interpolation will use held interpolation
         instead.

    Linear interpolation is done element-by-element for array, vector, and
    matrix data types. If linear interpolation is requested for two array
    values with different sizes, held interpolation will be used instead.

    Attribute Value Blocking
    ========================

    While prims can effectively be removed from a scene by deactivating
    them, properties cannot. However, it is possible to B{block an
    attribute\'s value}, thus making the attribute behave as if it has a
    definition (and possibly metadata), but no authored value.

    One blocks an attribute using UsdAttribute::Block() , which will block
    the attribute in the stage\'s current UsdEditTarget, by authoring an
    SdfValueBlock in the attribute\'s *default*, and only values authored
    in weaker layers than the editTarget will be blocked. If the value
    block is the strongest authored opinion for the attribute, the
    HasAuthoredValue() method will return *false*, and the HasValue() and
    Get() methods will only return *true* if the attribute possesses a
    fallback value from the prim\'s schema."Unblocking"a blocked attribute
    is as simple as setting a *default* or timeSample value for the
    attribute in the same or stronger layer.

    The semantics of Value Clips necessitate the ability to selectively
    block an attribute\'s value for only some intervals in its authored
    range of samples. One can block an attribute\'s value at time *t* by
    calling C{attr.Set(SdfValueBlock, t)} When an attribute is
    thusly"partially blocked", UsdAttribute::Get() will succeed only for
    those time intervals whose left/earlier bracketing timeSample is
    B{not} SdfValueBlock.

    Due to this time-varying potential of value blocking, it may be the
    case that an attribute\'s HasAuthoredValue() and HasValue() methods
    both return *true* (because they do not and cannot consider time-
    varying blocks), but Get() may yet return *false* over some intervals.

    Attributes of type SdfAssetPath and UsdAttribute::Get()
    =======================================================

    If an attribute\'s value type is SdfAssetPath or SdfAssetPathArray,
    Get() performs extra work to compute the resolved asset paths, using
    the layer that has the strongest value opinion as the anchor
    for"relative"asset paths. Both the unresolved and resolved results are
    available through SdfAssetPath::GetAssetPath() and
    SdfAssetPath::GetResolvedPath() , respectively.

    Clients that call Get() on many asset-path-valued attributes may wish
    to employ an ArResolverScopedCache to improve asset path resolution
    performance.
    '''
    __instance_size__: ClassVar[int] = ...
    def __init__(self) -> None:
        """
        Construct an invalid attribute.
        """
    def AddConnection(self, source: pxr.Sdf.Path | str, position: ListPosition = ...) -> bool:
        """
        Adds C{source} to the list of connections, in the position specified
        by C{position}.


        Issue an error if C{source} identifies a prototype prim or an object
        descendant to a prototype prim. It is not valid to author connections
        to these objects.

        What data this actually authors depends on what data is currently
        authored in the authoring layer, with respect to list-editing
        semantics, which we will document soon
        """
    def Block(self) -> None:
        """
        Remove all time samples on an attribute and author a *block*
        C{default} value.


        This causes the attribute to resolve as if there were no authored
        value opinions in weaker layers.

        See Attribute Value Blocking for more information, including
        information on time-varying blocking.
        """
    def Clear(self) -> bool:
        """
        Clears the authored default value and all time samples for this
        attribute at the current EditTarget and returns true on success.


        Calling clear when either no value is authored or no spec is present,
        is a silent no-op returning true.

        This method does not affect any other data authored on this attribute.
        """
    def ClearAtTime(self, time: TimeCode | float | pxr.Sdf.TimeCode) -> bool:
        """
        Clear the authored value for this attribute at the given *time*, at
        the current EditTarget and return true on success.


        UsdTimeCode::Default() can be used to clear the default value.

        Calling clear when either no value is authored or no spec is present,
        is a silent no-op returning true.
        """
    def ClearColorSpace(self) -> bool:
        """
        Clears authored color-space value on the attribute.



        SetColorSpace()
        """
    def ClearConnections(self) -> bool:
        """
        Remove all opinions about the connections list from the current edit
        target.
        """
    def ClearDefault(self) -> bool:
        """
        Shorthand for ClearAtTime(UsdTimeCode::Default()).
        """
    def Get(self, time: TimeCode | float | pxr.Sdf.TimeCode = ...) -> Any:
        """
        Perform value resolution to fetch the value of this attribute at the
        requested UsdTimeCode C{time}, which defaults to *default*.


        If no value is authored at C{time} but values are authored at other
        times, this function will return an interpolated value based on the
        stage's interpolation type. See Attribute Value Interpolation.

        If no value is authored and no fallback value is provided by the
        schema for this attribute, this function will return false. If the
        consumer's use-case requires a default value, the consumer will need
        to provide one, possibly using GetTypeName() .GetDefaultValue().

        This templated accessor is designed for high performance data-
        streaming applications, allowing one to fetch data into the same
        container repeatedly, avoiding memory allocations when possible
        (VtArray containers will be resized as necessary to conform to the
        size of data being read).

        This template is only instantiated for the valid scene description
        value types and their corresponding VtArray containers. See Basic
        Datatypes for Scene Description Provided by Sdf for the complete list
        of types.

        Values are retrieved without regard to this attribute's variability.
        For example, a uniform attribute may retrieve time sample values if
        any are authored. However, the USD_VALIDATE_VARIABILITY TF_DEBUG code
        will cause debug information to be output if values that are
        inconsistent with this attribute's variability are retrieved. See
        UsdAttribute::GetVariability for more details.

        true if there was a value to be read, it was of the type T requested,
        and we read it successfully - false otherwise. For more details, see
        TimeSamples, Defaults, and Value Resolution, and also Attributes of
        type SdfAssetPath and UsdAttribute::Get() for information on how to
        retrieve resolved asset paths from SdfAssetPath-valued attributes.
        """
    def GetBracketingTimeSamples(self, desiredTime: float) -> tuple[float, float, bool]:
        """
        Populate *lower* and *upper* with the next greater and lesser value
        relative to the *desiredTime*.


        Return false if no value exists or an error occurs, true if either a
        default value or timeSamples exist.

        Use standard resolution semantics: if a stronger default value is
        authored over weaker time samples, the default value hides the
        underlying timeSamples.

        1) If a sample exists at the *desiredTime*, set both upper and lower
        to *desiredTime*.

        2) If samples exist surrounding, but not equal to the *desiredTime*,
        set lower and upper to the bracketing samples nearest to the
        *desiredTime*.

        3) If the *desiredTime* is outside of the range of authored samples,
        clamp upper and lower to the nearest time sample.

        4) If no samples exist, do not modify upper and lower and set
        *hasTimeSamples* to false.

        In cases (1), (2) and (3), set *hasTimeSamples* to true.

        All four cases above are considered to be successful, thus the return
        value will be true and no error message will be emitted.
        """
    def GetColorSpace(self) -> str:
        """
        Gets the color space in which the attribute is authored.



        SetColorSpace() UsdStage Color Configuration API
        """
    def GetConnections(self) -> list[pxr.Sdf.Path]:
        """
        Compose this attribute's connections and fill C{sources} with the
        result.


        All preexisting elements in C{sources} are lost.

        Returns true if any connection path opinions have been authored and no
        composition errors were encountered, returns false otherwise. Note
        that authored opinions may include opinions that clear the connections
        and a return value of true does not necessarily indicate that
        C{sources} will contain any connection paths.

        See Relationship Targets and Attribute Connections for details on
        behavior when targets point to objects beneath instance prims.

        The result is not cached, and thus recomputed on each query.
        """
    def GetNumTimeSamples(self) -> int:
        """
        Returns the number of time samples that have been authored.


        This method uses the standard resolution semantics, so if a stronger
        default value is authored over weaker time samples, the default value
        will hide the underlying timesamples.

        This function will query all value clips that may contribute time
        samples for this attribute, opening them if needed. This may be
        expensive, especially if many clips are involved.
        """
    def GetResolveInfo(self, time: TimeCode | float | pxr.Sdf.TimeCode = ...) -> ResolveInfo:
        """
        Perform value resolution to determine the source of the resolved value
        of this attribute at the requested UsdTimeCode C{time}.
        """
    def GetRoleName(self) -> str:
        """
        Return the roleName for this attribute's typeName.
        """
    def GetTimeSamples(self) -> list[float]:
        """
        Populates a vector with authored sample times.


        Returns false only on error.

        This method uses the standard resolution semantics, so if a stronger
        default value is authored over weaker time samples, the default value
        will hide the underlying timesamples.

        This function will query all value clips that may contribute time
        samples for this attribute, opening them if needed. This may be
        expensive, especially if many clips are involved. times

        - on return, will contain the *sorted*, ascending timeSample
        ordinates. Any data in C{times} will be lost, as this method clears
        C{times}.

        UsdAttribute::GetTimeSamplesInInterval
        """
    def GetTimeSamplesInInterval(self, interval: pxr.Gf.Interval) -> list[float]:
        """
        Populates a vector with authored sample times in C{interval}.


        Returns false only on an error.

        This function will only query the value clips that may contribute time
        samples for this attribute in the given interval, opening them if
        necessary. interval

        - the GfInterval on which to gather time samples. times

        - on return, will contain the *sorted*, ascending timeSample
        ordinates. Any data in C{times} will be lost, as this method clears
        C{times}.

        UsdAttribute::GetTimeSamples
        """
    def GetTypeName(self) -> pxr.Sdf.ValueTypeName:
        '''
        Return the"scene description"value type name for this attribute.
        '''
    @staticmethod
    def GetUnionedTimeSamples(attrs: typing.Iterable[Attribute | pxr.UsdGeom.ConstraintTarget | pxr.UsdGeom.Primvar | pxr.UsdGeom.XformOp | pxr.UsdShade.Input | pxr.UsdShade.Output]) -> list[float]:
        """
        Populates the given vector, C{times} with the union of all the
        authored sample times on all of the given attributes, C{attrs}.



        This function will query all value clips that may contribute time
        samples for the attributes in C{attrs}, opening them if needed. This
        may be expensive, especially if many clips are involved. The
        accumulated sample times will be in sorted (increasing) order and will
        not contain any duplicates.

        This clears any existing values in the C{times} vector before
        accumulating sample times of the given attributes.

        false if any of the attributes in C{attr} are invalid or if there's an
        error when fetching time-samples for any of the attributes.

        UsdAttribute::GetTimeSamples

        UsdAttribute::GetUnionedTimeSamplesInInterval
        """
    @staticmethod
    def GetUnionedTimeSamplesInInterval(attrs: typing.Iterable[Attribute | pxr.UsdGeom.ConstraintTarget | pxr.UsdGeom.Primvar | pxr.UsdGeom.XformOp | pxr.UsdShade.Input | pxr.UsdShade.Output], interval: pxr.Gf.Interval) -> list[float]:
        """
        Populates the given vector, C{times} with the union of all the
        authored sample times in the GfInterval, C{interval} on all of the
        given attributes, C{attrs}.



        This function will only query the value clips that may contribute time
        samples for the attributes in C{attrs}, in the given C{interval},
        opening them if necessary. The accumulated sample times will be in
        sorted (increasing) order and will not contain any duplicates.

        This clears any existing values in the C{times} vector before
        accumulating sample times of the given attributes.

        false if any of the attributes in C{attr} are invalid or if there's an
        error fetching time-samples for any of the attributes.

        UsdAttribute::GetTimeSamplesInInterval

        UsdAttribute::GetUnionedTimeSamples
        """
    def GetVariability(self) -> pxr.Sdf.Variability:
        """
        An attribute's variability expresses whether it is intended to have
        time-samples ( C{SdfVariabilityVarying}), or only a single default
        value ( C{SdfVariabilityUniform}).


        Variability is required meta-data of all attributes, and its fallback
        value is SdfVariabilityVarying.
        """
    def HasAuthoredConnections(self) -> bool:
        """
        Return true if this attribute has any authored opinions regarding
        connections.


        Note that this includes opinions that remove connections, so a true
        return does not necessarily indicate that this attribute has
        connections.
        """
    def HasAuthoredValue(self) -> bool:
        """
        Return true if this attribute has either an authored default value or
        authored time samples.


        If the attribute has been blocked, then return C{false}
        """
    def HasAuthoredValueOpinion(self) -> bool:
        """
        Deprecated

        This method is deprecated because it returns C{true} even when an
        attribute is blocked. Please use HasAuthoredValue() instead. If you
        truly need to know whether the attribute has B{any} authored value
        opinions, *including blocks*, you can make the following query:
        C{attr.GetResolveInfo(). HasAuthoredValueOpinion()}

        Return true if this attribute has either an authored default value or
        authored time samples.
        """
    def HasColorSpace(self) -> bool:
        """
        Returns whether color-space is authored on the attribute.



        GetColorSpace()
        """
    def HasFallbackValue(self) -> bool:
        """
        Return true if this attribute has a fallback value provided by a
        registered schema.
        """
    def HasValue(self) -> bool:
        """
        Return true if this attribute has an authored default value, authored
        time samples or a fallback value provided by a registered schema.


        If the attribute has been blocked, then return C{true} if and only if
        it has a fallback value.
        """
    def RemoveConnection(self, source: pxr.Sdf.Path | str) -> bool:
        """
        Removes C{target} from the list of targets.


        Issue an error if C{source} identifies a prototype prim or an object
        descendant to a prototype prim. It is not valid to author connections
        to these objects.
        """
    def Set(self, value: Any, time: TimeCode | float | pxr.Sdf.TimeCode = ...) -> bool:
        """
        Set the value of this attribute in the current UsdEditTarget to
        C{value} at UsdTimeCode C{time}, which defaults to *default*.


        Values are authored without regard to this attribute's variability.
        For example, time sample values may be authored on a uniform
        attribute. However, the USD_VALIDATE_VARIABILITY TF_DEBUG code will
        cause debug information to be output if values that are inconsistent
        with this attribute's variability are authored. See
        UsdAttribute::GetVariability for more details.

        false and generate an error if type C{T} does not match this
        attribute's defined scene description type B{exactly}, or if there is
        no existing definition for the attribute.
        """
    def SetColorSpace(self, _colorSpace: str | pxr.Ar.ResolvedPath, /) -> None:
        """
        Sets the color space of the attribute to C{colorSpace}.



        GetColorSpace() UsdStage Color Configuration API
        """
    def SetConnections(self, sources: typing.Iterable[pxr.Sdf.Path | str]) -> bool:
        """
        Make the authoring layer's opinion of the connection list explicit,
        and set exactly to C{sources}.


        Issue an error if C{source} identifies a prototype prim or an object
        descendant to a prototype prim. It is not valid to author connections
        to these objects.

        If any path in C{sources} is invalid, issue an error and return false.
        """
    def SetTypeName(self, typeName: pxr.Sdf.ValueTypeName) -> bool:
        """
        Set the value for typeName at the current EditTarget, return true on
        success, false if the value can not be written.


        B{Note} that this value should not be changed as it is typically
        either automatically authored or provided by a property definition.
        This method is provided primarily for fixing invalid scene
        description.
        """
    def SetVariability(self, variability: pxr.Sdf.Variability) -> bool:
        """
        Set the value for variability at the current EditTarget, return true
        on success, false if the value can not be written.


        B{Note} that this value should not be changed as it is typically
        either automatically authored or provided by a property definition.
        This method is provided primarily for fixing invalid scene
        description.
        """
    def ValueMightBeTimeVarying(self) -> bool:
        """
        Return true if it is possible, but not certain, that this attribute's
        value changes over time, false otherwise.


        If this function returns false, it is certain that this attribute's
        value remains constant over time.

        This function is equivalent to checking if GetNumTimeSamples() >1, but
        may be more efficient since it does not actually need to get a full
        count of all time samples.
        """

class AttributeQuery(Boost.Python.instance):
    """
    Object for efficiently making repeated queries for attribute values.


    Retrieving an attribute's value at a particular time requires
    determining the source of strongest opinion for that value. Often
    (i.e. unless the attribute is affected by Value Clips) this source
    does not vary over time. UsdAttributeQuery uses this fact to speed up
    repeated value queries by caching the source information for an
    attribute. It is safe to use a UsdAttributeQuery for any attribute -
    if the attribute *is* affected by Value Clips, the performance gain
    will just be less.

    Resolve targets
    ===============

    An attribute query can also be constructed for an attribute along with
    a UsdResolveTarget. A resolve target allows value resolution to
    consider only a subrange of the prim stack instead of the entirety of
    it. All of the methods of an attribute query created with a resolve
    target will perform value resolution within that resolve target. This
    can be useful for finding the value of an attribute resolved up to a
    particular layer or for determining if a value authored on layer would
    be overridden by a stronger opinion.

    Thread safety
    =============

    This object provides the basic thread-safety guarantee. Multiple
    threads may call the value accessor functions simultaneously.

    Invalidation
    ============

    This object does not listen for change notification. If a consumer is
    holding on to a UsdAttributeQuery, it is their responsibility to
    dispose of it in response to a resync change to the associated
    attribute. Failing to do so may result in incorrect values or crashes
    due to dereferencing invalid objects.
    """
    @overload
    def __init__(self, attribute: Attribute | pxr.UsdGeom.ConstraintTarget | pxr.UsdGeom.Primvar | pxr.UsdGeom.XformOp | pxr.UsdShade.Input | pxr.UsdShade.Output) -> None:
        """
        Construct a new query for the attribute C{attr}.
        """
    @overload
    def __init__(self, prim: Prim, attributeName: str | pxr.Ar.ResolvedPath) -> None:
        """
        Construct a new query for the attribute named C{attrName} under the
        prim C{prim}.
        """
    @overload
    def __init__(self, attribute: Attribute | pxr.UsdGeom.ConstraintTarget | pxr.UsdGeom.Primvar | pxr.UsdGeom.XformOp | pxr.UsdShade.Input | pxr.UsdShade.Output, resolveTarget: ResolveTarget) -> None:
        """
        Construct a new query for the attribute C{attr} with the given resolve
        target C{resolveTarget}.


        Note that a UsdResolveTarget is associated with a particular prim so
        only resolve targets for the attribute's owning prim are allowed.
        """
    @staticmethod
    def CreateQueries(prim: Prim, attributeNames: list[str] | list[pxr.Ar.ResolvedPath]) -> list[AttributeQuery]:
        """
        Construct new queries for the attributes named in C{attrNames} under
        the prim C{prim}.


        The objects in the returned vector will line up 1-to-1 with
        C{attrNames}.
        """
    def Get(self, time: TimeCode | float | pxr.Sdf.TimeCode = ...) -> Any:
        """
        Perform value resolution to fetch the value of the attribute
        associated with this query at the requested UsdTimeCode C{time}.



        UsdAttribute::Get
        """
    def GetAttribute(self) -> Attribute:
        """
        Return the attribute associated with this query.
        """
    def GetBracketingTimeSamples(self, desiredTime: float) -> tuple[float, float, bool]:
        """
        Populate *lower* and *upper* with the next greater and lesser value
        relative to the *desiredTime*.



        UsdAttribute::GetBracketingTimeSamples
        """
    def GetNumTimeSamples(self) -> int:
        """
        Returns the number of time samples that have been authored.



        UsdAttribute::GetNumTimeSamples
        """
    def GetTimeSamples(self) -> list[float]:
        """
        Populates a vector with authored sample times.


        Returns false only on error.  Behaves identically to
        UsdAttribute::GetTimeSamples()

        UsdAttributeQuery::GetTimeSamplesInInterval
        """
    def GetTimeSamplesInInterval(self, interval: pxr.Gf.Interval) -> list[float]:
        """
        Populates a vector with authored sample times in C{interval}.


        Returns false only on an error.

        Behaves identically to UsdAttribute::GetTimeSamplesInInterval()
        """
    @staticmethod
    def GetUnionedTimeSamples(attrQueries: typing.Iterable[AttributeQuery]) -> list[float]:
        """
        Populates the given vector, C{times} with the union of all the
        authored sample times on all of the given attribute-query objects,
        C{attrQueries}.


        Behaves identically to UsdAttribute::GetUnionedTimeSamples()

        false if one or more attribute-queries in C{attrQueries} are invalid
        or if there's an error fetching time-samples for any of the attribute-
        query objects.

        UsdAttribute::GetUnionedTimeSamples

        UsdAttributeQuery::GetUnionedTimeSamplesInInterval
        """
    @staticmethod
    def GetUnionedTimeSamplesInInterval(attrQueries: typing.Iterable[AttributeQuery], interval: pxr.Gf.Interval) -> list[float]:
        """
        Populates the given vector, C{times} with the union of all the
        authored sample times in the GfInterval, C{interval} on all of the
        given attribute-query objects, C{attrQueries}.


        Behaves identically to UsdAttribute::GetUnionedTimeSamplesInInterval()

        false if one or more attribute-queries in C{attrQueries} are invalid
        or if there's an error fetching time-samples for any of the attribute-
        query objects.

        UsdAttribute::GetUnionedTimeSamplesInInterval
        """
    def HasAuthoredValue(self) -> bool:
        """
        Return true if this attribute has either an authored default value or
        authored time samples.


        If the attribute has been blocked, then return C{false}

        UsdAttribute::HasAuthoredValue()
        """
    def HasAuthoredValueOpinion(self) -> bool:
        """
        Deprecated

        This method is deprecated because it returns C{true} even when an
        attribute is blocked. Please use HasAuthoredValue() instead. If you
        truly need to know whether the attribute has B{any} authored value
        opinions, *including blocks*, you can make the following query:
        C{query.GetAttribute().GetResolveInfo(). HasAuthoredValueOpinion()}

        Return true if this attribute has either an authored default value or
        authored time samples.
        """
    def HasFallbackValue(self) -> bool:
        """
        Return true if the attribute associated with this query has a fallback
        value provided by a registered schema.



        UsdAttribute::HasFallbackValue
        """
    def HasValue(self) -> bool:
        """
        Return true if the attribute associated with this query has an
        authored default value, authored time samples or a fallback value
        provided by a registered schema.



        UsdAttribute::HasValue
        """
    def IsValid(self) -> bool:
        """
        Return true if this query is valid (i.e.


        it is associated with a valid attribute), false otherwise.
        """
    def ValueMightBeTimeVarying(self) -> bool:
        """
        Return true if it is possible, but not certain, that this attribute's
        value changes over time, false otherwise.



        UsdAttribute::ValueMightBeTimeVarying
        """
    def __bool__(self) -> bool:
        """
        Returns C{true} if the query object is valid, C{false} otherwise.
        """

class ClipsAPI(APISchemaBase):
    '''
    UsdClipsAPI is an API schema that provides an interface to a prim\'s
    clip metadata.


    Clips are a"value resolution"feature that allows one to specify a
    sequence of usd files (clips) to be consulted, over time, as a source
    of varying overrides for the prims at and beneath this prim in
    namespace.

    SetClipAssetPaths() establishes the set of clips that can be
    consulted. SetClipActive() specifies the ordering of clip application
    over time (clips can be repeated), while SetClipTimes() specifies
    time-mapping from stage-time to clip-time for the clip active at a
    given stage-time, which allows for time-dilation and repetition of
    clips. Finally, SetClipPrimPath() determines the path within each clip
    that will map to this prim, i.e. the location within the clip at which
    we will look for opinions for this prim.

    The clip asset paths, times and active metadata can also be specified
    through template clip metadata. This can be desirable when your set of
    assets is very large, as the template metadata is much more concise.
    SetClipTemplateAssetPath() establishes the asset identifier pattern of
    the set of clips to be consulted. SetClipTemplateStride() ,
    SetClipTemplateEndTime() , and SetClipTemplateStartTime() specify the
    range in which USD will search, based on the template. From the set of
    resolved asset paths, times and active will be derived internally.

    A prim may have multiple"clip sets"  named sets of clips that each
    have their own values for the metadata described above. For example, a
    prim might have a clip set named"Clips_1"that specifies some group of
    clip asset paths, and another clip set named"Clips_2"that uses an
    entirely different set of clip asset paths. These clip sets are
    composed across composition arcs, so clip sets for a prim may be
    defined in multiple sublayers or references, for example. Individual
    metadata for a given clip set may be sparsely overridden.

    Important facts about clips:
       - Within the layerstack in which clips are established, the
         opinions within the clips will be *weaker* than any local opinions in
         the layerstack, but em stronger than varying opinions coming across
         references and variants.

       - We will never look for metadata or default opinions in clips
         when performing value resolution on the owning stage, since these
         quantities must be time-invariant.
         This leads to the common structure in which we reference a model
         asset on a prim, and then author clips at the same site: the asset
         reference will provide the topology and unvarying data for the model,
         while the clips will provide the time-sampled animation.

    For further information, see Sequencable, Re-timable Animated"Value
    Clips"
    '''
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, prim: Prim) -> None:
        """
        Construct a UsdClipsAPI on UsdPrim C{prim}.


        Equivalent to UsdClipsAPI::Get (prim.GetStage(), prim.GetPath()) for a
        *valid* C{prim}, but will not immediately throw an error for an
        invalid C{prim}
        """
    @overload
    def __init__(self, schemaObj: SchemaBase) -> None:
        """
        Construct a UsdClipsAPI on the prim held by C{schemaObj}.


        Should be preferred over UsdClipsAPI (schemaObj.GetPrim()), as it
        preserves SchemaBase state.
        """
    @overload
    def ComputeClipAssetPaths(self, clipSet: str | pxr.Ar.ResolvedPath) -> list[pxr.Sdf.AssetPath]:
        """
        Computes and resolves the list of clip asset paths used by the clip
        set named C{clipSet}.


        This is the same list of paths that would be used during value
        resolution.

        If the clip set is defined using template clip metadata, this function
        will compute the asset paths based on the template parameters.
        Otherwise this function will use the authored clipAssetPaths.
        """
    @overload
    def ComputeClipAssetPaths(self) -> list[pxr.Sdf.AssetPath]:
        """
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        This function operates on the default clip set.
        """
    @overload
    def GenerateClipManifest(self, clipSet: str | pxr.Ar.ResolvedPath, writeBlocksForClipsWithMissingValues: bool = ...) -> pxr.Sdf.Layer:
        """
        Create a clip manifest containing entries for all attributes in the
        value clips for clip set C{clipSet}.


        This returns an anonymous layer that can be exported and reused (

        SetClipManifestAssetPath). If C{writeBlocksForClipsWithMissingValues}
        is C{true}, the generated manifest will have value blocks authored for
        each attribute at the activation times of clips that do not contain
        time samples for that attribute. This accelerates searches done when
        the interpolation of missing clip values is enabled. See
        GetInterpolateMissingClipValues and Interpolating Missing Values in
        Clip Set for more details.

        Returns an invalid SdfLayerRefPtr on failure.
        """
    @overload
    def GenerateClipManifest(self, writeBlocksForClipsWithMissingValues: bool = ...) -> pxr.Sdf.Layer:
        """
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        This function operates on the default clip set.



        UsdClipsAPISetNames
        """
    @staticmethod
    def GenerateClipManifestFromLayers(clipLayers: list[pxr.Sdf.Layer], clipPrimPath: pxr.Sdf.Path | str) -> pxr.Sdf.Layer:
        """
        Create a clip manifest containing entries for all attributes in the
        given C{clipLayers} that belong to the prim at C{clipPrimPath} and all
        descendants.


        This returns an anonymous layer that can be exported and reused (

        SetClipManifestAssetPath). Returns an invalid SdfLayerRefPtr on
        failure.
        """
    @staticmethod
    def Get(stage: Stage, path: pxr.Sdf.Path | str) -> ClipsAPI:
        """
        Return a UsdClipsAPI holding the prim adhering to this schema at
        C{path} on C{stage}.


        If no prim exists at C{path} on C{stage}, or if the prim at that path
        does not adhere to this schema, return an invalid schema object. This
        is shorthand for the following: ::

          UsdClipsAPI(stage->GetPrimAtPath(path));

        """
    @overload
    def GetClipActive(self, clipSet: str | pxr.Ar.ResolvedPath) -> pxr.Vt.Vec2dArray:
        """
        List of pairs (time, clip index) indicating the time on the stage at
        which the clip in the clip set named C{clipSet} specified by the clip
        index is active.


        For instance, a value of [(0.0, 0), (20.0, 1)] indicates that clip 0
        is active at time 0 and clip 1 is active at time 20.
        """
    @overload
    def GetClipActive(self) -> pxr.Vt.Vec2dArray:
        """
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        This function operates on the default clip set.



        UsdClipsAPISetNames
        """
    @overload
    def GetClipAssetPaths(self, clipSet: str | pxr.Ar.ResolvedPath) -> list[pxr.Sdf.AssetPath]:
        """
        List of asset paths to the clips in the clip set named C{clipSet}.


        This list is unordered, but elements in this list are referred to by
        index in other clip-related fields.
        """
    @overload
    def GetClipAssetPaths(self) -> list[pxr.Sdf.AssetPath]:
        """
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        This function operates on the default clip set.



        UsdClipsAPISetNames
        """
    @overload
    def GetClipManifestAssetPath(self, clipSet: str | pxr.Ar.ResolvedPath) -> pxr.Sdf.AssetPath:
        """
        Asset path for the clip manifest for the clip set named C{clipSet}.


        The clip manifest indicates which attributes have time samples
        authored in the clips specified on this prim. During value resolution,
        clips will only be examined if the attribute exists and is declared as
        varying in the manifest. See Clip Manifest for more details.

        For instance, if this prim's path is</Prim_1>, the clip prim path
        is</Prim>, and we want values for the attribute</Prim_1.size>, we will
        only look within this prim's clips if the attribute</Prim.size>exists
        and is varying in the manifest.
        """
    @overload
    def GetClipManifestAssetPath(self) -> pxr.Sdf.AssetPath:
        """
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        This function operates on the default clip set.



        UsdClipsAPISetNames
        """
    @overload
    def GetClipPrimPath(self, clipSet: str | pxr.Ar.ResolvedPath) -> str:
        """
        Path to the prim in the clips in the clip set named C{clipSet} from
        which time samples will be read.


        This prim's path will be substituted with this value to determine the
        final path in the clip from which to read data. For instance, if this
        prims'path is'/Prim_1', the clip prim path is'/Prim', and we want to
        get values for the attribute'/Prim_1.size'. The clip prim path will be
        substituted in, yielding'/Prim.size', and each clip will be examined
        for values at that path.
        """
    @overload
    def GetClipPrimPath(self) -> str:
        """
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        This function operates on the default clip set.



        UsdClipsAPISetNames
        """
    def GetClipSets(self) -> pxr.Sdf.StringListOp:
        """
        ListOp that may be used to affect how opinions from clip sets are
        applied during value resolution.


        By default, clip sets in a layer stack are examined in lexicographical
        order by name for attribute values during value resolution. The clip
        sets listOp can be used to reorder the clip sets in a layer stack or
        remove them entirely from consideration during value resolution
        without modifying the clips dictionary.

        This is *not* the list of clip sets that are authored on this prim. To
        retrieve that information, use GetClips to examine the clips
        dictionary directly.

        This function returns the clip sets listOp from the current edit
        target.
        """
    @overload
    def GetClipTemplateActiveOffset(self, clipSet: str | pxr.Ar.ResolvedPath) -> float:
        """
        A double representing the offset value used by USD when determining
        the active period for each clip.


        """
    @overload
    def GetClipTemplateActiveOffset(self) -> float:
        """
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        This function operates on the default clip set.



        UsdClipsAPISetNames
        """
    @overload
    def GetClipTemplateAssetPath(self, clipSet: str | pxr.Ar.ResolvedPath) -> str:
        """
        A template string representing a set of assets to be used as clips for
        the clip set named C{clipSet}.


        This string can be of two forms:

        integer frames: path/basename.###.usd

        subinteger frames: path/basename.##.##.usd.

        For the integer portion of the specification, USD will take a
        particular time, determined by the template start time, stride, and
        end time, and pad it with zeros up to the number of hashes provided so
        long as the number of hashes is greater than the digits required to
        specify the integer value.

        For instance:

        time = 12, template asset path = foo.##.usd =>foo.12.usd time = 12,
        template asset path = foo.###.usd =>foo.012.usd time = 333, template
        asset path = foo.#.usd =>foo.333.usd

        In the case of subinteger portion of a specifications, USD requires
        the specification to be exact.

        For instance:

        time = 1.15, template asset path = foo.#.###.usd =>foo.1.150.usd time
        = 1.145, template asset path = foo.#.##.usd =>foo.1.15.usd time = 1.1,
        template asset path = foo.#.##.usd =>foo.1.10.usd

        Note that USD requires that hash groups be adjacent in the string, and
        that there only be one or two such groups.
        """
    @overload
    def GetClipTemplateAssetPath(self) -> str:
        """
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        This function operates on the default clip set.



        UsdClipsAPISetNames
        """
    @overload
    def GetClipTemplateEndTime(self, clipSet: str | pxr.Ar.ResolvedPath) -> float:
        """
        A double which indicates the end of the range USD will use to to
        search for asset paths for the clip set named C{clipSet}.


        This value is inclusive in that range.

        GetClipTemplateAssetPath.
        """
    @overload
    def GetClipTemplateEndTime(self) -> float:
        """
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        This function operates on the default clip set.



        UsdClipsAPISetNames
        """
    @overload
    def GetClipTemplateStartTime(self, clipSet: str | pxr.Ar.ResolvedPath) -> float:
        """
        A double which indicates the start of the range USD will use to search
        for asset paths for the clip set named C{clipSet}.


        This value is inclusive in that range.

        GetClipTemplateAssetPath.
        """
    @overload
    def GetClipTemplateStartTime(self) -> float:
        """
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        This function operates on the default clip set.



        UsdClipsAPISetNames
        """
    @overload
    def GetClipTemplateStride(self, clipSet: str | pxr.Ar.ResolvedPath) -> float:
        """
        A double representing the increment value USD will use when searching
        for asset paths for the clip set named C{clipSet}.



        GetClipTemplateAssetPath.
        """
    @overload
    def GetClipTemplateStride(self) -> float:
        """
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        This function operates on the default clip set.



        UsdClipsAPISetNames
        """
    @overload
    def GetClipTimes(self, clipSet: str | pxr.Ar.ResolvedPath) -> pxr.Vt.Vec2dArray:
        """
        List of pairs (stage time, clip time) indicating the time in the
        active clip in the clip set named C{clipSet} that should be consulted
        for values at the corresponding stage time.


        During value resolution, this list will be sorted by stage time; times
        will then be linearly interpolated between consecutive entries. For
        instance, for clip times [(0.0, 0.0), (10.0, 20.0)], at stage time 0,
        values from the active clip at time 0 will be used, at stage time 5,
        values from the active clip at time 10, and at stage time 10, clip
        values at time 20.
        """
    @overload
    def GetClipTimes(self) -> pxr.Vt.Vec2dArray:
        """
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        This function operates on the default clip set.



        UsdClipsAPISetNames
        """
    def GetClips(self) -> dict:
        """
        Dictionary that contains the definition of the clip sets on this prim.


        Each entry in this dictionary defines a clip set: the entry's key is
        the name of the clip set and the entry's value is a dictionary
        containing the metadata that specifies the clips in the set.

        See UsdClipsAPIInfoKeys for the keys used for each clip set's
        dictionary, or use the other API to set or get values for a given clip
        set.
        """
    @overload
    def GetInterpolateMissingClipValues(self, clipSet: str | pxr.Ar.ResolvedPath) -> bool: ...
    @overload
    def GetInterpolateMissingClipValues(self) -> bool:
        """
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        This function operates on the default clip set.
        """
    @staticmethod
    def GetSchemaAttributeNames(includeInherited: bool = ...) -> list[str]:
        """
        Return a vector of names of all pre-declared attributes for this
        schema class and all its ancestor classes.


        Does not include attributes that may be authored by custom/extended
        methods of the schemas involved.
        """
    @overload
    def SetClipActive(self, activeClips: pxr.Vt.Vec2dArray | typing.Iterable[list[float]] | typing.Iterable[pxr.Gf.Vec2d] | typing.Iterable[tuple[float, float]], clipSet: str | pxr.Ar.ResolvedPath) -> None:
        """
        Set the active clip metadata for the clip set named C{clipSet}.



        GetClipActive()
        """
    @overload
    def SetClipActive(self, activeClips: pxr.Vt.Vec2dArray | typing.Iterable[list[float]] | typing.Iterable[pxr.Gf.Vec2d] | typing.Iterable[tuple[float, float]]) -> None:
        """
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        This function operates on the default clip set.



        UsdClipsAPISetNames
        """
    @overload
    def SetClipAssetPaths(self, assetPaths: list[pxr.Sdf.AssetPath] | list[str], clipSet: str | pxr.Ar.ResolvedPath) -> None:
        """
        Set the clip asset paths for the clip set named C{clipSet}.



        GetClipAssetPaths()
        """
    @overload
    def SetClipAssetPaths(self, assetPaths: list[pxr.Sdf.AssetPath] | list[str]) -> None:
        """
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        This function operates on the default clip set.



        UsdClipsAPISetNames
        """
    @overload
    def SetClipManifestAssetPath(self, manifestAssetPath: pxr.Sdf.AssetPath | str, clipSet: str | pxr.Ar.ResolvedPath) -> bool:
        """
        Set the clip manifest asset path for this prim.



        GetClipManifestAssetPath()
        """
    @overload
    def SetClipManifestAssetPath(self, manifestAssetPath: pxr.Sdf.AssetPath | str) -> bool:
        """
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        This function operates on the default clip set.



        UsdClipsAPISetNames
        """
    @overload
    def SetClipPrimPath(self, primPath: str | pxr.Ar.ResolvedPath, clipSet: str | pxr.Ar.ResolvedPath) -> bool:
        """
        Set the clip prim path for the clip set named C{clipSet}.



        GetClipPrimPath()
        """
    @overload
    def SetClipPrimPath(self, primPath: str | pxr.Ar.ResolvedPath) -> bool:
        """
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        This function operates on the default clip set.



        UsdClipsAPISetNames
        """
    def SetClipSets(self, clipSets: pxr.Sdf.StringListOp) -> bool:
        """
        Set the clip sets list op for this prim.



        GetClipSets
        """
    @overload
    def SetClipTemplateActiveOffset(self, clipTemplateActiveOffset: float, clipSet: str | pxr.Ar.ResolvedPath) -> bool:
        """
        Set the clip template offset for the clip set named C{clipSet}.



        GetClipTemplateActiveOffset
        """
    @overload
    def SetClipTemplateActiveOffset(self, clipTemplateActiveOffset: float) -> bool:
        """
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        This function operates on the default clip set.



        UsdClipsAPISetNames
        """
    @overload
    def SetClipTemplateAssetPath(self, clipTemplateAssetPath: str | pxr.Ar.ResolvedPath, clipSet: str | pxr.Ar.ResolvedPath) -> None:
        """
        Set the clip template asset path for the clip set named C{clipSet}.



        GetClipTemplateAssetPath
        """
    @overload
    def SetClipTemplateAssetPath(self, clipTemplateAssetPath: str | pxr.Ar.ResolvedPath) -> None:
        """
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        This function operates on the default clip set.



        UsdClipsAPISetNames
        """
    @overload
    def SetClipTemplateEndTime(self, clipTemplateEndTime: float, clipSet: str | pxr.Ar.ResolvedPath) -> bool:
        """
        Set the template end time for the clipset named C{clipSet}.



        GetClipTemplateEndTime()
        """
    @overload
    def SetClipTemplateEndTime(self, clipTemplateEndTime: float) -> bool:
        """
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        This function operates on the default clip set.



        UsdClipsAPISetNames
        """
    @overload
    def SetClipTemplateStartTime(self, clipTemplateStartTime: float, clipSet: str | pxr.Ar.ResolvedPath) -> bool:
        """
        Set the template start time for the clip set named C{clipSet}.



        GetClipTemplateStartTime
        """
    @overload
    def SetClipTemplateStartTime(self, clipTemplateStartTime: float) -> bool:
        """
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        This function operates on the default clip set.



        UsdClipsAPISetNames
        """
    @overload
    def SetClipTemplateStride(self, clipTemplateStride: float, clipSet: str | pxr.Ar.ResolvedPath) -> bool:
        """
        Set the template stride for the clip set named C{clipSet}.



        GetClipTemplateStride()
        """
    @overload
    def SetClipTemplateStride(self, clipTemplateStride: float) -> bool:
        """
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        This function operates on the default clip set.



        UsdClipsAPISetNames
        """
    @overload
    def SetClipTimes(self, clipTimes: pxr.Vt.Vec2dArray | typing.Iterable[list[float]] | typing.Iterable[pxr.Gf.Vec2d] | typing.Iterable[tuple[float, float]], clipSet: str | pxr.Ar.ResolvedPath) -> None:
        """
        Set the clip times metadata for this prim.



        GetClipTimes()
        """
    @overload
    def SetClipTimes(self, clipTimes: pxr.Vt.Vec2dArray | typing.Iterable[list[float]] | typing.Iterable[pxr.Gf.Vec2d] | typing.Iterable[tuple[float, float]]) -> None:
        """
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        This function operates on the default clip set.



        UsdClipsAPISetNames
        """
    def SetClips(self, clips: dict) -> bool:
        """
        Set the clips dictionary for this prim.



        GetClips
        """
    @overload
    def SetInterpolateMissingClipValues(self, interpolate: bool, clipSet: str | pxr.Ar.ResolvedPath) -> bool:
        """
        Set whether missing clip values are interpolated from surrounding
        clips.
        """
    @overload
    def SetInterpolateMissingClipValues(self, interpolate: bool) -> bool:
        """
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        This function operates on the default clip set.
        """
    @staticmethod
    def _GetStaticTfType() -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...

class CollectionAPI(APISchemaBase):
    '''
    This is a general purpose API schema, used to describe a collection of
    heterogeneous objects within the scene.


    "Objects"here may be prims or properties belonging to prims or other
    collections. It\'s an add-on schema that can be applied many times to a
    prim with different collection names.

    A collection allows an enumeration of a set of paths to include and a
    set of paths to exclude. Whether the descendants of an included path
    are members of a collection are decided by its expansion rule (see
    below). If the collection excludes paths that are not descendents of
    included paths, the collection implicitly includes the root path</>.
    If such a collection also includes paths that are not descendants of
    the excluded paths, it is considered invalid, since the intention is
    ambiguous.

    All the properties authored by the schema are namespaced
    under"collection:". The given name of the collection provides
    additional namespacing for the various per-collection properties,
    which include the following:

       - B{uniform token collection: *collectionName* :expansionRule} -
         specified how the paths that are included in the collection must be
         expanded to determine its members. Possible values include:
       - B{explicitOnly} - only paths in the includes rel targets and not
         in the excludes rel targets belong to the collection.

       - B{expandPrims} - all the prims at or below the includes rel-
         targets (and not under the excludes rel-targets) belong to the
         collection. Any property paths included in the collection would, of
         course, also be honored. This is the default behavior as it satisfies
         most use cases.

       - B{expandPrimsAndProperties} - like expandPrims, but also includes
         all properties on all matched prims. We\'re still not quite sure what
         the use cases are for this, but you can use it to capture a whole lot
         of UsdObjects very concisely.

       - B{bool collection: *collectionName* :includeRoot} - boolean
         attribute indicating whether the pseudo-root path</>should be counted
         as one of the included target paths. The fallback is false. This
         separate attribute is required because relationships cannot directly
         target the root. When expansionRule is explicitOnly, this attribute is
         ignored.

       - B{rel collection: *collectionName* :includes} - specifies a list
         of targets that are included in the collection. This can target prims
         or properties directly. A collection can insert the rules of another
         collection by making its *includes* relationship target the
         B{collection:{collectionName}} property on the owning prim of the
         collection to be included (see UsdCollectionAPI::GetCollectionAttr).
         It is important to note that including another collection does not
         guarantee the contents of that collection will be in the final
         collection; instead, the rules are merged. This means, for example, an
         exclude entry may exclude a portion of the included collection. When a
         collection includes one or more collections, the order in which
         targets are added to the includes relationship may become significant,
         if there are conflicting opinions about the same path. Targets that
         are added later are considered to be stronger than earlier targets for
         the same path.

       - B{rel collection: *collectionName* :excludes} - specifies a list
         of targets that are excluded below the B{included} paths in this
         collection. This can target prims or properties directly, but B{cannot
         target another collection}. This is to keep the membership determining
         logic simple, efficient and easier to reason about. Finally, it is
         invalid for a collection to exclude paths that are not included in it.
         The presence of such"orphaned"excluded paths will not affect the set
         of paths included in the collection, but may affect the performance of
         querying membership of a path in the collection (see
         UsdCollectionAPI::MembershipQuery::IsPathIncluded) or of enumerating
         the objects belonging to the collection (see
         UsdCollectionAPI::GetIncludedObjects).

       - B{uniform opaque collection: *collectionName*} - opaque attribute
         (meaning it can never have a value) that represents the collection for
         the purpose of allowing another collection to include it. When this
         property is targeted by another collection\'s *includes* relationship,
         the rules of this collection will be inserted into the rules of the
         collection that includes it.

    B{Implicit inclusion}

    In some scenarios it is useful to express a collection that includes
    everything except certain paths. To support this, a collection that
    has an exclude that is not a descendent of any include will include
    the root path</>.

    B{Creating collections in C++} ::

      bool ApplyCollections(UsdPrim const  & prim)
      {       
          /* Assuming the folling prim hierarchy:
          |- Vehicles 
          |    |- FourWheelers
          |    |    |- CarA
          |    |    |- CarB
          |    |    |- CarC
          |    |    |- CarD
          |    |    |- TruckA
          |    |    |- TruckB
          |    |- TwoWheelers
          |    |    |- BikeA
          |    |    |- BikeB
          |    |    |- BicycleA
          |    |        |- FrontWheel
          |    |        |- BackWheel
          |    |- Other
          |    |    |- TricycleA
          |    |        |- FrontWheel
          |    |        |- BackWheels
          */
  
          // Create a collection that includes only the cars, by adding all 
          // of "FourWheelers" and excluding the trucks.
          UsdCollectionAPI cars = UsdCollectionAPI::Apply(prim, "cars");
          cars.CreateIncludesRel().AddTarget(SdfPath("/Vehicles/FourWheelers"));
          cars.CreateExcludesRel().AddTarget(SdfPath("/Vehicles/FourWheelers/TruckA"));
          cars.CreateExcludesRel().AddTarget(SdfPath("/Vehicles/FourWheelers/TruckB"));
  
          // Create a collection that includes only the bikes by explicitly inluding 
          // just the two bikes in the collection.
          UsdCollectionAPI bikes = UsdCollectionAPI::Apply(prim, "bikes");
          bikes.CreateExpansionRuleAttr(VtValue(UsdTokens->explicitOnly));
          bikes.CreateIncludesRel().AddTarget(SdfPath("/Vehicles/TwoWheelers/BikeA"));
          bikes.CreateIncludesRel().AddTarget(SdfPath("/Vehicles/TwoWheelers/BikeB"));
  
          // Create an explicit collection of slow-moving vehicles. 
          // An explicit collection implies that descendants (i.e. the front and back 
          // wheels) are not considered to be included in the collection.
          UsdCollectionAPI slowVehicles = UsdCollectionAPI::Apply(prim, "slowVehicles");
          slowVehicles.CreateExpansionRuleAttr(VtValue(UsdTokens->explicitOnly));
          slowVehicles.CreateIncludesRel().AddTarget(SdfPath("/Vehicles/TwoWheelers/BicycleA"));
          slowVehicles.CreateIncludesRel().AddTarget(SdfPath("/Vehicles/Other/TricycleA"));
  
          UsdCollectionAPI vehicles = UsdCollectionAPI::Apply(prim, "vehicles");
          vehicles.CreateIncludesRel().AddTarget(cars.GetCollectionPath());
          vehicles.CreateIncludesRel().AddTarget(bikes.GetCollectionPath());
          vehicles.CreateIncludesRel().AddTarget(slowVehicles.GetCollectionPath());
          vehicles.CreateIncludesRel().AddTarget(SdfPath("/Vehicles/FourWheelers/TruckA"));
          vehicles.CreateIncludesRel().AddTarget(SdfPath("/Vehicles/FourWheelers/TruckB"));
  
  
          UsdCollectionAPI::MembershipQuery query = vehicles.ComputeMembershipQuery();
  
          // CarA is included in the \'vehicles\' collection through the \'cars\' collection.
          TF_AXIOM(query.IsPathIncluded("/Vehicles/FourWheelers/CarA"))
  
          // BikeB is included in the \'vehicles\' collection through the \'cars\' collection.
          TF_AXIOM(query.IsPathIncluded("/Vehicles/TwoWheelers/BikeB"))
  
          // BikeB is included directly in the \'vehicles\' collection 
          TF_AXIOM(query.IsPathIncluded("/Vehicles/FourWheelers/TruckA"))
  
          // BicycleA is included, but it\'s descendants are not, since it is part of 
          // an "explicitOnly" collection.
          TF_AXIOM(query.IsPathIncluded("/Vehicles/TwoWheelers/BicycleA"))
          TF_AXIOM(!query.IsPathIncluded("/Vehicles/TwoWheelers/BicycleA/FrontWheel"))
  
          // TricycleA is included, but it\'s descendants are not, since it is part of 
          // an "explicitOnly" collection.
          TF_AXIOM(query.IsPathIncluded("/Vehicles/Other/TricycleA"))
          TF_AXIOM(!query.IsPathIncluded("/Vehicles/Other/TricycleA/BackWheels"))
  
          SdfPathSet includedPaths;
          UsdCollectionAPI::ComputeIncludedPaths(query, prim.GetStage(), 
                                                  & includedPaths);
          std::set<UsdObject> includedObjects;
          UsdCollectionAPI::ComputeIncludedObjects(query, prim.GetStage(), 
                                                    & includedObjects);
      }
  

    For any described attribute *Fallback* *Value* or *Allowed* *Values*
    below that are text/tokens, the actual token is published and defined
    in UsdTokens. So to set an attribute to the value"rightHanded", use
    UsdTokens->rightHanded as the value.
    '''
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self, prim: Prim, name: str | pxr.Ar.ResolvedPath) -> None:
        '''
        Construct a UsdCollectionAPI on UsdPrim C{prim} with name C{name}.


        Equivalent to UsdCollectionAPI::Get ( prim.GetStage(),
        prim.GetPath().AppendProperty("collection:name"));

        for a *valid* C{prim}, but will not immediately throw an error for an
        invalid C{prim}
        '''
    @overload
    def __init__(self, _schemaObj: Prim, _name: str | pxr.Ar.ResolvedPath, /) -> None:
        """
        Construct a UsdCollectionAPI on the prim held by C{schemaObj} with
        name C{name}.


        Should be preferred over UsdCollectionAPI (schemaObj.GetPrim(), name),
        as it preserves SchemaBase state.
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, schemaObj: SchemaBase, name: object) -> None: ...
    @staticmethod
    def Apply(prim: Prim, name: str | pxr.Ar.ResolvedPath) -> CollectionAPI:
        '''
        Applies this B{multiple-apply} API schema to the given C{prim} along
        with the given instance name, C{name}.


        This information is stored by adding"CollectionAPI:<i>name</i>"to the
        token-valued, listOp metadata *apiSchemas* on the prim. For example,
        if C{name} is\'instance1\', the token\'CollectionAPI:instance1\'is added
        to\'apiSchemas\'.

        A valid UsdCollectionAPI object is returned upon success. An invalid
        (or empty) UsdCollectionAPI object is returned upon failure. See
        UsdPrim::ApplyAPI() for conditions resulting in failure.

        UsdPrim::GetAppliedSchemas()

        UsdPrim::HasAPI()

        UsdPrim::CanApplyAPI()

        UsdPrim::ApplyAPI()

        UsdPrim::RemoveAPI()
        '''
    def BlockCollection(self) -> bool:
        '''
        Blocks the targets of the includes and excludes relationships of the
        collection, making it<* *empty* if"includeRoot"is false (or unset) or.



           - *include everything* if"includeRoot"is true. (assuming there are
             no opinions in stronger edit targets).

        '''
    @staticmethod
    def CanApply(prim: Prim, name: str | pxr.Ar.ResolvedPath) -> _CanApplyResult:
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
        Test whether a given C{name} contains the"collection:"prefix.
        '''
    @staticmethod
    def ComputeIncludedObjects(query: UsdCollectionMembershipQuery, stage: Stage, predicate: _PrimFlagsPredicate | _Term = ...) -> list[Object]:
        """
        Returns all the usd objects that satisfy the predicate, C{pred} in the
        collection represented by the UsdCollectionMembershipQuery object,
        C{query}.


        The results depends on the load state of the UsdStage, C{stage}.
        """
    @staticmethod
    def ComputeIncludedPaths(query: UsdCollectionMembershipQuery, stage: Stage, predicate: _PrimFlagsPredicate | _Term = ...) -> list[pxr.Sdf.Path]:
        """
        Returns all the paths that satisfy the predicate, C{pred} in the
        collection represented by the UsdCollectionMembershipQuery object,
        C{query}.


        The result depends on the load state of the UsdStage, C{stage}.
        """
    def ComputeMembershipQuery(self) -> UsdCollectionMembershipQuery:
        """
        Computes and returns a UsdCollectionMembershipQuery object which can
        be used to query inclusion or exclusion of paths in the collection.
        """
    def CreateCollectionAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> Attribute:
        """
        See GetCollectionAttr() , and also Create vs Get Property Methods for
        when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateExcludesRel(self) -> Relationship:
        """
        See GetExcludesRel() , and also Create vs Get Property Methods for
        when to use Get vs Create.
        """
    def CreateExpansionRuleAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> Attribute:
        """
        See GetExpansionRuleAttr() , and also Create vs Get Property Methods
        for when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateIncludeRootAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> Attribute:
        """
        See GetIncludeRootAttr() , and also Create vs Get Property Methods for
        when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateIncludesRel(self) -> Relationship:
        """
        See GetIncludesRel() , and also Create vs Get Property Methods for
        when to use Get vs Create.
        """
    def CreateMembershipExpressionAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> Attribute:
        """
        See GetMembershipExpressionAttr() , and also Create vs Get Property
        Methods for when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def ExcludePath(self, pathToExclude: pxr.Sdf.Path | str) -> bool:
        """
        Excludes or removes the given path, C{pathToExclude} from the
        collection.


        If the collection is empty, the collection becomes one that includes
        all paths except the givne path. Otherwise, this does nothing if the
        path is not included in the collection.

        This does not modify the expansion-rule of the collection. Hence, if
        the expansionRule is *expandPrims* or *expandPrimsAndProperties*, then
        the descendants of C{pathToExclude} will also be excluded from the
        collection, unless explicitly included.

        UsdCollectionAPI::IncludePath()
        """
    @overload
    @staticmethod
    def Get(stage: Stage, path: pxr.Sdf.Path | str) -> CollectionAPI:
        """
        Return a UsdCollectionAPI holding the prim adhering to this schema at
        C{path} on C{stage}.


        If no prim exists at C{path} on C{stage}, or if the prim at that path
        does not adhere to this schema, return an invalid schema object.
        C{path} must be of the format<path>.collection:name.

        This is shorthand for the following: ::

          TfToken name = SdfPath::StripNamespace(path.GetToken());
          UsdCollectionAPI(
              stage->GetPrimAtPath(path.GetPrimPath()), name);

        """
    @overload
    @staticmethod
    def Get(prim: Prim, name: str | pxr.Ar.ResolvedPath) -> CollectionAPI:
        """
        Return a UsdCollectionAPI with name C{name} holding the prim C{prim}.


        Shorthand for UsdCollectionAPI(prim, name);
        """
    @staticmethod
    def GetAll(prim: Prim) -> list[CollectionAPI]:
        """
        Return a vector of all named instances of UsdCollectionAPI on the
        given C{prim}.
        """
    @staticmethod
    def GetAllCollections(prim: Prim) -> list[CollectionAPI]:
        """
        Returns all the named collections on the given USD prim.


        Deprecated

        Use GetAll(prim) instead.
        """
    @overload
    @staticmethod
    def GetCollection(stage: Stage, collectionPath: pxr.Sdf.Path | str) -> CollectionAPI:
        """
        Returns the collection represented by the given collection path,
        C{collectionPath} on the given USD stage.
        """
    @overload
    @staticmethod
    def GetCollection(prim: Prim, name: str | pxr.Ar.ResolvedPath) -> CollectionAPI:
        """
        Returns the schema object representing a collection named C{name} on
        the given C{prim}.
        """
    def GetCollectionAttr(self) -> Attribute:
        """
        This property represents the collection for the purpose of allowing
        another collection to include it.


        When this property is targeted by another collection's *includes*
        relationship, the rules of this collection will be inserted into the
        rules of the collection that includes it.

        Declaration

        C{uniform opaque __INSTANCE_NAME__}

        C++ Type

        SdfOpaqueValue

        Usd Type

        SdfValueTypeNames->Opaque

        Variability

        SdfVariabilityUniform
        """
    def GetCollectionPath(self) -> pxr.Sdf.Path:
        '''
        Returns the canonical path that represents this collection.


        This points to the property named"collection:{collectionName}"on the
        prim defining the collection. This is the path to be used
        to"include"this collection in another collection.

        GetCollectionAttr()
        '''
    def GetExcludesRel(self) -> Relationship:
        '''
        Specifies a list of targets that are excluded below the included paths
        in this collection.


        This can target prims or properties directly, but cannot target
        another collection. This is to keep the membership determining logic
        simple, efficient and easier to reason about. Finally, it is invalid
        for a collection to exclude paths that are not included in it. The
        presence of such"orphaned"excluded paths will not affect the set of
        paths included in the collection, but may affect the performance of
        querying membership of a path in the collection (see
        UsdCollectionAPI::MembershipQuery::IsPathIncluded) or of enumerating
        the objects belonging to the collection (see
        UsdCollectionAPI::GetIncludedObjects).
        '''
    def GetExpansionRuleAttr(self) -> Attribute:
        '''
        Specifies how the paths that are included in the collection must be
        expanded to determine its members.



        Declaration

        C{uniform token expansionRule ="expandPrims"}

        C++ Type

        TfToken

        Usd Type

        SdfValueTypeNames->Token

        Variability

        SdfVariabilityUniform

        Allowed Values

        explicitOnly, expandPrims, expandPrimsAndProperties
        '''
    def GetIncludeRootAttr(self) -> Attribute:
        """
        Boolean attribute indicating whether the pseudo-root path</>should be
        counted as one of the included target paths.


        The fallback is false. This separate attribute is required because
        relationships cannot directly target the root.

        Declaration

        C{uniform bool includeRoot}

        C++ Type

        bool

        Usd Type

        SdfValueTypeNames->Bool

        Variability

        SdfVariabilityUniform
        """
    def GetIncludesRel(self) -> Relationship:
        """
        Specifies a list of targets that are included in the collection.


        This can target prims or properties directly. A collection can insert
        the rules of another collection by making its *includes* relationship
        target the B{collection:{collectionName}} property on the owning prim
        of the collection to be included
        """
    def GetMembershipExpressionAttr(self) -> Attribute:
        """
        Specifies a path expression that determines membership in this
        collection.



        Declaration

        C{uniform pathExpression membershipExpression}

        C++ Type

        SdfPathExpression

        Usd Type

        SdfValueTypeNames->PathExpression

        Variability

        SdfVariabilityUniform
        """
    def GetName(self) -> str:
        """
        Returns the name of this multiple-apply schema instance.
        """
    @staticmethod
    def GetNamedCollectionPath(prim: Prim, collectionName: str | pxr.Ar.ResolvedPath) -> pxr.Sdf.Path:
        """
        Returns the canonical path to the collection named, C{name} on the
        given prim, C{prim}.



        GetCollectionPath()
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
    def HasNoIncludedPaths(self) -> bool:
        """
        Returns true if the collection has nothing included in it.


        This requires both that the includes relationship have no target
        paths, and that the includeRoot attribute be false. Note that there
        may be cases where the collection has no objects included in it even
        when HasNoIncludedPaths() returns false. For example, if the included
        objects are unloaded or if the included objects are also excluded.
        """
    def IncludePath(self, pathToInclude: pxr.Sdf.Path | str) -> bool:
        """
        Includes or adds the given path, C{pathToInclude} in the collection.


        This does nothing if the path is already included in the collection.

        This does not modify the expansion-rule of the collection. Hence, if
        the expansionRule is *expandPrims* or *expandPrimsAndProperties*, then
        the descendants of C{pathToInclude} will be also included in the
        collection unless explicitly excluded.

        UsdCollectionAPI::ExcludePath()
        """
    @staticmethod
    def IsCollectionAPIPath(_path: pxr.Sdf.Path | str, /) -> bool:
        """
        Checks if the given path C{path} is of an API schema of type
        CollectionAPI.


        If so, it stores the instance name of the schema in C{name} and
        returns true. Otherwise, it returns false.
        """
    @staticmethod
    def IsSchemaPropertyBaseName(baseName: str | pxr.Ar.ResolvedPath) -> bool:
        """
        Checks if the given name C{baseName} is the base name of a property of
        CollectionAPI.
        """
    def ResetCollection(self) -> bool:
        '''
        Resets the collection by clearing both the includes and excludes
        targets of the collection in the current UsdEditTarget.



        This does not modify the"includeRoot"attribute which is used to
        include or exclude everything (i.e. the pseudoRoot) in the USD stage.
        '''
    def Validate(self) -> str:
        '''
        Validates the collection by checking the following rules:



           - a collection\'s expansionRule should be one
             of"explicitOnly","expandPrims"or"expandPrimsAndProperties".

           - a collection should not have have a circular dependency on
             another collection.

           - a collection should not have both includes and excludes among its
             top-level rules

        '''
    @staticmethod
    def _GetStaticTfType() -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...

class CompositionArc(Boost.Python.instance):
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """
    def GetArcType(self) -> Any: ...
    def GetIntroducingLayer(self) -> pxr.Sdf.Layer: ...
    def GetIntroducingListEditor(self) -> tuple: ...
    def GetIntroducingNode(self) -> pxr.Pcp.NodeRef: ...
    def GetIntroducingPrimPath(self) -> pxr.Sdf.Path: ...
    def GetTargetLayer(self) -> pxr.Sdf.Layer: ...
    def GetTargetNode(self) -> pxr.Pcp.NodeRef: ...
    def GetTargetPrimPath(self) -> pxr.Sdf.Path: ...
    def HasSpecs(self) -> bool: ...
    def IsAncestral(self) -> bool: ...
    def IsImplicit(self) -> bool: ...
    def IsIntroducedInRootLayerPrimSpec(self) -> bool: ...
    def IsIntroducedInRootLayerStack(self) -> bool: ...
    def MakeResolveTargetStrongerThan(self, subLayer: pxr.Sdf.Layer = ...) -> ResolveTarget: ...
    def MakeResolveTargetUpTo(self, subLayer: pxr.Sdf.Layer = ...) -> ResolveTarget: ...

class CrateInfo(Boost.Python.instance):
    """
    A class for introspecting the underlying qualities of
    .usdc'crate'files, for diagnostic purposes.
    """

    class Section(Boost.Python.instance):
        __instance_size__: ClassVar[int] = ...
        name: Incomplete
        size: Incomplete
        start: Incomplete
        @overload
        def __init__(self) -> None: ...
        @overload
        def __init__(self, name: str | pxr.Ar.ResolvedPath, start: int, size: int) -> None: ...

    class SummaryStats(Boost.Python.instance):
        __instance_size__: ClassVar[int] = ...
        numSpecs: Incomplete
        numUniqueFieldSets: Incomplete
        numUniqueFields: Incomplete
        numUniquePaths: Incomplete
        numUniqueStrings: Incomplete
        numUniqueTokens: Incomplete
        def __init__(self) -> None: ...
    __instance_size__: ClassVar[int] = ...
    def __init__(self) -> None: ...
    def GetFileVersion(self) -> str:
        """
        Return the file version.
        """
    def GetSections(self) -> list[CrateInfo.Section]:
        """
        Return the named file sections, their location and sizes in the file.
        """
    def GetSoftwareVersion(self) -> str:
        """
        Return the software version.
        """
    def GetSummaryStats(self) -> CrateInfo.SummaryStats:
        """
        Return summary statistics structure for this file.
        """
    @staticmethod
    def Open(fileName: str | pxr.Ar.ResolvedPath) -> CrateInfo:
        """
        Attempt to open and read C{fileName}.
        """
    def __bool__(self) -> bool:
        """
        Return true if this object refers to a valid file.
        """

class EditContext(Boost.Python.instance):
    '''
    A utility class to temporarily modify a stage\'s current EditTarget
    during an execution scope.


    This is an"RAII"-like object meant to be used as an automatic local
    variable. Upon construction, it sets a given stage\'s EditTarget, and
    upon destruction it restores the stage\'s EditTarget to what it was
    previously.

    Example usage, temporarily overriding a stage\'s EditTarget to direct
    an edit to the stage\'s session layer. When the *ctx* object expires,
    it restores the stage\'s EditTarget to whatever it was previously. ::

      void SetVisState(const UsdPrim  & prim, bool vis) {
          UsdEditContext ctx(prim.GetStage(),
                             prim.GetStage()->GetSessionLayer());
          prim.GetAttribute("visible").Set(vis);
      }

    B{Threading Note}

    When one thread is mutating a *UsdStage*, it is unsafe for any other
    thread to either query or mutate it. Using this class with a stage in
    such a way that it modifies the stage\'s EditTarget constitutes a
    mutation.
    '''
    __instance_size__: ClassVar[int] = ...
    def __init__(self, stage: Stage, editTarget: EditTarget | pxr.Sdf.Layer = ...) -> None:
        """
        Construct and save *stage's* current EditTarget to restore on
        destruction, then invoke stage->SetEditTarget(editTarget).


        If *stage* is invalid, a coding error will be issued by the
        constructor, and this class takes no action.

        If *editTarget* is invalid, a coding error will be issued by the
        *stage*, and its EditTarget will not be modified.
        """
    def __enter__(self) -> EditContext: ...
    def __exit__(self, type: type[BaseException] | None, value: BaseException | None, traceback: types.TracebackType | None) -> None: ...

class EditTarget(Boost.Python.instance):
    """
    Defines a mapping from scene graph paths to Sdf spec paths in a
    SdfLayer where edits should be directed, or up to where to perform
    partial composition.


    A UsdEditTarget can represent an arbitrary point in a composition
    graph for the purposes of placing edits and resolving values. This
    enables editing and resolving across references, classes, variants,
    and payloads.

    In the simplest case, an EditTarget represents a single layer in a
    stage's local LayerStack. In this case, the mapping that transforms
    scene graph paths to spec paths in the layer is the identity function.
    That is, the UsdAttribute path'/World/Foo.avar'would map to the
    SdfPropertySpec path'/World/Foo.avar'.

    For a more complex example, suppose'/World/Foo'in'Shot.usda'is a
    reference to'/Model'in'Model.usda'. One can construct a UsdEditTarget
    that maps scene graph paths from the'Shot.usda'stage across the
    reference to the appropriate paths in the'Model.usda'layer. For
    example, the UsdAttribute '/World/Foo.avar'would map to the
    SdfPropertySpec '/Model.avar'. Paths in the stage composed
    at'Shot.usda'that weren't prefixed by'/World/Foo'would not have a
    valid mapping to'Model.usda'.

    EditTargets may also work for any other kind of arc or series of arcs.
    This allows for editing across variants, classes, and payloads, or in
    a variant on the far side of a reference, for example.

    In addition to mapping scene paths to spec paths for editing,
    EditTargets may also be used to identify points in the composition
    graph for partial composition. Though it doesn't currently exist, a
    UsdCompose API that takes UsdEditTarget arguments may someday be
    provided.

    For convenience and deployment ease, SdfLayerHandles will implicitly
    convert to UsdEditTargets. A UsdEditTarget constructed in this way
    means direct opinions in a layer in a stage's local LayerStack.
    """
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None:
        """
        Construct a null EditTarget.


        A null EditTarget will return paths unchanged when asked to map paths.
        """
    @overload
    def __init__(self, layer: pxr.Sdf.Layer, node: pxr.Pcp.NodeRef = ...) -> None:
        """
        Construct an EditTarget with *layer* and *node*.


        The mapping will be used to map paths from the scene into the
        *layer's* namespace given the *PcpNodeRef* *node's* mapping.
        """
    def ComposeOver(self, weaker: EditTarget | pxr.Sdf.Layer) -> EditTarget:
        '''
        Return a new EditTarget composed over *weaker*.


        This is typically used to make an EditTarget"explicit". For example,
        an edit target with a layer but with no mapping and no LayerStack
        identifier indicates a layer in the local LayerStack of a composed
        scene. However, an EditTarget with the same layer but an explicit
        identity mapping and the LayerStack identifier of the composed scene
        may be desired. This can be obtained by composing a partial (e.g.
        layer only) EditTarget over an explicit EditTarget with layer, mapping
        and layer stack identifier.
        '''
    @staticmethod
    def ForLocalDirectVariant(layer: pxr.Sdf.Layer, varSelPath: pxr.Sdf.Path | str) -> EditTarget:
        """
        Convenience constructor for editing a direct variant in a local
        LayerStack.


        The C{varSelPath} must be a prim variant selection path (see
        SdfPath::IsPrimVariantSelectionPath() ).
        """
    def GetLayer(self) -> pxr.Sdf.Layer:
        """
        Return the layer this EditTarget contains.
        """
    def GetMapFunction(self) -> pxr.Pcp.MapFunction:
        """
        Returns the PcpMapFunction representing the map from source specs
        (including any variant selections) to the stage.
        """
    def GetPrimSpecForScenePath(self, scenePath: pxr.Sdf.Path | str) -> pxr.Sdf.PrimSpec:
        """
        Convenience function for getting the PrimSpec in the edit target's
        layer for *scenePath*.


        This is equivalent to
        target.GetLayer()->GetPrimAtPath(target.MapToSpecPath(scenePath)) if
        target has a valid layer. If this target IsNull or there is no valid
        mapping from *scenePath* to a SdfPrimSpec path in the layer, return
        null.
        """
    def GetPropertySpecForScenePath(self, scenePath: pxr.Sdf.Path | str) -> pxr.Sdf.PropertySpec: ...
    def GetSpecForScenePath(self, scenePath: pxr.Sdf.Path | str) -> pxr.Sdf.PrimSpec: ...
    def IsNull(self) -> bool:
        """
        Return true if this EditTarget is null.


        Null EditTargets map paths unchanged, and have no layer or LayerStack
        identifier.
        """
    def IsValid(self) -> bool:
        """
        Return true if this EditTarget is valid, false otherwise.


        Edit targets are considered valid when they have a layer.
        """
    def MapToSpecPath(self, scenePath: pxr.Sdf.Path | str) -> pxr.Sdf.Path:
        """
        Map the provided *scenePath* into a SdfSpec path for the EditTarget's
        layer, according to the EditTarget's mapping.


        Null edit targets and EditTargets for which *IsLocalLayer* are true
        return scenePath unchanged.
        """
    def __eq__(self, other: object) -> bool:
        """
        Equality comparison.
        """
    def __ne__(self, other: object) -> bool: ...

class FlattenResolveAssetPathContext(Boost.Python.instance):
    """
    Context object containing information used when resolving asset paths
    during layer stack flattening.
    """
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """
    @property
    def assetPath(self): ...
    @property
    def expressionVariables(self): ...
    @property
    def sourceLayer(self): ...

class Inherits(Boost.Python.instance):
    """
    A proxy class for applying listOp edits to the inherit paths list for
    a prim.


    All paths passed to the UsdInherits API are expected to be in the
    namespace of the owning prim's stage. Subroot prim inherit paths will
    be translated from this namespace to the namespace of the current edit
    target, if necessary. If a path cannot be translated, a coding error
    will be issued and no changes will be made. Root prim inherit paths
    will not be translated.
    """
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """
    def AddInherit(self, primPath: pxr.Sdf.Path | str, position: ListPosition = ...) -> bool:
        """
        Adds a path to the inheritPaths listOp at the current EditTarget, in
        the position specified by C{position}.
        """
    def ClearInherits(self) -> bool:
        """
        Removes the authored inheritPaths listOp edits at the current edit
        target.
        """
    def GetAllDirectInherits(self) -> list[pxr.Sdf.Path]:
        """
        Return all the paths in this prim's stage's local layer stack that
        would compose into this prim via direct inherits (excluding prim specs
        that would be composed into this prim due to inherits authored on
        ancestral prims) in strong-to-weak order.


        Note that there currently may not be any scene description at these
        paths on the stage. This returns all the potential places that such
        opinions could appear.
        """
    def GetPrim(self) -> Prim:
        """
        Return the prim this object is bound to.
        """
    def RemoveInherit(self, primPath: pxr.Sdf.Path | str) -> bool:
        """
        Removes the specified path from the inheritPaths listOp at the current
        EditTarget.
        """
    def SetInherits(self, _items: typing.Iterable[pxr.Sdf.Path | str], /) -> bool:
        """
        Explicitly set the inherited paths, potentially blocking weaker
        opinions that add or remove items, returning true on success, false if
        the edit could not be performed.
        """
    def __bool__(self) -> bool: ...

class InterpolationType(pxr.Tf.Tf_PyEnumWrapper):
    _baseName: ClassVar[str] = ...
    allValues: ClassVar[tuple] = ...
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def GetValueFromName(name: object) -> Any: ...

class ListPosition(pxr.Tf.Tf_PyEnumWrapper):
    _baseName: ClassVar[str] = ...
    allValues: ClassVar[tuple] = ...
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def GetValueFromName(name: object) -> Any: ...

class LoadPolicy(pxr.Tf.Tf_PyEnumWrapper):
    _baseName: ClassVar[str] = ...
    allValues: ClassVar[tuple] = ...
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def GetValueFromName(name: object) -> Any: ...

class ModelAPI(APISchemaBase):
    """
    UsdModelAPI is an API schema that provides an interface to a prim's
    model qualities, if it does, in fact, represent the root prim of a
    model.


    The first and foremost model quality is its *kind*, i.e. the metadata
    that establishes it as a model (See KindRegistry). UsdModelAPI
    provides various methods for setting and querying the prim's kind, as
    well as queries (also available on UsdPrim) for asking what category
    of model the prim is. See Kind and Model-ness.

    UsdModelAPI also provides access to a prim's assetInfo data. While any
    prim *can* host assetInfo, it is common that published (referenced)
    assets are packaged as models, therefore it is convenient to provide
    access to the one from the other.
    """

    class KindValidation(pxr.Tf.Tf_PyEnumWrapper):
        _baseName: ClassVar[str] = ...
        allValues: ClassVar[tuple] = ...
        def __init__(self, *args, **kwargs) -> None:
            """Raises an exception
            This class cannot be instantiated from Python
            """
        @staticmethod
        def GetValueFromName(name: object) -> Any: ...
    KindValidationModelHierarchy: ClassVar[ModelAPI.KindValidation] = ...
    KindValidationNone: ClassVar[ModelAPI.KindValidation] = ...
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, prim: Prim) -> None:
        """
        Construct a UsdModelAPI on UsdPrim C{prim}.


        Equivalent to UsdModelAPI::Get (prim.GetStage(), prim.GetPath()) for a
        *valid* C{prim}, but will not immediately throw an error for an
        invalid C{prim}
        """
    @overload
    def __init__(self, schemaObj: SchemaBase) -> None:
        """
        Construct a UsdModelAPI on the prim held by C{schemaObj}.


        Should be preferred over UsdModelAPI (schemaObj.GetPrim()), as it
        preserves SchemaBase state.
        """
    @staticmethod
    def Get(stage: Stage, path: pxr.Sdf.Path | str) -> ModelAPI:
        """
        Return a UsdModelAPI holding the prim adhering to this schema at
        C{path} on C{stage}.


        If no prim exists at C{path} on C{stage}, or if the prim at that path
        does not adhere to this schema, return an invalid schema object. This
        is shorthand for the following: ::

          UsdModelAPI(stage->GetPrimAtPath(path));

        """
    def GetAssetIdentifier(self) -> pxr.Sdf.AssetPath:
        """
        Returns the model's asset identifier as authored in the composed
        assetInfo dictionary.


        The asset identifier can be used to resolve the model's root layer via
        the asset resolver plugin.
        """
    def GetAssetInfo(self) -> dict:
        """
        Returns the model's composed assetInfo dictionary.


        The asset info dictionary is used to annotate models with various data
        related to asset management. For example, asset name, identifier,
        version etc.

        The elements of this dictionary are composed element-wise, and are
        nestable.
        """
    def GetAssetName(self) -> str:
        """
        Returns the model's asset name from the composed assetInfo dictionary.


        The asset name is the name of the asset, as would be used in a
        database query.
        """
    def GetAssetVersion(self) -> str:
        """
        Returns the model's resolved asset version.



        If you publish assets with an embedded version, then you may receive
        that version string. You may, however, cause your authoring tools to
        record the resolved version *at the time at which a reference to the
        asset was added to an aggregate*, at the referencing site. In such a
        pipeline, this API will always return that stronger opinion, even if
        the asset is republished with a newer version, and even though that
        newer version may be the one that is resolved when the UsdStage is
        opened.
        """
    def GetKind(self) -> str:
        """
        Retrieve the authored C{kind} for this prim.



        true if there was an authored kind that was successfully read,
        otherwise false.

        UsdPrim::GetKind
        """
    def GetPayloadAssetDependencies(self) -> pxr.Sdf.AssetPathArray:
        """
        Returns the list of asset dependencies referenced inside the payload
        of the model.


        This typically contains identifiers of external assets that are
        referenced inside the model's payload. When the model is created, this
        list is compiled and set at the root of the model. This enables
        efficient dependency analysis without the need to include the model's
        payload.
        """
    @staticmethod
    def GetSchemaAttributeNames(includeInherited: bool = ...) -> list[str]:
        """
        Return a vector of names of all pre-declared attributes for this
        schema class and all its ancestor classes.


        Does not include attributes that may be authored by custom/extended
        methods of the schemas involved.
        """
    def IsGroup(self) -> bool:
        """
        Return true if this prim represents a model group, based on its kind
        metadata.
        """
    def IsKind(self, baseKind: str | pxr.Ar.ResolvedPath, validation: pxr.Kind.Validation = ...) -> bool:
        '''
        Return true if the prim\'s kind metadata is or inherits from
        C{baseKind} as defined by the Kind Registry.


        If C{validation} is KindValidationModelHierarchy (the default), then
        this also ensures that if baseKind is a model, the prim conforms to
        the rules of model hierarchy, as defined by IsModel. If set to
        KindValidationNone, no additional validation is done.

        IsModel and IsGroup are preferrable to IsKind("model") as they are
        optimized for fast traversal.

        If a prim\'s model hierarchy is not valid, it is possible that that
        prim.IsModel() and prim.IsKind("model",
        Usd.ModelAPI.KindValidationNone) return different answers. (As a
        corallary, this is also true for for prim.IsGroup())
        '''
    def IsModel(self) -> bool:
        """
        Return true if this prim represents a model, based on its kind
        metadata.
        """
    def SetAssetIdentifier(self, _identifier: pxr.Sdf.AssetPath | str, /) -> None:
        """
        Sets the model's asset identifier to the given asset path,
        C{identifier}.



        GetAssetIdentifier()
        """
    def SetAssetInfo(self, _info: dict, /) -> None:
        """
        Sets the model's assetInfo dictionary to C{info} in the current edit
        target.
        """
    def SetAssetName(self, _assetName: str | pxr.Ar.ResolvedPath, /) -> None:
        """
        Sets the model's asset name to C{assetName}.



        GetAssetName()
        """
    def SetAssetVersion(self, _version: str | pxr.Ar.ResolvedPath, /) -> None:
        """
        Sets the model's asset version string.



        GetAssetVersion()
        """
    def SetKind(self, value: str | pxr.Ar.ResolvedPath) -> bool:
        """
        Author a C{kind} for this prim, at the current UsdEditTarget.



        true if C{kind} was successully authored, otherwise false.

        UsdPrim::SetKind
        """
    def SetPayloadAssetDependencies(self, _assetDeps: pxr.Sdf.AssetPathArray, /) -> None:
        """
        Sets the list of external asset dependencies referenced inside the
        payload of a model.



        GetPayloadAssetDependencies()
        """
    @staticmethod
    def _GetStaticTfType() -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...

class NamespaceEditor(Boost.Python.instance):
    """

    This code is a work in progress and should not be used in production
    scenarios. It is currently not feature-complete and subject to change.
    Provides namespace editing operations
    """
    def __init__(self, _stage: Stage, /) -> None: ...
    def ApplyEdits(self) -> bool:
        """
        Applies all the added namespace edits stored in this to namespace
        editor to its stage by authoring all scene description in the layer
        stack of the current edit target necessary to move or delete the
        composed objects that the edit paths refer to.


        Returns true if all the necessary edits are successfully performed;
        returns false and emits a coding error otherwise.
        """
    def CanApplyEdits(self) -> _UsdNamespaceEditorCanEditResult:
        """
        Returns whether all the added namespace edits stored in this to
        namespace editor can be applied to its stage.


        In other words, this returns whether ApplyEdits should be successful
        if it were called right now. If this would return false and C{whyNot}
        is provided, the reasons ApplyEdits would fail will be copied to
        whyNot.
        """
    def DeletePrim(self, _prim: Prim, /) -> bool:
        """
        Adds an edit operation to delete the composed prim at the path of
        C{prim} from this namespace editor's stage.


        This is equivalent to calling DeletePrimAtPath(prim.GetPath())

        Returns true if the prim provides a valid possible composed prim path;
        returns false and emits a coding error if not.
        """
    def DeletePrimAtPath(self, _path: pxr.Sdf.Path | str, /) -> bool:
        """
        Adds an edit operation to delete the composed prim at the given
        C{path} from this namespace editor's stage.


        Returns true if the path is a valid possible composed prim path;
        returns false and emits a coding error if not.
        """
    def DeleteProperty(self, _property: Property | pxr.UsdGeom.XformOp, /) -> bool:
        """
        Adds an edit operation to delete the composed property at the path of
        C{property} from this namespace editor's stage.


        This is equivalent to calling DeletePropertyAtPath(property.GetPath())

        Returns true if the property provides a valid possible composed
        property path; returns false and emits a coding error if not.
        """
    def DeletePropertyAtPath(self, _path: pxr.Sdf.Path | str, /) -> bool:
        """
        Adds an edit operation to delete the composed property at the given
        C{path} from this namespace editor's stage.


        Returns true if the path is a valid possible composed property path;
        returns false and emits a coding error if not.
        """
    def MovePrimAtPath(self, _path: pxr.Sdf.Path | str, _newPath: pxr.Sdf.Path | str, /) -> bool:
        """
        Adds an edit operation to move the composed prim at the given C{path}
        on this namespace editor's stage to instead be at the path C{newPath}.



        Returns true if both paths are valid possible composed prim path;
        returns false and emits a coding error if not.
        """
    def MovePropertyAtPath(self, _path: pxr.Sdf.Path | str, _newPath: pxr.Sdf.Path | str, /) -> bool:
        """
        Adds an edit operation to move the composed property at the given
        C{path} on this namespace editor's stage to instead be at the path
        C{newPath}.


        Returns true if both paths are valid possible composed property path;
        returns false and emits a coding error if not.
        """
    def RenamePrim(self, _prim: Prim, _newName: str | pxr.Ar.ResolvedPath, /) -> bool:
        """
        Adds an edit operation to rename the composed prim at the path of
        C{prim} on this namespace editor's stage to instead have the name
        C{newName}.


        Returns true if the prim provides a valid possible composed prim path
        and the new name is a valid possible prim name; returns false and
        emits a coding error if not.
        """
    def RenameProperty(self, _property: Property | pxr.UsdGeom.XformOp, _newName: str | pxr.Ar.ResolvedPath, /) -> bool:
        """
        Adds an edit operation to rename the composed property at the path of
        C{property} on this namespace editor's stage to instead have the name
        C{newName}.


        Returns true if the property provides a valid possible composed
        property path and the new name is a valid possible property name;
        returns false and emits a coding error if not.
        """
    @overload
    def ReparentPrim(self, _prim: Prim, _newParent: Prim, /) -> bool:
        """
        Adds an edit operation to reparent the composed prim at the path of
        C{prim} on this namespace editor's stage to instead be a namespace
        child of the composed prim at the path of C{newParent}.


        Returns true if the both the prim and the new parent prim provide a
        valid possible composed prim paths; returns false and emits a coding
        error if not.
        """
    @overload
    def ReparentPrim(self, _prim: Prim, _newParent: Prim, _newName: str | pxr.Ar.ResolvedPath, /) -> bool:
        """
        Adds an edit operation to reparent the composed prim at the path of
        C{prim} on this namespace editor's stage to instead be a prim named
        C{newName} that is a namespace child of the composed prim at the  path
        of C{newParent}.


        Returns true if the both the prim and the new parent prim provide a
        valid possible composed prim paths and the new name is a valid prim
        name; returns false and emits a coding error if not.
        """
    @overload
    def ReparentProperty(self, _property: Property | pxr.UsdGeom.XformOp, _newParent: Prim, /) -> bool:
        """
        Adds an edit operation to reparent the composed property at the path
        of C{property} on this namespace editor's stage to instead be a
        namespace child of the composed property at the path of C{newParent}.


        Returns true if the both the property and the new parent prim provide
        a valid possible composed paths; returns false and emits a coding
        error if not.
        """
    @overload
    def ReparentProperty(self, _property: Property | pxr.UsdGeom.XformOp, _newParent: Prim, _newName: str | pxr.Ar.ResolvedPath, /) -> bool:
        """
        Adds an edit operation to reparent the composed property at the path
        of C{property} on this namespace editor's stage to instead be a
        property named C{newName} that is a namespace child of the composed
        prim at the path of C{newParent}.


        Returns true if the both the property and the new parent prim provide
        a valid possible composed paths and the new name is a valid property
        name; returns false and emits a coding error if not.
        """

class Notice(Boost.Python.instance):
    class LayerMutingChanged(Notice.StageNotice):
        """
        Notice sent after a set of layers have been newly muted or unmuted.


        Note this does not necessarily mean the specified layers are currently
        loaded.

        LayerMutingChanged notice is sent before any UsdNotice::ObjectsChanged
        or UsdNotice::StageContentsChanged notices are sent resulting from
        muting or unmuting of layers.

        Note that LayerMutingChanged notice is sent even if the
        muting/unmuting layer does not belong to the current stage, or is a
        layer that does belong to the current stage but is not yet loaded
        because it is behind an unloaded payload or unselected variant.
        """
        def __init__(self, *args, **kwargs) -> None:
            """Raises an exception
            This class cannot be instantiated from Python
            """
        def GetMutedLayers(self) -> list[str]:
            """
            Returns the identifier of the layers that were muted.


            The stage's resolver context must be bound when looking up layers
            using the returned identifiers to ensure the same layers that would be
            used by the stage are found.
            """
        def GetUnmutedLayers(self) -> list[str]:
            """
            Returns the identifier of the layers that were unmuted.


            The stage's resolver context must be bound when looking up layers
            using the returned identifiers to ensure the same layers that would be
            used by the stage are found.
            """

    class ObjectsChanged(Notice.StageNotice):
        '''
        Notice sent in response to authored changes that affect UsdObjects.


        The kinds of object changes are divided into these categories:

           - Object resync:

        "Resyncs"are potentially structural changes that invalidate entire
        subtrees of UsdObjects (including prims and properties). For example,
        if the path"/foo"is resynced, then all subpaths
        like"/foo/bar"and"/foo/bar.baz"may be arbitrarily changed.

        When a prim is resynced, say"/foo/bar", it might have been created or
        destroyed. Indication of possible changes flows down the resynced prim
        namespace, implicitly via prim resync notices. We *do not* consider
        the parent"/foo"to be resynced, as this would incorrectly imply that
        some or all of"/foo/bar"\'s siblings (and their descendants) have also
        changed. Additionally, we do not propagate change indication to
        objects associated with the changed object through relationships or
        connections.

           - Resolved asset path resync:

        "Resolved asset path resyncs"invalidate asset paths in a subtree of
        objects. Asset paths authored anywhere in this subtree of objects
        (e.g. as attribute or metadata values) may now resolve to different
        locations, even though the asset path authored in scene description
        has not changed.

           - Changed info:

        "Changed-info"means that a nonstructural change has occurred, like an
        attribute value change or a value change to a metadata field not
        related to composition. Unlike resyncs, changed-info notices for an
        object do not imply that the subtree beneath that object have changed.

        This notice provides API for two client use-cases. Clients interested
        in testing whether specific objects are affected by the changes should
        use the methods that return a bool, like AffectedObject() . Clients
        that wish to reason about all changes as a whole should use the
        methods that return a PathRange, like GetResyncedPaths() .
        '''
        def __init__(self, *args, **kwargs) -> None:
            """Raises an exception
            This class cannot be instantiated from Python
            """
        def AffectedObject(self, _obj: Object | pxr.UsdGeom.XformOp, /) -> bool:
            """
            Return true if C{obj} was possibly affected by the layer changes that
            generated this notice.


            This is the case if either the object is subject to a resync or has
            changed info. Equivalent to: ::

              ResyncedObject(obj) || ResolvedAssetPathsResynced(obj) || ChangedInfoOnly(obj)

            """
        def ChangedInfoOnly(self, _obj: Object | pxr.UsdGeom.XformOp, /) -> bool:
            """
            Return true if C{obj} was changed but not resynced by the layer
            changes that generated this notice.


            This is the case if this object's exact path is present in
            GetChangedInfoOnlyPaths() .
            """
        @overload
        def GetChangedFields(self, _obj: Object | pxr.UsdGeom.XformOp, /) -> list[str]:
            """
            Return the set of changed fields in layers that affected C{obj}.


            This set will be empty for objects whose paths are not in
            GetResyncedPaths() or GetChangedInfoOnlyPaths() .

            If a field is present in this set, it does not necessarily mean the
            composed value of that field on C{obj} has changed. For example, if a
            metadata value on C{obj} is overridden in a stronger layer and is
            changed in a weaker layer, that field will appear in this set.
            However, since the value in the stronger layer did not change, the
            composed value returned by GetMetadata() will not have changed.
            """
        @overload
        def GetChangedFields(self, _path: pxr.Sdf.Path | str, /) -> list[str]:
            """
            This is an overloaded member function, provided for convenience. It
            differs from the above function only in what argument(s) it accepts.
            """
        def GetChangedInfoOnlyPaths(self) -> PathRange:
            '''
            Return the set of paths that have only info changes (those that do not
            affect the structure of cached UsdPrims on a UsdStage) in
            lexicographical order.


            Info changes do not imply entire subtree invalidation, so this set is
            not minimal regarding ancestors and descendants, as opposed to
            GetResyncedPaths() . For example, both the paths\'/foo\'and\'/foo/bar\'may
            appear in this set.

            The"only"in"changed info only paths"was historically meant to
            distinguish these paths from the object resync paths returned by
            GetResyncedPaths, since the former is subsumed by the latter. It is
            now slightly misleading; paths in"changed info only"are still subsumed
            by"object resync"paths, but are *not* subsumed by other types of
            changes, like"resolved asset path resyncs".
            '''
        def GetResolvedAssetPathsResyncedPaths(self) -> PathRange:
            """
            Return the set of paths affected by changes that may cause asset path
            values to resolve to different locations, even though the asset path
            authored in scene description has not changed.


            For example, asset paths using expression variables may be invalidated
            when a variable value is modified, even though the authored asset
            paths have not changed. The set of paths are returned in
            lexicographical order.

            Resolved asset path resyncs imply invalidation of asset paths within
            entire subtrees including all descendant prims and properties, so this
            set is minimal regarding ancestors and descendants. For example, if
            the path'/foo'appears in this set, all asset paths in the entire
            subtree at'/foo'are invalidated, so the path'/foo/bar'will not appear,
            but asset paths on that prim should be considered invalidated.
            """
        def GetResyncedPaths(self) -> PathRange:
            """
            Return the set of paths that are resynced in lexicographical order.


            Resyncs imply entire subtree invalidation of all descendant prims and
            properties, so this set is minimal regarding ancestors and
            descendants. For example, if the path'/foo'appears in this set, the
            entire subtree at'/foo'is resynced so the path'/foo/bar'will not
            appear, but it should be considered resynced.

            Since object resyncs fully invalidate entire subtrees, this set of
            paths subsumes all other paths. For example, if the path'/foo'appears
            in this set, but an attribute value was changed at'/foo/bar.x', this
            notice will only contain'/foo'in the set returned by this path and
            empty sets from all other functions. This is because the change
            to'/foo/bar.x'is implied by the resync of'/foo'.
            """
        @overload
        def HasChangedFields(self, _obj: Object | pxr.UsdGeom.XformOp, /) -> bool:
            """
            Return true if there are any changed fields that affected C{obj},
            false otherwise.


            See GetChangedFields for more details.
            """
        @overload
        def HasChangedFields(self, _path: pxr.Sdf.Path | str, /) -> bool:
            """
            This is an overloaded member function, provided for convenience. It
            differs from the above function only in what argument(s) it accepts.
            """
        def ResolvedAssetPathsResynced(self, _obj: Object | pxr.UsdGeom.XformOp, /) -> bool:
            """
            Return true if asset path values in C{obj} were resynced by the layer
            changes that generated this notice.


            This is the case if the object's path or an ancestor path is present
            in GetResolvedAssetPathsResyncedPaths() .
            """
        def ResyncedObject(self, _obj: Object | pxr.UsdGeom.XformOp, /) -> bool:
            """
            Return true if C{obj} was resynced by the layer changes that generated
            this notice.


            This is the case if the object's path or an ancestor path is present
            in GetResyncedPaths() .
            """

    class StageContentsChanged(Notice.StageNotice):
        def __init__(self, *args, **kwargs) -> None:
            """Raises an exception
            This class cannot be instantiated from Python
            """

    class StageEditTargetChanged(Notice.StageNotice):
        def __init__(self, *args, **kwargs) -> None:
            """Raises an exception
            This class cannot be instantiated from Python
            """

    class StageNotice(pxr.Tf.Notice):
        """
        Base class for UsdStage notices.
        """
        def __init__(self, *args, **kwargs) -> None:
            """Raises an exception
            This class cannot be instantiated from Python
            """
        def GetStage(self) -> Stage:
            """
            Return the stage associated with this notice.
            """
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """

class Object(Boost.Python.instance):
    """
    Base class for Usd scenegraph objects, providing common API.


    The commonality between the three types of scenegraph objects in Usd (
    UsdPrim, UsdAttribute, UsdRelationship) is that they can all have
    metadata. Other objects in the API ( UsdReferences, UsdVariantSets,
    etc.) simply *are* kinds of metadata.

    UsdObject 's API primarily provides schema for interacting with the
    metadata common to all the scenegraph objects, as well as generic
    access to metadata.

    section Usd_UsdObject_Lifetime Lifetime Management and Object Validity

    Every derived class of UsdObject supports explicit detection of object
    validity through an *explicit-bool* operator, so client code should
    always be able use objects safely, even across edits to the owning
    UsdStage. UsdObject classes also perform some level of validity
    checking upon every use, in order to facilitate debugging of unsafe
    code, although we reserve the right to activate that behavior only in
    debug builds, if it becomes compelling to do so for performance
    reasons. This per-use checking will cause a fatal error upon failing
    the inline validity check, with an error message describing the
    namespace location of the dereferenced object on its owning UsdStage.
    """
    __instance_size__: ClassVar[int] = ...
    def __init__(self) -> None:
        """
        Default constructor produces an invalid object.
        """
    def ClearAssetInfo(self) -> None:
        """
        Clear the authored opinion for this object's assetInfo dictionary at
        the current EditTarget.


        Do nothing if there is no such authored opinion.
        """
    def ClearAssetInfoByKey(self, keyPath: str | pxr.Ar.ResolvedPath) -> None:
        """
        Clear the authored opinion identified by C{keyPath} in this object's
        assetInfo dictionary at the current EditTarget.


        The C{keyPath} is a':'-separated path identifying a value in
        subdictionaries. Do nothing if there is no such authored opinion.
        """
    def ClearCustomData(self) -> None:
        """
        Clear the authored opinion for this object's customData dictionary at
        the current EditTarget.


        Do nothing if there is no such authored opinion.
        """
    def ClearCustomDataByKey(self, keyPath: str | pxr.Ar.ResolvedPath) -> None:
        """
        Clear the authored opinion identified by C{keyPath} in this object's
        customData dictionary at the current EditTarget.


        The C{keyPath} is a':'-separated path identifying a value in
        subdictionaries. Do nothing if there is no such authored opinion.
        """
    def ClearDisplayName(self) -> bool:
        """
        Clears this object's display name (metadata) in the current EditTarget
        (only).


        Returns true on success.
        """
    def ClearDocumentation(self) -> bool:
        """
        Clears this object's documentation (metadata) in the current
        EditTarget (only).


        Returns true on success.
        """
    def ClearHidden(self) -> bool:
        '''
        Clears the opinion for"Hidden"at the current EditTarget.
        '''
    def ClearMetadata(self, key: str | pxr.Ar.ResolvedPath) -> bool:
        """
        Clears the authored *key's* value at the current EditTarget, returning
        false on error.


        If no value is present, this method is a no-op and returns true. It is
        considered an error to call ClearMetadata when no spec is present for
        this UsdObject, i.e. if the object has no presence in the current
        UsdEditTarget.

        General Metadata in USD
        """
    def ClearMetadataByDictKey(self, key: str | pxr.Ar.ResolvedPath, keyPath: str | pxr.Ar.ResolvedPath) -> bool:
        """
        Clear any authored value identified by C{key} and C{keyPath} at the
        current EditTarget.


        The C{keyPath} is a':'-separated path identifying a path in
        subdictionaries stored in the metadata field at C{key}. Return true if
        the value is cleared successfully, false otherwise.

        Dictionary-valued Metadata
        """
    def GetAllAuthoredMetadata(self) -> dict:
        """
        Resolve and return all user-authored metadata on this object, sorted
        lexicographically.



        This method does not return field keys for composition arcs, such as
        references, inherits, payloads, sublayers, variants, or primChildren,
        nor does it return the default value or timeSamples.
        """
    def GetAllMetadata(self) -> dict:
        """
        Resolve and return all metadata (including both authored and fallback
        values) on this object, sorted lexicographically.



        This method does not return field keys for composition arcs, such as
        references, inherits, payloads, sublayers, variants, or primChildren,
        nor does it return the default value or timeSamples.
        """
    def GetAssetInfo(self) -> dict:
        """
        Return this object's composed assetInfo dictionary.


        The asset info dictionary is used to annotate objects representing the
        root-prims of assets (generally organized as models) with various data
        related to asset management. For example, asset name, root layer
        identifier, asset version etc.

        The elements of this dictionary are composed element-wise, and are
        nestable.

        There is no means to query an assetInfo field's valuetype other than
        fetching the value and interrogating it.

        GetAssetInfoByKey()
        """
    def GetAssetInfoByKey(self, keyPath: str | pxr.Ar.ResolvedPath) -> Any:
        """
        Return the element identified by C{keyPath} in this object's composed
        assetInfo dictionary.


        The C{keyPath} is a':'-separated path identifying a value in
        subdictionaries. This is in general more efficient than composing the
        entire assetInfo dictionary than pulling out one sub-element.
        """
    def GetCustomData(self) -> dict:
        '''
        Return this object\'s composed customData dictionary.


        CustomData is"custom metadata", a place for applications and users to
        put uniform data that is entirely dynamic and subject to no schema
        known to Usd. Unlike metadata like\'hidden\',\'displayName\'etc, which
        must be declared in code or a data file that is considered part of
        one\'s Usd distribution (e.g. a plugInfo.json file) to be used,
        customData keys and the datatypes of their corresponding values are ad
        hoc. No validation will ever be performed that values for the same key
        in different layers are of the same type - strongest simply wins.

        Dictionaries like customData are composed element-wise, and are
        nestable.

        There is no means to query a customData field\'s valuetype other than
        fetching the value and interrogating it.

        GetCustomDataByKey()
        '''
    def GetCustomDataByKey(self, keyPath: str | pxr.Ar.ResolvedPath) -> Any:
        """
        Return the element identified by C{keyPath} in this object's composed
        customData dictionary.


        The C{keyPath} is a':'-separated path identifying a value in
        subdictionaries. This is in general more efficient than composing the
        entire customData dictionary and then pulling out one sub-element.
        """
    def GetDescription(self) -> str:
        """
        Return a string that provides a brief summary description of the
        object.


        This method, along with IsValid() /bool_operator, is always safe to
        call on a possibly-expired object, and the description will specify
        whether the object is valid or expired, along with a few other bits of
        data.
        """
    def GetDisplayName(self) -> str:
        """
        Return this object's display name (metadata).


        This returns the empty string if no display name has been set.

        SetDisplayName()
        """
    def GetDocumentation(self) -> str:
        """
        Return this object's documentation (metadata).


        This returns the empty string if no documentation has been set.

        SetDocumentation()
        """
    def GetMetadata(self, key: str | pxr.Ar.ResolvedPath) -> Any:
        """
        Resolve the requested metadatum named C{key} into C{value}, returning
        true on success.



        false if C{key} was not resolvable, or if C{value's} type C{T}
        differed from that of the resolved metadatum.

        For any composition-related metadata, as enumerated in
        GetAllMetadata() , this method will return only the strongest opinion
        found, not applying the composition rules used by Pcp to process the
        data. For more processed/composed views of composition data, please
        refer to the specific interface classes, such as UsdReferences,
        UsdInherits, UsdVariantSets, etc.

        General Metadata in USD
        """
    def GetMetadataByDictKey(self, key: str | pxr.Ar.ResolvedPath, keyPath: str | pxr.Ar.ResolvedPath) -> Any:
        """
        Resolve the requested dictionary sub-element C{keyPath} of dictionary-
        valued metadatum named C{key} into C{value}, returning true on
        success.


        If you know you neeed just a small number of elements from a
        dictionary, accessing them element-wise using this method can be much
        less expensive than fetching the entire dictionary with
        GetMetadata(key).

        false if C{key} was not resolvable, or if C{value's} type C{T}
        differed from that of the resolved metadatum. The C{keyPath} is
        a':'-separated path addressing an element in subdictionaries.

        Dictionary-valued Metadata
        """
    def GetName(self) -> str:
        """
        Return the full name of this object, i.e.


        the last component of its SdfPath in namespace.

        This is equivalent to, but generally cheaper than, GetPath()
        .GetNameToken()
        """
    @staticmethod
    def GetNamespaceDelimiter() -> str: ...
    def GetPath(self) -> pxr.Sdf.Path:
        """
        Return the complete scene path to this object on its UsdStage, which
        may (UsdPrim) or may not (all other subclasses) return a cached
        result.
        """
    def GetPrim(self) -> Prim:
        """
        Return this object if it is a prim, otherwise return this object's
        nearest owning prim.
        """
    def GetPrimPath(self) -> pxr.Sdf.Path:
        """
        Return this object's path if this object is a prim, otherwise this
        object's nearest owning prim's path.


        Equivalent to GetPrim() . GetPath() .
        """
    def GetStage(self) -> Stage:
        """
        Return the stage that owns the object, and to whose state and lifetime
        this object's validity is tied.
        """
    def HasAssetInfo(self) -> bool:
        """
        Return true if there are any authored or fallback opinions for this
        object's assetInfo dictionary, false otherwise.
        """
    def HasAssetInfoKey(self, keyPath: str | pxr.Ar.ResolvedPath) -> bool:
        """
        Return true if there are any authored or fallback opinions for the
        element identified by C{keyPath} in this object's assetInfo
        dictionary, false otherwise.


        The C{keyPath} is a':'-separated path identifying a value in
        subdictionaries.
        """
    def HasAuthoredAssetInfo(self) -> bool:
        """
        Return true if there are any authored opinions (excluding fallback)
        for this object's assetInfo dictionary, false otherwise.
        """
    def HasAuthoredAssetInfoKey(self, keyPath: str | pxr.Ar.ResolvedPath) -> bool:
        """
        Return true if there are any authored opinions (excluding fallback)
        for the element identified by C{keyPath} in this object's assetInfo
        dictionary, false otherwise.


        The C{keyPath} is a':'-separated path identifying a value in
        subdictionaries.
        """
    def HasAuthoredCustomData(self) -> bool:
        """
        Return true if there are any authored opinions (excluding fallback)
        for this object's customData dictionary, false otherwise.
        """
    def HasAuthoredCustomDataKey(self, keyPath: str | pxr.Ar.ResolvedPath) -> bool:
        """
        Return true if there are any authored opinions (excluding fallback)
        for the element identified by C{keyPath} in this object's customData
        dictionary, false otherwise.


        The C{keyPath} is a':'-separated path identifying a value in
        subdictionaries.
        """
    def HasAuthoredDisplayName(self) -> bool:
        """
        Returns true if displayName was explicitly authored and GetMetadata()
        will return a meaningful value for displayName.


        """
    def HasAuthoredDocumentation(self) -> bool:
        """
        Returns true if documentation was explicitly authored and
        GetMetadata() will return a meaningful value for documentation.


        """
    def HasAuthoredHidden(self) -> bool:
        """
        Returns true if hidden was explicitly authored and GetMetadata() will
        return a meaningful value for Hidden.


        Note that IsHidden returns a fallback value (false) when hidden is not
        authored.
        """
    def HasAuthoredMetadata(self, key: str | pxr.Ar.ResolvedPath) -> bool:
        """
        Returns true if the *key* has an authored value, false if no value was
        authored or the only value available is a prim's metadata fallback.
        """
    def HasAuthoredMetadataDictKey(self, key: str | pxr.Ar.ResolvedPath, keyPath: str | pxr.Ar.ResolvedPath) -> bool:
        """
        Return true if there exists any authored opinion (excluding fallbacks)
        for C{key} and C{keyPath}.


        The C{keyPath} is a':'-separated path identifying a value in
        subdictionaries stored in the metadata field at C{key}.

        Dictionary-valued Metadata
        """
    def HasCustomData(self) -> bool:
        """
        Return true if there are any authored or fallback opinions for this
        object's customData dictionary, false otherwise.
        """
    def HasCustomDataKey(self, keyPath: str | pxr.Ar.ResolvedPath) -> bool:
        """
        Return true if there are any authored or fallback opinions for the
        element identified by C{keyPath} in this object's customData
        dictionary, false otherwise.


        The C{keyPath} is a':'-separated path identifying a value in
        subdictionaries.
        """
    def HasMetadata(self, key: str | pxr.Ar.ResolvedPath) -> bool:
        """
        Returns true if the *key* has a meaningful value, that is, if
        GetMetadata() will provide a value, either because it was authored or
        because a prim's metadata fallback will be provided.
        """
    def HasMetadataDictKey(self, key: str | pxr.Ar.ResolvedPath, keyPath: str | pxr.Ar.ResolvedPath) -> bool:
        """
        Return true if there exists any authored or fallback opinion for
        C{key} and C{keyPath}.


        The C{keyPath} is a':'-separated path identifying a value in
        subdictionaries stored in the metadata field at C{key}.

        Dictionary-valued Metadata
        """
    def IsHidden(self) -> bool:
        '''
        Gets the value of the\'hidden\'metadata field, false if not authored.


        When an object is marked as hidden, it is an indicator to clients who
        generically display objects (such as GUI widgets) that this object
        should not be included, unless explicitly asked for. Although this is
        just a hint and thus up to each application to interpret, we use it
        primarily as a way of simplifying hierarchy displays, by hiding *only*
        the representation of the object itself, *not* its subtree,
        instead"pulling up"everything below it one level in the hierarchical
        nesting.

        Note again that this is a hint for UI only - it should not be
        interpreted by any renderer as making a prim invisible to drawing.
        '''
    def IsValid(self) -> bool:
        """
        Return true if this is a valid object, false otherwise.
        """
    def SetAssetInfo(self, assetInfo: dict) -> None:
        """
        Author this object's assetInfo dictionary to C{assetInfo} at the
        current EditTarget.
        """
    def SetAssetInfoByKey(self, keyPath: str | pxr.Ar.ResolvedPath, value: Any) -> None:
        """
        Author the element identified by C{keyPath} in this object's assetInfo
        dictionary at the current EditTarget.


        The C{keyPath} is a':'-separated path identifying a value in
        subdictionaries.
        """
    def SetCustomData(self, customData: dict) -> None:
        """
        Author this object's customData dictionary to C{customData} at the
        current EditTarget.
        """
    def SetCustomDataByKey(self, keyPath: str | pxr.Ar.ResolvedPath, value: Any) -> None:
        """
        Author the element identified by C{keyPath} in this object's
        customData dictionary at the current EditTarget.


        The C{keyPath} is a':'-separated path identifying a value in
        subdictionaries.
        """
    def SetDisplayName(self, name: str | pxr.Ar.ResolvedPath) -> bool:
        """
        Sets this object's display name (metadata).


        Returns true on success.

        DisplayName is meant to be a descriptive label, not necessarily an
        alternate identifier; therefore there is no restriction on which
        characters can appear in it.
        """
    def SetDocumentation(self, doc: str | pxr.Ar.ResolvedPath) -> bool:
        """
        Sets this object's documentation (metadata). Returns true on success.
        """
    def SetHidden(self, hidden: bool) -> bool:
        """
        Sets the value of the'hidden'metadata field.


        See IsHidden() for details.
        """
    def SetMetadata(self, key: str | pxr.Ar.ResolvedPath, value: Any) -> bool:
        """
        Set metadatum C{key's} value to C{value}.



        false if C{value's} type does not match the schema type for C{key}.

        General Metadata in USD
        """
    def SetMetadataByDictKey(self, key: str | pxr.Ar.ResolvedPath, keyPath: str | pxr.Ar.ResolvedPath, value: Any) -> bool:
        """
        Author C{value} to the field identified by C{key} and C{keyPath} at
        the current EditTarget.


        The C{keyPath} is a':'-separated path identifying a value in
        subdictionaries stored in the metadata field at C{key}. Return true if
        the value is authored successfully, false otherwise.

        Dictionary-valued Metadata
        """
    def __bool__(self) -> bool:
        """
        Returns C{true} if this object is valid, C{false} otherwise.
        """
    def __eq__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...

class Payloads(Boost.Python.instance):
    """
    UsdPayloads provides an interface to authoring and introspecting
    payloads.


    Payloads behave the same as Usd references except that payloads can be
    optionally loaded.
    """
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """
    def AddInternalPayload(self, primPath: pxr.Sdf.Path | str, layerOffset: pxr.Sdf.LayerOffset = ..., position: ListPosition = ...) -> bool:
        """
        Add an internal payload to the specified prim.



        Internal Payloads
        """
    @overload
    def AddPayload(self, payload: pxr.Sdf.Payload, position: ListPosition = ...) -> bool:
        """
        Adds a payload to the payload listOp at the current EditTarget, in the
        position specified by C{position}.



        Why adding references may fail for explanation of expectations on
        C{payload} and what return values and errors to expect, and ListOps
        and List Editing for details on list editing and composition of
        listOps.
        """
    @overload
    def AddPayload(self, assetPath: str | pxr.Ar.ResolvedPath, primPath: pxr.Sdf.Path | str, layerOffset: pxr.Sdf.LayerOffset = ..., position: ListPosition = ...) -> bool:
        """
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        """
    @overload
    def AddPayload(self, assetPath: str | pxr.Ar.ResolvedPath, layerOffset: pxr.Sdf.LayerOffset = ..., position: ListPosition = ...) -> bool:
        """
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.



        Payloads Without Prim Paths
        """
    def ClearPayloads(self) -> bool:
        '''
        Removes the authored payload listOp edits at the current EditTarget.


        The same caveats for Remove() apply to Clear(). In fact, Clear() may
        actually increase the number of composed payloads, if the listOp being
        cleared contained the"remove"operator.

        ListOps and List Editing
        '''
    def GetPrim(self) -> Prim:
        """
        Return the prim this object is bound to.
        """
    def RemovePayload(self, payload: pxr.Sdf.Payload) -> bool:
        """
        Removes the specified payload from the payloads listOp at the current
        EditTarget.


        This does not necessarily eliminate the payload completely, as it may
        be added or set in another layer in the same LayerStack as the current
        EditTarget.

        ListOps and List Editing
        """
    def SetPayloads(self, _items: list[pxr.Sdf.Payload], /) -> bool:
        """
        Explicitly set the payloads, potentially blocking weaker opinions that
        add or remove items.



        Why adding payloads may fail for explanation of expectations on
        C{items} and what return values and errors to expect, and ListOps and
        List Editing for details on list editing and composition of listOps.
        """
    def __bool__(self) -> bool: ...

class Prim(Object):
    '''
    UsdPrim is the sole persistent scenegraph object on a UsdStage, and is
    the embodiment of a"Prim"as described in the *Universal Scene
    Description Composition Compendium*


    A UsdPrim is the principal container of other types of scene
    description. It provides API for accessing and creating all of the
    contained kinds of scene description, which include:
       - UsdVariantSets - all VariantSets on the prim ( GetVariantSets() ,
         GetVariantSet() )

       - UsdReferences - all references on the prim ( GetReferences() )

       - UsdInherits - all inherits on the prim ( GetInherits() )

       - UsdSpecializes - all specializes on the prim ( GetSpecializes() )
         As well as access to the API objects for properties contained within
         the prim - UsdPrim as well as all of the following classes are
         subclasses of UsdObject :
       - UsdProperty - generic access to all attributes and relationships.
         A UsdProperty can be queried and cast to a UsdAttribute or
         UsdRelationship using UsdObject::Is<>() and UsdObject::As<>() . (
         GetPropertyNames() , GetProperties() , GetPropertiesInNamespace() ,
         GetPropertyOrder() , SetPropertyOrder() )

       - UsdAttribute - access to default and timesampled attribute
         values, as well as value resolution information, and attribute-
         specific metadata ( CreateAttribute() , GetAttribute() ,
         GetAttributes() , HasAttribute() )

       - UsdRelationship - access to authoring and resolving relationships
         to other prims and properties ( CreateRelationship() ,
         GetRelationship() , GetRelationships() , HasRelationship() )
         UsdPrim also provides access to iteration through its prim children,
         optionally making use of the prim predicates facility ( GetChildren()
         , GetAllChildren() , GetFilteredChildren() ).

    Management
    ==========

    Clients acquire UsdPrim objects, which act like weak/guarded pointers
    to persistent objects owned and managed by their originating UsdStage.
    We provide the following guarantees for a UsdPrim acquired via
    UsdStage::GetPrimAtPath() or UsdStage::OverridePrim() or
    UsdStage::DefinePrim() :
       - As long as no further mutations to the structure of the UsdStage
         are made, the UsdPrim will still be valid. Loading and Unloading are
         considered structural mutations.

       - When the UsdStage \'s structure *is* mutated, the thread
         performing the mutation will receive a UsdNotice::ObjectsChanged
         notice after the stage has been reconfigured, which provides details
         as to what prims may have been created or destroyed, and what prims
         may simply have changed in some structural way.
         Prim access in"reader"threads should be limited to GetPrimAtPath() ,
         which will never cause a mutation to the Stage or its layers.

    Please refer to UsdNotice for a listing of the events that could cause
    UsdNotice::ObjectsChanged to be emitted.
    '''
    __instance_size__: ClassVar[int] = ...
    def __init__(self) -> None:
        """
        Construct an invalid prim.
        """
    def AddAppliedSchema(self, _appliedSchemaName: str | pxr.Ar.ResolvedPath, /) -> bool:
        """
        Adds the applied API schema name token C{appliedSchemaName} to the
        *apiSchemas* metadata for this prim at the current edit target.


        For multiple-apply schemas the name token should include the instance
        name for the applied schema, for example'CollectionAPI:plasticStuff'.

        The name will only be added if the list operation at the edit target
        does not already have this applied schema in its explicit, prepended,
        or appended lists and is always added to the end of either the
        prepended or explicit items.

        Returns true upon success or if the API schema is already applied in
        the current edit target.

        An error is issued and false returned for any of the following
        conditions:
           - this prim is not a valid prim for editing

           - this prim is valid, but cannot be reached or overridden in the
             current edit target

           - the schema name cannot be added to the apiSchemas listOp metadata
             Unlike ApplyAPI this method does not require that the name token
             refer to a valid API schema type. ApplyAPI is the preferred method for
             applying valid API schemas.
        """
    @overload
    def ApplyAPI(self, schemaType: pxr.Tf.Type) -> bool:
        """
        This is an overload of ApplyAPI that takes a TfType C{schemaType}.
        """
    @overload
    def ApplyAPI(self, schemaType: pxr.Tf.Type, instanceName: str | pxr.Ar.ResolvedPath) -> bool:
        """
        This is an overload of ApplyAPI with C{instanceName} that takes a
        TfType C{schemaType}.


        """
    @overload
    def ApplyAPI(self, schemaIdentifier: str | pxr.Ar.ResolvedPath) -> bool:
        """
        This is an overload of ApplyAPI that takes a C{schemaIdentifier} to
        determine the schema type.


        """
    @overload
    def ApplyAPI(self, schemaIdentifier: str | pxr.Ar.ResolvedPath, instanceName: str | pxr.Ar.ResolvedPath) -> bool:
        """
        This is an overload of ApplyAPI with C{instanceName} that takes a
        C{schemaIdentifier} to determine the schema type.


        """
    @overload
    def ApplyAPI(self, schemaFamily: str | pxr.Ar.ResolvedPath, schemaVersion: int) -> bool:
        """
        This is an overload of ApplyAPI that takes a C{schemaFamily} and
        C{schemaVersion} to determine the schema type.


        """
    @overload
    def ApplyAPI(self, schemaFamily: str | pxr.Ar.ResolvedPath, schemaVersion: int, instanceName: str | pxr.Ar.ResolvedPath) -> bool:
        """
        This is an overload of ApplyAPI with C{instanceName} that takes a
        C{schemaFamily} and C{schemaVersion} to determine the schema type.


        """
    @overload
    def CanApplyAPI(self, schemaType: pxr.Tf.Type) -> _CanApplyAPIResult:
        """
        This is an overload of CanApplyAPI that takes a TfType C{schemaType}.


        """
    @overload
    def CanApplyAPI(self, schemaType: pxr.Tf.Type, instanceName: str | pxr.Ar.ResolvedPath) -> _CanApplyAPIResult:
        """
        This is an overload of CanApplyAPI with C{instanceName} that takes a
        TfType C{schemaType}.


        """
    @overload
    def CanApplyAPI(self, schemaIdentifier: str | pxr.Ar.ResolvedPath) -> _CanApplyAPIResult:
        """
        This is an overload of CanApplyAPI that takes a C{schemaIdentifier} to
        determine the schema type.


        """
    @overload
    def CanApplyAPI(self, schemaIdentifier: str | pxr.Ar.ResolvedPath, instanceName: str | pxr.Ar.ResolvedPath) -> _CanApplyAPIResult:
        """
        This is an overload of CanApplyAPI with C{instanceName} that takes a
        C{schemaIdentifier} to determine the schema type.


        """
    @overload
    def CanApplyAPI(self, schemaFamily: str | pxr.Ar.ResolvedPath, schemaVersion: int) -> _CanApplyAPIResult:
        """
        This is an overload of CanApplyAPI that takes a C{schemaFamily} and
        C{schemaVersion} to determine the schema type.


        """
    @overload
    def CanApplyAPI(self, schemaFamily: str | pxr.Ar.ResolvedPath, schemaVersion: int, instanceName: str | pxr.Ar.ResolvedPath) -> _CanApplyAPIResult:
        """
        This is an overload of CanApplyAPI with C{instanceName} that takes a
        C{schemaFamily} and C{schemaVersion} to determine the schema type.


        """
    def ClearActive(self) -> bool:
        '''
        Remove the authored\'active\'opinion at the current EditTarget.


        Do nothing if there is no authored opinion.

        See How"active"Affects Prims on a UsdStage for the effects of
        activating or deactivating a prim.
        '''
    def ClearChildrenReorder(self) -> None:
        """
        Remove the opinion for the metadata used to reorder children of this
        prim at the current EditTarget.
        """
    def ClearInstanceable(self) -> bool:
        """
        Remove the authored'instanceable'opinion at the current EditTarget.


        Do nothing if there is no authored opinion.
        """
    def ClearPayload(self) -> bool:
        """
        Deprecated

        Clears the payload at the current EditTarget for this prim. Return
        false if the payload could not be cleared.
        """
    def ClearPropertyOrder(self) -> None:
        """
        Remove the opinion for propertyOrder metadata on this prim at the
        current EditTarget.
        """
    def ClearTypeName(self) -> bool:
        """
        Clear the opinion for this Prim's typeName at the current edit target.
        """
    def ComputeExpandedPrimIndex(self) -> pxr.Pcp.PrimIndex:
        """
        Compute the prim index containing all sites that could contribute
        opinions to this prim.


        This function is similar to UsdPrim::GetPrimIndex. However, the
        returned prim index includes all sites that could possibly contribute
        opinions to this prim, not just the sites that currently do so. This
        is useful in certain situations; for example, this could be used to
        generate a list of sites where clients could make edits to affect this
        prim, or for debugging purposes.

        For all prims in prototypes, including the prototype prim itself, this
        is the expanded version of the prim index that was chosen to be shared
        with all other instances. Thus, the prim index's path will not be the
        same as the prim's path. Note that this behavior deviates slightly
        from UsdPrim::GetPrimIndex which always returns an empty prim index
        for the prototype prim itself.

        This function may be relatively slow, since it will recompute the prim
        index on every call. Clients should prefer UsdPrim::GetPrimIndex
        unless the additional site information is truly needed.
        """
    @overload
    def CreateAttribute(self, name: str | pxr.Ar.ResolvedPath, typeName: pxr.Sdf.ValueTypeName, custom: bool = ..., variability: pxr.Sdf.Variability = ...) -> Attribute:
        """
        Author scene description for the attribute named *attrName* at the
        current EditTarget if none already exists.


        Return a valid attribute if scene description was successfully
        authored or if it already existed, return invalid attribute otherwise.
        Note that the supplied *typeName* and *custom* arguments are only used
        in one specific case. See below for details.

        Suggested use: ::

          if (UsdAttribute myAttr = prim.CreateAttribute(...)) {
             // success. 
          }

        To call this, GetPrim() must return a valid prim.

           - If a spec for this attribute already exists at the current edit
             target, do nothing.

           - If a spec for *attrName* of a different spec type (e.g. a
             relationship) exists at the current EditTarget, issue an error.

           - If *name* refers to a builtin attribute according to the prim's
             definition, author an attribute spec with required metadata from the
             definition.

           - If *name* refers to a builtin relationship, issue an error.

           - If there exists an absolute strongest authored attribute spec for
             *attrName*, author an attribute spec at the current EditTarget by
             copying required metadata from that strongest spec.

           - If there exists an absolute strongest authored relationship spec
             for *attrName*, issue an error.

           - Otherwise author an attribute spec at the current EditTarget
             using the provided *typeName* and *custom* for the required metadata
             fields. Note that these supplied arguments are only ever used in this
             particular circumstance, in all other cases they are ignored.

        """
    @overload
    def CreateAttribute(self, nameElts: typing.Iterable[str | pxr.Ar.ResolvedPath], typeName: pxr.Sdf.ValueTypeName, custom: bool = ..., variability: pxr.Sdf.Variability = ...) -> Attribute:
        """
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        This overload of CreateAttribute() accepts a vector of name components
        used to construct a *namespaced* property name.


        For details, see Names, Namespace Ordering, and Property Namespaces
        """
    @overload
    def CreateRelationship(self, name: str | pxr.Ar.ResolvedPath, custom: bool = ...) -> Relationship:
        """
        Author scene description for the relationship named *relName* at the
        current EditTarget if none already exists.


        Return a valid relationship if scene description was successfully
        authored or if it already existed, return an invalid relationship
        otherwise.

        Suggested use: ::

          if (UsdRelationship myRel = prim.CreateRelationship(...)) {
             // success. 
          }

        To call this, GetPrim() must return a valid prim.

           - If a spec for this relationship already exists at the current
             edit target, do nothing.

           - If a spec for *relName* of a different spec type (e.g. an
             attribute) exists at the current EditTarget, issue an error.

           - If *name* refers to a builtin relationship according to the
             prim's definition, author a relationship spec with required metadata
             from the definition.

           - If *name* refers to a builtin attribute, issue an error.

           - If there exists an absolute strongest authored relationship spec
             for *relName*, author a relationship spec at the current EditTarget by
             copying required metadata from that strongest spec.

           - If there exists an absolute strongest authored attribute spec for
             *relName*, issue an error.

           - Otherwise author a uniform relationship spec at the current
             EditTarget, honoring C{custom}.

        """
    @overload
    def CreateRelationship(self, nameElts: typing.Iterable[str | pxr.Ar.ResolvedPath], custom: bool = ...) -> Relationship:
        """
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        This overload of CreateRelationship() accepts a vector of name
        components used to construct a *namespaced* property name.


        For details, see Names, Namespace Ordering, and Property Namespaces
        """
    @overload
    def FindAllAttributeConnectionPaths(self, traversalPredicate: _PrimFlagsPredicate | _Term, predicate: typing.Callable[[Attribute | pxr.UsdGeom.ConstraintTarget | pxr.UsdGeom.Primvar | pxr.UsdGeom.XformOp | pxr.UsdShade.Input | pxr.UsdShade.Output], bool] = ..., recurseOnSources: bool = ...) -> list[pxr.Sdf.Path]:
        """
        Search the prim subtree rooted at this prim according to
        C{traversalPredicate} for attributes for which C{predicate} returns
        true, collect their connection source paths and return them in an
        arbitrary order.


        If C{recurseOnSources} is true, act as if this function was invoked on
        the connected prims and owning prims of connected properties also and
        return the union.
        """
    @overload
    def FindAllAttributeConnectionPaths(self, predicate: typing.Callable[[Attribute | pxr.UsdGeom.ConstraintTarget | pxr.UsdGeom.Primvar | pxr.UsdGeom.XformOp | pxr.UsdShade.Input | pxr.UsdShade.Output], bool] = ..., recurseOnSources: bool = ...) -> list[pxr.Sdf.Path]:
        """
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        Invoke FindAllAttributeConnectionPaths() with the
        UsdPrimDefaultPredicate as its traversalPredicate.
        """
    @overload
    def FindAllRelationshipTargetPaths(self, traversalPredicate: _PrimFlagsPredicate | _Term, predicate: typing.Callable[[Relationship], bool] = ..., recurseOnTargets: bool = ...) -> list[pxr.Sdf.Path]:
        """
        Search the prim subtree rooted at this prim according to
        C{traversalPredicate} for relationships for which C{predicate} returns
        true, collect their target paths and return them in an arbitrary
        order.


        If C{recurseOnTargets} is true, act as if this function was invoked on
        the targeted prims and owning prims of targeted properties also (but
        not of forwarding relationships) and return the union.
        """
    @overload
    def FindAllRelationshipTargetPaths(self, predicate: typing.Callable[[Relationship], bool] = ..., recurseOnTargets: bool = ...) -> list[pxr.Sdf.Path]:
        """
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        Invoke FindAllRelationshipTargetPaths() with the
        UsdPrimDefaultPredicate as its traversalPredicate.
        """
    def GetAllChildren(self) -> list:
        """
        Return all this prim's children as an iterable range.
        """
    def GetAllChildrenNames(self) -> list[str]:
        """
        Return the names of the child prims in the order they appear when
        iterating over GetAllChildren.


        """
    def GetAppliedSchemas(self) -> list[str]:
        """
        Return a vector containing the names of API schemas which have been
        applied to this prim.


        This includes both the authored API schemas applied using the Apply()
        method on the particular schema class as well as any built-in API
        schemas that are automatically included through the prim type's prim
        definition. To get only the authored API schemas use GetPrimTypeInfo
        instead.
        """
    def GetAttribute(self, attrName: str | pxr.Ar.ResolvedPath) -> Attribute:
        '''
        Return a UsdAttribute with the name *attrName*.


        The attribute returned may or may not B{actually} exist so it must be
        checked for validity. Suggested use: ::

          if (UsdAttribute myAttr = prim.GetAttribute("myAttr")) {
             // myAttr is safe to use. 
             // Edits to the owning stage requires subsequent validation.
          } else {
             // myAttr was not defined/authored
          }

        '''
    def GetAttributeAtPath(self, path: pxr.Sdf.Path | str) -> Attribute:
        """
        Returns the attribute at C{path} on the same stage as this prim.


        If path is relative, it will be anchored to the path of this prim.

        There is no guarantee that this method returns an attribute on this
        prim. This is only guaranteed if path is a purely relative property
        path.

        GetAttribute(const TfToken&) const

        UsdStage::GetAttributeAtPath(const SdfPath&) const
        """
    def GetAttributes(self) -> list[Attribute]:
        """
        Like GetProperties() , but exclude all relationships from the result.
        """
    def GetAuthoredAttributes(self) -> list[Attribute]:
        """
        Like GetAttributes() , but exclude attributes without authored scene
        description from the result.


        See UsdProperty::IsAuthored() .
        """
    def GetAuthoredProperties(self, predicate: typing.Callable[[str | pxr.Ar.ResolvedPath], bool] = ...) -> list[Property]:
        """
        Return this prim's properties (attributes and relationships) that have
        authored scene description, ordered by name according to the strongest
        propertyOrder statement in scene description if one exists, otherwise
        ordered according to TfDictionaryLessThan.


        If a valid C{predicate} is passed in, then only authored properties
        whose names pass the predicate are included in the result. This is
        useful if the client is interested only in a subset of authored
        properties on the prim. For example, only the ones in a given
        namespace or only the ones needed to compute a value.

        GetProperties()

        UsdProperty::IsAuthored()
        """
    @overload
    def GetAuthoredPropertiesInNamespace(self, namespaces: typing.Iterable[str | pxr.Ar.ResolvedPath]) -> list[Property]:
        """
        Like GetPropertiesInNamespace() , but exclude properties that do not
        have authored scene description from the result.


        See UsdProperty::IsAuthored() .

        For details of namespaced properties, see Names, Namespace Ordering,
        and Property Namespaces
        """
    @overload
    def GetAuthoredPropertiesInNamespace(self, namespaces: str | pxr.Ar.ResolvedPath) -> list[Property]:
        """
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        C{namespaces} must be an already-concatenated ordered set of
        namespaces, and may or may not terminate with the namespace-separator
        character.


        If C{namespaces} is empty, this method is equivalent to
        GetAuthoredProperties() .
        """
    def GetAuthoredPropertyNames(self, predicate: typing.Callable[[str | pxr.Ar.ResolvedPath], bool] = ...) -> list[str]:
        """
        Return this prim's property names (attributes and relationships) that
        have authored scene description, ordered according to the strongest
        propertyOrder statement in scene description if one exists, otherwise
        ordered according to TfDictionaryLessThan.


        If a valid C{predicate} is passed in, then only the authored
        properties whose names pass the predicate are included in the result.
        This is useful if the client is interested only in a subset of
        authored properties on the prim. For example, only the ones in a given
        namespace or only the ones needed to compute a value.

        GetPropertyNames()

        UsdProperty::IsAuthored()
        """
    def GetAuthoredRelationships(self) -> list[Relationship]:
        """
        Like GetRelationships() , but exclude relationships without authored
        scene description from the result.


        See UsdProperty::IsAuthored() .
        """
    def GetChild(self, name: str | pxr.Ar.ResolvedPath) -> Prim:
        """
        Return this prim's direct child named C{name} if it has one, otherwise
        return an invalid UsdPrim.


        Equivalent to: ::

          prim.GetStage()->GetPrimAtPath(prim.GetPath().AppendChild(name))

        """
    def GetChildren(self) -> list:
        """
        Return this prim's active, loaded, defined, non-abstract children as
        an iterable range.


        Equivalent to: ::

          GetFilteredChildren(UsdPrimDefaultPredicate)

        See Prim predicate flags and UsdPrimDefaultPredicate for more
        information.
        """
    def GetChildrenNames(self) -> list[str]:
        """
        Return the names of the child prims in the order they appear when
        iterating over GetChildren.


        """
    def GetChildrenReorder(self) -> list[str]:
        """
        Return the strongest opinion for the metadata used to reorder children
        of this prim.


        Due to how reordering of prim children is composed, this value cannot
        be relied on to get the actual order of the prim's children. Use
        GetChidrenNames, GetAllChildrenNames, GetFilteredChildrenNames to get
        the true child order if needed.
        """
    def GetFilteredChildren(self, predicate: _PrimFlagsPredicate | _Term) -> list:
        """
        Return a subset of all of this prim's children filtered by
        C{predicate} as an iterable range.


        The C{predicate} is generated by combining a series of prim flag terms
        with either&&or || and !.

        Example usage: ::

          // Get all active model children.
          GetFilteredChildren(UsdPrimIsActive && UsdPrimIsModel);
  
          // Get all model children that pass the default predicate.
          GetFilteredChildren(UsdPrimDefaultPredicate && UsdPrimIsModel);

        If this prim is an instance, no children will be returned unless
        UsdTraverseInstanceProxies is used to allow instance proxies to be
        returned, or if this prim is itself an instance proxy.

        See Prim predicate flags and UsdPrimDefaultPredicate for more
        information.
        """
    def GetFilteredChildrenNames(self, _predicate: _PrimFlagsPredicate | _Term, /) -> list[str]:
        """
        Return the names of the child prims in the order they appear when
        iterating over GetFilteredChildren( C{predicate}).


        """
    def GetFilteredNextSibling(self, _predicate: _PrimFlagsPredicate | _Term, /) -> Prim:
        """
        Return this prim's next sibling that matches C{predicate} if it has
        one, otherwise return the invalid UsdPrim.


        See Prim predicate flags and UsdPrimDefaultPredicate for more
        information.
        """
    def GetInherits(self) -> Inherits:
        """
        Return a UsdInherits object that allows one to add, remove, or mutate
        inherits *at the currently set UsdEditTarget*.


        While the UsdInherits object has no methods for *listing* the
        currently authored inherits on a prim, one can use a
        UsdPrimCompositionQuery to query the inherits arcs that are composed
        by this prim.

        UsdPrimCompositionQuery::GetDirectInherits
        """
    def GetInstances(self) -> list[Prim]:
        """
        If this prim is a prototype prim, returns all prims that are instances
        of this prototype.


        Otherwise, returns an empty vector.

        Note that this function will return prims in prototypes for instances
        that are nested beneath other instances.
        """
    def GetKind(self) -> str:
        '''
        Retrieve the authored C{kind} for this prim.


        To test whether the returned C{kind} matches a particular
        known"clientKind": ::

          TfToken kind;
  
          bool isClientKind = prim.GetKind(&kind) and
                              KindRegistry::IsA(kind, clientKind);

        true if there was an authored kind that was successfully read,
        otherwise false. Note that this will return false for pseudoroot even
        though pseudoroot is always a group, without any kind (in order to
        respect model hierarchy rules)

        The Kind module for further details on how to use Kind for
        classification, and how to extend the taxonomy.
        '''
    def GetNextSibling(self) -> Prim:
        """
        Return this prim's next active, loaded, defined, non-abstract sibling
        if it has one, otherwise return an invalid UsdPrim.


        Equivalent to: ::

          GetFilteredNextSibling(UsdPrimDefaultPredicate)

        See Prim predicate flags and UsdPrimDefaultPredicate for more
        information.
        """
    def GetObjectAtPath(self, path: pxr.Sdf.Path | str) -> Object:
        """
        Returns the object at C{path} on the same stage as this prim.


        If path is is relative, it will be anchored to the path of this prim.

        UsdStage::GetObjectAtPath(const SdfPath&) const
        """
    def GetParent(self) -> Prim:
        """
        Return this prim's parent prim.


        Return an invalid UsdPrim if this is a root prim.
        """
    def GetPayloads(self) -> Payloads:
        """
        Return a UsdPayloads object that allows one to add, remove, or mutate
        payloads *at the currently set UsdEditTarget*.


        While the UsdPayloads object has no methods for *listing* the
        currently authored payloads on a prim, one can use a
        UsdPrimCompositionQuery to query the payload arcs that are composed by
        this prim.
        """
    def GetPrimAtPath(self, path: pxr.Sdf.Path | str) -> Prim:
        """
        Returns the prim at C{path} on the same stage as this prim.


        If path is is relative, it will be anchored to the path of this prim.

        UsdStage::GetPrimAtPath(const SdfPath&) const
        """
    def GetPrimDefinition(self) -> PrimDefinition:
        """
        Return this prim's definition based on the prim's type if the type is
        a registered prim type.


        Returns an empty prim definition if it is not.
        """
    def GetPrimInPrototype(self) -> Prim:
        """
        If this prim is an instance proxy, return the UsdPrim for the
        corresponding prim in the instance's prototype.


        Otherwise, return an invalid UsdPrim.
        """
    def GetPrimIndex(self) -> pxr.Pcp.PrimIndex:
        """
        Return the cached prim index containing all sites that can contribute
        opinions to this prim.


        The prim index can be used to examine the composition arcs and scene
        description sites that can contribute to this prim's property and
        metadata values.

        The prim index returned by this function is optimized and may not
        include sites that do not contribute opinions to this prim. Use
        UsdPrim::ComputeExpandedPrimIndex to compute a prim index that
        includes all possible sites that could contribute opinions.

        This prim index will be empty for prototype prims. This ensures that
        these prims do not provide any attribute or metadata values. For all
        other prims in prototypes, this is the prim index that was chosen to
        be shared with all other instances. In either case, the prim index's
        path will not be the same as the prim's path.

        Prim indexes may be invalidated by changes to the UsdStage and cannot
        detect if they are expired. Clients should avoid keeping copies of the
        prim index across such changes, which include scene description
        changes or changes to load state.
        """
    def GetPrimStack(self) -> list[pxr.Sdf.PrimSpec]:
        '''
        Return all the authored SdfPrimSpecs that may contain opinions for
        this prim in order from strong to weak.


        This does not include all the places where contributing prim specs
        could potentially be created; rather, it includes only those prim
        specs that already exist. To discover all the places that prim specs
        could be authored that would contribute opinions, see"Composition
        Structure"

        Use this method for debugging and diagnostic purposes. It is B{not}
        advisable to retain a PrimStack for expedited metadata value
        resolution, since not all metadata resolves with
        simple"strongestopinion wins"semantics.
        '''
    def GetPrimStackWithLayerOffsets(self) -> list[tuple[pxr.Sdf.PrimSpec, pxr.Sdf.LayerOffset]]:
        '''
        Return all the authored SdfPrimSpecs that may contain opinions for
        this prim in order from strong to weak paired with the cumulative
        layer offset from the stage\'s root layer to the layer containing the
        prim spec.


        This behaves exactly the same as UsdPrim::GetPrimStack with the
        addition of providing the cumulative layer offset of each spec\'s
        layer.

        Use this method for debugging and diagnostic purposes. It is B{not}
        advisable to retain a PrimStack for expedited metadata value
        resolution, since not all metadata resolves with
        simple"strongestopinion wins"semantics.
        '''
    def GetPrimTypeInfo(self) -> PrimTypeInfo:
        '''
        Return the prim\'s full type info composed from its type name, applied
        API schemas, and any fallback types defined on the stage for
        unrecognized prim type names.


        The returned type structure contains the"true"schema type used to
        create this prim\'s prim definition and answer the IsA query. This
        value is cached and efficient to query. The cached values are
        guaranteed to exist for (at least) as long as the prim\'s stage is
        open.

        GetTypeName

        GetAppliedSchemas

        Fallback Prim Types
        '''
    def GetProperties(self, predicate: typing.Callable[[str | pxr.Ar.ResolvedPath], bool] = ...) -> list[Property]:
        """
        Return all of this prim's properties (attributes and relationships),
        including all builtin properties, ordered by name according to the
        strongest propertyOrder statement in scene description if one exists,
        otherwise ordered according to TfDictionaryLessThan.


        If a valid C{predicate} is passed in, then only properties whose names
        pass the predicate are included in the result. This is useful if the
        client is interested only in a subset of properties on the prim. For
        example, only the ones in a given namespace or only the ones needed to
        compute a value.

        To obtain only either attributes or relationships, use either
        GetAttributes() or GetRelationships() .

        To determine whether a property is either an attribute or a
        relationship, use the UsdObject::As() and UsdObject::Is() methods in
        C++: ::

          // Use As<>() to obtain a subclass instance.
          if (UsdAttribute attr = property.As<UsdAttribute>()) {
              // use attribute 'attr'.
          else if (UsdRelationship rel = property.As<UsdRelationship>()) {
              // use relationship 'rel'.
          }
  
          // Use Is<>() to discriminate only.
          if (property.Is<UsdAttribute>()) {
              // property is an attribute.
          }

        In Python, use the standard isinstance() function: ::

          if isinstance(property, Usd.Attribute):
              # property is a Usd.Attribute.
          elif isinstance(property, Usd.Relationship):
              # property is a Usd.Relationship.

        GetAuthoredProperties()

        UsdProperty::IsAuthored()
        """
    @overload
    def GetPropertiesInNamespace(self, namespaces: typing.Iterable[str | pxr.Ar.ResolvedPath]) -> list[Property]:
        '''
        Return this prim\'s properties that are inside the given property
        namespace ordered according to the strongest propertyOrder statement
        in scene description if one exists, otherwise ordered according to
        TfDictionaryLessThan.


        A C{namespaces} argument whose elements are ["ri","attribute"] will
        return all the properties under the namespace"ri:attribute",
        i.e."ri:attribute:*". An empty C{namespaces} argument is equivalent to
        GetProperties() .

        For details of namespaced properties, see Names, Namespace Ordering,
        and Property Namespaces
        '''
    @overload
    def GetPropertiesInNamespace(self, namespaces: str | pxr.Ar.ResolvedPath) -> list[Property]:
        """
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        C{namespaces} must be an already-concatenated ordered set of
        namespaces, and may or may not terminate with the namespace-separator
        character.


        If C{namespaces} is empty, this method is equivalent to
        GetProperties() .
        """
    def GetProperty(self, propName: str | pxr.Ar.ResolvedPath) -> Property:
        '''
        Return a UsdProperty with the name *propName*.


        The property returned may or may not B{actually} exist so it must be
        checked for validity. Suggested use: ::

          if (UsdProperty myProp = prim.GetProperty("myProp")) {
             // myProp is safe to use. 
             // Edits to the owning stage requires subsequent validation.
          } else {
             // myProp was not defined/authored
          }

        '''
    def GetPropertyAtPath(self, path: pxr.Sdf.Path | str) -> Property:
        """
        Returns the property at C{path} on the same stage as this prim.


        If path is relative, it will be anchored to the path of this prim.

        There is no guarantee that this method returns a property on this
        prim. This is only guaranteed if path is a purely relative property
        path.

        GetProperty(const TfToken&) const

        UsdStage::GetPropertyAtPath(const SdfPath&) const
        """
    def GetPropertyNames(self, predicate: typing.Callable[[str | pxr.Ar.ResolvedPath], bool] = ...) -> list[str]:
        """
        Return all of this prim's property names (attributes and
        relationships), including all builtin properties.


        If a valid C{predicate} is passed in, then only properties whose names
        pass the predicate are included in the result. This is useful if the
        client is interested only in a subset of properties on the prim. For
        example, only the ones in a given namespace or only the ones needed to
        compute a value.

        GetAuthoredPropertyNames()

        UsdProperty::IsAuthored()
        """
    def GetPropertyOrder(self) -> list[str]:
        """
        Return the strongest propertyOrder metadata value authored on this
        prim.
        """
    def GetPrototype(self) -> Prim:
        """
        If this prim is an instance, return the UsdPrim for the corresponding
        prototype.


        Otherwise, return an invalid UsdPrim.
        """
    def GetReferences(self) -> References:
        """
        Return a UsdReferences object that allows one to add, remove, or
        mutate references *at the currently set UsdEditTarget*.


        While the UsdReferences object has no methods for *listing* the
        currently authored references on a prim, one can use a
        UsdPrimCompositionQuery to query the reference arcs that are composed
        by this prim.

        UsdPrimCompositionQuery::GetDirectReferences
        """
    def GetRelationship(self, relName: str | pxr.Ar.ResolvedPath) -> Relationship:
        '''
        Return a UsdRelationship with the name *relName*.


        The relationship returned may or may not B{actually} exist so it must
        be checked for validity. Suggested use: ::

          if (UsdRelationship myRel = prim.GetRelationship("myRel")) {
             // myRel is safe to use.
             // Edits to the owning stage requires subsequent validation.
          } else {
             // myRel was not defined/authored
          }

        '''
    def GetRelationshipAtPath(self, path: pxr.Sdf.Path | str) -> Relationship:
        """
        Returns the relationship at C{path} on the same stage as this prim.


        If path is relative, it will be anchored to the path of this prim.

        There is no guarantee that this method returns a relationship on this
        prim. This is only guaranteed if path is a purely relative property
        path.

        GetRelationship(const TfToken&) const

        UsdStage::GetRelationshipAtPath(const SdfPath&) const
        """
    def GetRelationships(self) -> list[Relationship]:
        """
        Like GetProperties() , but exclude all attributes from the result.
        """
    def GetSpecializes(self) -> Specializes:
        """
        Return a UsdSpecializes object that allows one to add, remove, or
        mutate specializes *at the currently set UsdEditTarget*.


        While the UsdSpecializes object has no methods for *listing* the
        currently authored specializes on a prim, one can use a
        UsdPrimCompositionQuery to query the specializes arcs that are
        composed by this prim.
        """
    def GetSpecifier(self) -> pxr.Sdf.Specifier:
        """
        Return this prim's composed specifier.
        """
    def GetTypeName(self) -> str:
        """
        Return this prim's composed type name.


        This value is cached and is efficient to query. Note that this is just
        the composed type name as authored and may not represent the full type
        of the prim and its prim definition. If you need to reason about the
        actual type of the prim, use GetPrimTypeInfo instead as it accounts
        for recognized schemas, applied API schemas, fallback types, etc.
        """
    def GetVariantSet(self, _variantSetName: str | pxr.Ar.ResolvedPath, /) -> VariantSet:
        """
        Retrieve a specifically named VariantSet for editing or constructing a
        UsdEditTarget.


        This is a shortcut for ::

          prim.GetVariantSets().GetVariantSet(variantSetName)

        """
    def GetVariantSets(self) -> VariantSets:
        """
        Return a UsdVariantSets object representing all the VariantSets
        present on this prim.


        The returned object also provides the API for adding new VariantSets
        to the prim.
        """
    @overload
    def GetVersionIfHasAPIInFamily(self, _schemaFamily: str | pxr.Ar.ResolvedPath, /) -> int:
        """
        Return true if the prim has an applied API schema that is any version
        the schemas in the given C{schemaFamily} and if so, populates
        C{schemaVersion} with the version of the schema that this prim HasAPI.


        This function will consider both single-apply and multiple-apply API
        schemas in the schema family. For the multiple-apply API schemas is a
        this will return true if any instance of one of the schemas has been
        applied.

        Note that if more than one version of the schemas in C{schemaFamily}
        are applied to this prim, the highest version number of these schemas
        will be populated in C{schemaVersion}.
        """
    @overload
    def GetVersionIfHasAPIInFamily(self, _schemaFamily: str | pxr.Ar.ResolvedPath, _instanceName: str | pxr.Ar.ResolvedPath, /) -> int:
        """
        Return true if the prim has a specific instance C{instanceName} of an
        applied multiple-apply API schema that is any version the schemas in
        the given C{schemaFamily} and if so, populates C{schemaVersion} with
        the version of the schema that this prim HasAPI.


        C{instanceName} must be non-empty, otherwise it is a coding error.

        Note that if more than one version of the schemas in C{schemaFamily}
        is multiple-apply and applied to this prim with the given
        C{instanceName}, the highest version number of these schemas will be
        populated in C{schemaVersion}.
        """
    def GetVersionIfIsInFamily(self, _schemaFamily: str | pxr.Ar.ResolvedPath, /) -> int:
        """
        Return true if the prim's schema type, is or inherits from the schema
        type of any version the schema in the given C{schemaFamily} and if so,
        populates C{schemaVersion} with the version of the schema that this
        prim IsA.
        """
    @overload
    def HasAPI(self, schemaType: pxr.Tf.Type) -> bool:
        """
        This is an overload of HasAPI that takes a TfType C{schemaType}.
        """
    @overload
    def HasAPI(self, schemaType: pxr.Tf.Type, instanceName: str | pxr.Ar.ResolvedPath) -> bool:
        """
        This is an overload of HasAPI with C{instanceName} that takes a TfType
        C{schemaType}.


        """
    @overload
    def HasAPI(self, schemaIdentifier: str | pxr.Ar.ResolvedPath) -> bool:
        """
        This is an overload of HasAPI that takes a C{schemaIdentifier} to
        determine the schema type.


        """
    @overload
    def HasAPI(self, schemaIdentifier: str | pxr.Ar.ResolvedPath, instanceName: str | pxr.Ar.ResolvedPath) -> bool:
        """
        This is an overload of HasAPI with C{instanceName} that takes a
        C{schemaIdentifier} to determine the schema type.


        """
    @overload
    def HasAPI(self, schemaFamily: str | pxr.Ar.ResolvedPath, schemaVersion: int) -> bool:
        """
        This is an overload of HasAPI that takes a C{schemaFamily} and
        C{schemaVersion} to determine the schema type.


        """
    @overload
    def HasAPI(self, schemaFamily: str | pxr.Ar.ResolvedPath, schemaVersion: int, instanceName: str | pxr.Ar.ResolvedPath) -> bool:
        """
        This is an overload of HasAPI with C{instanceName} that takes a
        C{schemaFamily} and C{schemaVersion} to determine the schema type.


        """
    @overload
    def HasAPIInFamily(self, schemaFamily: str | pxr.Ar.ResolvedPath) -> bool:
        """
        Return true if the prim has an applied API schema that is any version
        of the schemas in the given C{schemaFamily}.


        This function will consider both single-apply and multiple-apply API
        schemas in the schema family. For the multiple-apply API schemas, this
        will return true if any instance of one of the schemas has been
        applied.
        """
    @overload
    def HasAPIInFamily(self, schemaFamily: str | pxr.Ar.ResolvedPath, instanceName: str | pxr.Ar.ResolvedPath) -> bool:
        """
        Return true if the prim has a specific instance C{instanceName} of an
        applied multiple-apply API schema that is any version the schemas in
        the given C{schemaFamily}.


        C{instanceName} must be non-empty, otherwise it is a coding error.
        """
    @overload
    def HasAPIInFamily(self, schemaFamily: str | pxr.Ar.ResolvedPath, schemaVersion: int, versionPolicy: SchemaRegistry.VersionPolicy) -> bool:
        """
        Return true if the prim has an applied API schema that is a schema in
        the given C{schemaFamily} that matches the version filter provided by
        C{schemaVersion} and C{versionPolicy}.


        This function will consider both single-apply and multiple-apply API
        schemas in the schema family. For the multiple-apply API schemas, this
        will return true if any instance of one of the filter-passing schemas
        has been applied.
        """
    @overload
    def HasAPIInFamily(self, schemaFamily: str | pxr.Ar.ResolvedPath, schemaVersion: int, versionPolicy: SchemaRegistry.VersionPolicy, instanceName: str | pxr.Ar.ResolvedPath) -> bool:
        """
        Return true if the prim has a specific instance C{instanceName} of an
        applied multiple-apply API schema in the given C{schemaFamily} that
        matches the version filter provided by C{schemaVersion} and
        C{versionPolicy}.


        C{instanceName} must be non-empty, otherwise it is a coding error.
        """
    @overload
    def HasAPIInFamily(self, schemaType: pxr.Tf.Type, versionPolicy: SchemaRegistry.VersionPolicy) -> bool:
        """
        Overload for convenience of HasAPIInFamily that finds a registered
        schema for the given C{schemaType} and uses that schema's family and
        version.
        """
    @overload
    def HasAPIInFamily(self, schemaType: pxr.Tf.Type, versionPolicy: SchemaRegistry.VersionPolicy, instanceName: str | pxr.Ar.ResolvedPath) -> bool:
        """
        Overload for convenience of HasAPIInFamily that finds a registered
        schema for the given C{schemaType} and uses that schema's family and
        version.
        """
    @overload
    def HasAPIInFamily(self, schemaIdentifier: str | pxr.Ar.ResolvedPath, versionPolicy: SchemaRegistry.VersionPolicy) -> bool:
        """
        Overload for convenience of HasAPIInFamily that parses the schema
        family and version to use from the given C{schemaIdentifier}.


        Note that the schema identifier is not required to be a registered
        schema as it only parsed to get what its family and version would be
        See UsdSchemaRegistry::ParseSchemaFamilyAndVersionFromIdentifier.
        """
    @overload
    def HasAPIInFamily(self, schemaIdentifier: str | pxr.Ar.ResolvedPath, versionPolicy: SchemaRegistry.VersionPolicy, instanceName: str | pxr.Ar.ResolvedPath) -> bool:
        """
        Overload for convenience of HasAPIInFamily that parses the schema
        family and version to use from the given C{schemaIdentifier}.


        Note that the schema identifier is not required to be a registered
        schema as it only parsed to get what its family and version would be
        See UsdSchemaRegistry::ParseSchemaFamilyAndVersionFromIdentifier.
        """
    def HasAttribute(self, attrName: str | pxr.Ar.ResolvedPath) -> bool:
        """
        Return true if this prim has an attribute named C{attrName}, false
        otherwise.
        """
    def HasAuthoredActive(self) -> bool:
        '''
        Return true if this prim has an authored opinion for\'active\', false
        otherwise.


        See How"active"Affects Prims on a UsdStage for what it means for a
        prim to be active.
        '''
    def HasAuthoredInherits(self) -> bool:
        """
        Return true if this prim has any authored inherits.
        """
    def HasAuthoredInstanceable(self) -> bool:
        """
        Return true if this prim has an authored opinion for'instanceable',
        false otherwise.
        """
    def HasAuthoredPayloads(self) -> bool:
        """
        Return true if this prim has any authored payloads.
        """
    def HasAuthoredReferences(self) -> bool:
        """
        Return true if this prim has any authored references.
        """
    def HasAuthoredSpecializes(self) -> bool:
        """
        Returns true if this prim has any authored specializes.
        """
    def HasAuthoredTypeName(self) -> bool:
        """
        Return true if a typeName has been authored.
        """
    def HasDefiningSpecifier(self) -> bool:
        """
        Return true if this prim has a specifier of type SdfSpecifierDef or
        SdfSpecifierClass.



        SdfIsDefiningSpecifier
        """
    def HasPayload(self) -> bool:
        """
        Deprecated

        Return true if a payload is present on this prim.

        Payloads: Impact of Using and Not Using
        """
    def HasProperty(self, propName: str | pxr.Ar.ResolvedPath) -> bool:
        """
        Return true if this prim has an property named C{propName}, false
        otherwise.
        """
    def HasRelationship(self, relName: str | pxr.Ar.ResolvedPath) -> bool:
        """
        Return true if this prim has a relationship named C{relName}, false
        otherwise.
        """
    def HasVariantSets(self) -> bool:
        """
        Return true if this prim has any authored VariantSets.



        this connotes only the *existence* of one of more VariantSets, *not*
        that such VariantSets necessarily contain any variants or variant
        opinions.
        """
    @overload
    def IsA(self, schemaType: pxr.Tf.Type) -> bool:
        """
        This is an overload of IsA that takes a TfType C{schemaType}.
        """
    @overload
    def IsA(self, schemaIdentifier: str | pxr.Ar.ResolvedPath) -> bool:
        """
        This is an overload of IsA that takes a C{schemaIdentifier} to
        determine the schema type.


        """
    @overload
    def IsA(self, schemaFamily: str | pxr.Ar.ResolvedPath, version: int) -> bool:
        """
        This is an overload of IsA that takes a C{schemaFamily} and
        C{schemaVersion} to determine the schema type.


        """
    def IsAbstract(self) -> bool:
        """
        Return true if this prim or any of its ancestors is a class.
        """
    def IsActive(self) -> bool:
        '''
        Return true if this prim is active, meaning neither it nor any of its
        ancestors have active=false.


        Return false otherwise.

        See How"active"Affects Prims on a UsdStage for what it means for a
        prim to be active.
        '''
    def IsComponent(self) -> bool:
        """
        Return true if this prim is a component model based on its kind
        metadata, false otherwise.


        If this prim is a component, it is also necessarily a model.
        """
    def IsDefined(self) -> bool:
        """
        Return true if this prim and all its ancestors have defining
        specifiers, false otherwise.



        SdfIsDefiningSpecifier.
        """
    def IsGroup(self) -> bool:
        """
        Return true if this prim is a model group based on its kind metadata,
        false otherwise.


        If this prim is a group, it is also necessarily a model.

        Note that pseudoroot is always a group (in order to respect model
        hierarchy rules), even though it cannot have a kind.
        """
    @overload
    def IsInFamily(self, schemaFamily: str | pxr.Ar.ResolvedPath) -> bool:
        """
        Return true if the prim's schema type is or inherits from the schema
        type of any version of the schemas in the given C{schemaFamily}.
        """
    @overload
    def IsInFamily(self, schemaFamily: str | pxr.Ar.ResolvedPath, version: int, versionPolicy: SchemaRegistry.VersionPolicy) -> bool:
        """
        Return true if the prim's schema type, is or inherits from the schema
        type of any schema in the given C{schemaFamily} that matches the
        version filter provided by C{schemaVersion} and C{versionPolicy}.
        """
    @overload
    def IsInFamily(self, schemaType: pxr.Tf.Type, versionPolicy: SchemaRegistry.VersionPolicy) -> bool:
        """
        Overload for convenience of IsInFamily that finds a registered schema
        for the given C{schemaType} and uses that schema's family and version.
        """
    @overload
    def IsInFamily(self, schemaIdentifier: str | pxr.Ar.ResolvedPath, versionPolicy: SchemaRegistry.VersionPolicy) -> bool:
        """
        Overload for convenience of IsInFamily that parses the schema family
        and version to use from the given C{schemaIdentifier}.


        Note that the schema identifier is not required to be a registered
        schema as it only parsed to get what its family and version would be
        See UsdSchemaRegistry::ParseSchemaFamilyAndVersionFromIdentifier.
        """
    def IsInPrototype(self) -> bool:
        """
        Return true if this prim is a prototype prim or a descendant of a
        prototype prim, false otherwise.



        IsPrototype
        """
    def IsInstance(self) -> bool:
        """
        Return true if this prim is an instance of a prototype, false
        otherwise.


        If this prim is an instance, calling GetPrototype() will return the
        UsdPrim for the corresponding prototype prim.
        """
    def IsInstanceProxy(self) -> bool:
        """
        Return true if this prim is an instance proxy, false otherwise.


        An instance proxy prim represents a descendent of an instance prim.
        """
    def IsInstanceable(self) -> bool:
        """
        Return true if this prim has been marked as instanceable.


        Note that this is not the same as IsInstance() . A prim may return
        true for IsInstanceable() and false for IsInstance() if this prim is
        not active or if it is marked as instanceable but contains no
        instanceable data.
        """
    def IsLoaded(self) -> bool:
        """
        Return true if this prim is active, and *either* it is loadable and it
        is loaded, *or* its nearest loadable ancestor is loaded, *or* it has
        no loadable ancestor; false otherwise.
        """
    def IsModel(self) -> bool:
        """
        Return true if this prim is a model based on its kind metadata, false
        otherwise.
        """
    @staticmethod
    def IsPathInPrototype(path: pxr.Sdf.Path | str) -> bool:
        """
        Return true if the given C{path} identifies a prototype prim or a prim
        or property descendant of a prototype prim, false otherwise.



        IsPrototypePath
        """
    def IsPrototype(self) -> bool:
        """
        Return true if this prim is an instancing prototype prim, false
        otherwise.



        IsInPrototype
        """
    @staticmethod
    def IsPrototypePath(path: pxr.Sdf.Path | str) -> bool:
        """
        Return true if the given C{path} identifies a prototype prim, false
        otherwise.


        This function will return false for prim and property paths that are
        descendants of a prototype prim path.

        IsPathInPrototype
        """
    def IsPseudoRoot(self) -> bool:
        """
        Returns true if the prim is the pseudo root.



        Equivalent to ::

          prim.GetPath() == SdfPath::AbsoluteRootPath()

        """
    def IsSubComponent(self) -> bool:
        """
        Return true if this prim is a subcomponent based on its kind metadata,
        false otherwise.


        Note that subcomponent query is not cached because we only cache
        model-hierarchy-related information, and therefore will be
        considerably slower than other kind-based queries.
        """
    def Load(self, policy: LoadPolicy = ...) -> None:
        """
        Load this prim, all its ancestors, and by default all its descendants.


        If C{loadPolicy} is UsdLoadWithoutDescendants, then load only this
        prim and its ancestors.

        See UsdStage::Load for additional details.
        """
    def MakeResolveTargetStrongerThanEditTarget(self, _editTarget: EditTarget | pxr.Sdf.Layer, /) -> ResolveTarget:
        """
        Creates and returns a resolve target that, when passed to a
        UsdAttributeQuery for one of this prim's attributes, causes value
        resolution to only consider specs that are stronger than the spec that
        would be authored for this prim when using the given C{editTarget}.


        If the edit target would not affect any specs that could contribute to
        this prim, a null resolve target is returned.
        """
    def MakeResolveTargetUpToEditTarget(self, _editTarget: EditTarget | pxr.Sdf.Layer, /) -> ResolveTarget:
        """
        Creates and returns a resolve target that, when passed to a
        UsdAttributeQuery for one of this prim's attributes, causes value
        resolution to only consider weaker specs up to and including the spec
        that would be authored for this prim when using the given
        C{editTarget}.


        If the edit target would not affect any specs that could contribute to
        this prim, a null resolve target is returned.
        """
    @overload
    def RemoveAPI(self, schemaType: pxr.Tf.Type) -> bool:
        """
        This is an overload of RemoveAPI that takes a TfType C{schemaType}.
        """
    @overload
    def RemoveAPI(self, schemaType: pxr.Tf.Type, instanceName: str | pxr.Ar.ResolvedPath) -> bool:
        """
        This is an overload of RemoveAPI with C{instanceName} that takes a
        TfType C{schemaType}.


        """
    @overload
    def RemoveAPI(self, schemaIdentifier: str | pxr.Ar.ResolvedPath) -> bool:
        """
        This is an overload of RemoveAPI that takes a C{schemaIdentifier} to
        determine the schema type.


        """
    @overload
    def RemoveAPI(self, schemaIdentifier: str | pxr.Ar.ResolvedPath, instanceName: str | pxr.Ar.ResolvedPath) -> bool:
        """
        This is an overload of RemoveAPI with C{instanceName} that takes a
        C{schemaIdentifier} to determine the schema type.


        """
    @overload
    def RemoveAPI(self, schemaFamily: str | pxr.Ar.ResolvedPath, schemaVersion: int) -> bool:
        """
        This is an overload of RemoveAPI that takes a C{schemaFamily} and
        C{schemaVersion} to determine the schema type.


        """
    @overload
    def RemoveAPI(self, schemaFamily: str | pxr.Ar.ResolvedPath, schemaVersion: int, instanceName: str | pxr.Ar.ResolvedPath) -> bool:
        """
        This is an overload of RemoveAPI with C{instanceName} that takes a
        C{schemaFamily} and C{schemaVersion} to determine the schema type.


        """
    def RemoveAppliedSchema(self, _appliedSchemaName: str | pxr.Ar.ResolvedPath, /) -> bool:
        """
        Removes the applied API schema name token C{appliedSchemaName} from
        the *apiSchemas* metadata for this prim at the current edit target.


        For multiple-apply schemas the name token should include the instance
        name for the applied schema, for example'CollectionAPI:plasticStuff'

        For an explicit list operation, this removes the applied schema name
        from the explicit items list if it was present. For a non-explicit
        list operation, this will remove any occurrence of the applied schema
        name from the prepended and appended item as well as adding it to the
        deleted items list.

        Returns true upon success or if the API schema is already deleted in
        the current edit target.

        An error is issued and false returned for any of the following
        conditions:
           - this prim is not a valid prim for editing

           - this prim is valid, but cannot be reached or overridden in the
             current edit target

           - the schema name cannot be deleted in the apiSchemas listOp
             metadata
             Unlike RemoveAPI this method does not require that the name token
             refer to a valid API schema type. RemoveAPI is the preferred method
             for removing valid API schemas.
        """
    def RemoveProperty(self, propName: str | pxr.Ar.ResolvedPath) -> bool:
        """
        Remove all scene description for the property with the given
        C{propName} *in the current UsdEditTarget*.


        Return true if the property is removed, false otherwise.

        Because this method can only remove opinions about the property from
        the current EditTarget, you may generally find it more useful to use
        UsdAttribute::Block() , which will ensure that all values from the
        EditTarget and weaker layers for the property will be ignored.
        """
    def SetActive(self, active: bool) -> bool:
        '''
        Author\'active\'metadata for this prim at the current EditTarget.


        See How"active"Affects Prims on a UsdStage for the effects of
        activating or deactivating a prim.
        '''
    def SetChildrenReorder(self, order: list[str] | list[pxr.Ar.ResolvedPath]) -> None:
        """
        Author an opinion for the metadata used to reorder children of this
        prim at the current EditTarget.
        """
    def SetInstanceable(self, instanceable: bool) -> bool:
        """
        Author'instanceable'metadata for this prim at the current EditTarget.
        """
    def SetKind(self, value: str | pxr.Ar.ResolvedPath) -> bool:
        """
        Author a C{kind} for this prim, at the current UsdEditTarget.



        true if C{kind} was successully authored, otherwise false.
        """
    @overload
    def SetPayload(self, payload: pxr.Sdf.Payload) -> bool:
        """
        Deprecated

        Author payload metadata for this prim at the current edit target.
        Return true on success, false if the value could not be set.

        Payloads: Impact of Using and Not Using
        """
    @overload
    def SetPayload(self, assetPath: str | pxr.Ar.ResolvedPath, primPath: pxr.Sdf.Path | str) -> bool:
        """
        Deprecated

        Shorthand for SetPayload(SdfPayload(assetPath, primPath)).
        """
    @overload
    def SetPayload(self, layer: pxr.Sdf.Layer, primPath: pxr.Sdf.Path | str) -> bool:
        """
        Deprecated

        Shorthand for SetPayload( SdfPayload (layer->GetIdentifier(),
        primPath)).
        """
    def SetPropertyOrder(self, order: list[str] | list[pxr.Ar.ResolvedPath]) -> None:
        """
        Author an opinion for propertyOrder metadata on this prim at the
        current EditTarget.
        """
    def SetSpecifier(self, specifier: pxr.Sdf.Specifier) -> bool:
        """
        Author an opinion for this Prim's specifier at the current edit
        target.
        """
    def SetTypeName(self, typeName: str | pxr.Ar.ResolvedPath) -> bool:
        """
        Author this Prim's typeName at the current EditTarget.
        """
    def Unload(self) -> None:
        """
        Unloads this prim and all its descendants.


        See UsdStage::Unload for additional details.
        """
    def _GetSourcePrimIndex(self) -> pxr.Pcp.PrimIndex: ...

class PrimCompositionQuery(Boost.Python.instance):
    """
    Object for making optionally filtered composition queries about a
    prim.


    It creates a list of strength ordering UsdPrimCompositionQueryArc that
    can be filtered by a combination of criteria and returned.

    Invalidation
    ============

    This object does not listen for change notification. If a consumer is
    holding on to a UsdPrimCompositionQuery, it is their responsibility to
    dispose of it in response to a resync change to the associated prim.
    Failing to do so may result in incorrect values or crashes due to
    dereferencing invalid objects.
    """

    class ArcIntroducedFilter(Boost.Python.enum):
        All: ClassVar[PrimCompositionQuery.ArcIntroducedFilter] = ...
        IntroducedInRootLayerPrimSpec: ClassVar[PrimCompositionQuery.ArcIntroducedFilter] = ...
        IntroducedInRootLayerStack: ClassVar[PrimCompositionQuery.ArcIntroducedFilter] = ...
        names: ClassVar[dict] = ...
        values: ClassVar[dict] = ...

    class ArcTypeFilter(Boost.Python.enum):
        All: ClassVar[PrimCompositionQuery.ArcTypeFilter] = ...
        Inherit: ClassVar[PrimCompositionQuery.ArcTypeFilter] = ...
        InheritOrSpecialize: ClassVar[PrimCompositionQuery.ArcTypeFilter] = ...
        NotInheritOrSpecialize: ClassVar[PrimCompositionQuery.ArcTypeFilter] = ...
        NotReferenceOrPayload: ClassVar[PrimCompositionQuery.ArcTypeFilter] = ...
        NotVariant: ClassVar[PrimCompositionQuery.ArcTypeFilter] = ...
        Payload: ClassVar[PrimCompositionQuery.ArcTypeFilter] = ...
        Reference: ClassVar[PrimCompositionQuery.ArcTypeFilter] = ...
        ReferenceOrPayload: ClassVar[PrimCompositionQuery.ArcTypeFilter] = ...
        Specialize: ClassVar[PrimCompositionQuery.ArcTypeFilter] = ...
        Variant: ClassVar[PrimCompositionQuery.ArcTypeFilter] = ...
        names: ClassVar[dict] = ...
        values: ClassVar[dict] = ...

    class DependencyTypeFilter(Boost.Python.enum):
        All: ClassVar[PrimCompositionQuery.DependencyTypeFilter] = ...
        Ancestral: ClassVar[PrimCompositionQuery.DependencyTypeFilter] = ...
        Direct: ClassVar[PrimCompositionQuery.DependencyTypeFilter] = ...
        names: ClassVar[dict] = ...
        values: ClassVar[dict] = ...

    class Filter(Boost.Python.instance):
        """
        Aggregate filter for filtering composition arcs by the previously
        defined criteria.
        """
        __instance_size__: ClassVar[int] = ...
        arcIntroducedFilter: Incomplete
        arcTypeFilter: Incomplete
        dependencyTypeFilter: Incomplete
        hasSpecsFilter: Incomplete
        def __init__(self) -> None: ...
        def __eq__(self, other: object) -> bool: ...
        def __ne__(self, other: object) -> bool: ...

    class HasSpecsFilter(Boost.Python.enum):
        All: ClassVar[PrimCompositionQuery.HasSpecsFilter] = ...
        HasNoSpecs: ClassVar[PrimCompositionQuery.HasSpecsFilter] = ...
        HasSpecs: ClassVar[PrimCompositionQuery.HasSpecsFilter] = ...
        names: ClassVar[dict] = ...
        values: ClassVar[dict] = ...
    filter: PrimCompositionQuery.Filter
    @overload
    def __init__(self, prim: Prim, filter: PrimCompositionQuery.Filter) -> None:
        """
        Create a prim composition query for the C{with} the given option
        C{filter}.
        """
    @overload
    def __init__(self, prim: Prim) -> None: ...
    def GetCompositionArcs(self) -> list[PrimCompositionQueryArc]:
        """
        Return a list of composition arcs for this query's prim using the
        current query filter.


        The composition arcs are always returned in order from strongest to
        weakest regardless of the filter.
        """
    @staticmethod
    def GetDirectInherits(_prim: Prim, /) -> PrimCompositionQuery:
        """
        Returns a prim composition query for the given C{prim} with a preset
        filter that only returns inherit arcs that are not ancestral.
        """
    @staticmethod
    def GetDirectReferences(_prim: Prim, /) -> PrimCompositionQuery:
        """
        Returns a prim composition query for the given C{prim} with a preset
        filter that only returns reference arcs that are not ancestral.
        """
    @staticmethod
    def GetDirectRootLayerArcs(_prim: Prim, /) -> PrimCompositionQuery:
        """
        Returns a prim composition query for the given C{prim} with a preset
        filter that only returns direct arcs that were introduced by opinions
        defined in a layer in the root layer stack.
        """

class PrimDefinition(Boost.Python.instance):
    """
    Class representing the builtin definition of a prim given the schemas
    registered in the schema registry.


    It provides access to the the builtin properties and metadata of a
    prim whose type is defined by this definition.

    Instances of this class can only be created by the UsdSchemaRegistry.
    """

    class Attribute(Property):
        """
        Accessor to a attribute's definition in the prim definition.


        These are returned by calls to
        UsdPrimDefinition::GetAttributeDefinition and can be freely converted
        to from a Property accessor. These can be used to check that a
        property exists and is an attribute (via conversion to bool) and to
        get attribute relevant field values that are defined for a property in
        the prim definition.

        This class is just a thin wrapper around the property representation
        in the UsdPrimDefinition that creates it and cannot be stored or
        accessed beyond the lifetime of the prim definition itself.
        """
        __instance_size__: ClassVar[int] = ...
        @overload
        def __init__(self) -> None:
            """
            Default constructor returns an invalid attribute.
            """
        @overload
        def __init__(self, property: PrimDefinition.Property) -> None:
            """
            Copy constructor from a Property to allow implicit conversion.
            """
        def GetFallbackValue(self) -> Any:
            """
            Retrieves the fallback value of type C{T} for this attribute and
            stores it in C{value} if possible.


            Returns true if this attribute has a fallback value defined with the
            expected type. Returns false otherwise.
            """
        def GetTypeName(self) -> pxr.Sdf.ValueTypeName:
            """
            Returns the value type name of this attribute in the prim definition.
            """
        def GetTypeNameToken(self) -> str:
            """
            Returns the token value of the type name of this attribute in the prim
            definition.
            """
        def __bool__(self) -> bool:
            """
            Conversion to bool returns true if this represents a valid property in
            the prim definition that is an attribute, and false otherwise.
            """

    class Property(Boost.Python.instance):
        """
        Accessor to a property's definition in the prim definition.


        These are returned by calls to
        UsdPrimDefinition::GetPropertyDefinition and can be used check the
        existence of a property (via conversion to bool) and get field values
        that a defined for a property in the prim definition.

        This class is just a thin wrapper around the property representation
        in the UsdPrimDefinition that creates it and cannot be stored or
        accessed beyond the lifetime of the prim definition itself.
        """
        __instance_size__: ClassVar[int] = ...
        def __init__(self) -> None:
            """
            Default constructor returns an invalid property.
            """
        def GetDocumentation(self) -> str:
            """
            Returns the documentation metadata defined by the prim definition for
            this property.
            """
        def GetMetadata(self, key: str | pxr.Ar.ResolvedPath) -> Any:
            """
            Retrieves the fallback value for the metadata field named C{key}, that
            is defined for this property in the prim definition, and stores it in
            C{value} if possible.


            Returns true if a value is defined for the given metadata C{key} for
            this property. Returns false otherwise.
            """
        def GetMetadataByDictKey(self, key: str | pxr.Ar.ResolvedPath, keyPath: str | pxr.Ar.ResolvedPath) -> Any:
            """
            Retrieves the value at C{keyPath} from the dictionary value for the
            dictionary metadata field named C{key}, that is defined for this
            property in the prim definition, and stores it in C{value} if
            possible.


            Returns true if a dictionary value is defined for the given metadata
            C{key} for this property and it contains a value at C{keyPath}.
            Returns false otherwise.
            """
        def GetName(self) -> str:
            """
            Returns the name of the requested property.


            Note that the return value of GetName gives no indication as to
            whether this is a valid property.
            """
        def GetSpecType(self) -> pxr.Sdf.SpecType:
            """
            Returns the spec type of this property in the prim definition.
            """
        def GetVariability(self) -> pxr.Sdf.Variability:
            """
            Returns the variability of this property in the prim definition.
            """
        def IsAttribute(self) -> bool:
            """
            Return true if the property is a valid is a valid property in the prim
            definition and is an attribute.
            """
        def IsRelationship(self) -> bool:
            """
            Return true if the property is a valid is a valid property in the prim
            definition and is a relationship.
            """
        def ListMetadataFields(self) -> list[str]:
            """
            Returns the list of names of metadata fields that are defined for this
            property in the prim definition.


            """
        def __bool__(self) -> bool:
            """
            Conversion to bool returns true if this represents a valid property in
            the prim definition, and false otherwise.
            """

    class Relationship(Property):
        """
        Accessor to a relationship's definition in the prim definition.


        These are returned by calls to
        UsdPrimDefinition::GetRelationshipDefinition and can be freely
        converted to from a Property accessor. These can be used to check that
        a property exists and is a relationship (via conversion to bool) and
        to get relationship relevant field values that are defined for a
        property in the prim definition.

        This class is just a thin wrapper around the property representation
        in the UsdPrimDefinition that creates it and cannot be stored or
        accessed beyond the lifetime of the prim definition itself.
        """
        __instance_size__: ClassVar[int] = ...
        @overload
        def __init__(self) -> None:
            """
            Default constructor returns an invalid relationship.
            """
        @overload
        def __init__(self, property: PrimDefinition.Property) -> None:
            """
            Copy constructor from a Property to allow implicit conversion.
            """
        def __bool__(self) -> bool:
            """
            Conversion to bool returns true if this represents a valid property in
            the prim definition that is a relationship, and false otherwise.
            """
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """
    @overload
    def FlattenTo(self, layer: pxr.Sdf.Layer, path: pxr.Sdf.Path | str, newSpecSpecifier: pxr.Sdf.Specifier = ...) -> bool:
        '''
        Copies the contents of this prim definition to a prim spec on the
        given C{layer} at the given C{path}.


        This includes the entire property spec for each of this definition\'s
        built-in properties as well as all of this definition\'s prim metadata.

        If the prim definition represents a concrete prim type, the type name
        of the prim spec is set to the the type name of this prim definition.
        Otherwise the type name is set to empty. The\'apiSchemas\'metadata on
        the prim spec will always be explicitly set to the combined list of
        all API schemas applied to this prim definition, i.e. the list
        returned by UsdPrimDefinition::GetAppliedAPISchemas. Note that if this
        prim definition is an API schema prim definition (see
        UsdSchemaRegistry::FindAppliedAPIPrimDefinition) then\'apiSchemas\'will
        be empty as this prim definition does not"have"an applied API because
        instead it"is"an applied API.

        If there is no prim spec at the given C{path}, a new prim spec is
        created at that path with the specifier C{newSpecSpecifier}. Any
        necessary ancestor specs will be created as well but they will always
        be created as overs. If a spec does exist at C{path}, then all of its
        properties and schema allowed metadata are cleared before it is
        populated from the prim definition.
        '''
    @overload
    def FlattenTo(self, parent: Prim, name: str | pxr.Ar.ResolvedPath, newSpecSpecifier: pxr.Sdf.Specifier = ...) -> Prim:
        """
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        Copies the contents of this prim definition to a prim spec at the
        current edit target for a prim with the given C{name} under the prim
        C{parent}.
        """
    @overload
    def FlattenTo(self, prim: Prim, newSpecSpecifier: pxr.Sdf.Specifier = ...) -> Prim:
        """
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        Copies the contents of this prim definition to a prim spec at the
        current edit target for the given C{prim}.
        """
    def GetAppliedAPISchemas(self) -> list[str]:
        """
        Return the list of names of the API schemas that have been applied to
        this prim definition in order.
        """
    def GetAttributeDefinition(self, attrName: str | pxr.Ar.ResolvedPath) -> PrimDefinition.Attribute:
        """
        Returns an attribute accessor the property named C{attrName} if it is
        defined by this this prim definition and is an attribute.


        If a property with the given name doesn't exist or exists but isn't an
        attribute, this will return an invalid Attribute.
        """
    def GetAttributeFallbackValue(self, attrName: str | pxr.Ar.ResolvedPath) -> Any:
        """
        Retrieves the fallback value for the attribute named C{attrName} and
        stores it in C{value} if possible.


        Returns true if the attribute exists in this prim definition and it
        has a fallback value defined. Returns false otherwise.
        """
    def GetDocumentation(self) -> str:
        """
        Returns the documentation metadata defined by the prim definition for
        the prim itself.
        """
    def GetMetadata(self, key: str | pxr.Ar.ResolvedPath) -> Any:
        """
        Retrieves the fallback value for the metadata field named C{key}, that
        is defined by this prim definition for the prim itself and stores it
        in C{value} if possible.


        Returns true if a fallback value is defined for the given metadata
        C{key}. Returns false otherwise.
        """
    def GetMetadataByDictKey(self, key: str | pxr.Ar.ResolvedPath, keyPath: str | pxr.Ar.ResolvedPath) -> Any:
        """
        Retrieves the value at C{keyPath} from the fallback dictionary value
        for the dictionary metadata field named C{key}, that is defined by
        this prim definition for the prim itself, and stores it in C{value} if
        possible.


        Returns true if a fallback dictionary value is defined for the given
        metadata C{key} and it contains a value at C{keyPath}. Returns false
        otherwise.
        """
    def GetPropertyDefinition(self, propName: str | pxr.Ar.ResolvedPath) -> PrimDefinition.Property:
        """
        Returns a property accessor the property named C{propName} if it is
        defined by this this prim definition.


        If a property with the given name doesn't exist, this will return an
        invalid Property.
        """
    def GetPropertyDocumentation(self, propName: str | pxr.Ar.ResolvedPath) -> str:
        """
        Returns the documentation metadata defined by the prim definition for
        the property named C{propName} if it exists.
        """
    def GetPropertyMetadata(self, propName: str | pxr.Ar.ResolvedPath, key: str | pxr.Ar.ResolvedPath) -> Any:
        """
        Retrieves the fallback value for the metadata field named C{key}, that
        is defined by this prim definition for the property named C{propName},
        and stores it in C{value} if possible.


        Returns true if a fallback value is defined for the given metadata
        C{key} for the named property. Returns false otherwise.
        """
    def GetPropertyMetadataByDictKey(self, propName: str | pxr.Ar.ResolvedPath, key: str | pxr.Ar.ResolvedPath, keyPath: str | pxr.Ar.ResolvedPath) -> Any:
        """
        Retrieves the value at C{keyPath} from the fallback dictionary value
        for the dictionary metadata field named C{key}, that is defined by
        this prim definition for the property named C{propName}, and stores it
        in C{value} if possible.


        Returns true if a fallback dictionary value is defined for the given
        metadata C{key} for the named property and it contains a value at
        C{keyPath}. Returns false otherwise.
        """
    def GetPropertyNames(self) -> list[str]:
        """
        Return the list of names of builtin properties for this prim
        definition.
        """
    def GetRelationshipDefinition(self, relName: str | pxr.Ar.ResolvedPath) -> PrimDefinition.Relationship:
        """
        Returns a relationship accessor the property named C{relName} if it is
        defined by this this prim definition and is a relationship.


        If a property with the given name doesn't exist or exists but isn't a
        relationship, this will return an invalid Relationship.
        """
    def GetSchemaAttributeSpec(self, attrName: str | pxr.Ar.ResolvedPath) -> pxr.Sdf.AttributeSpec:
        """
        Deprecated

        Use GetAttributeDefinition instead.

        This is a convenience method. It is shorthand for
        TfDynamic_cast<SdfAttributeSpecHandle>(GetSchemaPropertySpec(primType,
        attrName));
        """
    def GetSchemaPropertySpec(self, propName: str | pxr.Ar.ResolvedPath) -> pxr.Sdf.PropertySpec:
        """
        Deprecated

        Use GetPropertyDefinition instead.

        Return the property spec that defines the fallback for the property
        named *propName* on prims of this prim definition's type. Return null
        if there is no such property spec.
        """
    def GetSchemaRelationshipSpec(self, relName: str | pxr.Ar.ResolvedPath) -> pxr.Sdf.RelationshipSpec:
        """
        Deprecated

        Use GetRelationshipDefinition instead.

        This is a convenience method. It is shorthand for
        TfDynamic_cast<SdfRelationshipSpecHandle>(GetSchemaPropertySpec(primType,
        relName));
        """
    def GetSpecType(self, propName: str | pxr.Ar.ResolvedPath) -> pxr.Sdf.SpecType:
        """
        Return the SdfSpecType for C{propName} if it is a builtin property of
        the prim type represented by this prim definition.


        Otherwise return SdfSpecTypeUnknown.
        """
    def ListMetadataFields(self) -> list[str]:
        """
        Returns the list of names of metadata fields that are defined by this
        prim definition for the prim itself.
        """
    def ListPropertyMetadataFields(self, _propName: str | pxr.Ar.ResolvedPath, /) -> list[str]:
        """
        Returns the list of names of metadata fields that are defined by this
        prim definition for property C{propName} if a property named
        C{propName} exists.
        """

class PrimRange(Boost.Python.instance):
    '''
    An forward-iterable range that traverses a subtree of prims rooted at
    a given prim in depth-first order.


    In addition to depth-first order, UsdPrimRange provides the optional
    ability to traverse in depth-first pre- and post-order wher prims
    appear twice in the range; first before all descendants and then again
    immediately after all descendants. This is useful for maintaining
    state associated with subtrees, in a stack-like fashion. See
    UsdPrimRange::iterator::IsPostVisit() to detect when an iterator is
    visiting a prim for the second time.

    There are several constructors providing different levels of
    configurability; ultimately, one can provide a prim predicate for a
    custom iteration, just as one would use UsdPrim::GetFilteredChildren()
    in a custom recursion.

    Why would one want to use a UsdPrimRange rather than just iterating
    over the results of UsdPrim::GetFilteredDescendants() ? Primarily, if
    one of the following applies:
       - You need to perform pre-and-post-order processing

       - You may want to prune sub-trees from processing (see
         UsdPrimRange::iterator::PruneChildren() )

       - You want to treat the root prim itself uniformly with its
         descendents (GetFilteredDescendants() will not return the root prim
         itself, while UsdPrimRange will - see UsdPrimRange::Stage for an
         exception).
         B{Using UsdPrimRange in C++}

    UsdPrimRange provides standard container-like semantics. For example:
    ::

      // simple range-for iteration
      for (UsdPrim prim: UsdPrimRange(rootPrim)) {
          ProcessPrim(prim);
      }
  
      // using stl algorithms
      std::vector<UsdPrim> meshes;
      auto range = stage->Traverse();
      std::copy_if(range.begin(), range.end(), std::back_inserter(meshes),
                   [](UsdPrim const &) { return prim.IsA<UsdGeomMesh>(); });
  
      // iterator-based iterating, with subtree pruning
      UsdPrimRange range(rootPrim);
      for (auto iter = range.begin(); iter != range.end(); ++iter) {
          if (UsdModelAPI(*iter).GetKind() == KindTokens->component) {
              iter.PruneChildren();
          }
          else {
              nonComponents.push_back(*iter);
          }
      }

    B{Using Usd.PrimRange in python}

    The python wrapping for PrimRange is python-iterable, so it can used
    directly as the object of a"for x in..."clause; however in that usage
    one loses access to PrimRange methods such as PruneChildren() and
    IsPostVisit(). Simply create the iterator outside the loop to overcome
    this limitation. Finally, in python, prim predicates must be combined
    with bit-wise operators rather than logical operators because the
    latter are not overridable. ::

      # simple iteration
      for prim in Usd.PrimRange(rootPrim):
          ProcessPrim(prim)
  
      # filtered range using iterator to invoke iterator methods
      it = iter(Usd.PrimRange.Stage(stage, Usd.PrimIsLoaded  &  ~Usd.PrimIsAbstract))
      for prim in it:
          if Usd.ModelAPI(prim).GetKind() == Kind.Tokens.component:
              it.PruneChildren()
          else:
              nonComponents.append(prim)

    Finally, since iterators in python are not directly dereferencable, we
    provide the *python* *only* methods GetCurrentPrim() and IsValid(),
    documented in the python help system.
    '''

    class _Iterator(Boost.Python.instance):
        def __init__(self, *args, **kwargs) -> None:
            """Raises an exception
            This class cannot be instantiated from Python
            """
        def GetCurrentPrim(self) -> Prim:
            """Since an iterator cannot be dereferenced in python, GetCurrentPrim()
             performs the same function: yielding the currently visited prim."""
        def IsPostVisit(self) -> bool: ...
        def IsValid(self) -> bool:
            """true if the iterator is not yet exhausted"""
        def PruneChildren(self) -> None: ...
        def __iter__(self) -> typing_extensions.Self: ...
        def __next__(self) -> Prim: ...
    @overload
    def __init__(self, root: Prim) -> None:
        """
        Construct a PrimRange that traverses the subtree rooted at C{start} in
        depth-first order, visiting prims that pass the default predicate (as
        defined by UsdPrimDefaultPredicate).
        """
    @overload
    def __init__(self, root: Prim, predicate: _PrimFlagsPredicate | _Term) -> None:
        """
        Construct a PrimRange that traverses the subtree rooted at C{start} in
        depth-first order, visiting prims that pass C{predicate}.
        """
    @staticmethod
    def AllPrims(root: Prim) -> PrimRange:
        """
        Construct a PrimRange that traverses the subtree rooted at C{start} in
        depth-first order, visiting all prims (including deactivated,
        undefined, and abstract prims).
        """
    @staticmethod
    def AllPrimsPreAndPostVisit(root: Prim) -> PrimRange:
        """
        Construct a PrimRange that traverses the subtree rooted at C{start} in
        depth-first order, visiting all prims (including deactivated,
        undefined, and abstract prims) with pre- and post-order visitation.


        Pre- and post-order visitation means that each prim appears twice in
        the range; not only prior to all its descendants as with an ordinary
        traversal but also immediately following its descendants. This lets
        client code maintain state for subtrees. See
        UsdPrimRange::iterator::IsPostVisit() .
        """
    def IsValid(self) -> bool:
        """true if the iterator is not yet exhausted"""
    @overload
    @staticmethod
    def PreAndPostVisit(root: Prim) -> PrimRange:
        """
        Create a PrimRange that traverses the subtree rooted at C{start} in
        depth-first order, visiting prims that pass the default predicate (as
        defined by UsdPrimDefaultPredicate) with pre- and post-order
        visitation.


        Pre- and post-order visitation means that each prim appears twice in
        the range; not only prior to all its descendants as with an ordinary
        traversal but also immediately following its descendants. This lets
        client code maintain state for subtrees. See
        UsdPrimRange::iterator::IsPostVisit() .
        """
    @overload
    @staticmethod
    def PreAndPostVisit(root: Prim, predicate: _PrimFlagsPredicate | _Term) -> PrimRange:
        """
        Create a PrimRange that traverses the subtree rooted at C{start} in
        depth-first order, visiting prims that pass C{predicate} with pre- and
        post-order visitation.


        Pre- and post-order visitation means that each prim appears twice in
        the range; not only prior to all its descendants as with an ordinary
        traversal but also immediately following its descendants. This lets
        client code maintain state for subtrees. See
        UsdPrimRange::iterator::IsPostVisit() .
        """
    @overload
    @staticmethod
    def Stage(stage: Stage, predicate: _PrimFlagsPredicate | _Term) -> PrimRange:
        """
        Create a PrimRange that traverses all the prims on C{stage}, and
        visits those that pass the default predicate (as defined by
        UsdPrimDefaultPredicate).
        """
    @overload
    @staticmethod
    def Stage(stage: Stage) -> PrimRange: ...
    def __bool__(self) -> bool:
        """
        Return true if this range contains one or more prims, false otherwise.
        """
    def __eq__(self, other: object) -> bool:
        """
        Return true if this range is equivalent to C{other}.
        """
    def __iter__(self) -> _Iterator: ...
    def __ne__(self, other: object) -> bool: ...

class PrimTypeInfo(Boost.Python.instance):
    '''
    Class that holds the full type information for a prim.


    It holds the type name, applied API schema names, and possibly a
    mapped schema type name which represent a unique full type. The info
    this holds is used to cache and provide the"real"schema type for the
    prim\'s type name regardless of whether it is a recognized prim type or
    not. The optional"mapped schema type name"is used to obtain a valid
    schema type for an unrecognized prim type name if the stage provides a
    fallback type for the unrecognized type. This class also provides
    access to the prim definition that defines all the built-in properties
    and metadata of a prim of this type.
    '''
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """
    def GetAppliedAPISchemas(self) -> list[str]:
        """
        Returns the list of applied API schemas, directly authored on the
        prim, that impart additional properties on its prim definition.


        This does NOT include the applied API schemas that may be defined in
        the conrete prim type's prim definition..
        """
    @staticmethod
    def GetEmptyPrimType() -> PrimTypeInfo:
        """
        Returns the empty prim type info.
        """
    def GetPrimDefinition(self) -> PrimDefinition:
        """
        Returns the prim definition associated with this prim type's schema
        type and applied API schemas.
        """
    def GetSchemaType(self) -> pxr.Tf.Type:
        """
        Returns the TfType of the actual concrete schema that prims of this
        type will use to create their prim definition.


        Typically, this will be the type registered in the schema registry for
        the concrete prim type returned by GetTypeName. But if the stage
        provided this type info with a fallback type because the prim type
        name is not a recognized schema, this will return the provided
        fallback schema type instead.

        Fallback Prim Types
        """
    def GetSchemaTypeName(self) -> str:
        """
        Returns the type name associated with the schema type returned from
        GetSchemaType.


        This will always be equivalent to calling
        UsdSchemaRegistry::GetConcreteSchemaTypeName on the type returned by
        GetSchemaType and will typically be the same as GetTypeName as long as
        the prim type name is a recognized prim type.

        Fallback Prim Types
        """
    def GetTypeName(self) -> str:
        """
        Returns the concrete prim type name.
        """
    def __eq__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...

class Property(Object):
    """
    Base class for UsdAttribute and UsdRelationship scenegraph objects.


    UsdProperty has a bool conversion operator that validates that the
    property IsDefined() and thus valid for querying and authoring values
    and metadata. This is a fairly expensive query that we do B{not}
    cache, so if client code retains UsdProperty objects it should manage
    its object validity closely for performance. An ideal pattern is to
    listen for UsdNotice::StageContentsChanged notifications, and
    revalidate/refetch retained UsdObjects only then and otherwise use
    them without validity checking.
    """
    __instance_size__: ClassVar[int] = ...
    def __init__(self) -> None:
        """
        Construct an invalid property.
        """
    def ClearDisplayGroup(self) -> bool:
        """
        Clears this property's display group (metadata) in the current
        EditTarget (only).


        Returns true on success.
        """
    @overload
    def FlattenTo(self, parent: Prim) -> Property:
        """
        Flattens this property to a property spec with the same name beneath
        the given C{parent} prim in the edit target of its owning stage.


        The C{parent} prim may belong to a different stage than this
        property's owning stage.

        Flattening authors all authored resolved values and metadata for this
        property into the destination property spec. If this property is a
        builtin property, fallback values and metadata will also be authored
        if the destination property has a different fallback value or no
        fallback value, or if the destination property has an authored value
        that overrides its fallback.

        Attribute connections and relationship targets that target an object
        beneath this property's owning prim will be remapped to target objects
        beneath the destination C{parent} prim.

        If the destination spec already exists, it will be overwritten.

        UsdStage::Flatten
        """
    @overload
    def FlattenTo(self, parent: Prim, propName: str | pxr.Ar.ResolvedPath) -> Property:
        """
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        Flattens this property to a property spec with the given C{propName}
        beneath the given C{parent} prim in the edit target of its owning
        stage.


        The C{parent} prim may belong to a different stage than this
        property's owning stage.
        """
    @overload
    def FlattenTo(self, property: Property | pxr.UsdGeom.XformOp) -> Property:
        """
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        Flattens this property to a property spec for the given C{property} in
        the edit target of its owning prim's stage.


        The C{property} owning prim may belong to a different stage than this
        property's owning stage.
        """
    def GetBaseName(self) -> str:
        '''
        Return this property\'s name with all namespace prefixes removed, i.e.


        the last component of the return value of GetName()

        This is generally the property\'s"client name"; property namespaces are
        often used to group related properties together. The namespace
        prefixes the property name but many consumers will care only about un-
        namespaced name, i.e. its BaseName. For more information, see Names,
        Namespace Ordering, and Property Namespaces
        '''
    def GetDisplayGroup(self) -> str:
        """
        Return this property's display group (metadata).


        This returns the empty token if no display group has been set.

        SetDisplayGroup()
        """
    def GetNamespace(self) -> str:
        """
        Return this property's complete namespace prefix.


        Return the empty token if this property has no namespaces.

        This is the complement of GetBaseName() , although it does *not*
        contain a trailing namespace delimiter
        """
    def GetNestedDisplayGroups(self) -> list[str]:
        """
        Return this property's displayGroup as a sequence of groups to be
        nested, or an empty vector if displayGroup is empty or not authored.
        """
    def GetPropertyStack(self, time: TimeCode | float | pxr.Sdf.TimeCode = ...) -> list[pxr.Sdf.PropertySpec]:
        """
        Returns a strength-ordered list of property specs that provide
        opinions for this property.


        If C{time} is UsdTimeCode::Default() , *or* this property is a
        UsdRelationship (which are never affected by clips), we will not
        consider value clips for opinions. For any other C{time}, for a
        UsdAttribute, clips whose samples may contribute an opinion will be
        included. These specs are ordered from strongest to weakest opinion,
        although if C{time} requires interpolation between two adjacent clips,
        both clips will appear, sequentially.

        The results returned by this method are meant for debugging and
        diagnostic purposes. It is B{not} advisable to retain a PropertyStack
        for the purposes of expedited value resolution for properties, since
        the makeup of an attribute's PropertyStack may itself be time-varying.
        To expedite repeated value resolution of attributes, you should
        instead retain a C{UsdAttributeQuery}.

        UsdClipsAPI
        """
    def GetPropertyStackWithLayerOffsets(self, time: TimeCode | float | pxr.Sdf.TimeCode = ...) -> list[tuple[pxr.Sdf.PropertySpec, pxr.Sdf.LayerOffset]]:
        """
        Returns a strength-ordered list of property specs that provide
        opinions for this property paired with the cumulative layer offset
        from the stage's root layer to the layer containing the property spec.


        This behaves exactly the same as UsdProperty::GetPropertyStack with
        the addition of providing the cumulative layer offset of each spec's
        layer.

        The results returned by this method are meant for debugging and
        diagnostic purposes. It is B{not} advisable to retain a PropertyStack
        for the purposes of expedited value resolution for properties, since
        the makeup of an attribute's PropertyStack may itself be time-varying.
        To expedite repeated value resolution of attributes, you should
        instead retain a C{UsdAttributeQuery}.
        """
    def HasAuthoredDisplayGroup(self) -> bool:
        """
        Returns true if displayGroup was explicitly authored and GetMetadata()
        will return a meaningful value for displayGroup.


        """
    def IsAuthored(self) -> bool:
        """
        Return true if there are any authored opinions for this property in
        any layer that contributes to this stage, false otherwise.
        """
    def IsAuthoredAt(self, editTarget: EditTarget | pxr.Sdf.Layer) -> bool:
        """
        Return true if there is an SdfPropertySpec authored for this property
        at the given *editTarget*, otherwise return false.


        Note that this method does not do partial composition. It does not
        consider whether authored scene description exists at *editTarget* or
        weaker, only B{exactly at} the given *editTarget*.
        """
    def IsCustom(self) -> bool:
        """
        Return true if this is a custom property (i.e., not part of a prim
        schema).


        The'custom'modifier in USD serves the same function as
        Alembic's'userProperties', which is to say as a categorization for ad
        hoc client data not formalized into any schema, and therefore not
        carrying an expectation of specific processing by consuming
        applications.
        """
    def IsDefined(self) -> bool:
        """
        Return true if this is a builtin property or if the strongest authored
        SdfPropertySpec for this property's path matches this property's
        dynamic type.


        That is, SdfRelationshipSpec in case this is a UsdRelationship, and
        SdfAttributeSpec in case this is a UsdAttribute. Return C{false} if
        this property's prim has expired.

        For attributes, a C{true} return does not imply that this attribute
        possesses a value, only that has been declared, is of a certain type
        and variability, and that it is safe to use to query and author values
        and metadata.
        """
    def SetCustom(self, isCustom: bool) -> bool:
        """
        Set the value for custom at the current EditTarget, return true on
        success, false if the value can not be written.


        B{Note} that this value should not be changed as it is typically
        either automatically authored or provided by a property definition.
        This method is provided primarily for fixing invalid scene
        description.
        """
    def SetDisplayGroup(self, displayGroup: str | pxr.Ar.ResolvedPath) -> bool:
        """
        Sets this property's display group (metadata).


        Returns true on success.

        DisplayGroup provides UI hinting for grouping related properties
        together for display. We define a convention for specifying nesting of
        groups by recognizing the property namespace separator in displayGroup
        as denoting group-nesting.

        SetNestedDisplayGroups()
        """
    def SetNestedDisplayGroups(self, nestedGroups: typing.Iterable[str | pxr.Ar.ResolvedPath]) -> bool:
        """
        Sets this property's display group (metadata) to the nested sequence.


        Returns true on success.

        A displayGroup set with this method can still be retrieved with
        GetDisplayGroup() , with the namespace separator embedded in the
        result. If C{nestedGroups} is empty, we author an empty string for
        displayGroup.

        SetDisplayGroup()
        """
    def SplitName(self) -> list[str]:
        """
        Return this property's name elements including namespaces and its base
        name as the final element.
        """

class References(Boost.Python.instance):
    '''
    UsdReferences provides an interface to authoring and introspecting
    references in Usd.


    References are the primary operator for"encapsulated aggregation"of
    scene description. *aggregation* means that references let us build up
    rich scenes by composing scene description recorded in a (most often)
    different layer. A scene can reference the same layer many times at
    different locations in a scene\'s namespace. Referenced scene
    description can be overridden in the referencing (or stronger) layers,
    allowing each instance of the reference to be directly
    customized/overridden. *Encapsulated* means that regardless of how
    much scene description is in the referenced layer, only the scene
    description under and composed from (via other composition arcs in the
    referenced layer) the targeted prim will be composed into the
    aggregate scene. Multiple references to the same layer will result in
    the layer being opened and retained in memory only once, although each
    referencing prim will compose unique prim indices for the tree rooted
    at the referenced prim.

    Important Qualities and Effective Use of References
    ===================================================

       - Any prim can host zero, one or multiple references

       - References are list editable; that is, they compose differently
         than ordinary properties and metadata. In any given LayerStack, each
         authored reference operation at the same SdfPath location in each
         layer (i.e. on the same prim) will compose into an aggregate result by
         adding to, removing from, or replacing"weaker"references.

       - References can target the same LayerStack in which they are
         authored, as long as doing so does not introduce a cycle in the
         composition graph. See Expressing"internal"references to the
         containing LayerStack

       - The C{identifier} component of a reference in the provided API
         can be a resolvable asset-path to some external layer, empty, in which
         case the reference targets the root layer of the LayerStack containing
         the referencing layer, or the identifier of an existing anonymous, in-
         memory-only SdfLayer. Care should be exercised in the latter case:
         calling Export() on an anonymous layer to serialize it to a file will
         not attempt to replace any references to anonymous layers with
         references to file-backed layers.

       - Opinions brought in by reference on an ancestor prim are weaker
         than opinions brought in by references on a descendant prim.

    References may omit the target prim path if the referenced layer has
    the\'defaultPrim\'metadata set. In this case, the reference targets
    the\'defaultPrim\'in the referenced layer. A layer\'s defaultPrim can be
    authored and accessed on a UsdStage whose root layer is the layer in
    question: see UsdStage::GetDefaultPrim() and
    UsdStage::SetDefaultPrim() . One can also author defaultPrim directly
    on an SdfLayer - see SdfLayer::GetDefaultPrim() ,
    SdfLayer::SetDefaultPrim() .

    References may omit the identifier specifying the referenced layer.
    This creates an"internal"reference. During composition, the referenced
    layer will be resolved to the root layer of the LayerStack containing
    the layer where the reference was authored. See AddInternalReference()
    .

    References may target any prim in a layer. In the simplest and most
    common case, a root prim in a layer will be referenced. However,
    referencing sub-root prims can be useful in a variety of other cases;
    for example, a user might organize prims into a meaningful hierarchy
    in a layer for display purposes, then use sub-root references to
    reference a selection from that hierarchy into a scene.

    Sub-root references have subtle behaviors with respect to opinions and
    composition arcs authored on ancestors of the referenced prim. Users
    should carefully consider this when deciding whether to use sub-root
    references. These issues can be avoided by not authoring any
    properties or metadata on ancestors of prims that are meant to be
    referenced.

    Consider the following example: ::

      * shot.usda                                 | * asset.usda
                                                  |
      #usda 1.0                                   | #usda 1.0
                                                  |
      over "Class"                                | class "Class"
      {                                           | {
          over "B"                                | }
          {                                       |
              over "Model"                        | def "A" (
              {                                   |    inherits = </Class>
                  int a = 3                       | )
              }                                   | {
          }                                       |     token purpose = "render"
      }                                           |
                                                  |     def "B" (
      over "A"                                    |        variantSets = "type"
      {                                           |        variants = {
          over "B" (                              |             string type = "a"
              # variant selection won\'t be used   |        }
              variants = {                        |     )
                  string type = "b"               |     {
              }                                   |         variantSet "type" = {
          )                                       |             "a" {
          {                                       |                 def "Model"
          }                                       |                 {
      }                                           |                     int a = 1
                                                  |                 }
      def "ReferencedModel" (                     |             }
          references = @./asset.usda@</A/B/Model> |             "b" {
      )                                           |                 def "Model"
      {                                           |                 {
      }                                           |                     int a = 2
                                                  |                 }
                                                  |             }
                                                  |         }
                                                  |     }
                                                  | }

       - Property and metadata opinions on the ancestors of the referenced
         prim *are not* present in the composed stage and will never contribute
         to any computations. In this example, the opinion for the attribute
         /A.purpose in asset.usda will never be visible in the UsdStage for
         shot.usda.

       - Property and metadata opinions due to ancestral composition arcs
         *are* present in the composed stage. In this example, the attribute
         /Class/B/Model.a in shot.usda will be present in the UsdStage for
         shot.usda, even though the inherit arc is authored on an ancestor of
         the referenced prim.

       - A consequence of these rules is that users might not be able to
         override ancestral variant selections that affect the referenced prim.
         In this example, the Model prim being referenced comes from the
         variant selection {type=a} on prim /A/B in asset.usda. The {type=b}
         variant cannot be selected in shot.usda, even if prims with the same
         hierarchy happen to exist there. There are various workarounds for
         this; in this example, the {type=b} variant selection could be
         authored on /Class/B/Model in shot.usda instead because of the inherit
         arc that was established on prim /A.

    AddReference() and SetReferences() can each fail for a number of
    reasons. If one of the specified prim targets for one of the
    references is not a prim, we will generate an error, fail to author
    any scene description, and return C{false}. If anything goes wrong in
    attempting to write the reference, we also return false, and the
    reference will also remain unauthored. Otherwise, if the reference was
    successfully authored, we will return C{true}. B{A successful
    reference authoring operation may still generate composition errors!}
    Just because the reference you specified was syntactically correct and
    therefore successfully authored, does not imply it was meaningful. If
    you wish to ensure that the reference you are about to author will be
    meaningfully consumable by your stage, you are strongly encouraged to
    B{ensure it will resolve to an actual file by using
    UsdStage::ResolveIdentifierToEditTarget() before authoring the
    reference.}

    When adding an internal reference, the given prim path is expected to
    be in the namespace of the owning prim\'s stage. Sub-root prim paths
    will be translated from this namespace to the namespace of the current
    edit target, if necessary. If a path cannot be translated, a coding
    error will be issued and no changes will be made. Non-sub-root paths
    will not be translated.

    Immediately upon successful authoring of the reference (before
    returning from AddReference() , RemoveReference() , ClearReferences()
    , or SetReferences() ), the UsdStage on which the reference was
    authored will recompose the subtree rooted at the prim hosting the
    reference. If the provided identifier does not resolve to a layer that
    is already opened or that can be opened in the usd format, *or* if the
    provided primPath is not an actual prim in that layer, the stage\'s
    recomposition will fail, and pass on composition errors to the client.
    '''
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """
    def AddInternalReference(self, primPath: pxr.Sdf.Path | str, layerOffset: pxr.Sdf.LayerOffset = ..., position: ListPosition = ...) -> bool:
        """
        Add an internal reference to the specified prim.



        Internal References
        """
    @overload
    def AddReference(self, ref: pxr.Sdf.Reference, position: ListPosition = ...) -> bool:
        """
        Adds a reference to the reference listOp at the current EditTarget, in
        the position specified by C{position}.



        Why adding references may fail for explanation of expectations on
        C{ref} and what return values and errors to expect, and ListOps and
        List Editing for details on list editing and composition of listOps.
        """
    @overload
    def AddReference(self, assetPath: str | pxr.Ar.ResolvedPath, primPath: pxr.Sdf.Path | str, layerOffset: pxr.Sdf.LayerOffset = ..., position: ListPosition = ...) -> bool:
        """
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        """
    @overload
    def AddReference(self, assetPath: str | pxr.Ar.ResolvedPath, layerOffset: pxr.Sdf.LayerOffset = ..., position: ListPosition = ...) -> bool:
        """
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.



        References Without Prim Paths
        """
    def ClearReferences(self) -> bool:
        '''
        Removes the authored reference listOp edits at the current EditTarget.


        The same caveats for Remove() apply to Clear(). In fact, Clear() may
        actually increase the number of composed references, if the listOp
        being cleared contained the"remove"operator.

        ListOps and List Editing
        '''
    def GetPrim(self) -> Prim:
        """
        Return the prim this object is bound to.
        """
    def RemoveReference(self, ref: pxr.Sdf.Reference) -> bool:
        """
        Removes the specified reference from the references listOp at the
        current EditTarget.


        This does not necessarily eliminate the reference completely, as it
        may be added or set in another layer in the same LayerStack as the
        current EditTarget.

        ListOps and List Editing
        """
    def SetReferences(self, _items: list[pxr.Sdf.Reference], /) -> bool:
        """
        Explicitly set the references, potentially blocking weaker opinions
        that add or remove items.



        Why adding references may fail for explanation of expectations on
        C{ref} and what return values and errors to expect, and ListOps and
        List Editing for details on list editing and composition of listOps.
        """
    def __bool__(self) -> bool: ...

class Relationship(Property):
    '''
    A UsdRelationship creates dependencies between scenegraph objects by
    allowing a prim to *target* other prims, attributes, or relationships.


    Relationship Characteristics
    ============================

    A UsdRelationship is a pointer to other objects, which are named by
    their scenegraph paths. When authoring relationships, the *target*
    parameters should be scenegraph paths in the composed namespace of the
    UsdStage into which you are authoring. If your edits are targeted to a
    different layer, across various composition arcs (because you
    specified a non-default UsdEditTarget), the target\'s path will be
    automatically translated into the proper namespace.

    A single UsdRelationship can target multiple other objects, which can
    be of UsdPrim, UsdAttribute, or UsdRelationship type. UsdRelationship
    participates in"list editing", which means that stronger layers in a
    composed scene can add, remove, or reorder targets authored on the
    relationship in weaker layers *without* stomping the weaker opinions,
    although stomping behavior is still possible, via SetTargets() .

    An authored relationship creates a dependency of the targeting prim on
    the targeted prim(s). We consider these dependencies to
    be"loaddependencies", which means that when we load the targeting
    prim\'s"load group", we will also load the targeted prims\'load groups,
    to ensure that all the data required to render the model containing
    the targeting prim is composed and available.

    Like UsdAttribute, UsdRelationship objects are meant to be ephemeral,
    live on the stack, and be cheap to refetch from their owning UsdPrim.

    Unlike UsdAttribute s, which can either be uniform over all time or
    vary in value over time, UsdRelationship is B{always uniform}.

    Relationship Restrictions
    =========================

    When authoring relationship targets in a stage\'s local LayerStack, all
    target paths are legal (Note we may restrict this prior to launch to
    only allowing targeting of already-extant scenegraph objects).
    However, a relationship target that is legal in a local LayerStack may
    become unreachable when the stage\'s root layer is *referenced* into an
    aggregate, and will cause an error when attempting to load/compose the
    aggregate.

    This can happen because references encapsulate just the tree whose
    root is targeted in the reference - no other scene description in the
    referenced layer will be composed into the aggregate. So if some
    descendant prim of the referenced root targets a relationship to
    another tree in the same layer, that relationship would dangle, and
    the client will error in GetTargets() or GetForwardedTargets() .

    Authoring targets to objects within prototypes is not allowed, since
    prototype prims do not have a stable identity across runs. Consumers
    must author targets to the object within an instance instead.

    Relationships authored in a descendent prim of a referenced prim may
    not target the referenced prim itself or any of its immediate child
    properties if the referencing prim is instanceable. Allowing this
    would break the ability for this relationship to be instanced and
    shared by multiple instances  it would force consumers of
    relationships within prototypes to resolve targets in the context of
    each of that prototype\'s instances.

    Relationship Forwarding
    =======================

    Because a relationship can target another relationship, we can and do
    provide the ability to resolve chained or *forwarded* relationships.
    This can be useful in several situations, including:

       - Combining relationships with VariantSets to create
         demultiplexers. A prim can host a relationship that serves as
         a"binding post"for other prims to target. The prim also hosts
         a"bindingVariant" UsdVariantSet whose variants each modulate the
         target of the binding-post relationship. We can now change the
         *forwarded* target of all prims targeting the binding-post by simply
         switching the bindingVariant VariantSet. We will work through this
         example in the USD reference manual.

       - Defining a relationship as part of a model\'s interface (so that
         it can be targeted in model hierarchy with no models loaded), which,
         inside the model\'s payload, forwards to prims useful to a client, the
         set of which may vary depending on the model\'s configured VariantSets.

    '''
    __instance_size__: ClassVar[int] = ...
    def __init__(self) -> None:
        """
        Construct an invalid relationship.
        """
    def AddTarget(self, target: pxr.Sdf.Path | str, position: ListPosition = ...) -> bool:
        """
        Adds C{target} to the list of targets, in the position specified by
        C{position}.


        Passing paths to prototype prims or any other objects in prototypes
        will cause an error to be issued. It is not valid to author targets to
        these objects.

        What data this actually authors depends on what data is currently
        authored in the authoring layer, with respect to list-editing
        semantics, which we will document soon
        """
    def ClearTargets(self, removeSpec: bool) -> bool:
        """
        Remove all opinions about the target list from the current edit
        target.


        Only remove the spec if C{removeSpec} is true (leave the spec to
        preserve meta-data we may have intentionally authored on the
        relationship)
        """
    def GetForwardedTargets(self) -> list[pxr.Sdf.Path]:
        '''
        Compose this relationship\'s *ultimate* targets, taking into
        account"relationship forwarding", and fill C{targets} with the result.


        All preexisting elements in C{targets} are lost. This method never
        inserts relationship paths in C{targets}.

        Returns true if any of the visited relationships that are not"purely
        forwarding"has an authored opinion for its target paths and no
        composition errors were encountered while computing any targets.
        Purely forwarding, in this context, means the relationship has at
        least one target but all of its targets are paths to other
        relationships. Note that authored opinions may include opinions that
        clear the targets and a return value of true does not necessarily
        indicate that C{targets} will not be empty.

        Returns false otherwise. When composition errors occur, this function
        continues to collect successfully composed targets, but returns false
        to indicate to the caller that errors occurred.

        When a forwarded target cannot be determined, e.g. due to a
        composition error, no value is returned for that target; the
        alternative would be to return the relationship path at which the
        forwarded targets could not be composed, however this would require
        all callers of GetForwardedTargets() to account for unexpected
        relationship paths being returned with the expected target results.
        For example, a particular caller may expect only prim paths in the
        target vector, but when composition errors occur, relationships would
        be included, potentially triggering additional down stream errors.

        See Relationship Forwarding for details on the semantics.

        The result is not cached, so will be recomputed on every query.
        '''
    def GetTargets(self) -> list[pxr.Sdf.Path]:
        """
        Compose this relationship's targets and fill C{targets} with the
        result.


        All preexisting elements in C{targets} are lost.

        Returns true if any target path opinions have been authored and no
        composition errors were encountered, returns false otherwise. Note
        that authored opinions may include opinions that clear the targets and
        a return value of true does not necessarily indicate that C{targets}
        will contain any target paths.

        See Relationship Targets and Attribute Connections for details on
        behavior when targets point to objects beneath instance prims.

        The result is not cached, so will be recomputed on every query.
        """
    def HasAuthoredTargets(self) -> bool:
        """
        Returns true if any target path opinions have been authored.


        Note that this may include opinions that clear targets and may not
        indicate that target paths will exist for this relationship.
        """
    def RemoveTarget(self, target: pxr.Sdf.Path | str) -> bool:
        """
        Removes C{target} from the list of targets.


        Passing paths to prototype prims or any other objects in prototypes
        will cause an error to be issued. It is not valid to author targets to
        these objects.
        """
    def SetTargets(self, targets: typing.Iterable[pxr.Sdf.Path | str]) -> bool:
        """
        Make the authoring layer's opinion of the targets list explicit, and
        set exactly to C{targets}.


        Passing paths to prototype prims or any other objects in prototypes
        will cause an error to be issued. It is not valid to author targets to
        these objects.

        If any target in C{targets} is invalid, no targets will be authored
        and this function will return false.
        """

class ResolveInfo(Boost.Python.instance):
    """
    Container for information about the source of an attribute's value,
    i.e.


    the'resolved'location of the attribute.

    For more details, see TimeSamples, Defaults, and Value Resolution.
    """
    __instance_size__: ClassVar[int] = ...
    def __init__(self) -> None: ...
    def GetNode(self) -> pxr.Pcp.NodeRef:
        """
        Return the node within the containing PcpPrimIndex that provided the
        resolved value opinion.
        """
    def GetSource(self) -> ResolveInfoSource:
        """
        Return the source of the associated attribute's value.
        """
    def ValueIsBlocked(self) -> bool:
        """
        Return true if this UsdResolveInfo represents an attribute whose value
        is blocked.



        UsdAttribute::Block()
        """

class ResolveInfoSource(pxr.Tf.Tf_PyEnumWrapper):
    _baseName: ClassVar[str] = ...
    allValues: ClassVar[tuple] = ...
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def GetValueFromName(name: object) -> Any: ...

class ResolveTarget(Boost.Python.instance):
    """
    Defines a subrange of nodes and layers within a prim's prim index to
    consider when performing value resolution for the prim's attributes.


    A resolve target can then be passed to UsdAttributeQuery during its
    construction to have all of the queries made by the UsdAttributeQuery
    use the resolve target's subrange for their value resolution.

    Resolve targets can be created via methods on
    UsdPrimCompositionQueryArc to to limit value resolution to a subrange
    of the prim's composed specs that are no stronger that arc, or a
    subrange of specs that is strictly stronger than that arc (optionally
    providing a particular layer within the arc's layer stack to further
    limit the range of specs).

    Alternatively, resolve targets can also be created via methods on
    UsdPrim that can limit value resolution to either up to or stronger
    than the spec that would be edited when setting a value for the prim
    using the given UsdEditTarget.

    Unlike UsdEditTarget, a UsdResolveTarget is only relevant to the prim
    it is created for and can only be used in a UsdAttributeQuery for
    attributes on this prim.

    Invalidation
    ============

    This object does not listen for change notification. If a consumer is
    holding on to a UsdResolveTarget, it is their responsibility to
    dispose of it in response to a resync change to the associated prim.
    Failing to do so may result in incorrect values or crashes due to
    dereferencing invalid objects.
    """
    __instance_size__: ClassVar[int] = ...
    def __init__(self) -> None: ...
    def GetPrimIndex(self) -> pxr.Pcp.PrimIndex:
        """
        Get the prim index of the resolve target.
        """
    def GetStartLayer(self) -> pxr.Sdf.Layer:
        """
        Returns the layer in the layer stack of the start node that value
        resolution with this resolve target will start at.
        """
    def GetStartNode(self) -> pxr.Pcp.NodeRef:
        """
        Returns the node that value resolution with this resolve target will
        start at.
        """
    def GetStopLayer(self) -> pxr.Sdf.Layer:
        """
        Returns the layer in the layer stack of the stop node that value
        resolution with this resolve target will stop at.
        """
    def GetStopNode(self) -> pxr.Pcp.NodeRef:
        '''
        Returns the node that value resolution with this resolve target will
        stop at when the"stop at"layer is reached.
        '''
    def IsNull(self) -> bool:
        """
        Returns true if this is a null resolve target.
        """

class SchemaBase(Boost.Python.instance):
    """
    The base class for all schema types in Usd.


    Schema objects hold a UsdPrim internally and provide a layer of
    specific named API atop the underlying scene graph.

    Schema objects are polymorphic but they are intended to be created as
    automatic local variables, so they may be passed and returned by-
    value. This leaves them subject to slicing. This means that if one
    passes a C{SpecificSchema} instance to a function that takes a
    UsdSchemaBase *by-value*, all the polymorphic behavior specific to
    C{SpecificSchema} is lost.

    To avoid slicing, it is encouraged that functions taking schema object
    arguments take them by C{const&} if const access is sufficient,
    otherwise by non-const pointer.
    """
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self, prim: Prim) -> None:
        """
        Construct and store C{prim} as the held prim.
        """
    @overload
    def __init__(self, otherSchema: SchemaBase) -> None:
        """
        Construct and store for the same prim held by C{otherSchema}.
        """
    @overload
    def __init__(self) -> None: ...
    def GetPath(self) -> pxr.Sdf.Path:
        """
        Shorthand for GetPrim() -> GetPath() .
        """
    def GetPrim(self) -> Prim:
        """
        Return this schema object's held prim.
        """
    @staticmethod
    def GetSchemaAttributeNames(includeInherited: bool = ...) -> list[str]: ...
    def GetSchemaClassPrimDefinition(self) -> PrimDefinition:
        """
        Return the prim definition associated with this schema instance if one
        exists, otherwise return null.


        This does not use the held prim's type. To get the held prim
        instance's definition, use UsdPrim::GetPrimDefinition() .

        UsdPrim::GetPrimDefinition()
        """
    def GetSchemaKind(self) -> SchemaKind:
        """
        Returns the kind of schema this class is.
        """
    def IsAPISchema(self) -> bool:
        """
        Returns whether this is an API schema or not.
        """
    def IsAppliedAPISchema(self) -> bool:
        """
        Returns whether this is an applied API schema or not.


        If this returns true this class will have an Apply() method
        """
    def IsConcrete(self) -> bool:
        """
        Returns whether or not this class corresponds to a concrete
        instantiable prim type in scene description.


        If this is true, GetStaticPrimDefinition() will return a valid prim
        definition with a non-empty typeName.
        """
    def IsMultipleApplyAPISchema(self) -> bool:
        """
        Returns whether this is an applied API schema or not.


        If this returns true the constructor, Get and Apply methods of this
        class will take in the name of the API schema instance.
        """
    def IsTyped(self) -> bool:
        """
        Returns whether or not this class inherits from UsdTyped.


        Types which inherit from UsdTyped can impart a typename on a UsdPrim.
        """
    def __bool__(self) -> bool:
        """
        Return true if this schema object is compatible with its held prim,
        false otherwise.


        For untyped schemas return true if the held prim is not expired,
        otherwise return false. For typed schemas return true if the held prim
        is not expired and its type is the schema's type or a subtype of the
        schema's type. Otherwise return false. This method invokes polymorphic
        behavior.

        UsdSchemaBase::_IsCompatible()
        """

class SchemaKind(Boost.Python.enum):
    AbstractBase: ClassVar[SchemaKind] = ...
    AbstractTyped: ClassVar[SchemaKind] = ...
    ConcreteTyped: ClassVar[SchemaKind] = ...
    Invalid: ClassVar[SchemaKind] = ...
    MultipleApplyAPI: ClassVar[SchemaKind] = ...
    NonAppliedAPI: ClassVar[SchemaKind] = ...
    SingleApplyAPI: ClassVar[SchemaKind] = ...
    names: ClassVar[dict] = ...
    values: ClassVar[dict] = ...

class SchemaRegistry(Boost.Python.instance):
    '''
    Singleton registry that provides access to schema type information and
    the prim definitions for registered Usd"IsA"and applied API schema
    types.


    It also contains the data from the generated schemas that is used by
    prim definitions to provide properties and fallbacks.

    The data contained herein comes from the generatedSchema.usda file
    (generated when a schema.usda file is processed by *usdGenSchema*) of
    each schema-defining module. The registry expects each schema type to
    be represented as a single prim spec with its inheritance flattened,
    i.e. the prim spec contains a union of all its local and class
    inherited property specs and metadata fields.

    It is used by the Usd core, via UsdPrimDefinition, to determine how to
    create scene description for unauthored"built-in"properties of schema
    classes, to enumerate all properties for a given schema class, and
    finally to provide fallback values for unauthored built-in properties.
    '''

    class SchemaInfo(Boost.Python.instance):
        """
        Structure that holds the information about a schema that is registered
        with the schema registry.
        """
        def __init__(self, *args, **kwargs) -> None:
            """Raises an exception
            This class cannot be instantiated from Python
            """
        @property
        def family(self): ...
        @property
        def identifier(self): ...
        @property
        def kind(self): ...
        @property
        def type(self): ...
        @property
        def version(self): ...

    class VersionPolicy(Boost.Python.enum):
        All: ClassVar[SchemaRegistry.VersionPolicy] = ...
        GreaterThan: ClassVar[SchemaRegistry.VersionPolicy] = ...
        GreaterThanOrEqual: ClassVar[SchemaRegistry.VersionPolicy] = ...
        LessThan: ClassVar[SchemaRegistry.VersionPolicy] = ...
        LessThanOrEqual: ClassVar[SchemaRegistry.VersionPolicy] = ...
        names: ClassVar[dict] = ...
        values: ClassVar[dict] = ...
    def __init__(self) -> None: ...
    def BuildComposedPrimDefinition(self, _primType: str | pxr.Ar.ResolvedPath, _appliedAPISchemas: list[str] | list[pxr.Ar.ResolvedPath], /) -> PrimDefinition:
        """
        Composes and returns a new UsdPrimDefinition from the given
        C{primType} and list of C{appliedSchemas}.


        This prim definition will contain a union of properties from the
        registered prim definitions of each of the provided types.
        """
    def FindAppliedAPIPrimDefinition(self, typeName: str | pxr.Ar.ResolvedPath) -> PrimDefinition:
        """
        Finds the prim definition for the given C{typeName} token if
        C{typeName} is a registered applied API schema type.


        Returns null if it is not.
        """
    def FindConcretePrimDefinition(self, typeName: str | pxr.Ar.ResolvedPath) -> PrimDefinition:
        """
        Finds the prim definition for the given C{typeName} token if
        C{typeName} is a registered concrete typed schema type.


        Returns null if it is not.
        """
    @overload
    @staticmethod
    def FindSchemaInfo(schemaType: pxr.Tf.Type) -> SchemaRegistry.SchemaInfo:
        """
        Finds and returns the schema info for a registered schema with the
        given C{schemaType}.


        Returns null if no registered schema with the schema type exists.
        """
    @overload
    @staticmethod
    def FindSchemaInfo(schemaIdentifier: str | pxr.Ar.ResolvedPath) -> SchemaRegistry.SchemaInfo:
        """
        Finds and returns the schema info for a registered schema with the
        given C{schemaIdentifier}.


        Returns null if no registered schema with the schema identifier
        exists.
        """
    @overload
    @staticmethod
    def FindSchemaInfo(schemaFamily: str | pxr.Ar.ResolvedPath, schemaVersion: int) -> SchemaRegistry.SchemaInfo:
        """
        Finds and returns the schema info for a registered schema in the given
        C{schemaFamily} with the given C{schemaVersion}.


        Returns null if no registered schema in the schema family with the
        given version exists.
        """
    @overload
    @staticmethod
    def FindSchemaInfosInFamily(schemaFamily: str | pxr.Ar.ResolvedPath) -> list[SchemaRegistry.SchemaInfo]:
        """
        Finds all schemas in the given C{schemaFamily} and returns their their
        schema info ordered from highest version to lowest version.
        """
    @overload
    @staticmethod
    def FindSchemaInfosInFamily(schemaFamily: str | pxr.Ar.ResolvedPath, schemaVersion: int, versionPolicy: SchemaRegistry.VersionPolicy) -> list[SchemaRegistry.SchemaInfo]:
        """
        Finds all schemas in the given C{schemaFamily}, filtered according to
        the given C{schemaVersion} and C{versionPolicy}, and returns their
        their schema info ordered from highest version to lowest version.
        """
    @staticmethod
    def GetAPISchemaCanOnlyApplyToTypeNames(apiSchemaName: str | pxr.Ar.ResolvedPath, instanceName: str | pxr.Ar.ResolvedPath = ...) -> list[str]:
        '''
        Returns a list of prim type names that the given C{apiSchemaName} can
        only be applied to.


        A non-empty list indicates that the API schema can only be applied to
        prim that are or derive from prim type names in the list. If the list
        is empty, the API schema can be applied to prims of any type.

        If a non-empty C{instanceName} is provided, this will first look for a
        list of"can only apply to"names specific to that instance of the API
        schema and return that if found. If a list is not found for the
        specific instance, it will fall back to looking for a"can only apply
        to"list for just the schema name itself.
        '''
    @staticmethod
    def GetAPISchemaTypeName(schemaType: pxr.Tf.Type) -> str:
        """
        Return the type name in the USD schema for API schema types only from
        the given registered C{schemaType}.
        """
    @staticmethod
    def GetAPITypeFromSchemaTypeName(typeName: str | pxr.Ar.ResolvedPath) -> pxr.Tf.Type:
        """
        Return the TfType of the schema corresponding to the given API schema
        type name C{typeName}.


        This the inverse of GetAPISchemaTypeNAme.
        """
    @staticmethod
    def GetAutoApplyAPISchemas() -> dict:
        """
        Returns a map of the names of all registered auto apply API schemas to
        the list of type names each is registered to be auto applied to.


        The list of type names to apply to will directly match what is
        specified in the plugin metadata for each schema type. While auto
        apply schemas do account for the existence and validity of the type
        names and expand to include derived types of the listed types, the
        type lists returned by this function do not.
        """
    @staticmethod
    def GetConcreteSchemaTypeName(schemaType: pxr.Tf.Type) -> str:
        """
        Return the type name in the USD schema for concrete prim types only
        from the given registered C{schemaType}.
        """
    @staticmethod
    def GetConcreteTypeFromSchemaTypeName(typeName: str | pxr.Ar.ResolvedPath) -> pxr.Tf.Type:
        """
        Return the TfType of the schema corresponding to the given concrete
        prim type name C{typeName}.


        This the inverse of GetConcreteSchemaTypeName.
        """
    def GetEmptyPrimDefinition(self) -> PrimDefinition:
        """
        Returns the empty prim definition.
        """
    def GetFallbackPrimTypes(self) -> dict:
        """
        Returns a dictionary mapping concrete schema prim type names to a
        VtTokenArray of fallback prim type names if fallback types are defined
        for the schema type in its registered schema.


        The standard use case for this to provide schema defined metadata that
        can be saved with a stage to inform an older version of USD - that may
        not have some schema types - as to which types it can used instead
        when encountering a prim of one these types.

        UsdStage::WriteFallbackPrimTypes

        Fallback Prim Types
        """
    @staticmethod
    def GetMultipleApplyNameTemplateBaseName(nameTemplate: str | pxr.Ar.ResolvedPath) -> str:
        """
        Returns the base name for the multiple apply schema name template
        C{nameTemplate}.


        The base name is the substring of the given name template that comes
        after the instance name placeholder and the subsequent namespace
        delimiter. If the given property name does not contain the instance
        name placeholder, it is not a name template and the name template is
        returned as is.
        """
    @overload
    @staticmethod
    def GetSchemaKind(primType: pxr.Tf.Type) -> SchemaKind:
        """
        Returns the kind of the schema the given C{schemaType} represents.


        This returns UsdSchemaKind::Invalid if C{schemaType} is not a valid
        schema type or if the kind cannot be determined from type's plugin
        information.
        """
    @overload
    @staticmethod
    def GetSchemaKind(primType: str | pxr.Ar.ResolvedPath) -> SchemaKind:
        """
        Returns the kind of the schema the given C{typeName} represents.


        This returns UsdSchemaKind::Invalid if C{typeName} is not a valid
        schema type name or if the kind cannot be determined from type's
        plugin information.
        """
    @staticmethod
    def GetSchemaTypeName(schemaType: pxr.Tf.Type) -> str:
        """
        Return the type name in the USD schema for prims or API schemas of the
        given registered C{schemaType}.
        """
    @staticmethod
    def GetTypeFromName(typeName: str | pxr.Ar.ResolvedPath) -> pxr.Tf.Type:
        '''
        Finds the TfType of a schema with C{typeName}.


        This is primarily for when you have been provided Schema typeName
        (perhaps from a User Interface or Script) and need to identify if a
        prim\'s type inherits/is that typeName. If the type name IS known, then
        using the schema class is preferred. ::

          # This code attempts to match all prims on a stage to a given
          # user specified type, making the traditional schema based idioms not
          # applicable.
          data = parser.parse_args()
          tfType = UsdSchemaRegistry.GetTypeFromName(data.type)
          matchedPrims = [p for p in stage.Traverse() if p.IsA(tfType)] 

        It\'s worth noting that GetTypeFromName("Sphere") ==
        GetTypeFromName("UsdGeomSphere"), as this function resolves both the
        Schema\'s C++ class name and any registered aliases from a modules
        plugInfo.json file. However, GetTypeFromName("Boundable") !=
        GetTypeFromName("UsdGeomBoundable") because type aliases don\'t get
        registered for abstract schema types.
        '''
    @staticmethod
    def GetTypeFromSchemaTypeName(typeName: str | pxr.Ar.ResolvedPath) -> pxr.Tf.Type:
        """
        Return the TfType of the schema corresponding to the given prim or API
        schema name C{typeName}.


        This the inverse of GetSchemaTypeName.
        """
    @staticmethod
    def GetTypeNameAndInstance(typeName: str | pxr.Ar.ResolvedPath) -> tuple:
        """
        Returns the schema type name and the instance name parsed from the
        given C{apiSchemaName}.


        C{apiSchemaName} is the name of an applied schema as it appears in the
        list of applied schemas on a prim. For single-apply API schemas the
        name will just be the schema type name. For multiple-apply schemas the
        name should include the schema type name and the applied instance name
        separated by a namespace delimiter, for
        example'CollectionAPI:plasticStuff'.

        This function returns the separated schema type name and instance name
        component tokens if possible, otherwise it returns the
        C{apiSchemaName} as the type name and an empty instance name.

        Note that no validation is done on the returned tokens. Clients are
        advised to use GetTypeFromSchemaTypeName() to validate the typeName
        token.

        UsdPrim::AddAppliedSchema(const TfToken&) const

        UsdPrim::GetAppliedSchemas() const
        """
    @overload
    @staticmethod
    def IsAbstract(primType: pxr.Tf.Type) -> bool:
        """
        Returns true if the prim type C{primType} is an abstract schema type
        and, unlike a concrete type, is not instantiable in scene description.
        """
    @overload
    @staticmethod
    def IsAbstract(primType: str | pxr.Ar.ResolvedPath) -> bool:
        """
        Returns true if the prim type C{primType} is an abstract schema type
        and, unlike a concrete type, is not instantiable in scene description.
        """
    @staticmethod
    def IsAllowedAPISchemaInstanceName(apiSchemaName: str | pxr.Ar.ResolvedPath, instanceName: str | pxr.Ar.ResolvedPath) -> bool:
        """
        Returns true if the given C{instanceName} is an allowed instance name
        for the multiple apply API schema named C{apiSchemaName}.


        Any instance name that matches the name of a property provided by the
        API schema is disallowed and will return false. If the schema type has
        plugin metadata that specifies allowed instance names, then only those
        specified names are allowed for the schema type. If the instance name
        is empty or the API is not a multiple apply schema, this will return
        false.
        """
    @staticmethod
    def IsAllowedSchemaFamily(schemaFamily: str | pxr.Ar.ResolvedPath) -> bool:
        """
        Returns whether the given C{schemaFamily} is an allowed schema family
        name.


        A schema family is allowed if it's a valid identifier and does not
        itself contain a version suffix.
        """
    @staticmethod
    def IsAllowedSchemaIdentifier(schemaIdentifier: str | pxr.Ar.ResolvedPath) -> bool:
        """
        Returns whether the given C{schemaIdentifier} is an allowed schema
        identifier.


        A schema identifier is allowed if it can be  parsed into a allowed
        schema family and schema version and it is the identifier that would
        be created from that parsed family and version.
        """
    @overload
    @staticmethod
    def IsAppliedAPISchema(apiSchemaType: pxr.Tf.Type) -> bool:
        """
        Returns true if C{apiSchemaType} is an applied API schema type.
        """
    @overload
    @staticmethod
    def IsAppliedAPISchema(apiSchemaType: str | pxr.Ar.ResolvedPath) -> bool:
        """
        Returns true if C{apiSchemaType} is an applied API schema type.
        """
    @overload
    @staticmethod
    def IsConcrete(primType: pxr.Tf.Type) -> bool:
        """
        Returns true if the prim type C{primType} is instantiable in scene
        description.
        """
    @overload
    @staticmethod
    def IsConcrete(primType: str | pxr.Ar.ResolvedPath) -> bool:
        """
        Returns true if the prim type C{primType} is instantiable in scene
        description.
        """
    @staticmethod
    def IsDisallowedField(fieldName: str | pxr.Ar.ResolvedPath) -> bool:
        """
        Returns true if the field C{fieldName} cannot have fallback values
        specified in schemas.


        Fields are generally disallowed because their fallback values aren't
        used. For instance, fallback values for composition arcs aren't used
        during composition, so allowing them to be set in schemas would be
        misleading.
        """
    @overload
    @staticmethod
    def IsMultipleApplyAPISchema(apiSchemaType: pxr.Tf.Type) -> bool:
        """
        Returns true if C{apiSchemaType} is a multiple-apply API schema type.
        """
    @overload
    @staticmethod
    def IsMultipleApplyAPISchema(apiSchemaType: str | pxr.Ar.ResolvedPath) -> bool:
        """
        Returns true if C{apiSchemaType} is a multiple-apply API schema type.
        """
    @staticmethod
    def IsMultipleApplyNameTemplate(nameTemplate: str | pxr.Ar.ResolvedPath) -> bool:
        '''
        Returns true if C{nameTemplate} is a multiple apply schema name
        template.


        The given C{nameTemplate} is a name template if and only if it
        contains the instance name place holder"__INSTANCE_NAME__"as an exact
        match as one of the tokenized components of the name tokenized by the
        namespace delimiter.
        '''
    @staticmethod
    def IsTyped(primType: pxr.Tf.Type) -> bool:
        """
        Returns true if the prim type C{primType} inherits from UsdTyped.
        """
    @staticmethod
    def MakeMultipleApplyNameInstance(_nameTemplate: str | pxr.Ar.ResolvedPath, /, nameTemplate: str | pxr.Ar.ResolvedPath) -> str:
        '''
        Returns an instance of a multiple apply schema name from the given
        C{nameTemplate} for the given C{instanceName}.


        The returned name is created by replacing the instance name
        placeholder"__INSTANCE_NAME__"in the name template with the given
        instance name. If the instance name placeholder is not found in
        C{nameTemplate}, then the name template is not multiple apply name
        template and is returned as is.

        Note that the instance name placeholder must be found as an exact full
        word match with one of the tokenized components of the name template,
        when tokenized by the namespace delimiter, in order for it to be
        treated as a placeholder and substituted with the instance name.
        '''
    @staticmethod
    def MakeMultipleApplyNameTemplate(_namespacePrefix: str | pxr.Ar.ResolvedPath, /, namespacePrefix: str | pxr.Ar.ResolvedPath) -> str:
        '''
        Creates a name template that can represent a property or API schema
        that belongs to a multiple apply schema and will therefore have
        multiple instances with different names.


        The name template is created by joining the C{namespacePrefix}, the
        instance name placeholder"__INSTANCE_NAME__", and the C{baseName}
        using the namespace delimiter. Therefore the returned name template
        will be of one of the following forms depending on whether either of
        the inputs is empty:
           - namespacePrefix: B{INSTANCE_NAME} :baseName

           - namespacePrefix: B{INSTANCE_NAME}

           - B{INSTANCE_NAME} :baseName

           - B{INSTANCE_NAME}

        Name templates can be passed to MakeMultipleApplyNameInstance along
        with an instance name to create the name for a particular instance.
        '''
    @staticmethod
    def MakeSchemaIdentifierForFamilyAndVersion(schemaFamily: str | pxr.Ar.ResolvedPath, schemaVersion: int) -> str:
        """
        Creates the schema identifier that would be used to define a schema of
        the given C{schemaFamily} with the given C{schemaVersion}.


        If the provided schema version is zero, the returned identifier will
        be the schema family itself. For all other versions, the returned
        identifier will be the family followed by an underscore and the
        version number.

        If C{schemaFamily} is not an allowed schema family, this function will
        append the appropriate version suffix, but the returned identifier
        will not be an allowed schema identifier.
        """
    @staticmethod
    def ParseSchemaFamilyAndVersionFromIdentifier(schemaIdentifier: str | pxr.Ar.ResolvedPath) -> tuple:
        '''
        Parses and returns the schema family and version values from the given
        C{schemaIdentifier}.


        A schema identifier\'s version is indicated by a suffix consisting of
        an underscore followed by a positive integer which is its version. The
        schema family is the string before this suffix. If the identifier does
        not have a suffix matching this pattern, then the schema version is
        zero and the schema family is the identifier itself.

        For example: Identifier"FooAPI_1"returns ("FooAPI", 1)
        Identifier"FooAPI"returns ("FooAPI", 0)

        Note that this function only parses what the schema family and version
        would be for the given schema identifier and does not require that
        C{schemaIdentifier} be a registered schema itself or even an allowed
        schema identifier.
        '''
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

class Specializes(Boost.Python.instance):
    """
    A proxy class for applying listOp edits to the specializes list for a
    prim.


    All paths passed to the UsdSpecializes API are expected to be in the
    namespace of the owning prim's stage. Subroot prim specializes paths
    will be translated from this namespace to the namespace of the current
    edit target, if necessary. If a path cannot be translated, a coding
    error will be issued and no changes will be made. Root prim
    specializes paths will not be translated.
    """
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """
    def AddSpecialize(self, primPath: pxr.Sdf.Path | str, position: ListPosition = ...) -> bool:
        """
        Adds a path to the specializes listOp at the current EditTarget, in
        the position specified by C{position}.
        """
    def ClearSpecializes(self) -> bool:
        """
        Removes the authored specializes listOp edits at the current edit
        target.
        """
    def GetPrim(self) -> Prim:
        """
        Return the prim this object is bound to.
        """
    def RemoveSpecialize(self, primPath: pxr.Sdf.Path | str) -> bool:
        """
        Removes the specified path from the specializes listOp at the current
        EditTarget.
        """
    def SetSpecializes(self, _items: typing.Iterable[pxr.Sdf.Path | str], /) -> bool:
        """
        Explicitly set specializes paths, potentially blocking weaker opinions
        that add or remove items, returning true on success, false if the edit
        could not be performed.
        """
    def __bool__(self) -> bool: ...

class Stage(Boost.Python.instance):
    '''
    The outermost container for scene description, which owns and presents
    composed prims as a scenegraph, following the composition recipe
    recursively described in its associated"root layer".


    USD derives its persistent-storage scalability by combining and
    reusing simple compositions into richer aggregates using referencing
    and layering with sparse overrides. Ultimately, every composition
    (i.e."scene") is identifiable by its root layer, i.e. the C{.usd}
    file, and a scene is instantiated in an application on a UsdStage that
    presents a composed view of the scene\'s root layer. Each simple
    composition referenced into a larger composition could be presented on
    its own UsdStage, at the same (or not) time that it is participating
    in the larger composition on its own UsdStage; all of the underlying
    layers will be shared by the two stages, while each maintains its own
    scenegraph of composed prims.

    A UsdStage has sole ownership over the UsdPrim \'s with which it is
    populated, and retains *shared* ownership (with other stages and
    direct clients of SdfLayer \'s, via the Sdf_LayerRegistry that
    underlies all SdfLayer creation methods) of layers. It provides
    roughly five categories of API that address different aspects of scene
    management:

       - Stage lifetime management methods for constructing and initially
         populating a UsdStage from an existing layer file, or one that will be
         created as a result, in memory or on the filesystem.

       - Load/unload working set management methods that allow you to
         specify which payloads should be included and excluded from the
         stage\'s composition.

       - Variant management methods to manage policy for which variant to
         use when composing prims that provide a named variant set, but do not
         specify a selection.

       - Prim access, creation, and mutation methods that allow you to
         find, create, or remove a prim identified by a path on the stage. This
         group also provides methods for efficiently traversing the prims on
         the stage.

       - Layers and EditTargets methods provide access to the layers in
         the stage\'s *root LayerStack* (i.e. the root layer and all of its
         recursive sublayers), and the ability to set a UsdEditTarget into
         which all subsequent mutations to objects associated with the stage
         (e.g. prims, properties, etc) will go.

       - Serialization methods for"flattening"a composition (to varying
         degrees), and exporting a completely flattened view of the stage to a
         string or file. These methods can be very useful for targeted asset
         optimization and debugging, though care should be exercized with large
         scenes, as flattening defeats some of the benefits of referenced scene
         description, and may produce very large results, especially in file
         formats that do not support data de-duplication, like the usda text
         format!

    Stage Session Layers
    ====================

    Each UsdStage can possess an optional"session layer". The purpose of a
    session layer is to hold ephemeral edits that modify a UsdStage \'s
    contents or behavior in a way that is useful to the client, but should
    not be considered as permanent mutations to be recorded upon export. A
    very common use of session layers is to make variant selections, to
    pick a specific LOD or shading variation, for example. The session
    layer is also frequently used to override the visibility of geometry
    and assets in the scene. A session layer, if present, contributes to a
    UsdStage \'s identity, for purposes of stage-caching, etc.

    To edit content in a session layer, get the layer\'s edit target using
    stage->GetEditTargetForLocalLayer(stage-> GetSessionLayer() ) and set
    that target in the stage by calling SetEditTarget() or creating a
    UsdEditContext.
    '''

    class InitialLoadSet(pxr.Tf.Tf_PyEnumWrapper):
        _baseName: ClassVar[str] = ...
        allValues: ClassVar[tuple] = ...
        def __init__(self, *args, **kwargs) -> None:
            """Raises an exception
            This class cannot be instantiated from Python
            """
        @staticmethod
        def GetValueFromName(name: object) -> Any: ...
    LoadAll: ClassVar[Stage.InitialLoadSet] = ...
    LoadNone: ClassVar[Stage.InitialLoadSet] = ...
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """
    def ClearDefaultPrim(self) -> None:
        """
        Clear the default prim layer metadata in this stage's root layer.


        This is shorthand for: ::

          stage->GetRootLayer()->ClearDefaultPrim();

         Note that this function always authors to the stage's root layer. To
        author to a different layer, use the SdfLayer::SetDefaultPrim() API.
        """
    def ClearMetadata(self, _key: str | pxr.Ar.ResolvedPath, /) -> bool:
        """
        Clear the value of stage metadatum C{key}, if the stage's current
        UsdEditTarget is the root or session layer.


        If the current EditTarget is any other layer, raise a coding error.

        true if authoring was successful, false otherwise. Generates a coding
        error if C{key} is not allowed as layer metadata.

        General Metadata in USD
        """
    def ClearMetadataByDictKey(self, _key: str | pxr.Ar.ResolvedPath, _keyPath: str | pxr.Ar.ResolvedPath, /) -> bool:
        """
        Clear any authored value identified by C{key} and C{keyPath} at the
        current EditTarget.


        The C{keyPath} is a':'-separated path identifying a path in
        subdictionaries stored in the metadata field at C{key}. If C{keyPath}
        is empty, no action is taken.

        true if the value is cleared successfully, false otherwise. Generates
        a coding error if C{key} is not allowed as layer metadata.

        Dictionary-valued Metadata
        """
    def CreateClassPrim(self, rootPrimPath: pxr.Sdf.Path | str) -> Prim:
        """
        Author an *SdfPrimSpec* with *specifier* == *SdfSpecifierClass* for
        the class at root prim path C{path} at the current EditTarget.


        The current EditTarget must have UsdEditTarget::IsLocalLayer() ==
        true.

        The given *path* must be an absolute, root prim path that does not
        contain any variant selections.

        If a defined ( UsdPrim::IsDefined() ) non-class prim already exists at
        C{path}, issue an error and return an invalid UsdPrim.

        If it is impossible to author the necessary PrimSpec, issue an error
        and return an invalid *UsdPrim*.
        """
    @overload
    @staticmethod
    def CreateInMemory(load: Stage.InitialLoadSet = ...) -> Stage:
        """
        Creates a new stage only in memory, analogous to creating an anonymous
        SdfLayer.


        If C{pathResolverContext} is provided it will be bound when creating
        the root layer at C{identifier} and whenever asset path resolution is
        done for this stage, regardless of what other context may be bound at
        that time. Otherwise Usd will create the root layer with no context
        bound, then create a context for all future asset path resolution for
        the stage by calling ArResolver::CreateDefaultContext.

        The initial set of prims to load on the stage can be specified using
        the C{load} parameter.

        UsdStage::InitialLoadSet. Invoking an overload that does not take a
        C{sessionLayer} argument will create a stage with an anonymous in-
        memory session layer. To create a stage without a session layer, pass
        TfNullPtr (or None in python) as the C{sessionLayer} argument.
        """
    @overload
    @staticmethod
    def CreateInMemory(identifier: str | pxr.Ar.ResolvedPath, load: Stage.InitialLoadSet = ...) -> Stage:
        """
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        """
    @overload
    @staticmethod
    def CreateInMemory(identifier: str | pxr.Ar.ResolvedPath, pathResolverContext: pxr.Ar.ResolverContext, load: Stage.InitialLoadSet = ...) -> Stage:
        """
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        """
    @overload
    @staticmethod
    def CreateInMemory(identifier: str | pxr.Ar.ResolvedPath, sessionLayer: pxr.Sdf.Layer, load: Stage.InitialLoadSet = ...) -> Stage:
        """
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        """
    @overload
    @staticmethod
    def CreateInMemory(identifier: str | pxr.Ar.ResolvedPath, sessionLayer: pxr.Sdf.Layer, pathResolverContext: pxr.Ar.ResolverContext, load: Stage.InitialLoadSet = ...) -> Stage:
        """
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        """
    @overload
    @staticmethod
    def CreateNew(identifier: str | pxr.Ar.ResolvedPath, load: Stage.InitialLoadSet = ...) -> Stage:
        """
        Create a new stage with root layer C{identifier}, destroying
        potentially existing files with that identifier; it is considered an
        error if an existing, open layer is present with this identifier.



        SdfLayer::CreateNew() Invoking an overload that does not take a
        C{sessionLayer} argument will create a stage with an anonymous in-
        memory session layer. To create a stage without a session layer, pass
        TfNullPtr (or None in python) as the C{sessionLayer} argument. The
        initial set of prims to load on the stage can be specified using the
        C{load} parameter.

        UsdStage::InitialLoadSet. If C{pathResolverContext} is provided it
        will be bound when creating the root layer at C{identifier} and
        whenever asset path resolution is done for this stage, regardless of
        what other context may be bound at that time. Otherwise Usd will
        create the root layer with no context bound, then create a context for
        all future asset path resolution for the stage by calling
        ArResolver::CreateDefaultContextForAsset with the root layer's
        repository path if the layer has one, otherwise its resolved path.
        """
    @overload
    @staticmethod
    def CreateNew(identifier: str | pxr.Ar.ResolvedPath, sessionLayer: pxr.Sdf.Layer, load: Stage.InitialLoadSet = ...) -> Stage:
        """
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        """
    @overload
    @staticmethod
    def CreateNew(identifier: str | pxr.Ar.ResolvedPath, sessionLayer: pxr.Sdf.Layer, pathResolverContext: pxr.Ar.ResolverContext, load: Stage.InitialLoadSet = ...) -> Stage:
        """
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        """
    @overload
    @staticmethod
    def CreateNew(identifier: str | pxr.Ar.ResolvedPath, pathResolverContext: pxr.Ar.ResolverContext, load: Stage.InitialLoadSet = ...) -> Stage:
        """
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        """
    def DefinePrim(self, path: pxr.Sdf.Path | str, typeName: str | pxr.Ar.ResolvedPath = ...) -> Prim:
        """
        Attempt to ensure a *UsdPrim* at C{path} is defined (according to
        UsdPrim::IsDefined() ) on this stage.


        If a prim at C{path} is already defined on this stage and C{typeName}
        is empty or equal to the existing prim's typeName, return that prim.
        Otherwise author an *SdfPrimSpec* with *specifier* ==
        *SdfSpecifierDef* and C{typeName} for the prim at C{path} at the
        current EditTarget. Author *SdfPrimSpec* s with C{specifier} ==
        *SdfSpecifierDef* and empty typeName at the current EditTarget for any
        nonexistent, or existing but not *Defined* ancestors.

        The given *path* must be an absolute prim path that does not contain
        any variant selections.

        If it is impossible to author any of the necessary PrimSpecs (for
        example, in case *path* cannot map to the current UsdEditTarget 's
        namespace or one of the ancestors of C{path} is inactive on the
        UsdStage), issue an error and return an invalid *UsdPrim*.

        Note that this method may return a defined prim whose typeName does
        not match the supplied C{typeName}, in case a stronger typeName
        opinion overrides the opinion at the current EditTarget.
        """
    @overload
    def ExpandPopulationMask(self, traversalPredicate: _PrimFlagsPredicate | _Term, relationshipPredicate: typing.Callable[[Relationship], bool] = ..., attributePredicate: typing.Callable[[Attribute | pxr.UsdGeom.ConstraintTarget | pxr.UsdGeom.Primvar | pxr.UsdGeom.XformOp | pxr.UsdShade.Input | pxr.UsdShade.Output], bool] = ...) -> None:
        """
        Expand this stage's population mask to include the targets of all
        relationships that pass C{relPred} and connections to all attributes
        that pass C{attrPred} recursively.


        The attributes and relationships are those on all the prims found by
        traversing the stage according to C{traversalPredicate}. If C{relPred}
        is null, include all relationship targets; if C{attrPred} is null,
        include all connections.

        This function can be used, for example, to expand a population mask
        for a given prim to include bound materials, if those bound materials
        are expressed as relationships or attribute connections.

        See also UsdPrim::FindAllRelationshipTargetPaths() and
        UsdPrim::FindAllAttributeConnectionPaths() .
        """
    @overload
    def ExpandPopulationMask(self, relationshipPredicate: typing.Callable[[Relationship], bool] = ..., attributePredicate: typing.Callable[[Attribute | pxr.UsdGeom.ConstraintTarget | pxr.UsdGeom.Primvar | pxr.UsdGeom.XformOp | pxr.UsdShade.Input | pxr.UsdShade.Output], bool] = ...) -> None:
        """
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        This convenience overload invokes ExpandPopulationMask() with the
        UsdPrimDefaultPredicate traversal predicate.
        """
    def Export(self, filename: str | pxr.Ar.ResolvedPath, addSourceFileComment: bool = ..., args: dict = ...) -> bool:
        """
        Writes out the composite scene as a single flattened layer into
        *filename*.


        If addSourceFileComment is true, a comment in the output layer will
        mention the input layer it was generated from.

        See UsdStage::Flatten for details of the flattening transformation.
        """
    def ExportToString(self, addSourceFileComment: bool = ...) -> str:
        """
        Writes the composite scene as a flattened Usd text representation into
        the given *string*.


        If addSourceFileComment is true, a comment in the output layer will
        mention the input layer it was generated from.

        See UsdStage::Flatten for details of the flattening transformation.
        """
    def FindLoadable(self, rootPath: pxr.Sdf.Path | str = ...) -> list[pxr.Sdf.Path]:
        """
        Returns an SdfPathSet of all paths that can be loaded.


        Note that this method does not return paths to inactive prims as they
        cannot be loaded.

        The set returned includes loaded and unloaded paths. To determine the
        set of unloaded paths, one can diff this set with the current load
        set, for example: ::

          SdfPathSet loaded = stage->GetLoadSet(),
                     all = stage->FindLoadable(),
                     result;
          std::set_difference(loaded.begin(), loaded.end(),
                              all.begin(), all.end(),
                              std::inserter(result, result.end()));

        See Working Set Management for more information.
        """
    def Flatten(self, addSourceFileComment: bool = ...) -> pxr.Sdf.Layer:
        """
        Returns a single, anonymous, merged layer for this composite scene.


        Specifically, this function removes B{most} composition metadata and
        authors the resolved values for each object directly into the
        flattened layer.

        All VariantSets are removed and only the currently selected variants
        will be present in the resulting layer.

        Class prims will still exist, however all inherits arcs will have been
        removed and the inherited data will be copied onto each child object.
        Composition arcs authored on the class itself will be flattened into
        the class.

        Flatten preserves scenegraph instancing by creating independent roots
        for each prototype currently composed on this stage, and adding a
        single internal reference arc on each instance prim to its
        corresponding prototype.

        Time samples across sublayer offsets will will have the time offset
        and scale applied to each time index.

        Finally, any deactivated prims will be pruned from the result.
        """
    def GetAttributeAtPath(self, path: pxr.Sdf.Path | str) -> Attribute:
        """
        Return the UsdAttribute at C{path}, or an invalid UsdAttribute if none
        exists.


        This is equivalent to ::

          stage.GetObjectAtPath(path).As<UsdAttribute>();

        GetObjectAtPath(const SdfPath&) const
        """
    @staticmethod
    def GetColorConfigFallbacks() -> tuple[None, pxr.Sdf.AssetPath, str]:
        """
        Returns the global fallback values
        of'colorConfiguration'and'colorManagementSystem'.


        These are set in the plugInfo.json file of a plugin, but can be
        overridden by calling the static method SetColorConfigFallbacks() .

        The python wrapping of this method returns a tuple containing
        (colorConfiguration, colorManagementSystem).

        SetColorConfigFallbacks, Color Configuration API
        """
    def GetColorConfiguration(self) -> pxr.Sdf.AssetPath:
        """
        Returns the default color configuration used to interpret the per-
        attribute color-spaces in the composed USD stage.


        Color Configuration API
        """
    def GetColorManagementSystem(self) -> str:
        """
        Sets the name of the color management system to be used for loading
        and interpreting the color configuration file.


        Color Configuration API
        """
    def GetDefaultPrim(self) -> Prim:
        """
        Return the root UsdPrim on this stage whose name is the root layer's
        defaultPrim metadata's value.


        Return an invalid prim if there is no such prim or if the root layer's
        defaultPrim metadata is unset or is not a valid prim name. Note that
        this function only examines this stage's rootLayer. It does not
        consider sublayers of the rootLayer. See also
        SdfLayer::GetDefaultPrim() .
        """
    def GetEditTarget(self) -> EditTarget:
        """
        Return the stage's EditTarget.
        """
    @overload
    def GetEditTargetForLocalLayer(self, _i: int, /) -> EditTarget:
        """
        Return a UsdEditTarget for editing the layer at index *i* in the layer
        stack.


        This edit target will incorporate any layer time offset that applies
        to the sublayer.
        """
    @overload
    def GetEditTargetForLocalLayer(self, _layer: pxr.Sdf.Layer, /) -> EditTarget:
        """
        Return a UsdEditTarget for editing the given local *layer*.


        If the given layer appears more than once in the layer stack, the time
        offset to the first occurrence will be used.
        """
    def GetEndTimeCode(self) -> float:
        """
        Returns the stage's end timeCode.


        If the stage has an associated session layer with an end timeCode
        opinion, this value is returned. Otherwise, the end timeCode opinion
        from the root layer is returned.
        """
    def GetFramesPerSecond(self) -> float:
        """
        Returns the stage's framesPerSecond value.


        This makes an advisory statement about how the contained data can be
        most usefully consumed and presented. It's primarily an indication of
        the expected playback rate for the data, but a timeline editing tool
        might also want to use this to decide how to scale and label its
        timeline.

        The default value of framesPerSecond is 24.
        """
    @staticmethod
    def GetGlobalVariantFallbacks() -> dict:
        """
        Get the global variant fallback preferences used in new UsdStages.
        """
    def GetInterpolationType(self) -> InterpolationType:
        """
        Returns the interpolation type used during value resolution for all
        attributes on this stage.
        """
    def GetLayerStack(self, includeSessionLayers: bool = ...) -> list[pxr.Sdf.Layer]:
        """
        Return this stage's local layers in strong-to-weak order.


        If *includeSessionLayers* is true, return the linearized strong-to-
        weak sublayers rooted at the stage's session layer followed by the
        linearized strong-to-weak sublayers rooted at this stage's root layer.
        If *includeSessionLayers* is false, omit the sublayers rooted at this
        stage's session layer.
        """
    def GetLoadRules(self) -> StageLoadRules:
        """
        Return the stage's current UsdStageLoadRules governing payload
        inclusion.


        See Working Set Management for more information.
        """
    def GetLoadSet(self) -> list[pxr.Sdf.Path]:
        """
        Returns a set of all loaded paths.


        The paths returned are both those that have been explicitly loaded and
        those that were loaded as a result of dependencies, ancestors or
        descendants of explicitly loaded paths.

        This method does not return paths to inactive prims.

        See Working Set Management for more information.
        """
    def GetMetadata(self, _key: str | pxr.Ar.ResolvedPath, /) -> Any:
        """
        Return in C{value} an authored or fallback value (if one was defined
        for the given metadatum) for Stage metadatum C{key}.


        Order of resolution is session layer, followed by root layer, else
        fallback to the SdfSchema.

        true if we successfully retrieved a value of the requested type; false
        if C{key} is not allowed as layer metadata or no value was found.
        Generates a coding error if we retrieved a stored value of a type
        other than the requested type

        General Metadata in USD
        """
    def GetMetadataByDictKey(self, _key: str | pxr.Ar.ResolvedPath, _keyPath: str | pxr.Ar.ResolvedPath, /) -> Any:
        """
        Resolve the requested dictionary sub-element C{keyPath} of dictionary-
        valued metadatum named C{key}, returning the resolved value.


        If you know you need just a small number of elements from a
        dictionary, accessing them element-wise using this method can be much
        less expensive than fetching the entire dictionary with
        GetMetadata(key).

        true if we successfully retrieved a value of the requested type; false
        if C{key} is not allowed as layer metadata or no value was found.
        Generates a coding error if we retrieved a stored value of a type
        other than the requested type The C{keyPath} is a':'-separated path
        addressing an element in subdictionaries. If C{keyPath} is empty,
        returns an empty VtValue.
        """
    def GetMutedLayers(self) -> list[str]:
        """
        Returns a vector of all layers that have been muted on this stage.
        """
    def GetObjectAtPath(self, path: pxr.Sdf.Path | str) -> Object:
        """
        Return the UsdObject at C{path}, or an invalid UsdObject if none
        exists.


        If C{path} indicates a prim beneath an instance, returns an instance
        proxy prim if a prim exists at the corresponding path in that
        instance's prototype. If C{path} indicates a property beneath a child
        of an instance, returns a property whose parent prim is an instance
        proxy prim.

        Example: ::

          if (UsdObject obj = stage->GetObjectAtPath(path)) {
              if (UsdPrim prim = obj.As<UsdPrim>()) {
                  // Do things with prim
              }
              else if (UsdProperty prop = obj.As<UsdProperty>()) {
                  // Do things with property. We can also cast to
                  // UsdRelationship or UsdAttribute using this same pattern.
              }
          }
          else {
              // No object at specified path
          }

        """
    def GetPathResolverContext(self) -> pxr.Ar.ResolverContext:
        """
        Return the path resolver context for all path resolution during
        composition of this stage.


        Useful for external clients that want to resolve paths with the same
        context as this stage, or create new stages with the same context.
        """
    def GetPopulationMask(self) -> StagePopulationMask:
        """
        Return this stage's population mask.
        """
    def GetPrimAtPath(self, path: pxr.Sdf.Path | str) -> Prim:
        '''
        Return the UsdPrim at C{path}, or an invalid UsdPrim if none exists.


        If C{path} indicates a prim beneath an instance, returns an instance
        proxy prim if a prim exists at the corresponding path in that
        instance\'s prototype.

        Unlike OverridePrim() and DefinePrim() , this method will never author
        scene description, and therefore is safe to use as a"reader"in the Usd
        multi-threading model.
        '''
    def GetPropertyAtPath(self, path: pxr.Sdf.Path | str) -> Property:
        """
        Return the UsdProperty at C{path}, or an invalid UsdProperty if none
        exists.


        This is equivalent to ::

          stage.GetObjectAtPath(path).As<UsdProperty>();

        GetObjectAtPath(const SdfPath&) const
        """
    def GetPrototypes(self) -> list[Prim]:
        """
        Returns all native instancing prototype prims.
        """
    def GetPseudoRoot(self) -> Prim:
        '''
        Return the stage\'s"pseudo-root"prim, whose name is defined by Usd.


        The stage\'s named root prims are namespace children of this prim,
        which exists to make the namespace hierarchy a tree instead of a
        forest. This simplifies algorithms that want to traverse all prims.

        A UsdStage always has a pseudo-root prim, unless there was an error
        opening or creating the stage, in which case this method returns an
        invalid UsdPrim.
        '''
    def GetRelationshipAtPath(self, path: pxr.Sdf.Path | str) -> Relationship:
        """
        Return the UsdAttribute at C{path}, or an invalid UsdAttribute if none
        exists.


        This is equivalent to ::

          stage.GetObjectAtPath(path).As<UsdRelationship>();

        GetObjectAtPath(const SdfPath&) const
        """
    def GetRootLayer(self) -> pxr.Sdf.Layer:
        """
        Return this stage's root layer.
        """
    def GetSessionLayer(self) -> pxr.Sdf.Layer:
        """
        Return this stage's root session layer.
        """
    def GetStartTimeCode(self) -> float:
        """
        Returns the stage's start timeCode.


        If the stage has an associated session layer with a start timeCode
        opinion, this value is returned. Otherwise, the start timeCode opinion
        from the root layer is returned.
        """
    def GetTimeCodesPerSecond(self) -> float:
        """
        Returns the stage's timeCodesPerSecond value.


        The timeCodesPerSecond value scales the time ordinate for the samples
        contained in the stage to seconds. If timeCodesPerSecond is 24, then a
        sample at time ordinate 24 should be viewed exactly one second after
        the sample at time ordinate 0.

        Like SdfLayer::GetTimeCodesPerSecond, this accessor uses a dynamic
        fallback to framesPerSecond. The order of precedence is:

           - timeCodesPerSecond from session layer

           - timeCodesPerSecond from root layer

           - framesPerSecond from session layer

           - framesPerSecond from root layer

           - fallback value of 24

        """
    def GetUsedLayers(self, includeClipLayers: bool = ...) -> list[pxr.Sdf.Layer]:
        """
        Return a vector of all of the layers *currently* consumed by this
        stage, as determined by the composition arcs that were traversed to
        compose and populate the stage.


        The list of consumed layers will change with the stage's load-set and
        variant selections, so the return value should be considered only a
        snapshot. The return value will include the stage's session layer, if
        it has one. If *includeClipLayers* is true, we will also include all
        of the layers that this stage has had to open so far to perform value
        resolution of attributes affected by Value Clips
        """
    def HasAuthoredMetadata(self, _key: str | pxr.Ar.ResolvedPath, /) -> bool:
        """
        Returns C{true} if the *key* has an authored value, C{false} if no
        value was authored or the only value available is the SdfSchema 's
        metadata fallback.



        If a value for a metadatum *not* legal to author on layers is present
        in the root or session layer (which could happen through hand-editing
        or use of certain low-level API's), this method will still return
        C{false}.
        """
    def HasAuthoredMetadataDictKey(self, _key: str | pxr.Ar.ResolvedPath, _keyPath: str | pxr.Ar.ResolvedPath, /) -> bool:
        """
        Return true if there exists any authored opinion (excluding fallbacks)
        for C{key} and C{keyPath}.



        The C{keyPath} is a':'-separated path identifying a value in
        subdictionaries stored in the metadata field at C{key}. If C{keyPath}
        is empty, returns C{false}.

        Dictionary-valued Metadata
        """
    def HasAuthoredTimeCodeRange(self) -> bool:
        """
        Returns true if the stage has both start and end timeCodes authored in
        the session layer or the root layer of the stage.
        """
    def HasDefaultPrim(self) -> bool:
        """
        Return true if this stage's root layer has an authored opinion for the
        default prim layer metadata.


        This is shorthand for: ::

          stage->GetRootLayer()->HasDefaultPrim();

         Note that this function only consults the stage's root layer. To
        consult a different layer, use the SdfLayer::HasDefaultPrim() API.
        """
    def HasLocalLayer(self, layer: pxr.Sdf.Layer) -> bool:
        """
        Return true if *layer* is one of the layers in this stage's local,
        root layerStack.
        """
    def HasMetadata(self, _key: str | pxr.Ar.ResolvedPath, /) -> bool:
        """
        Returns true if the *key* has a meaningful value, that is, if
        GetMetadata() will provide a value, either because it was authored or
        because the Stage metadata was defined with a meaningful fallback
        value.


        Returns false if C{key} is not allowed as layer metadata.
        """
    def HasMetadataDictKey(self, _key: str | pxr.Ar.ResolvedPath, _keyPath: str | pxr.Ar.ResolvedPath, /) -> bool:
        """
        Return true if there exists any authored or fallback opinion for
        C{key} and C{keyPath}.


        The C{keyPath} is a':'-separated path identifying a value in
        subdictionaries stored in the metadata field at C{key}. If C{keyPath}
        is empty, returns C{false}.

        Returns false if C{key} is not allowed as layer metadata.

        Dictionary-valued Metadata
        """
    def IsLayerMuted(self, layerIdentifier: str | pxr.Ar.ResolvedPath) -> bool:
        """
        Returns true if the layer specified by C{layerIdentifier} is muted in
        this cache, false otherwise.


        See documentation on MuteLayer for details on how C{layerIdentifier}
        is compared to the layers that have been muted.
        """
    @staticmethod
    def IsSupportedFile(filePath: str | pxr.Ar.ResolvedPath) -> bool:
        """
        Indicates whether the specified file is supported by UsdStage.


        This function is a cheap way to determine whether a file might be
        open-able with UsdStage::Open. It is purely based on the given
        C{filePath} and does not open the file or perform analysis on the
        contents. As such, UsdStage::Open may still fail even if this function
        returns true.
        """
    def Load(self, path: pxr.Sdf.Path | str = ..., policy: LoadPolicy = ...) -> Prim:
        """
        Modify this stage's load rules to load the prim at C{path}, its
        ancestors, and all of its descendants if C{policy} is
        UsdLoadWithDescendants.


        If C{policy} is UsdLoadWithoutDescendants, then payloads on descendant
        prims are not loaded.

        See Working Set Management for more information.
        """
    def LoadAndUnload(self, loadSet: typing.Iterable[pxr.Sdf.Path | str], unloadSet: typing.Iterable[pxr.Sdf.Path | str], policy: LoadPolicy = ...) -> None:
        """
        Unload and load the given path sets.


        The effect is as if the unload set were processed first followed by
        the load set.

        This is equivalent to calling UsdStage::Unload for each item in the
        unloadSet followed by UsdStage::Load for each item in the loadSet,
        however this method is more efficient as all operations are committed
        in a single batch. The C{policy} argument is described in the
        documentation for Load() .

        See Working Set Management for more information.
        """
    def MuteAndUnmuteLayers(self, muteLayers: typing.Iterable[str | pxr.Ar.ResolvedPath], unmuteLayers: typing.Iterable[str | pxr.Ar.ResolvedPath]) -> None:
        """
        Mute and unmute the layers identified in C{muteLayers} and
        C{unmuteLayers}.



        This is equivalent to calling UsdStage::UnmuteLayer for each layer in
        C{unmuteLayers} followed by UsdStage::MuteLayer for each layer in
        C{muteLayers}, however this method is more efficient as all operations
        are committed in a single batch.
        """
    def MuteLayer(self, layerIdentifier: str | pxr.Ar.ResolvedPath) -> None:
        """
        Mute the layer identified by C{layerIdentifier}.


        Muted layers are ignored by the stage; they do not participate in
        value resolution or composition and do not appear in any LayerStack.
        If the root layer of a reference or payload LayerStack is muted, the
        behavior is as if the muted layer did not exist, which means a
        composition error will be generated.

        A canonical identifier for each layer in C{layersToMute} will be
        computed using ArResolver::CreateIdentifier using the stage's root
        layer as the anchoring asset. Any layer encountered during composition
        with the same identifier will be considered muted and ignored.

        Note that muting a layer will cause this stage to release all
        references to that layer. If no other client is holding on to
        references to that layer, it will be unloaded. In this case, if there
        are unsaved edits to the muted layer, those edits are lost.  Since
        anonymous layers are not serialized, muting an anonymous layer will
        cause that layer and its contents to be lost in this case.

        Muting a layer that has not been used by this stage is not an error.
        If that layer is encountered later, muting will take effect and that
        layer will be ignored.

        The root layer of this stage may not be muted; attempting to do so
        will generate a coding error.
        """
    @overload
    @staticmethod
    def Open(filePath: str | pxr.Ar.ResolvedPath, load: Stage.InitialLoadSet = ...) -> Stage:
        """
        Attempt to find a matching existing stage in a cache if
        UsdStageCacheContext objects exist on the stack.


        Failing that, create a new stage and recursively compose prims defined
        within and referenced by the layer at C{filePath}, which must already
        exist.

        The initial set of prims to load on the stage can be specified using
        the C{load} parameter.

        UsdStage::InitialLoadSet. If C{pathResolverContext} is provided it
        will be bound when opening the root layer at C{filePath} and whenever
        asset path resolution is done for this stage, regardless of what other
        context may be bound at that time. Otherwise Usd will open the root
        layer with no context bound, then create a context for all future
        asset path resolution for the stage by calling
        ArResolver::CreateDefaultContextForAsset with the layer's repository
        path if the layer has one, otherwise its resolved path.
        """
    @overload
    @staticmethod
    def Open(filePath: str | pxr.Ar.ResolvedPath, pathResolverContext: pxr.Ar.ResolverContext, load: Stage.InitialLoadSet = ...) -> Stage:
        """
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        """
    @overload
    @staticmethod
    def Open(rootLayer: pxr.Sdf.Layer, load: Stage.InitialLoadSet = ...) -> Stage:
        """
        Open a stage rooted at C{rootLayer}.


        Attempt to find a stage that matches the passed arguments in a
        UsdStageCache if UsdStageCacheContext objects exist on the calling
        stack. If a matching stage is found, return that stage. Otherwise,
        create a new stage rooted at C{rootLayer}.

        Invoking an overload that does not take a C{sessionLayer} argument
        will create a stage with an anonymous in-memory session layer. To
        create a stage without a session layer, pass TfNullPtr (or None in
        python) as the C{sessionLayer} argument.

        The initial set of prims to load on the stage can be specified using
        the C{load} parameter.

        UsdStage::InitialLoadSet. If C{pathResolverContext} is provided it
        will be bound when whenever asset path resolution is done for this
        stage, regardless of what other context may be bound at that time.
        Otherwise Usd will create a context for all future asset path
        resolution for the stage by calling
        ArResolver::CreateDefaultContextForAsset with the layer's repository
        path if the layer has one, otherwise its resolved path.

        When searching for a matching stage in bound UsdStageCache s, only the
        provided arguments matter for cache lookup. For example, if only a
        root layer (or a root layer file path) is provided, the first stage
        found in any cache that has that root layer is returned. So, for
        example if you require that the stage have no session layer, you must
        explicitly specify TfNullPtr (or None in python) for the sessionLayer
        argument.
        """
    @overload
    @staticmethod
    def Open(rootLayer: pxr.Sdf.Layer, sessionLayer: pxr.Sdf.Layer, load: Stage.InitialLoadSet = ...) -> Stage:
        """
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        """
    @overload
    @staticmethod
    def Open(rootLayer: pxr.Sdf.Layer, pathResolverContext: pxr.Ar.ResolverContext, load: Stage.InitialLoadSet = ...) -> Stage:
        """
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        """
    @overload
    @staticmethod
    def Open(rootLayer: pxr.Sdf.Layer, sessionLayer: pxr.Sdf.Layer, pathResolverContext: pxr.Ar.ResolverContext, load: Stage.InitialLoadSet = ...) -> Stage:
        """
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        """
    @overload
    @staticmethod
    def OpenMasked(filePath: str | pxr.Ar.ResolvedPath, mask: StagePopulationMask, load: Stage.InitialLoadSet = ...) -> Stage:
        """
        Create a new stage and recursively compose prims defined within and
        referenced by the layer at C{filePath} which must already exist,
        subject to C{mask}.


        These OpenMasked() methods do not automatically consult or populate
        UsdStageCache s.

        The initial set of prims to load on the stage can be specified using
        the C{load} parameter.

        UsdStage::InitialLoadSet. If C{pathResolverContext} is provided it
        will be bound when opening the root layer at C{filePath} and whenever
        asset path resolution is done for this stage, regardless of what other
        context may be bound at that time. Otherwise Usd will open the root
        layer with no context bound, then create a context for all future
        asset path resolution for the stage by calling
        ArResolver::CreateDefaultContextForAsset with the layer's repository
        path if the layer has one, otherwise its resolved path.
        """
    @overload
    @staticmethod
    def OpenMasked(filePath: str | pxr.Ar.ResolvedPath, pathResolverContext: pxr.Ar.ResolverContext, mask: StagePopulationMask, load: Stage.InitialLoadSet = ...) -> Stage:
        """
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        """
    @overload
    @staticmethod
    def OpenMasked(rootLayer: pxr.Sdf.Layer, mask: StagePopulationMask, load: Stage.InitialLoadSet = ...) -> Stage:
        """
        Open a stage rooted at C{rootLayer} and with limited population
        subject to C{mask}.


        These OpenMasked() methods do not automatically consult or populate
        UsdStageCache s.

        Invoking an overload that does not take a C{sessionLayer} argument
        will create a stage with an anonymous in-memory session layer. To
        create a stage without a session layer, pass TfNullPtr (or None in
        python) as the C{sessionLayer} argument.

        The initial set of prims to load on the stage can be specified using
        the C{load} parameter.

        UsdStage::InitialLoadSet. If C{pathResolverContext} is provided it
        will be bound when whenever asset path resolution is done for this
        stage, regardless of what other context may be bound at that time.
        Otherwise Usd will create a context for all future asset path
        resolution for the stage by calling
        ArResolver::CreateDefaultContextForAsset with the layer's repository
        path if the layer has one, otherwise its resolved path.
        """
    @overload
    @staticmethod
    def OpenMasked(rootLayer: pxr.Sdf.Layer, sessionLayer: pxr.Sdf.Layer, mask: StagePopulationMask, load: Stage.InitialLoadSet = ...) -> Stage:
        """
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        """
    @overload
    @staticmethod
    def OpenMasked(rootLayer: pxr.Sdf.Layer, pathResolverContext: pxr.Ar.ResolverContext, mask: StagePopulationMask, load: Stage.InitialLoadSet = ...) -> Stage:
        """
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        """
    @overload
    @staticmethod
    def OpenMasked(rootLayer: pxr.Sdf.Layer, sessionLayer: pxr.Sdf.Layer, pathResolverContext: pxr.Ar.ResolverContext, mask: StagePopulationMask, load: Stage.InitialLoadSet = ...) -> Stage:
        """
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        """
    def OverridePrim(self, path: pxr.Sdf.Path | str) -> Prim:
        """
        Attempt to ensure a *UsdPrim* at C{path} exists on this stage.


        If a prim already exists at C{path}, return it. Otherwise author
        *SdfPrimSpecs* with *specifier* == *SdfSpecifierOver* and empty
        *typeName* at the current EditTarget to create this prim and any
        nonexistent ancestors, then return it.

        The given *path* must be an absolute prim path that does not contain
        any variant selections.

        If it is impossible to author any of the necessary PrimSpecs, (for
        example, in case *path* cannot map to the current UsdEditTarget 's
        namespace) issue an error and return an invalid *UsdPrim*.

        If an ancestor of C{path} identifies an *inactive* prim, author scene
        description as described above but return an invalid prim, since the
        resulting prim is descendant to an inactive prim.
        """
    def Reload(self) -> None:
        """
        Calls SdfLayer::Reload on all layers contributing to this stage,
        except session layers and sublayers of session layers.


        This includes non-session sublayers, references and payloads. Note
        that reloading anonymous layers clears their content, so invoking
        Reload() on a stage constructed via CreateInMemory() will clear its
        root layer.

        This method is considered a mutation, which has potentially global
        effect! Unlike the various Load() methods whose actions affect only
        B{this stage}, Reload() may cause layers to change their contents, and
        because layers are global resources shared by potentially many Stages,
        calling Reload() on one stage may result in a mutation to any number
        of stages. In general, unless you are highly confident your stage is
        the only consumer of its layers, you should only call Reload() when
        you are assured no other threads may be reading from any Stages.
        """
    def RemovePrim(self, path: pxr.Sdf.Path | str) -> bool:
        """
        Remove all scene description for the given C{path} and its subtree *in
        the current UsdEditTarget*.


        This method does not do what you might initially think! Calling this
        function will not necessarily cause the UsdPrim at C{path} on this
        stage to disappear. Completely eradicating a prim from a composition
        can be an involved process, involving edits to many contributing
        layers, some of which (in many circumstances) will not be editable by
        a client. This method is a surgical instrument that *can* be used
        iteratively to effect complete removal of a prim and its subtree from
        namespace, assuming the proper permissions are acquired, but more
        commonly it is used to perform layer-level operations; e.g.: ensuring
        that a given layer (as expressed by a UsdEditTarget) provides no
        opinions for a prim and its subtree.

        Generally, if your eye is attracted to this method, you probably want
        to instead use UsdPrim::SetActive(false), which will provide the
        composed effect of removing the prim and its subtree from the
        composition, without actually removing any scene description, which as
        a bonus, means that the effect is reversible at a later time!
        """
    def ResolveIdentifierToEditTarget(self, identifier: str | pxr.Ar.ResolvedPath) -> str:
        '''
        Resolve the given identifier using this stage\'s ArResolverContext and
        the layer of its GetEditTarget() as an anchor for relative references
        (e.g.


        @./siblingFile.usd@).

        a non-empty string containing either the same identifier that was
        passed in (if the identifier refers to an already-opened layer or
        an"anonymous", in-memory layer), or a resolved layer filepath. If the
        identifier was not resolvable, return the empty string.
        '''
    def Save(self) -> None:
        """
        Calls SdfLayer::Save on all dirty layers contributing to this stage
        except session layers and sublayers of session layers.


        This function will emit a warning and skip each dirty anonymous layer
        it encounters, since anonymous layers cannot be saved with
        SdfLayer::Save. These layers must be manually exported by calling
        SdfLayer::Export.
        """
    def SaveSessionLayers(self) -> None:
        """
        Calls SdfLayer::Save on all dirty session layers and sublayers of
        session layers contributing to this stage.


        This function will emit a warning and skip each dirty anonymous layer
        it encounters, since anonymous layers cannot be saved with
        SdfLayer::Save. These layers must be manually exported by calling
        SdfLayer::Export.
        """
    @staticmethod
    def SetColorConfigFallbacks(colorConfiguration: pxr.Sdf.AssetPath | str = ..., colorManagementSystem: str | pxr.Ar.ResolvedPath = ...) -> None:
        """
        Sets the global fallback values of color configuration metadata which
        includes the'colorConfiguration'asset path and the name of the color
        management system.


        This overrides any fallback values authored in plugInfo files.

        If the specified value of C{colorConfiguration} or
        C{colorManagementSystem} is empty, then the corresponding fallback
        value isn't set. In other words, for this call to have an effect, at
        least one value must be non-empty. Additionally, these can't be reset
        to empty values.

        GetColorConfigFallbacks() Color Configuration API
        """
    def SetColorConfiguration(self, _colorConfig: pxr.Sdf.AssetPath | str, /) -> None:
        """
        Sets the default color configuration to be used to interpret the per-
        attribute color-spaces in the composed USD stage.


        This is specified as asset path which can be resolved to the color
        spec file.

        Color Configuration API
        """
    def SetColorManagementSystem(self, _cms: str | pxr.Ar.ResolvedPath, /) -> None:
        """
        Sets the name of the color management system used to interpret the
        color configuration file pointed at by the colorConfiguration
        metadata.


        Color Configuration API
        """
    def SetDefaultPrim(self, prim: Prim) -> None:
        """
        Set the default prim layer metadata in this stage's root layer.


        This is shorthand for: ::

          stage->GetRootLayer()->SetDefaultPrim(prim.GetName());

         Note that this function always authors to the stage's root layer. To
        author to a different layer, use the SdfLayer::SetDefaultPrim() API.
        """
    def SetEditTarget(self, editTarget: EditTarget | pxr.Sdf.Layer) -> None:
        """
        Set the stage's EditTarget.


        If *editTarget.IsLocalLayer()*, check to see if it's a layer in this
        stage's local LayerStack. If not, issue an error and do nothing. If
        *editTarget* is invalid, issue an error and do nothing. If
        *editTarget* differs from the stage's current EditTarget, set the
        EditTarget and send UsdNotice::StageChangedEditTarget. Otherwise do
        nothing.
        """
    def SetEndTimeCode(self, _unknownArg1: float, /) -> None:
        """
        Sets the stage's end timeCode.


        The end timeCode is set in the current EditTarget, if it is the root
        layer of the stage or the session layer associated with the stage. If
        the current EditTarget is neither, a warning is issued and the end
        timeCode is not set.
        """
    def SetFramesPerSecond(self, _framesPerSecond: float, /) -> None:
        """
        Sets the stage's framesPerSecond value.


        The framesPerSecond value is set in the current EditTarget, if it is
        the root layer of the stage or the session layer associated with the
        stage. If the current EditTarget is neither, a warning is issued and
        no value is set.

        GetFramesPerSecond()
        """
    @staticmethod
    def SetGlobalVariantFallbacks(_fallbacks: dict, /) -> None:
        """
        Set the global variant fallback preferences used in new UsdStages.


        This overrides any fallbacks configured in plugin metadata, and only
        affects stages created after this call.

        This does not affect existing UsdStages.
        """
    def SetInterpolationType(self, _interpolationType: InterpolationType, /) -> None:
        """
        Sets the interpolation type used during value resolution for all
        attributes on this stage.


        Changing this will cause a UsdNotice::StageContentsChanged notice to
        be sent, as values at times where no samples are authored may have
        changed.
        """
    def SetLoadRules(self, rules: StageLoadRules) -> None:
        """
        Set the UsdStageLoadRules to govern payload inclusion on this stage.


        This rebuilds the stage's entire prim hierarchy to follow C{rules}.

        Note that subsequent calls to Load() , Unload() , LoadAndUnload() will
        modify this stages load rules as described in the documentation for
        those member functions.

        See Working Set Management for more information.
        """
    def SetMetadata(self, _key: str | pxr.Ar.ResolvedPath, _value: Any, /) -> bool:
        """
        Set the value of Stage metadatum C{key} to C{value}, if the stage's
        current UsdEditTarget is the root or session layer.


        If the current EditTarget is any other layer, raise a coding error.

        true if authoring was successful, false otherwise. Generates a coding
        error if C{key} is not allowed as layer metadata.

        General Metadata in USD
        """
    def SetMetadataByDictKey(self, _key: str | pxr.Ar.ResolvedPath, _keyPath: str | pxr.Ar.ResolvedPath, _value: Any, /) -> bool:
        """
        Author C{value} to the field identified by C{key} and C{keyPath} at
        the current EditTarget.


        The C{keyPath} is a':'-separated path identifying a value in
        subdictionaries stored in the metadata field at C{key}. If C{keyPath}
        is empty, no action is taken.

        true if the value is authored successfully, false otherwise. Generates
        a coding error if C{key} is not allowed as layer metadata.

        Dictionary-valued Metadata
        """
    def SetPopulationMask(self, mask: StagePopulationMask) -> None:
        """
        Set this stage's population mask and recompose the stage.
        """
    def SetStartTimeCode(self, _unknownArg1: float, /) -> None:
        """
        Sets the stage's start timeCode.


        The start timeCode is set in the current EditTarget, if it is the root
        layer of the stage or the session layer associated with the stage. If
        the current EditTarget is neither, a warning is issued and the start
        timeCode is not set.
        """
    def SetTimeCodesPerSecond(self, _timeCodesPerSecond: float, /) -> None:
        """
        Sets the stage's timeCodesPerSecond value.


        The timeCodesPerSecond value is set in the current EditTarget, if it
        is the root layer of the stage or the session layer associated with
        the stage. If the current EditTarget is neither, a warning is issued
        and no value is set.

        GetTimeCodesPerSecond()
        """
    @overload
    def Traverse(self) -> PrimRange:
        '''
        Traverse the active, loaded, defined, non-abstract prims on this stage
        depth-first.


        Traverse() returns a UsdPrimRange, which allows low-latency traversal,
        with the ability to prune subtrees from traversal. It is python
        iterable, so in its simplest form, one can do: ::

          for prim in stage.Traverse():
              print prim.GetPath()

        If either a pre-and-post-order traversal or a traversal rooted at a
        particular prim is desired, construct a UsdPrimRange directly.

        You\'ll need to use the returned UsdPrimRange \'s iterator to perform
        actions such as pruning subtrees. See the"Using Usd.PrimRange
        inpython"section in UsdPrimRange for more details and examples.

        This is equivalent to UsdPrimRange::Stage() .
        '''
    @overload
    def Traverse(self, predicate: _PrimFlagsPredicate | _Term) -> PrimRange:
        """
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        Traverse the prims on this stage subject to C{predicate}.


        This is equivalent to UsdPrimRange::Stage() .
        """
    def TraverseAll(self) -> PrimRange:
        """
        Traverse all the prims on this stage depth-first.



        Traverse()

        UsdPrimRange::Stage()
        """
    def Unload(self, path: pxr.Sdf.Path | str = ...) -> None:
        """
        Modify this stage's load rules to unload the prim and its descendants
        specified by C{path}.


        See Working Set Management for more information.
        """
    def UnmuteLayer(self, layerIdentifier: str | pxr.Ar.ResolvedPath) -> None:
        """
        Unmute the layer identified by C{layerIdentifier} if it had previously
        been muted.
        """
    def WriteFallbackPrimTypes(self) -> None:
        """
        Writes the fallback prim types defined in the schema registry to the
        stage as dictionary valued fallback prim type metadata.


        If the stage already has fallback prim type metadata, the fallback
        types from the schema registry will be added to the existing metadata,
        only for types that are already present in the dictionary, i.e. this
        won't overwrite existing fallback entries.

        The current edit target determines whether the metadata is written to
        the root layer or the session layer. If the edit target specifies
        another layer besides these, this will produce an error.

        This function can be used at any point before calling Save or Export
        on a stage to record the fallback types for the current schemas. This
        allows another version of Usd to open this stage and treat prim types
        it doesn't recognize as a type it does recognize defined for it in
        this metadata.

        Fallback Prim Types UsdSchemaRegistry::GetFallbackPrimTypes
        """
    def _GetPcpCache(self) -> pxr.Pcp.Cache: ...
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

class StageCache(Boost.Python.instance):
    """
    A strongly concurrency safe collection of UsdStageRefPtr s, enabling
    sharing across multiple clients and threads.


    See UsdStageCacheContext for typical use cases finding UsdStage s in a
    cache and publishing UsdStage s to a cache.

    UsdStageCache is strongly thread safe: all operations other than
    construction and destruction may be performed concurrently.

    Clients typically populate and fetch UsdStage s in caches by binding a
    UsdStageCacheContext object to a cache, then using the
    UsdStage::Open() API. See UsdStageCacheContext for more details.
    Clients may also populate and fetch directly via
    UsdStageCache::Insert() , UsdStageCache::Find() ,
    UsdStageCache::FindOneMatching() , and
    UsdStageCache::FindAllMatching() API.

    Caches provide a mechanism that associates a lightweight key,
    UsdStageCache::Id, with a cached stage. A UsdStageCache::Id can be
    converted to and from long int and string. This can be useful for
    communicating within a third party application that cannot transmit
    arbitrary C++ objects. See UsdStageCache::GetId() .

    Clients may iterate all cache elements using
    UsdStageCache::GetAllStages() and remove elements with
    UsdStageCache::Erase() , UsdStageCache::EraseAll() , and
    UsdStageCache::Clear() .

    Note that this class is a regular type: it can be copied and assigned
    at will. It is not a singleton. Also, since it holds a collection of
    UsdStageRefPtr objects, copying it does not create new UsdStage
    instances, it merely copies the RefPtrs.

    Enabling the USD_STAGE_CACHE TF_DEBUG code will issue debug output for
    UsdStageCache Find/Insert/Erase/Clear operations. Also see
    UsdStageCache::SetDebugName() and UsdStageCache::GetDebugName() .
    """

    class Id(Boost.Python.instance):
        """
        A lightweight identifier that may be used to identify a particular
        cached stage within a UsdStageCache.


        An identifier may be converted to and from long int and string, to
        facilitate use within restricted contexts.

        Id objects are only valid with the stage from which they were
        obtained. It never makes sense to use an Id with a stage other than
        the one it was obtained from.
        """
        __instance_size__: ClassVar[int] = ...
        def __init__(self) -> None:
            """
            Default construct an invalid id.
            """
        @staticmethod
        def FromLongInt(val: int) -> StageCache.Id:
            """
            Create an Id from an integral value.


            The supplied C{val} must have been obtained by calling ToLongInt()
            previously.
            """
        @staticmethod
        def FromString(s: str | pxr.Ar.ResolvedPath) -> StageCache.Id:
            """
            Create an Id from a string value.


            The supplied C{val} must have been obtained by calling ToString()
            previously.
            """
        def IsValid(self) -> bool:
            """
            Return true if this Id is valid.
            """
        def ToLongInt(self) -> int:
            """
            Convert this Id to an integral representation.
            """
        def ToString(self) -> str:
            """
            Convert this Id to a string representation.
            """
        def __bool__(self) -> bool:
            """
            Return true if this Id is valid.
            """
        def __eq__(self, other: object) -> bool: ...
        def __ge__(self, other: object) -> bool: ...
        def __gt__(self, other: object) -> bool: ...
        def __hash__(self) -> int: ...
        def __le__(self, other: object) -> bool: ...
        def __lt__(self, other: object) -> bool: ...
        def __ne__(self, other: object) -> bool: ...
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None:
        """
        Default construct an empty cache.
        """
    @overload
    def __init__(self, _other: StageCache, /) -> None:
        """
        Construct a new cache as a copy of C{other}.
        """
    def Clear(self) -> None:
        """
        Remove all entries from this cache, leaving it empty and equivalent to
        a default-constructed cache.


        Since the cache contains UsdStageRefPtr, erasing a stage from the
        cache will only destroy the stage if no other UsdStageRefPtrs exist
        referring to it.
        """
    @overload
    def Contains(self, stage: Stage) -> bool:
        """
        Return true if C{stage} is present in this cache, false otherwise.
        """
    @overload
    def Contains(self, id: StageCache.Id) -> bool:
        """
        Return true if C{id} is present in this cache, false otherwise.
        """
    @overload
    def Erase(self, id: StageCache.Id) -> bool:
        """
        Erase the stage identified by C{id} from this cache and return true.


        If C{id} is invalid or there is no associated stage in this cache, do
        nothing and return false. Since the cache contains UsdStageRefPtr,
        erasing a stage from the cache will only destroy the stage if no other
        UsdStageRefPtrs exist referring to it.
        """
    @overload
    def Erase(self, stage: Stage) -> bool:
        """
        Erase C{stage} from this cache and return true.


        If C{stage} is not present in this cache, do nothing and return false.
        Since the cache contains UsdStageRefPtr, erasing a stage from the
        cache will only destroy the stage if no other UsdStageRefPtrs exist
        referring to it.
        """
    @overload
    def EraseAll(self, rootLayer: pxr.Sdf.Layer) -> int:
        """
        Erase all stages present in the cache with C{rootLayer} and return the
        number erased.


        Since the cache contains UsdStageRefPtr, erasing a stage from the
        cache will only destroy the stage if no other UsdStageRefPtrs exist
        referring to it.
        """
    @overload
    def EraseAll(self, rootLayer: pxr.Sdf.Layer, sessionLayer: pxr.Sdf.Layer) -> int:
        """
        Erase all stages present in the cache with C{rootLayer} and
        C{sessionLayer} and return the number erased.


        Since the cache contains UsdStageRefPtr, erasing a stage from the
        cache will only destroy the stage if no other UsdStageRefPtrs exist
        referring to it.
        """
    @overload
    def EraseAll(self, rootLayer: pxr.Sdf.Layer, sessionLayer: pxr.Sdf.Layer, pathResolverContext: pxr.Ar.ResolverContext) -> int:
        """
        Erase all stages present in the cache with C{rootLayer},
        C{sessionLayer}, and C{pathResolverContext} and return the number
        erased.


        Since the cache contains UsdStageRefPtr, erasing a stage from the
        cache will only destroy the stage if no other UsdStageRefPtrs exist
        referring to it.
        """
    def Find(self, id: StageCache.Id) -> Stage:
        """
        Find the stage in this cache corresponding to C{id} in this cache.


        If C{id} is not valid (see Id::IsValid() ) or if this cache does not
        have a stage corresponding to C{id}, return null.
        """
    @overload
    def FindAllMatching(self, rootLayer: pxr.Sdf.Layer) -> list[Stage]:
        """
        Find all stages in this cache with C{rootLayer}.


        If there is no matching stage in this cache, return an empty vector.
        """
    @overload
    def FindAllMatching(self, rootLayer: pxr.Sdf.Layer, sessionLayer: pxr.Sdf.Layer) -> list[Stage]:
        """
        Find all stages in this cache with C{rootLayer} and C{sessionLayer}.


        If there is no matching stage in this cache, return an empty vector.
        """
    @overload
    def FindAllMatching(self, rootLayer: pxr.Sdf.Layer, pathResolverContext: pxr.Ar.ResolverContext) -> list[Stage]:
        """
        Find all stages in this cache with C{rootLayer} and
        C{pathResolverContext}.


        If there is no matching stage in this cache, return an empty vector.
        """
    @overload
    def FindAllMatching(self, rootLayer: pxr.Sdf.Layer, sessionLayer: pxr.Sdf.Layer, pathResolverContext: pxr.Ar.ResolverContext) -> list[Stage]:
        """
        Find all stages in this cache with C{rootLayer}, C{sessionLayer}, and
        C{pathResolverContext}.


        If there is no matching stage in this cache, return an empty vector.
        If there is more than one matching stage in this cache, return an
        arbitrary matching one.
        """
    @overload
    def FindOneMatching(self, rootLayer: pxr.Sdf.Layer) -> Stage:
        """
        Find a stage in this cache with C{rootLayer}.


        If there is no matching stage in this cache, return null. If there is
        more than one matching stage in this cache, return an arbitrary
        matching one. See also FindAllMatching() .
        """
    @overload
    def FindOneMatching(self, rootLayer: pxr.Sdf.Layer, sessionLayer: pxr.Sdf.Layer) -> Stage:
        """
        Find a stage in this cache with C{rootLayer} and C{sessionLayer}.


        If there is no matching stage in this cache, return null. If there is
        more than one matching stage in this cache, return an arbitrary
        matching one. See also FindAllMatching() .
        """
    @overload
    def FindOneMatching(self, rootLayer: pxr.Sdf.Layer, pathResolverContext: pxr.Ar.ResolverContext) -> Stage:
        """
        Find a stage in this cache with C{rootLayer} and
        C{pathResolverContext}.


        If there is no matching stage in this cache, return null. If there is
        more than one matching stage in this cache, return an arbitrary
        matching one.

        FindAllMatching()
        """
    @overload
    def FindOneMatching(self, rootLayer: pxr.Sdf.Layer, sessionLayer: pxr.Sdf.Layer, pathResolverContext: pxr.Ar.ResolverContext) -> Stage:
        """
        Find a stage in this cache with C{rootLayer}, C{sessionLayer}, and
        C{pathResolverContext}.


        If there is no matching stage in this cache, return null. If there is
        more than one matching stage in this cache, return an arbitrary
        matching one.

        FindAllMatching()
        """
    def GetAllStages(self) -> list[Stage]:
        """
        Return a vector containing the stages present in this cache.
        """
    def GetDebugName(self) -> str:
        """
        Retrieve this cache's debug name, set with SetDebugName() .


        If no debug name has been assigned, return the empty string.
        """
    def GetId(self, stage: Stage) -> StageCache.Id:
        """
        Return the Id associated with C{stage} in this cache.


        If C{stage} is not present in this cache, return an invalid Id.
        """
    def Insert(self, stage: Stage) -> StageCache.Id:
        """
        Insert C{stage} into this cache and return its associated Id.


        If the given C{stage} is already present in this cache, simply return
        its associated Id.
        """
    def IsEmpty(self) -> bool:
        """
        Return true if this cache holds no stages, false otherwise.
        """
    def SetDebugName(self, _debugName: str | pxr.Ar.ResolvedPath, /) -> None:
        """
        Assign a debug name to this cache.


        This will be emitted in debug output messages when the
        USD_STAGE_CACHES debug flag is enabled. If set to the empty string,
        the cache's address will be used instead.
        """
    def Size(self) -> int:
        """
        Return the number of stages present in this cache.
        """
    def swap(self, arg2: StageCache, /) -> None: ...

class StageCacheContext(Boost.Python.instance):
    """
    A context object that lets the UsdStage::Open() API read from or read
    from and write to a UsdStageCache instance during a scope of
    execution.


    Code examples illustrate typical use: ::

      {
          // A stage cache to work with.
          UsdStageCache stageCache;
  
          // Bind this cache.  UsdStage::Open() will attempt to find a matching
          // stage in the cache.  If none is found, it will open a new stage and
          // insert it into the cache.
          UsdStageCacheContext context(stageCache);
  
          // Since the cache is currently empty, this Open call will not find an
          // existing stage in the cache, but will insert the newly opened stage
          // in it.
          auto stage = UsdStage::Open(<args>);
  
          assert(stageCache.Contains(stage));
      
          // A subsequent Open() call with the same arguments will retrieve the
          // stage from cache.
          auto stage2 = UsdStage::Open(<args>);
          assert(stage2 == stage);
      }

    The UsdStage::Open() API examines caches in UsdStageCacheContexts that
    exist on the stack in the current thread in order starting with the
    most recently created (deepest in the stack) to the least recently
    created.

    The UsdUseButDoNotPopulateCache() function makes a cache available for
    UsdStage::Open() to find stages in, but newly opened stages will not
    be published to it. This can be useful if you want to make use of a
    cache but cannot or do not wish to mutate that cache.

    Passing UsdBlockStageCaches disables cache use entirely (as if no
    UsdStageCacheContexts exist on the stack), while
    UsdBlockStageCachePopulation disables writing to all bound caches (as
    if they were all established with UsdUseButDoNotPopulateCache()).

    Threading note: Different threads have different call stacks, so
    UsdStageCacheContext objects that exist in one thread's stack do not
    influence calls to UsdStage::Open() from a different thread.
    """
    @overload
    def __init__(self, _cache: StageCache, /) -> None:
        """
        Bind a cache for calls to UsdStage::Open() to read from and write to.
        """
    @overload
    def __init__(self, arg2: _NonPopulatingStageCacheWrapper, /) -> None: ...
    @overload
    def __init__(self, arg2: object, /) -> None: ...
    def __enter__(self) -> None: ...
    def __exit__(self, type: type[BaseException] | None, value: BaseException | None, traceback: types.TracebackType | None) -> None: ...

class StageCacheContextBlockType(pxr.Tf.Tf_PyEnumWrapper):
    _baseName: ClassVar[str] = ...
    allValues: ClassVar[tuple] = ...
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def GetValueFromName(name: object) -> Any: ...

class StageLoadRules(Boost.Python.instance):
    """
    This class represents rules that govern payload inclusion on
    UsdStages.


    Rules are represented as pairs of SdfPath and a Rule enum value, one
    of AllRule, OnlyRule, and NoneRule. To understand how rules apply to
    particular paths, see UsdStageLoadRules::GetEffectiveRuleForPath() .

    Convenience methods for manipulating rules by
    typical'Load'and'Unload'operations are provided in
    UsdStageLoadRules::LoadWithoutDescendants() ,
    UsdStageLoadRules::LoadWithDescendants() , UsdStageLoadRules::Unload()
    .

    For finer-grained rule crafting, see AddRule() .

    Remove redundant rules that do not change the effective load state
    with UsdStageLoadRules::Minimize() .
    """

    class Rule(pxr.Tf.Tf_PyEnumWrapper):
        _baseName: ClassVar[str] = ...
        allValues: ClassVar[tuple] = ...
        def __init__(self, *args, **kwargs) -> None:
            """Raises an exception
            This class cannot be instantiated from Python
            """
        @staticmethod
        def GetValueFromName(name: object) -> Any: ...
    AllRule: ClassVar[StageLoadRules.Rule] = ...
    NoneRule: ClassVar[StageLoadRules.Rule] = ...
    OnlyRule: ClassVar[StageLoadRules.Rule] = ...
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None:
        """
        Construct rules that load all payloads.
        """
    @overload
    def __init__(self, _unknownArg1: StageLoadRules, /) -> None: ...
    def AddRule(self, path: pxr.Sdf.Path | str, rule: StageLoadRules.Rule) -> None:
        """
        Add a literal rule. If there's already a rule for C{path}, replace it.
        """
    def GetEffectiveRuleForPath(self, path: pxr.Sdf.Path | str) -> StageLoadRules.Rule:
        '''
        Return the"effective"rule for the given C{path}.


        For example, if the closest ancestral rule of C{path} is an
        C{AllRule}, return C{AllRule}. If the closest ancestral rule of
        C{path} is for C{path} itself and it is an C{OnlyRule}, return
        C{OnlyRule}. Otherwise if there is a closest descendant rule to
        C{path} this is an C{OnlyRule} or an C{AllRule}, return C{OnlyRule}.
        Otherwise return C{NoneRule}.
        '''
    def GetRules(self) -> list[tuple[pxr.Sdf.Path, StageLoadRules.Rule]]:
        """
        Return all the rules as a vector.
        """
    def IsLoaded(self, path: pxr.Sdf.Path | str) -> bool:
        """
        Return true if the given C{path} is considered loaded by these rules,
        or false if it is considered unloaded.


        This is equivalent to GetEffectiveRuleForPath(path) != NoneRule.
        """
    def IsLoadedWithAllDescendants(self, path: pxr.Sdf.Path | str) -> bool:
        """
        Return true if the given C{path} and all descendants are considered
        loaded by these rules; false otherwise.
        """
    def IsLoadedWithNoDescendants(self, path: pxr.Sdf.Path | str) -> bool:
        """
        Return true if the given C{path} and is considered loaded, but none of
        its descendants are considered loaded by these rules; false otherwise.
        """
    @staticmethod
    def LoadAll() -> StageLoadRules:
        """
        Return rules that load all payloads.


        This is equivalent to default-constructed UsdStageLoadRules.
        """
    def LoadAndUnload(self, loadSet: typing.Iterable[pxr.Sdf.Path | str], unloadSet: typing.Iterable[pxr.Sdf.Path | str], policy: LoadPolicy) -> None:
        """
        Add rules as if Unload() was called for each element of C{unloadSet}
        followed by calls to either LoadWithDescendants() (if C{policy} is
        UsdLoadPolicy::LoadWithDescendants) or LoadWithoutDescendants() (if
        C{policy} is UsdLoadPolicy::LoadWithoutDescendants) for each element
        of C{loadSet}.
        """
    @staticmethod
    def LoadNone() -> StageLoadRules:
        """
        Return rules that load no payloads.
        """
    def LoadWithDescendants(self, path: pxr.Sdf.Path | str) -> None:
        """
        Add a rule indicating that C{path}, all its ancestors, and all its
        descendants shall be loaded.


        Any previous rules created by calling LoadWithoutDescendants() or
        Unload() on this path or descendant paths are replaced by this rule.
        For example, calling LoadWithoutDescendants('/World/sets/kitchen')
        followed by LoadWithDescendants('/World/sets') will effectively remove
        the rule created in the first call. See AddRule() for more direct
        manipulation.
        """
    def LoadWithoutDescendants(self, path: pxr.Sdf.Path | str) -> None:
        """
        Add a rule indicating that C{path} and all its ancestors but none of
        its descendants shall be loaded.


        Any previous rules created by calling LoadWithDescendants() or
        Unload() on this path or descendant paths are replaced or restricted
        by this rule. For example, calling LoadWithDescendants('/World/sets')
        followed by LoadWithoutDescendants('/World/sets/kitchen') will cause
        everything under'/World/sets'to load except for those things
        under'/World/sets/kitchen'. See AddRule() for more direct
        manipulation.
        """
    def Minimize(self) -> None:
        """
        Remove any redundant rules to make the set of rules as small as
        possible without changing behavior.
        """
    def SetRules(self, rules: typing.Iterable[tuple[pxr.Sdf.Path | str, StageLoadRules.Rule]]) -> None:
        """
        Set literal rules, must be sorted by SdfPath::operator< .
        """
    def Unload(self, path: pxr.Sdf.Path | str) -> None:
        """
        Add a rule indicating that C{path} and all its descendants shall be
        unloaded.


        Any previous rules created by calling LoadWithDescendants() or
        LoadWithoutDescendants() on this path or descendant paths are replaced
        or restricted by this rule. For example, calling
        LoadWithDescendants('/World/sets') followed by
        Unload('/World/sets/kitchen') will cause everything
        under'/World/sets'to load, except for'/World/sets/kitchen'and
        everything under it.
        """
    def swap(self, other: StageLoadRules) -> None: ...
    def __eq__(self, other: object) -> bool:
        """
        Return true if C{other} has exactly the same set of rules as this.


        Note that this means rules that are functionally equivalent may
        compare inequal. If this is not desired, ensure both sets of rules are
        reduced by Minimize() first.
        """
    def __hash__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...

class StagePopulationMask(Boost.Python.instance):
    """
    This class represents a mask that may be applied to a UsdStage to
    limit the set of UsdPrim s it populates.


    This is useful in cases where clients have a large scene but only wish
    to view or query a single or a handful of objects. For example,
    suppose we have a city block with buildings, cars, crowds of people,
    and a couple of main characters. Some tasks might only require looking
    at a single main character and perhaps a few props. We can create a
    population mask with the paths to the character and props of interest
    and open a UsdStage with that mask. Usd will avoid populating the
    other objects in the scene, saving time and memory. See
    UsdStage::OpenMasked() for more.

    A mask is defined by a set of SdfPath s with the following qualities:
    they are absolute prim paths (or the absolute root path), and no path
    in the set is an ancestor path of any other path in the set other than
    itself. For example, the set of paths ['/a/b','/a/c','/x/y'] is a
    valid mask, but the set of paths ['/a/b','/a/b/c','/x/y'] is
    redundant, since'/a/b'is an ancestor of'/a/b/c'. The path'/a/b/c'may
    be removed. The GetUnion() and Add() methods ensure that no redundant
    paths are added.

    Default-constructed UsdStagePopulationMask s are considered empty (
    IsEmpty() ) and include no paths. A population mask containing
    SdfPath::AbsoluteRootPath() includes all paths.
    """
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None:
        """
        Construct an empty mask that includes no paths.
        """
    @overload
    def __init__(self, arg2: object, /) -> None: ...
    @overload
    def Add(self, _other: StagePopulationMask, /) -> StagePopulationMask:
        """
        Assign this mask to be its union with C{other} and return a reference
        to this mask.
        """
    @overload
    def Add(self, _path: pxr.Sdf.Path | str, /) -> StagePopulationMask:
        """
        Assign this mask to be its union with C{path} and return a reference
        to this mask.
        """
    @staticmethod
    def All() -> StagePopulationMask:
        """
        Return a mask that includes all paths.


        This is the mask that contains the absolute root path.
        """
    def GetIncludedChildNames(self, path: pxr.Sdf.Path | str) -> tuple:
        """
        Return true if this mask includes any child prims beneath C{path},
        false otherwise.


        If only specific child prims beneath C{path} are included, the names
        of those children will be returned in C{childNames}. If all child
        prims beneath C{path} are included, C{childNames} will be empty.
        """
    def GetIntersection(self, other: StagePopulationMask) -> StagePopulationMask:
        """
        Return a mask that is the intersection of this and C{other}.
        """
    def GetPaths(self) -> list[pxr.Sdf.Path]:
        """
        Return the set of paths that define this mask.
        """
    @overload
    def GetUnion(self, other: StagePopulationMask) -> StagePopulationMask:
        """
        Return a mask that is the union of this and C{other}.
        """
    @overload
    def GetUnion(self, path: pxr.Sdf.Path | str) -> StagePopulationMask:
        """
        Return a mask that is the union of this and a mask containing the
        single C{path}.
        """
    @overload
    def Includes(self, other: StagePopulationMask) -> bool:
        """
        Return true if this mask is a superset of C{other}.


        That is, if this mask includes at least every path that C{other}
        includes.
        """
    @overload
    def Includes(self, path: pxr.Sdf.Path | str) -> bool:
        """
        Return true if this mask includes C{path}.


        This is true if C{path} is one of the paths in this mask, or if it is
        either a descendant or an ancestor of one of the paths in this mask.
        """
    def IncludesSubtree(self, path: pxr.Sdf.Path | str) -> bool:
        """
        Return true if this mask includes C{path} and all paths descendant to
        C{path}.


        For example, consider a mask containing the path'/a/b'. Then the
        following holds: ::

          mask.Includes('/a') -> true
          mask.Includes('/a/b') -> true
          mask.IncludesSubtree('/a') -> false
          mask.IncludesSubtree('/a/b') -> true

        """
    @staticmethod
    def Intersection(_l: StagePopulationMask, _r: StagePopulationMask, /) -> StagePopulationMask:
        """
        Return a mask that is the intersection of C{l} and C{r}.
        """
    def IsEmpty(self) -> bool:
        """
        Return true if this mask contains no paths.


        Empty masks include no paths.
        """
    @staticmethod
    def Union(_l: StagePopulationMask, _r: StagePopulationMask, /) -> StagePopulationMask:
        """
        Return a mask that is the union of C{l} and C{r}.
        """
    def __eq__(self, other: object) -> bool:
        """
        Return true if this mask is equivalent to C{other}.
        """
    def __hash__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...

class TimeCode(Boost.Python.instance):
    """
    Represent a time value, which may be either numeric, holding a double
    value, or a sentinel value UsdTimeCode::Default() .


    A UsdTimeCode does *not* represent an SMPTE timecode, although we may,
    in future, support conversion functions between the two. Instead,
    UsdTimeCode is an abstraction that acknowledges that in the principal
    domains of use for USD, there are many different ways of encoding
    time, and USD must be able to capture and translate between all of
    them for interchange, retaining as much intent of the authoring
    application as possible.

    A UsdTimeCode is therefore a unitless, generic time measurement that
    serves as the ordinate for time-sampled data in USD files. A client of
    USD relies on the UsdStage (which in turn consults metadata authored
    in its root layer) to define the mapping of TimeCodes to units like
    seconds and frames.

    UsdStage::GetStartTimeCode()

    UsdStage::GetEndTimeCode()

    UsdStage::GetTimeCodesPerSecond()

    UsdStage::GetFramesPerSecond() As described in TimeSamples, Defaults,
    and Value Resolution, USD optionally provides an
    unvarying,'default'value for every attribute. UsdTimeCode embodies a
    time value that can either be a floating-point sample time, or the
    default.

    All UsdAttribute and derived API that requires a time parameter
    defaults to UsdTimeCode::Default() if the parameter is left
    unspecified, and auto-constructs from a floating-point argument.

    UsdTimeCode::EarliestTime() is provided to aid clients who wish to
    retrieve the first authored timesample for any attribute.
    """

    class Tokens(Boost.Python.instance):
        DEFAULT: ClassVar[str] = ...  # read-only
        EARLIEST: ClassVar[str] = ...  # read-only
        def __init__(self, *args, **kwargs) -> None:
            """Raises an exception
            This class cannot be instantiated from Python
            """
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self, _t: float, /) -> None:
        """
        Construct with optional time value. Impilicitly convert from double.
        """
    @overload
    def __init__(self, _timeCode: TimeCode | float | pxr.Sdf.TimeCode, /) -> None:
        """
        Construct and implicitly cast from SdfTimeCode.
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, arg2: TimeCode | float | pxr.Sdf.TimeCode, /) -> None: ...
    @staticmethod
    def Default() -> TimeCode:
        """
        Produce a UsdTimeCode representing the sentinel value for'default'.



        In inequality comparisons, Default() is considered less than any
        numeric TimeCode, including EarliestTime() , indicative of the fact
        that in UsdAttribute value resolution, the sample at Default() (if
        any) is always weaker than any numeric timeSample in the same layer.
        For more information, see TimeSamples, Defaults, and Value Resolution
        """
    @staticmethod
    def EarliestTime() -> TimeCode:
        """
        Produce a UsdTimeCode representing the lowest/earliest possible
        timeCode.


        Thus, for any given timeSample *s*, its time ordinate *t* will obey:
        t>= UsdTimeCode::EarliestTime()

        This is useful for clients that wish to retrieve the first authored
        timeSample for an attribute, as they can use
        UsdTimeCode::EarliestTime() as the *time* argument to
        UsdAttribute::Get() and UsdAttribute::GetBracketingTimeSamples()
        """
    def GetValue(self) -> float:
        """
        Return the numeric value for this time.


        If this time *IsDefault()*, return a quiet NaN value.
        """
    def IsDefault(self) -> bool:
        """
        Return true if this time represents the'default'sentinel value, false
        otherwise.


        This is equivalent to !IsNumeric().
        """
    def IsEarliestTime(self) -> bool:
        """
        Return true if this time represents the lowest/earliest possible
        timeCode, false otherwise.
        """
    def IsNumeric(self) -> bool:
        """
        Return true if this time represents a numeric value, false otherwise.


        This is equivalent to !IsDefault().
        """
    @staticmethod
    def SafeStep(maxValue: float = ..., maxCompression: float = ...) -> float:
        """
        Produce a safe step value such that for any numeric UsdTimeCode t in
        [-maxValue, maxValue], t +/- (step / maxCompression) != t with a
        safety factor of 2.


        This is shorthand for std::numeric_limits<double>::epsilon() *
        maxValue * maxCompression * 2.0. Such a step value is recommended for
        simulating jump discontinuities in time samples. For example, author
        value x at time t, and value y at time t + SafeStep() . This ensures
        that as the sample times are shifted and scaled, t and t + SafeStep()
        remain distinct so long as they adhere to the C{maxValue} and
        C{maxCompression} limits.
        """
    def __eq__(self, other: object) -> bool: ...
    def __ge__(self, other: object) -> bool: ...
    def __gt__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    def __le__(self, other: object) -> bool: ...
    def __lt__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...

class Tokens(Boost.Python.instance):
    APISchemaBase: ClassVar[str] = ...  # read-only
    ClipsAPI: ClassVar[str] = ...  # read-only
    CollectionAPI: ClassVar[str] = ...  # read-only
    ModelAPI: ClassVar[str] = ...  # read-only
    Typed: ClassVar[str] = ...  # read-only
    apiSchemas: ClassVar[str] = ...  # read-only
    clipSets: ClassVar[str] = ...  # read-only
    clips: ClassVar[str] = ...  # read-only
    collection: ClassVar[str] = ...  # read-only
    collection_MultipleApplyTemplate_: ClassVar[str] = ...  # read-only
    collection_MultipleApplyTemplate_Excludes: ClassVar[str] = ...  # read-only
    collection_MultipleApplyTemplate_ExpansionRule: ClassVar[str] = ...  # read-only
    collection_MultipleApplyTemplate_IncludeRoot: ClassVar[str] = ...  # read-only
    collection_MultipleApplyTemplate_Includes: ClassVar[str] = ...  # read-only
    collection_MultipleApplyTemplate_MembershipExpression: ClassVar[str] = ...  # read-only
    exclude: ClassVar[str] = ...  # read-only
    expandPrims: ClassVar[str] = ...  # read-only
    expandPrimsAndProperties: ClassVar[str] = ...  # read-only
    explicitOnly: ClassVar[str] = ...  # read-only
    fallbackPrimTypes: ClassVar[str] = ...  # read-only
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """

class Typed(SchemaBase):
    '''
    The base class for all *typed* schemas (those that can impart a
    typeName to a UsdPrim), and therefore the base class for all concrete,
    instantiable"IsA"schemas.


    UsdTyped implements a typeName-based query for its override of
    UsdSchemaBase::_IsCompatible() . It provides no other behavior.
    '''
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, prim: Prim) -> None:
        """
        Construct a UsdTyped on UsdPrim C{prim}.


        Equivalent to UsdTyped::Get (prim.GetStage(), prim.GetPath()) for a
        *valid* C{prim}, but will not immediately throw an error for an
        invalid C{prim}
        """
    @overload
    def __init__(self, schemaObj: SchemaBase) -> None:
        """
        Construct a UsdTyped on the prim held by C{schemaObj}.


        Should be preferred over UsdTyped (schemaObj.GetPrim()), as it
        preserves SchemaBase state.
        """
    @staticmethod
    def Get(stage: Stage, path: pxr.Sdf.Path | str) -> Typed:
        """
        Return a UsdTyped holding the prim adhering to this schema at C{path}
        on C{stage}.


        If no prim exists at C{path} on C{stage}, or if the prim at that path
        does not adhere to this schema, return an invalid schema object. This
        is shorthand for the following: ::

          UsdTyped(stage->GetPrimAtPath(path));

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

class UsdCollectionMembershipQuery(Boost.Python.instance):
    __instance_size__: ClassVar[int] = ...
    def __init__(self) -> None: ...
    def GetAsPathExpansionRuleMap(self) -> dict: ...
    def GetIncludedCollections(self) -> list: ...
    def HasExcludes(self) -> bool: ...
    @overload
    def IsPathIncluded(self, path: pxr.Sdf.Path | str) -> bool: ...
    @overload
    def IsPathIncluded(self, path: pxr.Sdf.Path | str, parentExpansionRule: object) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...

class UsdFileFormat(pxr.Sdf.FileFormat):
    """
    File format for USD files.


    When creating a file through the SdfLayer::CreateNew() interface, the
    meaningful SdfFileFormat::FileFormatArguments are as follows:
       - UsdUsdFileFormatTokens->FormatArg, which must be a supported
         format's'Id'. The possible values are UsdUsdaFileFormatTokens->Id or
         UsdUsdcFileFormatTokens->Id.
         If no UsdUsdFileFormatTokens->FormatArg is supplied, the default is
         UsdUsdcFileFormatTokens->Id.
    """

    class Tokens(Boost.Python.instance):
        FormatArg: ClassVar[str] = ...  # read-only
        Id: ClassVar[str] = ...  # read-only
        Target: ClassVar[str] = ...  # read-only
        Version: ClassVar[str] = ...  # read-only
        def __init__(self, *args, **kwargs) -> None:
            """Raises an exception
            This class cannot be instantiated from Python
            """
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def GetUnderlyingFormatForLayer(_layer: pxr.Sdf.Layer, /) -> str:
        '''
        Returns the value of the"format"argument to be used in the
        FileFormatArguments when exporting or saving the given layer.


        Returns an empty token if the given layer does not have this file
        format.
        '''

class VariantSet(Boost.Python.instance):
    """
    A UsdVariantSet represents a single VariantSet in USD (e.g.


    modelingVariant or shadingVariant), which can have multiple variations
    that express different sets of opinions about the scene description
    rooted at the prim that defines the VariantSet.

    (More detailed description of variants to follow)
    """
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """
    def AddVariant(self, variantName: str | pxr.Ar.ResolvedPath, position: ListPosition = ...) -> bool:
        '''
        Author a variant spec for *variantName* in this VariantSet at the
        stage\'s current EditTarget, in the position specified by C{position}.


        Return true if the spec was successfully authored, false otherwise.

        This will create the VariantSet itself, if necessary, so as long as
        UsdPrim "prim"is valid, the following should always work: ::

          UsdVariantSet vs = prim.GetVariantSet("myVariantSet");
          vs.AddVariant("myFirstVariation");
          vs.SetVariantSelection("myFirstVariation");
          {
              UsdEditContext ctx(vs.GetVariantEditContext());
              // Now all of our subsequent edits will go "inside" the 
              // \'myFirstVariation\' variant of \'myVariantSet\'
          }

        '''
    def BlockVariantSelection(self) -> bool:
        """
        Block any weaker selections for this VariantSet by authoring an empty
        string at the stage's current EditTarget.


        Return true on success, false otherwise.
        """
    def ClearVariantSelection(self) -> bool:
        """
        Clear any selection for this VariantSet from the current EditTarget.


        Return true on success, false otherwise.
        """
    def GetName(self) -> str:
        """
        Return this VariantSet's name.
        """
    def GetPrim(self) -> Prim:
        """
        Return this VariantSet's held prim.
        """
    def GetVariantEditContext(self, layer: pxr.Sdf.Layer = ...) -> EditContext:
        '''
        Helper function for configuring a UsdStage \'s EditTarget to author
        into the currently selected variant.


        Returns configuration for a UsdEditContext

        To begin editing into VariantSet *varSet\'s* currently selected
        variant:

        In C++, we would use the following pattern: ::

          {
              UsdEditContext ctxt(varSet.GetVariantEditContext());
  
              // All Usd mutation of the UsdStage on which varSet sits will
              // now go "inside" the currently selected variant of varSet
          }

        In python, the pattern is: ::

          with varSet.GetVariantEditContext():
              # Now sending mutations to current variant

        See GetVariantEditTarget() for discussion of C{layer} parameter
        '''
    def GetVariantEditTarget(self, layer: pxr.Sdf.Layer = ...) -> EditTarget:
        """
        Return a *UsdEditTarget* that edits the currently selected variant in
        this VariantSet in *layer*.


        If there is no currently selected variant in this VariantSet, return
        an invalid EditTarget.

        If *layer* is unspecified, then we will use the layer of our prim's
        stage's current UsdEditTarget.

        Currently, we require *layer* to be in the stage's local LayerStack
        (see UsdStage::HasLocalLayer() ), and will issue an error and return
        an invalid EditTarget if *layer* is not. We may relax this restriction
        in the future, if need arises, but it introduces several complications
        in specification and behavior.
        """
    def GetVariantNames(self) -> list[str]:
        """
        Return the composed variant names for this VariantSet, ordered
        lexicographically.
        """
    def GetVariantSelection(self) -> str:
        """
        Return the variant selection for this VariantSet.


        If there is no selection, return the empty string.
        """
    def HasAuthoredVariant(self, _variantName: str | pxr.Ar.ResolvedPath, /) -> bool:
        """
        Returns true if this VariantSet already possesses a variant.
        """
    def HasAuthoredVariantSelection(self) -> str:
        """
        Returns true if there is a selection authored for this VariantSet in
        any layer.


        If requested, the variant selection (if any) will be returned in
        C{value}.
        """
    def IsValid(self) -> bool:
        """
        Is this UsdVariantSet object usable? If not, calling any of its other
        methods is likely to crash.
        """
    def SetVariantSelection(self, variantName: str | pxr.Ar.ResolvedPath) -> bool:
        """
        Author a variant selection for this VariantSet, setting it to
        *variantName* in the stage's current EditTarget.


        If C{variantName} is empty, clear the variant selection (see
        ClearVariantSelection). Call BlockVariantSelection to explicitly set
        an empty variant selection.

        Return true if the selection was successfully authored or cleared,
        false otherwise.
        """
    def __bool__(self) -> bool:
        """
        Equivalent to IsValid() .
        """

class VariantSets(Boost.Python.instance):
    """
    UsdVariantSets represents the collection of VariantSets that are
    present on a UsdPrim.


    A UsdVariantSets object, retrieved from a prim via
    UsdPrim::GetVariantSets() , provides the API for interrogating and
    modifying the composed list of VariantSets active defined on the prim,
    and also the facility for authoring a VariantSet *selection* for any
    of those VariantSets.
    """
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """
    def AddVariantSet(self, variantSetName: str | pxr.Ar.ResolvedPath, position: ListPosition = ...) -> VariantSet:
        """
        Find an existing, or create a new VariantSet on the originating
        UsdPrim, named C{variantSetName}.


        This step is not always necessary, because if this UsdVariantSets
        object is valid, then ::

          varSetsObj.GetVariantSet(variantSetName).AddVariant(variantName);

         will always succeed, creating the VariantSet first, if necessary.
        This method exists for situations in which you want to create a
        VariantSet without necessarily populating it with variants.
        """
    def GetAllVariantSelections(self) -> dict:
        """
        Returns the composed map of all variant selections authored on the the
        originating UsdPrim, regardless of whether a corresponding variant set
        exists.
        """
    def GetNames(self) -> list[str]:
        """
        Compute the list of all VariantSets authored on the originating
        UsdPrim.


        Always return true. Clear the contents of C{names} and store the
        result there.
        """
    def GetVariantSelection(self, variantSetName: str | pxr.Ar.ResolvedPath) -> str:
        """
        Return the composed variant selection for the VariantSet named
        *variantSetName*.


        If there is no selection, (or C{variantSetName} does not exist) return
        the empty string.
        """
    def GetVariantSet(self, variantSetName: str | pxr.Ar.ResolvedPath) -> VariantSet:
        """
        Return a UsdVariantSet object for C{variantSetName}.


        This always succeeds, although the returned VariantSet will be invalid
        if the originating prim is invalid
        """
    def HasVariantSet(self, variantSetName: str | pxr.Ar.ResolvedPath) -> bool:
        """
        Returns true if a VariantSet named C{variantSetName} exists on the
        originating prim.
        """
    def SetSelection(self, variantSetName: str | pxr.Ar.ResolvedPath, variantName: str | pxr.Ar.ResolvedPath) -> bool: ...

class ZipFile(Boost.Python.instance):
    """
    Class for reading a zip file.


    This class is primarily intended to support the .usdz file format. It
    is not a general-purpose zip reader, as it does not implement the full
    zip file specification. In particular:

       - This class does not natively support decompressing data from a
         zip archive. Clients may access the data exactly as stored in the file
         and perform their own decompression if desired.

       - This class does not rely on the central directory in order to
         read the contents of the file. This allows it to operate on partial
         zip archives. However, this also means it may handle certain zip files
         incorrectly. For example, if a file was deleted from a zip archive by
         just removing its central directory header, that file will still be
         found by this class.

    """

    class FileInfo(Boost.Python.instance):
        """
        Information for a file in the zip archive.
        """
        def __init__(self, *args, **kwargs) -> None:
            """Raises an exception
            This class cannot be instantiated from Python
            """
        @property
        def compressionMethod(self): ...
        @property
        def crc(self): ...
        @property
        def dataOffset(self): ...
        @property
        def encrypted(self): ...
        @property
        def size(self): ...
        @property
        def uncompressedSize(self): ...
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """
    def DumpContents(self) -> None:
        """
        Print out listing of contents of this zip archive to stdout.


        For diagnostic purposes only.
        """
    def GetFile(self, path: object) -> Any: ...
    def GetFileInfo(self, path: object) -> Any: ...
    def GetFileNames(self) -> list: ...
    @staticmethod
    def Open(filePath: str | pxr.Ar.ResolvedPath) -> ZipFile:
        """
        Opens the zip archive at C{filePath}.


        Returns invalid object on error.
        """

class ZipFileWriter(Boost.Python.instance):
    """
    Class for writing a zip file.


    This class is primarily intended to support the .usdz file format. It
    is not a general-purpose zip writer, as it does not implement the full
    zip file specification. However, all files written by this class
    should be valid zip files and readable by external zip modules and
    utilities.
    """
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """
    def AddFile(self, filePath: str | pxr.Ar.ResolvedPath, filePathInArchive: str | pxr.Ar.ResolvedPath = ...) -> str:
        """
        Adds the file at C{filePath} to the zip archive with no compression
        applied.


        If C{filePathInArchive} is non-empty, the file will be added at that
        path in the archive. Otherwise, it will be added at C{filePath}.

        Returns the file path used to identify the file in the zip archive on
        success. This path conforms to the zip file specification and may not
        be the same as C{filePath} or C{filePathInArchive}. Returns an empty
        string on failure.
        """
    @staticmethod
    def CreateNew(filePath: str | pxr.Ar.ResolvedPath) -> ZipFileWriter:
        """
        Create a new file writer with C{filePath} as the destination file path
        where the zip archive will be written.


        The zip file will not be written to C{filePath} until the writer is
        destroyed or Save() is called.

        Returns an invalid object on error.
        """
    def Discard(self) -> None:
        """
        Discards the zip archive so that it is not saved to the destination
        file path.


        Once discarded, the file writer is invalid and may not be reused.
        """
    def Save(self) -> bool:
        """
        Finalizes the zip archive and saves it to the destination file path.


        Once saved, the file writer is invalid and may not be reused. Returns
        true on success, false otherwise.
        """
    def __enter__(self) -> ZipFileWriter: ...
    def __exit__(self, type: type[BaseException] | None, value: BaseException | None, traceback: types.TracebackType | None) -> None: ...

class _CanApplyAPIResult(Boost.Python.instance):
    __instance_size__: ClassVar[int] = ...
    def __init__(self, arg2: bool, arg3: object, /) -> None: ...
    def __bool__(self) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    def __getitem__(self, arg2: int, /) -> Any: ...
    def __ne__(self, other: object) -> bool: ...
    @property
    def whyNot(self): ...

class _CanApplyResult(Boost.Python.instance):
    __instance_size__: ClassVar[int] = ...
    def __init__(self, arg2: bool, arg3: object, /) -> None: ...
    def __bool__(self) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    def __getitem__(self, arg2: int, /) -> Any: ...
    def __ne__(self, other: object) -> bool: ...
    @property
    def whyNot(self): ...

class _NonPopulatingStageCacheWrapper(Boost.Python.instance):
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """

class _PrimFlagsConjunction(_PrimFlagsPredicate):
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """
    def __and__(self, arg2: _Term, /) -> Any: ...
    def __iand__(self, arg2: _Term, /) -> Any: ...
    def __invert__(self) -> Any: ...
    def __rand__(self, arg2: _Term, /) -> Any: ...

class _PrimFlagsDisjunction(_PrimFlagsPredicate):
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """
    def __invert__(self) -> Any: ...
    def __ior__(self, arg2: _Term, /) -> Any: ...
    def __or__(self, arg2: _Term, /) -> Any: ...
    def __ror__(self, arg2: _Term, /) -> Any: ...

class _PrimFlagsPredicate(Boost.Python.instance):
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def Contradiction() -> _PrimFlagsPredicate: ...
    @staticmethod
    def Tautology() -> _PrimFlagsPredicate: ...
    def __call__(self, arg2: Prim, /) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...

class _Term(Boost.Python.instance):
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """
    def __and__(self, arg2: _Term, /) -> Any: ...
    def __eq__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    def __invert__(self) -> Any: ...
    def __ne__(self, other: object) -> bool: ...
    def __or__(self, arg2: _Term, /) -> Any: ...

class _UsdNamespaceEditorCanEditResult(Boost.Python.instance):
    __instance_size__: ClassVar[int] = ...
    def __init__(self, arg2: bool, arg3: object, /) -> None: ...
    def __bool__(self) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    def __getitem__(self, arg2: int, /) -> Any: ...
    def __ne__(self, other: object) -> bool: ...
    @property
    def whyNot(self): ...

def ComputeIncludedObjectsFromCollection(query: UsdCollectionMembershipQuery, stage: Stage, predicate: _PrimFlagsPredicate | _Term = ...) -> list[Object]:
    """
    Returns all the usd objects that satisfy the predicate, C{pred} in the
    collection represented by the UsdCollectionMembershipQuery object,
    C{query}.


    The results depends on the load state of the UsdStage, C{stage}.
    """
def ComputeIncludedPathsFromCollection(query: UsdCollectionMembershipQuery, stage: Stage, predicate: _PrimFlagsPredicate | _Term = ...) -> list[pxr.Sdf.Path]:
    """
    Returns all the paths that satisfy the predicate, C{pred} in the
    collection represented by the UsdCollectionMembershipQuery object,
    C{query}.


    The result depends on the load state of the UsdStage, C{stage}.
    """
@overload
def Describe(_unknownArg1: Object | pxr.UsdGeom.XformOp, /) -> str:
    """
    Return a human-readable description.
    """
@overload
def Describe(_unknownArg1: Stage, /) -> str:
    """
    This is an overloaded member function, provided for convenience. It
    differs from the above function only in what argument(s) it accepts.
    """
@overload
def Describe(_unknownArg1: StageCache, /) -> str:
    """
    This is an overloaded member function, provided for convenience. It
    differs from the above function only in what argument(s) it accepts.
    """
@overload
def FlattenLayerStack(layerStack: pxr.Pcp.LayerStack, tag: str | pxr.Ar.ResolvedPath = ...) -> pxr.Sdf.Layer:
    '''
    Flatten C{layerStack} into a single layer with the given optional
    C{tag}.


    A composed UsdStage created from this flattened layer will be the same
    as a composed UsdStage whose root layer stack is the original layer
    stack.

    Unlike UsdStage::Flatten() , this function does not flatten
    composition arcs, such as references, payloads, inherits, specializes,
    or variants.

    Sublayer time offsets on the sublayers will be applied to remap any
    time-keyed scene description, such as timeSamples and clips.

    Asset paths will be resolved to absolute form, to ensure that they
    continue to identify the same asset from the output layer.

    Asset paths containing stage variable expressions will be evaluated
    using the variables from the root and session layer of C{layerStack}
    before being resolved.

    UsdFlattenLayerStackResolveAssetPath A few historical scene
    description features cannot be flattened into a single opinion because
    they unfortunately encode operations that are not closed under
    composition. Specifically, the SdfListOp
    operations"add"and"reorder"cannot be flattened. Instead,"add"will be
    converted to"append", and"reorder"will be discarded.
    '''
@overload
def FlattenLayerStack(layerStack: object, resolveAssetPathFn: object, tag: object = ...) -> pxr.Sdf.Layer: ...
def FlattenLayerStackAdvanced(layerStack: object, resolveAssetPathFn: object, tag: object = ...) -> pxr.Sdf.Layer: ...
def FlattenLayerStackResolveAssetPath(sourceLayer: pxr.Sdf.Layer, assetPath: str | pxr.Ar.ResolvedPath) -> str:
    """
    Implements the default asset path flattening behavior for
    C{UsdFlattenLayerStack}.


    C{assetPath} will be anchored to C{sourceLayer} by calling
    SdfComputeAssetPathRelativeToLayer. This function assumes that
    C{assetPath} does not contain a stage variable expression.
    """
def FlattenLayerStackResolveAssetPathAdvanced(context: FlattenResolveAssetPathContext) -> str:
    """
    Implements the default asset path flattening behavior for
    C{UsdFlattenLayerStack}.


    The asset path in C{context} will be anchored to the source layer by
    calling SdfComputeAssetPathRelativeToLayer. If the asset path contains
    a stage variable expression, it will be evaluated using the expression
    variables in C{context} before being anchored.
    """
def GetMajorVersion() -> int:
    """Get the major version number for this build of USD.
    Returns a value of type int.
    USD versions are described as (major,minor,patch)"""
def GetMinorVersion() -> int:
    """Get the minor version number for this build of USD.
    Returns a value of type int.
    USD versions are described as (major,minor,patch)"""
def GetPatchVersion() -> int:
    """Get the patch version number for this build of USD.
    Returns a value of type int.
    USD versions are described as (major,minor,patch)"""
def GetVersion() -> tuple:
    """Get the complete version number for this build of USD.
    Returns a value of type tuple(int,int,int).
    USD versions are described as (major,minor,patch)"""
@overload
def TraverseInstanceProxies(predicate: _PrimFlagsPredicate | _Term) -> _PrimFlagsPredicate:
    """
    This function is used to allow the prim traversal functions listed
    under Prim predicate flags to traverse beneath instance prims and
    return descendants that pass the specified C{predicate} as instance
    proxy prims.


    For example: ::

      // Return all children of the specified prim.  
      // If prim is an instance, return all children as instance proxy prims.
      prim.GetFilteredChildren(
          UsdTraverseInstanceProxies(UsdPrimAllPrimsPredicate))
  
      // Return children of the specified prim that pass the default predicate.
      // If prim is an instance, return the children that pass this predicate
      // as instance proxy prims.
      prim.GetFilteredChildren(UsdTraverseInstanceProxies());
  
      // Return all model or group children of the specified prim.
      // If prim is an instance, return the children that pass this predicate 
      // as instance proxy prims.
      prim.GetFilteredChildren(UsdTraverseInstanceProxies(UsdPrimIsModel || UsdPrimIsGroup));

    Users may also call Usd_PrimFlagsPredicate::TraverseInstanceProxies to
    enable traversal beneath instance prims. This function is equivalent
    to: ::

      predicate.TraverseInstanceProxies(true);

    However, this function may be more convenient, especially when calling
    a prim traversal function with a default-constructed tautology
    predicate.
    """
@overload
def TraverseInstanceProxies() -> _PrimFlagsPredicate:
    """
    This is an overloaded member function, provided for convenience. It
    differs from the above function only in what argument(s) it accepts.
    Convenience method equivalent to calling UsdTraverseInstanceProxies
    with the UsdPrimDefaultPredicate that is used by default for prim
    traversals.
    """
def UseButDoNotPopulateCache(_cache: StageCache, /) -> _NonPopulatingStageCacheWrapper:
    """
    Indicate that a UsdStageCacheContext should be bound in a read-only
    fashion.


    Calls to UsdStage::Open() will attempt to find stages in C{cache} when
    a UsdStageCacheContext is present on the stack. See
    UsdStageCacheContext for more details and example use.
    """
def _TestPrimRangeRoundTrip(arg1: object, /) -> Any: ...
def _UnsafeGetStageForTesting(arg1: Object | pxr.UsdGeom.XformOp, /) -> Stage: ...
