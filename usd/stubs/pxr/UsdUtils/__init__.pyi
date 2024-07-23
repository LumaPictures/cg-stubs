# mypy: disable-error-code="misc, override, no-redef"

import Boost.Python
import pxr.Ar
import pxr.Sdf
import pxr.Tf
import pxr.Usd
import pxr.UsdGeom
import pxr.UsdShade
import typing
import typing_extensions
from . import complianceChecker as complianceChecker, constantsGroup as constantsGroup, fixBrokenPixarSchemas as fixBrokenPixarSchemas, toolPaths as toolPaths, updateSchemaWithSdrNode as updateSchemaWithSdrNode, usdzUtils as usdzUtils
from pxr.UsdUtils.complianceChecker import ComplianceChecker as ComplianceChecker
from pxr.UsdUtils.fixBrokenPixarSchemas import FixBrokenPixarSchemas as FixBrokenPixarSchemas
from pxr.UsdUtils.updateSchemaWithSdrNode import PropertyDefiningKeys as PropertyDefiningKeys, SchemaDefiningKeys as SchemaDefiningKeys, SchemaDefiningMiscConstants as SchemaDefiningMiscConstants, UpdateSchemaWithSdrNode as UpdateSchemaWithSdrNode
from pxr.UsdUtils.usdzUtils import ExtractUsdzPackage as ExtractUsdzPackage, UsdzAssetIterator as UsdzAssetIterator
from typing import Any, ClassVar, overload

__MFB_FULL_PACKAGE_NAME: str

class CoalescingDiagnosticDelegate(Boost.Python.instance):
    """
    A class which collects warnings and statuses from the Tf diagnostic
    manager system in a thread safe manner.


    This class allows clients to get both the unfiltered results, as well
    as a compressed view which deduplicates diagnostic events by their
    source line number, function and file from which they occurred.
    """
    __instance_size__: ClassVar[int] = ...
    def __init__(self) -> None: ...
    def DumpCoalescedDiagnosticsToStderr(self) -> None: ...
    def DumpCoalescedDiagnosticsToStdout(self) -> None: ...
    def DumpUncoalescedDiagnostics(self) -> None: ...
    def TakeCoalescedDiagnostics(self) -> list[CoalescingDiagnosticDelegate]:
        """
        Get all pending diagnostics in a coalesced form.



        This method clears the pending diagnostics.
        """
    def TakeUncoalescedDiagnostics(self) -> list[[pxr.Tf.DiagnosticBase]]:
        """
        Get all pending diagnostics without any coalescing.



        This method clears the pending diagnostics.
        """

class CoalescingDiagnosticDelegateItem(Boost.Python.instance):
    """
    An item used in coalesced results, containing a shared component: the
    file/function/line number, and a set of unshared components: the call
    context and commentary.
    """
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """
    @property
    def sharedItem(self): ...
    @property
    def unsharedItems(self): ...

class CoalescingDiagnosticDelegateSharedItem(Boost.Python.instance):
    """
    The shared component in a coalesced result This type can be thought of
    as the key by which we coalesce our diagnostics.
    """
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """
    @property
    def sourceFileName(self): ...
    @property
    def sourceFunction(self): ...
    @property
    def sourceLineNumber(self): ...

class CoalescingDiagnosticDelegateUnsharedItem(Boost.Python.instance):
    """
    The unshared component in a coalesced result.
    """
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """
    @property
    def commentary(self): ...
    @property
    def context(self): ...

class ConditionalAbortDiagnosticDelegate(Boost.Python.instance):
    '''
    A class that allows client application to instantiate a diagnostic
    delegate that can be used to abort operations for a non fatal USD
    error or warning based on immutable include exclude rules defined for
    this instance.


    These rules are regex strings where case sensitive matching is done on
    error/warning text or the location of the code path where the
    error/warning occured. Note that these rules will be respected only
    during the lifetime of the delegate. Include Rules determine what
    errors or warnings will cause a fatal abort. Exclude Rules determine
    what errors or warnings matched from the Include Rules should not
    cause the fatal abort. Example: to abort on all errors and warnings
    coming from"*pxr*"codepath but not
    from"*ConditionalAbortDiagnosticDelegate*", a client can create the
    following delegate: ::

      UsdUtilsConditionalAbortDiagnosticDelegateErrorFilters includeFilters;
      UsdUtilsConditionalAbortDiagnosticDelegateErrorFilters excludeFilters;
      includeFilters.SetCodePathFilters({"*pxr*"});
      excludeFilters.SetCodePathFilters({"*ConditionalAbortDiagnosticDelegate*"});
      UsdUtilsConditionalAbortDiagnosticDelegate delegate = 
          UsdUtilsConditionalAbortDiagnosticDelegate(includeFilters,
              excludeFilters);

    '''
    __instance_size__: ClassVar[int] = ...
    def __init__(self, _includeFilters: ConditionalAbortDiagnosticDelegateErrorFilters, _excludeFilters: ConditionalAbortDiagnosticDelegateErrorFilters, /) -> None:
        """
        Constructor to initialize conditionalAbortDiagnosticDelegate.


        Responsible for adding this delegate instance to TfDiagnosticMgr and
        also sets the C{includeFilters} and C{excludeFilters}

        The _includeFilters and _excludeFilters are immutable
        """

class ConditionalAbortDiagnosticDelegateErrorFilters(Boost.Python.instance):
    """
    A class which represents the inclusion exclusion filters on which
    errors will be matched stringFilters: matching and filtering will be
    done on explicit string of the error/warning codePathFilters: matching
    and filtering will be done on errors/warnings coming from a specific
    usd code path.
    """
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, _stringFilters: typing.Iterable[str | pxr.Ar.ResolvedPath], _codePathFilters: typing.Iterable[str | pxr.Ar.ResolvedPath], /) -> None: ...
    def GetCodePathFilters(self) -> list[str]: ...
    def GetStringFilters(self) -> list[str]: ...
    def SetCodePathFilters(self, codePathFilters: typing.Iterable[str | pxr.Ar.ResolvedPath]) -> None: ...
    def SetStringFilters(self, stringFilters: typing.Iterable[str | pxr.Ar.ResolvedPath]) -> None: ...

class DependencyInfo(Boost.Python.instance):
    """
    Class containing information from a processed dependency.


    A UsdUtilsDependencyInfo object is passed into the user processing
    function and contains relevant asset path and dependency information.
    Additionally, a UsdUtilsDependencyInfo object is also returned from
    the user processing function and communicates back to the asset
    localization routine any changes that were made during processing.
    """
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, _assetPath: str | pxr.Ar.ResolvedPath, /) -> None: ...
    @overload
    def __init__(self, _assetPath: str | pxr.Ar.ResolvedPath, _dependencies: typing.Iterable[str | pxr.Ar.ResolvedPath], /) -> None: ...
    @overload
    def __init__(self, arg2: DependencyInfo, /) -> None: ...
    @property
    def assetPath(self) -> str:
        """
        Returns the asset value path for the dependency.


        When UsdUtilsDependencyInfo is returned as a parameter from a user
        processing function, the localization system compares the value with
        the value that was originally authored in the layer.

        If the values are the same, no special action is taken and processing
        will continue as normal.

        If the returned value is an empty string, the system will ignore this
        path as well as any dependencies associated with it.

        If the returned value differs from what what was originally authored
        into the layer, the system will instead operate on the updated. value.
        If the updated path can be opened as a layer, it will be enqueued and
        searched for additional dependencies.

        Note: A coding error will be issued if a user processing function
        attempts to modify an asset path contained in an existing package.
        """
    @property
    def dependencies(self) -> list[str]:
        """
        Returns a list of dependencies related to the asset path.


        Paths in this vector are specified relative to their containing layer.
        When passed into the user processing function, if this array is
        populated, then the asset path resolved to one or more values, such as
        in the case of UDIM tiles or clip asset path template strings.

        When this structure is returned from a processing function, each path
        contained within will in turn be processed by the system. Any path
        that can be opened as a layer, will be enqueued and searched for
        additional dependencies.
        """

class RegisteredVariantSet(Boost.Python.instance):
    """
    Class that holds information about variantSets that are registered
    with the pipeline.


    Registered variantSets are known variantSets in a pipeline that may
    need to be reasoned about by apps during import/export.

    UsdUtilsGetRegisteredVariantSets
    """

    class SelectionExportPolicy(Boost.Python.enum):
        Always: ClassVar[RegisteredVariantSet.SelectionExportPolicy] = ...
        IfAuthored: ClassVar[RegisteredVariantSet.SelectionExportPolicy] = ...
        Never: ClassVar[RegisteredVariantSet.SelectionExportPolicy] = ...
        names: ClassVar[dict] = ...
        values: ClassVar[dict] = ...
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """
    @property
    def name(self): ...
    @property
    def selectionExportPolicy(self): ...

