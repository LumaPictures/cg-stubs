# mypy: disable-error-code="misc, override, no-redef"

import Boost.Python
import pxr.Gf
import pxr.Tf
import typing
from _typeshed import Incomplete
from pxr.Ts.TsTest_Comparator import TsTest_Comparator as TsTest_Comparator
from pxr.Ts.TsTest_CompareBaseline import TsTest_CompareBaseline as TsTest_CompareBaseline
from pxr.Ts.TsTest_Grapher import TsTest_Grapher as TsTest_Grapher
from typing import Any, ClassVar, overload

ExtrapolationHeld: ExtrapolationType
ExtrapolationLinear: ExtrapolationType
KnotBezier: KnotType
KnotHeld: KnotType
KnotLinear: KnotType
Left: Side
Right: Side
__MFB_FULL_PACKAGE_NAME: str

class ExtrapolationType(pxr.Tf.Tf_PyEnumWrapper):
    _baseName: ClassVar[str] = ...
    allValues: ClassVar[tuple] = ...
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def GetValueFromName(name: object) -> Any: ...

class KeyFrame(Boost.Python.instance):
    '''
    Specifies the value of an TsSpline object at a particular point in
    time.


    Keyframes also specify the shape of a spline as it passes through each
    keyframe: the knot type specifies what interpolation technique to use
    (TsKnotHeld, TsKnotLinear, or TsKnotBezier), and tangent handles
    specify the shape of the spline as it passes through the keyframe.

    It is also possible for keyframes to be"dual-valued."This means that a
    separate keyframe value  the left-side value  is used when approaching
    the keyframe from lower time values. The regular value is then used
    starting at the keyframe\'s time and when approaching that time from
    higher times to the right. Dual-value knots are necessary to
    compensate for instantaneous shifts in coordinate frames, such as the
    shift that occurs when there is a constraint switch. The spline can
    snap to the new value required to maintain the same position in
    worldspace.

    B{Note:} TsKeyFrame is a value, not a formal object.
    '''
    isDualValued: Incomplete
    knotType: KnotType
    leftLen: Incomplete
    leftSlope: Incomplete
    rightLen: Incomplete
    rightSlope: Incomplete
    tangentSymmetryBroken: bool
    time: Time
    value: Any
    @overload
    def __init__(self, time: float = ..., value: Any = ..., knotType: KnotType = ..., leftSlope: Any = ..., rightSlope: Any = ..., leftLen: float = ..., rightLen: float = ...) -> None:
        """
        Constructs a single-valued keyframe.
        """
    @overload
    def __init__(self, time: float, leftValue: Any, rightValue: Any, knotType: KnotType, leftSlope: Any = ..., rightSlope: Any = ..., leftLen: float = ..., rightLen: float = ...) -> None:
        """
        Constructs a dual-valued keyframe.
        """
    @overload
    def __init__(self, _kf: KeyFrame, /) -> None:
        """
        Constructs a keyframe by duplicating an existing TsKeyFrame.
        """
    def CanSetKnotType(self, _unknownArg1: KnotType, /) -> _AnnotatedBoolResult:
        """
        Checks whether the key frame's value type supports the given knot
        type.
        """
    def GetValue(self, _side: Side, /) -> Any:
        """
        Gets the value at this keyframe on the given side.
        """
    def IsEquivalentAtSide(self, _keyFrame: KeyFrame, _side: Side, /) -> bool:
        """
        Gets whether this key frame is at the same time and is equivalent to
        C{keyFrame} on the given C{side}.


        In other words, replacing this key frame with C{keyFrame} in a spline
        will have no effect on how the spline evaluates for any time on the
        given C{side} of this key frame.
        """
    def SetValue(self, _val: Any, _side: Side, /) -> None:
        """
        Sets the value at this keyframe on the given side.
        """
    def __eq__(self, other: object) -> bool:
        """
        Compare this keyframe with another.
        """
    def __ne__(self, other: object) -> bool: ...
    @property
    def hasTangents(self): ...
    @property
    def isInterpolatable(self) -> bool:
        """
        Gets whether the value type of this keyframe is interpolatable.
        """
    @property
    def supportsTangents(self): ...

