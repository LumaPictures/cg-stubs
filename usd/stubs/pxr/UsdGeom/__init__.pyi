# mypy: disable-error-code="misc, override, no-redef"

import Boost.Python
import pxr.Ar
import pxr.Gf
import pxr.Sdf
import pxr.Tf
import pxr.Usd
import pxr.UsdShade
import pxr.Vt
import typing
from _typeshed import Incomplete
from typing import Any, ClassVar, overload

__MFB_FULL_PACKAGE_NAME: str

class BBoxCache(Boost.Python.instance):
    '''
    Caches bounds by recursively computing and aggregating bounds of
    children in world space and aggregating the result back into local
    space.


    The cache is configured for a specific time and
    UsdGeomImageable::GetPurposeAttr() set of purposes. When querying a
    bound, transforms and extents are read either from the time specified
    or UsdTimeCode::Default() , following TimeSamples, Defaults, and Value
    Resolution standard time-sample value resolution. As noted in
    SetIncludedPurposes() , changing the included purposes does not
    invalidate the cache, because we cache purpose along with the
    geometric data.

    Child prims that are invisible at the requested time are excluded when
    computing a prim\'s bounds. However, if a bound is requested directly
    for an excluded prim, it will be computed. Additionally, only prims
    deriving from UsdGeomImageable are included in child bounds
    computations.

    Unlike standard UsdStage traversals, the traversal performed by the
    UsdGeomBBoxCache includes prims that are unloaded (see
    UsdPrim::IsLoaded() ). This makes it possible to fetch bounds for a
    UsdStage that has been opened without *forcePopulate*, provided the
    unloaded model prims have authored extent hints (see
    UsdGeomModelAPI::GetExtentsHint() ).

    This class is optimized for computing tight
    B{untransformed"object"space} bounds for component-models. In the
    absence of component models, bounds are optimized for world-space,
    since there is no other easily identifiable space for which to
    optimize, and we cannot optimize for every prim\'s local space without
    performing quadratic work.

    The TfDebug flag, USDGEOM_BBOX, is provided for debugging.

    Warnings:
       - This class should only be used with valid UsdPrim objects.

       - This cache does not listen for change notifications; the user is
         responsible for clearing the cache when changes occur.

       - Thread safety: instances of this class may not be used
         concurrently.

       - Plugins may be loaded in order to compute extents for prim types
         provided by that plugin. See
         UsdGeomBoundable::ComputeExtentFromPlugins

    '''
    __instance_size__: ClassVar[int] = ...
    def __init__(self, time: pxr.Usd.TimeCode | float | pxr.Sdf.TimeCode, includedPurposes: list[str] | list[pxr.Ar.ResolvedPath], useExtentsHint: bool = ..., ignoreVisibility: bool = ...) -> None:
        """
        Construct a new BBoxCache for a specific C{time} and set of
        C{includedPurposes}.


        Only prims with a purpose that matches the C{includedPurposes} will be
        considered when accumulating child bounds. See UsdGeomImageable for
        allowed purpose values.

        If C{useExtentsHint} is true, then when computing the bounds for any
        model-root prim, if the prim is visible at C{time}, we will fetch its
        extents hint (via UsdGeomModelAPI::GetExtentsHint() ). If it is
        authored, we use it to compute the bounding box for the selected
        combination of includedPurposes by combining bounding box hints that
        have been cached for various values of purposes.

        If C{ignoreVisibility} is true invisible prims will be included during
        bounds computations.
        """
    def Clear(self) -> None:
        """
        Clears all pre-cached values.
        """
    def ClearBaseTime(self) -> None:
        """
        Clear this cache's baseTime if one has been set.


        After calling this, the cache will use its time as the baseTime value.
        """
    def ComputeLocalBound(self, prim: pxr.Usd.Prim) -> pxr.Gf.BBox3d:
        """
        Computes the oriented bounding box of the given prim, leveraging any
        pre-existing, cached bounds.


        The computed bound includes the transform authored on the prim itself,
        but does not include any ancestor transforms (it does not include the
        local-to-world transform).

        See ComputeWorldBound() for notes on performance and error handling.
        """
    def ComputePointInstanceLocalBound(self, instancer: PointInstancer, instanceId: int) -> pxr.Gf.BBox3d:
        """
        Compute the oriented bounding boxes of the given point instances.
        """
    def ComputePointInstanceLocalBounds(self, instancer: PointInstancer, instanceIds: int) -> tuple[int, pxr.Gf.BBox3d]:
        """
        Compute the oriented bounding boxes of the given point instances.


        The computed bounds include the transform authored on the instancer
        itself, but does not include any ancestor transforms (it does not
        include the local-to-world transform).

        The C{result} pointer must point to C{numIds} GfBBox3d instances to be
        filled.
        """
    def ComputePointInstanceRelativeBound(self, instancer: PointInstancer, instanceId: int, relativeToAncestorPrim: pxr.Usd.Prim) -> pxr.Gf.BBox3d:
        """
        Compute the bound of the given point instance in the space of an
        ancestor prim C{relativeToAncestorPrim}.
        """
    def ComputePointInstanceRelativeBounds(self, instancer: PointInstancer, instanceIds: int, relativeToAncestorPrim: pxr.Usd.Prim) -> tuple[int, pxr.Gf.BBox3d]:
        """
        Compute the bounds of the given point instances in the space of an
        ancestor prim C{relativeToAncestorPrim}.


        Write the results to C{result}.

        The computed bound excludes the local transform at
        C{relativeToAncestorPrim}. The computed bound may be incorrect if
        C{relativeToAncestorPrim} is not an ancestor of C{prim}.

        The C{result} pointer must point to C{numIds} GfBBox3d instances to be
        filled.
        """
    def ComputePointInstanceUntransformedBound(self, instancer: PointInstancer, instanceId: int) -> pxr.Gf.BBox3d:
        """
        Computes the bound of the given point instances, but does not include
        the instancer's transform.
        """
    def ComputePointInstanceUntransformedBounds(self, instancer: PointInstancer, instanceIds: int) -> tuple[int, pxr.Gf.BBox3d]:
        """
        Computes the bound of the given point instances, but does not include
        the transform (if any) authored on the instancer itself.


        B{IMPORTANT:} while the BBox does not contain the local
        transformation, in general it may still contain a non-identity
        transformation matrix to put the bounds in the correct space.
        Therefore, to obtain the correct axis-aligned bounding box, the client
        must call ComputeAlignedRange().

        The C{result} pointer must point to C{numIds} GfBBox3d instances to be
        filled.
        """
    def ComputePointInstanceWorldBound(self, instancer: PointInstancer, instanceId: int) -> pxr.Gf.BBox3d:
        """
        Compute the bound of the given point instance in world space.
        """
    def ComputePointInstanceWorldBounds(self, instancer: PointInstancer, instanceIds: int) -> tuple[int, pxr.Gf.BBox3d]:
        """
        Compute the bound of the given point instances in world space.


        The bounds of each instance is computed and then transformed to world
        space. The C{result} pointer must point to C{numIds} GfBBox3d
        instances to be filled.
        """
    def ComputeRelativeBound(self, prim: pxr.Usd.Prim, relativeRootPrim: pxr.Usd.Prim) -> pxr.Gf.BBox3d:
        """
        Compute the bound of the given prim in the space of an ancestor prim,
        C{relativeToAncestorPrim}, leveraging any pre-existing cached bounds.


        The computed bound excludes the local transform at
        C{relativeToAncestorPrim}. The computed bound may be incorrect if
        C{relativeToAncestorPrim} is not an ancestor of C{prim}.
        """
    @overload
    def ComputeUntransformedBound(self, prim: pxr.Usd.Prim) -> pxr.Gf.BBox3d:
        """
        Computes the bound of the prim's children leveraging any pre-existing,
        cached bounds, but does not include the transform (if any) authored on
        the prim itself.


        B{IMPORTANT:} while the BBox does not contain the local
        transformation, in general it may still contain a non-identity
        transformation matrix to put the bounds in the correct space.
        Therefore, to obtain the correct axis-aligned bounding box, the client
        must call ComputeAlignedRange().

        See ComputeWorldBound() for notes on performance and error handling.
        """
    @overload
    def ComputeUntransformedBound(self, prim: pxr.Usd.Prim, pathsToSkip: typing.Iterable[pxr.Sdf.Path | str], ctmOverrides: pxr.Tf.HashMap[pxr.Sdf.Path | str, pxr.Gf.Matrix4d, pxr.Sdf.Path.Hash]) -> pxr.Gf.BBox3d:
        """
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        Computes the bound of the prim's descendents while excluding the
        subtrees rooted at the paths in C{pathsToSkip}.


        Additionally, the parameter C{ctmOverrides} is used to specify
        overrides to the CTM values of certain paths underneath the prim. The
        CTM values in the C{ctmOverrides} map are in the space of the given
        prim, C{prim}.

        This leverages any pre-existing, cached bounds, but does not include
        the transform (if any) authored on the prim itself.

        B{IMPORTANT:} while the BBox does not contain the local
        transformation, in general it may still contain a non-identity
        transformation matrix to put the bounds in the correct space.
        Therefore, to obtain the correct axis-aligned bounding box, the client
        must call ComputeAlignedRange().

        See ComputeWorldBound() for notes on performance and error handling.
        """
    def ComputeWorldBound(self, prim: pxr.Usd.Prim) -> pxr.Gf.BBox3d:
        """
        Compute the bound of the given prim in world space, leveraging any
        pre-existing, cached bounds.


        The bound of the prim is computed, including the transform (if any)
        authored on the node itself, and then transformed to world space.

        Error handling note: No checking of C{prim} validity is performed. If
        C{prim} is invalid, this method will abort the program; therefore it
        is the client's responsibility to ensure C{prim} is valid.
        """
    def ComputeWorldBoundWithOverrides(self, prim: pxr.Usd.Prim, pathsToSkip: typing.Iterable[pxr.Sdf.Path | str], primOverride: pxr.Gf.Matrix4d, ctmOverrides: pxr.Tf.HashMap[pxr.Sdf.Path | str, pxr.Gf.Matrix4d, pxr.Sdf.Path.Hash]) -> pxr.Gf.BBox3d:
        """
        Computes the bound of the prim's descendents in world space while
        excluding the subtrees rooted at the paths in C{pathsToSkip}.


        Additionally, the parameter C{primOverride} overrides the local-to-
        world transform of the prim and C{ctmOverrides} is used to specify
        overrides the local-to-world transforms of certain paths underneath
        the prim.

        This leverages any pre-existing, cached bounds, but does not include
        the transform (if any) authored on the prim itself.

        See ComputeWorldBound() for notes on performance and error handling.
        """
    def GetBaseTime(self) -> pxr.Usd.TimeCode:
        """
        Return the base time if set, otherwise GetTime() .


        Use HasBaseTime() to observe if a base time has been set.
        """
    def GetIncludedPurposes(self) -> list[str]:
        """
        Get the current set of included purposes.
        """
    def GetTime(self) -> pxr.Usd.TimeCode:
        """
        Get the current time from which this cache is reading values.
        """
    def GetUseExtentsHint(self) -> bool:
        """
        Returns whether authored extent hints are used to compute bounding
        boxes.
        """
    def HasBaseTime(self) -> bool:
        """
        Return true if this cache has a baseTime that's been explicitly set,
        false otherwise.
        """
    def SetBaseTime(self, time: pxr.Usd.TimeCode | float | pxr.Sdf.TimeCode) -> None:
        """
        Set the base time value for this bbox cache.


        This value is used only when computing bboxes for point instancer
        instances (see ComputePointInstanceWorldBounds() , for example). See
        UsdGeomPointInstancer::ComputeExtentAtTime() for more information. If
        unset, the bbox cache uses its time ( GetTime() / SetTime() ) for this
        value.

        Note that setting the base time does not invalidate any cache entries.
        """
    def SetIncludedPurposes(self, includedPurposes: list[str] | list[pxr.Ar.ResolvedPath]) -> None:
        """
        Indicate the set of C{includedPurposes} to use when resolving child
        bounds.


        Each child's purpose must match one of the elements of this set to be
        included in the computation; if it does not, child is excluded.

        Note the use of *child* in the docs above, purpose is ignored for the
        prim for whose bounds are directly queried.

        Changing this value B{does not invalidate existing caches}.
        """
    def SetTime(self, time: pxr.Usd.TimeCode | float | pxr.Sdf.TimeCode) -> None:
        """
        Use the new C{time} when computing values and may clear any existing
        values cached for the previous time.


        Setting C{time} to the current time is a no-op.
        """

class BasisCurves(Curves):
    '''
    BasisCurves are a batched curve representation analogous to the
    classic RIB definition via Basis and Curves statements.


    BasisCurves are often used to render dense aggregate geometry like
    hair or grass.

    A\'matrix\'and\'vstep\'associated with the *basis* are used to interpolate
    the vertices of a cubic BasisCurves. (The basis attribute is unused
    for linear BasisCurves.)

    A single prim may have many curves whose count is determined
    implicitly by the length of the *curveVertexCounts* vector. Each
    individual curve is composed of one or more segments. Each segment is
    defined by four vertices for cubic curves and two vertices for linear
    curves. See the next section for more information on how to map curve
    vertex counts to segment counts.

    Segment Indexing
    ================

    Interpolating a curve requires knowing how to decompose it into its
    individual segments.

    The segments of a cubic curve are determined by the vertex count, the
    *wrap* (periodicity), and the vstep of the basis. For linear curves,
    the basis token is ignored and only the vertex count and wrap are
    needed.

    cubic basis

    vstep

    bezier

    3

    catmullRom

    1

    bspline

    1

    The first segment of a cubic (nonperiodic) curve is always defined by
    its first four points. The vstep is the increment used to determine
    what vertex indices define the next segment. For a two segment
    (nonperiodic) bspline basis curve (vstep = 1), the first segment will
    be defined by interpolating vertices [0, 1, 2, 3] and the second
    segment will be defined by [1, 2, 3, 4]. For a two segment bezier
    basis curve (vstep = 3), the first segment will be defined by
    interpolating vertices [0, 1, 2, 3] and the second segment will be
    defined by [3, 4, 5, 6]. If the vstep is not one, then you must take
    special care to make sure that the number of cvs properly divides by
    your vstep. (The indices described are relative to the initial vertex
    index for a batched curve.)

    For periodic curves, at least one of the curve\'s initial vertices are
    repeated to close the curve. For cubic curves, the number of vertices
    repeated is\'4 - vstep\'. For linear curves, only one vertex is repeated
    to close the loop.

    Pinned curves are a special case of nonperiodic curves that only
    affects the behavior of cubic Bspline and Catmull-Rom curves. To
    evaluate or render pinned curves, a client must effectively
    add\'phantom points\'at the beginning and end of every curve in a batch.
    These phantom points are injected to ensure that the interpolated
    curve begins at P[0] and ends at P[n-1].

    For a curve with initial point P[0] and last point P[n-1], the phantom
    points are defined as. P[-1] = 2 * P[0] - P[1] P[n] = 2 * P[n-1] -
    P[n-2]

    Pinned cubic curves will (usually) have to be unpacked into the
    standard nonperiodic representation before rendering. This unpacking
    can add some additional overhead. However, using pinned curves reduces
    the amount of data recorded in a scene and (more importantly) better
    records the authors\'intent for interchange.

    The additional phantom points mean that the minimum curve vertex count
    for cubic bspline and catmullRom curves is 2. Linear curve segments
    are defined by two vertices. A two segment linear curve\'s first
    segment would be defined by interpolating vertices [0, 1]. The second
    segment would be defined by vertices [1, 2]. (Again, for a batched
    curve, indices are relative to the initial vertex index.)

    When validating curve topology, each renderable entry in the
    curveVertexCounts vector must pass this check.

    type

    wrap

    validitity

    linear

    nonperiodic

    curveVertexCounts[i]>2

    linear

    periodic

    curveVertexCounts[i]>3

    cubic

    nonperiodic

    (curveVertexCounts[i] - 4) % vstep == 0

    cubic

    periodic

    (curveVertexCounts[i]) % vstep == 0

    cubic

    pinned (catmullRom/bspline)

    (curveVertexCounts[i] - 2)>= 0

    Cubic Vertex Interpolation
    ==========================

    Linear Vertex Interpolation
    ===========================

    Linear interpolation is always used on curves of type linear.\'t\'with
    domain [0, 1], the curve is defined by the equation P0 * (1-t) + P1 *
    t. t at 0 describes the first point and t at 1 describes the end
    point.

    Primvar Interpolation
    =====================

    For cubic curves, primvar data can be either interpolated cubically
    between vertices or linearly across segments. The corresponding token
    for cubic interpolation is\'vertex\'and for linear interpolation
    is\'varying\'. Per vertex data should be the same size as the number of
    vertices in your curve. Segment varying data is dependent on the wrap
    (periodicity) and number of segments in your curve. For linear curves,
    varying and vertex data would be interpolated the same way. By
    convention varying is the preferred interpolation because of the
    association of varying with linear interpolation.

    To convert an entry in the curveVertexCounts vector into a segment
    count for an individual curve, apply these rules. Sum up all the
    results in order to compute how many total segments all curves have.

    The following tables describe the expected segment count for the\'i\'th
    curve in a curve batch as well as the entire batch. Python syntax
    like\'[:]\'(to describe all members of an array) and\'len(...)\'(to
    describe the length of an array) are used.

    type

    wrap

    curve segment count

    batch segment count

    linear

    nonperiodic

    curveVertexCounts[i] - 1

    sum(curveVertexCounts[:]) - len(curveVertexCounts)

    linear

    periodic

    curveVertexCounts[i]

    sum(curveVertexCounts[:])

    cubic

    nonperiodic

    (curveVertexCounts[i] - 4) / vstep + 1

    sum(curveVertexCounts[:] - 4) / vstep + len(curveVertexCounts)

    cubic

    periodic

    curveVertexCounts[i] / vstep

    sum(curveVertexCounts[:]) / vstep

    cubic

    pinned (catmullRom/bspline)

    (curveVertexCounts[i] - 2) + 1

    sum(curveVertexCounts[:] - 2) + len(curveVertexCounts)

    The following table descrives the expected size of varying (linearly
    interpolated) data, derived from the segment counts computed above.

    wrap

    curve varying count

    batch varying count

    nonperiodic/pinned

    segmentCounts[i] + 1

    sum(segmentCounts[:]) + len(curveVertexCounts)

    periodic

    segmentCounts[i]

    sum(segmentCounts[:])

    Both curve types additionally define\'constant\'interpolation for the
    entire prim and\'uniform\'interpolation as per curve data.

    Take care when providing support for linearly interpolated data for
    cubic curves. Its shape doesn\'t provide a one to one mapping with
    either the number of curves (like\'uniform\') or the number of vertices
    (like\'vertex\') and so it is often overlooked. This is the only
    primitive in UsdGeom (as of this writing) where this is true. For
    meshes, while they use different interpolation
    methods,\'varying\'and\'vertex\'are both specified per point. It\'s common
    to assume that curves follow a similar pattern and build in structures
    and language for per primitive, per element, and per point data only
    to come upon these arrays that don\'t quite fit into either of those
    categories. It is also common to conflate\'varying\'with being per
    segment data and use the segmentCount rules table instead of its
    neighboring varying data table rules. We suspect that this is because
    for the common case of nonperiodic cubic curves, both the provided
    segment count and varying data size formula end with\'+ 1\'. While
    debugging, users may look at the double\'+ 1\'as a mistake and try to
    remove it. We take this time to enumerate these issues because we\'ve
    fallen into them before and hope that we save others time in their own
    implementations. As an example of deriving per curve segment and
    varying primvar data counts from the wrap, type, basis, and
    curveVertexCount, the following table is provided.

    wrap

    type

    basis

    curveVertexCount

    curveSegmentCount

    varyingDataCount

    nonperiodic

    linear

    N/A

    [2 3 2 5]

    [1 2 1 4]

    [2 3 2 5]

    nonperiodic

    cubic

    bezier

    [4 7 10 4 7]

    [1 2 3 1 2]

    [2 3 4 2 3]

    nonperiodic

    cubic

    bspline

    [5 4 6 7]

    [2 1 3 4]

    [3 2 4 5]

    periodic

    cubic

    bezier

    [6 9 6]

    [2 3 2]

    [2 3 2]

    periodic

    linear

    N/A

    [3 7]

    [3 7]

    [3 7]

    Tubes and Ribbons
    =================

    The strictest definition of a curve as an infinitely thin wire is not
    particularly useful for describing production scenes. The additional
    *widths* and *normals* attributes can be used to describe cylindrical
    tubes and or flat oriented ribbons.

    Curves with only widths defined are imaged as tubes with radius\'width
    / 2\'. Curves with both widths and normals are imaged as ribbons
    oriented in the direction of the interpolated normal vectors.

    While not technically UsdGeomPrimvars, widths and normals also have
    interpolation metadata. It\'s common for authored widths to have
    constant, varying, or vertex interpolation (see
    UsdGeomCurves::GetWidthsInterpolation() ). It\'s common for authored
    normals to have varying interpolation (see
    UsdGeomPointBased::GetNormalsInterpolation() ).

    The file used to generate these curves can be found in
    extras/usd/examples/usdGeomExamples/basisCurves.usda. It\'s provided as
    a reference on how to properly image both tubes and ribbons. The first
    row of curves are linear; the second are cubic bezier. (We aim in
    future releases of HdSt to fix the discontinuity seen with broken
    tangents to better match offline renderers like RenderMan.) The yellow
    and violet cubic curves represent cubic vertex width interpolation for
    which there is no equivalent for linear curves.

    How did this prim type get its name? This prim is a portmanteau of two
    different statements in the original RenderMan
    specification:\'Basis\'and\'Curves\'. For any described attribute
    *Fallback* *Value* or *Allowed* *Values* below that are text/tokens,
    the actual token is published and defined in UsdGeomTokens. So to set
    an attribute to the value"rightHanded", use UsdGeomTokens->rightHanded
    as the value.
    '''
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None:
        """
        Construct a UsdGeomBasisCurves on UsdPrim C{prim}.


        Equivalent to UsdGeomBasisCurves::Get (prim.GetStage(),
        prim.GetPath()) for a *valid* C{prim}, but will not immediately throw
        an error for an invalid C{prim}
        """
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None:
        """
        Construct a UsdGeomBasisCurves on the prim held by C{schemaObj}.


        Should be preferred over UsdGeomBasisCurves (schemaObj.GetPrim()), as
        it preserves SchemaBase state.
        """
    def ComputeInterpolationForSize(self, _n: int, _timeCode: pxr.Usd.TimeCode | float | pxr.Sdf.TimeCode, /) -> tuple[str, list[tuple[str, int]]]:
        """
        Computes interpolation token for C{n}.


        If this returns an empty token and C{info} was non-None, it'll contain
        the expected value for each token.

        The topology is determined using C{timeCode}.
        """
    def ComputeUniformDataSize(self, _timeCode: pxr.Usd.TimeCode | float | pxr.Sdf.TimeCode, /) -> int:
        '''
        Computes the expected size for data with"uniform"interpolation.


        If you\'re trying to determine what interpolation to use, it is more
        efficient to use C{ComputeInterpolationForSize}
        '''
    def ComputeVaryingDataSize(self, _timeCode: pxr.Usd.TimeCode | float | pxr.Sdf.TimeCode, /) -> int:
        '''
        Computes the expected size for data with"varying"interpolation.


        If you\'re trying to determine what interpolation to use, it is more
        efficient to use C{ComputeInterpolationForSize}
        '''
    def ComputeVertexDataSize(self, _timeCode: pxr.Usd.TimeCode | float | pxr.Sdf.TimeCode, /) -> int:
        '''
        Computes the expected size for data with"vertex"interpolation.


        If you\'re trying to determine what interpolation to use, it is more
        efficient to use C{ComputeInterpolationForSize}
        '''
    def CreateBasisAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetBasisAttr() , and also Create vs Get Property Methods for when
        to use Get vs Create.


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
    def CreateWrapAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetWrapAttr() , and also Create vs Get Property Methods for when
        to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    @staticmethod
    def Define(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> BasisCurves:
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
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> BasisCurves:
        """
        Return a UsdGeomBasisCurves holding the prim adhering to this schema
        at C{path} on C{stage}.


        If no prim exists at C{path} on C{stage}, or if the prim at that path
        does not adhere to this schema, return an invalid schema object. This
        is shorthand for the following: ::

          UsdGeomBasisCurves(stage->GetPrimAtPath(path));

        """
    def GetBasisAttr(self) -> pxr.Usd.Attribute:
        '''
        The basis specifies the vstep and matrix used for cubic interpolation.



        The\'hermite\'and\'power\'tokens have been removed. We\'ve provided
        UsdGeomHermiteCurves as an alternative for the\'hermite\'basis.

        Declaration

        C{uniform token basis ="bezier"}

        C++ Type

        TfToken

        Usd Type

        SdfValueTypeNames->Token

        Variability

        SdfVariabilityUniform

        Allowed Values

        bezier, bspline, catmullRom
        '''
    @staticmethod
    def GetSchemaAttributeNames(includeInherited: bool = ...) -> list[str]:
        """
        Return a vector of names of all pre-declared attributes for this
        schema class and all its ancestor classes.


        Does not include attributes that may be authored by custom/extended
        methods of the schemas involved.
        """
    def GetTypeAttr(self) -> pxr.Usd.Attribute:
        '''
        Linear curves interpolate linearly between two vertices.


        Cubic curves use a basis matrix with four vertices to interpolate a
        segment.

        Declaration

        C{uniform token type ="cubic"}

        C++ Type

        TfToken

        Usd Type

        SdfValueTypeNames->Token

        Variability

        SdfVariabilityUniform

        Allowed Values

        linear, cubic
        '''
    def GetWrapAttr(self) -> pxr.Usd.Attribute:
        '''
        If wrap is set to periodic, the curve when rendered will repeat the
        initial vertices (dependent on the vstep) to close the curve.


        If wrap is set to\'pinned\', phantom points may be created to ensure
        that the curve interpolation starts at P[0] and ends at P[n-1].

        Declaration

        C{uniform token wrap ="nonperiodic"}

        C++ Type

        TfToken

        Usd Type

        SdfValueTypeNames->Token

        Variability

        SdfVariabilityUniform

        Allowed Values

        nonperiodic, periodic, pinned
        '''
    @staticmethod
    def _GetStaticTfType() -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...

class Boundable(Xformable):
    '''
    Boundable introduces the ability for a prim to persistently cache a
    rectilinear, local-space, extent.


    Why Extent and not Bounds ?
    ===========================

    Boundable introduces the notion of"extent", which is a cached
    computation of a prim\'s local-space 3D range for its resolved
    attributes B{at the layer and time in which extent is authored}. We
    have found that with composed scene description, attempting to cache
    pre-computed bounds at interior prims in a scene graph is very
    fragile, given the ease with which one can author a single attribute
    in a stronger layer that can invalidate many authored caches - or with
    which a re-published, referenced asset can do the same.

    Therefore, we limit to precomputing (generally) leaf-prim extent,
    which avoids the need to read in large point arrays to compute bounds,
    and provides UsdGeomBBoxCache the means to efficiently compute and
    (session-only) cache intermediate bounds. You are free to compute and
    author intermediate bounds into your scenes, of course, which may work
    well if you have sufficient locks on your pipeline to guarantee that
    once authored, the geometry and transforms upon which they are based
    will remain unchanged, or if accuracy of the bounds is not an ironclad
    requisite.

    When intermediate bounds are authored on Boundable parents, the child
    prims will be pruned from BBox computation; the authored extent is
    expected to incorporate all child bounds.
    '''
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None:
        """
        Construct a UsdGeomBoundable on UsdPrim C{prim}.


        Equivalent to UsdGeomBoundable::Get (prim.GetStage(), prim.GetPath())
        for a *valid* C{prim}, but will not immediately throw an error for an
        invalid C{prim}
        """
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None:
        """
        Construct a UsdGeomBoundable on the prim held by C{schemaObj}.


        Should be preferred over UsdGeomBoundable (schemaObj.GetPrim()), as it
        preserves SchemaBase state.
        """
    def ComputeExtent(self, time: pxr.Usd.TimeCode | float | pxr.Sdf.TimeCode) -> pxr.Vt.Vec3fArray:
        """
        If an extent is authored on this boundable, it queries the C{extent}
        from the extent attribute, otherwise if ComputeExtentFunction is
        registered for the boundable's type, it computes the C{extent} at
        C{time}.


        Returns true when extent is successfully populated, false otherwise.

        ComputeExtentFromPlugins

        UsdGeomRegisterComputeExtentFunction
        """
    @overload
    @staticmethod
    def ComputeExtentFromPlugins(boundable: Boundable, time: pxr.Usd.TimeCode | float | pxr.Sdf.TimeCode) -> pxr.Vt.Vec3fArray:
        """
        Compute the extent for the Boundable prim C{boundable} at time
        C{time}.


        If successful, populates C{extent} with the result and returns
        C{true}, otherwise returns C{false}.

        The extent computation is based on the concrete type of the prim
        represented by C{boundable}. Plugins that provide a Boundable prim
        type may implement and register an extent computation for that type
        using UsdGeomRegisterComputeExtentFunction. ComputeExtentFromPlugins
        will use this function to compute extents for all prims of that type.
        If no function has been registered for a prim type, but a function has
        been registered for one of its base types, that function will be used
        instead.

        This function may load plugins in order to access the extent
        computation for a prim type.
        """
    @overload
    @staticmethod
    def ComputeExtentFromPlugins(boundable: Boundable, time: pxr.Usd.TimeCode | float | pxr.Sdf.TimeCode, transform: pxr.Gf.Matrix4d) -> pxr.Vt.Vec3fArray:
        """
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        Computes the extent as if the matrix C{transform} was first applied.
        """
    def CreateExtentAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetExtentAttr() , and also Create vs Get Property Methods for when
        to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    @staticmethod
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> Boundable:
        """
        Return a UsdGeomBoundable holding the prim adhering to this schema at
        C{path} on C{stage}.


        If no prim exists at C{path} on C{stage}, or if the prim at that path
        does not adhere to this schema, return an invalid schema object. This
        is shorthand for the following: ::

          UsdGeomBoundable(stage->GetPrimAtPath(path));

        """
    def GetExtentAttr(self) -> pxr.Usd.Attribute:
        """
        Extent is a three dimensional range measuring the geometric extent of
        the authored gprim in its own local space (i.e.


        its own transform not applied), *without* accounting for any shader-
        induced displacement. If B{any} extent value has been authored for a
        given Boundable, then it should be authored at every timeSample at
        which geometry-affecting properties are authored, to ensure correct
        evaluation via ComputeExtent() . If B{no} extent value has been
        authored, then ComputeExtent() will call the Boundable's registered
        ComputeExtentFunction(), which may be expensive, which is why we
        strongly encourage proper authoring of extent.

        ComputeExtent()

        Why Extent and not Bounds? . An authored extent on a prim which has
        children is expected to include the extent of all children, as they
        will be pruned from BBox computation during traversal.

        Declaration

        C{float3[] extent}

        C++ Type

        VtArray<GfVec3f>

        Usd Type

        SdfValueTypeNames->Float3Array
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

class Camera(Xformable):
    '''
    Transformable camera.


    Describes optical properties of a camera via a common set of
    attributes that provide control over the camera\'s frustum as well as
    its depth of field. For stereo, the left and right camera are
    individual prims tagged through the stereoRole attribute.

    There is a corresponding class GfCamera, which can hold the state of a
    camera (at a particular time). UsdGeomCamera::GetCamera() and
    UsdGeomCamera::SetFromCamera() convert between a USD camera prim and a
    GfCamera.

    To obtain the camera\'s location in world space, call the following on
    a UsdGeomCamera \'camera\': ::

      GfMatrix4d camXform = camera.ComputeLocalToWorldTransform(time);

    B{Cameras in USD are always"Y up", regardless of the stage\'s
    orientation (i.e. UsdGeomGetStageUpAxis() ).} This means that the
    inverse of\'camXform\'(the VIEW half of the MODELVIEW transform in
    OpenGL parlance) will transform the world such that the camera is at
    the origin, looking down the -Z axis, with +Y as the up axis, and +X
    pointing to the right. This describes a B{right handed coordinate
    system}.

    Units of Measure for Camera Properties
    ======================================

    Despite the familiarity of millimeters for specifying some physical
    camera properties, UsdGeomCamera opts for greater consistency with all
    other UsdGeom schemas, which measure geometric properties in scene
    units, as determined by UsdGeomGetStageMetersPerUnit() . We do make a
    concession, however, in that lens and filmback properties are measured
    in B{tenths of a scene unit} rather than"raw"scene units. This means
    that with the fallback value of.01 for *metersPerUnit* - i.e. scene
    unit of centimeters - then these"tenth of scene unit"properties are
    effectively millimeters.

    If one adds a Camera prim to a UsdStage whose scene unit is not
    centimeters, the fallback values for filmback properties will be
    incorrect (or at the least, unexpected) in an absolute sense; however,
    proper imaging through a"default camera"with focusing disabled depends
    only on ratios of the other properties, so the camera is still usable.
    However, it follows that if even one property is authored in the
    correct scene units, then they all must be.

    Linear Algebra in UsdGeom For any described attribute *Fallback*
    *Value* or *Allowed* *Values* below that are text/tokens, the actual
    token is published and defined in UsdGeomTokens. So to set an
    attribute to the value"rightHanded", use UsdGeomTokens->rightHanded as
    the value.
    '''
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None:
        """
        Construct a UsdGeomCamera on UsdPrim C{prim}.


        Equivalent to UsdGeomCamera::Get (prim.GetStage(), prim.GetPath()) for
        a *valid* C{prim}, but will not immediately throw an error for an
        invalid C{prim}
        """
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None:
        """
        Construct a UsdGeomCamera on the prim held by C{schemaObj}.


        Should be preferred over UsdGeomCamera (schemaObj.GetPrim()), as it
        preserves SchemaBase state.
        """
    def CreateClippingPlanesAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetClippingPlanesAttr() , and also Create vs Get Property Methods
        for when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateClippingRangeAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetClippingRangeAttr() , and also Create vs Get Property Methods
        for when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateExposureAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetExposureAttr() , and also Create vs Get Property Methods for
        when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateFStopAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetFStopAttr() , and also Create vs Get Property Methods for when
        to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateFocalLengthAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetFocalLengthAttr() , and also Create vs Get Property Methods for
        when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateFocusDistanceAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetFocusDistanceAttr() , and also Create vs Get Property Methods
        for when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateHorizontalApertureAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetHorizontalApertureAttr() , and also Create vs Get Property
        Methods for when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateHorizontalApertureOffsetAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetHorizontalApertureOffsetAttr() , and also Create vs Get
        Property Methods for when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateProjectionAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetProjectionAttr() , and also Create vs Get Property Methods for
        when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateShutterCloseAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetShutterCloseAttr() , and also Create vs Get Property Methods
        for when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateShutterOpenAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetShutterOpenAttr() , and also Create vs Get Property Methods for
        when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateStereoRoleAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetStereoRoleAttr() , and also Create vs Get Property Methods for
        when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateVerticalApertureAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetVerticalApertureAttr() , and also Create vs Get Property
        Methods for when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateVerticalApertureOffsetAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetVerticalApertureOffsetAttr() , and also Create vs Get Property
        Methods for when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    @staticmethod
    def Define(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> Camera:
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
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> Camera:
        """
        Return a UsdGeomCamera holding the prim adhering to this schema at
        C{path} on C{stage}.


        If no prim exists at C{path} on C{stage}, or if the prim at that path
        does not adhere to this schema, return an invalid schema object. This
        is shorthand for the following: ::

          UsdGeomCamera(stage->GetPrimAtPath(path));

        """
    def GetCamera(self, time: pxr.Usd.TimeCode | float | pxr.Sdf.TimeCode = ...) -> pxr.Gf.Camera:
        """
        Creates a GfCamera object from the attribute values at C{time}.
        """
    def GetClippingPlanesAttr(self) -> pxr.Usd.Attribute:
        """
        Additional, arbitrarily oriented clipping planes.


        A vector (a,b,c,d) encodes a clipping plane that cuts off (x,y,z) with
        a * x + b * y + c * z + d * 1<0 where (x,y,z) are the coordinates in
        the camera's space.

        Declaration

        C{float4[] clippingPlanes = []}

        C++ Type

        VtArray<GfVec4f>

        Usd Type

        SdfValueTypeNames->Float4Array
        """
    def GetClippingRangeAttr(self) -> pxr.Usd.Attribute:
        """
        Near and far clipping distances in scene units; see Units of Measure
        for Camera Properties.



        Declaration

        C{float2 clippingRange = (1, 1000000)}

        C++ Type

        GfVec2f

        Usd Type

        SdfValueTypeNames->Float2
        """
    def GetExposureAttr(self) -> pxr.Usd.Attribute:
        """
        Exposure adjustment, as a log base-2 value.


        The default of 0.0 has no effect. A value of 1.0 will double the
        image-plane intensities in a rendered image; a value of -1.0 will
        halve them.

        Declaration

        C{float exposure = 0}

        C++ Type

        float

        Usd Type

        SdfValueTypeNames->Float
        """
    def GetFStopAttr(self) -> pxr.Usd.Attribute:
        """
        Lens aperture.


        Defaults to 0.0, which turns off focusing.

        Declaration

        C{float fStop = 0}

        C++ Type

        float

        Usd Type

        SdfValueTypeNames->Float
        """
    def GetFocalLengthAttr(self) -> pxr.Usd.Attribute:
        """
        Perspective focal length in tenths of a scene unit; see Units of
        Measure for Camera Properties.



        Declaration

        C{float focalLength = 50}

        C++ Type

        float

        Usd Type

        SdfValueTypeNames->Float
        """
    def GetFocusDistanceAttr(self) -> pxr.Usd.Attribute:
        """
        Distance from the camera to the focus plane in scene units; see Units
        of Measure for Camera Properties.



        Declaration

        C{float focusDistance = 0}

        C++ Type

        float

        Usd Type

        SdfValueTypeNames->Float
        """
    def GetHorizontalApertureAttr(self) -> pxr.Usd.Attribute:
        """
        Horizontal aperture in tenths of a scene unit; see Units of Measure
        for Camera Properties.


        Default is the equivalent of the standard 35mm spherical projector
        aperture.

        Declaration

        C{float horizontalAperture = 20.955}

        C++ Type

        float

        Usd Type

        SdfValueTypeNames->Float
        """
    def GetHorizontalApertureOffsetAttr(self) -> pxr.Usd.Attribute:
        """
        Horizontal aperture offset in the same units as horizontalAperture.


        Defaults to 0.

        Declaration

        C{float horizontalApertureOffset = 0}

        C++ Type

        float

        Usd Type

        SdfValueTypeNames->Float
        """
    def GetProjectionAttr(self) -> pxr.Usd.Attribute:
        '''

        Declaration

        C{token projection ="perspective"}

        C++ Type

        TfToken

        Usd Type

        SdfValueTypeNames->Token

        Allowed Values

        perspective, orthographic
        '''
    @staticmethod
    def GetSchemaAttributeNames(includeInherited: bool = ...) -> list[str]:
        """
        Return a vector of names of all pre-declared attributes for this
        schema class and all its ancestor classes.


        Does not include attributes that may be authored by custom/extended
        methods of the schemas involved.
        """
    def GetShutterCloseAttr(self) -> pxr.Usd.Attribute:
        """
        Frame relative shutter close time, analogous comments from
        shutter:open apply.


        A value greater or equal to shutter:open should be authored, otherwise
        there is no exposure and a renderer should produce a black image.

        Declaration

        C{double shutter:close = 0}

        C++ Type

        double

        Usd Type

        SdfValueTypeNames->Double
        """
    def GetShutterOpenAttr(self) -> pxr.Usd.Attribute:
        """
        Frame relative shutter open time in UsdTimeCode units (negative value
        indicates that the shutter opens before the current frame time).


        Used for motion blur.

        Declaration

        C{double shutter:open = 0}

        C++ Type

        double

        Usd Type

        SdfValueTypeNames->Double
        """
    def GetStereoRoleAttr(self) -> pxr.Usd.Attribute:
        '''
        If different from mono, the camera is intended to be the left or right
        camera of a stereo setup.



        Declaration

        C{uniform token stereoRole ="mono"}

        C++ Type

        TfToken

        Usd Type

        SdfValueTypeNames->Token

        Variability

        SdfVariabilityUniform

        Allowed Values

        mono, left, right
        '''
    def GetVerticalApertureAttr(self) -> pxr.Usd.Attribute:
        """
        Vertical aperture in tenths of a scene unit; see Units of Measure for
        Camera Properties.


        Default is the equivalent of the standard 35mm spherical projector
        aperture.

        Declaration

        C{float verticalAperture = 15.2908}

        C++ Type

        float

        Usd Type

        SdfValueTypeNames->Float
        """
    def GetVerticalApertureOffsetAttr(self) -> pxr.Usd.Attribute:
        """
        Vertical aperture offset in the same units as verticalAperture.


        Defaults to 0.

        Declaration

        C{float verticalApertureOffset = 0}

        C++ Type

        float

        Usd Type

        SdfValueTypeNames->Float
        """
    def SetFromCamera(self, camera: pxr.Gf.Camera, time: pxr.Usd.TimeCode | float | pxr.Sdf.TimeCode = ...) -> None:
        """
        Write attribute values from C{camera} for C{time}.


        These attributes will be updated:
           - projection

           - horizontalAperture

           - horizontalApertureOffset

           - verticalAperture

           - verticalApertureOffset

           - focalLength

           - clippingRange

           - clippingPlanes

           - fStop

           - focalDistance

           - xformOpOrder and xformOp:transform

        This will clear any existing xformOpOrder and replace it with a single
        xformOp:transform entry. The xformOp:transform property is created or
        updated here to match the transform on C{camera}. This operation will
        fail if there are stronger xform op opinions in the composed layer
        stack that are stronger than that of the current edit target.
        """
    @staticmethod
    def _GetStaticTfType() -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...

class Capsule(Gprim):
    '''
    Defines a primitive capsule, i.e.


    a cylinder capped by two half spheres, centered at the origin, whose
    spine is along the specified *axis*. The spherical cap heights
    (sagitta) of the two endcaps are a function of the relative radii of
    the endcaps, such that cylinder tangent and sphere tangent are
    coincident and maintain C1 continuity.

    For any described attribute *Fallback* *Value* or *Allowed* *Values*
    below that are text/tokens, the actual token is published and defined
    in UsdGeomTokens. So to set an attribute to the value"rightHanded",
    use UsdGeomTokens->rightHanded as the value.
    '''
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None:
        """
        Construct a UsdGeomCapsule on UsdPrim C{prim}.


        Equivalent to UsdGeomCapsule::Get (prim.GetStage(), prim.GetPath())
        for a *valid* C{prim}, but will not immediately throw an error for an
        invalid C{prim}
        """
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None:
        """
        Construct a UsdGeomCapsule on the prim held by C{schemaObj}.


        Should be preferred over UsdGeomCapsule (schemaObj.GetPrim()), as it
        preserves SchemaBase state.
        """
    def CreateAxisAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetAxisAttr() , and also Create vs Get Property Methods for when
        to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateExtentAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetExtentAttr() , and also Create vs Get Property Methods for when
        to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateHeightAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetHeightAttr() , and also Create vs Get Property Methods for when
        to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateRadiusAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetRadiusAttr() , and also Create vs Get Property Methods for when
        to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    @staticmethod
    def Define(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> Capsule:
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
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> Capsule:
        """
        Return a UsdGeomCapsule holding the prim adhering to this schema at
        C{path} on C{stage}.


        If no prim exists at C{path} on C{stage}, or if the prim at that path
        does not adhere to this schema, return an invalid schema object. This
        is shorthand for the following: ::

          UsdGeomCapsule(stage->GetPrimAtPath(path));

        """
    def GetAxisAttr(self) -> pxr.Usd.Attribute:
        '''
        The axis along which the spine of the capsule is aligned.



        Declaration

        C{uniform token axis ="Z"}

        C++ Type

        TfToken

        Usd Type

        SdfValueTypeNames->Token

        Variability

        SdfVariabilityUniform

        Allowed Values

        X, Y, Z
        '''
    def GetExtentAttr(self) -> pxr.Usd.Attribute:
        """
        Extent is re-defined on Capsule only to provide a fallback value.



        UsdGeomGprim::GetExtentAttr() .

        Declaration

        C{float3[] extent = [(-0.5, -0.5, -1), (0.5, 0.5, 1)]}

        C++ Type

        VtArray<GfVec3f>

        Usd Type

        SdfValueTypeNames->Float3Array
        """
    def GetHeightAttr(self) -> pxr.Usd.Attribute:
        """
        The length of the capsule's spine along the specified *axis* excluding
        the size of the two half spheres, i.e.


        the length of the cylinder portion of the capsule. If you author
        *height* you must also author *extent*.

        GetExtentAttr()

        Declaration

        C{double height = 1}

        C++ Type

        double

        Usd Type

        SdfValueTypeNames->Double
        """
    def GetRadiusAttr(self) -> pxr.Usd.Attribute:
        """
        The radius of the capsule.


        If you author *radius* you must also author *extent*.

        GetExtentAttr()

        Declaration

        C{double radius = 0.5}

        C++ Type

        double

        Usd Type

        SdfValueTypeNames->Double
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

class Capsule_1(Gprim):
    '''
    Defines a primitive capsule, i.e.


    a cylinder capped by two half spheres, with potentially different
    radii, centered at the origin, and whose spine is along the specified
    *axis*. The spherical cap heights (sagitta) of the two endcaps are a
    function of the relative radii of the endcaps, such that cylinder
    tangent and sphere tangent are coincident and maintain C1 continuity.

    For any described attribute *Fallback* *Value* or *Allowed* *Values*
    below that are text/tokens, the actual token is published and defined
    in UsdGeomTokens. So to set an attribute to the value"rightHanded",
    use UsdGeomTokens->rightHanded as the value.
    '''
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None:
        """
        Construct a UsdGeomCapsule_1 on UsdPrim C{prim}.


        Equivalent to UsdGeomCapsule_1::Get (prim.GetStage(), prim.GetPath())
        for a *valid* C{prim}, but will not immediately throw an error for an
        invalid C{prim}
        """
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None:
        """
        Construct a UsdGeomCapsule_1 on the prim held by C{schemaObj}.


        Should be preferred over UsdGeomCapsule_1 (schemaObj.GetPrim()), as it
        preserves SchemaBase state.
        """
    def CreateAxisAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetAxisAttr() , and also Create vs Get Property Methods for when
        to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateExtentAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetExtentAttr() , and also Create vs Get Property Methods for when
        to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateHeightAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetHeightAttr() , and also Create vs Get Property Methods for when
        to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateRadiusBottomAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetRadiusBottomAttr() , and also Create vs Get Property Methods
        for when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateRadiusTopAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetRadiusTopAttr() , and also Create vs Get Property Methods for
        when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    @staticmethod
    def Define(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> Capsule_1:
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
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> Capsule_1:
        """
        Return a UsdGeomCapsule_1 holding the prim adhering to this schema at
        C{path} on C{stage}.


        If no prim exists at C{path} on C{stage}, or if the prim at that path
        does not adhere to this schema, return an invalid schema object. This
        is shorthand for the following: ::

          UsdGeomCapsule_1(stage->GetPrimAtPath(path));

        """
    def GetAxisAttr(self) -> pxr.Usd.Attribute:
        '''
        The axis along which the spine of the capsule is aligned.



        Declaration

        C{uniform token axis ="Z"}

        C++ Type

        TfToken

        Usd Type

        SdfValueTypeNames->Token

        Variability

        SdfVariabilityUniform

        Allowed Values

        X, Y, Z
        '''
    def GetExtentAttr(self) -> pxr.Usd.Attribute:
        """
        Extent is re-defined on Capsule only to provide a fallback value.



        UsdGeomGprim::GetExtentAttr() .

        Declaration

        C{float3[] extent = [(-0.5, -0.5, -1), (0.5, 0.5, 1)]}

        C++ Type

        VtArray<GfVec3f>

        Usd Type

        SdfValueTypeNames->Float3Array
        """
    def GetHeightAttr(self) -> pxr.Usd.Attribute:
        """
        The length of the capsule's spine along the specified *axis* excluding
        the size of the two half spheres, i.e.


        the length of the cylinder portion of the capsule. If you author
        *height* you must also author *extent*.

        GetExtentAttr()

        Declaration

        C{double height = 1}

        C++ Type

        double

        Usd Type

        SdfValueTypeNames->Double
        """
    def GetRadiusBottomAttr(self) -> pxr.Usd.Attribute:
        """
        The radius of the capping sphere at the bottom of the capsule - i.e.


        the sphere located in the direction of the negative *axis*. If you
        author *radius* you must also author *extent*.

        GetExtentAttr()

        Declaration

        C{double radiusBottom = 0.5}

        C++ Type

        double

        Usd Type

        SdfValueTypeNames->Double
        """
    def GetRadiusTopAttr(self) -> pxr.Usd.Attribute:
        """
        The radius of the capping sphere at the top of the capsule - i.e.


        the sphere in the direction of the positive *axis*. If you author
        *radius* you must also author *extent*.

        GetExtentAttr()

        Declaration

        C{double radiusTop = 0.5}

        C++ Type

        double

        Usd Type

        SdfValueTypeNames->Double
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

class Cone(Gprim):
    '''
    Defines a primitive cone, centered at the origin, whose spine is along
    the specified *axis*, with the apex of the cone pointing in the
    direction of the positive axis.


    The fallback values for Cube, Sphere, Cone, and Cylinder are set so
    that they all pack into the same volume/bounds.

    For any described attribute *Fallback* *Value* or *Allowed* *Values*
    below that are text/tokens, the actual token is published and defined
    in UsdGeomTokens. So to set an attribute to the value"rightHanded",
    use UsdGeomTokens->rightHanded as the value.
    '''
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None:
        """
        Construct a UsdGeomCone on UsdPrim C{prim}.


        Equivalent to UsdGeomCone::Get (prim.GetStage(), prim.GetPath()) for a
        *valid* C{prim}, but will not immediately throw an error for an
        invalid C{prim}
        """
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None:
        """
        Construct a UsdGeomCone on the prim held by C{schemaObj}.


        Should be preferred over UsdGeomCone (schemaObj.GetPrim()), as it
        preserves SchemaBase state.
        """
    def CreateAxisAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetAxisAttr() , and also Create vs Get Property Methods for when
        to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateExtentAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetExtentAttr() , and also Create vs Get Property Methods for when
        to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateHeightAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetHeightAttr() , and also Create vs Get Property Methods for when
        to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateRadiusAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetRadiusAttr() , and also Create vs Get Property Methods for when
        to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    @staticmethod
    def Define(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> Cone:
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
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> Cone:
        """
        Return a UsdGeomCone holding the prim adhering to this schema at
        C{path} on C{stage}.


        If no prim exists at C{path} on C{stage}, or if the prim at that path
        does not adhere to this schema, return an invalid schema object. This
        is shorthand for the following: ::

          UsdGeomCone(stage->GetPrimAtPath(path));

        """
    def GetAxisAttr(self) -> pxr.Usd.Attribute:
        '''
        The axis along which the spine of the cone is aligned.



        Declaration

        C{uniform token axis ="Z"}

        C++ Type

        TfToken

        Usd Type

        SdfValueTypeNames->Token

        Variability

        SdfVariabilityUniform

        Allowed Values

        X, Y, Z
        '''
    def GetExtentAttr(self) -> pxr.Usd.Attribute:
        """
        Extent is re-defined on Cone only to provide a fallback value.



        UsdGeomGprim::GetExtentAttr() .

        Declaration

        C{float3[] extent = [(-1, -1, -1), (1, 1, 1)]}

        C++ Type

        VtArray<GfVec3f>

        Usd Type

        SdfValueTypeNames->Float3Array
        """
    def GetHeightAttr(self) -> pxr.Usd.Attribute:
        """
        The length of the cone's spine along the specified *axis*.


        If you author *height* you must also author *extent*.

        GetExtentAttr()

        Declaration

        C{double height = 2}

        C++ Type

        double

        Usd Type

        SdfValueTypeNames->Double
        """
    def GetRadiusAttr(self) -> pxr.Usd.Attribute:
        """
        The radius of the cone.


        If you author *radius* you must also author *extent*.

        GetExtentAttr()

        Declaration

        C{double radius = 1}

        C++ Type

        double

        Usd Type

        SdfValueTypeNames->Double
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

class ConstraintTarget(Boost.Python.instance):
    """
    Schema wrapper for UsdAttribute for authoring and introspecting
    attributes that are constraint targets.


    Constraint targets correspond roughly to what some DCC's call
    locators. They are coordinate frames, represented as (animated or
    static) GfMatrix4d values. We represent them as attributes in USD
    rather than transformable prims because generally we require no other
    coordinated information about a constraint target other than its name
    and its matrix value, and because attributes are more concise than
    prims.

    Because consumer clients often care only about the identity and value
    of constraint targets and may be able to usefully consume them without
    caring about the actual geometry with which they may logically
    correspond, UsdGeom aggregates all constraint targets onto a model's
    root prim, assuming that an exporter will use property namespacing
    within the constraint target attribute's name to indicate a path to a
    prim within the model with which the constraint target may correspond.

    To facilitate instancing, and also position-tweaking of baked assets,
    we stipulate that constraint target values always be recorded in
    B{model-relative transformation space}. In other words, to get the
    world-space value of a constraint target, transform it by the local-
    to-world transformation of the prim on which it is recorded.
    ComputeInWorldSpace() will perform this calculation.
    """
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, attr: pxr.Usd.Attribute | ConstraintTarget | Primvar | XformOp | pxr.UsdShade.Input | pxr.UsdShade.Output) -> None:
        """
        Speculative constructor that will produce a valid
        UsdGeomConstraintTarget when C{attr} already represents an attribute
        that is a UsdGeomConstraintTarget, and produces an *invalid*
        UsdGeomConstraintTarget otherwise (i.e.


        UsdGeomConstraintTarget_explicit_bool will return false).

        Calling C{UsdGeomConstraintTarget::IsValid(attr)} will return the same
        truth value as the object returned by this constructor, but if you
        plan to subsequently use the ConstraintTarget anyways, just construct
        the object and bool-evaluate it before proceeding.
        """
    def ComputeInWorldSpace(self, time: pxr.Usd.TimeCode | float | pxr.Sdf.TimeCode = ...) -> pxr.Gf.Matrix4d:
        """
        Computes the value of the constraint target in world space.


        If a valid UsdGeomXformCache is provided in the argument C{xfCache},
        it is used to evaluate the CTM of the model to which the constraint
        target belongs.

        To get the constraint value in model-space (or local space), simply
        use UsdGeomConstraintTarget::Get() , since the authored values must
        already be in model-space.
        """
    def Get(self, _value: pxr.Gf.Matrix4d, /, time: pxr.Usd.TimeCode | float | pxr.Sdf.TimeCode = ...) -> bool:
        """
        Get the attribute value of the ConstraintTarget at C{time}.
        """
    def GetAttr(self) -> pxr.Usd.Attribute:
        """
        Explicit UsdAttribute extractor.
        """
    @staticmethod
    def GetConstraintAttrName(_constraintName: str | pxr.Ar.ResolvedPath, /) -> str:
        """
        Returns the fully namespaced constraint attribute name, given the
        constraint name.
        """
    def GetIdentifier(self) -> str:
        """
        Get the stored identifier unique to the enclosing model's namespace
        for this constraint target.



        SetIdentifier()
        """
    def IsDefined(self) -> bool:
        """
        Return true if the wrapped UsdAttribute::IsDefined() , and in addition
        the attribute is identified as a ConstraintTarget.
        """
    @classmethod
    def IsValid(cls, _attr: pxr.Usd.Attribute | ConstraintTarget | Primvar | XformOp | pxr.UsdShade.Input | pxr.UsdShade.Output, /) -> bool:
        """
        Test whether a given UsdAttribute represents valid ConstraintTarget,
        which implies that creating a UsdGeomConstraintTarget from the
        attribute will succeed.


        Success implies that C{attr.IsDefined()} is true.
        """
    def Set(self, value: pxr.Gf.Matrix4d, time: pxr.Usd.TimeCode | float | pxr.Sdf.TimeCode = ...) -> bool:
        """
        Set the attribute value of the ConstraintTarget at C{time}.
        """
    def SetIdentifier(self, identifier: str | pxr.Ar.ResolvedPath) -> None:
        """
        Explicitly sets the stored identifier to the given string.


        Clients are responsible for ensuring the uniqueness of this identifier
        within the enclosing model's namespace.
        """
    def __bool__(self) -> bool:
        """
        Explicit bool conversion operator.


        A ConstraintTarget object converts to C{true} iff it is valid for
        querying and authoring values and metadata (which is identically
        equivalent to IsDefined() ). It converts to C{false} otherwise.
        """

class Cube(Gprim):
    """
    Defines a primitive rectilinear cube centered at the origin.


    The fallback values for Cube, Sphere, Cone, and Cylinder are set so
    that they all pack into the same volume/bounds.
    """
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None:
        """
        Construct a UsdGeomCube on UsdPrim C{prim}.


        Equivalent to UsdGeomCube::Get (prim.GetStage(), prim.GetPath()) for a
        *valid* C{prim}, but will not immediately throw an error for an
        invalid C{prim}
        """
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None:
        """
        Construct a UsdGeomCube on the prim held by C{schemaObj}.


        Should be preferred over UsdGeomCube (schemaObj.GetPrim()), as it
        preserves SchemaBase state.
        """
    def CreateExtentAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetExtentAttr() , and also Create vs Get Property Methods for when
        to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateSizeAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetSizeAttr() , and also Create vs Get Property Methods for when
        to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    @staticmethod
    def Define(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> Cube:
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
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> Cube:
        """
        Return a UsdGeomCube holding the prim adhering to this schema at
        C{path} on C{stage}.


        If no prim exists at C{path} on C{stage}, or if the prim at that path
        does not adhere to this schema, return an invalid schema object. This
        is shorthand for the following: ::

          UsdGeomCube(stage->GetPrimAtPath(path));

        """
    def GetExtentAttr(self) -> pxr.Usd.Attribute:
        """
        Extent is re-defined on Cube only to provide a fallback value.



        UsdGeomGprim::GetExtentAttr() .

        Declaration

        C{float3[] extent = [(-1, -1, -1), (1, 1, 1)]}

        C++ Type

        VtArray<GfVec3f>

        Usd Type

        SdfValueTypeNames->Float3Array
        """
    @staticmethod
    def GetSchemaAttributeNames(includeInherited: bool = ...) -> list[str]:
        """
        Return a vector of names of all pre-declared attributes for this
        schema class and all its ancestor classes.


        Does not include attributes that may be authored by custom/extended
        methods of the schemas involved.
        """
    def GetSizeAttr(self) -> pxr.Usd.Attribute:
        """
        Indicates the length of each edge of the cube.


        If you author *size* you must also author *extent*.

        GetExtentAttr()

        Declaration

        C{double size = 2}

        C++ Type

        double

        Usd Type

        SdfValueTypeNames->Double
        """
    @staticmethod
    def _GetStaticTfType() -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...

class Curves(PointBased):
    """
    Base class for UsdGeomBasisCurves, UsdGeomNurbsCurves, and
    UsdGeomHermiteCurves.


    The BasisCurves schema is designed to be analagous to offline
    renderers'notion of batched curves (such as the classical RIB
    definition via Basis and Curves statements), while the NurbsCurve
    schema is designed to be analgous to the NURBS curves found in
    packages like Maya and Houdini while retaining their consistency with
    the RenderMan specification for NURBS Patches. HermiteCurves are
    useful for the interchange of animation guides and paths.

    It is safe to use the length of the curve vertex count to derive the
    number of curves and the number and layout of curve vertices, but this
    schema should NOT be used to derive the number of curve points. While
    vertex indices are implicit in all shipped descendent types of this
    schema, one should not assume that all internal or future shipped
    schemas will follow this pattern. Be sure to key any indexing behavior
    off the concrete type, not this abstract type.
    """
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None:
        """
        Construct a UsdGeomCurves on UsdPrim C{prim}.


        Equivalent to UsdGeomCurves::Get (prim.GetStage(), prim.GetPath()) for
        a *valid* C{prim}, but will not immediately throw an error for an
        invalid C{prim}
        """
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None:
        """
        Construct a UsdGeomCurves on the prim held by C{schemaObj}.


        Should be preferred over UsdGeomCurves (schemaObj.GetPrim()), as it
        preserves SchemaBase state.
        """
    @staticmethod
    def ComputeExtent(points: pxr.Vt.Vec3fArray | typing.Iterable[list[float]] | typing.Iterable[pxr.Gf.Vec3f] | typing.Iterable[tuple[float, float, float]], widths: pxr.Vt.FloatArray | typing.Iterable[float]) -> pxr.Vt.Vec3fArray:
        """
        Compute the extent for the curves defined by points and widths.



        true upon success, false if unable to calculate extent. On success,
        extent will contain an approximate axis-aligned bounding box of the
        curve defined by points with the given widths.

        This function is to provide easy authoring of extent for usd authoring
        tools, hence it is static and acts outside a specific prim (as in
        attribute based methods).
        """
    def CreateCurveVertexCountsAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetCurveVertexCountsAttr() , and also Create vs Get Property
        Methods for when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateWidthsAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetWidthsAttr() , and also Create vs Get Property Methods for when
        to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    @staticmethod
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> Curves:
        """
        Return a UsdGeomCurves holding the prim adhering to this schema at
        C{path} on C{stage}.


        If no prim exists at C{path} on C{stage}, or if the prim at that path
        does not adhere to this schema, return an invalid schema object. This
        is shorthand for the following: ::

          UsdGeomCurves(stage->GetPrimAtPath(path));

        """
    def GetCurveCount(self, timeCode: pxr.Usd.TimeCode | float | pxr.Sdf.TimeCode = ...) -> int:
        """
        Returns the number of curves as defined by the size of the
        *curveVertexCounts* array at *timeCode*.



        For most code, this check will be performant. When using file formats
        where the cost of attribute reading is high and the time sampled array
        will be read into memory later, it may be better to explicitly read
        the value once and check the size of the array directly.

        GetCurveVertexCountsAttr()
        """
    def GetCurveVertexCountsAttr(self) -> pxr.Usd.Attribute:
        """
        Curves-derived primitives can represent multiple distinct, potentially
        disconnected curves.


        The length of'curveVertexCounts'gives the number of such curves, and
        each element describes the number of vertices in the corresponding
        curve

        Declaration

        C{int[] curveVertexCounts}

        C++ Type

        VtArray<int>

        Usd Type

        SdfValueTypeNames->IntArray
        """
    @staticmethod
    def GetSchemaAttributeNames(includeInherited: bool = ...) -> list[str]:
        """
        Return a vector of names of all pre-declared attributes for this
        schema class and all its ancestor classes.


        Does not include attributes that may be authored by custom/extended
        methods of the schemas involved.
        """
    def GetWidthsAttr(self) -> pxr.Usd.Attribute:
        '''
        Provides width specification for the curves, whose application will
        depend on whether the curve is oriented (normals are defined for it),
        in which case widths are"ribbon width", or unoriented, in which case
        widths are cylinder width.


        \'widths\'is not a generic Primvar, but the number of elements in this
        attribute will be determined by its\'interpolation\'. See
        SetWidthsInterpolation() . If\'widths\'and\'primvars:widths\'are both
        specified, the latter has precedence.

        Declaration

        C{float[] widths}

        C++ Type

        VtArray<float>

        Usd Type

        SdfValueTypeNames->FloatArray
        '''
    def GetWidthsInterpolation(self) -> str:
        """
        Get the interpolation for the *widths* attribute.


        Although'widths'is not classified as a generic UsdGeomPrimvar (and
        will not be included in the results of
        UsdGeomPrimvarsAPI::GetPrimvars() ) it does require an interpolation
        specification. The fallback interpolation, if left unspecified, is
        UsdGeomTokens->vertex, which means a width value is specified at the
        end of each curve segment.
        """
    def SetWidthsInterpolation(self, interpolation: str | pxr.Ar.ResolvedPath) -> bool:
        """
        Set the interpolation for the *widths* attribute.



        true upon success, false if C{interpolation} is not a legal value as
        defined by UsdPrimvar::IsValidInterpolation(), or if there was a
        problem setting the value. No attempt is made to validate that the
        widths attr's value contains the right number of elements to match its
        interpolation to its prim's topology.

        GetWidthsInterpolation()
        """
    @staticmethod
    def _GetStaticTfType() -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...

class Cylinder(Gprim):
    '''
    Defines a primitive cylinder with closed ends, centered at the origin,
    whose spine is along the specified *axis*.


    The fallback values for Cube, Sphere, Cone, and Cylinder are set so
    that they all pack into the same volume/bounds.

    For any described attribute *Fallback* *Value* or *Allowed* *Values*
    below that are text/tokens, the actual token is published and defined
    in UsdGeomTokens. So to set an attribute to the value"rightHanded",
    use UsdGeomTokens->rightHanded as the value.
    '''
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None:
        """
        Construct a UsdGeomCylinder on UsdPrim C{prim}.


        Equivalent to UsdGeomCylinder::Get (prim.GetStage(), prim.GetPath())
        for a *valid* C{prim}, but will not immediately throw an error for an
        invalid C{prim}
        """
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None:
        """
        Construct a UsdGeomCylinder on the prim held by C{schemaObj}.


        Should be preferred over UsdGeomCylinder (schemaObj.GetPrim()), as it
        preserves SchemaBase state.
        """
    def CreateAxisAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetAxisAttr() , and also Create vs Get Property Methods for when
        to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateExtentAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetExtentAttr() , and also Create vs Get Property Methods for when
        to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateHeightAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetHeightAttr() , and also Create vs Get Property Methods for when
        to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateRadiusAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetRadiusAttr() , and also Create vs Get Property Methods for when
        to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    @staticmethod
    def Define(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> Cylinder:
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
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> Cylinder:
        """
        Return a UsdGeomCylinder holding the prim adhering to this schema at
        C{path} on C{stage}.


        If no prim exists at C{path} on C{stage}, or if the prim at that path
        does not adhere to this schema, return an invalid schema object. This
        is shorthand for the following: ::

          UsdGeomCylinder(stage->GetPrimAtPath(path));

        """
    def GetAxisAttr(self) -> pxr.Usd.Attribute:
        '''
        The axis along which the spine of the cylinder is aligned.



        Declaration

        C{uniform token axis ="Z"}

        C++ Type

        TfToken

        Usd Type

        SdfValueTypeNames->Token

        Variability

        SdfVariabilityUniform

        Allowed Values

        X, Y, Z
        '''
    def GetExtentAttr(self) -> pxr.Usd.Attribute:
        """
        Extent is re-defined on Cylinder only to provide a fallback value.



        UsdGeomGprim::GetExtentAttr() .

        Declaration

        C{float3[] extent = [(-1, -1, -1), (1, 1, 1)]}

        C++ Type

        VtArray<GfVec3f>

        Usd Type

        SdfValueTypeNames->Float3Array
        """
    def GetHeightAttr(self) -> pxr.Usd.Attribute:
        """
        The size of the cylinder's spine along the specified *axis*.


        If you author *height* you must also author *extent*.

        GetExtentAttr()

        Declaration

        C{double height = 2}

        C++ Type

        double

        Usd Type

        SdfValueTypeNames->Double
        """
    def GetRadiusAttr(self) -> pxr.Usd.Attribute:
        """
        The radius of the cylinder.


        If you author *radius* you must also author *extent*.

        GetExtentAttr()

        Declaration

        C{double radius = 1}

        C++ Type

        double

        Usd Type

        SdfValueTypeNames->Double
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

class Cylinder_1(Gprim):
    '''
    Defines a primitive cylinder with closed ends, centered at the origin,
    whose spine is along the specified *axis*, with a pair of radii
    describing the size of the end points.


    The fallback values for Cube, Sphere, Cone, and Cylinder are set so
    that they all pack into the same volume/bounds.

    For any described attribute *Fallback* *Value* or *Allowed* *Values*
    below that are text/tokens, the actual token is published and defined
    in UsdGeomTokens. So to set an attribute to the value"rightHanded",
    use UsdGeomTokens->rightHanded as the value.
    '''
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None:
        """
        Construct a UsdGeomCylinder_1 on UsdPrim C{prim}.


        Equivalent to UsdGeomCylinder_1::Get (prim.GetStage(), prim.GetPath())
        for a *valid* C{prim}, but will not immediately throw an error for an
        invalid C{prim}
        """
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None:
        """
        Construct a UsdGeomCylinder_1 on the prim held by C{schemaObj}.


        Should be preferred over UsdGeomCylinder_1 (schemaObj.GetPrim()), as
        it preserves SchemaBase state.
        """
    def CreateAxisAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetAxisAttr() , and also Create vs Get Property Methods for when
        to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateExtentAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetExtentAttr() , and also Create vs Get Property Methods for when
        to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateHeightAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetHeightAttr() , and also Create vs Get Property Methods for when
        to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateRadiusBottomAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetRadiusBottomAttr() , and also Create vs Get Property Methods
        for when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateRadiusTopAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetRadiusTopAttr() , and also Create vs Get Property Methods for
        when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    @staticmethod
    def Define(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> Cylinder_1:
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
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> Cylinder_1:
        """
        Return a UsdGeomCylinder_1 holding the prim adhering to this schema at
        C{path} on C{stage}.


        If no prim exists at C{path} on C{stage}, or if the prim at that path
        does not adhere to this schema, return an invalid schema object. This
        is shorthand for the following: ::

          UsdGeomCylinder_1(stage->GetPrimAtPath(path));

        """
    def GetAxisAttr(self) -> pxr.Usd.Attribute:
        '''
        The axis along which the spine of the cylinder is aligned.



        Declaration

        C{uniform token axis ="Z"}

        C++ Type

        TfToken

        Usd Type

        SdfValueTypeNames->Token

        Variability

        SdfVariabilityUniform

        Allowed Values

        X, Y, Z
        '''
    def GetExtentAttr(self) -> pxr.Usd.Attribute:
        """
        Extent is re-defined on Cylinder only to provide a fallback value.



        UsdGeomGprim::GetExtentAttr() .

        Declaration

        C{float3[] extent = [(-1, -1, -1), (1, 1, 1)]}

        C++ Type

        VtArray<GfVec3f>

        Usd Type

        SdfValueTypeNames->Float3Array
        """
    def GetHeightAttr(self) -> pxr.Usd.Attribute:
        """
        The length of the cylinder's spine along the specified *axis*.


        If you author *height* you must also author *extent*.

        GetExtentAttr()

        Declaration

        C{double height = 2}

        C++ Type

        double

        Usd Type

        SdfValueTypeNames->Double
        """
    def GetRadiusBottomAttr(self) -> pxr.Usd.Attribute:
        """
        The radius of the bottom of the cylinder - i.e.


        the face point located along the negative *axis*. If you author
        *radiusBottom* you must also author *extent*.

        GetExtentAttr()

        Declaration

        C{double radiusBottom = 1}

        C++ Type

        double

        Usd Type

        SdfValueTypeNames->Double
        """
    def GetRadiusTopAttr(self) -> pxr.Usd.Attribute:
        """
        The radius of the top of the cylinder - i.e.


        the face located along the positive *axis*. If you author *radiusTop*
        you must also author *extent*.

        GetExtentAttr()

        Declaration

        C{double radiusTop = 1}

        C++ Type

        double

        Usd Type

        SdfValueTypeNames->Double
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

class Gprim(Boundable):
    '''
    Base class for all geometric primitives.



    Gprim encodes basic graphical properties such as *doubleSided* and
    *orientation*, and provides primvars for"display
    color"and"displayopacity"that travel with geometry to be used as
    shader overrides.

    For any described attribute *Fallback* *Value* or *Allowed* *Values*
    below that are text/tokens, the actual token is published and defined
    in UsdGeomTokens. So to set an attribute to the value"rightHanded",
    use UsdGeomTokens->rightHanded as the value.
    '''
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None:
        """
        Construct a UsdGeomGprim on UsdPrim C{prim}.


        Equivalent to UsdGeomGprim::Get (prim.GetStage(), prim.GetPath()) for
        a *valid* C{prim}, but will not immediately throw an error for an
        invalid C{prim}
        """
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None:
        """
        Construct a UsdGeomGprim on the prim held by C{schemaObj}.


        Should be preferred over UsdGeomGprim (schemaObj.GetPrim()), as it
        preserves SchemaBase state.
        """
    def CreateDisplayColorAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetDisplayColorAttr() , and also Create vs Get Property Methods
        for when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateDisplayColorPrimvar(self, interpolation: str | pxr.Ar.ResolvedPath = ..., elementSize: int = ...) -> Primvar:
        """
        Convenience function to create the displayColor primvar, optionally
        specifying interpolation and elementSize.



        CreateDisplayColorAttr() , GetDisplayColorPrimvar()
        """
    def CreateDisplayOpacityAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetDisplayOpacityAttr() , and also Create vs Get Property Methods
        for when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateDisplayOpacityPrimvar(self, interpolation: str | pxr.Ar.ResolvedPath = ..., elementSize: int = ...) -> Primvar:
        """
        Convenience function to create the displayOpacity primvar, optionally
        specifying interpolation and elementSize.



        CreateDisplayOpacityAttr() , GetDisplayOpacityPrimvar()
        """
    def CreateDoubleSidedAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetDoubleSidedAttr() , and also Create vs Get Property Methods for
        when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateOrientationAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetOrientationAttr() , and also Create vs Get Property Methods for
        when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    @staticmethod
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> Gprim:
        """
        Return a UsdGeomGprim holding the prim adhering to this schema at
        C{path} on C{stage}.


        If no prim exists at C{path} on C{stage}, or if the prim at that path
        does not adhere to this schema, return an invalid schema object. This
        is shorthand for the following: ::

          UsdGeomGprim(stage->GetPrimAtPath(path));

        """
    def GetDisplayColorAttr(self) -> pxr.Usd.Attribute:
        '''
        It is useful to have an"official"colorSet that can be used as a
        display or modeling color, even in the absence of any specified shader
        for a gprim.


        DisplayColor serves this role; because it is a UsdGeomPrimvar, it can
        also be used as a gprim override for any shader that consumes a
        *displayColor* parameter.

        Declaration

        C{color3f[] primvars:displayColor}

        C++ Type

        VtArray<GfVec3f>

        Usd Type

        SdfValueTypeNames->Color3fArray
        '''
    def GetDisplayColorPrimvar(self) -> Primvar:
        """
        Convenience function to get the displayColor Attribute as a Primvar.



        GetDisplayColorAttr() , CreateDisplayColorPrimvar()
        """
    def GetDisplayOpacityAttr(self) -> pxr.Usd.Attribute:
        """
        Companion to *displayColor* that specifies opacity, broken out as an
        independent attribute rather than an rgba color, both so that each can
        be independently overridden, and because shaders rarely consume rgba
        parameters.



        Declaration

        C{float[] primvars:displayOpacity}

        C++ Type

        VtArray<float>

        Usd Type

        SdfValueTypeNames->FloatArray
        """
    def GetDisplayOpacityPrimvar(self) -> Primvar:
        """
        Convenience function to get the displayOpacity Attribute as a Primvar.



        GetDisplayOpacityAttr() , CreateDisplayOpacityPrimvar()
        """
    def GetDoubleSidedAttr(self) -> pxr.Usd.Attribute:
        '''
        Although some renderers treat all parametric or polygonal surfaces as
        if they were effectively laminae with outward-facing normals on both
        sides, some renderers derive significant optimizations by considering
        these surfaces to have only a single outward side, typically
        determined by control-point winding order and/or *orientation*.


        By doing so they can perform"backface culling"to avoid drawing the
        many polygons of most closed surfaces that face away from the viewer.

        However, it is often advantageous to model thin objects such as paper
        and cloth as single, open surfaces that must be viewable from both
        sides, always. Setting a gprim\'s *doubleSided* attribute to C{true}
        instructs all renderers to disable optimizations such as backface
        culling for the gprim, and attempt (not all renderers are able to do
        so, but the USD reference GL renderer always will) to provide forward-
        facing normals on each side of the surface for lighting calculations.

        Declaration

        C{uniform bool doubleSided = 0}

        C++ Type

        bool

        Usd Type

        SdfValueTypeNames->Bool

        Variability

        SdfVariabilityUniform
        '''
    def GetOrientationAttr(self) -> pxr.Usd.Attribute:
        '''
        Orientation specifies whether the gprim\'s surface normal should be
        computed using the right hand rule, or the left hand rule.


        Please see Coordinate System, Winding Order, Orientation, and Surface
        Normals for a deeper explanation and generalization of orientation to
        composed scenes with transformation hierarchies.

        Declaration

        C{uniform token orientation ="rightHanded"}

        C++ Type

        TfToken

        Usd Type

        SdfValueTypeNames->Token

        Variability

        SdfVariabilityUniform

        Allowed Values

        rightHanded, leftHanded
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

class HermiteCurves(Curves):
    """
    This schema specifies a cubic hermite interpolated curve batch as
    sometimes used for defining guides for animation.


    While hermite curves can be useful because they interpolate through
    their control points, they are not well supported by high-end
    renderers for imaging. Therefore, while we include this schema for
    interchange, we strongly recommend the use of UsdGeomBasisCurves as
    the representation of curves intended to be rendered (ie. hair or
    grass). Hermite curves can be converted to a Bezier representation
    (though not from Bezier back to Hermite in general).

    Point Interpolation
    ===================

    The initial cubic curve segment is defined by the first two points and
    first two tangents. Additional segments are defined by additional
    point / tangent pairs. The number of segments for each non-batched
    hermite curve would be len(curve.points) - 1. The total number of
    segments for the batched UsdGeomHermiteCurves representation is
    len(points) - len(curveVertexCounts).

    Primvar, Width, and Normal Interpolation
    ========================================

    Primvar interpolation is not well specified for this type as it is not
    intended as a rendering representation. We suggest that per point
    primvars would be linearly interpolated across each segment and should
    be tagged as'varying'.

    It is not immediately clear how to specify cubic
    or'vertex'interpolation for this type, as we lack a specification for
    primvar tangents. This also means that width and normal interpolation
    should be restricted to varying (linear), uniform (per curve element),
    or constant (per prim).
    """

    class PointAndTangentArrays(Boost.Python.instance):
        """
        Represents points and tangents of the same size.


        Utility to interleave point and tangent data. This class is immutable.
        """
        __instance_size__: ClassVar[int] = ...
        @overload
        def __init__(self) -> None:
            """
            Construct empty points and tangents arrays.
            """
        @overload
        def __init__(self, _points: pxr.Vt.Vec3fArray | typing.Iterable[list[float]] | typing.Iterable[pxr.Gf.Vec3f] | typing.Iterable[tuple[float, float, float]], _tangents: pxr.Vt.Vec3fArray | typing.Iterable[list[float]] | typing.Iterable[pxr.Gf.Vec3f] | typing.Iterable[tuple[float, float, float]], /) -> None:
            """
            Initializes C{points} and C{tangents} if they are the same size.


            If points and tangents are not the same size, an empty container is
            created.
            """
        def GetPoints(self) -> pxr.Vt.Vec3fArray:
            """
            Get separated points array.
            """
        def GetTangents(self) -> pxr.Vt.Vec3fArray:
            """
            Get separated tangents array.
            """
        def Interleave(self) -> pxr.Vt.Vec3fArray:
            """
            Interleaves points (P0, ..., Pn) and tangents (T0, ..., Tn) into one
            array (P0, T0, ..., Pn, Tn).
            """
        def IsEmpty(self) -> bool:
            """
            Returns true if the containers are empty.
            """
        @staticmethod
        def Separate(_interleaved: pxr.Vt.Vec3fArray | typing.Iterable[list[float]] | typing.Iterable[pxr.Gf.Vec3f] | typing.Iterable[tuple[float, float, float]], /) -> HermiteCurves.PointAndTangentArrays:
            """
            Given an C{interleaved} points and tangents arrays (P0, T0, ..., Pn,
            Tn), separates them into two arrays (P0, ..., PN) and (T0, ..., Tn).
            """
        def __bool__(self) -> bool:
            """
            Returns true if there are values.
            """
        def __eq__(self, other: object) -> bool: ...
        def __ne__(self, other: object) -> bool: ...
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None:
        """
        Construct a UsdGeomHermiteCurves on UsdPrim C{prim}.


        Equivalent to UsdGeomHermiteCurves::Get (prim.GetStage(),
        prim.GetPath()) for a *valid* C{prim}, but will not immediately throw
        an error for an invalid C{prim}
        """
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None:
        """
        Construct a UsdGeomHermiteCurves on the prim held by C{schemaObj}.


        Should be preferred over UsdGeomHermiteCurves (schemaObj.GetPrim()),
        as it preserves SchemaBase state.
        """
    def CreateTangentsAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetTangentsAttr() , and also Create vs Get Property Methods for
        when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    @staticmethod
    def Define(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> HermiteCurves:
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
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> HermiteCurves:
        """
        Return a UsdGeomHermiteCurves holding the prim adhering to this schema
        at C{path} on C{stage}.


        If no prim exists at C{path} on C{stage}, or if the prim at that path
        does not adhere to this schema, return an invalid schema object. This
        is shorthand for the following: ::

          UsdGeomHermiteCurves(stage->GetPrimAtPath(path));

        """
    @staticmethod
    def GetSchemaAttributeNames(includeInherited: bool = ...) -> list[str]:
        """
        Return a vector of names of all pre-declared attributes for this
        schema class and all its ancestor classes.


        Does not include attributes that may be authored by custom/extended
        methods of the schemas involved.
        """
    def GetTangentsAttr(self) -> pxr.Usd.Attribute:
        """
        Defines the outgoing trajectory tangent for each point.


        Tangents should be the same size as the points attribute.

        Declaration

        C{vector3f[] tangents = []}

        C++ Type

        VtArray<GfVec3f>

        Usd Type

        SdfValueTypeNames->Vector3fArray
        """
    @staticmethod
    def _GetStaticTfType() -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...

class Imageable(pxr.Usd.Typed):
    '''
    Base class for all prims that may require rendering or visualization
    of some sort.


    The primary attributes of Imageable are *visibility* and *purpose*,
    which each provide instructions for what geometry should be included
    for processing by rendering and other computations.

    Deprecated

    Imageable also provides API for accessing primvars, which has been
    moved to the UsdGeomPrimvarsAPI schema, because primvars can now be
    applied on non-Imageable prim types. This API is planned to be
    removed, UsdGeomPrimvarsAPI should be used directly instead.

    For any described attribute *Fallback* *Value* or *Allowed* *Values*
    below that are text/tokens, the actual token is published and defined
    in UsdGeomTokens. So to set an attribute to the value"rightHanded",
    use UsdGeomTokens->rightHanded as the value.
    '''

    class PurposeInfo(Boost.Python.instance):
        """
        Value type containing information about a prim's computed effective
        purpose as well as storing whether the prim's purpose value can be
        inherited by namespace children if necessary.


        This provides the purpose information necessary for efficiently
        computing and caching the purposes of a hierarchy of prims.

        GetPurposeAttr() , Imageable Purpose
        """
        __instance_size__: ClassVar[int] = ...
        isInheritable: Incomplete
        purpose: Incomplete
        @overload
        def __init__(self) -> None: ...
        @overload
        def __init__(self, _purpose_: str | pxr.Ar.ResolvedPath, _isInheritable_: bool, /) -> None: ...
        def GetInheritablePurpose(self) -> str:
            """
            Returns the purpose if it's inheritable, returns empty if it is not.
            """
        def __bool__(self) -> bool:
            """
            Returns true if this represents a purpose that has been computed.
            """
        def __eq__(self, other: object) -> bool: ...
        def __ne__(self, other: object) -> bool: ...
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None:
        """
        Construct a UsdGeomImageable on UsdPrim C{prim}.


        Equivalent to UsdGeomImageable::Get (prim.GetStage(), prim.GetPath())
        for a *valid* C{prim}, but will not immediately throw an error for an
        invalid C{prim}
        """
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None:
        """
        Construct a UsdGeomImageable on the prim held by C{schemaObj}.


        Should be preferred over UsdGeomImageable (schemaObj.GetPrim()), as it
        preserves SchemaBase state.
        """
    def ComputeEffectiveVisibility(self, purpose: str | pxr.Ar.ResolvedPath = ..., time: pxr.Usd.TimeCode | float | pxr.Sdf.TimeCode = ...) -> str:
        '''
        Calculate the effective purpose visibility of this prim for the given
        C{purpose}, taking into account opinions for the corresponding purpose
        attribute, along with overall visibility opinions.


        If ComputeVisibility() returns"invisible", then
        ComputeEffectiveVisibility() is"invisible"for all purpose values.
        Otherwise, ComputeEffectiveVisibility() returns the value of the
        nearest ancestral authored opinion for the corresponding purpose
        visibility attribute, as retured by GetPurposeVisibilityAttr(purpose).

        Note that the value returned here can be"invisible"(indicating the
        prim is invisible for the given purpose),"visible"(indicating that
        it\'s visible), or"inherited"(indicating that the purpose visibility is
        context-dependent and the fallback behavior must be determined by the
        caller.

        This function should be considered a reference implementation for
        correctness. B{If called on each prim in the context of a traversal we
        will perform massive overcomputation, because sibling prims share sub-
        problems in the query that can be efficiently cached, but are not
        (cannot be) by this simple implementation.} If you have control of
        your traversal, it will be far more efficient to manage visibility on
        a stack as you traverse.

        UsdGeomVisibilityAPI

        GetPurposeVisibilityAttr()

        ComputeVisibility()
        '''
    def ComputeLocalBound(self, time: pxr.Usd.TimeCode | float | pxr.Sdf.TimeCode, purpose1: str | pxr.Ar.ResolvedPath = ..., purpose2: str | pxr.Ar.ResolvedPath = ..., purpose3: str | pxr.Ar.ResolvedPath = ..., purpose4: str | pxr.Ar.ResolvedPath = ...) -> pxr.Gf.BBox3d:
        """
        Compute the bound of this prim in local space, at the specified
        C{time}, and for the specified purposes.


        The bound of the prim is computed, including the transform (if any)
        authored on the node itself.

        It is an error to not specify any purposes, which will result in the
        return of an empty box.

        B{If you need to compute bounds for multiple prims on a stage, it will
        be much, much more efficient to instantiate a UsdGeomBBoxCache and
        query it directly; doing so will reuse sub-computations shared by the
        prims.}
        """
    def ComputeLocalToWorldTransform(self, time: pxr.Usd.TimeCode | float | pxr.Sdf.TimeCode) -> pxr.Gf.Matrix4d:
        """
        Compute the transformation matrix for this prim at the given time,
        including the transform authored on the Prim itself, if present.


        B{If you need to compute the transform for multiple prims on a stage,
        it will be much, much more efficient to instantiate a
        UsdGeomXformCache and query it directly; doing so will reuse sub-
        computations shared by the prims.}
        """
    def ComputeParentToWorldTransform(self, time: pxr.Usd.TimeCode | float | pxr.Sdf.TimeCode) -> pxr.Gf.Matrix4d:
        """
        Compute the transformation matrix for this prim at the given time,
        *NOT* including the transform authored on the prim itself.


        B{If you need to compute the transform for multiple prims on a stage,
        it will be much, much more efficient to instantiate a
        UsdGeomXformCache and query it directly; doing so will reuse sub-
        computations shared by the prims.}
        """
    def ComputeProxyPrim(self) -> tuple[pxr.Usd.Prim, pxr.Usd.Prim]:
        """
        Find the prim whose purpose is *proxy* that serves as the proxy for
        this prim, as established by the GetProxyPrimRel() , or an invalid
        UsdPrim if this prim has no proxy.


        This method will find the proxy for *any* prim whose computed purpose
        (see ComputePurpose() ) is *render*. If provided and a proxy was
        found, we will set *renderPrim to the root of the *render* subtree
        upon which the renderProxy relationship was authored.

        If the renderProxy relationship has more than one target, we will
        issue a warning and return an invalid UsdPrim. If the targeted prim
        does not have a resolved purpose of *proxy*, we will warn and return
        an invalid prim.

        This function should be considered a reference implementation for
        correctness. B{If called on each prim in the context of a traversal we
        will perform massive overcomputation, because sibling prims share sub-
        problems in the query that can be efficiently cached, but are not
        (cannot be) by this simple implementation.} If you have control of
        your traversal, it will be far more efficient to compute proxy-prims
        on a stack as you traverse.

        Currently the returned prim will not contain any instancing context if
        it is inside a prototype - its path will be relative to the
        prototype's root. Once UsdPrim is instancing-aware in the core, we can
        change this method to return a context-aware result.

        SetProxyPrim() , GetProxyPrimRel()
        """
    def ComputePurpose(self) -> str:
        """
        Calculate the effective purpose information about this prim.


        This is equivalent to extracting the purpose from the value returned
        by ComputePurposeInfo() .

        This function should be considered a reference implementation for
        correctness. B{If called on each prim in the context of a traversal we
        will perform massive overcomputation, because sibling prims share sub-
        problems in the query that can be efficiently cached, but are not
        (cannot be) by this simple implementation.} If you have control of
        your traversal, it will be far more efficient to manage purpose, along
        with visibility, on a stack as you traverse.

        GetPurposeAttr() , Imageable Purpose
        """
    @overload
    def ComputePurposeInfo(self) -> Imageable.PurposeInfo:
        """
        Calculate the effective purpose information about this prim which
        includes final computed purpose value of the prim as well as whether
        the purpose value should be inherited by namespace children without
        their own purpose opinions.


        This function should be considered a reference implementation for
        correctness. B{If called on each prim in the context of a traversal we
        will perform massive overcomputation, because sibling prims share sub-
        problems in the query that can be efficiently cached, but are not
        (cannot be) by this simple implementation.} If you have control of
        your traversal, it will be far more efficient to manage purpose, along
        with visibility, on a stack as you traverse.

        GetPurposeAttr() , Imageable Purpose
        """
    @overload
    def ComputePurposeInfo(self, parentPurposeInfo: Imageable.PurposeInfo) -> Imageable.PurposeInfo:
        """
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        Calculates the effective purpose information about this prim, given
        the computed purpose information of its parent prim.


        This can be much more efficient than using CommputePurposeInfo() when
        PurposeInfo values are properly computed and cached for a hierarchy of
        prims using this function.

        GetPurposeAttr() , Imageable Purpose
        """
    def ComputeUntransformedBound(self, time: pxr.Usd.TimeCode | float | pxr.Sdf.TimeCode, purpose1: str | pxr.Ar.ResolvedPath = ..., purpose2: str | pxr.Ar.ResolvedPath = ..., purpose3: str | pxr.Ar.ResolvedPath = ..., purpose4: str | pxr.Ar.ResolvedPath = ...) -> pxr.Gf.BBox3d:
        """
        Compute the untransformed bound of this prim, at the specified
        C{time}, and for the specified purposes.


        The bound of the prim is computed in its object space, ignoring any
        transforms authored on or above the prim.

        It is an error to not specify any purposes, which will result in the
        return of an empty box.

        B{If you need to compute bounds for multiple prims on a stage, it will
        be much, much more efficient to instantiate a UsdGeomBBoxCache and
        query it directly; doing so will reuse sub-computations shared by the
        prims.}
        """
    def ComputeVisibility(self, time: pxr.Usd.TimeCode | float | pxr.Sdf.TimeCode = ...) -> str:
        '''
        Calculate the effective visibility of this prim, as defined by its
        most ancestral authored"invisible"opinion, if any.


        A prim is considered visible at the current C{time} if none of its
        Imageable ancestors express an authored"invisible"opinion, which is
        what leads to the"simple pruning"behavior described in
        GetVisibilityAttr() .

        This function should be considered a reference implementation for
        correctness. B{If called on each prim in the context of a traversal we
        will perform massive overcomputation, because sibling prims share sub-
        problems in the query that can be efficiently cached, but are not
        (cannot be) by this simple implementation.} If you have control of
        your traversal, it will be far more efficient to manage visibility on
        a stack as you traverse.

        GetVisibilityAttr()
        '''
    def ComputeWorldBound(self, time: pxr.Usd.TimeCode | float | pxr.Sdf.TimeCode, purpose1: str | pxr.Ar.ResolvedPath = ..., purpose2: str | pxr.Ar.ResolvedPath = ..., purpose3: str | pxr.Ar.ResolvedPath = ..., purpose4: str | pxr.Ar.ResolvedPath = ...) -> pxr.Gf.BBox3d:
        """
        Compute the bound of this prim in world space, at the specified
        C{time}, and for the specified purposes.


        The bound of the prim is computed, including the transform (if any)
        authored on the node itself, and then transformed to world space.

        It is an error to not specify any purposes, which will result in the
        return of an empty box.

        B{If you need to compute bounds for multiple prims on a stage, it will
        be much, much more efficient to instantiate a UsdGeomBBoxCache and
        query it directly; doing so will reuse sub-computations shared by the
        prims.}
        """
    def CreateProxyPrimRel(self) -> pxr.Usd.Relationship:
        """
        See GetProxyPrimRel() , and also Create vs Get Property Methods for
        when to use Get vs Create.
        """
    def CreatePurposeAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetPurposeAttr() , and also Create vs Get Property Methods for
        when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateVisibilityAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetVisibilityAttr() , and also Create vs Get Property Methods for
        when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    @staticmethod
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> Imageable:
        """
        Return a UsdGeomImageable holding the prim adhering to this schema at
        C{path} on C{stage}.


        If no prim exists at C{path} on C{stage}, or if the prim at that path
        does not adhere to this schema, return an invalid schema object. This
        is shorthand for the following: ::

          UsdGeomImageable(stage->GetPrimAtPath(path));

        """
    @staticmethod
    def GetOrderedPurposeTokens() -> list[str]:
        """
        Returns an ordered list of allowed values of the purpose attribute.


        The ordering is important because it defines the protocol between
        UsdGeomModelAPI and UsdGeomBBoxCache for caching and retrieving
        extents hints by purpose.

        The order is: [default, render, proxy, guide]

        See

        UsdGeomModelAPI::GetExtentsHint() .

        GetOrderedPurposeTokens()
        """
    def GetProxyPrimRel(self) -> pxr.Usd.Relationship:
        '''
        The *proxyPrim* relationship allows us to link a prim whose *purpose*
        is"render"to its (single target) purpose="proxy"prim.


        This is entirely optional, but can be useful in several scenarios:

           - In a pipeline that does pruning (for complexity management) by
             deactivating prims composed from asset references, when we deactivate
             a purpose="render"prim, we will be able to discover and additionally
             deactivate its associated purpose="proxy"prim, so that preview renders
             reflect the pruning accurately.

           - DCC importers may be able to make more aggressive optimizations
             for interactive processing and display if they can discover the proxy
             for a given render prim.

           - With a little more work, a Hydra-based application will be able
             to map a picked proxy prim back to its render geometry for selection.

        It is only valid to author the proxyPrim relationship on prims whose
        purpose is"render".
        '''
    def GetPurposeAttr(self) -> pxr.Usd.Attribute:
        '''
        Purpose is a classification of geometry into categories that can each
        be independently included or excluded from traversals of prims on a
        stage, such as rendering or bounding-box computation traversals.


        See Imageable Purpose for more detail about how *purpose* is computed
        and used.

        Declaration

        C{uniform token purpose ="default"}

        C++ Type

        TfToken

        Usd Type

        SdfValueTypeNames->Token

        Variability

        SdfVariabilityUniform

        Allowed Values

        default, render, proxy, guide
        '''
    def GetPurposeVisibilityAttr(self, purpose: str | pxr.Ar.ResolvedPath = ...) -> pxr.Usd.Attribute:
        '''
        Return the attribute that is used for expressing visibility opinions
        for the given C{purpose}.


        For"default"purpose, return the overall *visibility* attribute.
        For"guide","proxy", or"render"purpose, return *guideVisibility*,
        *proxyVisibility*, or *renderVisibility* if UsdGeomVisibilityAPI is
        applied to the prim. If UsdGeomvVisibiltyAPI is not applied, an empty
        attribute is returned for purposes other than default.

        UsdGeomVisibilityAPI::Apply

        UsdGeomVisibilityAPI::GetPurposeVisibilityAttr
        '''
    @staticmethod
    def GetSchemaAttributeNames(includeInherited: bool = ...) -> list[str]:
        """
        Return a vector of names of all pre-declared attributes for this
        schema class and all its ancestor classes.


        Does not include attributes that may be authored by custom/extended
        methods of the schemas involved.
        """
    def GetVisibilityAttr(self) -> pxr.Usd.Attribute:
        '''
        Visibility is meant to be the simplest form of"pruning"visibility that
        is supported by most DCC apps.


        Visibility is animatable, allowing a sub-tree of geometry to be
        present for some segment of a shot, and absent from others; unlike the
        action of deactivating geometry prims, invisible geometry is still
        available for inspection, for positioning, for defining volumes, etc.

        Declaration

        C{token visibility ="inherited"}

        C++ Type

        TfToken

        Usd Type

        SdfValueTypeNames->Token

        Allowed Values

        inherited, invisible
        '''
    def MakeInvisible(self, time: pxr.Usd.TimeCode | float | pxr.Sdf.TimeCode = ...) -> None:
        """
        Makes the imageable invisible if it is visible at the given time.



        When visibility is animated, this only works when it is invoked
        sequentially at increasing time samples. If visibility is already
        authored and animated in the scene, calling MakeVisible() at an
        arbitrary (in-between) frame isn't guaranteed to work.

        Be sure to set the edit target to the layer containing the strongest
        visibility opinion or to a stronger layer.

        MakeVisible()

        ComputeVisibility()
        """
    def MakeVisible(self, time: pxr.Usd.TimeCode | float | pxr.Sdf.TimeCode = ...) -> None:
        """
        Make the imageable visible if it is invisible at the given time.


        Since visibility is pruning, this may need to override some ancestor's
        visibility and all-but-one of the ancestor's children's visibility,
        for all the ancestors of this prim up to the highest ancestor that is
        explicitly invisible, to preserve the visibility state.

        If MakeVisible() (or MakeInvisible() ) is going to be applied to all
        the prims on a stage, ancestors must be processed prior to descendants
        to get the correct behavior.

        When visibility is animated, this only works when it is invoked
        sequentially at increasing time samples. If visibility is already
        authored and animated in the scene, calling MakeVisible() at an
        arbitrary (in-between) frame isn't guaranteed to work.

        This will only work properly if all ancestor prims of the imageable
        are B{defined}, as the imageable schema is only valid on defined
        prims.

        Be sure to set the edit target to the layer containing the strongest
        visibility opinion or to a stronger layer.

        MakeInvisible()

        ComputeVisibility()
        """
    @overload
    def SetProxyPrim(self, proxy: pxr.Usd.Prim) -> bool:
        """
        Convenience function for authoring the *renderProxy* rel on this prim
        to target the given C{proxy} prim.


        To facilitate authoring on sparse or unloaded stages, we do not
        perform any validation of this prim's purpose or the type or purpose
        of the specified prim.

        ComputeProxyPrim() , GetProxyPrimRel()
        """
    @overload
    def SetProxyPrim(self, proxy: pxr.Usd.SchemaBase) -> bool: ...
    @staticmethod
    def _GetStaticTfType() -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...

class LinearUnits(Boost.Python.instance):
    """
    Container class for static double-precision symbols representing
    common units of measure expressed in meters.



    Encoding Stage Linear Units
    """
    centimeters: ClassVar[float] = ...  # read-only
    feet: ClassVar[float] = ...  # read-only
    inches: ClassVar[float] = ...  # read-only
    kilometers: ClassVar[float] = ...  # read-only
    lightYears: ClassVar[float] = ...  # read-only
    meters: ClassVar[float] = ...  # read-only
    micrometers: ClassVar[float] = ...  # read-only
    miles: ClassVar[float] = ...  # read-only
    millimeters: ClassVar[float] = ...  # read-only
    nanometers: ClassVar[float] = ...  # read-only
    yards: ClassVar[float] = ...  # read-only
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """

class Mesh(PointBased):
    '''
    Encodes a mesh with optional subdivision properties and features.


    As a point-based primitive, meshes are defined in terms of points that
    are connected into edges and faces. Many references to meshes use the
    term\'vertex\'in place of or interchangeably with\'points\', while some
    use\'vertex\'to refer to the\'face-vertices\'that define a face. To avoid
    confusion, the term\'vertex\'is intentionally avoided in favor
    of\'points\'or\'face-vertices\'.

    The connectivity between points, edges and faces is encoded using a
    common minimal topological description of the faces of the mesh. Each
    face is defined by a set of face-vertices using indices into the
    Mesh\'s *points* array (inherited from UsdGeomPointBased) and laid out
    in a single linear *faceVertexIndices* array for efficiency. A
    companion *faceVertexCounts* array provides, for each face, the number
    of consecutive face-vertices in *faceVertexIndices* that define the
    face. No additional connectivity information is required or
    constructed, so no adjacency or neighborhood queries are available.

    A key property of this mesh schema is that it encodes both subdivision
    surfaces and simpler polygonal meshes. This is achieved by varying the
    *subdivisionScheme* attribute, which is set to specify Catmull-Clark
    subdivision by default, so polygonal meshes must always be explicitly
    declared. The available subdivision schemes and additional subdivision
    features encoded in optional attributes conform to the feature set of
    OpenSubdiv (
    https://graphics.pixar.com/opensubdiv/docs/subdivision_surfaces.html).

    B{A Note About Primvars}

    The following list clarifies the number of elements for and the
    interpolation behavior of the different primvar interpolation types
    for meshes:

       - B{constant} : One element for the entire mesh; no interpolation.

       - B{uniform} : One element for each face of the mesh; elements are
         typically not interpolated but are inherited by other faces derived
         from a given face (via subdivision, tessellation, etc.).

       - B{varying} : One element for each point of the mesh;
         interpolation of point data is always linear.

       - B{vertex} : One element for each point of the mesh; interpolation
         of point data is applied according to the *subdivisionScheme*
         attribute.

       - B{faceVarying} : One element for each of the face-vertices that
         define the mesh topology; interpolation of face-vertex data may be
         smooth or linear, according to the *subdivisionScheme* and
         *faceVaryingLinearInterpolation* attributes.

    Primvar interpolation types and related utilities are described more
    generally in Interpolation of Geometric Primitive Variables.

    B{A Note About Normals}

    Normals should not be authored on a subdivision mesh, since
    subdivision algorithms define their own normals. They should only be
    authored for polygonal meshes ( *subdivisionScheme* ="none").

    The *normals* attribute inherited from UsdGeomPointBased is not a
    generic primvar, but the number of elements in this attribute will be
    determined by its *interpolation*. See
    UsdGeomPointBased::GetNormalsInterpolation() . If *normals* and
    *primvars:normals* are both specified, the latter has precedence. If a
    polygonal mesh specifies B{neither} *normals* nor *primvars:normals*,
    then it should be treated and rendered as faceted, with no attempt to
    compute smooth normals.

    The normals generated for smooth subdivision schemes, e.g. Catmull-
    Clark and Loop, will likewise be smooth, but others, e.g. Bilinear,
    may be discontinuous between faces and/or within non-planar irregular
    faces.

    For any described attribute *Fallback* *Value* or *Allowed* *Values*
    below that are text/tokens, the actual token is published and defined
    in UsdGeomTokens. So to set an attribute to the value"rightHanded",
    use UsdGeomTokens->rightHanded as the value.
    '''
    SHARPNESS_INFINITE: ClassVar[float] = ...
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None:
        """
        Construct a UsdGeomMesh on UsdPrim C{prim}.


        Equivalent to UsdGeomMesh::Get (prim.GetStage(), prim.GetPath()) for a
        *valid* C{prim}, but will not immediately throw an error for an
        invalid C{prim}
        """
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None:
        """
        Construct a UsdGeomMesh on the prim held by C{schemaObj}.


        Should be preferred over UsdGeomMesh (schemaObj.GetPrim()), as it
        preserves SchemaBase state.
        """
    def CreateCornerIndicesAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetCornerIndicesAttr() , and also Create vs Get Property Methods
        for when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateCornerSharpnessesAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetCornerSharpnessesAttr() , and also Create vs Get Property
        Methods for when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateCreaseIndicesAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetCreaseIndicesAttr() , and also Create vs Get Property Methods
        for when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateCreaseLengthsAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetCreaseLengthsAttr() , and also Create vs Get Property Methods
        for when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateCreaseSharpnessesAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetCreaseSharpnessesAttr() , and also Create vs Get Property
        Methods for when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateFaceVaryingLinearInterpolationAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetFaceVaryingLinearInterpolationAttr() , and also Create vs Get
        Property Methods for when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateFaceVertexCountsAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetFaceVertexCountsAttr() , and also Create vs Get Property
        Methods for when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateFaceVertexIndicesAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetFaceVertexIndicesAttr() , and also Create vs Get Property
        Methods for when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateHoleIndicesAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetHoleIndicesAttr() , and also Create vs Get Property Methods for
        when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateInterpolateBoundaryAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetInterpolateBoundaryAttr() , and also Create vs Get Property
        Methods for when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateSubdivisionSchemeAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetSubdivisionSchemeAttr() , and also Create vs Get Property
        Methods for when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateTriangleSubdivisionRuleAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetTriangleSubdivisionRuleAttr() , and also Create vs Get Property
        Methods for when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    @staticmethod
    def Define(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> Mesh:
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
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> Mesh:
        """
        Return a UsdGeomMesh holding the prim adhering to this schema at
        C{path} on C{stage}.


        If no prim exists at C{path} on C{stage}, or if the prim at that path
        does not adhere to this schema, return an invalid schema object. This
        is shorthand for the following: ::

          UsdGeomMesh(stage->GetPrimAtPath(path));

        """
    def GetCornerIndicesAttr(self) -> pxr.Usd.Attribute:
        """
        The indices of points for which a corresponding sharpness value is
        specified in *cornerSharpnesses* (so the size of this array must match
        that of *cornerSharpnesses*).



        Declaration

        C{int[] cornerIndices = []}

        C++ Type

        VtArray<int>

        Usd Type

        SdfValueTypeNames->IntArray
        """
    def GetCornerSharpnessesAttr(self) -> pxr.Usd.Attribute:
        """
        The sharpness values associated with a corresponding set of points
        specified in *cornerIndices* (so the size of this array must match
        that of *cornerIndices*).


        Use the constant C{SHARPNESS_INFINITE} for a perfectly sharp corner.

        Declaration

        C{float[] cornerSharpnesses = []}

        C++ Type

        VtArray<float>

        Usd Type

        SdfValueTypeNames->FloatArray
        """
    def GetCreaseIndicesAttr(self) -> pxr.Usd.Attribute:
        """
        The indices of points grouped into sets of successive pairs that
        identify edges to be creased.


        The size of this array must be equal to the sum of all elements of the
        *creaseLengths* attribute.

        Declaration

        C{int[] creaseIndices = []}

        C++ Type

        VtArray<int>

        Usd Type

        SdfValueTypeNames->IntArray
        """
    def GetCreaseLengthsAttr(self) -> pxr.Usd.Attribute:
        """
        The length of this array specifies the number of creases (sets of
        adjacent sharpened edges) on the mesh.


        Each element gives the number of points of each crease, whose indices
        are successively laid out in the *creaseIndices* attribute. Since each
        crease must be at least one edge long, each element of this array must
        be at least two.

        Declaration

        C{int[] creaseLengths = []}

        C++ Type

        VtArray<int>

        Usd Type

        SdfValueTypeNames->IntArray
        """
    def GetCreaseSharpnessesAttr(self) -> pxr.Usd.Attribute:
        """
        The per-crease or per-edge sharpness values for all creases.


        Since *creaseLengths* encodes the number of points in each crease, the
        number of elements in this array will be either len(creaseLengths) or
        the sum over all X of (creaseLengths[X] - 1). Note that while the RI
        spec allows each crease to have either a single sharpness or a value
        per-edge, USD will encode either a single sharpness per crease on a
        mesh, or sharpnesses for all edges making up the creases on a mesh.
        Use the constant C{SHARPNESS_INFINITE} for a perfectly sharp crease.

        Declaration

        C{float[] creaseSharpnesses = []}

        C++ Type

        VtArray<float>

        Usd Type

        SdfValueTypeNames->FloatArray
        """
    def GetFaceCount(self, timeCode: pxr.Usd.TimeCode | float | pxr.Sdf.TimeCode = ...) -> int:
        """
        Returns the number of faces as defined by the size of the
        *faceVertexCounts* array at *timeCode*.



        For most code, this check will be performant. When using file formats
        where the cost of attribute reading is high and the time sampled array
        will be read into memory later, it may be better to explicitly read
        the value once and check the size of the array directly.

        GetFaceVertexCountsAttr()
        """
    def GetFaceVaryingLinearInterpolationAttr(self) -> pxr.Usd.Attribute:
        '''
        Specifies how elements of a primvar of interpolation
        type"faceVarying"are interpolated for subdivision surfaces.


        Interpolation can be as smooth as a"vertex"primvar or constrained to
        be linear at features specified by several options. Valid values
        correspond to choices available in OpenSubdiv:

           - B{none} : No linear constraints or sharpening, smooth everywhere

           - B{cornersOnly} : Sharpen corners of discontinuous boundaries
             only, smooth everywhere else

           - B{cornersPlus1} : The default, same as"cornersOnly"plus
             additional sharpening at points where three or more distinct face-
             varying values occur

           - B{cornersPlus2} : Same as"cornersPlus1"plus additional sharpening
             at points with at least one discontinuous boundary corner or only one
             discontinuous boundary edge (a dart)

           - B{boundaries} : Piecewise linear along discontinuous boundaries,
             smooth interior

           - B{all} : Piecewise linear everywhere

        These are illustrated and described in more detail in the OpenSubdiv
        documentation:
        https://graphics.pixar.com/opensubdiv/docs/subdivision_surfaces.html#face-
        varying-interpolation-rules

        Declaration

        C{token faceVaryingLinearInterpolation ="cornersPlus1"}

        C++ Type

        TfToken

        Usd Type

        SdfValueTypeNames->Token

        Allowed Values

        none, cornersOnly, cornersPlus1, cornersPlus2, boundaries, all
        '''
    def GetFaceVertexCountsAttr(self) -> pxr.Usd.Attribute:
        """
        Provides the number of vertices in each face of the mesh, which is
        also the number of consecutive indices in *faceVertexIndices* that
        define the face.


        The length of this attribute is the number of faces in the mesh. If
        this attribute has more than one timeSample, the mesh is considered to
        be topologically varying.

        Declaration

        C{int[] faceVertexCounts}

        C++ Type

        VtArray<int>

        Usd Type

        SdfValueTypeNames->IntArray
        """
    def GetFaceVertexIndicesAttr(self) -> pxr.Usd.Attribute:
        """
        Flat list of the index (into the *points* attribute) of each vertex of
        each face in the mesh.


        If this attribute has more than one timeSample, the mesh is considered
        to be topologically varying.

        Declaration

        C{int[] faceVertexIndices}

        C++ Type

        VtArray<int>

        Usd Type

        SdfValueTypeNames->IntArray
        """
    def GetHoleIndicesAttr(self) -> pxr.Usd.Attribute:
        """
        The indices of all faces that should be treated as holes, i.e.


        made invisible. This is traditionally a feature of subdivision
        surfaces and not generally applied to polygonal meshes.

        Declaration

        C{int[] holeIndices = []}

        C++ Type

        VtArray<int>

        Usd Type

        SdfValueTypeNames->IntArray
        """
    def GetInterpolateBoundaryAttr(self) -> pxr.Usd.Attribute:
        '''
        Specifies how subdivision is applied for faces adjacent to boundary
        edges and boundary points.


        Valid values correspond to choices available in OpenSubdiv:

           - B{none} : No boundary interpolation is applied and boundary faces
             are effectively treated as holes

           - B{edgeOnly} : A sequence of boundary edges defines a smooth curve
             to which the edges of subdivided boundary faces converge

           - B{edgeAndCorner} : The default, similar to"edgeOnly"but the
             smooth boundary curve is made sharp at corner points

        These are illustrated and described in more detail in the OpenSubdiv
        documentation:
        https://graphics.pixar.com/opensubdiv/docs/subdivision_surfaces.html#boundary-
        interpolation-rules

        Declaration

        C{token interpolateBoundary ="edgeAndCorner"}

        C++ Type

        TfToken

        Usd Type

        SdfValueTypeNames->Token

        Allowed Values

        none, edgeOnly, edgeAndCorner
        '''
    @staticmethod
    def GetSchemaAttributeNames(includeInherited: bool = ...) -> list[str]:
        """
        Return a vector of names of all pre-declared attributes for this
        schema class and all its ancestor classes.


        Does not include attributes that may be authored by custom/extended
        methods of the schemas involved.
        """
    def GetSubdivisionSchemeAttr(self) -> pxr.Usd.Attribute:
        '''
        The subdivision scheme to be applied to the surface.


        Valid values are:

           - B{catmullClark} : The default, Catmull-Clark subdivision;
             preferred for quad-dominant meshes (generalizes B-splines);
             interpolation of point data is smooth (non-linear)

           - B{loop} : Loop subdivision; preferred for purely triangular
             meshes; interpolation of point data is smooth (non-linear)

           - B{bilinear} : Subdivision reduces all faces to quads
             (topologically similar to"catmullClark"); interpolation of point data
             is bilinear

           - B{none} : No subdivision, i.e. a simple polygonal mesh;
             interpolation of point data is linear

        Polygonal meshes are typically lighter weight and faster to render,
        depending on renderer and render mode. Use of"bilinear"will produce a
        similar shape to a polygonal mesh and may offer additional guarantees
        of watertightness and additional subdivision features (e.g. holes) but
        may also not respect authored normals.

        Declaration

        C{uniform token subdivisionScheme ="catmullClark"}

        C++ Type

        TfToken

        Usd Type

        SdfValueTypeNames->Token

        Variability

        SdfVariabilityUniform

        Allowed Values

        catmullClark, loop, bilinear, none
        '''
    def GetTriangleSubdivisionRuleAttr(self) -> pxr.Usd.Attribute:
        '''
        Specifies an option to the subdivision rules for the Catmull-Clark
        scheme to try and improve undesirable artifacts when subdividing
        triangles.


        Valid values are"catmullClark"for the standard rules (the default)
        and"smooth"for the improvement.

        See
        https://graphics.pixar.com/opensubdiv/docs/subdivision_surfaces.html#triangle-
        subdivision-rule

        Declaration

        C{token triangleSubdivisionRule ="catmullClark"}

        C++ Type

        TfToken

        Usd Type

        SdfValueTypeNames->Token

        Allowed Values

        catmullClark, smooth
        '''
    @staticmethod
    def ValidateTopology(faceVertexIndices: pxr.Vt.IntArray | typing.Iterable[int], faceVertexCounts: pxr.Vt.IntArray | typing.Iterable[int], numPoints: int) -> tuple:
        """
        Validate the topology of a mesh.


        This validates that the sum of C{faceVertexCounts} is equal to the
        size of the C{faceVertexIndices} array, and that all face vertex
        indices in the C{faceVertexIndices} array are in the range [0,
        numPoints). Returns true if the topology is valid, or false otherwise.
        If the topology is invalid and C{reason} is non-null, an error message
        describing the validation error will be set.
        """
    @staticmethod
    def _GetStaticTfType() -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...

class ModelAPI(pxr.Usd.APISchemaBase):
    '''
    UsdGeomModelAPI extends the generic UsdModelAPI schema with geometry
    specific concepts such as cached extents for the entire model,
    constraint targets, and geometry-inspired extensions to the payload
    lofting process.


    As described in GetExtentsHint() below, it is useful to cache extents
    at the model level. UsdGeomModelAPI provides schema for computing and
    storing these cached extents, which can be consumed by
    UsdGeomBBoxCache to provide fast access to precomputed extents that
    will be used as the model\'s bounds ( see
    UsdGeomBBoxCache::UsdGeomBBoxCache() ).

    Draw Modes
    ==========

    Draw modes provide optional alternate imaging behavior for USD
    subtrees with kind model. *model:drawMode* (which is inheritable) and
    *model:applyDrawMode* (which is not) are resolved into a decision to
    stop traversing the scene graph at a certain point, and replace a USD
    subtree with proxy geometry.

    The value of *model:drawMode* determines the type of proxy geometry:
       - *origin* - Draw the model-space basis vectors of the replaced
         prim.

       - *bounds* - Draw the model-space bounding box of the replaced
         prim.

       - *cards* - Draw textured quads as a placeholder for the replaced
         prim.

       - *default* - An explicit opinion to draw the USD subtree as
         normal.

       - *inherited* - Defer to the parent opinion.

    *model:drawMode* falls back to *inherited* so that a whole scene, a
    large group, or all prototypes of a model hierarchy PointInstancer can
    be assigned a draw mode with a single attribute edit. If no draw mode
    is explicitly set in a hierarchy, the resolved value is *default*.

    *model:applyDrawMode* is meant to be written when an asset is
    authored, and provides flexibility for different asset types. For
    example, a character assembly (composed of character, clothes, etc)
    might have *model:applyDrawMode* set at the top of the subtree so the
    whole group can be drawn as a single card object. An effects subtree
    might have *model:applyDrawMode* set at a lower level so each particle
    group draws individually.

    Models of kind component are automatically treated as if
    *model:applyDrawMode* were true if *model:applyDrawMode* is not
    authored on the component prim. A component prim will be drawn drawn
    with a simplified representation when the prim has kind component,
    *model:applyDrawMode* is not authored (or authored to be true), and
    the resolved (i.e. inherited down namespace) value for
    *model:drawMode* is not *default*. If you don\'t want component prims
    to use the resolved non-default drawMode, you must apply the
    UsdGeomModelAPI schema on the prim and explicitly set
    *model:applyDrawMode* to false.

    Cards Geometry
    ==============

    The specific geometry used in cards mode is controlled by the
    *model:cardGeometry* attribute:
       - *cross* - Generate a quad normal to each basis direction and
         negative. Locate each quad so that it bisects the model extents.

       - *box* - Generate a quad normal to each basis direction and
         negative. Locate each quad on a face of the model extents, facing out.

       - *fromTexture* - Generate a quad for each supplied texture from
         attributes stored in that texture\'s metadata.

    For *cross* and *box* mode, the extents are calculated for purposes
    *default*, *proxy*, and *render*, at their earliest authored time. If
    the model has no textures, all six card faces are rendered using
    *model:drawModeColor*. If one or more textures are present, only axes
    with one or more textures assigned are drawn. For each axis, if both
    textures (positive and negative) are specified, they\'ll be used on the
    corresponding card faces; if only one texture is specified, it will be
    mapped to the opposite card face after being flipped on the texture\'s
    s-axis. Any card faces with invalid asset paths will be drawn with
    *model:drawModeColor*.

    Both *model:cardGeometry* and *model:drawModeColor* should be authored
    on the prim where the draw mode takes effect, since these attributes
    are not inherited.

    For *fromTexture* mode, only card faces with valid textures assigned
    are drawn. The geometry is generated by pulling the *worldtoscreen*
    attribute out of texture metadata. This is expected to be a 4x4 matrix
    mapping the model-space position of the card quad to the clip-space
    quad with corners (-1,-1,0) and (1,1,0). The card vertices are
    generated by transforming the clip-space corners by the inverse of
    *worldtoscreen*. Textures are mapped so that (s) and (t) map to (+x)
    and (+y) in clip space. If the metadata cannot be read in the right
    format, or the matrix can\'t be inverted, the card face is not drawn.

    All card faces are drawn and textured as single-sided.

    For any described attribute *Fallback* *Value* or *Allowed* *Values*
    below that are text/tokens, the actual token is published and defined
    in UsdGeomTokens. So to set an attribute to the value"rightHanded",
    use UsdGeomTokens->rightHanded as the value.
    '''
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None:
        """
        Construct a UsdGeomModelAPI on UsdPrim C{prim}.


        Equivalent to UsdGeomModelAPI::Get (prim.GetStage(), prim.GetPath())
        for a *valid* C{prim}, but will not immediately throw an error for an
        invalid C{prim}
        """
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None:
        """
        Construct a UsdGeomModelAPI on the prim held by C{schemaObj}.


        Should be preferred over UsdGeomModelAPI (schemaObj.GetPrim()), as it
        preserves SchemaBase state.
        """
    @staticmethod
    def Apply(prim: pxr.Usd.Prim) -> ModelAPI:
        '''
        Applies this B{single-apply} API schema to the given C{prim}.


        This information is stored by adding"GeomModelAPI"to the token-valued,
        listOp metadata *apiSchemas* on the prim.

        A valid UsdGeomModelAPI object is returned upon success. An invalid
        (or empty) UsdGeomModelAPI object is returned upon failure. See
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
    def ComputeExtentsHint(self, bboxCache: BBoxCache) -> pxr.Vt.Vec3fArray:
        """
        Compute a value suitable for passing to SetExtentsHint() .


        If this model is a UsdGeomBoundable, call
        UsdGeomBoundable::ComputeExtentFromPlugins() with the C{bboxCache} 's
        time code. If that function returns true, then populate the returned
        array with the min and max repeated according to the number of tokens
        in UsdGeomImageable::GetOrderedPurposeTokens() . Otherwise return an
        array with a single empty range.

        If this model is not a UsdGeomBoundable, populate the return value by
        calling UsdGeomBBoxCache::ComputeUntransformedBound() (and
        GfBBox3d::ComputeAlignedBox() on that result) for each token in
        UsdGeomImageable::GetOrderedPurposeTokens() .

        In either case the, Nth successive pair of entries in the returned
        array will be the min and max coordinates of the extent corresponding
        to the Nth token in UsdGeomImageable::GetOrderedPurposeTokens() ,
        except trailing empty boxes are omitted, unless all boxes are empty in
        which case the result is a single empty box.

        For example, if GetOrderedPurposeTokens() is [default, render, proxy,
        guide] and this function returns [(0,0,0), (1,1,1), (+FLT_MAX),
        (-FLT_MIN), (0,0,0), (1,1,1)] then this means that the computed
        extents for'default'and'proxy'purpose are [(0,0,0), (1,1,1)] and the
        extents for'render'and'guide'purposes are empty.

        This function modifies C{bboxCache's} included purposes.

        C{bboxCache} must not be used concurrently during the execution of
        this function.
        """
    def ComputeModelDrawMode(self, parentDrawMode: str | pxr.Ar.ResolvedPath = ...) -> str:
        '''
        Calculate the effective model:drawMode of this prim.


        If the draw mode is authored on this prim, it\'s used. Otherwise, the
        fallback value is"inherited", which defers to the parent opinion. The
        first non-inherited opinion found walking from this prim towards the
        root is used. If the attribute isn\'t set on any ancestors, we
        return"default"(meaning, disable"drawMode"geometry).

        If this function is being called in a traversal context to compute the
        draw mode of an entire hierarchy of prims, it would be beneficial to
        cache and pass in the computed parent draw-mode via the
        C{parentDrawMode} parameter. This avoids repeated upward traversal to
        look for ancestor opinions.

        When C{parentDrawMode} is empty (or unspecified), this function does
        an upward traversal to find the closest ancestor with an authored
        model:drawMode.

        GetModelDrawModeAttr()
        '''
    def CreateConstraintTarget(self, _constraintName: str | pxr.Ar.ResolvedPath, /) -> ConstraintTarget:
        """
        Creates a new constraint target with the given name,
        C{constraintName}.


        If the constraint target already exists, then the existing target is
        returned. If it does not exist, a new one is created and returned.
        """
    def CreateModelApplyDrawModeAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetModelApplyDrawModeAttr() , and also Create vs Get Property
        Methods for when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateModelCardGeometryAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetModelCardGeometryAttr() , and also Create vs Get Property
        Methods for when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateModelCardTextureXNegAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetModelCardTextureXNegAttr() , and also Create vs Get Property
        Methods for when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateModelCardTextureXPosAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetModelCardTextureXPosAttr() , and also Create vs Get Property
        Methods for when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateModelCardTextureYNegAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetModelCardTextureYNegAttr() , and also Create vs Get Property
        Methods for when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateModelCardTextureYPosAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetModelCardTextureYPosAttr() , and also Create vs Get Property
        Methods for when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateModelCardTextureZNegAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetModelCardTextureZNegAttr() , and also Create vs Get Property
        Methods for when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateModelCardTextureZPosAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetModelCardTextureZPosAttr() , and also Create vs Get Property
        Methods for when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateModelDrawModeAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetModelDrawModeAttr() , and also Create vs Get Property Methods
        for when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateModelDrawModeColorAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetModelDrawModeColorAttr() , and also Create vs Get Property
        Methods for when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    @staticmethod
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> ModelAPI:
        """
        Return a UsdGeomModelAPI holding the prim adhering to this schema at
        C{path} on C{stage}.


        If no prim exists at C{path} on C{stage}, or if the prim at that path
        does not adhere to this schema, return an invalid schema object. This
        is shorthand for the following: ::

          UsdGeomModelAPI(stage->GetPrimAtPath(path));

        """
    def GetConstraintTarget(self, _constraintName: str | pxr.Ar.ResolvedPath, /) -> ConstraintTarget:
        """
        Get the constraint target with the given name, C{constraintName}.


        If the requested constraint target does not exist, then an invalid
        UsdConstraintTarget object is returned.
        """
    def GetConstraintTargets(self) -> list[ConstraintTarget]:
        '''
        Returns all the constraint targets belonging to the model.


        Only valid constraint targets in the"constraintTargets"namespace are
        returned by this method.
        '''
    def GetExtentsHint(self, time: pxr.Usd.TimeCode | float | pxr.Sdf.TimeCode = ...) -> pxr.Vt.Vec3fArray:
        '''
        Retrieve the authored value (if any) of this model\'s"extentsHint".


        Persistent caching of bounds in USD is a potentially perilous
        endeavor, given that:
           - It is very easy to add overrides in new super-layers that
             invalidate the cached bounds, and no practical way to automatically
             detect when this happens

           - It is possible for references to be allowed to"float", so that
             asset updates can flow directly into cached scenes. Such changes in
             referenced scene description can also invalidate cached bounds in
             referencing layers.
             For these reasons, as a general rule, we only persistently cache leaf
             gprim extents in object space. However, even with cached gprim
             extents, computing bounds can be expensive. Since model-level bounds
             are so useful to many graphics applications, we make an exception,
             with some caveats. The"extentsHint"should be considered entirely
             optional (whereas gprim extent is not); if authored, it should
             contains the extents for various values of gprim purposes. The extents
             for different values of purpose are stored in a linear Vec3f array as
             pairs of GfVec3f values in the order specified by
             UsdGeomImageable::GetOrderedPurposeTokens() . This list is trimmed to
             only include non-empty extents. i.e., if a model has only default and
             render geoms, then it will only have 4 GfVec3f values in its
             extentsHint array. We do not skip over zero extents, so if a model has
             only default and proxy geom, we will author six GfVec3f \'s, the middle
             two representing an zero extent for render geometry.

        A UsdGeomBBoxCache can be configured to first consult the cached
        extents when evaluating model roots, rather than descending into the
        models for the full computation. This is not the default behavior, and
        gives us a convenient way to validate that the cached extentsHint is
        still valid.

        C{true} if a value was fetched; C{false} if no value was authored, or
        on error. It is an error to make this query of a prim that is not a
        model root.

        UsdGeomImageable::GetPurposeAttr() ,
        UsdGeomImageable::GetOrderedPurposeTokens()
        '''
    def GetExtentsHintAttr(self) -> pxr.Usd.Attribute:
        """
        Returns the custom'extentsHint'attribute if it exits.
        """
    def GetModelApplyDrawModeAttr(self) -> pxr.Usd.Attribute:
        """
        If true, and the resolved value of *model:drawMode* is non-default,
        apply an alternate imaging mode to this prim.


        See Draw Modes.

        Declaration

        C{uniform bool model:applyDrawMode = 0}

        C++ Type

        bool

        Usd Type

        SdfValueTypeNames->Bool

        Variability

        SdfVariabilityUniform
        """
    def GetModelCardGeometryAttr(self) -> pxr.Usd.Attribute:
        '''
        The geometry to generate for imaging prims inserted for *cards*
        imaging mode.


        See Cards Geometry for geometry descriptions.

        Declaration

        C{uniform token model:cardGeometry ="cross"}

        C++ Type

        TfToken

        Usd Type

        SdfValueTypeNames->Token

        Variability

        SdfVariabilityUniform

        Allowed Values

        cross, box, fromTexture
        '''
    def GetModelCardTextureXNegAttr(self) -> pxr.Usd.Attribute:
        """
        In *cards* imaging mode, the texture applied to the X- quad.


        The texture axes (s,t) are mapped to model-space axes (y, -z).

        Declaration

        C{asset model:cardTextureXNeg}

        C++ Type

        SdfAssetPath

        Usd Type

        SdfValueTypeNames->Asset
        """
    def GetModelCardTextureXPosAttr(self) -> pxr.Usd.Attribute:
        """
        In *cards* imaging mode, the texture applied to the X+ quad.


        The texture axes (s,t) are mapped to model-space axes (-y, -z).

        Declaration

        C{asset model:cardTextureXPos}

        C++ Type

        SdfAssetPath

        Usd Type

        SdfValueTypeNames->Asset
        """
    def GetModelCardTextureYNegAttr(self) -> pxr.Usd.Attribute:
        """
        In *cards* imaging mode, the texture applied to the Y- quad.


        The texture axes (s,t) are mapped to model-space axes (-x, -z).

        Declaration

        C{asset model:cardTextureYNeg}

        C++ Type

        SdfAssetPath

        Usd Type

        SdfValueTypeNames->Asset
        """
    def GetModelCardTextureYPosAttr(self) -> pxr.Usd.Attribute:
        """
        In *cards* imaging mode, the texture applied to the Y+ quad.


        The texture axes (s,t) are mapped to model-space axes (x, -z).

        Declaration

        C{asset model:cardTextureYPos}

        C++ Type

        SdfAssetPath

        Usd Type

        SdfValueTypeNames->Asset
        """
    def GetModelCardTextureZNegAttr(self) -> pxr.Usd.Attribute:
        """
        In *cards* imaging mode, the texture applied to the Z- quad.


        The texture axes (s,t) are mapped to model-space axes (-x, -y).

        Declaration

        C{asset model:cardTextureZNeg}

        C++ Type

        SdfAssetPath

        Usd Type

        SdfValueTypeNames->Asset
        """
    def GetModelCardTextureZPosAttr(self) -> pxr.Usd.Attribute:
        """
        In *cards* imaging mode, the texture applied to the Z+ quad.


        The texture axes (s,t) are mapped to model-space axes (x, -y).

        Declaration

        C{asset model:cardTextureZPos}

        C++ Type

        SdfAssetPath

        Usd Type

        SdfValueTypeNames->Asset
        """
    def GetModelDrawModeAttr(self) -> pxr.Usd.Attribute:
        '''
        Alternate imaging mode; applied to this prim or child prims where
        *model:applyDrawMode* is true, or where the prim has kind *component*
        and *model:applyDrawMode* is not authored.


        See Draw Modes for mode descriptions.

        Declaration

        C{uniform token model:drawMode ="inherited"}

        C++ Type

        TfToken

        Usd Type

        SdfValueTypeNames->Token

        Variability

        SdfVariabilityUniform

        Allowed Values

        origin, bounds, cards, default, inherited
        '''
    def GetModelDrawModeColorAttr(self) -> pxr.Usd.Attribute:
        """
        The base color of imaging prims inserted for alternate imaging modes.


        For *origin* and *bounds* modes, this controls line color; for *cards*
        mode, this controls the fallback quad color.

        Declaration

        C{uniform float3 model:drawModeColor = (0.18, 0.18, 0.18)}

        C++ Type

        GfVec3f

        Usd Type

        SdfValueTypeNames->Float3

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
    def SetExtentsHint(self, extents: pxr.Vt.Vec3fArray | typing.Iterable[list[float]] | typing.Iterable[pxr.Gf.Vec3f] | typing.Iterable[tuple[float, float, float]], time: pxr.Usd.TimeCode | float | pxr.Sdf.TimeCode = ...) -> bool:
        """
        Authors the extentsHint array for this model at the given time.



        GetExtentsHint()
        """
    @staticmethod
    def _GetStaticTfType() -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...

class MotionAPI(pxr.Usd.APISchemaBase):
    """
    UsdGeomMotionAPI encodes data that can live on any prim that may
    affect computations involving:



       - computed motion for motion blur

       - sampling for motion blur

    The motion:blurScale attribute allows artists to scale the B{amount}
    of motion blur to be rendered for parts of the scene without changing
    the recorded animation. See Effectively Applying motion:blurScale for
    use and implementation details.
    """
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None:
        """
        Construct a UsdGeomMotionAPI on UsdPrim C{prim}.


        Equivalent to UsdGeomMotionAPI::Get (prim.GetStage(), prim.GetPath())
        for a *valid* C{prim}, but will not immediately throw an error for an
        invalid C{prim}
        """
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None:
        """
        Construct a UsdGeomMotionAPI on the prim held by C{schemaObj}.


        Should be preferred over UsdGeomMotionAPI (schemaObj.GetPrim()), as it
        preserves SchemaBase state.
        """
    @staticmethod
    def Apply(prim: pxr.Usd.Prim) -> MotionAPI:
        '''
        Applies this B{single-apply} API schema to the given C{prim}.


        This information is stored by adding"MotionAPI"to the token-valued,
        listOp metadata *apiSchemas* on the prim.

        A valid UsdGeomMotionAPI object is returned upon success. An invalid
        (or empty) UsdGeomMotionAPI object is returned upon failure. See
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
    def ComputeMotionBlurScale(self, time: pxr.Usd.TimeCode | float | pxr.Sdf.TimeCode = ...) -> float:
        """
        Compute the inherited value of *motion:blurScale* at C{time}, i.e.


        the authored value on the prim closest to this prim in namespace,
        resolved upwards through its ancestors in namespace.

        the inherited value, or 1.0 if neither the prim nor any of its
        ancestors possesses an authored value.

        this is a reference implementation that is not particularly efficient
        if evaluating over many prims, because it does not share inherited
        results.
        """
    def ComputeNonlinearSampleCount(self, time: pxr.Usd.TimeCode | float | pxr.Sdf.TimeCode = ...) -> int:
        """
        Compute the inherited value of *nonlinearSampleCount* at C{time}, i.e.


        the authored value on the prim closest to this prim in namespace,
        resolved upwards through its ancestors in namespace.

        the inherited value, or 3 if neither the prim nor any of its ancestors
        possesses an authored value.

        this is a reference implementation that is not particularly efficient
        if evaluating over many prims, because it does not share inherited
        results.
        """
    def ComputeVelocityScale(self, time: pxr.Usd.TimeCode | float | pxr.Sdf.TimeCode = ...) -> float:
        """
        Deprecated

        Compute the inherited value of *velocityScale* at C{time}, i.e. the
        authored value on the prim closest to this prim in namespace, resolved
        upwards through its ancestors in namespace.

        the inherited value, or 1.0 if neither the prim nor any of its
        ancestors possesses an authored value.

        this is a reference implementation that is not particularly efficient
        if evaluating over many prims, because it does not share inherited
        results.
        """
    def CreateMotionBlurScaleAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetMotionBlurScaleAttr() , and also Create vs Get Property Methods
        for when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateNonlinearSampleCountAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetNonlinearSampleCountAttr() , and also Create vs Get Property
        Methods for when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateVelocityScaleAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetVelocityScaleAttr() , and also Create vs Get Property Methods
        for when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    @staticmethod
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> MotionAPI:
        """
        Return a UsdGeomMotionAPI holding the prim adhering to this schema at
        C{path} on C{stage}.


        If no prim exists at C{path} on C{stage}, or if the prim at that path
        does not adhere to this schema, return an invalid schema object. This
        is shorthand for the following: ::

          UsdGeomMotionAPI(stage->GetPrimAtPath(path));

        """
    def GetMotionBlurScaleAttr(self) -> pxr.Usd.Attribute:
        '''
        BlurScale is an B{inherited} float attribute that stipulates the
        rendered motion blur (as typically specified via UsdGeomCamera \'s
        *shutter:open* and *shutter:close* properties) should be scaled for
        B{all objects} at and beneath the prim in namespace on which the
        *motion:blurScale* value is specified.


        Without changing any other data in the scene, *blurScale* allows
        artists to"dial in"the amount of blur on a per-object basis. A
        *blurScale* value of zero removes all blur, a value of 0.5 reduces
        blur by half, and a value of 2.0 doubles the blur. The legal range for
        *blurScale* is [0, inf), although very high values may result in
        extremely expensive renders, and may exceed the capabilities of some
        renderers.

        Although renderers are free to implement this feature however they see
        fit, see Effectively Applying motion:blurScale for our guidance on
        implementing the feature universally and efficiently.

        ComputeMotionBlurScale()

        Declaration

        C{float motion:blurScale = 1}

        C++ Type

        float

        Usd Type

        SdfValueTypeNames->Float
        '''
    def GetNonlinearSampleCountAttr(self) -> pxr.Usd.Attribute:
        """
        Determines the number of position or transformation samples created
        when motion is described by attributes contributing non-linear terms.


        To give an example, imagine an application (such as a renderer)
        consuming'points'and the USD document also contains'accelerations'for
        the same prim. Unless the application can consume
        these'accelerations'itself, an intermediate layer has to compute
        samples within the sampling interval for the point positions based on
        the value of'points','velocities'and'accelerations'. The number of
        these samples is given by'nonlinearSampleCount'. The samples are
        equally spaced within the sampling interval.

        Another example involves the PointInstancer
        where'nonlinearSampleCount'is relevant
        when'angularVelocities'or'accelerations'are authored.

        'nonlinearSampleCount'is an B{inherited} attribute, also see
        ComputeNonlinearSampleCount()

        Declaration

        C{int motion:nonlinearSampleCount = 3}

        C++ Type

        int

        Usd Type

        SdfValueTypeNames->Int
        """
    @staticmethod
    def GetSchemaAttributeNames(includeInherited: bool = ...) -> list[str]:
        """
        Return a vector of names of all pre-declared attributes for this
        schema class and all its ancestor classes.


        Does not include attributes that may be authored by custom/extended
        methods of the schemas involved.
        """
    def GetVelocityScaleAttr(self) -> pxr.Usd.Attribute:
        """
        Deprecated

        VelocityScale is an B{inherited} float attribute that velocity-based
        schemas (e.g. PointBased, PointInstancer) can consume to compute
        interpolated positions and orientations by applying velocity and
        angularVelocity, which is required for interpolating between samples
        when topology is varying over time. Although these quantities are
        generally physically computed by a simulator, sometimes we require
        more or less motion-blur to achieve the desired look.  VelocityScale
        allows artists to dial-in, as a post-sim correction, a scale factor to
        be applied to the velocity prior to computing interpolated positions
        from it.

        Declaration

        C{float motion:velocityScale = 1}

        C++ Type

        float

        Usd Type

        SdfValueTypeNames->Float
        """
    @staticmethod
    def _GetStaticTfType() -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...

class NurbsCurves(Curves):
    """
    This schema is analagous to NURBS Curves in packages like Maya and
    Houdini, often used for interchange of rigging and modeling curves.


    Unlike Maya, this curve spec supports batching of multiple curves into
    a single prim, widths, and normals in the schema. Additionally, we
    require'numSegments + 2 * degree + 1'knots (2 more than maya does).
    This is to be more consistent with RenderMan's NURBS patch
    specification.

    To express a periodic curve:
       - knot[0] = knot[1] - (knots[-2] - knots[-3];

       - knot[-1] = knot[-2] + (knot[2] - knots[1]);

    To express a nonperiodic curve:
       - knot[0] = knot[1];

       - knot[-1] = knot[-2];

    In spite of these slight differences in the spec, curves generated in
    Maya should be preserved when roundtripping.

    *order* and *range*, when representing a batched NurbsCurve should be
    authored one value per curve. *knots* should be the concatentation of
    all batched curves.
    """
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None:
        """
        Construct a UsdGeomNurbsCurves on UsdPrim C{prim}.


        Equivalent to UsdGeomNurbsCurves::Get (prim.GetStage(),
        prim.GetPath()) for a *valid* C{prim}, but will not immediately throw
        an error for an invalid C{prim}
        """
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None:
        """
        Construct a UsdGeomNurbsCurves on the prim held by C{schemaObj}.


        Should be preferred over UsdGeomNurbsCurves (schemaObj.GetPrim()), as
        it preserves SchemaBase state.
        """
    def CreateKnotsAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetKnotsAttr() , and also Create vs Get Property Methods for when
        to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateOrderAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetOrderAttr() , and also Create vs Get Property Methods for when
        to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreatePointWeightsAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetPointWeightsAttr() , and also Create vs Get Property Methods
        for when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateRangesAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetRangesAttr() , and also Create vs Get Property Methods for when
        to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    @staticmethod
    def Define(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> NurbsCurves:
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
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> NurbsCurves:
        """
        Return a UsdGeomNurbsCurves holding the prim adhering to this schema
        at C{path} on C{stage}.


        If no prim exists at C{path} on C{stage}, or if the prim at that path
        does not adhere to this schema, return an invalid schema object. This
        is shorthand for the following: ::

          UsdGeomNurbsCurves(stage->GetPrimAtPath(path));

        """
    def GetKnotsAttr(self) -> pxr.Usd.Attribute:
        """
        Knot vector providing curve parameterization.


        The length of the slice of the array for the ith curve must be (
        curveVertexCount[i] + order[i] ), and its entries must take on
        monotonically increasing values.

        Declaration

        C{double[] knots}

        C++ Type

        VtArray<double>

        Usd Type

        SdfValueTypeNames->DoubleArray
        """
    def GetOrderAttr(self) -> pxr.Usd.Attribute:
        """
        Order of the curve.


        Order must be positive and is equal to the degree of the polynomial
        basis to be evaluated, plus 1. Its value for the'i'th curve must be
        less than or equal to curveVertexCount[i]

        Declaration

        C{int[] order = []}

        C++ Type

        VtArray<int>

        Usd Type

        SdfValueTypeNames->IntArray
        """
    def GetPointWeightsAttr(self) -> pxr.Usd.Attribute:
        '''
        Optionally provides"w"components for each control point, thus must be
        the same length as the points attribute.


        If authored, the curve will be rational. If unauthored, the curve will
        be polynomial, i.e. weight for all points is 1.0.

        Some DCC\'s pre-weight the *points*, but in this schema, *points* are
        not pre-weighted.

        Declaration

        C{double[] pointWeights}

        C++ Type

        VtArray<double>

        Usd Type

        SdfValueTypeNames->DoubleArray
        '''
    def GetRangesAttr(self) -> pxr.Usd.Attribute:
        """
        Provides the minimum and maximum parametric values (as defined by
        knots) over which the curve is actually defined.


        The minimum must be less than the maximum, and greater than or equal
        to the value of the knots['i'th curve slice][order[i]-1]. The maxium
        must be less than or equal to the last element's value in knots['i'th
        curve slice]. Range maps to (vmin, vmax) in the RenderMan spec.

        Declaration

        C{double2[] ranges}

        C++ Type

        VtArray<GfVec2d>

        Usd Type

        SdfValueTypeNames->Double2Array
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

class NurbsPatch(PointBased):
    '''
    Encodes a rational or polynomial non-uniform B-spline surface, with
    optional trim curves.


    The encoding mostly follows that of RiNuPatch and RiTrimCurve:
    https://renderman.pixar.com/resources/RenderMan_20/geometricPrimitives.html#rinupatch,
    with some minor renaming and coalescing for clarity.

    The layout of control vertices in the *points* attribute inherited
    from UsdGeomPointBased is row-major with U considered rows, and V
    columns.

    B{NurbsPatch Form}

    The authored points, orders, knots, weights, and ranges are all that
    is required to render the nurbs patch. However, the only way to model
    closed surfaces with nurbs is to ensure that the first and last
    control points along the given axis are coincident. Similarly, to
    ensure the surface is not only closed but also C2 continuous, the last
    *order* - 1 control points must be (correspondingly) coincident with
    the first *order* - 1 control points, and also the spacing of the last
    corresponding knots must be the same as the first corresponding knots.

    B{Form} is provided as an aid to interchange between modeling and
    animation applications so that they can robustly identify the intent
    with which the surface was modelled, and take measures (if they are
    able) to preserve the continuity/concidence constraints as the surface
    may be rigged or deformed.
       - An *open-form* NurbsPatch has no continuity constraints.

       - A *closed-form* NurbsPatch expects the first and last control
         points to overlap

       - A *periodic-form* NurbsPatch expects the first and last *order* -
         1 control points to overlap.
         B{Nurbs vs Subdivision Surfaces}

    Nurbs are an important modeling primitive in CAD/CAM tools and early
    computer graphics DCC\'s. Because they have a natural UV
    parameterization they easily support"trim curves", which allow smooth
    shapes to be carved out of the surface.

    However, the topology of the patch is always rectangular, and joining
    two nurbs patches together (especially when they have differing
    numbers of spans) is difficult to do smoothly. Also, nurbs are not
    supported by the Ptex texturing technology ( http://ptex.us).

    Neither of these limitations are shared by subdivision surfaces;
    therefore, although they do not subscribe to trim-curve-based shaping,
    subdivs are often considered a more flexible modeling primitive.

    For any described attribute *Fallback* *Value* or *Allowed* *Values*
    below that are text/tokens, the actual token is published and defined
    in UsdGeomTokens. So to set an attribute to the value"rightHanded",
    use UsdGeomTokens->rightHanded as the value.
    '''
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None:
        """
        Construct a UsdGeomNurbsPatch on UsdPrim C{prim}.


        Equivalent to UsdGeomNurbsPatch::Get (prim.GetStage(), prim.GetPath())
        for a *valid* C{prim}, but will not immediately throw an error for an
        invalid C{prim}
        """
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None:
        """
        Construct a UsdGeomNurbsPatch on the prim held by C{schemaObj}.


        Should be preferred over UsdGeomNurbsPatch (schemaObj.GetPrim()), as
        it preserves SchemaBase state.
        """
    def CreatePointWeightsAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetPointWeightsAttr() , and also Create vs Get Property Methods
        for when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateTrimCurveCountsAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetTrimCurveCountsAttr() , and also Create vs Get Property Methods
        for when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateTrimCurveKnotsAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetTrimCurveKnotsAttr() , and also Create vs Get Property Methods
        for when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateTrimCurveOrdersAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetTrimCurveOrdersAttr() , and also Create vs Get Property Methods
        for when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateTrimCurvePointsAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetTrimCurvePointsAttr() , and also Create vs Get Property Methods
        for when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateTrimCurveRangesAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetTrimCurveRangesAttr() , and also Create vs Get Property Methods
        for when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateTrimCurveVertexCountsAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetTrimCurveVertexCountsAttr() , and also Create vs Get Property
        Methods for when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateUFormAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetUFormAttr() , and also Create vs Get Property Methods for when
        to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateUKnotsAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetUKnotsAttr() , and also Create vs Get Property Methods for when
        to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateUOrderAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetUOrderAttr() , and also Create vs Get Property Methods for when
        to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateURangeAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetURangeAttr() , and also Create vs Get Property Methods for when
        to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateUVertexCountAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetUVertexCountAttr() , and also Create vs Get Property Methods
        for when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateVFormAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetVFormAttr() , and also Create vs Get Property Methods for when
        to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateVKnotsAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetVKnotsAttr() , and also Create vs Get Property Methods for when
        to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateVOrderAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetVOrderAttr() , and also Create vs Get Property Methods for when
        to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateVRangeAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetVRangeAttr() , and also Create vs Get Property Methods for when
        to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateVVertexCountAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetVVertexCountAttr() , and also Create vs Get Property Methods
        for when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    @staticmethod
    def Define(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> NurbsPatch:
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
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> NurbsPatch:
        """
        Return a UsdGeomNurbsPatch holding the prim adhering to this schema at
        C{path} on C{stage}.


        If no prim exists at C{path} on C{stage}, or if the prim at that path
        does not adhere to this schema, return an invalid schema object. This
        is shorthand for the following: ::

          UsdGeomNurbsPatch(stage->GetPrimAtPath(path));

        """
    def GetPointWeightsAttr(self) -> pxr.Usd.Attribute:
        '''
        Optionally provides"w"components for each control point, thus must be
        the same length as the points attribute.


        If authored, the patch will be rational. If unauthored, the patch will
        be polynomial, i.e. weight for all points is 1.0.

        Some DCC\'s pre-weight the *points*, but in this schema, *points* are
        not pre-weighted.

        Declaration

        C{double[] pointWeights}

        C++ Type

        VtArray<double>

        Usd Type

        SdfValueTypeNames->DoubleArray
        '''
    @staticmethod
    def GetSchemaAttributeNames(includeInherited: bool = ...) -> list[str]:
        """
        Return a vector of names of all pre-declared attributes for this
        schema class and all its ancestor classes.


        Does not include attributes that may be authored by custom/extended
        methods of the schemas involved.
        """
    def GetTrimCurveCountsAttr(self) -> pxr.Usd.Attribute:
        '''
        Each element specifies how many curves are present in each"loop"of the
        trimCurve, and the length of the array determines how many loops the
        trimCurve contains.


        The sum of all elements is the total nuber of curves in the trim, to
        which we will refer as *nCurves* in describing the other trim
        attributes.

        Declaration

        C{int[] trimCurve:counts}

        C++ Type

        VtArray<int>

        Usd Type

        SdfValueTypeNames->IntArray
        '''
    def GetTrimCurveKnotsAttr(self) -> pxr.Usd.Attribute:
        """
        Flat list of parametric values for each of the *nCurves* curves.


        There will be as many knots as the sum over all elements of
        *vertexCounts* plus the sum over all elements of *orders*.

        Declaration

        C{double[] trimCurve:knots}

        C++ Type

        VtArray<double>

        Usd Type

        SdfValueTypeNames->DoubleArray
        """
    def GetTrimCurveOrdersAttr(self) -> pxr.Usd.Attribute:
        """
        Flat list of orders for each of the *nCurves* curves.



        Declaration

        C{int[] trimCurve:orders}

        C++ Type

        VtArray<int>

        Usd Type

        SdfValueTypeNames->IntArray
        """
    def GetTrimCurvePointsAttr(self) -> pxr.Usd.Attribute:
        """
        Flat list of homogeneous 2D points (u, v, w) that comprise the
        *nCurves* curves.


        The number of points should be equal to the um over all elements of
        *vertexCounts*.

        Declaration

        C{double3[] trimCurve:points}

        C++ Type

        VtArray<GfVec3d>

        Usd Type

        SdfValueTypeNames->Double3Array
        """
    def GetTrimCurveRangesAttr(self) -> pxr.Usd.Attribute:
        """
        Flat list of minimum and maximum parametric values (as defined by
        *knots*) for each of the *nCurves* curves.



        Declaration

        C{double2[] trimCurve:ranges}

        C++ Type

        VtArray<GfVec2d>

        Usd Type

        SdfValueTypeNames->Double2Array
        """
    def GetTrimCurveVertexCountsAttr(self) -> pxr.Usd.Attribute:
        """
        Flat list of number of vertices for each of the *nCurves* curves.



        Declaration

        C{int[] trimCurve:vertexCounts}

        C++ Type

        VtArray<int>

        Usd Type

        SdfValueTypeNames->IntArray
        """
    def GetUFormAttr(self) -> pxr.Usd.Attribute:
        '''
        Interpret the control grid and knot vectors as representing an open,
        geometrically closed, or geometrically closed and C2 continuous
        surface along the U dimension.



        NurbsPatch Form

        Declaration

        C{uniform token uForm ="open"}

        C++ Type

        TfToken

        Usd Type

        SdfValueTypeNames->Token

        Variability

        SdfVariabilityUniform

        Allowed Values

        open, closed, periodic
        '''
    def GetUKnotsAttr(self) -> pxr.Usd.Attribute:
        """
        Knot vector for U direction providing U parameterization.


        The length of this array must be ( uVertexCount + uOrder), and its
        entries must take on monotonically increasing values.

        Declaration

        C{double[] uKnots}

        C++ Type

        VtArray<double>

        Usd Type

        SdfValueTypeNames->DoubleArray
        """
    def GetUOrderAttr(self) -> pxr.Usd.Attribute:
        """
        Order in the U direction.


        Order must be positive and is equal to the degree of the polynomial
        basis to be evaluated, plus 1.

        Declaration

        C{int uOrder}

        C++ Type

        int

        Usd Type

        SdfValueTypeNames->Int
        """
    def GetURangeAttr(self) -> pxr.Usd.Attribute:
        """
        Provides the minimum and maximum parametric values (as defined by
        uKnots) over which the surface is actually defined.


        The minimum must be less than the maximum, and greater than or equal
        to the value of uKnots[uOrder-1]. The maxium must be less than or
        equal to the last element's value in uKnots.

        Declaration

        C{double2 uRange}

        C++ Type

        GfVec2d

        Usd Type

        SdfValueTypeNames->Double2
        """
    def GetUVertexCountAttr(self) -> pxr.Usd.Attribute:
        """
        Number of vertices in the U direction.


        Should be at least as large as uOrder.

        Declaration

        C{int uVertexCount}

        C++ Type

        int

        Usd Type

        SdfValueTypeNames->Int
        """
    def GetVFormAttr(self) -> pxr.Usd.Attribute:
        '''
        Interpret the control grid and knot vectors as representing an open,
        geometrically closed, or geometrically closed and C2 continuous
        surface along the V dimension.



        NurbsPatch Form

        Declaration

        C{uniform token vForm ="open"}

        C++ Type

        TfToken

        Usd Type

        SdfValueTypeNames->Token

        Variability

        SdfVariabilityUniform

        Allowed Values

        open, closed, periodic
        '''
    def GetVKnotsAttr(self) -> pxr.Usd.Attribute:
        """
        Knot vector for V direction providing U parameterization.


        The length of this array must be ( vVertexCount + vOrder), and its
        entries must take on monotonically increasing values.

        Declaration

        C{double[] vKnots}

        C++ Type

        VtArray<double>

        Usd Type

        SdfValueTypeNames->DoubleArray
        """
    def GetVOrderAttr(self) -> pxr.Usd.Attribute:
        """
        Order in the V direction.


        Order must be positive and is equal to the degree of the polynomial
        basis to be evaluated, plus 1.

        Declaration

        C{int vOrder}

        C++ Type

        int

        Usd Type

        SdfValueTypeNames->Int
        """
    def GetVRangeAttr(self) -> pxr.Usd.Attribute:
        """
        Provides the minimum and maximum parametric values (as defined by
        vKnots) over which the surface is actually defined.


        The minimum must be less than the maximum, and greater than or equal
        to the value of vKnots[vOrder-1]. The maxium must be less than or
        equal to the last element's value in vKnots.

        Declaration

        C{double2 vRange}

        C++ Type

        GfVec2d

        Usd Type

        SdfValueTypeNames->Double2
        """
    def GetVVertexCountAttr(self) -> pxr.Usd.Attribute:
        """
        Number of vertices in the V direction.


        Should be at least as large as vOrder.

        Declaration

        C{int vVertexCount}

        C++ Type

        int

        Usd Type

        SdfValueTypeNames->Int
        """
    @staticmethod
    def _GetStaticTfType() -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...

class Plane(Gprim):
    '''
    Defines a primitive plane, centered at the origin, and is defined by a
    cardinal axis, width, and length.


    The plane is double-sided by default.

    The axis of width and length are perpendicular to the plane\'s *axis*:

    axis

    width

    length

    X

    z-axis

    y-axis

    Y

    x-axis

    z-axis

    Z

    x-axis

    y-axis

    For any described attribute *Fallback* *Value* or *Allowed* *Values*
    below that are text/tokens, the actual token is published and defined
    in UsdGeomTokens. So to set an attribute to the value"rightHanded",
    use UsdGeomTokens->rightHanded as the value.
    '''
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None:
        """
        Construct a UsdGeomPlane on UsdPrim C{prim}.


        Equivalent to UsdGeomPlane::Get (prim.GetStage(), prim.GetPath()) for
        a *valid* C{prim}, but will not immediately throw an error for an
        invalid C{prim}
        """
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None:
        """
        Construct a UsdGeomPlane on the prim held by C{schemaObj}.


        Should be preferred over UsdGeomPlane (schemaObj.GetPrim()), as it
        preserves SchemaBase state.
        """
    def CreateAxisAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetAxisAttr() , and also Create vs Get Property Methods for when
        to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateDoubleSidedAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetDoubleSidedAttr() , and also Create vs Get Property Methods for
        when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateExtentAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetExtentAttr() , and also Create vs Get Property Methods for when
        to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateLengthAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetLengthAttr() , and also Create vs Get Property Methods for when
        to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateWidthAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetWidthAttr() , and also Create vs Get Property Methods for when
        to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    @staticmethod
    def Define(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> Plane:
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
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> Plane:
        """
        Return a UsdGeomPlane holding the prim adhering to this schema at
        C{path} on C{stage}.


        If no prim exists at C{path} on C{stage}, or if the prim at that path
        does not adhere to this schema, return an invalid schema object. This
        is shorthand for the following: ::

          UsdGeomPlane(stage->GetPrimAtPath(path));

        """
    def GetAxisAttr(self) -> pxr.Usd.Attribute:
        '''
        The axis along which the surface of the plane is aligned.


        When set to\'Z\'the plane is in the xy-plane; when *axis* is\'X\'the plane
        is in the yz-plane, and when *axis* is\'Y\'the plane is in the xz-plane.

        UsdGeomGprim::GetAxisAttr().

        Declaration

        C{uniform token axis ="Z"}

        C++ Type

        TfToken

        Usd Type

        SdfValueTypeNames->Token

        Variability

        SdfVariabilityUniform

        Allowed Values

        X, Y, Z
        '''
    def GetDoubleSidedAttr(self) -> pxr.Usd.Attribute:
        """
        Planes are double-sided by default.


        Clients may also support single-sided planes.

        UsdGeomGprim::GetDoubleSidedAttr()

        Declaration

        C{uniform bool doubleSided = 1}

        C++ Type

        bool

        Usd Type

        SdfValueTypeNames->Bool

        Variability

        SdfVariabilityUniform
        """
    def GetExtentAttr(self) -> pxr.Usd.Attribute:
        """
        Extent is re-defined on Plane only to provide a fallback value.



        UsdGeomGprim::GetExtentAttr() .

        Declaration

        C{float3[] extent = [(-1, -1, 0), (1, 1, 0)]}

        C++ Type

        VtArray<GfVec3f>

        Usd Type

        SdfValueTypeNames->Float3Array
        """
    def GetLengthAttr(self) -> pxr.Usd.Attribute:
        """
        The length of the plane, which aligns to the y-axis when *axis*
        is'Z'or'X', or to the z-axis when *axis* is'Y'.


        If you author *length* you must also author *extent*.

        UsdGeomGprim::GetExtentAttr()

        Declaration

        C{double length = 2}

        C++ Type

        double

        Usd Type

        SdfValueTypeNames->Double
        """
    @staticmethod
    def GetSchemaAttributeNames(includeInherited: bool = ...) -> list[str]:
        """
        Return a vector of names of all pre-declared attributes for this
        schema class and all its ancestor classes.


        Does not include attributes that may be authored by custom/extended
        methods of the schemas involved.
        """
    def GetWidthAttr(self) -> pxr.Usd.Attribute:
        """
        The width of the plane, which aligns to the x-axis when *axis*
        is'Z'or'Y', or to the z-axis when *axis* is'X'.


        If you author *width* you must also author *extent*.

        UsdGeomGprim::GetExtentAttr()

        Declaration

        C{double width = 2}

        C++ Type

        double

        Usd Type

        SdfValueTypeNames->Double
        """
    @staticmethod
    def _GetStaticTfType() -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...

class PointBased(Gprim):
    """
    Base class for all UsdGeomGprims that possess points, providing common
    attributes such as normals and velocities.
    """
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None:
        """
        Construct a UsdGeomPointBased on UsdPrim C{prim}.


        Equivalent to UsdGeomPointBased::Get (prim.GetStage(), prim.GetPath())
        for a *valid* C{prim}, but will not immediately throw an error for an
        invalid C{prim}
        """
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None:
        """
        Construct a UsdGeomPointBased on the prim held by C{schemaObj}.


        Should be preferred over UsdGeomPointBased (schemaObj.GetPrim()), as
        it preserves SchemaBase state.
        """
    @staticmethod
    def ComputeExtent(points: pxr.Vt.Vec3fArray | typing.Iterable[list[float]] | typing.Iterable[pxr.Gf.Vec3f] | typing.Iterable[tuple[float, float, float]]) -> pxr.Vt.Vec3fArray:
        """
        Compute the extent for the point cloud defined by points.



        true on success, false if extents was unable to be calculated. On
        success, extent will contain the axis-aligned bounding box of the
        point cloud defined by points.

        This function is to provide easy authoring of extent for usd authoring
        tools, hence it is static and acts outside a specific prim (as in
        attribute based methods).
        """
    def ComputePointsAtTime(self, time: pxr.Usd.TimeCode | float | pxr.Sdf.TimeCode, baseTime: pxr.Usd.TimeCode | float | pxr.Sdf.TimeCode) -> pxr.Vt.Vec3fArray:
        """
        Compute points given the positions, velocities and accelerations at
        C{time}.


        This will return C{false} and leave C{points} untouched if:
           - C{points} is None

           - one of C{time} and C{baseTime} is numeric and the other is
             UsdTimeCode::Default() (they must either both be numeric or both be
             default)

           - there is no authored points attribute

        If there is no error, we will return C{true} and C{points} will
        contain the computed points.

        points

        - the out parameter for the new points. Its size will depend on the
        authored data. time

        - UsdTimeCode at which we want to evaluate the transforms baseTime

        - required for correct interpolation between samples when *velocities*
        or *accelerations* are present. If there are samples for *positions*
        and *velocities* at t1 and t2, normal value resolution would attempt
        to interpolate between the two samples, and if they could not be
        interpolated because they differ in size (common in cases where
        velocity is authored), will choose the sample at t1. When sampling for
        the purposes of motion-blur, for example, it is common, when rendering
        the frame at t2, to sample at [ t2-shutter/2, t2+shutter/2 ] for a
        shutter interval of *shutter*. The first sample falls between t1 and
        t2, but we must sample at t2 and apply velocity-based interpolation
        based on those samples to get a correct result. In such scenarios, one
        should provide a C{baseTime} of t2 when querying *both* samples. If
        your application does not care about off-sample interpolation, it can
        supply the same value for C{baseTime} that it does for C{time}. When
        C{baseTime} is less than or equal to C{time}, we will choose the lower
        bracketing timeSample.
        """
    def ComputePointsAtTimes(self, times: typing.Iterable[pxr.Usd.TimeCode | float | pxr.Sdf.TimeCode], baseTime: pxr.Usd.TimeCode | float | pxr.Sdf.TimeCode) -> list[list[pxr.Gf.Vec3f]]:
        """
        Compute points as in ComputePointsAtTime, but using multiple sample
        times.


        An array of vector arrays is returned where each vector array contains
        the points for the corresponding time in C{times}.

        times

        - A vector containing the UsdTimeCodes at which we want to sample.
        """
    def CreateAccelerationsAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetAccelerationsAttr() , and also Create vs Get Property Methods
        for when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateNormalsAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetNormalsAttr() , and also Create vs Get Property Methods for
        when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreatePointsAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetPointsAttr() , and also Create vs Get Property Methods for when
        to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateVelocitiesAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetVelocitiesAttr() , and also Create vs Get Property Methods for
        when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    @staticmethod
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> PointBased:
        """
        Return a UsdGeomPointBased holding the prim adhering to this schema at
        C{path} on C{stage}.


        If no prim exists at C{path} on C{stage}, or if the prim at that path
        does not adhere to this schema, return an invalid schema object. This
        is shorthand for the following: ::

          UsdGeomPointBased(stage->GetPrimAtPath(path));

        """
    def GetAccelerationsAttr(self) -> pxr.Usd.Attribute:
        """
        If provided,'accelerations'should be used with velocities to compute
        positions between samples for the'points'attribute rather than
        interpolating between neighboring'points'samples.


        Acceleration is measured in position units per second-squared. To
        convert to position units per squared UsdTimeCode, divide by the
        square of UsdStage::GetTimeCodesPerSecond() .

        Declaration

        C{vector3f[] accelerations}

        C++ Type

        VtArray<GfVec3f>

        Usd Type

        SdfValueTypeNames->Vector3fArray
        """
    def GetNormalsAttr(self) -> pxr.Usd.Attribute:
        """
        Provide an object-space orientation for individual points, which,
        depending on subclass, may define a surface, curve, or free points.


        Note that'normals'should not be authored on any Mesh that is
        subdivided, since the subdivision algorithm will define its own
        normals.'normals'is not a generic primvar, but the number of elements
        in this attribute will be determined by its'interpolation'. See
        SetNormalsInterpolation() . If'normals'and'primvars:normals'are both
        specified, the latter has precedence.

        Declaration

        C{normal3f[] normals}

        C++ Type

        VtArray<GfVec3f>

        Usd Type

        SdfValueTypeNames->Normal3fArray
        """
    def GetNormalsInterpolation(self) -> str:
        """
        Get the interpolation for the *normals* attribute.


        Although'normals'is not classified as a generic UsdGeomPrimvar (and
        will not be included in the results of
        UsdGeomPrimvarsAPI::GetPrimvars() ) it does require an interpolation
        specification. The fallback interpolation, if left unspecified, is
        UsdGeomTokens->vertex, which will generally produce smooth shading on
        a polygonal mesh. To achieve partial or fully faceted shading of a
        polygonal mesh with normals, one should use UsdGeomTokens->faceVarying
        or UsdGeomTokens->uniform interpolation.
        """
    def GetPointsAttr(self) -> pxr.Usd.Attribute:
        """
        The primary geometry attribute for all PointBased primitives,
        describes points in (local) space.



        Declaration

        C{point3f[] points}

        C++ Type

        VtArray<GfVec3f>

        Usd Type

        SdfValueTypeNames->Point3fArray
        """
    @staticmethod
    def GetSchemaAttributeNames(includeInherited: bool = ...) -> list[str]:
        """
        Return a vector of names of all pre-declared attributes for this
        schema class and all its ancestor classes.


        Does not include attributes that may be authored by custom/extended
        methods of the schemas involved.
        """
    def GetVelocitiesAttr(self) -> pxr.Usd.Attribute:
        """
        If provided,'velocities'should be used by renderers to.


        compute positions between samples for the'points'attribute, rather
        than interpolating between neighboring'points'samples. This is the
        only reasonable means of computing motion blur for topologically
        varying PointBased primitives. It follows that the length of
        each'velocities'sample must match the length of the
        corresponding'points'sample. Velocity is measured in position units
        per second, as per most simulation software. To convert to position
        units per UsdTimeCode, divide by UsdStage::GetTimeCodesPerSecond() .

        See also Applying Timesampled Velocities to Geometry.

        Declaration

        C{vector3f[] velocities}

        C++ Type

        VtArray<GfVec3f>

        Usd Type

        SdfValueTypeNames->Vector3fArray
        """
    def SetNormalsInterpolation(self, interpolation: str | pxr.Ar.ResolvedPath) -> bool:
        """
        Set the interpolation for the *normals* attribute.



        true upon success, false if C{interpolation} is not a legal value as
        defined by UsdGeomPrimvar::IsValidInterpolation() , or if there was a
        problem setting the value. No attempt is made to validate that the
        normals attr's value contains the right number of elements to match
        its interpolation to its prim's topology.

        GetNormalsInterpolation()
        """
    @staticmethod
    def _GetStaticTfType() -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...

class PointInstancer(Boundable):
    '''
    Encodes vectorized instancing of multiple, potentially animated,
    prototypes (object/instance masters), which can be arbitrary
    prims/subtrees on a UsdStage.


    PointInstancer is a"multi instancer", as it allows multiple prototypes
    to be scattered among its"points". We use a UsdRelationship
    *prototypes* to identify and order all of the possible prototypes, by
    targeting the root prim of each prototype. The ordering imparted by
    relationships associates a zero-based integer with each prototype, and
    it is these integers we use to identify the prototype of each
    instance, compactly, and allowing prototypes to be swapped out without
    needing to reauthor all of the per-instance data.

    The PointInstancer schema is designed to scale to billions of
    instances, which motivates the choice to split the per-instance
    transformation into position, (quaternion) orientation, and scales,
    rather than a 4x4 matrix per-instance. In addition to requiring fewer
    bytes even if all elements are authored (32 bytes vs 64 for a single-
    precision 4x4 matrix), we can also be selective about which attributes
    need to animate over time, for substantial data reduction in many
    cases.

    Note that PointInstancer is *not* a Gprim, since it is not a graphical
    primitive by any stretch of the imagination. It *is*, however,
    Boundable, since we will sometimes want to treat the entire
    PointInstancer similarly to a procedural, from the perspective of
    inclusion or framing.

    Varying Instance Identity over Time
    ===================================

    PointInstancers originating from simulations often have the
    characteristic that points/instances are"born", move around for some
    time period, and then die (or leave the area of interest). In such
    cases, billions of instances may be birthed over time, while at any
    *specific* time, only a much smaller number are actually alive. To
    encode this situation efficiently, the simulator may re-use indices in
    the instance arrays, when a particle dies, its index will be taken
    over by a new particle that may be birthed in a much different
    location. This presents challenges both for identity-tracking, and for
    motion-blur.

    We facilitate identity tracking by providing an optional, animatable
    *ids* attribute, that specifies the 64 bit integer ID of the particle
    at each index, at each point in time. If the simulator keeps
    monotonically increasing a particle-count each time a new particle is
    birthed, it will serve perfectly as particle *ids*.

    We facilitate motion blur for varying-topology particle streams by
    optionally allowing per-instance *velocities* and *angularVelocities*
    to be authored. If instance transforms are requested at a time between
    samples and either of the velocity attributes is authored, then we
    will not attempt to interpolate samples of *positions* or
    *orientations*. If not authored, and the bracketing samples have the
    same length, then we will interpolate.

    Computing an Instance Transform
    ===============================

    Each instance\'s transformation is a combination of the SRT affine
    transform described by its scale, orientation, and position, applied
    *after* (i.e. less locally than) the local to parent transformation
    computed at the root of the prototype it is instancing.

    If your processing of prototype geometry naturally takes into account
    the transform of the prototype root, then this term can be omitted
    from the computation of each instance transform, and this can be
    controlled when computing instance transformation matrices using the
    UsdGeomPointInstancer::PrototypeXformInclusion enumeration.

    To understand the computation of the instance transform, in order to
    put an instance of a PointInstancer into the space of the
    PointInstancer\'s parent prim we do the following:

       - Apply (most locally) the authored local to parent transformation
         for *prototypes[protoIndices[i]]*

       - If *scales* is authored, next apply the scaling matrix from
         *scales[i]*

       - If *orientations* is authored: B{if *angularVelocities* is
         authored}, first multiply *orientations[i]* by the unit quaternion
         derived by scaling *angularVelocities[i]* by the time differential
         from the left-bracketing timeSample for *orientation* to the requested
         evaluation time *t*, storing the result in *R*, B{else} assign *R*
         directly from *orientations[i]*. Apply the rotation matrix derived
         from *R*.

       - Apply the translation derived from *positions[i]*. If
         *velocities* is authored, apply the translation deriving from
         *velocities[i]* scaled by the time differential from the left-
         bracketing timeSample for *positions* to the requested evaluation time
         *t*.

       - Least locally, apply the transformation authored on the
         PointInstancer prim itself (or the
         UsdGeomImageable::ComputeLocalToWorldTransform() of the PointInstancer
         to put the instance directly into world space)

    If neither *velocities* nor *angularVelocities* are authored, we
    fallback to standard position and orientation computation logic (using
    linear interpolation between timeSamples) as described by Applying
    Timesampled Velocities to Geometry.

    B{Scaling Velocities for Interpolation}

    When computing time-differentials by which to apply velocity or
    angularVelocity to positions or orientations, we must scale by ( 1.0 /
    UsdStage::GetTimeCodesPerSecond() ), because velocities are recorded
    in units/second, while we are interpolating in UsdTimeCode ordinates.

    We provide both high and low-level API\'s for dealing with the
    transformation as a matrix, both will compute the instance matrices
    using multiple threads; the low-level API allows the client to cache
    unvarying inputs so that they need not be read duplicately when
    computing over time.

    See also Applying Timesampled Velocities to Geometry.

    Primvars on PointInstancer
    ==========================

    Primvars authored on a PointInstancer prim should always be applied to
    each instance with *constant* interpolation at the root of the
    instance. When you are authoring primvars on a PointInstancer, think
    about it as if you were authoring them on a point-cloud (e.g. a
    UsdGeomPoints gprim). The same interpolation rules for points apply
    here, substituting"instance"for"point".

    In other words, the (constant) value extracted for each instance from
    the authored primvar value depends on the authored *interpolation* and
    *elementSize* of the primvar, as follows:
       - B{constant} or B{uniform} : the entire authored value of the
         primvar should be applied exactly to each instance.

       - B{varying}, B{vertex}, or B{faceVarying} : the first
         *elementSize* elements of the authored primvar array should be
         assigned to instance zero, the second *elementSize* elements should be
         assigned to instance one, and so forth.

    Masking Instances:"Deactivating"and Invising
    ============================================

    Often a PointInstancer is created"upstream"in a graphics pipeline, and
    the needs of"downstream"clients necessitate eliminating some of the
    instances from further consideration. Accomplishing this pruning by
    re-authoring all of the per-instance attributes is not very
    attractive, since it may mean destructively editing a large quantity
    of data. We therefore provide means of"masking"instances by ID, such
    that the instance data is unmolested, but per-instance transform and
    primvar data can be retrieved with the no-longer-desired instances
    eliminated from the (smaller) arrays. PointInstancer allows two
    independent means of masking instances by ID, each with different
    features that meet the needs of various clients in a pipeline. Both
    pruning features\'lists of ID\'s are combined to produce the mask
    returned by ComputeMaskAtTime() .

    If a PointInstancer has no authored *ids* attribute, the masking
    features will still be available, with the integers specifying element
    position in the *protoIndices* array rather than ID.

    The first masking feature encodes a list of IDs in a list-editable
    metadatum called *inactiveIds*, which, although it does not have any
    similar impact to stage population as prim activation, it shares with
    that feature that its application is uniform over all time. Because it
    is list-editable, we can *sparsely* add and remove instances from it
    in many layers.

    This sparse application pattern makes *inactiveIds* a good choice when
    further downstream clients may need to reverse masking decisions made
    upstream, in a manner that is robust to many kinds of future changes
    to the upstream data.

    See ActivateId() , ActivateIds() , DeactivateId() , DeactivateIds() ,
    ActivateAllIds()

    The second masking feature encodes a list of IDs in a time-varying
    Int64Array-valued UsdAttribute called *invisibleIds*, since it shares
    with Imageable visibility the ability to animate object visibility.

    Unlike *inactiveIds*, overriding a set of opinions for *invisibleIds*
    is not at all straightforward, because one will, in general need to
    reauthor (in the overriding layer) B{all} timeSamples for the
    attribute just to change one Id\'s visibility state, so it cannot be
    authored sparsely. But it can be a very useful tool for situations
    like encoding pre-computed camera-frustum culling of geometry when
    either or both of the instances or the camera is animated.

    See VisId() , VisIds() , InvisId() , InvisIds() , VisAllIds()

    Processing and Not Processing Prototypes
    ========================================

    Any prim in the scenegraph can be targeted as a prototype by the
    *prototypes* relationship. We do not, however, provide a specific
    mechanism for identifying prototypes as geometry that should not be
    drawn (or processed) in their own, local spaces in the scenegraph. We
    encourage organizing all prototypes as children of the PointInstancer
    prim that consumes them, and pruning"raw"processing and drawing
    traversals when they encounter a PointInstancer prim; this is what the
    UsdGeomBBoxCache and UsdImaging engines do.

    There *is* a pattern one can deploy for organizing the prototypes such
    that they will automatically be skipped by basic
    UsdPrim::GetChildren() or UsdPrimRange traversals. Usd prims each have
    a specifier of"def","over", or"class". The default traversals skip
    over prims that are"pure overs"or classes. So to protect prototypes
    from all generic traversals and processing, place them under a prim
    that is just an"over". For example, ::

      01 def PointInstancer "Crowd_Mid"
      02 {
      03     rel prototypes = [ </Crowd_Mid/Prototypes/MaleThin_Business>, </Crowd_Mid/Prototypes/MaleThin_Casual> ]
      04     
      05     over "Prototypes" 
      06     {
      07          def "MaleThin_Business" (
      08              references = [@MaleGroupA/usd/MaleGroupA.usd@</MaleGroupA>]
      09              variants = {
      10                  string modelingVariant = "Thin"
      11                  string costumeVariant = "BusinessAttire"
      12              }
      13          )
      14          { ... }
      15          
      16          def "MaleThin_Casual"
      17          ...
      18     }
      19 }

    '''

    class MaskApplication(pxr.Tf.Tf_PyEnumWrapper):
        _baseName: ClassVar[str] = ...
        allValues: ClassVar[tuple] = ...
        def __init__(self, *args, **kwargs) -> None:
            """Raises an exception
            This class cannot be instantiated from Python
            """
        @staticmethod
        def GetValueFromName(name: object) -> Any: ...

    class ProtoXformInclusion(pxr.Tf.Tf_PyEnumWrapper):
        _baseName: ClassVar[str] = ...
        allValues: ClassVar[tuple] = ...
        def __init__(self, *args, **kwargs) -> None:
            """Raises an exception
            This class cannot be instantiated from Python
            """
        @staticmethod
        def GetValueFromName(name: object) -> Any: ...
    ApplyMask: ClassVar[PointInstancer.MaskApplication] = ...
    ExcludeProtoXform: ClassVar[PointInstancer.ProtoXformInclusion] = ...
    IgnoreMask: ClassVar[PointInstancer.MaskApplication] = ...
    IncludeProtoXform: ClassVar[PointInstancer.ProtoXformInclusion] = ...
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None:
        """
        Construct a UsdGeomPointInstancer on UsdPrim C{prim}.


        Equivalent to UsdGeomPointInstancer::Get (prim.GetStage(),
        prim.GetPath()) for a *valid* C{prim}, but will not immediately throw
        an error for an invalid C{prim}
        """
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None:
        """
        Construct a UsdGeomPointInstancer on the prim held by C{schemaObj}.


        Should be preferred over UsdGeomPointInstancer (schemaObj.GetPrim()),
        as it preserves SchemaBase state.
        """
    def ActivateAllIds(self) -> bool:
        '''
        Ensure that all instances are active over all time.


        This does not guarantee that the instances will be rendered, because
        each may still be"invisible"due to its presence in the *invisibleIds*
        attribute (see VisId() , InvisId() )
        '''
    def ActivateId(self, id: int) -> bool:
        '''
        Ensure that the instance identified by C{id} is active over all time.


        This activation is encoded sparsely, affecting no other instances.

        This does not guarantee that the instance will be rendered, because it
        may still be"invisible"due to C{id} being present in the
        *invisibleIds* attribute (see VisId() , InvisId() )
        '''
    def ActivateIds(self, ids: pxr.Vt.Int64Array | typing.Iterable[int]) -> bool:
        '''
        Ensure that the instances identified by C{ids} are active over all
        time.


        This activation is encoded sparsely, affecting no other instances.

        This does not guarantee that the instances will be rendered, because
        each may still be"invisible"due to its presence in the *invisibleIds*
        attribute (see VisId() , InvisId() )
        '''
    def ComputeExtentAtTime(self, time: pxr.Usd.TimeCode | float | pxr.Sdf.TimeCode, baseTime: pxr.Usd.TimeCode | float | pxr.Sdf.TimeCode) -> pxr.Vt.Vec3fArray:
        '''
        Compute the extent of the point instancer based on the per-
        instance,"PointInstancer relative"transforms at C{time}, as described
        in Computing an Instance Transform.


        If there is no error, we return C{true} and C{extent} will be the
        tightest bounds we can compute efficiently. If an error occurs,
        C{false} will be returned and C{extent} will be left untouched.

        For now, this uses a UsdGeomBBoxCache with the"default","proxy",
        and"render"purposes.

        extent

        - the out parameter for the extent. On success, it will contain two
        elements representing the min and max. time

        - UsdTimeCode at which we want to evaluate the extent baseTime

        - required for correct interpolation between samples when *velocities*
        or *angularVelocities* are present. If there are samples for
        *positions* and *velocities* at t1 and t2, normal value resolution
        would attempt to interpolate between the two samples, and if they
        could not be interpolated because they differ in size (common in cases
        where velocity is authored), will choose the sample at t1. When
        sampling for the purposes of motion-blur, for example, it is common,
        when rendering the frame at t2, to sample at [ t2-shutter/2,
        t2+shutter/2 ] for a shutter interval of *shutter*. The first sample
        falls between t1 and t2, but we must sample at t2 and apply velocity-
        based interpolation based on those samples to get a correct result. In
        such scenarios, one should provide a C{baseTime} of t2 when querying
        *both* samples. If your application does not care about off-sample
        interpolation, it can supply the same value for C{baseTime} that it
        does for C{time}. When C{baseTime} is less than or equal to C{time},
        we will choose the lower bracketing timeSample.
        '''
    def ComputeExtentAtTimes(self, times: typing.Iterable[pxr.Usd.TimeCode | float | pxr.Sdf.TimeCode], baseTime: pxr.Usd.TimeCode | float | pxr.Sdf.TimeCode) -> list[pxr.Vt.Vec3fArray]:
        """
        Compute the extent of the point instancer as in ComputeExtentAtTime,
        but across multiple C{times}.


        This is equivalent to, but more efficient than, calling
        ComputeExtentAtTime several times. Each element in C{extents} is the
        computed extent at the corresponding time in C{times}.

        As in ComputeExtentAtTime, if there is no error, we return C{true} and
        C{extents} will be the tightest bounds we can compute efficiently. If
        an error occurs computing the extent at any time, C{false} will be
        returned and C{extents} will be left untouched.

        times

        - A vector containing the UsdTimeCodes at which we want to sample.
        """
    def ComputeInstanceTransformsAtTime(self, time: pxr.Usd.TimeCode | float | pxr.Sdf.TimeCode, baseTime: pxr.Usd.TimeCode | float | pxr.Sdf.TimeCode, doProtoXforms: PointInstancer.ProtoXformInclusion = ..., applyMask: PointInstancer.MaskApplication = ...) -> pxr.Vt.Matrix4dArray:
        '''
        Compute the per-instance,"PointInstancer relative"transforms given the
        positions, scales, orientations, velocities and angularVelocities at
        C{time}, as described in Computing an Instance Transform.


        This will return C{false} and leave C{xforms} untouched if:
           - C{xforms} is None

           - one of C{time} and C{baseTime} is numeric and the other is
             UsdTimeCode::Default() (they must either both be numeric or both be
             default)

           - there is no authored *protoIndices* attribute or *positions*
             attribute

           - the size of any of the per-instance attributes does not match the
             size of *protoIndices*

           - C{doProtoXforms} is C{IncludeProtoXform} but an index value in
             *protoIndices* is outside the range [0, prototypes.size())

           - C{applyMask} is C{ApplyMask} and a mask is set but the size of
             the mask does not match the size of *protoIndices*.

        If there is no error, we will return C{true} and C{xforms} will
        contain the computed transformations.

        xforms

        - the out parameter for the transformations. Its size will depend on
        the authored data and C{applyMask} time

        - UsdTimeCode at which we want to evaluate the transforms baseTime

        - required for correct interpolation between samples when *velocities*
        or *angularVelocities* are present. If there are samples for
        *positions* and *velocities* at t1 and t2, normal value resolution
        would attempt to interpolate between the two samples, and if they
        could not be interpolated because they differ in size (common in cases
        where velocity is authored), will choose the sample at t1. When
        sampling for the purposes of motion-blur, for example, it is common,
        when rendering the frame at t2, to sample at [ t2-shutter/2,
        t2+shutter/2 ] for a shutter interval of *shutter*. The first sample
        falls between t1 and t2, but we must sample at t2 and apply velocity-
        based interpolation based on those samples to get a correct result. In
        such scenarios, one should provide a C{baseTime} of t2 when querying
        *both* samples. If your application does not care about off-sample
        interpolation, it can supply the same value for C{baseTime} that it
        does for C{time}. When C{baseTime} is less than or equal to C{time},
        we will choose the lower bracketing timeSample. Selecting sample times
        with respect to baseTime will be performed independently for positions
        and orientations. doProtoXforms

        - specifies whether to include the root transformation of each
        instance\'s prototype in the instance\'s transform. Default is to
        include it, but some clients may want to apply the proto transform as
        part of the prototype itself, so they can specify C{ExcludeProtoXform}
        instead. applyMask

        - specifies whether to apply ApplyMaskToArray() to the computed
        result. The default is C{ApplyMask}.
        '''
    def ComputeInstanceTransformsAtTimes(self, times: typing.Iterable[pxr.Usd.TimeCode | float | pxr.Sdf.TimeCode], baseTime: pxr.Usd.TimeCode | float | pxr.Sdf.TimeCode, doProtoXforms: PointInstancer.ProtoXformInclusion = ..., applyMask: PointInstancer.MaskApplication = ...) -> list[list[pxr.Gf.Matrix4d]]:
        """
        Compute the per-instance transforms as in
        ComputeInstanceTransformsAtTime, but using multiple sample times.


        An array of matrix arrays is returned where each matrix array contains
        the instance transforms for the corresponding time in C{times}.

        times

        - A vector containing the UsdTimeCodes at which we want to sample.
        """
    def ComputeMaskAtTime(self, time: pxr.Usd.TimeCode | float | pxr.Sdf.TimeCode) -> list:
        '''
        Computes a presence mask to be applied to per-instance data arrays
        based on authored *inactiveIds*, *invisibleIds*, and *ids*.


        If no *ids* attribute has been authored, then the values in
        *inactiveIds* and *invisibleIds* will be interpreted directly as
        indices of *protoIndices*.

        If C{ids} is non-None, it is assumed to be the id-mapping to apply,
        and must match the length of *protoIndices* at C{time}. If None, we
        will call GetIdsAttr() .Get(time)

        If all"live"instances at UsdTimeCode C{time} pass the mask, we will
        return an B{empty} mask so that clients can trivially recognize the
        common"no masking"case. The returned mask can be used with
        ApplyMaskToArray() , and will contain a C{true} value for every
        element that should survive.
        '''
    def CreateAccelerationsAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetAccelerationsAttr() , and also Create vs Get Property Methods
        for when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateAngularVelocitiesAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetAngularVelocitiesAttr() , and also Create vs Get Property
        Methods for when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateIdsAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetIdsAttr() , and also Create vs Get Property Methods for when to
        use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateInvisibleIdsAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetInvisibleIdsAttr() , and also Create vs Get Property Methods
        for when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateOrientationsAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetOrientationsAttr() , and also Create vs Get Property Methods
        for when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateOrientationsfAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetOrientationsfAttr() , and also Create vs Get Property Methods
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
    def CreateProtoIndicesAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetProtoIndicesAttr() , and also Create vs Get Property Methods
        for when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreatePrototypesRel(self) -> pxr.Usd.Relationship:
        """
        See GetPrototypesRel() , and also Create vs Get Property Methods for
        when to use Get vs Create.
        """
    def CreateScalesAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetScalesAttr() , and also Create vs Get Property Methods for when
        to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateVelocitiesAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetVelocitiesAttr() , and also Create vs Get Property Methods for
        when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def DeactivateId(self, id: int) -> bool:
        """
        Ensure that the instance identified by C{id} is inactive over all
        time.


        This deactivation is encoded sparsely, affecting no other instances.

        A deactivated instance is guaranteed not to render if the renderer
        honors masking.
        """
    def DeactivateIds(self, ids: pxr.Vt.Int64Array | typing.Iterable[int]) -> bool:
        """
        Ensure that the instances identified by C{ids} are inactive over all
        time.


        This deactivation is encoded sparsely, affecting no other instances.

        A deactivated instance is guaranteed not to render if the renderer
        honors masking.
        """
    @staticmethod
    def Define(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> PointInstancer:
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
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> PointInstancer:
        """
        Return a UsdGeomPointInstancer holding the prim adhering to this
        schema at C{path} on C{stage}.


        If no prim exists at C{path} on C{stage}, or if the prim at that path
        does not adhere to this schema, return an invalid schema object. This
        is shorthand for the following: ::

          UsdGeomPointInstancer(stage->GetPrimAtPath(path));

        """
    def GetAccelerationsAttr(self) -> pxr.Usd.Attribute:
        """
        If authored, per-instance'accelerations'will be used with velocities
        to compute positions between samples for the'positions'attribute
        rather than interpolating between neighboring'positions'samples.


        Acceleration is measured in position units per second-squared. To
        convert to position units per squared UsdTimeCode, divide by the
        square of UsdStage::GetTimeCodesPerSecond() .

        Declaration

        C{vector3f[] accelerations}

        C++ Type

        VtArray<GfVec3f>

        Usd Type

        SdfValueTypeNames->Vector3fArray
        """
    def GetAngularVelocitiesAttr(self) -> pxr.Usd.Attribute:
        """
        If authored, per-instance angular velocity vector to be used for
        interoplating orientations.


        Angular velocities should be considered mandatory if both
        *protoIndices* and *orientations* are animated. Angular velocity is
        measured in B{degrees} per second. To convert to degrees per
        UsdTimeCode, divide by UsdStage::GetTimeCodesPerSecond() .

        See also Computing an Instance Transform.

        Declaration

        C{vector3f[] angularVelocities}

        C++ Type

        VtArray<GfVec3f>

        Usd Type

        SdfValueTypeNames->Vector3fArray
        """
    def GetIdsAttr(self) -> pxr.Usd.Attribute:
        """
        Ids are optional; if authored, the ids array should be the same length
        as the *protoIndices* array, specifying (at each timeSample if
        instance identities are changing) the id of each instance.


        The type is signed intentionally, so that clients can encode some
        binary state on Id'd instances without adding a separate primvar. See
        also Varying Instance Identity over Time

        Declaration

        C{int64[] ids}

        C++ Type

        VtArray<int64_t>

        Usd Type

        SdfValueTypeNames->Int64Array
        """
    def GetInstanceCount(self, timeCode: pxr.Usd.TimeCode | float | pxr.Sdf.TimeCode = ...) -> int:
        """
        Returns the number of instances as defined by the size of the
        *protoIndices* array at *timeCode*.



        For most code, this check will be performant. When using file formats
        where the cost of attribute reading is high and the time sampled array
        will be read into memory later, it may be better to explicitly read
        the value once and check the size of the array directly.

        GetProtoIndicesAttr()
        """
    def GetInvisibleIdsAttr(self) -> pxr.Usd.Attribute:
        """
        A list of id's to make invisible at the evaluation time.


        See invisibleIds: Animatable Masking.

        Declaration

        C{int64[] invisibleIds = []}

        C++ Type

        VtArray<int64_t>

        Usd Type

        SdfValueTypeNames->Int64Array
        """
    def GetOrientationsAttr(self) -> pxr.Usd.Attribute:
        '''
        If authored, per-instance orientation of each instance about its
        prototype\'s origin, represented as a unit length quaternion, which
        allows us to encode it with sufficient precision in a compact GfQuath.


        It is client\'s responsibility to ensure that authored quaternions are
        unit length; the convenience API below for authoring orientations from
        rotation matrices will ensure that quaternions are unit length, though
        it will not make any attempt to select the"better (for
        interpolationwith respect to neighboring samples)"of the two possible
        quaternions that encode the rotation.

        See also Computing an Instance Transform.

        Declaration

        C{quath[] orientations}

        C++ Type

        VtArray<GfQuath>

        Usd Type

        SdfValueTypeNames->QuathArray
        '''
    def GetOrientationsfAttr(self) -> pxr.Usd.Attribute:
        '''
        If authored, per-instance orientation of each instance about its
        prototype\'s origin, represented as a unit length quaternion, encoded
        as a GfQuatf to support higher precision computations.


        It is client\'s responsibility to ensure that authored quaternions are
        unit length; the convenience API below for authoring orientations from
        rotation matrices will ensure that quaternions are unit length, though
        it will not make any attempt to select the"better (for
        interpolationwith respect to neighboring samples)"of the two possible
        quaternions that encode the rotation. Note that if the earliest time
        sample (or default value if there are no time samples) of
        orientationsf is not empty orientationsf will be preferred over
        orientations if both are authored.

        See also Computing an Instance Transform.

        Declaration

        C{quatf[] orientationsf}

        C++ Type

        VtArray<GfQuatf>

        Usd Type

        SdfValueTypeNames->QuatfArray
        '''
    def GetPositionsAttr(self) -> pxr.Usd.Attribute:
        """
        B{Required property}.


        Per-instance position. See also Computing an Instance Transform.

        Declaration

        C{point3f[] positions}

        C++ Type

        VtArray<GfVec3f>

        Usd Type

        SdfValueTypeNames->Point3fArray
        """
    def GetProtoIndicesAttr(self) -> pxr.Usd.Attribute:
        """
        B{Required property}.


        Per-instance index into *prototypes* relationship that identifies what
        geometry should be drawn for each instance. B{Topology attribute} -
        can be animated, but at a potential performance impact for streaming.

        Declaration

        C{int[] protoIndices}

        C++ Type

        VtArray<int>

        Usd Type

        SdfValueTypeNames->IntArray
        """
    def GetPrototypesRel(self) -> pxr.Usd.Relationship:
        """
        B{Required property}.


        Orders and targets the prototype root prims, which can be located
        anywhere in the scenegraph that is convenient, although we promote
        organizing prototypes as children of the PointInstancer. The position
        of a prototype in this relationship defines the value an instance
        would specify in the *protoIndices* attribute to instance that
        prototype. Since relationships are uniform, this property cannot be
        animated.
        """
    def GetScalesAttr(self) -> pxr.Usd.Attribute:
        """
        If authored, per-instance scale to be applied to each instance, before
        any rotation is applied.


        See also Computing an Instance Transform.

        Declaration

        C{float3[] scales}

        C++ Type

        VtArray<GfVec3f>

        Usd Type

        SdfValueTypeNames->Float3Array
        """
    @staticmethod
    def GetSchemaAttributeNames(includeInherited: bool = ...) -> list[str]:
        """
        Return a vector of names of all pre-declared attributes for this
        schema class and all its ancestor classes.


        Does not include attributes that may be authored by custom/extended
        methods of the schemas involved.
        """
    def GetVelocitiesAttr(self) -> pxr.Usd.Attribute:
        """
        If provided, per-instance'velocities'will be used to compute positions
        between samples for the'positions'attribute, rather than interpolating
        between neighboring'positions'samples.


        Velocities should be considered mandatory if both *protoIndices* and
        *positions* are animated. Velocity is measured in position units per
        second, as per most simulation software. To convert to position units
        per UsdTimeCode, divide by UsdStage::GetTimeCodesPerSecond() .

        See also Computing an Instance Transform, Applying Timesampled
        Velocities to Geometry.

        Declaration

        C{vector3f[] velocities}

        C++ Type

        VtArray<GfVec3f>

        Usd Type

        SdfValueTypeNames->Vector3fArray
        """
    def InvisId(self, id: int, time: pxr.Usd.TimeCode | float | pxr.Sdf.TimeCode) -> bool:
        """
        Ensure that the instance identified by C{id} is invisible at C{time}.


        This will cause *invisibleIds* to first be broken down (keyed) at
        C{time}, causing all animation in weaker layers that the current
        UsdEditTarget to be overridden. Has no effect on any timeSamples other
        than the one at C{time}.

        An invised instance is guaranteed not to render if the renderer honors
        masking.
        """
    def InvisIds(self, ids: pxr.Vt.Int64Array | typing.Iterable[int], time: pxr.Usd.TimeCode | float | pxr.Sdf.TimeCode) -> bool:
        """
        Ensure that the instances identified by C{ids} are invisible at
        C{time}.


        This will cause *invisibleIds* to first be broken down (keyed) at
        C{time}, causing all animation in weaker layers that the current
        UsdEditTarget to be overridden. Has no effect on any timeSamples other
        than the one at C{time}.

        An invised instance is guaranteed not to render if the renderer honors
        masking.
        """
    def VisAllIds(self, time: pxr.Usd.TimeCode | float | pxr.Sdf.TimeCode) -> bool:
        '''
        Ensure that all instances are visible at C{time}.


        Operates by authoring an empty array at C{time}.

        This does not guarantee that the instances will be rendered, because
        each may still be"inactive"due to its id being present in the
        *inactivevIds* metadata (see ActivateId() , DeactivateId() )
        '''
    def VisId(self, id: int, time: pxr.Usd.TimeCode | float | pxr.Sdf.TimeCode) -> bool:
        '''
        Ensure that the instance identified by C{id} is visible at C{time}.


        This will cause *invisibleIds* to first be broken down (keyed) at
        C{time}, causing all animation in weaker layers that the current
        UsdEditTarget to be overridden. Has no effect on any timeSamples other
        than the one at C{time}. If the *invisibleIds* attribute is not
        authored or is blocked, this operation is a no-op.

        This does not guarantee that the instance will be rendered, because it
        may still be"inactive"due to C{id} being present in the *inactivevIds*
        metadata (see ActivateId() , DeactivateId() )
        '''
    def VisIds(self, ids: pxr.Vt.Int64Array | typing.Iterable[int], time: pxr.Usd.TimeCode | float | pxr.Sdf.TimeCode) -> bool:
        '''
        Ensure that the instances identified by C{ids} are visible at C{time}.


        This will cause *invisibleIds* to first be broken down (keyed) at
        C{time}, causing all animation in weaker layers that the current
        UsdEditTarget to be overridden. Has no effect on any timeSamples other
        than the one at C{time}. If the *invisibleIds* attribute is not
        authored or is blocked, this operation is a no-op.

        This does not guarantee that the instances will be rendered, because
        each may still be"inactive"due to C{id} being present in the
        *inactivevIds* metadata (see ActivateId() , DeactivateId() )
        '''
    @staticmethod
    def _GetStaticTfType() -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...

class Points(PointBased):
    """
    Points are analogous to the RiPoints spec.



    Points can be an efficient means of storing and rendering particle
    effects comprised of thousands or millions of small particles. Points
    generally receive a single shading sample each, which should take
    *normals* into account, if present.

    While not technically UsdGeomPrimvars, the widths and normals also
    have interpolation metadata. It's common for authored widths and
    normals to have constant or varying interpolation.
    """
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None:
        """
        Construct a UsdGeomPoints on UsdPrim C{prim}.


        Equivalent to UsdGeomPoints::Get (prim.GetStage(), prim.GetPath()) for
        a *valid* C{prim}, but will not immediately throw an error for an
        invalid C{prim}
        """
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None:
        """
        Construct a UsdGeomPoints on the prim held by C{schemaObj}.


        Should be preferred over UsdGeomPoints (schemaObj.GetPrim()), as it
        preserves SchemaBase state.
        """
    @staticmethod
    def ComputeExtent(points: pxr.Vt.Vec3fArray | typing.Iterable[list[float]] | typing.Iterable[pxr.Gf.Vec3f] | typing.Iterable[tuple[float, float, float]], widths: pxr.Vt.FloatArray | typing.Iterable[float]) -> pxr.Vt.Vec3fArray:
        """
        Compute the extent for the point cloud defined by points and widths.



        true upon success, false if widths and points are different sized
        arrays. On success, extent will contain the axis-aligned bounding box
        of the point cloud defined by points with the given widths.

        This function is to provide easy authoring of extent for usd authoring
        tools, hence it is static and acts outside a specific prim (as in
        attribute based methods).
        """
    def CreateIdsAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetIdsAttr() , and also Create vs Get Property Methods for when to
        use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateWidthsAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetWidthsAttr() , and also Create vs Get Property Methods for when
        to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    @staticmethod
    def Define(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> Points:
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
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> Points:
        """
        Return a UsdGeomPoints holding the prim adhering to this schema at
        C{path} on C{stage}.


        If no prim exists at C{path} on C{stage}, or if the prim at that path
        does not adhere to this schema, return an invalid schema object. This
        is shorthand for the following: ::

          UsdGeomPoints(stage->GetPrimAtPath(path));

        """
    def GetIdsAttr(self) -> pxr.Usd.Attribute:
        """
        Ids are optional; if authored, the ids array should be the same length
        as the points array, specifying (at each timesample if point
        identities are changing) the id of each point.


        The type is signed intentionally, so that clients can encode some
        binary state on Id'd points without adding a separate primvar.

        Declaration

        C{int64[] ids}

        C++ Type

        VtArray<int64_t>

        Usd Type

        SdfValueTypeNames->Int64Array
        """
    def GetPointCount(self, timeCode: pxr.Usd.TimeCode | float | pxr.Sdf.TimeCode = ...) -> int:
        """
        Returns the number of points as defined by the size of the *points*
        array at *timeCode*.



        For most code, this check will be performant. When using file formats
        where the cost of attribute reading is high and the time sampled array
        will be read into memory later, it may be better to explicitly read
        the value once and check the size of the array directly.

        GetPointsAttr()
        """
    @staticmethod
    def GetSchemaAttributeNames(includeInherited: bool = ...) -> list[str]:
        """
        Return a vector of names of all pre-declared attributes for this
        schema class and all its ancestor classes.


        Does not include attributes that may be authored by custom/extended
        methods of the schemas involved.
        """
    def GetWidthsAttr(self) -> pxr.Usd.Attribute:
        """
        Widths are defined as the *diameter* of the points, in object space.


        'widths'is not a generic Primvar, but the number of elements in this
        attribute will be determined by its'interpolation'. See
        SetWidthsInterpolation() . If'widths'and'primvars:widths'are both
        specified, the latter has precedence.

        Declaration

        C{float[] widths}

        C++ Type

        VtArray<float>

        Usd Type

        SdfValueTypeNames->FloatArray
        """
    def GetWidthsInterpolation(self) -> str:
        """
        Get the interpolation for the *widths* attribute.


        Although'widths'is not classified as a generic UsdGeomPrimvar (and
        will not be included in the results of
        UsdGeomPrimvarsAPI::GetPrimvars() ) it does require an interpolation
        specification. The fallback interpolation, if left unspecified, is
        UsdGeomTokens->vertex, which means a width value is specified for each
        point.
        """
    def SetWidthsInterpolation(self, interpolation: str | pxr.Ar.ResolvedPath) -> bool:
        """
        Set the interpolation for the *widths* attribute.



        true upon success, false if C{interpolation} is not a legal value as
        defined by UsdPrimvar::IsValidInterpolation(), or if there was a
        problem setting the value. No attempt is made to validate that the
        widths attr's value contains the right number of elements to match its
        interpolation to its prim's topology.

        GetWidthsInterpolation()
        """
    @staticmethod
    def _GetStaticTfType() -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...

class Primvar(Boost.Python.instance):
    '''
    Schema wrapper for UsdAttribute for authoring and introspecting
    attributes that are primvars.


    UsdGeomPrimvar provides API for authoring and retrieving the
    additional data required to encode an attribute as a"Primvar", which
    is a convenient contraction of RenderMan\'s"Primitive Variable"concept,
    which is represented in Alembic as"arbitrary geometry
    parameters"(arbGeomParams).

    This includes the attribute\'s interpolation across the primitive
    (which RenderMan refers to as its class specifier and Alembic as its
    "geometry scope" ); it also includes the attribute\'s elementSize,
    which states how many values in the value array must be aggregated for
    each element on the primitive. An attribute\'s TypeName also factors
    into the encoding of Primvar.

    What is the Purpose of a Primvar?
    =================================

    There are three key aspects of Primvar identity:
       - Primvars define a value that can vary across the primitive on
         which they are defined, via prescribed interpolation rules

       - Taken collectively on a prim, its Primvars describe the"per-
         primitiveoverrides"to the material to which the prim is bound.
         Different renderers may communicate the variables to the shaders using
         different mechanisms over which Usd has no control; Primvars simply
         provide the classification that any renderer should use to locate
         potential overrides. Do please note that primvars override parameters
         on UsdShadeShader objects, *not* Interface Attributes on
         UsdShadeMaterial prims.

       - *Primvars inherit down scene namespace.* Regular USD attributes
         only apply to the prim on which they are specified, but primvars
         implicitly also apply to any child prims, unless those child prims
         have their own opinions about those primvars. This capability
         necessarily entails added cost to check for inherited values, but the
         benefit is that it allows concise encoding of certain opinions that
         broadly affect large amounts of geometry. See
         UsdGeomImageable::FindInheritedPrimvars().

    Creating and Accessing Primvars
    ===============================

    The UsdGeomPrimvarsAPI schema provides a complete interface for
    creating and querying prims for primvars.

    The B{only} way to create a new Primvar in scene description is by
    calling UsdGeomPrimvarsAPI::CreatePrimvar() . One
    cannot"enhance"or"promote"an already existing attribute into a
    Primvar, because doing so may require a namespace edit to rename the
    attribute, which cannot, in general, be done within a single
    UsdEditContext. Instead, create a new UsdGeomPrimvar of the desired
    name using UsdGeomPrimvarsAPI::CreatePrimvar() , and then copy the
    existing attribute onto the new UsdGeomPrimvar.

    Primvar names can contain arbitrary sub-namespaces. The behavior of
    UsdGeomImageable::GetPrimvar(TfToken const & name) is to
    prepend"primvars:"onto\'name\'if it is not already a prefix, and return
    the result, which means we do not have any ambiguity between the
    primvars"primvars:nsA:foo"and"primvars:nsB:foo". B{There are reserved
    keywords that may not be used as the base names of primvars,} and
    attempting to create Primvars of these names will result in a coding
    error. The reserved keywords are tokens the Primvar uses internally to
    encode various features, such as the"indices"keyword used by Indexed
    Primvars.

    If a client wishes to access an already-extant attribute as a Primvar,
    (which may or may not actually be valid Primvar), they can use the
    speculative constructor; typically, a primvar is only"interesting"if
    it additionally provides a value. This might look like: ::

      UsdGeomPrimvar primvar = UsdGeomPrimvar(usdAttr);
      if (primvar.HasValue()) {
          VtValue values;
          primvar.Get(&values, timeCode);
          TfToken interpolation = primvar.GetInterpolation();
          int     elementSize = primvar.GetElementSize();
          ...
      }

    or, because Get() returns C{true} if and only if it found a value: ::

      UsdGeomPrimvar primvar = UsdGeomPrimvar(usdAttr);
      VtValue values;
      if (primvar.Get(&values, timeCode)) {
          TfToken interpolation = primvar.GetInterpolation();
          int     elementSize = primvar.GetElementSize();
          ...
      }

    As discussed in greater detail in Indexed Primvars, primvars can
    optionally contain a (possibly time-varying) indexing attribute that
    establishes a sharing topology for elements of the primvar. Consumers
    can always chose to ignore the possibility of indexed data by
    exclusively using the ComputeFlattened() API. If a client wishes to
    preserve indexing in their processing of a primvar, we suggest a
    pattern like the following, which accounts for the fact that a
    stronger layer can block a primvar\'s indexing from a weaker layer, via
    UsdGeomPrimvar::BlockIndices() : ::

      VtValue values;
      VtIntArray indices;
  
      if (primvar.Get(&values, timeCode)){
          if (primvar.GetIndices(&indices, timeCode)){
              // primvar is indexed: validate/process values and indices together
          }
          else {
              // primvar is not indexed: validate/process values as flat array
          }
      }

    UsdGeomPrimvar presents a small slice of the UsdAttribute API - enough
    to extract the data that comprises the"Declaration info", and get/set
    of the attribute value. A UsdGeomPrimvar also auto-converts to
    UsdAttribute, so you can pass a UsdGeomPrimvar to any function that
    accepts a UsdAttribute or const-ref thereto.

    Primvar Allowed Scene Description Types and Plurality
    =====================================================

    There are no limitations imposed on the allowable scene description
    types for Primvars; it is the responsibility of each consuming client
    to perform renderer-specific conversions, if need be (the USD
    distribution will include reference RenderMan conversion utilities).

    A note about type plurality of Primvars: It is legitimate for a
    Primvar to be of scalar or array type, and again, consuming clients
    must be prepared to accommodate both. However, while it is not
    possible, in all cases, for USD to *prevent* one from *changing* the
    type of an attribute in different layers or variants of an asset, it
    is never a good idea to do so. This is relevant because, except in a
    few special cases, it is not possible to encode an *interpolation* of
    any value greater than *constant* without providing multiple (i.e.
    array) data values. Therefore, if there is any possibility that
    downstream clients might need to change a Primvar\'s interpolation, the
    Primvar-creator should encode it as an array rather than a scalar.

    Why allow scalar values at all, then? First, sometimes it brings
    clarity to (use of) a shader\'s API to acknowledge that some parameters
    are meant to be single-valued over a shaded primitive. Second, many
    DCC\'s provide far richer affordances for editing scalars than they do
    array values, and we feel it is safer to let the content creator make
    the decision/tradeoff of which kind of flexibility is more relevant,
    rather than leaving it to an importer/exporter pair to interpret.

    Also, like all attributes, Primvars can be time-sampled, and values
    can be authored and consumed just as any other attribute. There is
    currently no validation that the length of value arrays matches to the
    size required by a gprim\'s topology, interpolation, and elementSize.

    For consumer convenience, we provide GetDeclarationInfo() , which
    returns all the type information (other than topology) needed to
    compute the required array size, which is also all the information
    required to prepare the Primvar\'s value for consumption by a renderer.

    Lifetime Management and Primvar Validity
    ========================================

    UsdGeomPrimvar has an explicit bool operator that validates that the
    attribute IsDefined() and thus valid for querying and authoring values
    and metadata. This is a fairly expensive query that we do B{not}
    cache, so if client code retains UsdGeomPrimvar objects, it should
    manage its object validity closely, for performance. An ideal pattern
    is to listen for UsdNotice::StageContentsChanged notifications, and
    revalidate/refetch its retained UsdGeomPrimvar s only then, and
    otherwise use them without validity checking.

    Interpolation of Geometric Primitive Variables
    ==============================================

    In the following explanation of the meaning of the various
    kinds/levels of Primvar interpolation, each bolded bullet gives the
    name of the token in UsdGeomTokens that provides the value. So to set
    a Primvar\'s interpolation to"varying", one would: ::

      primvar.SetInterpolation(UsdGeomTokens->varying);

    Reprinted and adapted from the RPS documentation, which contains
    further details, *interpolation* describes how the Primvar will be
    interpolated over the uv parameter space of a surface primitive (or
    curve or pointcloud). The possible values are:
       - B{constant} One value remains constant over the entire surface
         primitive.

       - B{uniform} One value remains constant for each uv patch segment
         of the surface primitive (which is a *face* for meshes).

       - B{varying} Four values are interpolated over each uv patch
         segment of the surface. Bilinear interpolation is used for
         interpolation between the four values.

       - B{vertex} Values are interpolated between each vertex in the
         surface primitive. The basis function of the surface is used for
         interpolation between vertices.

       - B{faceVarying} For polygons and subdivision surfaces, four values
         are interpolated over each face of the mesh. Bilinear interpolation is
         used for interpolation between the four values.

    UsdGeomPrimvar As Example of Attribute Schema
    =============================================

    Just as UsdSchemaBase and its subclasses provide the pattern for how
    to layer schema onto the generic UsdPrim object, UsdGeomPrimvar
    provides an example of how to layer schema onto a generic UsdAttribute
    object. In both cases, the schema object wraps and contains the
    UsdObject.

    Primvar Namespace Inheritance
    =============================

    Constant interpolation primvar values can be inherited down namespace.
    That is, a primvar value set on a prim will also apply to any child
    prims, unless those children have their own opinions about those named
    primvars. For complete details on how primvars inherit, see
    usdGeom_PrimvarInheritance.

    UsdGeomImageable::FindInheritablePrimvars().
    '''
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, attr: pxr.Usd.Attribute | ConstraintTarget | Primvar | XformOp | pxr.UsdShade.Input | pxr.UsdShade.Output) -> None:
        """
        Speculative constructor that will produce a valid UsdGeomPrimvar when
        C{attr} already represents an attribute that is Primvar, and produces
        an *invalid* Primvar otherwise (i.e.


        operator bool() will return false).

        Calling C{UsdGeomPrimvar::IsPrimvar(attr)} will return the same truth
        value as this constructor, but if you plan to subsequently use the
        Primvar anyways, just use this constructor, as demonstrated in the
        class documentation.
        """
    def BlockIndices(self) -> None:
        """
        Block the indices that were previously set.


        This effectively makes an indexed primvar no longer indexed. This is
        useful when overriding an existing primvar.
        """
    def ComputeFlattened(self, time: pxr.Usd.TimeCode | float | pxr.Sdf.TimeCode = ...) -> Any: ...
    def CreateIndicesAttr(self) -> pxr.Usd.Attribute:
        """
        Returns the existing indices attribute if the primvar is indexed or
        creates a new one.
        """
    def Get(self, time: pxr.Usd.TimeCode | float | pxr.Sdf.TimeCode = ...) -> Any:
        """
        Get the attribute value of the Primvar at C{time}.



        Usd_Handling_Indexed_Primvars for proper handling of indexed primvars
        """
    def GetAttr(self) -> pxr.Usd.Attribute:
        """
        Explicit UsdAttribute extractor.
        """
    def GetBaseName(self) -> str:
        """

        UsdAttribute::GetBaseName()
        """
    def GetDeclarationInfo(self) -> tuple:
        '''
        Convenience function for fetching all information required to properly
        declare this Primvar.


        The C{name} returned is the"client name", stripped of
        the"primvars"namespace, i.e. equivalent to GetPrimvarName()

        May also be more efficient than querying key individually.
        '''
    def GetElementSize(self) -> int:
        '''
        Return the"element size"for this Primvar, which is 1 if unauthored.


        If this Primvar\'s type is *not* an array type, (e.g."Vec3f[]"), then
        elementSize is irrelevant.

        ElementSize does *not* generally encode the length of an array-type
        primvar, and rarely needs to be authored. ElementSize can be thought
        of as a way to create an"aggregate interpolatable type", by dictating
        how many consecutive elements in the value array should be taken as an
        atomic element to be interpolated over a gprim.

        For example, spherical harmonics are often represented as a collection
        of nine floating-point coefficients, and the coefficients need to be
        sampled across a gprim\'s surface: a perfect case for primvars.
        However, USD has no C{float9} datatype. But we can communicate the
        aggregation of nine floats successfully to renderers by declaring a
        simple float-array valued primvar, and setting its *elementSize* to 9.
        To author a *uniform* spherical harmonic primvar on a Mesh of 42
        faces, the primvar\'s array value would contain 9*42 = 378 float
        elements.
        '''
    def GetIndices(self, time: pxr.Usd.TimeCode | float | pxr.Sdf.TimeCode = ...) -> pxr.Vt.IntArray:
        '''
        Returns the value of the indices array associated with the indexed
        primvar at C{time}.



        SetIndices() , Proper Client Handling of"Indexed"Primvars
        '''
    def GetIndicesAttr(self) -> pxr.Usd.Attribute:
        """
        Returns a valid indices attribute if the primvar is indexed.


        Returns an invalid attribute otherwise.
        """
    def GetInterpolation(self) -> str:
        """
        Return the Primvar's interpolation, which is UsdGeomTokens->constant
        if unauthored.


        Interpolation determines how the Primvar interpolates over a geometric
        primitive. See Interpolation of Geometric Primitive Variables
        """
    def GetName(self) -> str:
        """

        UsdAttribute::GetName()
        """
    def GetNamespace(self) -> str:
        """

        UsdAttribute::GetNamespace()
        """
    def GetPrimvarName(self) -> str:
        '''
        Returns the primvar\'s name, devoid of the"primvars:"namespace.


        This is the name by which clients should refer to the primvar, if not
        by its full attribute name - i.e. they should B{not}, in general, use
        GetBaseName() . In the error condition in which this Primvar object is
        not backed by a properly namespaced UsdAttribute, return an empty
        TfToken.
        '''
    def GetTimeSamples(self) -> list[float]:
        '''
        Populates a vector with authored sample times for this primvar.


        Returns false on error.

        This considers any timeSamples authored on the
        associated"indices"attribute if the primvar is indexed.

        UsdAttribute::GetTimeSamples
        '''
    def GetTimeSamplesInInterval(self, _interval: pxr.Gf.Interval, /) -> list[float]:
        '''
        Populates a vector with authored sample times in C{interval}.


        This considers any timeSamples authored on the
        associated"indices"attribute if the primvar is indexed.

        UsdAttribute::GetTimeSamplesInInterval
        '''
    def GetTypeName(self) -> pxr.Sdf.ValueTypeName:
        """

        UsdAttribute::GetTypeName()
        """
    def GetUnauthoredValuesIndex(self) -> int:
        """
        Returns the index that represents unauthored values in the indices
        array.



        SetUnauthoredValuesIndex()
        """
    def HasAuthoredElementSize(self) -> bool:
        """
        Has elementSize been explicitly authored on this Primvar?



        GetElementSize()
        """
    def HasAuthoredInterpolation(self) -> bool:
        """
        Has interpolation been explicitly authored on this Primvar?



        GetInterpolationSize()
        """
    def HasAuthoredValue(self) -> bool:
        """
        Return true if the underlying attribute has an unblocked, authored
        value.
        """
    def HasValue(self) -> bool:
        """
        Return true if the underlying attribute has a value, either from
        authored scene description or a fallback.
        """
    def IsDefined(self) -> bool:
        """
        Return true if the underlying UsdAttribute::IsDefined() , and in
        addition the attribute is identified as a Primvar.


        Does not imply that the primvar provides a value
        """
    def IsIdTarget(self) -> bool:
        """
        Returns true if the primvar is an Id primvar.



        UsdGeomPrimvar_Id_primvars
        """
    def IsIndexed(self) -> bool:
        '''
        Returns true if the primvar is indexed, i.e., if it has an
        associated"indices"attribute.


        If you are going to query the indices anyways, prefer to simply
        consult the return-value of GetIndices() , which will be more
        efficient.
        '''
    @staticmethod
    def IsPrimvar(attr: pxr.Usd.Attribute | ConstraintTarget | Primvar | XformOp | pxr.UsdShade.Input | pxr.UsdShade.Output) -> bool:
        """
        Test whether a given UsdAttribute represents valid Primvar, which
        implies that creating a UsdGeomPrimvar from the attribute will
        succeed.


        Success implies that C{attr.IsDefined()} is true.
        """
    @staticmethod
    def IsValidInterpolation(interpolation: str | pxr.Ar.ResolvedPath) -> bool:
        """
        Validate that the provided C{interpolation} is a valid setting for
        interpolation as defined by Interpolation of Geometric Primitive
        Variables.


        """
    @staticmethod
    def IsValidPrimvarName(name: str | pxr.Ar.ResolvedPath) -> bool:
        """
        Test whether a given C{name} represents a valid name of a primvar,
        which implies that creating a UsdGeomPrimvar with the given name will
        succeed.
        """
    def NameContainsNamespaces(self) -> bool:
        '''
        Does this primvar contain any namespaces other than
        the"primvars:"namespace?


        Some clients may only wish to consume primvars that have no extra
        namespaces in their names, for ease of translating to other systems
        that do not allow namespaces.
        '''
    def Set(self, value: Any, time: pxr.Usd.TimeCode | float | pxr.Sdf.TimeCode = ...) -> bool:
        """
        Set the attribute value of the Primvar at C{time}.
        """
    def SetElementSize(self, eltSize: int) -> bool:
        """
        Set the elementSize for this Primvar.


        Errors and returns false if C{eltSize} less than 1.

        GetElementSize()
        """
    def SetIdTarget(self, _path: pxr.Sdf.Path | str, /) -> bool:
        """
        This primvar must be of String or StringArray type for this method to
        succeed.


        If not, a coding error is raised.

        UsdGeomPrimvar_Id_primvars
        """
    def SetIndices(self, indices: pxr.Vt.IntArray | typing.Iterable[int], time: pxr.Usd.TimeCode | float | pxr.Sdf.TimeCode = ...) -> bool:
        '''
        Sets the indices value of the indexed primvar at C{time}.


        The values in the indices array must be valid indices into the
        authored array returned by Get() . The element numerality of the
        primvar\'s\'interpolation\'metadata applies to the"indices"array, not the
        attribute value array (returned by Get() ).
        '''
    def SetInterpolation(self, interpolation: str | pxr.Ar.ResolvedPath) -> bool:
        """
        Set the Primvar's interpolation.


        Errors and returns false if C{interpolation} is out of range as
        defined by IsValidInterpolation() . No attempt is made to validate
        that the Primvar's value contains the right number of elements to
        match its interpolation to its topology.

        GetInterpolation() , Interpolation of Geometric Primitive Variables
        """
    def SetUnauthoredValuesIndex(self, unauthoredValuesIndex: int) -> bool:
        """
        Set the index that represents unauthored values in the indices array.


        Some apps (like Maya) allow you to author primvars sparsely over a
        surface. Since most apps can't handle sparse primvars, Maya needs to
        provide a value even for the elements it didn't author. This metadatum
        provides a way to recover the information in apps that do support
        sparse authoring / representation of primvars.

        The fallback value of unauthoredValuesIndex is -1, which indicates
        that there are no unauthored values.

        GetUnauthoredValuesIndex()
        """
    def SplitName(self) -> list[str]:
        """

        UsdAttribute::SplitName()
        """
    @staticmethod
    def StripPrimvarsName(name: str | pxr.Ar.ResolvedPath) -> str:
        '''
        Returns the C{name}, devoid of the"primvars:"token if present,
        otherwise returns the C{name} unchanged.
        '''
    def ValueMightBeTimeVarying(self) -> bool:
        '''
        Return true if it is possible, but not certain, that this primvar\'s
        value changes over time, false otherwise.


        This considers time-varyingness of the associated"indices"attribute if
        the primvar is indexed.

        UsdAttribute::ValueMightBeTimeVarying
        '''
    def __bool__(self) -> bool:
        """
        Return true if this Primvar is valid for querying and authoring values
        and metadata, which is identically equivalent to IsDefined() .
        """
    def __eq__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...

class PrimvarsAPI(pxr.Usd.APISchemaBase):
    '''
    UsdGeomPrimvarsAPI encodes geometric"primitive variables", as
    UsdGeomPrimvar, which interpolate across a primitive\'s topology, can
    override shader inputs, and inherit down namespace.


    Which Method to Use to Retrieve Primvars
    ========================================

    While creating primvars is unambiguous ( CreatePrimvar() ), there are
    quite a few methods available for retrieving primvars, making it
    potentially confusing knowing which one to use. Here are some
    guidelines:

       - If you are populating a GUI with the primvars already available
         for authoring values on a prim, use GetPrimvars() .

       - If you want all of the"useful"(e.g. to a renderer) primvars
         available at a prim, including those inherited from ancestor prims,
         use FindPrimvarsWithInheritance() . Note that doing so individually
         for many prims will be inefficient.

       - To find a particular primvar defined directly on a prim, which
         may or may not provide a value, use GetPrimvar() .

       - To find a particular primvar defined on a prim or inherited from
         ancestors, which may or may not provide a value, use
         FindPrimvarWithInheritance() .

       - To *efficiently* query for primvars using the overloads of
         FindPrimvarWithInheritance() and FindPrimvarsWithInheritance() , one
         must first cache the results of FindIncrementallyInheritablePrimvars()
         for each non-leaf prim on the stage.

    '''
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None:
        """
        Construct a UsdGeomPrimvarsAPI on UsdPrim C{prim}.


        Equivalent to UsdGeomPrimvarsAPI::Get (prim.GetStage(),
        prim.GetPath()) for a *valid* C{prim}, but will not immediately throw
        an error for an invalid C{prim}
        """
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None:
        """
        Construct a UsdGeomPrimvarsAPI on the prim held by C{schemaObj}.


        Should be preferred over UsdGeomPrimvarsAPI (schemaObj.GetPrim()), as
        it preserves SchemaBase state.
        """
    def BlockPrimvar(self, name: str | pxr.Ar.ResolvedPath) -> None:
        """
        Remove all time samples on the primvar and its associated indices
        attr, and author a *block* C{default} value.


        This will cause authored opinions in weaker layers to be ignored.

        UsdAttribute::Block() , UsdGeomPrimvar::BlockIndices
        """
    @staticmethod
    def CanContainPropertyName(name: str | pxr.Ar.ResolvedPath) -> bool:
        '''
        Test whether a given C{name} contains the"primvars:"prefix.
        '''
    def CreateIndexedPrimvar(self, name: str | pxr.Ar.ResolvedPath, typeName: pxr.Sdf.ValueTypeName, value: Any, indices: pxr.Vt.IntArray | typing.Iterable[int], interpolation: str | pxr.Ar.ResolvedPath = ..., elementSize: int = ..., time: pxr.Usd.TimeCode | float | pxr.Sdf.TimeCode = ...) -> Primvar:
        """
        Author scene description to create an attribute and authoring a
        C{value} on this prim that will be recognized as an indexed Primvar
        with C{indices} appropriately set (i.e.


        will present as a valid UsdGeomPrimvar).

        an invalid UsdGeomPrimvar on error, a valid UsdGeomPrimvar otherwise.
        It is fine to call this method multiple times, and in different
        UsdEditTargets, even if there is an existing primvar of the same name,
        indexed or not.

        CreatePrimvar() , CreateNonIndexedPrimvar() ,
        UsdPrim::CreateAttribute() , UsdGeomPrimvar::IsPrimvar()
        """
    def CreateNonIndexedPrimvar(self, name: str | pxr.Ar.ResolvedPath, typeName: pxr.Sdf.ValueTypeName, value: Any, interpolation: str | pxr.Ar.ResolvedPath = ..., elementSize: int = ..., time: pxr.Usd.TimeCode | float | pxr.Sdf.TimeCode = ...) -> Primvar:
        """
        Author scene description to create an attribute and authoring a
        C{value} on this prim that will be recognized as a Primvar (i.e.


        will present as a valid UsdGeomPrimvar). Note that unlike
        CreatePrimvar using this API explicitly authors a block for the
        indices attr associated with the primvar, thereby blocking any indices
        set in any weaker layers.

        an invalid UsdGeomPrimvar on error, a valid UsdGeomPrimvar otherwise.
        It is fine to call this method multiple times, and in different
        UsdEditTargets, even if there is an existing primvar of the same name,
        indexed or not.

        CreatePrimvar() , CreateIndexedPrimvar() , UsdPrim::CreateAttribute()
        , UsdGeomPrimvar::IsPrimvar()
        """
    def CreatePrimvar(self, name: str | pxr.Ar.ResolvedPath, typeName: pxr.Sdf.ValueTypeName, interpolation: str | pxr.Ar.ResolvedPath = ..., elementSize: int = ...) -> Primvar:
        '''
        Author scene description to create an attribute on this prim that will
        be recognized as Primvar (i.e.


        will present as a valid UsdGeomPrimvar).

        The name of the created attribute may or may not be the specified
        C{name}, due to the possible need to apply property namespacing for
        primvars. See Creating and Accessing Primvars for more information.
        Creation may fail and return an invalid Primvar if C{name} contains a
        reserved keyword, such as the"indices"suffix we use for indexed
        primvars.

        The behavior with respect to the provided C{typeName} is the same as
        for UsdAttributes::Create(), and C{interpolation} and C{elementSize}
        are as described in UsdGeomPrimvar::GetInterpolation() and
        UsdGeomPrimvar::GetElementSize() .

        If C{interpolation} and/or C{elementSize} are left unspecified, we
        will author no opinions for them, which means any (strongest) opinion
        already authored in any contributing layer for these fields will
        become the Primvar\'s values, or the fallbacks if no opinions have been
        authored.

        an invalid UsdGeomPrimvar if we failed to create a valid attribute, a
        valid UsdGeomPrimvar otherwise. It is not an error to create over an
        existing, compatible attribute.

        UsdPrim::CreateAttribute() , UsdGeomPrimvar::IsPrimvar()
        '''
    def FindIncrementallyInheritablePrimvars(self, inheritedFromAncestors: typing.Iterable[Primvar]) -> list[Primvar]:
        """
        Compute the primvars that can be inherited from this prim by its child
        prims, starting from the set of primvars inherited from this prim's
        ancestors.


        If this method returns an empty vector, then this prim's children
        should inherit the same set of primvars available to this prim, i.e.
        the input C{inheritedFromAncestors}.

        As opposed to FindInheritablePrimvars() , which always recurses up
        through all of the prim's ancestors, this method allows more efficient
        computation of inheritable primvars by starting with the list of
        primvars inherited from this prim's ancestors, and returning a newly
        allocated vector only when this prim makes a change to the set of
        inherited primvars. This enables O(n) inherited primvar computation
        for all prims on a Stage, with potential to share computed results
        that are identical (i.e. when this method returns an empty vector, its
        parent's result can (and must!) be reused for all of the prim's
        children.

        Which Method to Use to Retrieve Primvars
        """
    def FindInheritablePrimvars(self) -> list[Primvar]:
        """
        Compute the primvars that can be inherited from this prim by its child
        prims, including the primvars that B{this} prim inherits from ancestor
        prims.


        Inherited primvars will be bound to attributes on the corresponding
        ancestor prims.

        Only primvars with B{authored}, B{non-blocked}, B{constant
        interpolation} values are inheritable; fallback values are not
        inherited. The order of the returned primvars is undefined.

        It is not generally useful to call this method on UsdGeomGprim leaf
        prims, and furthermore likely to be expensive since *most* primvars
        are defined on Gprims.

        Which Method to Use to Retrieve Primvars
        """
    @overload
    def FindPrimvarWithInheritance(self, name: str | pxr.Ar.ResolvedPath) -> Primvar:
        """
        Like GetPrimvar() , but if the named primvar does not exist or has no
        authored value on this prim, search for the named, value-producing
        primvar on ancestor prims.


        The returned primvar will be bound to the attribute on the
        corresponding ancestor prim on which it was found (if any). If neither
        this prim nor any ancestor contains a value-producing primvar, then
        the returned primvar will be the same as that returned by GetPrimvar()
        .

        This is probably the method you want to call when needing to consume a
        primvar of a particular name.

        Which Method to Use to Retrieve Primvars
        """
    @overload
    def FindPrimvarWithInheritance(self, name: str | pxr.Ar.ResolvedPath, inheritedFromAncestors: typing.Iterable[Primvar]) -> Primvar:
        """
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.

        This version of FindPrimvarWithInheritance() takes the pre-computed
        set of primvars inherited from this prim's ancestors, as computed by
        FindInheritablePrimvars() or FindIncrementallyInheritablePrimvars() on
        the prim's parent.



        Which Method to Use to Retrieve Primvars
        """
    @overload
    def FindPrimvarsWithInheritance(self) -> list[Primvar]:
        """
        Find all of the value-producing primvars either defined on this prim,
        or inherited from ancestor prims.



        Which Method to Use to Retrieve Primvars
        """
    @overload
    def FindPrimvarsWithInheritance(self, inheritedFromAncestors: typing.Iterable[Primvar]) -> list[Primvar]:
        """
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.

        This version of FindPrimvarsWithInheritance() takes the pre-computed
        set of primvars inherited from this prim's ancestors, as computed by
        FindInheritablePrimvars() or FindIncrementallyInheritablePrimvars() on
        the prim's parent.



        Which Method to Use to Retrieve Primvars
        """
    @staticmethod
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> PrimvarsAPI:
        """
        Return a UsdGeomPrimvarsAPI holding the prim adhering to this schema
        at C{path} on C{stage}.


        If no prim exists at C{path} on C{stage}, or if the prim at that path
        does not adhere to this schema, return an invalid schema object. This
        is shorthand for the following: ::

          UsdGeomPrimvarsAPI(stage->GetPrimAtPath(path));

        """
    def GetAuthoredPrimvars(self) -> list[Primvar]:
        """
        Like GetPrimvars() , but include only primvars that have some authored
        scene description (though not necessarily a value).



        Which Method to Use to Retrieve Primvars
        """
    def GetPrimvar(self, name: str | pxr.Ar.ResolvedPath) -> Primvar:
        """
        Return the Primvar object named by C{name}, which will be valid if a
        Primvar attribute definition already exists.


        Name lookup will account for Primvar namespacing, which means that
        this method will succeed in some cases where ::

          UsdGeomPrimvar(prim->GetAttribute(name))

         will not, unless C{name} is properly namespace prefixed.

        Just because a Primvar is valid and defined, and *even if* its
        underlying UsdAttribute (GetAttr()) answers HasValue() affirmatively,
        one must still check the return value of Get() , due to the potential
        of time-varying value blocks (see Attribute Value Blocking).

        HasPrimvar() , Which Method to Use to Retrieve Primvars
        """
    def GetPrimvars(self) -> list[Primvar]:
        """
        Return valid UsdGeomPrimvar objects for all defined Primvars on this
        prim, similarly to UsdPrim::GetAttributes() .


        The returned primvars may not possess any values, and therefore not be
        useful to some clients. For the primvars useful for inheritance
        computations, see GetPrimvarsWithAuthoredValues() , and for primvars
        useful for direct consumption, see GetPrimvarsWithValues() .

        Which Method to Use to Retrieve Primvars
        """
    def GetPrimvarsWithAuthoredValues(self) -> list[Primvar]:
        """
        Like GetPrimvars() , but include only primvars that have an
        B{authored} value.


        This is the query used when computing inheritable primvars, and is
        generally more useful than GetAuthoredPrimvars() .

        Which Method to Use to Retrieve Primvars
        """
    def GetPrimvarsWithValues(self) -> list[Primvar]:
        """
        Like GetPrimvars() , but include only primvars that have some value,
        whether it comes from authored scene description or a schema fallback.


        For most purposes, this method is more useful than GetPrimvars() .

        Which Method to Use to Retrieve Primvars
        """
    @staticmethod
    def GetSchemaAttributeNames(includeInherited: bool = ...) -> list[str]:
        """
        Return a vector of names of all pre-declared attributes for this
        schema class and all its ancestor classes.


        Does not include attributes that may be authored by custom/extended
        methods of the schemas involved.
        """
    def HasPossiblyInheritedPrimvar(self, name: str | pxr.Ar.ResolvedPath) -> bool:
        '''
        Is there a Primvar named C{name} with an authored value on this prim
        or any of its ancestors?


        This is probably the method you want to call when wanting to know
        whether or not the prim"has"a primvar of a particular name.

        FindPrimvarWithInheritance()
        '''
    def HasPrimvar(self, name: str | pxr.Ar.ResolvedPath) -> bool:
        """
        Is there a defined Primvar C{name} on this prim?


        Name lookup will account for Primvar namespacing.

        Like GetPrimvar() , a return value of C{true} for HasPrimvar() does
        not guarantee the primvar will produce a value.
        """
    def RemovePrimvar(self, name: str | pxr.Ar.ResolvedPath) -> bool:
        '''
        Author scene description to delete an attribute on this prim that was
        recognized as Primvar (i.e.


        will present as a valid UsdGeomPrimvar), *in the current
        UsdEditTarget*.

        Because this method can only remove opinions about the primvar from
        the current EditTarget, you may generally find it more useful to use
        BlockPrimvar() which will ensure that all values from the EditTarget
        and weaker layers for the primvar and its indices will be ignored.

        Removal may fail and return false if C{name} contains a reserved
        keyword, such as the"indices"suffix we use for indexed primvars.

        Note this will also remove the indices attribute associated with an
        indiced primvar.

        true if UsdGeomPrimvar and indices attribute was successfully removed,
        false otherwise.

        UsdPrim::RemoveProperty() )
        '''
    @staticmethod
    def _GetStaticTfType() -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...

class Scope(Imageable):
    """
    Scope is the simplest grouping primitive, and does not carry the
    baggage of transformability.


    Note that transforms should inherit down through a Scope successfully
    - it is just a guaranteed no-op from a transformability perspective.
    """
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None:
        """
        Construct a UsdGeomScope on UsdPrim C{prim}.


        Equivalent to UsdGeomScope::Get (prim.GetStage(), prim.GetPath()) for
        a *valid* C{prim}, but will not immediately throw an error for an
        invalid C{prim}
        """
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None:
        """
        Construct a UsdGeomScope on the prim held by C{schemaObj}.


        Should be preferred over UsdGeomScope (schemaObj.GetPrim()), as it
        preserves SchemaBase state.
        """
    @staticmethod
    def Define(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> Scope:
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
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> Scope:
        """
        Return a UsdGeomScope holding the prim adhering to this schema at
        C{path} on C{stage}.


        If no prim exists at C{path} on C{stage}, or if the prim at that path
        does not adhere to this schema, return an invalid schema object. This
        is shorthand for the following: ::

          UsdGeomScope(stage->GetPrimAtPath(path));

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

class Sphere(Gprim):
    """
    Defines a primitive sphere centered at the origin.


    The fallback values for Cube, Sphere, Cone, and Cylinder are set so
    that they all pack into the same volume/bounds.
    """
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None:
        """
        Construct a UsdGeomSphere on UsdPrim C{prim}.


        Equivalent to UsdGeomSphere::Get (prim.GetStage(), prim.GetPath()) for
        a *valid* C{prim}, but will not immediately throw an error for an
        invalid C{prim}
        """
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None:
        """
        Construct a UsdGeomSphere on the prim held by C{schemaObj}.


        Should be preferred over UsdGeomSphere (schemaObj.GetPrim()), as it
        preserves SchemaBase state.
        """
    def CreateExtentAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetExtentAttr() , and also Create vs Get Property Methods for when
        to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateRadiusAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetRadiusAttr() , and also Create vs Get Property Methods for when
        to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    @staticmethod
    def Define(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> Sphere:
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
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> Sphere:
        """
        Return a UsdGeomSphere holding the prim adhering to this schema at
        C{path} on C{stage}.


        If no prim exists at C{path} on C{stage}, or if the prim at that path
        does not adhere to this schema, return an invalid schema object. This
        is shorthand for the following: ::

          UsdGeomSphere(stage->GetPrimAtPath(path));

        """
    def GetExtentAttr(self) -> pxr.Usd.Attribute:
        """
        Extent is re-defined on Sphere only to provide a fallback value.



        UsdGeomGprim::GetExtentAttr() .

        Declaration

        C{float3[] extent = [(-1, -1, -1), (1, 1, 1)]}

        C++ Type

        VtArray<GfVec3f>

        Usd Type

        SdfValueTypeNames->Float3Array
        """
    def GetRadiusAttr(self) -> pxr.Usd.Attribute:
        """
        Indicates the sphere's radius.


        If you author *radius* you must also author *extent*.

        GetExtentAttr()

        Declaration

        C{double radius = 1}

        C++ Type

        double

        Usd Type

        SdfValueTypeNames->Double
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

class Subset(pxr.Usd.Typed):
    '''
    Encodes a subset of a piece of geometry (i.e.


    a UsdGeomImageable) as a set of indices. Currently supports encoding
    subsets of faces, points, edges, and tetrahedrons.

    To apply to a geometric prim, a GeomSubset prim must be the prim\'s
    direct child in namespace, and possess a concrete defining specifier
    (i.e. def). This restriction makes it easy and efficient to discover
    subsets of a prim. We might want to relax this restriction if it\'s
    common to have multiple B{families} of subsets on a gprim and if it\'s
    useful to be able to organize subsets belonging to a B{family} under a
    common scope. See\'familyName\'attribute for more info on defining a
    family of subsets.

    Note that a GeomSubset isn\'t an imageable (i.e. doesn\'t derive from
    UsdGeomImageable). So, you can\'t author B{visibility} for it or
    override its B{purpose}.

    Materials are bound to GeomSubsets just as they are for regular
    geometry using API available in UsdShade (UsdShadeMaterial::Bind).

    For any described attribute *Fallback* *Value* or *Allowed* *Values*
    below that are text/tokens, the actual token is published and defined
    in UsdGeomTokens. So to set an attribute to the value"rightHanded",
    use UsdGeomTokens->rightHanded as the value.
    '''
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None:
        """
        Construct a UsdGeomSubset on UsdPrim C{prim}.


        Equivalent to UsdGeomSubset::Get (prim.GetStage(), prim.GetPath()) for
        a *valid* C{prim}, but will not immediately throw an error for an
        invalid C{prim}
        """
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None:
        """
        Construct a UsdGeomSubset on the prim held by C{schemaObj}.


        Should be preferred over UsdGeomSubset (schemaObj.GetPrim()), as it
        preserves SchemaBase state.
        """
    def CreateElementTypeAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetElementTypeAttr() , and also Create vs Get Property Methods for
        when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateFamilyNameAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetFamilyNameAttr() , and also Create vs Get Property Methods for
        when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    @staticmethod
    def CreateGeomSubset(geom: Imageable, subsetName: str | pxr.Ar.ResolvedPath, elementType: str | pxr.Ar.ResolvedPath, indices: pxr.Vt.IntArray | typing.Iterable[int], familyName: str | pxr.Ar.ResolvedPath = ..., familyType: str | pxr.Ar.ResolvedPath = ...) -> Subset:
        """
        Creates a new GeomSubset below the given C{geom} with the given name,
        C{subsetName}, element type, C{elementType} and C{indices}.


        If a subset named C{subsetName} already exists below C{geom}, then
        this updates its attributes with the values of the provided arguments
        (indices value at time'default'will be updated) and returns it.

        The family type is set / updated on C{geom} only if a non-empty value
        is passed in for C{familyType} and C{familyName}.
        """
    def CreateIndicesAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetIndicesAttr() , and also Create vs Get Property Methods for
        when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    @staticmethod
    def CreateUniqueGeomSubset(geom: Imageable, subsetName: str | pxr.Ar.ResolvedPath, elementType: str | pxr.Ar.ResolvedPath, indices: pxr.Vt.IntArray | typing.Iterable[int], familyName: str | pxr.Ar.ResolvedPath = ..., familyType: str | pxr.Ar.ResolvedPath = ...) -> Subset:
        """
        Creates a new GeomSubset below the given imageable, C{geom} with the
        given name, C{subsetName}, element type, C{elementType} and
        C{indices}.


        If a subset named C{subsetName} already exists below C{geom}, then
        this creates a new subset by appending a suitable index as suffix to
        C{subsetName} (eg, subsetName_1) to avoid name collisions.

        The family type is set / updated on C{geom} only if a non-empty value
        is passed in for C{familyType} and C{familyName}.
        """
    @staticmethod
    def Define(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> Subset:
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
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> Subset:
        """
        Return a UsdGeomSubset holding the prim adhering to this schema at
        C{path} on C{stage}.


        If no prim exists at C{path} on C{stage}, or if the prim at that path
        does not adhere to this schema, return an invalid schema object. This
        is shorthand for the following: ::

          UsdGeomSubset(stage->GetPrimAtPath(path));

        """
    @staticmethod
    def GetAllGeomSubsetFamilyNames(geom: Imageable) -> list:
        """
        Returns the names of all the families of GeomSubsets defined on the
        given imageable, C{geom}.
        """
    @staticmethod
    def GetAllGeomSubsets(geom: Imageable) -> list[Subset]:
        """
        Returns all the GeomSubsets defined on the given imageable, C{geom}.
        """
    def GetElementTypeAttr(self) -> pxr.Usd.Attribute:
        '''
        The type of element that the indices target.


        "elementType"can have one of the following values:
           - B{face} : Identifies faces on a Gprim\'s surface. For a
             UsdGeomMesh, each element of the *indices* attribute would refer to an
             element of the Mesh\'s *faceCounts* attribute. For a UsdGeomTetMesh,
             each element of the *indices* attribute would refer to an element of
             the Mesh\'s *surfaceFaceVertexIndices* attribute.

           - B{point} : for any UsdGeomPointBased, each element of the
             *indices* attribute would refer to an element of the Mesh\'s *points*
             attribute

           - B{edge} : for any UsdGeomMesh, each pair of elements in the
             *indices* attribute would refer to a pair of points of the Mesh\'s
             *points* attribute that are connected as an implicit edge on the Mesh.
             These edges are derived from the Mesh\'s *faceVertexIndices* attribute.
             Edges are not currently defined for a UsdGeomTetMesh, but could be
             derived from all tetrahedron edges or surface face edges only if a
             specific use-case arises.

           - B{tetrahedron} : for any UsdGeomTetMesh, each element of the
             *indices* attribute would refer to an element of the TetMesh\'s
             *tetVertexIndices* attribute.

        Declaration

        C{uniform token elementType ="face"}

        C++ Type

        TfToken

        Usd Type

        SdfValueTypeNames->Token

        Variability

        SdfVariabilityUniform

        Allowed Values

        face, point, edge, tetrahedron
        '''
    def GetFamilyNameAttr(self) -> pxr.Usd.Attribute:
        '''
        The name of the family of subsets that this subset belongs to.


        This is optional and is primarily useful when there are multiple
        families of subsets under a geometric prim. In some cases, this could
        also be used for achieving proper roundtripping of subset data between
        DCC apps. When multiple subsets belonging to a prim have the same
        familyName, they are said to belong to the family. A *familyType*
        value can be encoded on the owner of a family of subsets as a token
        using the static method UsdGeomSubset::SetFamilyType()
        ."familyType"can have one of the following values:
           - B{UsdGeomTokens->partition} : implies that every element of the
             whole geometry appears exactly once in only one of the subsets
             belonging to the family.

           - B{UsdGeomTokens->nonOverlapping} : an element that appears in one
             subset may not appear in any other subset belonging to the family, and
             appears only once in the subset in which it appears.

           - B{UsdGeomTokens->unrestricted} : implies that there are no
             restrictions w.r.t. the membership of elements in the subsets. They
             could be overlapping and the union of all subsets in the family may
             not represent the whole.

        The validity of subset data is not enforced by the authoring APIs,
        however they can be checked using UsdGeomSubset::ValidateFamily() .

        Declaration

        C{uniform token familyName =""}

        C++ Type

        TfToken

        Usd Type

        SdfValueTypeNames->Token

        Variability

        SdfVariabilityUniform
        '''
    @staticmethod
    def GetFamilyType(geom: Imageable, familyName: str | pxr.Ar.ResolvedPath) -> str:
        """
        Returns the type of family that the GeomSubsets on the given geometric
        prim C{geom}, with the given family name, C{familyName} belong to.


        This only returns the token that's encoded on C{geom} and does not
        perform any actual validation on the family of GeomSubsets. Please use
        ValidateFamily() for such validation.

        When familyType is not set on C{geom}, the fallback value
        UsdTokens->unrestricted is returned.
        """
    @staticmethod
    def GetGeomSubsets(geom: Imageable, elementType: str | pxr.Ar.ResolvedPath = ..., familyName: str | pxr.Ar.ResolvedPath = ...) -> list[Subset]:
        """
        Returns all the GeomSubsets of the given C{elementType} belonging to
        the specified family, C{familyName} on the given imageable, C{geom}.


        If C{elementType} is empty, then subsets containing all element types
        are returned. If C{familyName} is left empty, then all subsets of the
        specified C{elementType} will be returned.
        """
    def GetIndicesAttr(self) -> pxr.Usd.Attribute:
        """
        The set of indices included in this subset.


        The indices need not be sorted, but the same index should not appear
        more than once. Indices are invalid if outside the range [0,
        elementCount) for the given time on the parent geometric prim.

        Declaration

        C{int[] indices = []}

        C++ Type

        VtArray<int>

        Usd Type

        SdfValueTypeNames->IntArray
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
    @staticmethod
    def GetUnassignedIndices(geom: Imageable, elementType: str | pxr.Ar.ResolvedPath, familyName: str | pxr.Ar.ResolvedPath, time: pxr.Usd.TimeCode | float | pxr.Sdf.TimeCode = ...) -> pxr.Vt.IntArray:
        """
        Utility for getting the list of indices that are not assigned to any
        of the GeomSubsets in the C{familyName} family on the given C{geom} at
        the timeCode, C{time}, given the element count (total number of
        indices in the array being subdivided).


        For C{elementType} UsdGeomTokens->edge, the output array of indices
        should be interpreted in pairs, as each sequential pair of indices
        corresponds to an edge between the two points. Each edge will be in
        the order (lowIndex, highIndex).

        If the C{elementType} is not applicable to the given C{geom}, an empty
        array is returned and a coding error is issued.
        """
    @overload
    @staticmethod
    def GetUnassignedIndices(subsets: typing.Iterable[Subset], elementCount: int, time: pxr.Usd.TimeCode | float | pxr.Sdf.TimeCode = ...) -> pxr.Vt.IntArray:
        """
        Deprecated

        Please use GetUnassignedIndices(geom, elementType,familyName, time)
        instead. Utility for getting the list of indices that are not assigned
        to any of the GeomSubsets in C{subsets} at the timeCode, C{time},
        given the element count (total number of indices in the array being
        subdivided), C{elementCount}.
        """
    @staticmethod
    def SetFamilyType(geom: Imageable, familyName: str | pxr.Ar.ResolvedPath, familyType: str | pxr.Ar.ResolvedPath) -> bool:
        """
        This method is used to encode the type of family that the GeomSubsets
        on the given geometric prim C{geom}, with the given family name,
        C{familyName} belong to.


        See UsdGeomSubset::GetFamilyNameAttr for the possible values for
        C{familyType}.

        When a family of GeomSubsets is tagged as a UsdGeomTokens->partition
        or UsdGeomTokens->nonOverlapping, the validity of the data (i.e.
        mutual exclusivity and/or wholeness) is not enforced by the authoring
        APIs. Use ValidateFamily() to validate the data in a family of
        GeomSubsets.

        Returns false upon failure to create or set the appropriate attribute
        on C{geom}.
        """
    @staticmethod
    def ValidateFamily(geom: Imageable, elementType: str | pxr.Ar.ResolvedPath = ..., familyName: str | pxr.Ar.ResolvedPath = ...) -> str:
        '''
        Validates whether the family of subsets identified by the given
        C{familyName} and C{elementType} on the given imageable, C{geom}
        contain valid data.


        If the family is designated as a partition or as non-overlapping using
        SetFamilyType() , then the validity of the data is checked. If the
        familyType is"unrestricted", then this performs only bounds checking
        of the values in the"indices"arrays.

        If C{reason} is not None, then it is populated with a string
        explaining why the family is invalid, if it is invalid.

        The python version of this method returns a tuple containing a (bool,
        string), where the bool has the validity of the family and the string
        contains the reason (if it\'s invalid).
        '''
    @staticmethod
    def ValidateSubsets(subsets: typing.Iterable[Subset], elementCount: int, familyType: str | pxr.Ar.ResolvedPath) -> str:
        """
        Deprecated

        Please use UsdGeomSubset::ValidateFamily instead. Validates the data
        in the given set of GeomSubsets, C{subsets}, given the total number of
        elements in the array being subdivided, C{elementCount} and the
        C{familyType} that the subsets belong to.

        For proper validation of indices in C{subsets}, all of the GeomSubsets
        must have the same'elementType'.

        If one or more subsets contain invalid data, then false is returned
        and C{reason} is populated with a string explaining the reason why it
        is invalid.

        The python version of this method returns a tuple containing a (bool,
        string), where the bool has the validity of the subsets and the string
        contains the reason (if they're invalid).
        """
    @staticmethod
    def _GetStaticTfType() -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...

class TetMesh(PointBased):
    """
    Encodes a tetrahedral mesh.


    A tetrahedral mesh is defined as a set of tetrahedra. Each tetrahedron
    is defined by a set of 4 points, with the triangles of the tetrahedron
    determined from these 4 points as described in the B{tetVertexIndices}
    attribute description. The mesh surface faces are encoded as
    triangles. Surface faces must be provided for consumers that need to
    do surface calculations, such as renderers or consumers using physics
    attachments. Both tetrahedra and surface face definitions use indices
    into the TetMesh's B{points} attribute, inherited from
    UsdGeomPointBased.
    """
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None:
        """
        Construct a UsdGeomTetMesh on UsdPrim C{prim}.


        Equivalent to UsdGeomTetMesh::Get (prim.GetStage(), prim.GetPath())
        for a *valid* C{prim}, but will not immediately throw an error for an
        invalid C{prim}
        """
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None:
        """
        Construct a UsdGeomTetMesh on the prim held by C{schemaObj}.


        Should be preferred over UsdGeomTetMesh (schemaObj.GetPrim()), as it
        preserves SchemaBase state.
        """
    @staticmethod
    def ComputeSurfaceFaces(tetMesh: TetMesh, timeCode: pxr.Usd.TimeCode | float | pxr.Sdf.TimeCode = ...) -> pxr.Vt.Vec3iArray:
        """
        ComputeSurfaceFaces determines the vertex indices of the surface faces
        from tetVertexIndices.


        The surface faces are the set of faces that occur only once when
        traversing the faces of all the tetrahedra. The algorithm is O(nlogn)
        in the number of tetrahedra. Method returns false if
        surfaceFaceIndices argument is nullptr and returns true otherwise. The
        algorithm can't be O(n) because we need to sort the resulting surface
        faces for deterministic behavior across different compilers and OS.
        """
    def CreateSurfaceFaceVertexIndicesAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetSurfaceFaceVertexIndicesAttr() , and also Create vs Get
        Property Methods for when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateTetVertexIndicesAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetTetVertexIndicesAttr() , and also Create vs Get Property
        Methods for when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    @staticmethod
    def Define(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> TetMesh:
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
    def FindInvertedElements(tetMesh: TetMesh, timeCode: pxr.Usd.TimeCode | float | pxr.Sdf.TimeCode = ...) -> pxr.Vt.IntArray:
        '''
        FindInvertedElements is used to determine if the tetMesh has inverted
        tetrahedral elements at the given time code.


        Inverted elements are determined wrt. the"orientation"attribute of the
        UsdGeomTetMesh and are stored in the invertedElements arg. Method
        returns true if it succeeds and if invertedElements is empty then all
        the tetrahedra have  the correct orientation.
        '''
    @staticmethod
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> TetMesh:
        """
        Return a UsdGeomTetMesh holding the prim adhering to this schema at
        C{path} on C{stage}.


        If no prim exists at C{path} on C{stage}, or if the prim at that path
        does not adhere to this schema, return an invalid schema object. This
        is shorthand for the following: ::

          UsdGeomTetMesh(stage->GetPrimAtPath(path));

        """
    @staticmethod
    def GetSchemaAttributeNames(includeInherited: bool = ...) -> list[str]:
        """
        Return a vector of names of all pre-declared attributes for this
        schema class and all its ancestor classes.


        Does not include attributes that may be authored by custom/extended
        methods of the schemas involved.
        """
    def GetSurfaceFaceVertexIndicesAttr(self) -> pxr.Usd.Attribute:
        """
        B{surfaceFaceVertexIndices} defines the triangle surface faces indices
        wrt.


        B{points} of the tetmesh surface. Again the B{orientation} attribute
        inherited from UsdGeomPrim should be set accordingly. The
        B{orientation} for faces of tetrahedra and  surface faces must match.

        Declaration

        C{int3[] surfaceFaceVertexIndices}

        C++ Type

        VtArray<GfVec3i>

        Usd Type

        SdfValueTypeNames->Int3Array
        """
    def GetTetVertexIndicesAttr(self) -> pxr.Usd.Attribute:
        '''
        Flat list of the index (into the B{points} attribute) of each vertex
        of each tetrahedron in the mesh.


        Each int4 corresponds to the indices of a single tetrahedron. Users
        should set the B{orientation} attribute of UsdGeomPrim accordingly.
        That is if the B{orientation} is"rightHanded", the CCW face ordering
        of a tetrahedron is [123],[032],[013],[021] with respect to the int4.
        This results in the normals facing outward from the center of the
        tetrahedron. The following diagram shows the face ordering of an
        unwrapped tetrahedron with"rightHanded"orientation.

        If the B{orientation} attribute is set to"leftHanded"the face ordering
        of the tetrahedron is [321],[230],[310],[120] and the leftHanded CW
        face normals point outward from the center of the tetrahedron. The
        following diagram shows the face ordering of an unwrapped tetrahedron
        with"leftHanded"orientation.

        Setting the B{orientation} attribute to align with the ordering of the
        int4 for the tetrahedrons is the responsibility of the user.

        Declaration

        C{int4[] tetVertexIndices}

        C++ Type

        VtArray<GfVec4i>

        Usd Type

        SdfValueTypeNames->Int4Array
        '''
    @staticmethod
    def _GetStaticTfType() -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...

class Tokens(Boost.Python.instance):
    BasisCurves: ClassVar[str] = ...  # read-only
    Boundable: ClassVar[str] = ...  # read-only
    Camera: ClassVar[str] = ...  # read-only
    Capsule: ClassVar[str] = ...  # read-only
    Capsule_1: ClassVar[str] = ...  # read-only
    Cone: ClassVar[str] = ...  # read-only
    Cube: ClassVar[str] = ...  # read-only
    Curves: ClassVar[str] = ...  # read-only
    Cylinder: ClassVar[str] = ...  # read-only
    Cylinder_1: ClassVar[str] = ...  # read-only
    GeomModelAPI: ClassVar[str] = ...  # read-only
    GeomSubset: ClassVar[str] = ...  # read-only
    Gprim: ClassVar[str] = ...  # read-only
    HermiteCurves: ClassVar[str] = ...  # read-only
    Imageable: ClassVar[str] = ...  # read-only
    Mesh: ClassVar[str] = ...  # read-only
    MotionAPI: ClassVar[str] = ...  # read-only
    NurbsCurves: ClassVar[str] = ...  # read-only
    NurbsPatch: ClassVar[str] = ...  # read-only
    Plane: ClassVar[str] = ...  # read-only
    PointBased: ClassVar[str] = ...  # read-only
    PointInstancer: ClassVar[str] = ...  # read-only
    Points: ClassVar[str] = ...  # read-only
    PrimvarsAPI: ClassVar[str] = ...  # read-only
    Scope: ClassVar[str] = ...  # read-only
    Sphere: ClassVar[str] = ...  # read-only
    TetMesh: ClassVar[str] = ...  # read-only
    VisibilityAPI: ClassVar[str] = ...  # read-only
    Xform: ClassVar[str] = ...  # read-only
    XformCommonAPI: ClassVar[str] = ...  # read-only
    Xformable: ClassVar[str] = ...  # read-only
    accelerations: ClassVar[str] = ...  # read-only
    all: ClassVar[str] = ...  # read-only
    angularVelocities: ClassVar[str] = ...  # read-only
    axis: ClassVar[str] = ...  # read-only
    basis: ClassVar[str] = ...  # read-only
    bezier: ClassVar[str] = ...  # read-only
    bilinear: ClassVar[str] = ...  # read-only
    boundaries: ClassVar[str] = ...  # read-only
    bounds: ClassVar[str] = ...  # read-only
    box: ClassVar[str] = ...  # read-only
    bspline: ClassVar[str] = ...  # read-only
    cards: ClassVar[str] = ...  # read-only
    catmullClark: ClassVar[str] = ...  # read-only
    catmullRom: ClassVar[str] = ...  # read-only
    clippingPlanes: ClassVar[str] = ...  # read-only
    clippingRange: ClassVar[str] = ...  # read-only
    closed: ClassVar[str] = ...  # read-only
    constant: ClassVar[str] = ...  # read-only
    cornerIndices: ClassVar[str] = ...  # read-only
    cornerSharpnesses: ClassVar[str] = ...  # read-only
    cornersOnly: ClassVar[str] = ...  # read-only
    cornersPlus1: ClassVar[str] = ...  # read-only
    cornersPlus2: ClassVar[str] = ...  # read-only
    creaseIndices: ClassVar[str] = ...  # read-only
    creaseLengths: ClassVar[str] = ...  # read-only
    creaseSharpnesses: ClassVar[str] = ...  # read-only
    cross: ClassVar[str] = ...  # read-only
    cubic: ClassVar[str] = ...  # read-only
    curveVertexCounts: ClassVar[str] = ...  # read-only
    default_: ClassVar[str] = ...  # read-only
    doubleSided: ClassVar[str] = ...  # read-only
    edge: ClassVar[str] = ...  # read-only
    edgeAndCorner: ClassVar[str] = ...  # read-only
    edgeOnly: ClassVar[str] = ...  # read-only
    elementSize: ClassVar[str] = ...  # read-only
    elementType: ClassVar[str] = ...  # read-only
    exposure: ClassVar[str] = ...  # read-only
    extent: ClassVar[str] = ...  # read-only
    extentsHint: ClassVar[str] = ...  # read-only
    fStop: ClassVar[str] = ...  # read-only
    face: ClassVar[str] = ...  # read-only
    faceVarying: ClassVar[str] = ...  # read-only
    faceVaryingLinearInterpolation: ClassVar[str] = ...  # read-only
    faceVertexCounts: ClassVar[str] = ...  # read-only
    faceVertexIndices: ClassVar[str] = ...  # read-only
    familyName: ClassVar[str] = ...  # read-only
    focalLength: ClassVar[str] = ...  # read-only
    focusDistance: ClassVar[str] = ...  # read-only
    fromTexture: ClassVar[str] = ...  # read-only
    guide: ClassVar[str] = ...  # read-only
    guideVisibility: ClassVar[str] = ...  # read-only
    height: ClassVar[str] = ...  # read-only
    hermite: ClassVar[str] = ...  # read-only
    holeIndices: ClassVar[str] = ...  # read-only
    horizontalAperture: ClassVar[str] = ...  # read-only
    horizontalApertureOffset: ClassVar[str] = ...  # read-only
    ids: ClassVar[str] = ...  # read-only
    inactiveIds: ClassVar[str] = ...  # read-only
    indices: ClassVar[str] = ...  # read-only
    inherited: ClassVar[str] = ...  # read-only
    interpolateBoundary: ClassVar[str] = ...  # read-only
    interpolation: ClassVar[str] = ...  # read-only
    invisible: ClassVar[str] = ...  # read-only
    invisibleIds: ClassVar[str] = ...  # read-only
    knots: ClassVar[str] = ...  # read-only
    left: ClassVar[str] = ...  # read-only
    leftHanded: ClassVar[str] = ...  # read-only
    length: ClassVar[str] = ...  # read-only
    linear: ClassVar[str] = ...  # read-only
    loop: ClassVar[str] = ...  # read-only
    metersPerUnit: ClassVar[str] = ...  # read-only
    modelApplyDrawMode: ClassVar[str] = ...  # read-only
    modelCardGeometry: ClassVar[str] = ...  # read-only
    modelCardTextureXNeg: ClassVar[str] = ...  # read-only
    modelCardTextureXPos: ClassVar[str] = ...  # read-only
    modelCardTextureYNeg: ClassVar[str] = ...  # read-only
    modelCardTextureYPos: ClassVar[str] = ...  # read-only
    modelCardTextureZNeg: ClassVar[str] = ...  # read-only
    modelCardTextureZPos: ClassVar[str] = ...  # read-only
    modelDrawMode: ClassVar[str] = ...  # read-only
    modelDrawModeColor: ClassVar[str] = ...  # read-only
    mono: ClassVar[str] = ...  # read-only
    motionBlurScale: ClassVar[str] = ...  # read-only
    motionNonlinearSampleCount: ClassVar[str] = ...  # read-only
    motionVelocityScale: ClassVar[str] = ...  # read-only
    nonOverlapping: ClassVar[str] = ...  # read-only
    none: ClassVar[str] = ...  # read-only
    nonperiodic: ClassVar[str] = ...  # read-only
    normals: ClassVar[str] = ...  # read-only
    open: ClassVar[str] = ...  # read-only
    order: ClassVar[str] = ...  # read-only
    orientation: ClassVar[str] = ...  # read-only
    orientations: ClassVar[str] = ...  # read-only
    orientationsf: ClassVar[str] = ...  # read-only
    origin: ClassVar[str] = ...  # read-only
    orthographic: ClassVar[str] = ...  # read-only
    partition: ClassVar[str] = ...  # read-only
    periodic: ClassVar[str] = ...  # read-only
    perspective: ClassVar[str] = ...  # read-only
    pinned: ClassVar[str] = ...  # read-only
    pivot: ClassVar[str] = ...  # read-only
    point: ClassVar[str] = ...  # read-only
    pointWeights: ClassVar[str] = ...  # read-only
    points: ClassVar[str] = ...  # read-only
    positions: ClassVar[str] = ...  # read-only
    power: ClassVar[str] = ...  # read-only
    primvarsDisplayColor: ClassVar[str] = ...  # read-only
    primvarsDisplayOpacity: ClassVar[str] = ...  # read-only
    projection: ClassVar[str] = ...  # read-only
    protoIndices: ClassVar[str] = ...  # read-only
    prototypes: ClassVar[str] = ...  # read-only
    proxy: ClassVar[str] = ...  # read-only
    proxyPrim: ClassVar[str] = ...  # read-only
    proxyVisibility: ClassVar[str] = ...  # read-only
    purpose: ClassVar[str] = ...  # read-only
    radius: ClassVar[str] = ...  # read-only
    radiusBottom: ClassVar[str] = ...  # read-only
    radiusTop: ClassVar[str] = ...  # read-only
    ranges: ClassVar[str] = ...  # read-only
    render: ClassVar[str] = ...  # read-only
    renderVisibility: ClassVar[str] = ...  # read-only
    right: ClassVar[str] = ...  # read-only
    rightHanded: ClassVar[str] = ...  # read-only
    scales: ClassVar[str] = ...  # read-only
    shutterClose: ClassVar[str] = ...  # read-only
    shutterOpen: ClassVar[str] = ...  # read-only
    size: ClassVar[str] = ...  # read-only
    smooth: ClassVar[str] = ...  # read-only
    stereoRole: ClassVar[str] = ...  # read-only
    subdivisionScheme: ClassVar[str] = ...  # read-only
    surfaceFaceVertexIndices: ClassVar[str] = ...  # read-only
    tangents: ClassVar[str] = ...  # read-only
    tetVertexIndices: ClassVar[str] = ...  # read-only
    tetrahedron: ClassVar[str] = ...  # read-only
    triangleSubdivisionRule: ClassVar[str] = ...  # read-only
    trimCurveCounts: ClassVar[str] = ...  # read-only
    trimCurveKnots: ClassVar[str] = ...  # read-only
    trimCurveOrders: ClassVar[str] = ...  # read-only
    trimCurvePoints: ClassVar[str] = ...  # read-only
    trimCurveRanges: ClassVar[str] = ...  # read-only
    trimCurveVertexCounts: ClassVar[str] = ...  # read-only
    type: ClassVar[str] = ...  # read-only
    uForm: ClassVar[str] = ...  # read-only
    uKnots: ClassVar[str] = ...  # read-only
    uOrder: ClassVar[str] = ...  # read-only
    uRange: ClassVar[str] = ...  # read-only
    uVertexCount: ClassVar[str] = ...  # read-only
    unauthoredValuesIndex: ClassVar[str] = ...  # read-only
    uniform: ClassVar[str] = ...  # read-only
    unrestricted: ClassVar[str] = ...  # read-only
    upAxis: ClassVar[str] = ...  # read-only
    vForm: ClassVar[str] = ...  # read-only
    vKnots: ClassVar[str] = ...  # read-only
    vOrder: ClassVar[str] = ...  # read-only
    vRange: ClassVar[str] = ...  # read-only
    vVertexCount: ClassVar[str] = ...  # read-only
    varying: ClassVar[str] = ...  # read-only
    velocities: ClassVar[str] = ...  # read-only
    vertex: ClassVar[str] = ...  # read-only
    verticalAperture: ClassVar[str] = ...  # read-only
    verticalApertureOffset: ClassVar[str] = ...  # read-only
    visibility: ClassVar[str] = ...  # read-only
    visible: ClassVar[str] = ...  # read-only
    width: ClassVar[str] = ...  # read-only
    widths: ClassVar[str] = ...  # read-only
    wrap: ClassVar[str] = ...  # read-only
    x: ClassVar[str] = ...  # read-only
    xformOpOrder: ClassVar[str] = ...  # read-only
    y: ClassVar[str] = ...  # read-only
    z: ClassVar[str] = ...  # read-only
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """

class VisibilityAPI(pxr.Usd.APISchemaBase):
    '''
    UsdGeomVisibilityAPI introduces properties that can be used to author
    visibility opinions.



    Currently, this schema only introduces the attributes that are used to
    control purpose visibility. Later, this schema will define *all*
    visibility-related properties and UsdGeomImageable will no longer
    define those properties. The purpose visibility attributes added by
    this schema, *guideVisibility*, *proxyVisibility*, and
    *renderVisibility* can each be used to control visibility for geometry
    of the corresponding purpose values, with the overall *visibility*
    attribute acting as an override. I.e., if *visibility* evaluates
    to"invisible", purpose visibility is invisible; otherwise, purpose
    visibility is determined by the corresponding purpose visibility
    attribute.

    Note that the behavior of *guideVisibility* is subtly different from
    the *proxyVisibility* and *renderVisibility* attributes, in
    that"guide"purpose visibility always evaluates to
    either"invisible"or"visible", whereas the other attributes may yield
    computed values of"inherited"if there is no authored opinion on the
    attribute or inherited from an ancestor. This is motivated by the fact
    that, in Pixar"s user workflows,we have never found a need to have all
    guides visible in a scene bydefault, whereas we do find that
    flexibility useful for"proxy"and"render"geometry.This schema can only
    be applied to UsdGeomImageable prims. TheUseGeomImageable schema
    provides API for computing the purpose visibilityvalues that result
    from the attributes introduced by this schema.For any described
    attribute \\em Fallback \\em Value or \\em Allowed \\em Values belowthat
    are text/tokens, the actual token is published and defined in \\ref
    UsdGeomTokens.So to set an attribute to the value"rightHanded", use
    UsdGeomTokens->rightHanded as the value.
    '''
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None:
        """
        Construct a UsdGeomVisibilityAPI on UsdPrim C{prim}.


        Equivalent to UsdGeomVisibilityAPI::Get (prim.GetStage(),
        prim.GetPath()) for a *valid* C{prim}, but will not immediately throw
        an error for an invalid C{prim}
        """
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None:
        """
        Construct a UsdGeomVisibilityAPI on the prim held by C{schemaObj}.


        Should be preferred over UsdGeomVisibilityAPI (schemaObj.GetPrim()),
        as it preserves SchemaBase state.
        """
    @staticmethod
    def Apply(prim: pxr.Usd.Prim) -> VisibilityAPI:
        '''
        Applies this B{single-apply} API schema to the given C{prim}.


        This information is stored by adding"VisibilityAPI"to the token-
        valued, listOp metadata *apiSchemas* on the prim.

        A valid UsdGeomVisibilityAPI object is returned upon success. An
        invalid (or empty) UsdGeomVisibilityAPI object is returned upon
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
    def CreateGuideVisibilityAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetGuideVisibilityAttr() , and also Create vs Get Property Methods
        for when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateProxyVisibilityAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetProxyVisibilityAttr() , and also Create vs Get Property Methods
        for when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateRenderVisibilityAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetRenderVisibilityAttr() , and also Create vs Get Property
        Methods for when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    @staticmethod
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> VisibilityAPI:
        """
        Return a UsdGeomVisibilityAPI holding the prim adhering to this schema
        at C{path} on C{stage}.


        If no prim exists at C{path} on C{stage}, or if the prim at that path
        does not adhere to this schema, return an invalid schema object. This
        is shorthand for the following: ::

          UsdGeomVisibilityAPI(stage->GetPrimAtPath(path));

        """
    def GetGuideVisibilityAttr(self) -> pxr.Usd.Attribute:
        '''
        This attribute controls visibility for geometry with purpose"guide".


        Unlike overall *visibility*, *guideVisibility* is uniform, and
        therefore cannot be animated.

        Also unlike overall *visibility*, *guideVisibility* is tri-state, in
        that a descendant with an opinion of"visible"overrides an ancestor
        opinion of"invisible".

        The *guideVisibility* attribute works in concert with the overall
        *visibility* attribute: The visibility of a prim with purpose"guide"is
        determined by the inherited values it receives for the *visibility*
        and *guideVisibility* attributes. If *visibility* evaluates
        to"invisible", the prim is invisible. If *visibility* evaluates
        to"inherited"and *guideVisibility* evaluates to"visible", then the
        prim is visible. B{Otherwise, it is invisible.}

        Declaration

        C{uniform token guideVisibility ="invisible"}

        C++ Type

        TfToken

        Usd Type

        SdfValueTypeNames->Token

        Variability

        SdfVariabilityUniform

        Allowed Values

        inherited, invisible, visible
        '''
    def GetProxyVisibilityAttr(self) -> pxr.Usd.Attribute:
        '''
        This attribute controls visibility for geometry with purpose"proxy".


        Unlike overall *visibility*, *proxyVisibility* is uniform, and
        therefore cannot be animated.

        Also unlike overall *visibility*, *proxyVisibility* is tri-state, in
        that a descendant with an opinion of"visible"overrides an ancestor
        opinion of"invisible".

        The *proxyVisibility* attribute works in concert with the overall
        *visibility* attribute: The visibility of a prim with purpose"proxy"is
        determined by the inherited values it receives for the *visibility*
        and *proxyVisibility* attributes. If *visibility* evaluates
        to"invisible", the prim is invisible. If *visibility* evaluates
        to"inherited"then: If *proxyVisibility* evaluates to"visible", then
        the prim is visible; if *proxyVisibility* evaluates to"invisible",
        then the prim is invisible; if *proxyVisibility* evaluates
        to"inherited", then the prim may either be visible or invisible,
        depending on a fallback value determined by the calling context.

        Declaration

        C{uniform token proxyVisibility ="inherited"}

        C++ Type

        TfToken

        Usd Type

        SdfValueTypeNames->Token

        Variability

        SdfVariabilityUniform

        Allowed Values

        inherited, invisible, visible
        '''
    def GetPurposeVisibilityAttr(self, purpose: str | pxr.Ar.ResolvedPath) -> pxr.Usd.Attribute:
        '''
        Return the attribute that is used for expressing visibility opinions
        for the given C{purpose}.


        The valid purpose tokens are"guide","proxy", and"render"which return
        the attributes *guideVisibility*, *proxyVisibility*, and
        *renderVisibility* respectively.

        Note that while"default"is a valid purpose token for
        UsdGeomImageable::GetPurposeVisibilityAttr, it is not a valid purpose
        for this function, as UsdGeomVisibilityAPI itself does not have a
        default visibility attribute. Calling this function with "default will
        result in a coding error.
        '''
    def GetRenderVisibilityAttr(self) -> pxr.Usd.Attribute:
        '''
        This attribute controls visibility for geometry with purpose"render".


        Unlike overall *visibility*, *renderVisibility* is uniform, and
        therefore cannot be animated.

        Also unlike overall *visibility*, *renderVisibility* is tri-state, in
        that a descendant with an opinion of"visible"overrides an ancestor
        opinion of"invisible".

        The *renderVisibility* attribute works in concert with the overall
        *visibility* attribute: The visibility of a prim with
        purpose"render"is determined by the inherited values it receives for
        the *visibility* and *renderVisibility* attributes. If *visibility*
        evaluates to"invisible", the prim is invisible. If *visibility*
        evaluates to"inherited"then: If *renderVisibility* evaluates
        to"visible", then the prim is visible; if *renderVisibility* evaluates
        to"invisible", then the prim is invisible; if *renderVisibility*
        evaluates to"inherited", then the prim may either be visible or
        invisible, depending on a fallback value determined by the calling
        context.

        Declaration

        C{uniform token renderVisibility ="inherited"}

        C++ Type

        TfToken

        Usd Type

        SdfValueTypeNames->Token

        Variability

        SdfVariabilityUniform

        Allowed Values

        inherited, invisible, visible
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

class Xform(Xformable):
    """
    Concrete prim schema for a transform, which implements Xformable.
    """
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None:
        """
        Construct a UsdGeomXform on UsdPrim C{prim}.


        Equivalent to UsdGeomXform::Get (prim.GetStage(), prim.GetPath()) for
        a *valid* C{prim}, but will not immediately throw an error for an
        invalid C{prim}
        """
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None:
        """
        Construct a UsdGeomXform on the prim held by C{schemaObj}.


        Should be preferred over UsdGeomXform (schemaObj.GetPrim()), as it
        preserves SchemaBase state.
        """
    @staticmethod
    def Define(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> Xform:
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
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> Xform:
        """
        Return a UsdGeomXform holding the prim adhering to this schema at
        C{path} on C{stage}.


        If no prim exists at C{path} on C{stage}, or if the prim at that path
        does not adhere to this schema, return an invalid schema object. This
        is shorthand for the following: ::

          UsdGeomXform(stage->GetPrimAtPath(path));

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

class XformCache(Boost.Python.instance):
    """
    A caching mechanism for transform matrices.


    For best performance, this object should be reused for multiple CTM
    queries.

    Instances of this type can be copied, though using Swap() may result
    in better performance.

    It is valid to cache prims from multiple stages in a single
    XformCache.

    WARNING: this class does not automatically invalidate cached values
    based on changes to the stage from which values were cached.
    Additionally, a separate instance of this class should be used per-
    thread, calling the Get* methods from multiple threads is not safe, as
    they mutate internal state.
    """
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self, time: pxr.Usd.TimeCode | float | pxr.Sdf.TimeCode) -> None:
        """
        Construct a new XformCache for the specified C{time}.
        """
    @overload
    def __init__(self) -> None:
        """
        Construct a new XformCache for UsdTimeCode::Default() .
        """
    def Clear(self) -> None:
        """
        Clears all pre-cached values.
        """
    def ComputeRelativeTransform(self, prim: pxr.Usd.Prim, ancestor: pxr.Usd.Prim) -> tuple:
        """
        Returns the result of concatenating all transforms beneath C{ancestor}
        that affect C{prim}.


        This includes the local transform of C{prim} itself, but not the local
        transform of C{ancestor}. If C{ancestor} is not an ancestor of
        C{prim}, the resulting transform is the local-to-world transformation
        of C{prim}.  The C{resetXformTsack} pointer must be valid. If any
        intermediate prims reset the transform stack, C{resetXformStack} will
        be set to true. Intermediate transforms are cached, but the result of
        this call itself is not cached.
        """
    def GetLocalToWorldTransform(self, prim: pxr.Usd.Prim) -> pxr.Gf.Matrix4d:
        """
        Compute the transformation matrix for the given C{prim}, including the
        transform authored on the Prim itself, if present.



        This method may mutate internal cache state and is not thread safe.
        """
    def GetLocalTransformation(self, prim: pxr.Usd.Prim) -> tuple:
        """
        Returns the local transformation of the prim.


        Uses the cached XformQuery to compute the result quickly. The
        C{resetsXformStack} pointer must be valid. It will be set to true if
        C{prim} resets the transform stack. The result of this call is cached.
        """
    def GetParentToWorldTransform(self, prim: pxr.Usd.Prim) -> pxr.Gf.Matrix4d:
        """
        Compute the transformation matrix for the given C{prim}, but do NOT
        include the transform authored on the prim itself.



        This method may mutate internal cache state and is not thread safe.
        """
    def GetTime(self) -> pxr.Usd.TimeCode:
        """
        Get the current time from which this cache is reading values.
        """
    def SetTime(self, time: pxr.Usd.TimeCode | float | pxr.Sdf.TimeCode) -> None:
        """
        Use the new C{time} when computing values and may clear any existing
        values cached for the previous time.


        Setting C{time} to the current time is a no-op.
        """
    def Swap(self, other: XformCache) -> None:
        """
        Swap the contents of this XformCache with C{other}.
        """

class XformCommonAPI(pxr.Usd.APISchemaBase):
    '''
    This class provides API for authoring and retrieving a standard set of
    component transformations which include a scale, a rotation, a scale-
    rotate pivot and a translation.


    The goal of the API is to enhance component-wise interchange. It
    achieves this by limiting the set of allowed basic ops and by
    specifying the order in which they are applied. In addition to the
    basic set of ops, the\'resetXformStack\'bit can also be set to indicate
    whether the underlying xformable resets the parent transformation
    (i.e. does not inherit it\'s parent\'s transformation).

    UsdGeomXformCommonAPI::GetResetXformStack()

    UsdGeomXformCommonAPI::SetResetXformStack() The operator-bool for the
    class will inform you whether an existing xformable is compatible with
    this API.

    The scale-rotate pivot is represented by a pair of (translate,
    inverse-translate) xformOps around the scale and rotate operations.
    The rotation operation can be any of the six allowed Euler angle sets.

    UsdGeomXformOp::Type. The xformOpOrder of an xformable that has all of
    the supported basic ops is as follows:
    ["xformOp:translate","xformOp:translate:pivot","xformOp:rotateXYZ","xformOp:scale","!invert!xformOp:translate:pivot"].

    It is worth noting that all of the ops are optional. For example, an
    xformable may have only a translate or a rotate. It would still be
    considered as compatible with this API. Individual SetTranslate() ,
    SetRotate() , SetScale() and SetPivot() methods are provided by this
    API to allow such sparse authoring.
    '''

    class OpFlags(pxr.Tf.Tf_PyEnumWrapper):
        _baseName: ClassVar[str] = ...
        allValues: ClassVar[tuple] = ...
        def __init__(self, *args, **kwargs) -> None:
            """Raises an exception
            This class cannot be instantiated from Python
            """
        @staticmethod
        def GetValueFromName(name: object) -> Any: ...

    class RotationOrder(pxr.Tf.Tf_PyEnumWrapper):
        _baseName: ClassVar[str] = ...
        allValues: ClassVar[tuple] = ...
        def __init__(self, *args, **kwargs) -> None:
            """Raises an exception
            This class cannot be instantiated from Python
            """
        @staticmethod
        def GetValueFromName(name: object) -> Any: ...
    OpPivot: ClassVar[XformCommonAPI.OpFlags] = ...
    OpRotate: ClassVar[XformCommonAPI.OpFlags] = ...
    OpScale: ClassVar[XformCommonAPI.OpFlags] = ...
    OpTranslate: ClassVar[XformCommonAPI.OpFlags] = ...
    RotationOrderXYZ: ClassVar[XformCommonAPI.RotationOrder] = ...
    RotationOrderXZY: ClassVar[XformCommonAPI.RotationOrder] = ...
    RotationOrderYXZ: ClassVar[XformCommonAPI.RotationOrder] = ...
    RotationOrderYZX: ClassVar[XformCommonAPI.RotationOrder] = ...
    RotationOrderZXY: ClassVar[XformCommonAPI.RotationOrder] = ...
    RotationOrderZYX: ClassVar[XformCommonAPI.RotationOrder] = ...
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None:
        """
        Construct a UsdGeomXformCommonAPI on UsdPrim C{prim}.


        Equivalent to UsdGeomXformCommonAPI::Get (prim.GetStage(),
        prim.GetPath()) for a *valid* C{prim}, but will not immediately throw
        an error for an invalid C{prim}
        """
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None:
        """
        Construct a UsdGeomXformCommonAPI on the prim held by C{schemaObj}.


        Should be preferred over UsdGeomXformCommonAPI (schemaObj.GetPrim()),
        as it preserves SchemaBase state.
        """
    @staticmethod
    def CanConvertOpTypeToRotationOrder(opType: XformOp.Type) -> bool:
        """
        Whether the given C{opType} has a corresponding value in the
        UsdGeomXformCommonAPI::RotationOrder enum (i.e., whether it is a
        three-axis rotation).
        """
    @staticmethod
    def ConvertOpTypeToRotationOrder(opType: XformOp.Type) -> XformCommonAPI.RotationOrder:
        """
        Converts the given C{opType} to the corresponding value in the
        UsdGeomXformCommonAPI::RotationOrder enum.


        For example, TypeRotateYZX corresponds to RotationOrderYZX. Raises a
        coding error if C{opType} is not convertible to RotationOrder (i.e.,
        if it isn't a three-axis rotation) and returns the default
        RotationOrderXYZ instead.
        """
    @staticmethod
    def ConvertRotationOrderToOpType(rotationOrder: XformCommonAPI.RotationOrder) -> XformOp.Type:
        """
        Converts the given C{rotOrder} to the corresponding value in the
        UsdGeomXformOp::Type enum.


        For example, RotationOrderYZX corresponds to TypeRotateYZX. Raises a
        coding error if C{rotOrder} is not one of the named enumerators of
        RotationOrder.
        """
    @overload
    def CreateXformOps(self, rotationOrder: XformCommonAPI.RotationOrder, op1: XformCommonAPI.OpFlags = ..., op2: XformCommonAPI.OpFlags = ..., op3: XformCommonAPI.OpFlags = ..., op4: XformCommonAPI.OpFlags = ...) -> tuple:
        """
        Creates the specified XformCommonAPI-compatible xform ops, or returns
        the existing ops if they already exist.


        If successful, returns an Ops object with all the ops on this prim,
        identified by type. If the requested xform ops couldn't be created or
        the prim is not XformCommonAPI-compatible, returns an Ops object with
        all invalid ops.

        The C{rotOrder} is only used if OpRotate is specified. Otherwise, it
        is ignored. (If you don't need to create a rotate op, you might find
        it helpful to use the other overload that takes no rotation order.)
        """
    @overload
    def CreateXformOps(self, op1: XformCommonAPI.OpFlags = ..., op2: XformCommonAPI.OpFlags = ..., op3: XformCommonAPI.OpFlags = ..., op4: XformCommonAPI.OpFlags = ...) -> tuple:
        """
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        This overload does not take a rotation order.


        If you specify OpRotate, then this overload assumes RotationOrderXYZ
        or the previously-authored rotation order. (If you do need to create a
        rotate op, you might find it helpful to use the other overload that
        explicitly takes a rotation order.)
        """
    @staticmethod
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> XformCommonAPI:
        """
        Return a UsdGeomXformCommonAPI holding the prim adhering to this
        schema at C{path} on C{stage}.


        If no prim exists at C{path} on C{stage}, or if the prim at that path
        does not adhere to this schema, return an invalid schema object. This
        is shorthand for the following: ::

          UsdGeomXformCommonAPI(stage->GetPrimAtPath(path));

        """
    def GetResetXformStack(self) -> bool:
        """
        Returns whether the xformable resets the transform stack.


        i.e., does not inherit the parent transformation.
        """
    @staticmethod
    def GetRotationTransform(rotation: pxr.Gf.Vec3f | list[float] | tuple[float, float, float], rotationOrder: XformCommonAPI.RotationOrder) -> pxr.Gf.Matrix4d:
        """
        Return the 4x4 matrix that applies the rotation encoded by rotation
        vector C{rotation} using the rotation order C{rotationOrder}.


        Deprecated

        Please use the result of ConvertRotationOrderToOpType() along with
        UsdGeomXformOp::GetOpTransform() instead.
        """
    @staticmethod
    def GetSchemaAttributeNames(includeInherited: bool = ...) -> list[str]:
        """
        Return a vector of names of all pre-declared attributes for this
        schema class and all its ancestor classes.


        Does not include attributes that may be authored by custom/extended
        methods of the schemas involved.
        """
    def GetXformVectors(self, time: pxr.Usd.TimeCode | float | pxr.Sdf.TimeCode) -> tuple:
        """
        Retrieve values of the various component xformOps at a given C{time}.


        Identity values are filled in for the component xformOps that don't
        exist or don't have an authored value.

        This method works even on prims with an incompatible xform schema,
        i.e. when the bool operator returns false. When the underlying
        xformable has an incompatible xform schema, it performs a full-on
        matrix decomposition to XYZ rotation order.
        """
    def GetXformVectorsByAccumulation(self, time: pxr.Usd.TimeCode | float | pxr.Sdf.TimeCode) -> tuple:
        """
        Retrieve values of the various component xformOps at a given C{time}.


        Identity values are filled in for the component xformOps that don't
        exist or don't have an authored value.

        This method allows some additional flexibility for xform schemas that
        do not strictly adhere to the xformCommonAPI. For incompatible
        schemas, this method will attempt to reduce the schema into one from
        which component vectors can be extracted by accumulating xformOp
        transforms of the common types.

        When the underlying xformable has a compatible xform schema, the usual
        component value extraction method is used instead. When the xform
        schema is incompatible and it cannot be reduced by accumulating
        transforms, it performs a full-on matrix decomposition to XYZ rotation
        order.
        """
    def SetPivot(self, pivot: pxr.Gf.Vec3f | list[float] | tuple[float, float, float], time: pxr.Usd.TimeCode | float | pxr.Sdf.TimeCode = ...) -> bool:
        """
        Set pivot position at C{time} to C{pivot}.
        """
    def SetResetXformStack(self, resetXformStack: bool) -> bool:
        """
        Set whether the xformable resets the transform stack.


        i.e., does not inherit the parent transformation.
        """
    def SetRotate(self, rotation: pxr.Gf.Vec3f | list[float] | tuple[float, float, float], rotationOrder: XformCommonAPI.RotationOrder = ..., time: pxr.Usd.TimeCode | float | pxr.Sdf.TimeCode = ...) -> bool:
        """
        Set rotation at C{time} to C{rotation}.
        """
    def SetScale(self, scale: pxr.Gf.Vec3f | list[float] | tuple[float, float, float], time: pxr.Usd.TimeCode | float | pxr.Sdf.TimeCode = ...) -> bool:
        """
        Set scale at C{time} to C{scale}.
        """
    def SetTranslate(self, translation: pxr.Gf.Vec3d | list[float] | tuple[float, float, float], time: pxr.Usd.TimeCode | float | pxr.Sdf.TimeCode = ...) -> bool:
        """
        Set translation at C{time} to C{translation}.
        """
    def SetXformVectors(self, translation: pxr.Gf.Vec3d | list[float] | tuple[float, float, float], rotation: pxr.Gf.Vec3f | list[float] | tuple[float, float, float], scale: pxr.Gf.Vec3f | list[float] | tuple[float, float, float], pivot: pxr.Gf.Vec3f | list[float] | tuple[float, float, float], rotationOrder: XformCommonAPI.RotationOrder, time: pxr.Usd.TimeCode | float | pxr.Sdf.TimeCode) -> bool:
        """
        Set values for the various component xformOps at a given C{time}.


        Calling this method will call all of the supported ops to be created,
        even if they only contain default (identity) values.

        To author individual operations selectively, use the Set[OpType]()
        API.

        Once the rotation order has been established for a given xformable
        (either because of an already defined (and compatible) rotate op or
        from calling SetXformVectors() or SetRotate() ), it cannot be changed.
        """
    @staticmethod
    def _GetStaticTfType() -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...

class XformOp(Boost.Python.instance):
    '''
    Schema wrapper for UsdAttribute for authoring and computing
    transformation operations, as consumed by UsdGeomXformable schema.


    The semantics of an op are determined primarily by its name, which
    allows us to decode an op very efficiently. All ops are independent
    attributes, which must live in the"xformOp"property namespace. The
    op\'s primary name within the namespace must be one of
    UsdGeomXformOpTypes, which determines the type of transformation
    operation, and its secondary name (or suffix) within the namespace
    (which is not required to exist), can be any name that distinguishes
    it from other ops of the same type. Suffixes are generally imposed by
    higer level xform API schemas.

    B{On packing order of rotateABC triples}  The order in which the axis
    rotations are recorded in a Vec3* for the six *rotateABC* Euler
    triples B{is always the same:} vec[0] = X, vec[1] = Y, vec[2] = Z. The
    *A*, *B*, *C* in the op name dictate the order in which their
    corresponding elements are consumed by the rotation, not how they are
    laid out.
    '''

    class Precision(pxr.Tf.Tf_PyEnumWrapper):
        _baseName: ClassVar[str] = ...
        allValues: ClassVar[tuple] = ...
        def __init__(self, *args, **kwargs) -> None:
            """Raises an exception
            This class cannot be instantiated from Python
            """
        @staticmethod
        def GetValueFromName(name: object) -> Any: ...

    class Type(pxr.Tf.Tf_PyEnumWrapper):
        _baseName: ClassVar[str] = ...
        allValues: ClassVar[tuple] = ...
        def __init__(self, *args, **kwargs) -> None:
            """Raises an exception
            This class cannot be instantiated from Python
            """
        @staticmethod
        def GetValueFromName(name: object) -> Any: ...
    PrecisionDouble: ClassVar[XformOp.Precision] = ...
    PrecisionFloat: ClassVar[XformOp.Precision] = ...
    PrecisionHalf: ClassVar[XformOp.Precision] = ...
    TypeInvalid: ClassVar[pxr.Tf.Type] = ...
    TypeOrient: ClassVar[pxr.Tf.Type] = ...
    TypeRotateX: ClassVar[pxr.Tf.Type] = ...
    TypeRotateXYZ: ClassVar[pxr.Tf.Type] = ...
    TypeRotateXZY: ClassVar[pxr.Tf.Type] = ...
    TypeRotateY: ClassVar[pxr.Tf.Type] = ...
    TypeRotateYXZ: ClassVar[pxr.Tf.Type] = ...
    TypeRotateYZX: ClassVar[pxr.Tf.Type] = ...
    TypeRotateZ: ClassVar[pxr.Tf.Type] = ...
    TypeRotateZXY: ClassVar[pxr.Tf.Type] = ...
    TypeRotateZYX: ClassVar[pxr.Tf.Type] = ...
    TypeScale: ClassVar[pxr.Tf.Type] = ...
    TypeTransform: ClassVar[pxr.Tf.Type] = ...
    TypeTranslate: ClassVar[pxr.Tf.Type] = ...
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, attr: pxr.Usd.Attribute | ConstraintTarget | Primvar | XformOp | pxr.UsdShade.Input | pxr.UsdShade.Output, isInverseOp: bool = ...) -> None:
        """
        Speculative constructor that will produce a valid UsdGeomXformOp when
        C{attr} already represents an attribute that is XformOp, and produces
        an *invalid* XformOp otherwise (i.e.


        explicit-bool conversion operator will return false).

        Calling C{UsdGeomXformOp::IsXformOp(attr)} will return the same truth
        value as this constructor, but if you plan to subsequently use the
        XformOp anyways, just use this constructor.

        C{isInverseOp} is set to true to indicate an inverse transformation
        op.

        This constructor exists mainly for internal use. Clients should use
        AddXformOp API (or one of Add*Op convenience API) to create and retain
        a copy of an UsdGeomXformOp object.
        """
    def Get(self, time: pxr.Usd.TimeCode | float | pxr.Sdf.TimeCode = ...) -> Any:
        """
        Get the attribute value of the XformOp at C{time}.



        For inverted ops, this returns the raw, uninverted value.
        """
    def GetAttr(self) -> pxr.Usd.Attribute:
        """
        Explicit UsdAttribute extractor.
        """
    def GetBaseName(self) -> str:
        """

        UsdAttribute::GetBaseName()
        """
    def GetName(self) -> str:
        """

        UsdAttribute::GetName()
        """
    def GetNamespace(self) -> str:
        """

        UsdAttribute::GetNamespace()
        """
    def GetNumTimeSamples(self) -> int:
        """
        Returns the number of time samples authored for this xformOp.
        """
    def GetOpName(self) -> str:
        '''
        Returns the opName as it appears in the xformOpOrder attribute.


        This will begin with"!invert!:xformOp:"if it is an inverse xform
        operation. If it is not an inverse xformOp, it will begin
        with\'xformOp:\'.

        This will be empty for an invalid xformOp.
        '''
    def GetOpTransform(self, _time: pxr.Usd.TimeCode | float | pxr.Sdf.TimeCode, /) -> pxr.Gf.Matrix4d:
        """
        Return the 4x4 matrix that applies the transformation encoded in this
        op at C{time}.


        Returns the identity matrix and issues a coding error if the op is
        invalid.

        If the op is valid, but has no authored value, the identity matrix is
        returned and no error is issued.
        """
    def GetOpType(self) -> pxr.Tf.Type:
        """
        Return the operation type of this op, one of UsdGeomXformOp::Type.
        """
    @staticmethod
    def GetOpTypeEnum(_opTypeToken: str | pxr.Ar.ResolvedPath, /) -> pxr.Tf.Type:
        """
        Returns the Type enum associated with the given C{opTypeToken}.
        """
    @staticmethod
    def GetOpTypeToken(_opType: pxr.Tf.Type, /) -> str:
        """
        Returns the TfToken used to encode the given C{opType}.


        Note that an empty TfToken is used to represent TypeInvalid
        """
    def GetPrecision(self) -> XformOp.Precision:
        """
        Returns the precision level of the xform op.
        """
    def GetTimeSamples(self) -> list[float]:
        """
        Populates the list of time samples at which the associated attribute
        is authored.
        """
    def GetTimeSamplesInInterval(self, _interval: pxr.Gf.Interval, /) -> list[float]:
        """
        Populates the list of time samples within the given C{interval}, at
        which the associated attribute is authored.
        """
    def GetTypeName(self) -> pxr.Sdf.ValueTypeName:
        """

        UsdAttribute::GetTypeName()
        """
    def IsDefined(self) -> bool:
        """
        Return true if the wrapped UsdAttribute::IsDefined() , and in addition
        the attribute is identified as a XformOp.
        """
    def IsInverseOp(self) -> bool:
        """
        Returns whether the xformOp represents an inverse operation.
        """
    def MightBeTimeVarying(self) -> bool:
        """
        Determine whether there is any possibility that this op's value may
        vary over time.


        The determination is based on a snapshot of the authored state of the
        op, and may become invalid in the face of further authoring.
        """
    def Set(self, value: Any, time: pxr.Usd.TimeCode | float | pxr.Sdf.TimeCode = ...) -> bool:
        """
        Set the attribute value of the XformOp at C{time}.



        This only works on non-inverse operations. If invoked on an inverse
        xform operation, a coding error is issued and no value is authored.
        """
    def SplitName(self) -> list[str]:
        """

        UsdAttribute::SplitName()
        """
    def __bool__(self) -> bool:
        """
        Explicit bool conversion operator.


        An XformOp object converts to C{true} iff it is valid for querying and
        authoring values and metadata, (which is identically equivalent to
        IsDefined() ), and converts to C{false} otherwise.
        """
    def __eq__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...

class XformOpTypes(Boost.Python.instance):
    orient: ClassVar[str] = ...  # read-only
    resetXformStack: ClassVar[str] = ...  # read-only
    rotateX: ClassVar[str] = ...  # read-only
    rotateXYZ: ClassVar[str] = ...  # read-only
    rotateXZY: ClassVar[str] = ...  # read-only
    rotateY: ClassVar[str] = ...  # read-only
    rotateYXZ: ClassVar[str] = ...  # read-only
    rotateYZX: ClassVar[str] = ...  # read-only
    rotateZ: ClassVar[str] = ...  # read-only
    rotateZXY: ClassVar[str] = ...  # read-only
    rotateZYX: ClassVar[str] = ...  # read-only
    scale: ClassVar[str] = ...  # read-only
    transform: ClassVar[str] = ...  # read-only
    translate: ClassVar[str] = ...  # read-only
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """

class Xformable(Imageable):
    '''
    Base class for all transformable prims, which allows arbitrary
    sequences of component affine transformations to be encoded.



    You may find it useful to review Linear Algebra in UsdGeom while
    reading this class description. B{Supported Component Transformation
    Operations}

    UsdGeomXformable currently supports arbitrary sequences of the
    following operations, each of which can be encoded in an attribute of
    the proper shape in any supported precision:
       - translate - 3D

       - scale - 3D

       - rotateX - 1D angle in degrees

       - rotateY - 1D angle in degrees

       - rotateZ - 1D angle in degrees

       - rotateABC - 3D where ABC can be any combination of the six
         principle Euler Angle sets: XYZ, XZY, YXZ, YZX, ZXY, ZYX. See note on
         rotation packing order

       - orient - 4D (quaternion)

       - transform - 4x4D
         B{Creating a Component Transformation}

    To add components to a UsdGeomXformable prim, simply call AddXformOp()
    with the desired op type, as enumerated in UsdGeomXformOp::Type, and
    the desired precision, which is one of UsdGeomXformOp::Precision.
    Optionally, you can also provide an"op suffix"for the operator that
    disambiguates it from other components of the same type on the same
    prim.  Application-specific transform schemas can use the suffixes to
    fill a role similar to that played by AbcGeom::XformOp\'s"Hint"enums
    for their own round-tripping logic.

    We also provide specific"Add"API for each type, for clarity and
    conciseness, e.g. AddTranslateOp() , AddRotateXYZOp() etc.

    AddXformOp() will return a UsdGeomXformOp object, which is a schema on
    a newly created UsdAttribute that provides convenience API for
    authoring and computing the component transformations. The
    UsdGeomXformOp can then be used to author any number of timesamples
    and default for the op.

    Each successive call to AddXformOp() adds an operator that will be
    applied"more locally"than the preceding operator, just as if we were
    pushing transforms onto a transformation stack - which is precisely
    what should happen when the operators are consumed by a reader.

    If you can, please try to use the UsdGeomXformCommonAPI, which wraps
    the UsdGeomXformable with an interface in which Op creation is taken
    care of for you, and there is a much higher chance that the data you
    author will be importable without flattening into other DCC\'s, as it
    conforms to a fixed set of Scale-Rotate-Translate Ops.

    Using the Authoring API B{Data Encoding and Op Ordering}

    Because there is no"fixed schema"of operations, all of the attributes
    that encode transform operations are dynamic, and are scoped in the
    namespace"xformOp". The second component of an attribute\'s name
    provides the *type* of operation, as listed above.
    An"xformOp"attribute can have additional namespace components derived
    from the *opSuffix* argument to the AddXformOp() suite of methods,
    which provides a preferred way of naming the ops such that we can have
    multiple"translate"ops with unique attribute names. For example, in
    the attribute named"xformOp:translate:maya:pivot","translate"is the
    type of operation and"maya:pivot"is the suffix.

    The following ordered list of attribute declarations in usda define a
    basic Scale-Rotate-Translate with XYZ Euler angles, wherein the
    translation is double-precision, and the remainder of the ops are
    single, in which we will:

       - Scale by 2.0 in each dimension

       - Rotate about the X, Y, and Z axes by 30, 60, and 90 degrees,
         respectively

       - Translate by 100 units in the Y direction
         ::

      float3 xformOp:rotateXYZ = (30, 60, 90)
      float3 xformOp:scale = (2, 2, 2)
      double3 xformOp:translate = (0, 100, 0)
      uniform token[] xformOpOrder = [ "xformOp:translate", "xformOp:rotateXYZ", "xformOp:scale" ]

    The attributes appear in the dictionary order in which USD, by
    default, sorts them. To ensure the ops are recovered and evaluated in
    the correct order, the schema introduces the B{xformOpOrder}
    attribute, which contains the names of the op attributes, in the
    precise sequence in which they should be pushed onto a transform
    stack. B{Note} that the order is opposite to what you might expect,
    given the matrix algebra described in Linear Algebra in UsdGeom. This
    also dictates order of op creation, since each call to AddXformOp()
    adds a new op to the end of the B{xformOpOrder} array, as a new"most-
    local"operation. See Example 2 below for C++ code that could have
    produced this USD.

    If it were important for the prim\'s rotations to be independently
    overridable, we could equivalently (at some performance cost) encode
    the transformation also like so: ::

      float xformOp:rotateX = 30
      float xformOp:rotateY = 60
      float xformOp:rotateZ = 90
      float3 xformOp:scale = (2, 2, 2)
      double3 xformOp:translate = (0, 100, 0)
      uniform token[] xformOpOrder = [ "xformOp:translate", "xformOp:rotateZ", "xformOp:rotateY", "xformOp:rotateX", "xformOp:scale" ]

    Again, note that although we are encoding an XYZ rotation, the three
    rotations appear in the B{xformOpOrder} in the opposite order, with Z,
    followed, by Y, followed by X.

    Were we to add a Maya-style scalePivot to the above example, it might
    look like the following: ::

      float3 xformOp:rotateXYZ = (30, 60, 90)
      float3 xformOp:scale = (2, 2, 2)
      double3 xformOp:translate = (0, 100, 0)
      double3 xformOp:translate:scalePivot
      uniform token[] xformOpOrder = [ "xformOp:translate", "xformOp:rotateXYZ", "xformOp:translate:scalePivot", "xformOp:scale" ]

    B{Paired"Inverted"Ops}

    We have been claiming that the ordered list of ops serves as a set of
    instructions to a transform stack, but you may have noticed in the
    last example that there is a missing operation - the pivot for the
    scale op needs to be applied in its inverse-form as a final (most
    local) op! In the AbcGeom::Xform schema, we would have encoded an
    actual"final"translation op whose value was authored by the exporter
    as the negation of the pivot\'s value. However, doing so would be
    brittle in USD, given that each op can be independently overridden,
    and the constraint that one attribute must be maintained as the
    negation of the other in order for successful re-importation of the
    schema cannot be expressed in USD.

    Our solution leverages the B{xformOpOrder} member of the schema,
    which, in addition to ordering the ops, may also contain one of two
    special tokens that address the paired op and"stack
    resetting"behavior.

    The"paired op"behavior is encoded as an"!invert!"prefix in
    B{xformOpOrder}, as the result of an AddXformOp(isInverseOp=True)
    call.  The B{xformOpOrder} for the last example would look like: ::

      uniform token[] xformOpOrder = [ "xformOp:translate", "xformOp:rotateXYZ", "xformOp:translate:scalePivot", "xformOp:scale", "!invert!xformOp:translate:scalePivot" ]

    When asked for its value via UsdGeomXformOp::GetOpTransform() ,
    an"inverted"Op (i.e. the"inverted"half of a set of paired Ops) will
    fetch the value of its paired attribute and return its negation. This
    works for all op types - an error will be issued if a"transform"type
    op is singular and cannot be inverted. When getting the authored value
    of an inverted op via UsdGeomXformOp::Get() , the raw, uninverted
    value of the associated attribute is returned.

    For the sake of robustness, B{setting a value on an inverted op is
    disallowed.} Attempting to set a value on an inverted op will result
    in a coding error and no value being set.

    B{Resetting the Transform Stack}

    The other special op/token that can appear in *xformOpOrder* is
    *"!resetXformStack!"*, which, appearing as the first element of
    *xformOpOrder*, indicates this prim should not inherit the
    transformation of its namespace parent. See SetResetXformStack()

    B{Expected Behavior for"Missing"Ops}

    If an importer expects Scale-Rotate-Translate operations, but a prim
    has only translate and rotate ops authored, the importer should assume
    an identity scale. This allows us to optimize the data a bit, if only
    a few components of a very rich schema (like Maya\'s) are authored in
    the app.

    B{Using the C++ API}

    #1. Creating a simple transform matrix encoding ::

      bool CreateMatrixWithDefault(UsdGeomXformable const  & gprim, GfMatrix4d const  & defValue)
      {
          if (UsdGeomXformOp transform = gprim.MakeMatrixXform()){
              return transform.Set(defValue, UsdTimeCode::Default());
          } else {
              return false;
          }
      }

    #2. Creating the simple SRT from the example above ::

      bool CreateExampleSRT(UsdGeomXformable const  & gprim)
      {
          // For insurance, we will make sure there aren\'t any ordered ops
          // before we start
          gprim.ClearXformOpOrder();
  
          UsdGeomXformOp s, r, t;
      
          if ( !(t = gprim.AddTranslateOp())){
              return false;
          }
          if ( !(r = gprim.AddRotateXYZOp())){
              return false;
          }
          if ( !(s = gprim.AddScaleOp())){
              return false;
          }
  
          return (t.Set(GfVec3d(0, 100, 0), UsdTimeCode::Default()) &&
                  r.Set(GfVec3f(30, 60, 90), UsdTimeCode::Default()) &&
                  s.Set(GfVec3f(2, 2, 2), UsdTimeCode::Default()));
      }

    #3. Creating a parameterized SRT with pivot using
    UsdGeomXformCommonAPI ::

      bool CreateSRTWithDefaults(UsdGeomXformable const  & gprim, 
                                 GfVec3d const  & defTranslate,
                                 GfVec3f const  & defRotateXYZ,
                                 GfVec3f const  & defScale,
                                 GfVec3f const  & defPivot)
      {
          if (UsdGeomXformCommonAPI xform = UsdGeomXformCommonAPI(gprim)){
              return xform.SetXformVectors(defTranslate, defRotateXYZ, defScale,
                                           defPivot, UsdGeomXformCommonAPI::RotationOrderXYZ,
                                           UsdTimeCode::Default());
          } else {
              return false;
          }
      }

    #4. Creating a rotate-only pivot transform with animated rotation and
    translation ::

      bool CreateAnimatedTransform(UsdGeomXformable const  & gprim, 
                                   GfVec3d const  & baseTranslate,
                                   GfVec3f const  & baseRotateXYZ,
                                   GfVec3f const  & defPivot)
      {
          // Only need to do this if you\'re overriding an existing scene
          if (!gprim.ClearXformOpOrder()){
              return false;
          }
      
          static const TfToken  pivSuffix("pivot");
          UsdGeomXformOp    trans = gprim.AddTranslateOp();
          UsdGeomXformOp    pivot = gprim.AddTranslateOp(UsdGeomXformOp::PrecisionFloat,
                                                         pivSuffix);
          UsdGeomXformOp   rotate = gprim.AddRotateXYZOp();
          UsdGeomXformOp pivotInv = gprim.AddTranslateOp(UsdGeomXformOp::PrecisionFloat,
                                                         pivSuffix,
                                                         /* isInverseOp = */ true);
          // Now that we have created all the ops, set default values.
          // Note that we do not need to (and cannot) set the value
          // for the pivot\'s inverse op.
          // For didactic brevity we are eliding success return value checks,
          // but would absolutely have them in exporters!
          trans.Set(baseTranslate, UsdTimeCode::Default());
          pivot.Set(defPivot, UsdTimeCode::Default());
          rotate.Set(baseRotateXYZ, UsdTimeCode::Default());
      
          // Now animate the translation and rotation over a fixed interval with
          // cheesy linear animation.
          GfVec3d  position(baseTranslate);
          GfVec3f  rotation(baseRotateXYZ);
      
          for (double frame = 0; frame < 100.0; frame += 1.0){
              trans.Set(position, frame);
              rotate.Set(rotation, frame);
              position[0] += 5.0;
              rotation[2] += 7.0;
          }
          return true;
      }

    '''
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None:
        """
        Construct a UsdGeomXformable on UsdPrim C{prim}.


        Equivalent to UsdGeomXformable::Get (prim.GetStage(), prim.GetPath())
        for a *valid* C{prim}, but will not immediately throw an error for an
        invalid C{prim}
        """
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None:
        """
        Construct a UsdGeomXformable on the prim held by C{schemaObj}.


        Should be preferred over UsdGeomXformable (schemaObj.GetPrim()), as it
        preserves SchemaBase state.
        """
    def AddOrientOp(self, precision: XformOp.Precision = ..., opSuffix: str | pxr.Ar.ResolvedPath = ..., isInverseOp: bool = ...) -> XformOp:
        """
        Add a orient op (arbitrary axis/angle rotation) to the local stack
        represented by this xformable.



        AddXformOp()
        """
    def AddRotateXOp(self, precision: XformOp.Precision = ..., opSuffix: str | pxr.Ar.ResolvedPath = ..., isInverseOp: bool = ...) -> XformOp:
        """
        Add a rotation about the X-axis to the local stack represented by this
        xformable.


        Set the angle value of the resulting UsdGeomXformOp B{in degrees}

        AddXformOp()
        """
    def AddRotateXYZOp(self, precision: XformOp.Precision = ..., opSuffix: str | pxr.Ar.ResolvedPath = ..., isInverseOp: bool = ...) -> XformOp:
        """
        Add a rotation op with XYZ rotation order to the local stack
        represented by this xformable.


        Set the angle value of the resulting UsdGeomXformOp B{in degrees}

        AddXformOp() , note on angle packing order
        """
    def AddRotateXZYOp(self, precision: XformOp.Precision = ..., opSuffix: str | pxr.Ar.ResolvedPath = ..., isInverseOp: bool = ...) -> XformOp:
        """
        Add a rotation op with XZY rotation order to the local stack
        represented by this xformable.


        Set the angle values of the resulting UsdGeomXformOp B{in degrees}

        AddXformOp() , note on angle packing order
        """
    def AddRotateYOp(self, precision: XformOp.Precision = ..., opSuffix: str | pxr.Ar.ResolvedPath = ..., isInverseOp: bool = ...) -> XformOp:
        """
        Add a rotation about the Y-axis to the local stack represented by this
        xformable.


        Set the angle value of the resulting UsdGeomXformOp B{in degrees}

        AddXformOp()
        """
    def AddRotateYXZOp(self, precision: XformOp.Precision = ..., opSuffix: str | pxr.Ar.ResolvedPath = ..., isInverseOp: bool = ...) -> XformOp:
        """
        Add a rotation op with YXZ rotation order to the local stack
        represented by this xformable.


        Set the angle values of the resulting UsdGeomXformOp B{in degrees}

        AddXformOp() , note on angle packing order
        """
    def AddRotateYZXOp(self, precision: XformOp.Precision = ..., opSuffix: str | pxr.Ar.ResolvedPath = ..., isInverseOp: bool = ...) -> XformOp:
        """
        Add a rotation op with YZX rotation order to the local stack
        represented by this xformable.


        Set the angle values of the resulting UsdGeomXformOp B{in degrees}

        AddXformOp() , note on angle packing order
        """
    def AddRotateZOp(self, precision: XformOp.Precision = ..., opSuffix: str | pxr.Ar.ResolvedPath = ..., isInverseOp: bool = ...) -> XformOp:
        """
        Add a rotation about the Z-axis to the local stack represented by this
        xformable.



        AddXformOp()
        """
    def AddRotateZXYOp(self, precision: XformOp.Precision = ..., opSuffix: str | pxr.Ar.ResolvedPath = ..., isInverseOp: bool = ...) -> XformOp:
        """
        Add a rotation op with ZXY rotation order to the local stack
        represented by this xformable.


        Set the angle values of the resulting UsdGeomXformOp B{in degrees}

        AddXformOp() , note on angle packing order
        """
    def AddRotateZYXOp(self, precision: XformOp.Precision = ..., opSuffix: str | pxr.Ar.ResolvedPath = ..., isInverseOp: bool = ...) -> XformOp:
        """
        Add a rotation op with ZYX rotation order to the local stack
        represented by this xformable.


        Set the angle values of the resulting UsdGeomXformOp B{in degrees}

        AddXformOp() , note on angle packing order
        """
    def AddScaleOp(self, precision: XformOp.Precision = ..., opSuffix: str | pxr.Ar.ResolvedPath = ..., isInverseOp: bool = ...) -> XformOp:
        """
        Add a scale operation to the local stack represented by this
        xformable.



        AddXformOp()
        """
    def AddTransformOp(self, precision: XformOp.Precision = ..., opSuffix: str | pxr.Ar.ResolvedPath = ..., isInverseOp: bool = ...) -> XformOp:
        """
        Add a tranform op (4x4 matrix transformation) to the local stack
        represented by this xformable.



        AddXformOp() Note: This method takes a precision argument only to be
        consistent with the other types of xformOps. The only valid precision
        here is double since matrix values cannot be encoded in floating-pt
        precision in Sdf.
        """
    def AddTranslateOp(self, precision: XformOp.Precision = ..., opSuffix: str | pxr.Ar.ResolvedPath = ..., isInverseOp: bool = ...) -> XformOp:
        """
        Add a translate operation to the local stack represented by this
        xformable.



        AddXformOp()
        """
    def AddXformOp(self, opType: XformOp.Type, precision: XformOp.Precision = ..., opSuffix: str | pxr.Ar.ResolvedPath = ..., isInverseOp: bool = ...) -> XformOp:
        '''
        Add an affine transformation to the local stack represented by this
        Xformable.


        This will fail if there is already a transform operation of the same
        name in the ordered ops on this prim (i.e. as returned by
        GetOrderedXformOps() ), or if an op of the same name exists at all on
        the prim with a different precision than that specified.

        The newly created operation will become the most-locally applied
        transformation on the prim, and will appear last in the list returned
        by GetOrderedXformOps() . It is OK to begin authoring values to the
        returned UsdGeomXformOp immediately, interspersed with subsequent
        calls to AddXformOp() - just note the order of application, which
        *can* be changed at any time (and in stronger layers) via
        SetXformOpOrder() .

        opType

        is the type of transform operation, one of UsdGeomXformOp::Type.
        precision

        allows you to specify the precision with which you desire to encode
        the data. This should be one of the values in the enum
        UsdGeomXformOp::Precision. opSuffix

        allows you to specify the purpose/meaning of the op in the stack. When
        opSuffix is specified, the associated attribute\'s name is set
        to"xformOp:<opType>:<opSuffix>". isInverseOp

        is used to indicate an inverse transformation operation.

        a UsdGeomXformOp that can be used to author to the operation. An error
        is issued and the returned object will be invalid (evaluate to false)
        if the op being added already exists in xformOpOrder or if the
        arguments supplied are invalid.

        If the attribute associated with the op already exists, but isn\'t of
        the requested precision, a coding error is issued, but a valid xformOp
        is returned with the existing attribute.
        '''
    def ClearXformOpOrder(self) -> bool:
        """
        Clears the local transform stack.
        """
    def CreateXformOpOrderAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetXformOpOrderAttr() , and also Create vs Get Property Methods
        for when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    @staticmethod
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> Xformable:
        """
        Return a UsdGeomXformable holding the prim adhering to this schema at
        C{path} on C{stage}.


        If no prim exists at C{path} on C{stage}, or if the prim at that path
        does not adhere to this schema, return an invalid schema object. This
        is shorthand for the following: ::

          UsdGeomXformable(stage->GetPrimAtPath(path));

        """
    @overload
    def GetLocalTransformation(self, time: pxr.Usd.TimeCode | float | pxr.Sdf.TimeCode = ...) -> pxr.Gf.Matrix4d:
        """
        Computes the fully-combined, local-to-parent transformation for this
        prim.


        If a client does not need to manipulate the individual ops themselves,
        and requires only the combined transform on this prim, this method
        will take care of all the data marshalling and linear algebra needed
        to combine the ops into a 4x4 affine transformation matrix, in double-
        precision, regardless of the precision of the op inputs.

        transform

        is the output parameter that will hold the local transform.
        resetsXformStack

        is the output parameter that informs client whether they need to reset
        the transform stack before pushing C{transform}. time

        is the UsdTimeCode at which to sample the ops.

        true on success, false if there was an error reading data.

        A coding error is issued if C{transform} or C{resetsXformStack} is
        None.
        """
    @overload
    def GetLocalTransformation(self, ops: typing.Iterable[XformOp], time: pxr.Usd.TimeCode | float | pxr.Sdf.TimeCode = ...) -> pxr.Gf.Matrix4d:
        """
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        Computes the fully-combined, local-to-parent transformation for this
        prim as efficiently as possible, using a pre-fetched (cached) list of
        ordered xform ops supplied by the client.


        transform

        is the output parameter that will hold the local transform.
        resetsXformStack

        is the output parameter that informs client whether they need to reset
        the transform stack before pushing C{transform}. ops

        is the ordered set of xform ops for this prim, and will be queried
        without any validity checking. Passing this in can save significant
        value-resolution costs, if the client is able to retain this data from
        a call to GetOrderedXformOps() . time

        is the UsdTimeCode at which to sample the ops.

        true on success, false if there was an error reading data.

        A coding error is issued if C{transform} or C{resetsXformStack} is
        None.
        """
    def GetOrderedXformOps(self) -> list:
        '''
        Return the ordered list of transform operations to be applied to this
        prim, in least-to-most-local order.


        This is determined by the intersection of authored op-attributes and
        the explicit ordering of those attributes encoded in the
        C{xformOpOrder} attribute on this prim. Any entries in C{xformOpOrder}
        that do not correspond to valid attributes on the xformable prim are
        skipped and a warning is issued.

        A UsdGeomTransformable that has not had any ops added via AddXformOp()
        will return an empty vector.

        The function also sets C{resetsXformStack} to true
        if"!resetXformStack!"appears *anywhere* in xformOpOrder (i.e., if the
        prim resets its parent\'s inherited transformation).

        A coding error is issued if resetsXformStack is None.

        GetResetXformStack()
        '''
    def GetOrientOp(self, opSuffix: str | pxr.Ar.ResolvedPath = ..., isInverseOp: bool = ...) -> XformOp:
        """
        Get an orient op (arbitrary axis/angle rotation) from the local stack
        represented by this xformable.



        GetXformOp()
        """
    def GetResetXformStack(self) -> bool:
        '''
        Does this prim reset its parent\'s inherited transformation?


        Returns true if"!resetXformStack!"appears *anywhere* in xformOpOrder.
        When this returns true, all ops upto the last"!resetXformStack!"in
        xformOpOrder are ignored when computing the local transformation.
        '''
    def GetRotateXOp(self, opSuffix: str | pxr.Ar.ResolvedPath = ..., isInverseOp: bool = ...) -> XformOp:
        """
        Get a rotation about the X-axis from the local stack represented by
        this xformable.



        GetXformOp()
        """
    def GetRotateXYZOp(self, opSuffix: str | pxr.Ar.ResolvedPath = ..., isInverseOp: bool = ...) -> XformOp:
        """
        Get a rotation op with XYZ rotation order from the local stack
        represented by this xformable.



        GetXformOp() , note on angle packing order
        """
    def GetRotateXZYOp(self, opSuffix: str | pxr.Ar.ResolvedPath = ..., isInverseOp: bool = ...) -> XformOp:
        """
        Get a rotation op with XZY rotation order from the local stack
        represented by this xformable.



        GetXformOp() , note on angle packing order
        """
    def GetRotateYOp(self, opSuffix: str | pxr.Ar.ResolvedPath = ..., isInverseOp: bool = ...) -> XformOp:
        """
        Get a rotation about the Y-axis from the local stack represented by
        this xformable.



        GetXformOp()
        """
    def GetRotateYXZOp(self, opSuffix: str | pxr.Ar.ResolvedPath = ..., isInverseOp: bool = ...) -> XformOp:
        """
        Get a rotation op with YXZ rotation order from the local stack
        represented by this xformable.



        GetXformOp() , note on angle packing order
        """
    def GetRotateYZXOp(self, opSuffix: str | pxr.Ar.ResolvedPath = ..., isInverseOp: bool = ...) -> XformOp:
        """
        Get a rotation op with YZX rotation order from the local stack
        represented by this xformable.



        GetXformOp() , note on angle packing order
        """
    def GetRotateZOp(self, opSuffix: str | pxr.Ar.ResolvedPath = ..., isInverseOp: bool = ...) -> XformOp:
        """
        Get a rotation about the Z-axis from the local stack represented by
        this xformable.



        GetXformOp()
        """
    def GetRotateZXYOp(self, opSuffix: str | pxr.Ar.ResolvedPath = ..., isInverseOp: bool = ...) -> XformOp:
        """
        Get a rotation op with ZXY rotation order from the local stack
        represented by this xformable.



        GetXformOp() , note on angle packing order
        """
    def GetRotateZYXOp(self, opSuffix: str | pxr.Ar.ResolvedPath = ..., isInverseOp: bool = ...) -> XformOp:
        """
        Get a rotation op with ZYX rotation order from the local stack
        represented by this xformable.



        GetXformOp() , note on angle packing order
        """
    def GetScaleOp(self, opSuffix: str | pxr.Ar.ResolvedPath = ..., isInverseOp: bool = ...) -> XformOp:
        """
        Get a scale operation from the local stack represented by this
        xformable.



        GetXformOp()
        """
    @staticmethod
    def GetSchemaAttributeNames(includeInherited: bool = ...) -> list[str]:
        """
        Return a vector of names of all pre-declared attributes for this
        schema class and all its ancestor classes.


        Does not include attributes that may be authored by custom/extended
        methods of the schemas involved.
        """
    def GetTimeSamples(self) -> list[float]:
        """
        Sets C{times} to the union of all the timesamples at which xformOps
        that are included in the xformOpOrder attribute are authored.


        This clears the C{times} vector before accumulating sample times from
        all the xformOps.

        UsdAttribute::GetTimeSamples
        """
    def GetTimeSamplesInInterval(self, _interval: pxr.Gf.Interval, /) -> list[float]:
        """
        Sets C{times} to the union of all the timesamples in the interval,
        C{interval}, at which xformOps that are included in the xformOpOrder
        attribute are authored.


        This clears the C{times} vector before accumulating sample times from
        all the xformOps.

        UsdAttribute::GetTimeSamples
        """
    def GetTransformOp(self, opSuffix: str | pxr.Ar.ResolvedPath = ..., isInverseOp: bool = ...) -> XformOp:
        """
        Get a tranform op (4x4 matrix transformation) from the local stack
        represented by this xformable.



        GetXformOp()
        """
    def GetTranslateOp(self, opSuffix: str | pxr.Ar.ResolvedPath = ..., isInverseOp: bool = ...) -> XformOp:
        """
        Get a translate operation from the local stack represented by this
        xformable.



        GetXformOp()
        """
    def GetXformOp(self, opType: XformOp.Type, opSuffix: str | pxr.Ar.ResolvedPath = ..., isInverseOp: bool = ...) -> XformOp:
        '''
        Get an affine transformation from the local stack represented by this
        Xformable.


        This will return an invalid op if there is no transform operation of
        the same name in the ordered ops on this prim (i.e. as returned by
        GetOrderedXformOps() )

        opType

        is the type of transform operation, one of UsdGeomXformOp::Type.
        opSuffix

        specifies the purpose/meaning of the op in the stack. When opSuffix is
        specified, the associated attribute\'s name
        is"xformOp:<opType>:<opSuffix>". isInverseOp

        is used to indicate an inverse transformation operation.

        a UsdGeomXformOp with the specified attributes. The returned object
        will be invalid (evaluate to false) if the op requested does not exist
        in xformOpOrder or if the arguments supplied are invalid.
        '''
    def GetXformOpOrderAttr(self) -> pxr.Usd.Attribute:
        """
        Encodes the sequence of transformation operations in the order in
        which they should be pushed onto a transform stack while visiting a
        UsdStage 's prims in a graph traversal that will effect the desired
        positioning for this prim and its descendant prims.


        You should rarely, if ever, need to manipulate this attribute
        directly. It is managed by the AddXformOp() , SetResetXformStack() ,
        and SetXformOpOrder() , and consulted by GetOrderedXformOps() and
        GetLocalTransformation() .

        Declaration

        C{uniform token[] xformOpOrder}

        C++ Type

        VtArray<TfToken>

        Usd Type

        SdfValueTypeNames->TokenArray

        Variability

        SdfVariabilityUniform
        """
    @staticmethod
    def IsTransformationAffectedByAttrNamed(_attrName: str | pxr.Ar.ResolvedPath, /) -> bool:
        """
        Returns true if the attribute named C{attrName} could affect the local
        transformation of an xformable prim.
        """
    def MakeMatrixXform(self) -> XformOp:
        """
        Clears the existing local transform stack and creates a new xform op
        of type'transform'.


        This API is provided for convenience since this is the most common
        xform authoring operation.

        ClearXformOpOrder()

        AddTransformOp()
        """
    def SetResetXformStack(self, resetXform: bool) -> bool:
        '''
        Specify whether this prim\'s transform should reset the transformation
        stack inherited from its parent prim.



        By default, parent transforms are inherited. SetResetXformStack() can
        be called at any time during authoring, but will always add
        a\'!resetXformStack!\'op as the *first* op in the ordered list, if one
        does not exist already. If one already exists, and C{resetXform} is
        false, it will remove all ops upto and including the
        last"!resetXformStack!"op.
        '''
    def SetXformOpOrder(self, orderedXformOps: typing.Iterable[XformOp], resetXformStack: bool = ...) -> bool:
        '''
        Reorder the already-existing transform ops on this prim.


        All elements in C{orderedXformOps} must be valid and represent
        attributes on this prim. Note that it is *not* required that all the
        existing operations be present in C{orderedXformOps}, so this method
        can be used to completely change the transformation structure applied
        to the prim.

        If C{resetXformStack} is set to true, then "!resetXformOp! will be set
        as the first op in xformOpOrder, to indicate that the prim does not
        inherit its parent\'s transformation.

        If you wish to re-specify a prim\'s transformation completely in a
        stronger layer, you should first call this method with an *empty*
        C{orderedXformOps} vector. From there you can call AddXformOp() just
        as if you were authoring to the prim from scratch.

        false if any of the elements of C{orderedXformOps} are not extant on
        this prim, or if an error occurred while authoring the ordering
        metadata. Under either condition, no scene description is authored.

        GetOrderedXformOps()
        '''
    @overload
    def TransformMightBeTimeVarying(self) -> bool:
        """
        Determine whether there is any possibility that this prim's *local*
        transformation may vary over time.


        The determination is based on a snapshot of the authored state of the
        op attributes on the prim, and may become invalid in the face of
        further authoring.
        """
    @overload
    def TransformMightBeTimeVarying(self, _ops: typing.Iterable[XformOp], /) -> bool:
        """
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        Determine whether there is any possibility that this prim's *local*
        transformation may vary over time, using a pre-fetched (cached) list
        of ordered xform ops supplied by the client.


        The determination is based on a snapshot of the authored state of the
        op attributes on the prim, and may become invalid in the face of
        further authoring.
        """
    @staticmethod
    def _GetStaticTfType() -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...

class _CanApplyResult(Boost.Python.instance):
    __instance_size__: ClassVar[int] = ...
    def __init__(self, arg2: bool, arg3: object, /) -> None: ...
    def __bool__(self) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    def __getitem__(self, arg2: int, /) -> Any: ...
    def __ne__(self, other: object) -> bool: ...
    @property
    def whyNot(self): ...

def GetFallbackUpAxis() -> str:
    '''
    Return the site-level fallback up axis as a TfToken.


    In a generic installation of USD, the fallback will be"Y". This can be
    changed to"Z"by adding, in a plugInfo.json file discoverable by USD\'s
    PlugPlugin mechanism: ::

      "UsdGeomMetrics": {
          "upAxis": "Z"
      }

    If more than one such entry is discovered and the values for upAxis
    differ, we will issue a warning during the first call to this
    function, and ignore all of them, so that we devolve to deterministic
    behavior of Y up axis until the problem is rectified.
    '''
def GetStageMetersPerUnit(stage: pxr.Usd.Stage) -> float:
    """
    Return *stage* 's authored *metersPerUnit*, or 0.01 if unauthored.



    Encoding Stage Linear Units
    """
def GetStageUpAxis(stage: pxr.Usd.Stage) -> str:
    """
    Fetch and return C{stage} 's upAxis.


    If unauthored, will return the value provided by
    UsdGeomGetFallbackUpAxis() . Exporters, however, are strongly
    encouraged to always set the upAxis for every USD file they create.

    one of: UsdGeomTokens->y or UsdGeomTokens->z, unless there was an
    error, in which case returns an empty TfToken

    Encoding Stage UpAxis
    """
def LinearUnitsAre(authoredUnits: float, standardUnits: float, epsilon: float = ...) -> bool:
    """
    Return *true* if the two given metrics are within the provided
    relative *epsilon* of each other, when you need to know an absolute
    metric rather than a scaling factor.



    Use like so: ::

      double stageUnits = UsdGeomGetStageMetersPerUnit(stage);
  
      if (UsdGeomLinearUnitsAre(stageUnits, UsdGeomLinearUnits::meters))
          // do something for meters
      else if (UsdGeomLinearUnitsAre(stageUnits, UsdGeomLinearUnits::feet))
          // do something for feet

    *false* if either input is zero or negative, otherwise relative
    floating-point comparison between the two inputs.

    Encoding Stage Linear Units
    """
def SetStageMetersPerUnit(stage: pxr.Usd.Stage, metersPerUnit: float) -> bool:
    """
    Author *stage* 's *metersPerUnit*.



    true if metersPerUnit was successfully set. The stage's UsdEditTarget
    must be either its root layer or session layer.

    Encoding Stage Linear Units
    """
def SetStageUpAxis(stage: pxr.Usd.Stage, upAxis: str | pxr.Ar.ResolvedPath) -> bool:
    """
    Set C{stage} 's upAxis to C{axis}, which must be one of
    UsdGeomTokens->y or UsdGeomTokens->z.


    UpAxis is stage-level metadata, therefore see UsdStage::SetMetadata()
    .

    true if upAxis was successfully set. The stage's UsdEditTarget must be
    either its root layer or session layer.

    Encoding Stage UpAxis
    """
def StageHasAuthoredMetersPerUnit(stage: pxr.Usd.Stage) -> bool:
    """
    Return whether *stage* has an authored *metersPerUnit*.



    Encoding Stage Linear Units
    """