class SparseAttrValueWriter(Boost.Python.instance):
    '''
    A utility class for authoring time-varying attribute values with
    simple run-length encoding, by skipping any redundant time-samples.


    Time-samples that are close enough to each other, with relative
    difference smaller than a fixed epsilon value are considered to be
    equivalent. This is to avoid unnecessary authoring of time-samples
    caused by numerical fuzz in certain computations.

    For vectors, matrices, and other composite types (like quaternions and
    arrays), each component is compared with the corresponding component
    for closeness. The chosen epsilon value for double precision floating
    point numbers is 1e-12. For single-precision, it is 1e-6 and for half-
    precision, it is 1e-2.

    Example c++ usage: ::

      UsdGeomSphere sphere = UsdGeomSphere::Define(stage, SdfPath("/Sphere"));
      UsdAttribute radius = sphere.CreateRadiusAttr();
      UsdUtilsSparseAttrValueWriter attrValueWriter(radius, 
              /*defaultValue*/ VtValue(1.0));
      attrValueWriter.SetTimeSample(VtValue(10.0), UsdTimeCode(1.0));
      attrValueWriter.SetTimeSample(VtValue(10.0), UsdTimeCode(2.0));
      attrValueWriter.SetTimeSample(VtValue(10.0), UsdTimeCode(3.0));
      attrValueWriter.SetTimeSample(VtValue(20.0), UsdTimeCode(4.0));

    Equivalent python example: ::

      sphere = UsdGeom.Sphere.Define(stage, Sdf.Path("/Sphere"))
      radius = sphere.CreateRadiusAttr()
      attrValueWriter = UsdUtils.SparseAttrValueWriter(radius, defaultValue=1.0)
      attrValueWriter.SetTimeSample(10.0, 1.0)
      attrValueWriter.SetTimeSample(10.0, 2.0)
      attrValueWriter.SetTimeSample(10.0, 3.0)
      attrValueWriter.SetTimeSample(20.0, 4.0)

    In the above examples, the specified default value of radius (1.0)
    will not be authored into scene description since it matches the
    fallback value. Additionally, the time-sample authored at time=2.0
    will be skipped since it is redundant. Also note that for correct
    behavior, the calls to SetTimeSample() must be made with sequentially
    increasing time values. If not, a coding error is issued and the
    authored animation may be incorrect.
    '''
    def __init__(self, attr: pxr.Usd.Attribute | pxr.UsdGeom.ConstraintTarget | pxr.UsdGeom.Primvar | pxr.UsdGeom.XformOp | pxr.UsdShade.Input | pxr.UsdShade.Output, defaultValue: Any = ...) -> None:
        """
        The constructor initializes the data required for run-length encoding
        of time-samples.


        It also sets the default value of C{attr} to C{defaultValue}, if
        C{defaultValue} is non-empty and different from the existing default
        value of C{attr}.

        C{defaultValue} can be unspecified (or left empty) if you don't care
        about authoring a default value. In this case, the sparse authoring
        logic is initialized with the existing authored default value or the
        fallback value, if C{attr} has one.
        """
    def SetTimeSample(self, value: Any, time: pxr.Usd.TimeCode | float | pxr.Sdf.TimeCode) -> bool:
        """
        Sets a new time-sample on the attribute with given C{value} at the
        given C{time}.


        The time-sample is only authored if it's different from the previously
        set time-sample, in which case the previous time-sample is also
        authored, in order to to end the previous run of contiguous identical
        values and start a new run.

        This incurs a copy of C{value}. Also, the value will be held in memory
        at least until the next time-sample is written or until the
        SparseAttrValueWriter instance is destroyed.
        """