class KnotType(pxr.Tf.Tf_PyEnumWrapper):
    _baseName: ClassVar[str] = ...
    allValues: ClassVar[tuple] = ...
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def GetValueFromName(name: object) -> Any: ...

class LoopParams(Boost.Python.instance):
    __instance_size__: ClassVar[int] = ...
    looping: bool
    valueOffset: float
    @overload
    def __init__(self, _looping: bool, _start: float, _period: float, _preRepeatFrames: float, _repeatFrames: float, _valueOffset: float, /) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def GetLoopedInterval(self) -> pxr.Gf.Interval: ...
    def GetMasterInterval(self) -> pxr.Gf.Interval: ...
    def IsValid(self) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    @property
    def period(self) -> float: ...
    @property
    def preRepeatFrames(self) -> float: ...
    @property
    def repeatFrames(self) -> float: ...
    @property
    def start(self) -> float: ...

class Side(pxr.Tf.Tf_PyEnumWrapper):
    _baseName: ClassVar[str] = ...
    allValues: ClassVar[tuple] = ...
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def GetValueFromName(name: object) -> Any: ...

class Spline(Boost.Python.instance):
    """
    Represents a spline value object.



    The TsSpline class defines spline representations. Use this class to
    define and manipulate avars over time. An TsSpline object is an
    anonymous value that can be freely passed around. It has no owning
    object.

    Internally TsSpline is copy-on-write. This means that making a copy of
    an TsSpline is nearly free in both time and memory, but making an edit
    to a copy of an TsSpline may incur the cost of copying all the data.

    TsSpline provides the basic thread safety guarantee: Multiple threads
    may read and copy an TsSpline object concurrently, but it's not safe
    to read from an TsSpline which another thread is concurrently writing
    to. Internally that means that any data which may be mutated by a
    const accessor must be protected by a mutex. Currently TsSpline has an
    immutable lock-free implementation.
    """
    extrapolation: tuple[ExtrapolationType, ExtrapolationType]
    loopParams: LoopParams
    @overload
    def __init__(self) -> None:
        """
        Constructs a spline with no key frames and held extrapolation.
        """
    @overload
    def __init__(self, _other: Spline, /) -> None:
        """
        Copy construct.
        """
    @overload
    def __init__(self, arg2: object, arg3: object = ..., arg4: object = ..., arg5: LoopParams = ..., /) -> None: ...
    @overload
    def __init__(self, arg2: object, arg3: object, /) -> None: ...
    def BakeSplineLoops(self) -> None: ...
    @overload
    def Breakdown(self, arg2: object, arg3: object, arg4: bool, arg5: float, /) -> dict:
        """
        Breaks down simultaneously at several times.


        When creating knots with flat tangents, the shape of the spline may
        change between the new knot and its adjacent knots. Simply breaking
        down a spline several times in a loop may result in key frame values
        that drift away from their original values. This function samples the
        spline first, ensuring that each new key frame will preserve the value
        at that time.

        If *value* is not empty, *value* is used instead of sampling the
        spline. For each time, if there is already a key frame at that time,
        the value and type of that keyframe will not be changed.

        The arguments are the same as Breakdown() . If C{keyFramesAtTimes} is
        given, it will be populated with the newly broken down or previously
        existing key frames at the given times.
        """
    @overload
    def Breakdown(self, _times: float, _type: KnotType, _flatTangents: bool, _tangentLength: float, _values: typing.Iterable[Any] = ..., /) -> tuple[None, pxr.Gf.Interval, KeyFrameMap]:
        """
        Breaks down simultaneously at several times.


        Caller can provide a value for each time. If a value is not provided
        at a given time (it is empty), this function will sample the spline.
        If a knot already exists at a given time, its value is not modified.

        The arguments are the same as Breakdown() . If C{keyFramesAtTimes} is
        given, it will be populated with the newly broken down or previously
        existing key frames at the given times.
        """
    @overload
    def Breakdown(self, _times: typing.Iterable[float], _types: typing.Iterable[KnotType], _flatTangents: bool, _tangentLength: float, _values: typing.Iterable[Any], /) -> dict:
        """
        Breaks down simultaneously at several times with knot types specified
        for each time.


        A knot type for each time must be provided, else it is a coding error.

        Caller can provide a value for each time. If a value is not provided
        at a given time (it is empty), this function will sample the spline.
        If a knot already exists at a given time, its value is not modified.

        The arguments are the same as Breakdown() . If C{keyFramesAtTimes} is
        given, it will be populated with the newly broken down or previously
        existing key frames at the given times.
        """
    @overload
    def Breakdown(self, _x: float, _type: KnotType, _flatTangents: bool, _tangentLength: float, _value: Any, /) -> dict:
        """
        Breakdown at time *x*.


        If a key frame exists at *x* then this does nothing, otherwise it
        inserts a key frame of type *type* at *x*. If the provided *value* is
        empty (the default), the new key frame's value is chosen such that the
        value at *x* doesn't change. If *value* is not empty, the new keyframe
        is always given that value.

        If *flatTangents* is C{false} and *x* is between the first and last
        key frames then it will also try to preserve the shape of the spline
        as much as possible. Otherwise, if the key frame type and value type
        support tangents, the key frame will have tangents with zero slope and
        length *tangentLength*.

        The return value is either the newly broken down keyframe, or the
        existing keyframe at the given time. If an error has occurred, an
        empty value may be returned.
        """
    def CanSetKeyFrame(self, _kf: KeyFrame, /) -> _AnnotatedBoolResult:
        """
        Checks if the given keyframe is a valid candidate to set, optionally
        returning the reason if it cannot.
        """
    def ClearRedundantKeyFrames(self, defaultValue: Any = ..., intervals: pxr.Gf.MultiInterval = ...) -> bool:
        """
        Removes redundant keyframes from the spline in the specified multi-
        interval.



        True if the spline was changed, false if not. defaultValue

        Used only to decide whether to remove the final keyframe. The final
        keyframe is removed if defaultValue is specified and the final
        keyframe has this value. intervals

        Only keyframes in the given multiInterval will be removed, although
        all keyframes will be considered in computing what is redundant.
        """
    def ClosestKeyFrame(self, arg2: float, /) -> Any:
        """ClosestKeyFrame(time) -> TsKeyFrame

        time : Time

        Finds the keyframe closest to the given time. Returns None if there are no keyframes."""
    def ClosestKeyFrameAfter(self, arg2: float, /) -> Any:
        """ClosestKeyFrameAfter(time) -> TsKeyFrame

        time : Time

        Finds the closest keyframe after the given time. Returns None if no such keyframe exists."""
    def ClosestKeyFrameBefore(self, arg2: float, /) -> Any:
        """ClosestKeyFrameBefore(time) -> TsKeyFrame

        time : Time

        Finds the closest keyframe before the given time. Returns None if no such keyframe exists."""
    def DoSidesDiffer(self, time: float) -> bool:
        """
        Returns whether the left-side value and the right-side value at the
        specified time are different.


        This is always false for a time where there is no keyframe. For a
        keyframe time, the sides differ if (1) there is a dual-valued keyframe
        with different values on the left and right side; or (2) the keyframe
        follows a held segment whose value does not match the keyframe's
        right-side value. Contrast this method with
        TsKeyFrame::GetIsDualValued, which only reports whether a keyframe is
        configured to have dual values.
        """
    @overload
    def Eval(self, time: float, side: Side = ...) -> Any:
        """
        Evaluates the value of the spline at the given time, interpolating the
        keyframes.


        If there are no keyframes, an empty VtValue is returned.
        """
    @overload
    def Eval(self, arg2: object, /) -> tuple:
        """Eval(times) -> sequence<VtValue>

        times : tuple<Time>

        Evaluates this spline at a tuple or list of times, returning a tuple of results."""
    def EvalDerivative(self, _time: float, /, side: Side = ...) -> Any:
        """
        Evaluates the derivative of the spline at the given time,
        interpolating the keyframes.


        If there are no keyframes, an empty VtValue is returned.
        """
    def EvalHeld(self, _time: float, /, side: Side = ...) -> Any:
        '''
        Evaluates the value of the spline at the given time without any
        interpolation, as if all keyframes and extrapolation modes were of
        type"held".


        If there are no keyframes, an empty VtValue is returned.
        '''
    def GetKeyFramesInMultiInterval(self, _unknownArg1: pxr.Gf.MultiInterval, /) -> list[KeyFrame]:
        """
        Returns the keyframes contained in the given GfMultiInterval.
        """
    def HasRedundantKeyFrames(self, defaultValue: Any = ...) -> bool:
        """
        Returns true if any of this spline's key frames are redundant.
        """
    @overload
    def IsKeyFrameRedundant(self, _keyFrame: float, _defaultValue: Any = ..., /) -> bool:
        """
        Returns true if the given key frame is redundant.


        A key frame is redundant if it can be removed without affecting the
        value of the spline at any time. If a spline has only one key frame
        and that key frame has the same value as this spline's default value,
        then that key frame is considered redundant. If a C{defaultValue}
        parameter is not supplied, the last knot on a spline is never
        considered redundant.
        """
    @overload
    def IsKeyFrameRedundant(self, _keyFrameTime: KeyFrame, _defaultValue: Any = ..., /) -> bool:
        """
        Returns true if the key frame at the given time is redundant.


        This is a convenience function for the version that takes a
        TsKeyFrame. If there is no key frame at the indicated time a
        TF_CODING_ERROR will occur and false is returned.
        """
    def IsLinear(self) -> bool:
        """
        Returns whether spline represents a simple linear relationship.
        """
    @overload
    def IsSegmentFlat(self, _kf1: KeyFrame, _kf2: KeyFrame, /) -> bool:
        """
        Returns true if the segment between the given (adjacent) key frames is
        flat.
        """
    @overload
    def IsSegmentFlat(self, _startTime: float, _endTime: float, /) -> bool:
        """
        Returns true if the segment between the given (adjacent) key frames is
        flat.


        This function will log a TF_CODING_ERROR if there is no key frame at
        either of the indicated times.
        """
    @overload
    def IsSegmentValueMonotonic(self, _kf1: KeyFrame, _kf2: KeyFrame, /) -> bool:
        """
        Returns true if the segment between the given (adjacent) key frames is
        monotonic (i.e.


        no extremes).

        This function will log a TF_CODING_ERROR if kf1>= kf2 TODO describe
        the preconditions
        """
    @overload
    def IsSegmentValueMonotonic(self, _startTime: float, _endTime: float, /) -> bool:
        """
        Returns true if the segment between the given (adjacent) key frames is
        monotonic (i.e.


        no extremes).

        Given times must correspond to key frames. see also
        IsSegmentValueMonotonic(kf1, kf2)
        """
    def IsTimeLooped(self, _time: float, /) -> bool:
        '''
        Is the given time in the"unrolled"region of a spline that is looping;
        i.e.


        not in the master region
        '''
    def IsVarying(self) -> bool:
        """
        Returns true if the value of the spline changes over time, whether due
        to differing values among keyframes or knot sides, or value changes
        via non-flat tangents.


        If allowEpsilonDifferences is true, then if the spline is of type
        double, then knot value differences that are tiny will count as 0.
        """
    def IsVaryingSignificantly(self) -> bool:
        """
        Like IsVarying() , but for splines of type double, allows tiny value
        differences.
        """
    def Range(self, arg2: float, arg3: float, /) -> tuple:
        """Range(startTime, endTime) -> tuple<VtValue>

        startTime : Time
        endTime : Time

        The minimum and maximum of this spline returned as a tuple pair over the given time domain."""
    def Sample(self, _startTime: float, _endTime: float, _timeScale: float, _valueScale: float, _tolerance: float, /) -> tuple:
        '''
        Evaluates the value of the spline over the given time interval.


        When the returned samples are scaled by *timeScale* and *valueScale*
        and linearly interpolated, the reconstructed curve will nowhere have
        an error greater than *tolerance*.

        Samples may be point samples or"blur"samples. A blur sample covers a
        finite time domain and a value range. It indicates that the value
        varies very quickly in the domain and that, to the given tolerance,
        only the minimum and maximum values are of interest. Blur domains are
        always half-open on the right.

        Samples are returned in non-decreasing time order. Two samples may
        have equal time in two cases. First, if both are point samples then
        the first is the left side evaluation of the value at time and the
        second is the right side evaluation. Second, if the first sample is a
        point sample and second is a blur sample then the point sample is the
        left side evaluation of time. Blur domains will not overlap and point
        samples, with the above exception, will not be inside any blur domain.

        Samples may be returned outside the given time interval.
        '''
    def SetKeyFrame(self, _kf: KeyFrame, /) -> None:
        """
        Sets a keyframe, optionally returning the time range affected.


        If a keyframe already exists at the specified time, it will be
        replaced. If the keyframe is not a valid type to set, an error will be
        emitted; to avoid this, call CanSetKeyFrame() first.
        """
    def SetKeyFrames(self, arg2: object, /) -> None:
        """SetKeyFrames(keyFrames)

        keyFrames : sequence<TsKeyFrame>

        Replaces all of the specified keyframes. Keyframes may be specified using any type of Python sequence, such as a list or tuple."""
    def clear(self) -> None: ...
    def has_key(self, arg2: float, /) -> bool: ...
    def keys(self) -> list: ...
    def values(self) -> list: ...
    def __contains__(self, arg2: float, /) -> bool: ...
    @overload
    def __delitem__(self, arg2: float, /) -> None: ...
    @overload
    def __delitem__(self, arg2: object, /) -> None: ...
    def __eq__(self, other: object) -> bool:
        """
        Equality operator.
        """
    @overload
    def __getitem__(self, arg2: float, /) -> KeyFrame: ...
    @overload
    def __getitem__(self, arg2: object, /) -> list: ...
    def __iter__(self) -> Any: ...
    def __len__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    @property
    def empty(self): ...
    @property
    def frameRange(self) -> pxr.Gf.Interval:
        """
        Returns the minimum and maximum keyframe frames in the spline.


        If there are no keyframes, the returned range will be empty.
        """
    @property
    def frames(self): ...
    @property
    def typeName(self) -> str:
        '''
        Returns the typename of the value type for keyframes in this spline,
        If no keyframes have been set, this will return"void".
        '''

