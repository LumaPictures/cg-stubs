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

class AssetPreviewsAPI(pxr.Usd.APISchemaBase):
    '''
    AssetPreviewsAPI is the interface for authoring and accessing
    precomputed, lightweight previews of assets.


    It is an applied schema, which means that an arbitrary number of prims
    on a stage can have the schema applied and therefore can contain
    previews; however, to access a stage\'s"default"previews, one consults
    the stage\'s C{defaultPrim}.

    AssetPreviewsAPI supports the following kinds of previews:
       - B{thumbnails} : a set of pre-rendered images of the asset. There
         is no prescribed size for thumbnail images, but care should be taken
         to ensure their inclusion does not substantially increase the overall
         size of an asset, as, for example, when packaged into USDZ.

    Although the UsdMediaAssetPreviewsAPI class can be used to interrogate
    any prim, no query in the API will succeed unless the schema has been
    applied to the prim. This schema deals only with asset paths, and
    clients wishing to directly consume the returned data must do so by
    retrieving an ArAsset from the session\'s ArAssetResolver.

    The schema defines no properties or metadata fallback values. Rather,
    Asset Previews are encoded as part of a prim\'s C{assetInfo} metadata.
    A default thumbnail image would look like: ::

      1.    assetInfo = {
      2.      dictionary previews = {
      3.          dictionary thumbnails = {
      4.              dictionary default = {
      5.                  asset defaultImage = @chair_thumb.jpg@
      6.              }
      7.          }
      8.      }
      9.    }

    '''

    class Thumbnails(Boost.Python.instance):
        '''
        Thumbnails is a value type that serves as schema to aid in
        serialization and deserialization of thumbnail images in the
        assetInfo["thumbnails"] dictionary.
        '''
        __instance_size__: ClassVar[int] = ...
        defaultImage: Incomplete
        def __init__(self, defaultImage: pxr.Sdf.AssetPath | str = ...) -> None: ...
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None:
        """
        Construct a UsdMediaAssetPreviewsAPI on UsdPrim C{prim}.


        Equivalent to UsdMediaAssetPreviewsAPI::Get (prim.GetStage(),
        prim.GetPath()) for a *valid* C{prim}, but will not immediately throw
        an error for an invalid C{prim}
        """
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None:
        """
        Construct a UsdMediaAssetPreviewsAPI on the prim held by C{schemaObj}.


        Should be preferred over UsdMediaAssetPreviewsAPI
        (schemaObj.GetPrim()), as it preserves SchemaBase state.
        """
    @staticmethod
    def Apply(prim: pxr.Usd.Prim) -> AssetPreviewsAPI:
        '''
        Applies this B{single-apply} API schema to the given C{prim}.


        This information is stored by adding"AssetPreviewsAPI"to the token-
        valued, listOp metadata *apiSchemas* on the prim.

        A valid UsdMediaAssetPreviewsAPI object is returned upon success. An
        invalid (or empty) UsdMediaAssetPreviewsAPI object is returned upon
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
    def ClearDefaultThumbnails(self) -> None:
        """
        Remove the entire entry for default Thumbnails in the current
        UsdEditTarget.
        """
    @staticmethod
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> AssetPreviewsAPI:
        """
        Return a UsdMediaAssetPreviewsAPI holding the prim adhering to this
        schema at C{path} on C{stage}.


        If no prim exists at C{path} on C{stage}, or if the prim at that path
        does not adhere to this schema, return an invalid schema object. This
        is shorthand for the following: ::

          UsdMediaAssetPreviewsAPI(stage->GetPrimAtPath(path));

        """
    @overload
    @staticmethod
    def GetAssetDefaultPreviews(layerPath: str | pxr.Ar.ResolvedPath) -> AssetPreviewsAPI:
        """
        Return a schema object that can be used to interrogate previews for
        the default prim of the stage constructed from C{layerPath}.


        The schema object will create and retain a minimal stage required for
        interrogation. This is equivalent to:
        C{GetAssetDefaultPreviews(SdfLayer::FindOrOpen(layerPath))}
        """
    @overload
    @staticmethod
    def GetAssetDefaultPreviews(layer: pxr.Sdf.Layer) -> AssetPreviewsAPI:
        """
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        """
    def GetDefaultThumbnails(self) -> AssetPreviewsAPI.Thumbnails:
        """
        Fetch the default Thumbnails data, returning C{true} if data was
        successfully fetched.
        """
    @staticmethod
    def GetSchemaAttributeNames(includeInherited: bool = ...) -> list[str]:
        """
        Return a vector of names of all pre-declared attributes for this
        schema class and all its ancestor classes.


        Does not include attributes that may be authored by custom/extended
        methods of the schemas involved.
        """
    def SetDefaultThumbnails(self, thumbnails: AssetPreviewsAPI.Thumbnails) -> None:
        """
        Author the default thumbnails dictionary from the provided Thumbnails
        data.
        """
    @staticmethod
    def _GetStaticTfType() -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...

class SpatialAudio(pxr.UsdGeom.Xformable):
    '''
    The SpatialAudio primitive defines basic properties for encoding
    playback of an audio file or stream within a USD Stage.


    The SpatialAudio schema derives from UsdGeomXformable since it can
    support full spatial audio while also supporting non-spatial mono and
    stereo sounds. One or more SpatialAudio prims can be placed anywhere
    in the namespace, though it is advantageous to place truly spatial
    audio prims under/inside the models from which the sound emanates, so
    that the audio prim need only be transformed relative to the model,
    rather than copying its animation.

    Timecode Attributes and Time Scaling
    ====================================

    *startTime* and *endTime* are timecode valued attributes which gives
    them the special behavior that layer offsets affecting the layer in
    which one of these values is authored are applied to the attribute\'s
    value itself during value resolution. This allows audio playback to be
    kept in sync with time sampled animation as the animation is affected
    by layer offsets in the composition. But this behavior brings with it
    some interesting edge cases and caveats when it comes to layer offsets
    that include scale.

    Although authored layer offsets may have a time scale which can scale
    the duration between an authored *startTime* and *endTime*, we make no
    attempt to infer any playback dilation of the actual audio media
    itself. Given that *startTime* and *endTime* can be independently
    authored in different layers with differing time scales, it is not
    possible, in general, to define an"original timeframe"from which we
    can compute a dilation to composed stage-time. Even if we could
    compute a composed dilation this way, it would still be impossible to
    flatten a stage or layer stack into a single layer and still retain
    the composed audio dilation using this schema.

    Although we do not expect it to be common, it is possible to apply a
    negative time scale to USD layers, which mostly has the effect of
    reversing animation in the affected composition. If a negative scale
    is applied to a composition that contains authored *startTime* and
    *endTime*, it will reverse their relative ordering in time. Therefore,
    we stipulate when *playbackMode*
    is"onceFromStartToEnd"or"loopFromStartToEnd", if *endTime* is less
    than *startTime*, then begin playback at *endTime*, and continue until
    *startTime*. When *startTime* and *endTime* are inverted, we do not,
    however, stipulate that playback of the audio media itself be
    inverted, since doing so"successfully"would require perfect knowledge
    of when, within the audio clip, relevant audio ends (so that we know
    how to offset the reversed audio to align it so that we reach
    the"beginning"at *startTime*), and sounds played in reverse are not
    likely to produce desirable results.

    For any described attribute *Fallback* *Value* or *Allowed* *Values*
    below that are text/tokens, the actual token is published and defined
    in UsdMediaTokens. So to set an attribute to the value"rightHanded",
    use UsdMediaTokens->rightHanded as the value.
    '''
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None:
        """
        Construct a UsdMediaSpatialAudio on UsdPrim C{prim}.


        Equivalent to UsdMediaSpatialAudio::Get (prim.GetStage(),
        prim.GetPath()) for a *valid* C{prim}, but will not immediately throw
        an error for an invalid C{prim}
        """
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None:
        """
        Construct a UsdMediaSpatialAudio on the prim held by C{schemaObj}.


        Should be preferred over UsdMediaSpatialAudio (schemaObj.GetPrim()),
        as it preserves SchemaBase state.
        """
    def CreateAuralModeAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetAuralModeAttr() , and also Create vs Get Property Methods for
        when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateEndTimeAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetEndTimeAttr() , and also Create vs Get Property Methods for
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
    def CreateGainAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetGainAttr() , and also Create vs Get Property Methods for when
        to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateMediaOffsetAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetMediaOffsetAttr() , and also Create vs Get Property Methods for
        when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreatePlaybackModeAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetPlaybackModeAttr() , and also Create vs Get Property Methods
        for when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateStartTimeAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetStartTimeAttr() , and also Create vs Get Property Methods for
        when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    @staticmethod
    def Define(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> SpatialAudio:
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
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> SpatialAudio:
        """
        Return a UsdMediaSpatialAudio holding the prim adhering to this schema
        at C{path} on C{stage}.


        If no prim exists at C{path} on C{stage}, or if the prim at that path
        does not adhere to this schema, return an invalid schema object. This
        is shorthand for the following: ::

          UsdMediaSpatialAudio(stage->GetPrimAtPath(path));

        """
    def GetAuralModeAttr(self) -> pxr.Usd.Attribute:
        '''
        Determines how audio should be played.


        Valid values are:
           - spatial: Play the audio in 3D space if the device can support
             spatial audio. if not, fall back to mono.

           - nonSpatial: Play the audio without regard to the SpatialAudio
             prim\'s position. If the audio media contains any form of stereo or
             other multi-channel sound, it is left to the application to determine
             whether the listener\'s position should be taken into account. We
             expect nonSpatial to be the choice for ambient sounds and music sound-
             tracks.

        Declaration

        C{uniform token auralMode ="spatial"}

        C++ Type

        TfToken

        Usd Type

        SdfValueTypeNames->Token

        Variability

        SdfVariabilityUniform

        Allowed Values

        spatial, nonSpatial
        '''
    def GetEndTimeAttr(self) -> pxr.Usd.Attribute:
        """
        Expressed in the timeCodesPerSecond of the containing stage, *endTime*
        specifies when the audio stream will cease playing during animation
        playback if the length of the referenced audio clip is longer than
        desired.


        This only applies if *playbackMode* is set to onceFromStartToEnd or
        loopFromStartToEnd, otherwise the *endTimeCode* of the stage is used
        instead of *endTime*. If *endTime* is less than *startTime*, it is
        expected that the audio will instead be played from *endTime* to
        *startTime*. Note that *endTime* is expressed as a timecode so that
        the stage can properly apply layer offsets when resolving its value.
        See Timecode Attributes and Time Scaling for more details and caveats.

        Declaration

        C{uniform timecode endTime = 0}

        C++ Type

        SdfTimeCode

        Usd Type

        SdfValueTypeNames->TimeCode

        Variability

        SdfVariabilityUniform
        """
    def GetFilePathAttr(self) -> pxr.Usd.Attribute:
        """
        Path to the audio file.


        In general, the formats allowed for audio files is no more constrained
        by USD than is image-type. As with images, however, usdz has stricter
        requirements based on DMA and format support in browsers and consumer
        devices. The allowed audio filetypes for usdz are M4A, MP3, WAV (in
        order of preference).

        Usdz Specification

        Declaration

        C{uniform asset filePath = @@}

        C++ Type

        SdfAssetPath

        Usd Type

        SdfValueTypeNames->Asset

        Variability

        SdfVariabilityUniform
        """
    def GetGainAttr(self) -> pxr.Usd.Attribute:
        '''
        Multiplier on the incoming audio signal.


        A value of 0"mutes"the signal. Negative values will be clamped to 0.

        Declaration

        C{double gain = 1}

        C++ Type

        double

        Usd Type

        SdfValueTypeNames->Double
        '''
    def GetMediaOffsetAttr(self) -> pxr.Usd.Attribute:
        """
        Expressed in seconds, *mediaOffset* specifies the offset from the
        referenced audio file's beginning at which we should begin playback
        when stage playback reaches the time that prim's audio should start.


        If the prim's *playbackMode* is a looping mode, *mediaOffset* is
        applied only to the first run-through of the audio clip; the second
        and all other loops begin from the start of the audio clip.

        Declaration

        C{uniform double mediaOffset = 0}

        C++ Type

        double

        Usd Type

        SdfValueTypeNames->Double

        Variability

        SdfVariabilityUniform
        """
    def GetPlaybackModeAttr(self) -> pxr.Usd.Attribute:
        '''
        Along with *startTime* and *endTime*, determines when the audio
        playback should start and stop during the stage\'s animation playback
        and whether the audio should loop during its duration.


        Valid values are:
           - onceFromStart: Play the audio once, starting at *startTime*,
             continuing until the audio completes.

           - onceFromStartToEnd: Play the audio once beginning at *startTime*,
             continuing until *endTime* or until the audio completes, whichever
             comes first.

           - loopFromStart: Start playing the audio at *startTime* and
             continue looping through to the stage\'s authored *endTimeCode*.

           - loopFromStartToEnd: Start playing the audio at *startTime* and
             continue looping through, stopping the audio at *endTime*.

           - loopFromStage: Start playing the audio at the stage\'s authored
             *startTimeCode* and continue looping through to the stage\'s authored
             *endTimeCode*. This can be useful for ambient sounds that should
             always be active.

        Declaration

        C{uniform token playbackMode ="onceFromStart"}

        C++ Type

        TfToken

        Usd Type

        SdfValueTypeNames->Token

        Variability

        SdfVariabilityUniform

        Allowed Values

        onceFromStart, onceFromStartToEnd, loopFromStart, loopFromStartToEnd,
        loopFromStage
        '''
    @staticmethod
    def GetSchemaAttributeNames(includeInherited: bool = ...) -> list[str]:
        """
        Return a vector of names of all pre-declared attributes for this
        schema class and all its ancestor classes.


        Does not include attributes that may be authored by custom/extended
        methods of the schemas involved.
        """
    def GetStartTimeAttr(self) -> pxr.Usd.Attribute:
        """
        Expressed in the timeCodesPerSecond of the containing stage,
        *startTime* specifies when the audio stream will start playing during
        animation playback.


        This value is ignored when *playbackMode* is set to loopFromStage as,
        in this mode, the audio will always start at the stage's authored
        *startTimeCode*. Note that *startTime* is expressed as a timecode so
        that the stage can properly apply layer offsets when resolving its
        value. See Timecode Attributes and Time Scaling for more details and
        caveats.

        Declaration

        C{uniform timecode startTime = 0}

        C++ Type

        SdfTimeCode

        Usd Type

        SdfValueTypeNames->TimeCode

        Variability

        SdfVariabilityUniform
        """
    @staticmethod
    def _GetStaticTfType() -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...

class Tokens(Boost.Python.instance):
    AssetPreviewsAPI: ClassVar[str] = ...  # read-only
    SpatialAudio: ClassVar[str] = ...  # read-only
    auralMode: ClassVar[str] = ...  # read-only
    defaultImage: ClassVar[str] = ...  # read-only
    endTime: ClassVar[str] = ...  # read-only
    filePath: ClassVar[str] = ...  # read-only
    gain: ClassVar[str] = ...  # read-only
    loopFromStage: ClassVar[str] = ...  # read-only
    loopFromStart: ClassVar[str] = ...  # read-only
    loopFromStartToEnd: ClassVar[str] = ...  # read-only
    mediaOffset: ClassVar[str] = ...  # read-only
    nonSpatial: ClassVar[str] = ...  # read-only
    onceFromStart: ClassVar[str] = ...  # read-only
    onceFromStartToEnd: ClassVar[str] = ...  # read-only
    playbackMode: ClassVar[str] = ...  # read-only
    previewThumbnails: ClassVar[str] = ...  # read-only
    previewThumbnailsDefault: ClassVar[str] = ...  # read-only
    previews: ClassVar[str] = ...  # read-only
    spatial: ClassVar[str] = ...  # read-only
    startTime: ClassVar[str] = ...  # read-only
    thumbnails: ClassVar[str] = ...  # read-only
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