class SparseValueWriter(Boost.Python.instance):
    '''
    Utility class that manages sparse authoring of a set of UsdAttributes.


    It does this by maintaining a map of UsdAttributes to their
    corresponding UsdUtilsSparseAttrValueWriter objects.

    To use this class, simply instantiate an instance of it and invoke the
    SetAttribute() method with various attributes and their associated
    time-samples.

    If the attribute has a default value, SetAttribute() must be called
    with time=Default first (multiple times, if necessary), followed by
    calls to author time-samples in sequentially increasing time order.

    This class is not threadsafe. In general, authoring to a single USD
    layer from multiple threads isn\'t threadsafe. Hence, there is little
    value in making this class threadsafe. Example c++ usage: ::

      UsdGeomCylinder cylinder = UsdGeomCylinder::Define(stage, SdfPath("/Cylinder"));
      UsdAttribute radius = cylinder.CreateRadiusAttr();
      UsdAttribute height = cylinder.CreateHeightAttr();
      UsdUtilsSparseValueWriter valueWriter;
      valueWriter.SetAttribute(radius, 2.0, UsdTimeCode::Default());
      valueWriter.SetAttribute(height, 2.0, UsdTimeCode::Default());
  
      valueWriter.SetAttribute(radius, 10.0, UsdTimeCode(1.0));
      valueWriter.SetAttribute(radius, 20.0, UsdTimeCode(2.0));
      valueWriter.SetAttribute(radius, 20.0, UsdTimeCode(3.0));
      valueWriter.SetAttribute(radius, 20.0, UsdTimeCode(4.0));
  
      valueWriter.SetAttribute(height, 2.0, UsdTimeCode(1.0));
      valueWriter.SetAttribute(height, 2.0, UsdTimeCode(2.0));
      valueWriter.SetAttribute(height, 3.0, UsdTimeCode(3.0));
      valueWriter.SetAttribute(height, 3.0, UsdTimeCode(4.0));

    Equivalent python code: ::

      cylinder = UsdGeom.Cylinder.Define(stage, Sdf.Path("/Cylinder"))
      radius = cylinder.CreateRadiusAttr()
      height = cylinder.CreateHeightAttr()
      valueWriter = UsdUtils.SparseValueWriter()
      valueWriter.SetAttribute(radius, 2.0, Usd.TimeCode.Default())
      valueWriter.SetAttribute(height, 2.0, Usd.TimeCode.Default())
  
      valueWriter.SetAttribute(radius, 10.0, 1.0)
      valueWriter.SetAttribute(radius, 20.0, 2.0)
      valueWriter.SetAttribute(radius, 20.0, 3.0)
      valueWriter.SetAttribute(radius, 20.0, 4.0)
  
      valueWriter.SetAttribute(height, 2.0, 1.0)
      valueWriter.SetAttribute(height, 2.0, 2.0)
      valueWriter.SetAttribute(height, 3.0, 3.0)
      valueWriter.SetAttribute(height, 3.0, 4.0)

    In the above example,
       - The default value of the"height"attribute is not authored into
         scene description since it matches the fallback value.

       - Time-samples at time=3.0 and time=4.0 will be skipped for the
         radius attribute.

       - For the"height"attribute, the first timesample at time=1.0 will
         be skipped since it matches the default value.

       - The last time-sample at time=4.0 will also be skipped
         for"height"since it matches the previously written value at time=3.0.

    '''
    __instance_size__: ClassVar[int] = ...
    def __init__(self) -> None: ...
    def GetSparseAttrValueWriters(self) -> list[SparseAttrValueWriter]:
        """
        Returns a new vector of UsdUtilsSparseAttrValueWriter populated from
        the attrValueWriter map.
        """
    def SetAttribute(self, attr: pxr.Usd.Attribute | pxr.UsdGeom.ConstraintTarget | pxr.UsdGeom.Primvar | pxr.UsdGeom.XformOp | pxr.UsdShade.Input | pxr.UsdShade.Output, value: Any, time: pxr.Usd.TimeCode | float | pxr.Sdf.TimeCode = ...) -> bool:
        """
        Sets the value of C{attr} to C{value} at time C{time}.


        The value is written sparsely, i.e., the default value is authored
        only if it is different from the fallback value or the existing
        default value, and any redundant time-samples are skipped when the
        attribute value does not change significantly between consecutive
        time-samples.
        """

class StageCache(Boost.Python.instance):
    """
    The UsdUtilsStageCache class provides a simple interface for handling
    a singleton usd stage cache for use by all USD clients.


    This way code from any location can make use of the same cache to
    maximize stage reuse.
    """
    __instance_size__: ClassVar[int] = ...
    def __init__(self) -> None: ...
    @staticmethod
    def Get() -> pxr.Usd.StageCache:
        """
        Returns the singleton stage cache.
        """
    @staticmethod
    def GetSessionLayerForVariantSelections(_modelName: str | pxr.Ar.ResolvedPath, _variantSelections: typing.Iterable[tuple[str | pxr.Ar.ResolvedPath, str | pxr.Ar.ResolvedPath]], /) -> pxr.Sdf.Layer:
        """
        Given variant selections as a vector of pairs (vector in case order
        matters to the client), constructs a session layer with overs on the
        given root modelName with the variant selections, or returns a cached
        session layer with those opinions.
        """

class TimeCodeRange(Boost.Python.instance):
    """
    Represents a range of UsdTimeCode values as start and end time codes
    and a stride value.


    A UsdUtilsTimeCodeRange can be iterated to retrieve all time code
    values in the range. The range may be empty, it may contain a single
    time code, or it may represent multiple time codes from start to end.
    The interval defined by the start and end time codes is closed on both
    ends.

    Note that when constructing a UsdUtilsTimeCodeRange,
    UsdTimeCode::EarliestTime() and UsdTimeCode::Default() cannot be used
    as the start or end time codes. Also, the end time code cannot be less
    than the start time code for positive stride values, and the end time
    code cannot be greater than the start time code for negative stride
    values. Finally, the stride value cannot be zero. If any of these
    conditions are not satisfied, then an invalid empty range will be
    returned.
    """

    class Tokens(Boost.Python.instance):
        EmptyTimeCodeRange: ClassVar[str] = ...  # read-only
        RangeSeparator: ClassVar[str] = ...  # read-only
        StrideSeparator: ClassVar[str] = ...  # read-only
        def __init__(self, *args, **kwargs) -> None:
            """Raises an exception
            This class cannot be instantiated from Python
            """

    class _Iterator(Boost.Python.instance):
        def __init__(self, *args, **kwargs) -> None:
            """Raises an exception
            This class cannot be instantiated from Python
            """
        def __iter__(self) -> typing_extensions.Self: ...
        def __next__(self) -> pxr.Usd.TimeCode: ...
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None:
        """
        Construct an invalid empty range.


        The start time code will be initialized to zero, and any iteration of
        the range will yield no time codes.
        """
    @overload
    def __init__(self, timeCode: pxr.Usd.TimeCode | float | pxr.Sdf.TimeCode) -> None:
        """
        Construct a range containing only the given C{timeCode}.


        An iteration of the range will yield only that time code.
        """
    @overload
    def __init__(self, startTimeCode: pxr.Usd.TimeCode | float | pxr.Sdf.TimeCode, endTimeCode: pxr.Usd.TimeCode | float | pxr.Sdf.TimeCode) -> None:
        """
        Construct a range containing the time codes from C{startTimeCode} to
        C{endTimeCode}.


        If C{endTimeCode} is greater than or equal to C{startTimeCode}, then
        the stride will be 1.0. Otherwise, the stride will be -1.0.
        """
    @overload
    def __init__(self, startTimeCode: pxr.Usd.TimeCode | float | pxr.Sdf.TimeCode, endTimeCode: pxr.Usd.TimeCode | float | pxr.Sdf.TimeCode, stride: float) -> None:
        """
        Construct a range containing the time codes from C{startTimeCode} to
        C{endTimeCode} using the stride value C{stride}.


        UsdTimeCode::EarliestTime() and UsdTimeCode::Default() cannot be used
        as C{startTimeCode} or C{endTimeCode}. If C{stride} is a positive
        value, then C{endTimeCode} cannot be less than C{startTimeCode}. If
        C{stride} is a negative value, then C{endTimeCode} cannot be greater
        than C{startTimeCode}. Finally, the stride value cannot be zero. If
        any of these conditions are not satisfied, then a coding error will be
        issued and an invalid empty range will be returned.
        """
    @staticmethod
    def CreateFromFrameSpec(_frameSpec: str | pxr.Ar.ResolvedPath, /) -> TimeCodeRange:
        """
        Create a time code range from C{frameSpec}.


        A FrameSpec is a compact string representation of a time code range. A
        FrameSpec may contain up to three floating point values for the start
        time code, end time code, and stride values of a time code range.

        A FrameSpec containing just a single floating point value represents a
        time code range containing only that time code.

        A FrameSpec containing two floating point values separated by the
        range separator (':') represents a time code range from the first
        value as the start time code to the second values as the end time
        code.

        A FrameSpec that specifies both a start and end time code value may
        also optionally specify a third floating point value as the stride,
        separating it from the first two values using the stride separator
        ('x').

        The following are examples of valid FrameSpecs: 123 101:105 105:101
        101:109x2 101:110x2 101:104x0.5

        An empty string corresponds to an invalid empty time code range.

        A coding error will be issued if the given string is malformed.
        """
    def IsValid(self) -> bool:
        """
        Return true if this range contains one or more time codes, or false
        otherwise.
        """
    def empty(self) -> bool: ...
    def __bool__(self) -> bool:
        """
        Return true if this range contains one or more time codes, or false
        otherwise.
        """
    def __eq__(self, other: object) -> bool:
        """
        Return true if this range is equivalent to C{other}.
        """
    def __iter__(self) -> _Iterator: ...
    def __ne__(self, other: object) -> bool: ...
    @property
    def endTimeCode(self) -> pxr.Usd.TimeCode:
        """
        Return the end time code of this range.
        """
    @property
    def frameSpec(self): ...
    @property
    def startTimeCode(self) -> pxr.Usd.TimeCode:
        """
        Return the start time code of this range.
        """
    @property
    def stride(self) -> float:
        """
        Return the stride value of this range.
        """