class TsTest_Evaluator(Boost.Python.instance):
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """
    def BakeInnerLoops(self, splineData: TsTest_SplineData) -> TsTest_SplineData: ...
    def Eval(self, splineData: TsTest_SplineData, sampleTimes: TsTest_SampleTimes) -> list: ...
    def Sample(self, splineData: TsTest_SplineData, tolerance: float) -> list: ...

class TsTest_Museum(Boost.Python.instance):
    class DataId(pxr.Tf.Tf_PyEnumWrapper):
        _baseName: ClassVar[str] = ...
        allValues: ClassVar[tuple] = ...
        def __init__(self, *args, **kwargs) -> None:
            """Raises an exception
            This class cannot be instantiated from Python
            """
        @staticmethod
        def GetValueFromName(name: object) -> Any: ...
    Crossover: ClassVar[DataId] = ...
    Recurve: ClassVar[DataId] = ...
    SimpleInnerLoop: ClassVar[DataId] = ...
    TwoKnotBezier: ClassVar[DataId] = ...
    TwoKnotLinear: ClassVar[DataId] = ...
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """
    def GetData(self) -> TsTest_SplineData: ...

class TsTest_Sample(Boost.Python.instance):
    __instance_size__: ClassVar[int] = ...
    time: Incomplete
    value: Incomplete
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, arg2: float, arg3: float, /) -> None: ...
    @overload
    def __init__(self, arg2: TsTest_Sample, /) -> None: ...

class TsTest_SampleTimes(Boost.Python.instance):
    class SampleTime(Boost.Python.instance):
        __instance_size__: ClassVar[int] = ...
        pre: Incomplete
        time: Incomplete
        @overload
        def __init__(self) -> None: ...
        @overload
        def __init__(self, arg2: float, /) -> None: ...
        @overload
        def __init__(self, arg2: float, arg3: bool, /) -> None: ...
        @overload
        def __init__(self, arg2: SampleTime, /) -> None: ...
        def __eq__(self, other: object) -> bool: ...
        def __lt__(self, other: object) -> bool: ...
        def __ne__(self, other: object) -> bool: ...
    @overload
    def __init__(self, times: object = ...) -> None: ...
    @overload
    def __init__(self, arg2: TsTest_SplineData, /) -> None: ...
    def AddExtrapolationTimes(self, extrapolationFactor: float) -> None: ...
    def AddKnotTimes(self) -> None: ...
    def AddStandardTimes(self) -> None: ...
    def AddTimes(self, arg2: object, /) -> None: ...
    def AddUniformInterpolationTimes(self, numSamples: int) -> None: ...
    def GetTimes(self) -> list: ...

class TsTest_SplineData(Boost.Python.instance):
    class ExtrapMethod(pxr.Tf.Tf_PyEnumWrapper):
        _baseName: ClassVar[str] = ...
        allValues: ClassVar[tuple] = ...
        def __init__(self, *args, **kwargs) -> None:
            """Raises an exception
            This class cannot be instantiated from Python
            """
        @staticmethod
        def GetValueFromName(name: object) -> Any: ...

    class Extrapolation(Boost.Python.instance):
        loopMode: Incomplete
        method: Incomplete
        slope: Incomplete
        @overload
        def __init__(self, arg2: Extrapolation, /) -> None: ...
        @overload
        def __init__(self, method: object = ..., slope: float = ..., loopMode: object = ...) -> None: ...
        def __eq__(self, other: object) -> bool: ...
        def __ne__(self, other: object) -> bool: ...

    class Feature(pxr.Tf.Tf_PyEnumWrapper):
        _baseName: ClassVar[str] = ...
        allValues: ClassVar[tuple] = ...
        def __init__(self, *args, **kwargs) -> None:
            """Raises an exception
            This class cannot be instantiated from Python
            """
        @staticmethod
        def GetValueFromName(name: object) -> Any: ...

    class InnerLoopParams(Boost.Python.instance):
        closedEnd: Incomplete
        enabled: Incomplete
        postLoopEnd: Incomplete
        preLoopStart: Incomplete
        protoEnd: Incomplete
        protoStart: Incomplete
        valueOffset: Incomplete
        @overload
        def __init__(self, arg2: InnerLoopParams, /) -> None: ...
        @overload
        def __init__(self, enabled: object = ..., protoStart: object = ..., protoEnd: object = ..., preLoopStart: object = ..., postLoopEnd: object = ..., closedEnd: object = ..., valueOffset: object = ...) -> None: ...
        def IsValid(self) -> bool: ...
        def __eq__(self, other: object) -> bool: ...
        def __ne__(self, other: object) -> bool: ...

    class InterpMethod(pxr.Tf.Tf_PyEnumWrapper):
        _baseName: ClassVar[str] = ...
        allValues: ClassVar[tuple] = ...
        def __init__(self, *args, **kwargs) -> None:
            """Raises an exception
            This class cannot be instantiated from Python
            """
        @staticmethod
        def GetValueFromName(name: object) -> Any: ...

    class Knot(Boost.Python.instance):
        isDualValued: Incomplete
        nextSegInterpMethod: Incomplete
        postAuto: Incomplete
        postLen: Incomplete
        postSlope: Incomplete
        preAuto: Incomplete
        preLen: Incomplete
        preSlope: Incomplete
        preValue: Incomplete
        time: Incomplete
        value: Incomplete
        @overload
        def __init__(self, arg2: Knot, /) -> None: ...
        @overload
        def __init__(self, time: object = ..., nextSegInterpMethod: object = ..., value: object = ..., preValue: object = ..., preSlope: object = ..., postSlope: object = ..., preLen: object = ..., postLen: object = ..., preAuto: object = ..., postAuto: object = ...) -> None: ...
        def __eq__(self, other: object) -> bool: ...
        def __lt__(self, other: object) -> bool: ...
        def __ne__(self, other: object) -> bool: ...

    class LoopMode(pxr.Tf.Tf_PyEnumWrapper):
        _baseName: ClassVar[str] = ...
        allValues: ClassVar[tuple] = ...
        def __init__(self, *args, **kwargs) -> None:
            """Raises an exception
            This class cannot be instantiated from Python
            """
        @staticmethod
        def GetValueFromName(name: object) -> Any: ...
    ExtrapHeld: ClassVar[ExtrapMethod] = ...
    ExtrapLinear: ClassVar[ExtrapMethod] = ...
    ExtrapLoop: ClassVar[ExtrapMethod] = ...
    ExtrapSloped: ClassVar[ExtrapMethod] = ...
    FeatureBezierSegments: ClassVar[Feature] = ...
    FeatureDualValuedKnots: ClassVar[Feature] = ...
    FeatureExtrapolatingLoops: ClassVar[Feature] = ...
    FeatureHeldSegments: ClassVar[Feature] = ...
    FeatureHermiteSegments: ClassVar[Feature] = ...
    FeatureInnerLoops: ClassVar[Feature] = ...
    FeatureLinearSegments: ClassVar[Feature] = ...
    InterpCurve: ClassVar[InterpMethod] = ...
    InterpHeld: ClassVar[InterpMethod] = ...
    InterpLinear: ClassVar[InterpMethod] = ...
    LoopContinue: ClassVar[LoopMode] = ...
    LoopNone: ClassVar[LoopMode] = ...
    LoopOscillate: ClassVar[LoopMode] = ...
    LoopRepeat: ClassVar[LoopMode] = ...
    LoopReset: ClassVar[LoopMode] = ...
    def __init__(self, isHermite: bool = ..., knots: object = ..., preExtrapolation: object = ..., postExtrapolation: object = ..., innerLoopParams: object = ...) -> None: ...
    def AddKnot(self, knot: Knot) -> None: ...
    def GetDebugDescription(self) -> str: ...
    def GetInnerLoopParams(self) -> InnerLoopParams: ...
    def GetIsHermite(self) -> bool: ...
    def GetKnots(self) -> list: ...
    def GetPostExtrapolation(self) -> Extrapolation: ...
    def GetPreExtrapolation(self) -> Extrapolation: ...
    def GetRequiredFeatures(self) -> int: ...
    def SetInnerLoopParams(self, params: InnerLoopParams) -> None: ...
    def SetIsHermite(self, isHermite: bool) -> None: ...
    def SetKnots(self, knots: object) -> None: ...
    def SetPostExtrapolation(self, postExtrap: Extrapolation) -> None: ...
    def SetPreExtrapolation(self, preExtrap: Extrapolation) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...