class UsdStageStatsKeys(Boost.Python.instance):
    activePrimCount: ClassVar[str] = ...  # read-only
    approxMemoryInMb: ClassVar[str] = ...  # read-only
    assetCount: ClassVar[str] = ...  # read-only
    inactivePrimCount: ClassVar[str] = ...  # read-only
    instanceCount: ClassVar[str] = ...  # read-only
    instancedModelCount: ClassVar[str] = ...  # read-only
    modelCount: ClassVar[str] = ...  # read-only
    primCounts: ClassVar[str] = ...  # read-only
    primCountsByType: ClassVar[str] = ...  # read-only
    primary: ClassVar[str] = ...  # read-only
    prototypeCount: ClassVar[str] = ...  # read-only
    prototypes: ClassVar[str] = ...  # read-only
    pureOverCount: ClassVar[str] = ...  # read-only
    totalInstanceCount: ClassVar[str] = ...  # read-only
    totalPrimCount: ClassVar[str] = ...  # read-only
    untyped: ClassVar[str] = ...  # read-only
    usedLayerCount: ClassVar[str] = ...  # read-only
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """

def AuthorCollection(collectionName: str | pxr.Ar.ResolvedPath, usdPrim: pxr.Usd.Prim, pathsToInclude: typing.Iterable[pxr.Sdf.Path | str], pathsToExclude: typing.Iterable[pxr.Sdf.Path | str] = ...) -> pxr.Usd.CollectionAPI:
    """
    Authors a collection named C{collectionName} on the given prim,
    C{usdPrim} with the given set of included paths ( C{pathsToInclude})
    and excluded paths ( C{pathsToExclude}).


    If a collection with the specified name already exists on C{usdPrim},
    its data is appended to. The resulting collection will contain both
    the old paths and the newly included paths.
    """
def ComputeAllDependencies(assetPath: pxr.Sdf.AssetPath | str, processingFunc: typing.Callable[[pxr.Sdf.Layer, DependencyInfo], DependencyInfo] = ...) -> tuple:
    """
    Recursively computes all the dependencies of the given asset and
    populates C{layers} with all the dependencies that can be opened as an
    SdfLayer.


    All of the resolved non-layer dependencies are populated in C{assets}.
    Any unresolved (layer and non-layer) asset paths are populated in
    C{unresolvedPaths}.

    If a function is provided for the C{processingFunc} parameter, it will
    be invoked on every asset path that is discovered during localization.
    Refer to UsdUtilsDependencyInfo for general information on User
    processing functions. Any changes made to the paths during the
    invocation of this function will not be written to processed layers.

    The input vectors to be populated with the results are *cleared*
    before any results are added to them.

    Returns true if the given asset was resolved correctly.
    """
def ComputeCollectionIncludesAndExcludes(includedRootPaths: typing.Iterable[pxr.Sdf.Path | str], usdStage: pxr.Usd.Stage, minInclusionRatio: float = ..., maxNumExcludesBelowInclude: int = ..., minIncludeExcludeCollectionSize: int = ..., pathsToIgnore: PathHashSet = ...) -> tuple[list[pxr.Sdf.Path], list[pxr.Sdf.Path]]:
    '''
    Computes the optimal set of paths to include and the set of paths to
    exclude below includes paths, in order to encode
    an"expandPrims"collection that contains the subtrees of prims rooted
    at C{includedRootPaths}.


    The algorithm used to determine a compact representation is driven by
    the following three parameters: C{minInclusionRatio},
    C{maxNumExcludesBelowInclude} and C{minIncludeExcludeCollectionSize}.
    See below for their descriptions.

    C{usdStage} is the USD stage to which the paths in
    C{includedRootPaths} belong. C{pathsToInclude} is populated with the
    set of paths to include. Any existing paths in the set are cleared
    before adding paths to it. C{pathsToExclude} is populated with the set
    of paths to exclude. Any existing paths in the set are cleared before
    adding paths to it. C{minInclusionRatio} is the minimum value of the
    ratio between the number of included paths and the sum of the number
    of included and excluded paths below an ancestor path, at or above
    which the ancestor path is included in the collection. For example, if
    an ancestor prim has four children and three out of the four are
    included in the collection, the inclusion ratio at the ancestor is
    0.75. This value should be in the range (0,1), if not, it\'s clamped to
    the range. C{maxNumExcludesBelowInclude} is the maximum number of
    paths that we exclude below any ancestor path that we include in a
    collection. This parameter only affects paths that have already passed
    the min-inclusion-ratio test. Setting this to 0 will cause all
    collections to have includes only (and no excludes). Setting it to a
    higher number will cause ancestor paths that are higher up in the
    namespace hierarchy to be included in collections.
    C{minIncludeExcludeCollectionSize} is the minimum size of a collection
    (i.e. the number of subtree-root paths included in it), at or above
    which the algorithm chooses to make a collection with both included
    and excluded paths, instead of creating a collection with only
    includes (containing the specified set of paths). UsdCollectionAPI
    C{pathsToIgnore} is the list of paths to be ignored by the algorithm
    used to determine the included and excluded paths for each collection.
    If non-empty, the paths in the hash set don\'t contribute towards the
    counts and ratios computed by the algorithm.

    Returns false if paths in C{includedRootPaths} (or their common
    ancestor) can\'t be found on the given C{usdStage}. parameters has an
    invalid value.

    The python version of this function returns a tuple containing the two
    lists (pathsToInclude, pathsToExclude).
    '''
@overload
def ComputeUsdStageStats(_rootLayerPath: str | pxr.Ar.ResolvedPath, /) -> tuple[pxr.Usd.Stage, dict]:
    '''
    Opens the given layer on a USD stage and collects various stats.


    The stats are populated in the dictionary-valued output param
    C{stats}.

    The set of stats include:
       - approxMemoryInMb - approximate memory allocated when opening the
         stage with all the models loaded.

       - totalPrimCount - total number of prims

       - modelCount - number of models

       - instancedModelCount - number of instanced models

       - assetCount - number of assets

       - prototypeCount - number of prototypes

       - totalInstanceCount - total number of instances (including nested
         instances)

       - two sub-dictionaries,\'primary\'and\'prototypes\'for the"primary"prim
         tree and for all the prototype subtrees respectively, containing the
         following stats:

       - primCounts - a sub-dictionary containing the following
       - totalPrimCount - number of prims

       - activePrimCount - number of active prims

       - inactivePrimCount - number of inactive prims

       - pureOverCount - number of pure overs

       - instanceCount - number of instances

       - primCountsByType - a sub-dictionary containing prim counts keyed
         by the prim type.

    Returns the stage that was opened.

    The"prototypes"subdictionary is populated only if the stage has one or
    more instanced models.

    The approximate memory allocated when opening the stage is computed
    and reported *only* if the TfMallocTag system has already been
    initialized by the client, and the number will represent only
    *additional* consumed memory, so if some of the layers the stage uses
    are already open, the true memory consumption for the stage may be
    higher than reported.

    TfMallocTag::IsInitialized()

    Only component models are included
    in\'modelCount\'and\'instancedModelCount\'.
    '''
@overload
def ComputeUsdStageStats(_stage: pxr.Usd.Stage, /) -> tuple[int, dict]:
    """
    This is an overloaded member function, provided for convenience. It
    differs from the above function only in what argument(s) it accepts.
    Computes stats on an already opened USD stage.


    Returns the total number of prims on the stage, including active,
    inactive. pure overs, prims inside prototypes etc.
    """
def CopyLayerMetadata(source: pxr.Sdf.Layer, destination: pxr.Sdf.Layer, skipSublayers: bool = ..., bakeUnauthoredFallbacks: bool = ...) -> bool:
    """
    Given two layers C{source} and C{destination}, copy the authored
    metadata from one to the other.


    By default, copy B{all} authored metadata; however, you can skip
    certain classes of metadata with the parameter C{skipSublayers}, which
    will prevent copying subLayers or subLayerOffsets

    Makes no attempt to clear metadata that may already be authored in
    C{destination}, but any fields that are already in C{destination} but
    also in C{source} will be replaced.

    Certain bits of layer metadata (eg. colorConfiguration and
    colorManagementSystem) can have their fallback values specified in the
    plugInfo.json files of plugins. When such metadata is unauthored in
    the source layer, if C{bakeUnauthoredFallbacks} is set to true, then
    the fallback values are baked into the destination layer.

    C{true} on success, C{false} on error.
    """
def CreateCollections(assignments: typing.Iterable[tuple[str | pxr.Ar.ResolvedPath, typing.Iterable[pxr.Sdf.Path | str]]], usdPrim: pxr.Usd.Prim, minInclusionRatio: float = ..., maxNumExcludesBelowInclude: int = ..., minIncludeExcludeCollectionSize: int = ...) -> list[pxr.Usd.CollectionAPI]:
    """
    Given a vector of (collection-name, path-set) pairs, C{assignments},
    creates and returns a vector of collections that include subtrees of
    prims rooted at the included paths.


    The collections are created on the given prim, C{usdPrim}.

    Based on the paths included in the various collections, this function
    computes a compact representation for each collection in parallel
    using UsdUtilsGetCollectionIncludesExcludes(). So, it takes the same
    set of parameters as that function: C{minInclusionRatio},
    C{maxNumExcludesBelowInclude} and C{minIncludeExcludeCollectionSize}.

    It is valid for the paths or subtrees specified in C{assignments} to
    have overlapping subtrees. In this case the overlapping bits will
    belong to multiple collections. C{assignments} is a vector of pairs
    representing collection names and paths to be included in the
    collection in each collection. C{usdPrim} is the prim on which the
    collections are created. C{minInclusionRatio} is the minimum value of
    the ratio between the number of included paths and the sum of the
    number of included and excluded paths below an ancestor path, at or
    above which the ancestor path is included in the collection. For
    example, if an ancestor prim has four children and three out of the
    four are included in the collection, the inclusion ratio at the
    ancestor is 0.75. This value should be in the range (0,1), if not,
    it's clamped to the range. C{maxNumExcludesBelowInclude} is the
    maximum number of paths that we exclude below any ancestor path that
    we include in a collection. This parameter only affects paths that
    have already passed the min-inclusion-ratio test. Setting this to 0
    will cause all collections to have includes only (and no excludes).
    Setting it to a higher number will cause ancestor paths that are
    higher up in the namespace hierarchy to be included in collections.
    C{minIncludeExcludeCollectionSize} is the minimum size of a collection
    (i.e. the number of subtree-root paths included in it), at or above
    which the algorithm chooses to make a collection with both included
    and excluded paths, instead of creating a collection with only
    includes (containing the specified set of paths). UsdCollectionAPI

    Returns the vector of UsdCollectionAPI objects that were created. If a
    collection is empty (i.e. includes no paths), then an empty collection
    is created for it with the default expansionRule. Hence, the size of
    the returned vector should match the size of C{assignments}.
    """
def CreateNewARKitUsdzPackage(assetPath: pxr.Sdf.AssetPath | str, usdzFilePath: str | pxr.Ar.ResolvedPath, firstLayerName: str | pxr.Ar.ResolvedPath = ..., editLayersInPlace: bool = ...) -> bool:
    '''
    Similar to UsdUtilsCreateNewUsdzPackage, this function packages all of
    the dependencies of the given asset.


    Assets targeted at the initial usdz implementation in ARKit operate
    under greater constraints than usdz files for more general\'in
    house\'uses, and this option attempts to ensure that these constraints
    are honored; this may involve more transformations to the data, which
    may cause loss of features such as VariantSets. Any anonymous layers
    that are encountered during dependency discovery will be serialized
    into the resulting package.

    If C{firstLayerName} is specified, it is modified to have
    the".usdc"extension, as required by the initial usdz implementation in
    ARKit.

    The C{editLayersInPlace} parameter controls the strategy used for
    managing changes to layers (including the root layer and all
    transitive layer dependencies) that occur during the package creation
    process. When C{editLayersInPlace} is false, a temporary, anonymous
    copy of each modified layer is created and written into the package.
    This has the advantage of leaving source layers untouched at the
    expense of creating a copy of each modified layer in memory for the
    duration of this function.

    When C{editLayersInPlace} is set to true, layers are modified in-place
    and not reverted or persisted once the package has been created. In
    this case, there is no overhead of creating copies of each modified
    layer. If you have UsdStages open during the function call that
    reference the layers being modified, you may receive warnings or
    composition errors. While these errors will not affect the resulting
    package adversely, it is strongly recommended that this function is
    run in isolation after any source UsdStages have been closed.

    Returns true if the package was created successfully.

    Clients of this function must take care of configuring the asset
    resolver context before invoking the function. To create a default
    resolver context, use CreateDefaultContextForAsset() with the asset
    path.

    If the given asset has a dependency on a directory (i.e. an external
    reference to a directory path), the dependency is ignored and the
    contents of the directory are not included in the created package.

    UsdUtilsCreateNewUsdzPackage()
    '''
def CreateNewUsdzPackage(assetPath: pxr.Sdf.AssetPath | str, usdzFilePath: str | pxr.Ar.ResolvedPath, firstLayerName: str | pxr.Ar.ResolvedPath = ..., editLayersInPlace: bool = ...) -> bool:
    """
    Creates a USDZ package containing the specified asset, identified by
    its C{assetPath}.


    The created package will include a localized version of the asset
    itself and all of its external dependencies. Any anonymous layers that
    are encountered during dependency discovery will be serialized into
    the resulting package. Due to localization, the packaged layers might
    be modified to have different asset paths.

    You can optionally specify a different package-internal name for the
    first layer of the asset by specifying C{firstLayerName}. By default,
    C{firstLayerName} is empty, meaning that the original name is
    preserved.

    The C{editLayersInPlace} parameter controls the strategy used for
    managing changes to layers (including the root layer and all
    transitive layer dependencies) that occur during the package creation
    process. When C{editLayersInPlace} is false, a temporary, anonymous
    copy of each modified layer is created and written into the package.
    This has the advantage of leaving source layers untouched at the
    expense of creating a copy of each modified layer in memory for the
    duration of this function.

    When C{editLayersInPlace} is set to true, layers are modified in-place
    and not reverted or persisted once the package has been created. In
    this case, there is no overhead of creating copies of each modified
    layer. If you have UsdStages open during the function call that
    reference the layers being modified, you may receive warnings or
    composition errors. While these errors will not affect the resulting
    package adversely, it is strongly recommended that this function is
    run in isolation after any source UsdStages have been closed.

    Returns true if the package was created successfully.

    Clients of this function must take care of configuring the asset
    resolver context before invoking the function. To create a default
    resolver context, use CreateDefaultContextForAsset() with the asset
    path.

    If the given asset has a dependency on a directory (i.e. an external
    reference to a directory path), the dependency is ignored and the
    contents of the directory are not included in the created package.

    UsdUtilsCreateNewARKitUsdzPackage()
    """
def ExtractExternalReferences(filePath: str | pxr.Ar.ResolvedPath) -> tuple:
    """
    Parses the file at C{filePath}, identifying external references, and
    sorting them into separate type-based buckets.


    Sublayers are returned in the C{sublayers} vector, references, whether
    prim references, value clip references or values from asset path
    attributes, are returned in the C{references} vector. Payload paths
    are returned in C{payloads}.

    No recursive chasing of dependencies is performed; that is the
    client's responsibility, if desired.

    Not all returned references are actually authored explicitly in the
    layer. For example, templated clip asset paths are resolved and
    expanded to include all available clip files that match the specified
    pattern.
    """
@overload
def FlattenLayerStack(stage: pxr.Usd.Stage, tag: str | pxr.Ar.ResolvedPath = ...) -> pxr.Sdf.Layer:
    '''
    Flatten the root layer stack of the given C{stage} into a single layer
    with the given optional C{tag}.


    The result layer can be substituted for the original layer stack while
    producing the same composed UsdStage.

    Unlike UsdStage::Export() , this function does not flatten composition
    arcs, such as references, payloads, inherits, specializes, or
    variants.

    Sublayer time offsets on the sublayers will be applied to remap any
    time-keyed scene description, such as timeSamples and clips.

    Asset paths will be resolved to absolute form, to ensure that they
    continue to identify the same asset from the output layer.

    UsdUtilsFlattenLayerStackResolveAssetPath A few historical scene
    description features cannot be flattened into a single opinion because
    they unfortunately encode operations that are not closed under
    composition. Specifically, the SdfListOp
    operations"add"and"reorder"cannot be flattened. Instead,"add"will be
    converted to"append", and"reorder"will be discarded.
    '''
@overload
def FlattenLayerStack(stage: pxr.Usd.Stage, resolveAssetPathFn: ResolveAssetPathFn, tag: str | pxr.Ar.ResolvedPath = ...) -> pxr.Sdf.Layer:
    '''
    Flatten the root layer stack of the given C{stage} into a single layer
    with the given optional C{tag} and using the C{resolveAssetPathFn} to
    resolve asset paths that are encountered.



    This is an advanced version of the above function.

    One use case for this version of the function is to flatten a layer
    stack that contains relative asset paths that we want to preserve as
    relative paths. For example: ::

      /source/root.usd # sublayers a.usd and b.usd
      /source/a.usd    # contains reference to ./subdir/layer.usd
      /source/b.usd
      /source/subdir/layer.usd

    We may want to generate C{"/dest/root.flat.usd"} knowing that we will
    (by some other means) also be copying C{"/source/subdir"} into
    C{"/dest/subdir"} . It\'s useful then to preserve the relative paths.

    Note, only the caller knows the ultimate destination of the flattened
    layer. So to accomplish this, we can provide a C{resolveAssetPathFn}
    callback that captures the outputDir, tests if the authored path is
    relative, and if so, computes a new relative path (based on where it
    will eventually be exported).
    '''
def FlattenLayerStackResolveAssetPath(sourceLayer: pxr.Sdf.Layer, assetPath: str | pxr.Ar.ResolvedPath) -> str:
    '''
    The default C{UsdUtilsResolvePathFn} used by
    C{UsdUtilsFlattenLayerStack}.


    For paths that the current ArResolver identifies as searchpaths or
    absolute paths, we return the unmodified path. However, any"Layer
    relative path"(see SdfComputeAssetPathRelativeToLayer) will be
    absolutized, because we do not know if the flattened layer\'s
    containing directory will be the same as any given source layer\'s in
    the incoming layerStack.
    '''
def GenerateClipManifestName(rootLayerName: str | pxr.Ar.ResolvedPath) -> str:
    """
    Generates a manifest file name based on an input file name.


    For example, if given'foo.usd', it generates'foo.manifest.usd'

    Note: this will not strip preceding paths off of a file name so
    /bar/baz/foo.usd will produce /bar/baz/foo.manifest.usd

    C{rootLayerName} The filepath used as a basis for generating our
    manifest layer name.
    """
def GenerateClipTopologyName(rootLayerName: str | pxr.Ar.ResolvedPath) -> str:
    """
    Generates a topology file name based on an input file name.


    For example, if given'foo.usd', it generates'foo.topology.usd'

    Note: this will not strip preceding paths off of a file name so
    /bar/baz/foo.usd will produce /bar/baz/foo.topology.usd

    C{rootLayerName} The filepath used as a basis for generating our
    topology layer name.
    """
def GetAlphaAttributeNameForColor(colorAttrName: str | pxr.Ar.ResolvedPath) -> str:
    """
    Define the shading pipeline's convention for naming a companion
    alpha/opacity attribute and primvarnames given the full name of a
    color-valued attribute.
    """
def GetDirtyLayers(stage: pxr.Usd.Stage, includeClipLayers: bool = ...) -> list[pxr.Sdf.Layer]:
    """
    Retrieve a list of all dirty layers from the stage's UsedLayers.
    """
def GetMaterialsScopeName(forceDefault: bool = ...) -> str:
    '''
    Get the name of the USD prim under which materials are expected to be
    authored.


    The scope name can be configured in the metadata of a plugInfo.json
    file like so: ::

      "UsdUtilsPipeline": {
          "MaterialsScopeName": "SomeScopeName"
      }

    If C{forceDefault} is true, any value specified in a plugInfo.json
    will be ignored and the built-in default will be returned. This is
    primarily used for unit testing purposes as a way to ignore any site-
    based configuration.
    '''
def GetModelNameFromRootLayer(_rootLayer: pxr.Sdf.Layer, /) -> str:
    """
    Returns the model name associated with a given root layer.


    In order, it looks for defaultPrim metadata, a prim matching the
    filename, and then the first concrete root prim.
    """
def GetPrefName() -> str:
    '''
    Returns the name of the reference position used on meshes and nurbs.


    By default the name is"pref".
    '''
def GetPrimAtPathWithForwarding(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> pxr.Usd.Prim:
    '''
    If a valid UsdPrim already exists at C{path} on the USD stage
    C{stage}, returns it.


    It not, it checks to see if the path belongs to a prim underneath an
    instance and returns the corresponding prototype prim.

    This returns an invalid UsdPrim if no corresponding prototype prim can
    be found and if no prim exists at the path.

    This method is similar to UsdStage::GetPrimAtPath() , in that it will
    never author scene description, and therefore is safe to use as
    a"reader"in the Usd multi-threading model.
    '''
def GetPrimaryCameraName(forceDefault: bool = ...) -> str:
    '''
    Get the name of the USD prim representing the primary camera.


    By default the name is"main_cam".

    The camera name can be configured in the metadata of a plugInfo.json
    file like so: ::

      "UsdUtilsPipeline": {
          "PrimaryCameraName": "SomeCameraName"
      }

    If C{forceDefault} is true, any value specified in a plugInfo.json
    will be ignored and the built-in default will be returned. This is
    primarily used for unit testing purposes as a way to ignore any site-
    based configuration.
    '''
def GetPrimaryUVSetName() -> str:
    '''
    Returns the name of the primary UV set used on meshes and nurbs.


    By default the name is"st".
    '''
def GetRegisteredVariantSets() -> list[RegisteredVariantSet]:
    '''
    Certain variant sets can be registered with the system.


    Returns the set of UsdUtilsRegisteredVariantSet objects that are
    registered with the pipeline.

    Variant sets can be registered through direct enumeration inside a
    C{plugInfo.json}, or via a plugin for situations that require dynamic
    configuration at runtime.

    This list will be empty until one or more C{plugInfo.json} files
    discoverable by your USD installation contain an entry in the
    UsdUtilsPipeline group like the following: ::

      "UsdUtilsPipeline": {
          "RegisteredVariantSets": {
              "modelingVariant": {
                  "selectionExportPolicy": "always"
              },
              "standin": {
                  "selectionExportPolicy": "never"
              }
          }
      }    

    After the above variantSets are registered, this will then load any
    plugin that has a C{plugInfo.json} with: ::

      "UsdUtilsPipeline": {
          "RegistersVariantSets": true
      }

    This plugin should then have code that registers code to run for
    C{UsdUtilsRegisteredVariantSet} : ::

      TF_REGISTRY_FUNCTION(UsdUtilsRegisteredVariantSet) {
        std::string variantSetName = ...;
        UsdUtilsRegisteredVariantSet::SelectionExportPolicy exportPolicy = ...;
        UsdUtilsRegisterVariantSet(variantSetName, exportPolicy);
      }

    UsdUtilsRegisterVariantSet
    '''
def LocalizeAsset(assetPath: pxr.Sdf.AssetPath | str, localizationDirectory: str | pxr.Ar.ResolvedPath, editLayersInPlace: bool = ..., processingFunc: typing.Callable[[pxr.Sdf.Layer, DependencyInfo], DependencyInfo] = ...) -> bool:
    """
    Creates a localized version of the asset identified by C{assetPath}
    and all of its external dependencies in the directory specified by
    C{localizationDirectory}.


    Any anonymous layers that are encountered during dependency discovery
    will be serialized into the resulting package. Due to localization,
    the packaged layers might be modified to have different asset paths.

    The C{editLayersInPlace} parameter controls the strategy used for
    managing changes to layers (including the root layer and all
    transitive layer dependencies) that occur during the package creation
    process. When C{editLayersInPlace} is false, a temporary, anonymous
    copy of each modified layer is created and written into the package.
    This has the advantage of leaving source layers untouched at the
    expense of creating a copy of each modified layer in memory for the
    duration of this function.

    When C{editLayersInPlace} is set to true, layers are modified in-place
    and not reverted or persisted once the package has been created. In
    this case, there is no overhead of creating copies of each modified
    layer. If you have UsdStages open during the function call that
    reference the layers being modified, you may receive warnings or
    composition errors. While these errors will not affect the resulting
    package adversely, it is strongly recommended that this function is
    run in isolation after any source UsdStages have been closed.

    If a function is provided for the C{processingFunc} parameter, it will
    be invoked on every asset path that is discovered during localization.
    This allows you to inject your own logic into the process. Refer to
    UsdUtilsDependencyInfo for general information on user processing
    functions. If an asset path is ignored in the processing function, it
    will be removed from the layer and excluded from the localized
    package. Paths that are modified will have their updated value written
    back into the localized layer. Paths that are added to the
    dependencies array during processing will be included in the resulting
    localized asset.

    Returns true if the package was created successfully.

    Clients of this function must take care of configuring the asset
    resolver context before invoking the function. To create a default
    resolver context, use CreateDefaultContextForAsset() with the asset
    path.

    If the given asset has a dependency on a directory (i.e. an external
    reference to a directory path), the dependency is ignored and the
    contents of the directory are not included in the created package.
    """
def ModifyAssetPaths(layer: pxr.Sdf.Layer, modifyFn: ModifyAssetPathFn) -> None:
    """
    Helper function that visits every asset path in C{layer}, calls
    C{modifyFn} and replaces the value with the return value of
    C{modifyFn}.


    This modifies C{layer} in place.

    This can be useful in preparing a layer for consumption in contexts
    that do not have access to the ArResolver for which the layer's asset
    paths were authored: we can replace all paths with their fully
    resolved equivalents, for example.
    """
def StitchClips(resultLayer: pxr.Sdf.Layer, clipLayerFiles: typing.Iterable[str | pxr.Ar.ResolvedPath], clipPath: pxr.Sdf.Path | str, startFrame: float = ..., endFrame: float = ..., interpolateMissingClipValues: bool = ..., clipSet: str | pxr.Ar.ResolvedPath = ...) -> bool:
    """
    A function that creates layers that use USD Value Clips to effectively
    merge the time samples in the given C{clipLayers} under C{clipPath}
    without copying the samples into a separate layer.


    C{resultLayer} The layer to which clip metadata and frame data will be
    written. The layer representing the static scene topology will be
    authored as a sublayer on this layer as well; it will be authored as
    the first sublayer in the list(strongest).

    C{clipLayerFiles} The files containing the time varying data.

    C{clipPath} The path at which we will put the clip metadata.

    C{startTimeCode} The first time coordinate for the rootLayer to point
    to. If none is provided, it will be the lowest startTimeCode available
    from the C{clipLayers}.

    C{endTimeCode} The last time coordinate for the rootLayer to point to.
    If none is provided, it will be the highest endTimeCode authored from
    the C{clipLayers}.

    C{interpolateMissingClipValues} Whether values for clips without
    samples are interpolated from surrounding clips. See
    UsdClipsAPI::GetInterpolateMissingClipValues for more details.

    C{clipSet} The name of the clipSet in which the aforementioned
    metadata will be authored.

    If this parameter is omitted, the default clipSet name will be
    authored. Details on how this is accomplished can be found below:

    Pre-existing opinions will be wiped away upon success. Upon failure,
    the original topology and manifest layers, if pre-existing, will be
    preserved. These layers will be named/looked up via the following
    scheme: topologyLayerName
    =<resultIdWithoutExt>.topology.<resultExt>manifestLayerName
    =<resultIdWithoutExt>.manifest.<resultExt> For example: if the
    resultLayerFile's name is foo.usd the expected topology layer will be
    foo.topology.usd and the expected manifest layer will be
    foo.manifest.usd.

    The topology layer contains the aggregated topology of the set of
    C{clipLayers}. This process will merge prims and properties, save for
    time varying properties, those will be accessed from the original clip
    files.

    The aggregation of topology works by merging a clipLayer at a time
    with the topologyLayer. If a prim already exists in the topologyLayer,
    its attributes will be merged.

    For example, if we have a layer, clipA with attributes
    /World/fx/foo.bar and a second layer with /World/fx/foo.baz. Our
    aggregate topology layer will contain both /World/fx/foo.bar,
    /World/fx/foo.baz.

    The manifest layer contains declarations for all attributes that exist
    under C{clipPath} and descendants in the clip layers with authored
    time samples. Any default values authored into the topology layer for
    these time sampled attributes will also be authored into the manifest.

    The C{resultLayer} will contain clip metadata at the specified
    C{clipPath}. The resultLayer will also have timeCode range data, such
    as start and end timeCodes written to it, with the starting position
    being provided by C{startTimeCode} and the ending provided by
    C{endTimeCode}.

    Note: an invalid clip path(because the prim doesn't exist in the
    aggregate topologyLayer) will result in a TF_CODING_ERROR.
    """
def StitchClipsManifest(manifestLayer: pxr.Sdf.Layer, topologyLayer: pxr.Sdf.Layer, clipPath: typing.Iterable[str | pxr.Ar.ResolvedPath], clipLayerFiles: pxr.Sdf.Path | str) -> bool:
    """
    A function which creates a clip manifest from the set of
    C{clipLayerFiles} for use in USD's Value Clips system.


    This manifest will contain declarations for attributes with authored
    time samples in the clip layers. If a time sampled attribute has a
    default value authored in the given C{topologyLayer}, that value will
    also be authored as its default in the manifest.

    C{manifestLayer} The layer where manifest data will be inserted.

    C{topologyLayer} The topology layer for C{clipLayerFiles}.

    C{clipLayerFiles} The files containing the time varying data.

    C{clipPrimPath} The manifest will contain attributes from this prim
    and its descendants in C{clipLayerFiles}.
    """
def StitchClipsTemplate(resultLayer: pxr.Sdf.Layer, topologyLayer: pxr.Sdf.Layer, manifestLayer: pxr.Sdf.Layer, clipPath: pxr.Sdf.Path | str, templatePath: str | pxr.Ar.ResolvedPath, startTimeCode: float, endTimeCode: float, stride: float, activeOffset: float = ..., interpolateMissingClipValues: bool = ..., clipSet: str | pxr.Ar.ResolvedPath = ...) -> bool:
    '''
    A function which authors clip template metadata on a particular prim
    in a result layer, as well as adding the topologyLayer to the list of
    subLayers on the C{resultLayer}.


    It will clear the C{resultLayer} and create a prim at C{clipPath}.
    Specifically, this will author clipPrimPath, clipTemplateAssetPath,
    clipTemplateStride, clipTemplateStartTime,  clipTemplateEndTime, and
    clipManifestAssetPath.

    C{resultLayer} The layer in which we will author the metadata.

    C{topologyLayer} The layer containing the aggregate topology of the
    clipLayers which the metadata refers to.

    C{manifestLayer} The layer containing manifest for the attributes in
    the clipLayers.

    C{clipPath} The path at which to author the metadata in C{resultLayer}

    C{templatePath} The template string to be authored at the
    clipTemplateAssetPath metadata key.

    C{startTime} The start time to be authored at the
    clipTemplateStartTime metadata key.

    C{endTime} The end time to be authored at the clipTemplateEndTime
    metadata key.

    C{stride} The stride to be authored at the clipTemplateStride metadata
    key.

    C{activeOffset} The offset to be authored at the
    clipTemplateActiveOffset metadata key.

    If this parameter is omitted, no value will be authored as the
    metadata is optional. C{interpolateMissingClipValues} Whether values
    for clips without samples are interpolated from surrounding clips. See
    UsdClipsAPI::GetInterpolateMissingClipValues for more details.

    C{clipSet} The name of the clipSet in which the aforementioned
    metadata will be authored.

    If this parameter is omitted, the default clipSet name("default") will
    be authored. For further information on these metadatum, see Advanced
    Scenegraph Scalability Features
    '''
def StitchClipsTopology(topologyLayer: pxr.Sdf.Layer, clipLayerFiles: typing.Iterable[str | pxr.Ar.ResolvedPath]) -> bool:
    """
    A function which aggregates the topology of a set of C{clipLayerFiles}
    for use in USD's Value Clips system.


    This aggregated scene topology will only include non-time-varying
    data, as it is for use in conjunction with the value clip metadata in
    a manifest layer.

    C{topologyLayer} The layer in which topology of the C{clipLayerFiles}
    will be aggregated and inserted.

    C{clipLayerFiles} The files containing the time varying data.
    """
def StitchInfo(strongObj: pxr.Sdf.Spec, weakObj: pxr.Sdf.Spec) -> None:
    """
    Merge the scene description for C{weakObj} into C{strongObj}.


    See documentation on UsdUtilsStitchLayers for a description of the
    merging behavior.
    """
def StitchLayers(strongLayer: pxr.Sdf.Layer, weakLayer: pxr.Sdf.Layer) -> None:
    '''
    Merge all scene description in C{weakLayer} into C{strongLayer}.


    Prims and properties in C{weakLayer} that do not exist in
    C{strongLayer} will be copied into C{strongLayer}. Prims and
    properties that do exist in C{strongLayer} will be merged with the
    existing scene description.

    Merging prims and properties is done on a field-by-field basis. In
    general, if a field has a value in C{strongLayer}, the value from
    C{weakLayer} will be ignored. However, certain fields have special
    rules for merging values together:

       - For map and dictionary-valued fields (including time samples), a
         dictionary merge is performed; values in the weaker dictionary are
         copied into the stronger dictionary only if the key does not already
         exist.

       - For listOp-valued fields, the listOps will be combined into a
         single listOp. The historical"add"and"reorder"list op operations
         cannot be combined in this way;"add"will be converted to"append",
         and"reorder"will be discarded.

       - The minimum startTimeCode value and maximum endTimeCode value
         will be used.

    '''
def UninstancePrimAtPath(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> pxr.Usd.Prim:
    """
    Given a path, uninstances all the instanced prims in the namespace
    chain and returns the resulting prim at the requested path.


    Returns a None prim if the given path doesn't exist and does not
    correspond to a valid prim inside a prototype.
    """