class TsTest_TsEvaluator(TsTest_Evaluator):
    __instance_size__: ClassVar[int] = ...
    def __init__(self) -> None: ...

class ValueSample(Boost.Python.instance):
    """
    An individual sample.


    A sample is either a blur, defining a rectangle, or linear, defining a
    line for linear interpolation. In both cases the sample is half-open
    on the right.
    """
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """
    @property
    def isBlur(self): ...
    @property
    def leftTime(self): ...
    @property
    def leftValue(self): ...
    @property
    def rightTime(self): ...
    @property
    def rightValue(self): ...

class _AnnotatedBoolResult(Boost.Python.instance):
    __instance_size__: ClassVar[int] = ...
    def __init__(self, arg2: bool, arg3: object, /) -> None: ...
    def __bool__(self) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    def __getitem__(self, arg2: int, /) -> Any: ...
    def __ne__(self, other: object) -> bool: ...
    @property
    def reasonWhyNot(self): ...

def SimplifySpline(_intervals: Spline, _maxErrorFraction: pxr.Gf.MultiInterval, _extremeMaxErrFract: float, /) -> None:
    """
    Remove as many knots as possible from spline without introducing error
    greater than maxErrorFraction, where maxErrorFraction is a percentage
    of the spline's total range (if the spline's value varies over a range
    of x, the largest error allowed will be x*maxErrorFraction).


    Only remove knots in intervals.
    """
def SimplifySplinesInParallel(_intervals: typing.Iterable[pxr.Gf.MultiInterval], _maxErrorFraction: float, _extremeMaxErrFract: float, /) -> None:
    """
    Run TsSimplifySpline() on a vector of splines in parallel.


    The splines in'splines'are mutated in place. The first two args must
    have the same length, unless the intervals arg is empty, in which case
    the full frame range of each spline is used. The remaining args are as
    in TsSimplifySpline.
    """
def TsTest_SampleBezier(splineData: TsTest_SplineData, numSamples: int) -> list: ...
