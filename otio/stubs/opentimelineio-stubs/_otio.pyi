import opentimelineio._opentime
import typing
from typing import Callable, ClassVar, overload

class AnyDictionary:
    clear: ClassVar[Callable] = ...
    get: ClassVar[Callable] = ...
    items: ClassVar[Callable] = ...
    keys: ClassVar[Callable] = ...
    pop: ClassVar[Callable] = ...
    popitem: ClassVar[Callable] = ...
    setdefault: ClassVar[Callable] = ...
    update: ClassVar[Callable] = ...
    values: ClassVar[Callable] = ...
    __contains__: ClassVar[Callable] = ...
    __copy__: ClassVar[Callable] = ...
    __deepcopy__: ClassVar[Callable] = ...
    __eq__: ClassVar[Callable] = ...
    __setitem__: ClassVar[Callable] = ...
    def __init__(self) -> None:
        """__init__(self: opentimelineio._otio.AnyDictionary) -> None"""
    def __delitem__(self, key: str) -> None:
        """__delitem__(self: opentimelineio._otio.AnyDictionary, key: str) -> None"""
    def __getitem__(self, key: str) -> object:
        """__getitem__(self: opentimelineio._otio.AnyDictionary, key: str) -> object"""
    def __internal_setitem__(self, key: str, item: PyAny) -> None:
        """__internal_setitem__(self: opentimelineio._otio.AnyDictionary, key: str, item: PyAny) -> None"""
    def __iter__(self) -> AnyDictionaryIterator:
        """__iter__(self: opentimelineio._otio.AnyDictionary) -> opentimelineio._otio.AnyDictionaryIterator"""
    def __len__(self) -> int:
        """__len__(self: opentimelineio._otio.AnyDictionary) -> int"""

class AnyDictionaryIterator:
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def __iter__(self) -> AnyDictionaryIterator:
        """__iter__(self: opentimelineio._otio.AnyDictionaryIterator) -> opentimelineio._otio.AnyDictionaryIterator"""
    def __next__(self) -> object:
        """__next__(self: opentimelineio._otio.AnyDictionaryIterator) -> object"""

class AnyVector:
    append: ClassVar[Callable] = ...
    clear: ClassVar[Callable] = ...
    count: ClassVar[Callable] = ...
    extend: ClassVar[Callable] = ...
    index: ClassVar[Callable] = ...
    insert: ClassVar[Callable] = ...
    pop: ClassVar[Callable] = ...
    remove: ClassVar[Callable] = ...
    reverse: ClassVar[Callable] = ...
    __add__: ClassVar[Callable] = ...
    __contains__: ClassVar[Callable] = ...
    __copy__: ClassVar[Callable] = ...
    __deepcopy__: ClassVar[Callable] = ...
    __delitem__: ClassVar[Callable] = ...
    __getitem__: ClassVar[Callable] = ...
    __iadd__: ClassVar[Callable] = ...
    __radd__: ClassVar[Callable] = ...
    __reversed__: ClassVar[Callable] = ...
    __setitem__: ClassVar[Callable] = ...
    def __init__(self) -> None:
        """__init__(self: opentimelineio._otio.AnyVector) -> None"""
    def __internal_insert(self, arg0: int, arg1: PyAny) -> None:
        """__internal_insert(self: opentimelineio._otio.AnyVector, arg0: int, arg1: PyAny) -> None"""
    def __internal_delitem__(self, index: int) -> None:
        """__internal_delitem__(self: opentimelineio._otio.AnyVector, index: int) -> None"""
    def __internal_getitem__(self, index: int) -> object:
        """__internal_getitem__(self: opentimelineio._otio.AnyVector, index: int) -> object"""
    def __internal_setitem__(self, index: int, item: PyAny) -> None:
        """__internal_setitem__(self: opentimelineio._otio.AnyVector, index: int, item: PyAny) -> None"""
    def __iter__(self) -> AnyVectorIterator:
        """__iter__(self: opentimelineio._otio.AnyVector) -> opentimelineio._otio.AnyVectorIterator"""
    def __len__(self) -> int:
        """__len__(self: opentimelineio._otio.AnyVector) -> int"""

class AnyVectorIterator:
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def __iter__(self) -> AnyVectorIterator:
        """__iter__(self: opentimelineio._otio.AnyVectorIterator) -> opentimelineio._otio.AnyVectorIterator"""
    def __next__(self) -> object:
        """__next__(self: opentimelineio._otio.AnyVectorIterator) -> object"""

class Box2d:
    max: V2d
    min: V2d
    @overload
    def __init__(self) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: opentimelineio._otio.Box2d) -> None

        2. __init__(self: opentimelineio._otio.Box2d, arg0: opentimelineio._otio.V2d) -> None

        3. __init__(self: opentimelineio._otio.Box2d, arg0: opentimelineio._otio.V2d, arg1: opentimelineio._otio.V2d) -> None
        """
    @overload
    def __init__(self, arg0: V2d) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: opentimelineio._otio.Box2d) -> None

        2. __init__(self: opentimelineio._otio.Box2d, arg0: opentimelineio._otio.V2d) -> None

        3. __init__(self: opentimelineio._otio.Box2d, arg0: opentimelineio._otio.V2d, arg1: opentimelineio._otio.V2d) -> None
        """
    @overload
    def __init__(self, arg0: V2d, arg1: V2d) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: opentimelineio._otio.Box2d) -> None

        2. __init__(self: opentimelineio._otio.Box2d, arg0: opentimelineio._otio.V2d) -> None

        3. __init__(self: opentimelineio._otio.Box2d, arg0: opentimelineio._otio.V2d, arg1: opentimelineio._otio.V2d) -> None
        """
    def center(self) -> V2d:
        """center(self: opentimelineio._otio.Box2d) -> opentimelineio._otio.V2d"""
    @overload
    def extendBy(self, arg0: V2d) -> None:
        """extendBy(*args, **kwargs)
        Overloaded function.

        1. extendBy(self: opentimelineio._otio.Box2d, arg0: opentimelineio._otio.V2d) -> None

        2. extendBy(self: opentimelineio._otio.Box2d, arg0: opentimelineio._otio.Box2d) -> None
        """
    @overload
    def extendBy(self, arg0: Box2d) -> None:
        """extendBy(*args, **kwargs)
        Overloaded function.

        1. extendBy(self: opentimelineio._otio.Box2d, arg0: opentimelineio._otio.V2d) -> None

        2. extendBy(self: opentimelineio._otio.Box2d, arg0: opentimelineio._otio.Box2d) -> None
        """
    @overload
    def intersects(self, arg0: V2d) -> bool:
        """intersects(*args, **kwargs)
        Overloaded function.

        1. intersects(self: opentimelineio._otio.Box2d, arg0: opentimelineio._otio.V2d) -> bool

        2. intersects(self: opentimelineio._otio.Box2d, arg0: opentimelineio._otio.Box2d) -> bool
        """
    @overload
    def intersects(self, arg0: Box2d) -> bool:
        """intersects(*args, **kwargs)
        Overloaded function.

        1. intersects(self: opentimelineio._otio.Box2d, arg0: opentimelineio._otio.V2d) -> bool

        2. intersects(self: opentimelineio._otio.Box2d, arg0: opentimelineio._otio.Box2d) -> bool
        """
    def __eq__(self, arg0: object) -> bool:
        """__eq__(self: opentimelineio._otio.Box2d, arg0: object) -> bool"""
    def __ne__(self, arg0: object) -> bool:
        """__ne__(self: opentimelineio._otio.Box2d, arg0: object) -> bool"""

class CannotComputeAvailableRangeError(OTIOError): ...

class Clip(Item):
    """
    A :class:`~Clip` is a segment of editable media (usually audio or video).

    Contains a :class:`.MediaReference` and a trim on that media reference.
    """
    DEFAULT_MEDIA_KEY: ClassVar[str] = ...  # read-only
    find_clips: ClassVar[Callable] = ...
    active_media_reference_key: str
    media_reference: MediaReference
    def __init__(self, name: str = ..., media_reference: MediaReference = ..., source_range: opentimelineio._opentime.TimeRange | None = ..., metadata: object = ..., active_media_reference: str = ...) -> None:
        """__init__(self: opentimelineio._otio.Clip, name: str = '', media_reference: opentimelineio._otio.MediaReference = None, source_range: Optional[opentimelineio._opentime.TimeRange] = None, metadata: object = None, active_media_reference: str = 'DEFAULT_MEDIA') -> None"""
    def media_references(self) -> dict[str, MediaReference]:
        """media_references(self: opentimelineio._otio.Clip) -> Dict[str, opentimelineio._otio.MediaReference]"""
    def set_media_references(self, arg0: dict[str, MediaReference], arg1: str) -> None:
        """set_media_references(self: opentimelineio._otio.Clip, arg0: Dict[str, opentimelineio._otio.MediaReference], arg1: str) -> None"""

class Composable(SerializableObjectWithMetadata):
    """
    An object that can be composed within a :class:`~Composition` (such as :class:`~Track` or :class:`.Stack`).
    """
    def __init__(self, name: str = ..., metadata: object = ...) -> None:
        """__init__(self: opentimelineio._otio.Composable, name: str = '', metadata: object = None) -> None"""
    def overlapping(self) -> bool:
        """overlapping(self: opentimelineio._otio.Composable) -> bool"""
    def parent(self) -> Composition:
        """parent(self: opentimelineio._otio.Composable) -> opentimelineio._otio.Composition"""
    def visible(self) -> bool:
        """visible(self: opentimelineio._otio.Composable) -> bool"""

class Composition(Item):
    """
    Base class for an :class:`~Item` that contains :class:`~Composable`\\s.

    Should be subclassed (for example by :class:`.Track` and :class:`.Stack`), not used directly.
    """
    append: ClassVar[Callable] = ...
    clear: ClassVar[Callable] = ...
    count: ClassVar[Callable] = ...
    extend: ClassVar[Callable] = ...
    index: ClassVar[Callable] = ...
    insert: ClassVar[Callable] = ...
    pop: ClassVar[Callable] = ...
    remove: ClassVar[Callable] = ...
    reverse: ClassVar[Callable] = ...
    __add__: ClassVar[Callable] = ...
    __delitem__: ClassVar[Callable] = ...
    __getitem__: ClassVar[Callable] = ...
    __iadd__: ClassVar[Callable] = ...
    __radd__: ClassVar[Callable] = ...
    __reversed__: ClassVar[Callable] = ...
    __setitem__: ClassVar[Callable] = ...
    def __init__(self, name: str = ..., children: list[Composable] | None = ..., source_range: opentimelineio._opentime.TimeRange | None = ..., metadata: object = ...) -> None:
        """__init__(self: opentimelineio._otio.Composition, name: str = '', children: Optional[List[opentimelineio._otio.Composable]] = None, source_range: Optional[opentimelineio._opentime.TimeRange] = None, metadata: object = None) -> None"""
    def __internal_insert(self, index: int, item: Composable) -> None:
        """__internal_insert(self: opentimelineio._otio.Composition, index: int, item: opentimelineio._otio.Composable) -> None"""
    def child_at_time(self, search_time: opentimelineio._opentime.RationalTime, shallow_search: bool = ...) -> Composable:
        """child_at_time(self: opentimelineio._otio.Composition, search_time: opentimelineio._opentime.RationalTime, shallow_search: bool = False) -> opentimelineio._otio.Composable"""
    def children_in_range(self, search_range: opentimelineio._opentime.TimeRange) -> list[SerializableObject]:
        """children_in_range(self: opentimelineio._otio.Composition, search_range: opentimelineio._opentime.TimeRange) -> List[opentimelineio._otio.SerializableObject]"""
    def find_children(self, descended_from_type: object = ..., search_range: opentimelineio._opentime.TimeRange | None = ..., shallow_search: bool = ...) -> list[SerializableObject]:
        """find_children(self: opentimelineio._otio.Composition, descended_from_type: object = None, search_range: Optional[opentimelineio._opentime.TimeRange] = None, shallow_search: bool = False) -> List[opentimelineio._otio.SerializableObject]"""
    def handles_of_child(self, child: Composable) -> tuple:
        """handles_of_child(self: opentimelineio._otio.Composition, child: opentimelineio._otio.Composable) -> tuple"""
    def has_clips(self) -> bool:
        """has_clips(self: opentimelineio._otio.Composition) -> bool"""
    def is_parent_of(self, other: Composable) -> bool:
        """is_parent_of(self: opentimelineio._otio.Composition, other: opentimelineio._otio.Composable) -> bool"""
    def range_of_all_children(self) -> dict:
        """range_of_all_children(self: opentimelineio._otio.Composition) -> dict"""
    def range_of_child(self, child: Composable, reference_space: Composable = ...) -> opentimelineio._opentime.TimeRange:
        """range_of_child(self: opentimelineio._otio.Composition, child: opentimelineio._otio.Composable, reference_space: opentimelineio._otio.Composable = None) -> opentimelineio._opentime.TimeRange"""
    def range_of_child_at_index(self, index: int) -> opentimelineio._opentime.TimeRange:
        """range_of_child_at_index(self: opentimelineio._otio.Composition, index: int) -> opentimelineio._opentime.TimeRange"""
    def trim_child_range(self, child_range: opentimelineio._opentime.TimeRange) -> opentimelineio._opentime.TimeRange | None:
        """trim_child_range(self: opentimelineio._otio.Composition, child_range: opentimelineio._opentime.TimeRange) -> Optional[opentimelineio._opentime.TimeRange]"""
    def trimmed_child_range(self, child_range: opentimelineio._opentime.TimeRange) -> opentimelineio._opentime.TimeRange | None:
        """trimmed_child_range(self: opentimelineio._otio.Composition, child_range: opentimelineio._opentime.TimeRange) -> Optional[opentimelineio._opentime.TimeRange]"""
    def trimmed_range_of_child(self, child: Composable, reference_space: Composable = ...) -> opentimelineio._opentime.TimeRange | None:
        """trimmed_range_of_child(self: opentimelineio._otio.Composition, child: opentimelineio._otio.Composable, reference_space: opentimelineio._otio.Composable = None) -> Optional[opentimelineio._opentime.TimeRange]"""
    def trimmed_range_of_child_at_index(self, index: int) -> opentimelineio._opentime.TimeRange:
        """trimmed_range_of_child_at_index(self: opentimelineio._otio.Composition, index: int) -> opentimelineio._opentime.TimeRange"""
    def __contains__(self, composable: Composable) -> bool:
        """__contains__(self: opentimelineio._otio.Composition, composable: opentimelineio._otio.Composable) -> bool"""
    def __internal_delitem__(self, index: int) -> None:
        """__internal_delitem__(self: opentimelineio._otio.Composition, index: int) -> None"""
    def __internal_getitem__(self, index: int) -> Composable:
        """__internal_getitem__(self: opentimelineio._otio.Composition, index: int) -> opentimelineio._otio.Composable"""
    def __internal_setitem__(self, index: int, item: Composable) -> None:
        """__internal_setitem__(self: opentimelineio._otio.Composition, index: int, item: opentimelineio._otio.Composable) -> None"""
    def __iter__(self) -> CompositionIterator:
        """__iter__(self: opentimelineio._otio.Composition) -> opentimelineio._otio.CompositionIterator"""
    def __len__(self) -> int:
        """__len__(self: opentimelineio._otio.Composition) -> int"""
    @property
    def composition_kind(self) -> str:
        """(arg0: opentimelineio._otio.Composition) -> str"""

class CompositionIterator:
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def __iter__(self) -> CompositionIterator:
        """__iter__(self: opentimelineio._otio.CompositionIterator) -> opentimelineio._otio.CompositionIterator"""
    def __next__(self) -> Composable:
        """__next__(self: opentimelineio._otio.CompositionIterator) -> opentimelineio._otio.Composable"""

class Effect(SerializableObjectWithMetadata):
    effect_name: str
    def __init__(self, name: str = ..., effect_name: str = ..., metadata: object = ...) -> None:
        """__init__(self: opentimelineio._otio.Effect, name: str = '', effect_name: str = '', metadata: object = None) -> None"""

class EffectVector:
    append: ClassVar[Callable] = ...
    clear: ClassVar[Callable] = ...
    count: ClassVar[Callable] = ...
    extend: ClassVar[Callable] = ...
    index: ClassVar[Callable] = ...
    insert: ClassVar[Callable] = ...
    pop: ClassVar[Callable] = ...
    remove: ClassVar[Callable] = ...
    reverse: ClassVar[Callable] = ...
    __add__: ClassVar[Callable] = ...
    __contains__: ClassVar[Callable] = ...
    __copy__: ClassVar[Callable] = ...
    __deepcopy__: ClassVar[Callable] = ...
    __delitem__: ClassVar[Callable] = ...
    __getitem__: ClassVar[Callable] = ...
    __iadd__: ClassVar[Callable] = ...
    __radd__: ClassVar[Callable] = ...
    __reversed__: ClassVar[Callable] = ...
    __setitem__: ClassVar[Callable] = ...
    def __init__(self) -> None:
        """__init__(self: opentimelineio._otio.EffectVector) -> None"""
    def __internal_insert(self, index: int, item) -> None:
        """__internal_insert(self: opentimelineio._otio.EffectVector, index: int, item: opentimelineio::v1_0::Effect) -> None"""
    def __internal_delitem__(self, index: int) -> None:
        """__internal_delitem__(self: opentimelineio._otio.EffectVector, index: int) -> None"""
    def __internal_getitem__(self, *args, **kwargs):
        """__internal_getitem__(self: opentimelineio._otio.EffectVector, index: int) -> opentimelineio::v1_0::Effect"""
    def __internal_setitem__(self, index: int, item) -> None:
        """__internal_setitem__(self: opentimelineio._otio.EffectVector, index: int, item: opentimelineio::v1_0::Effect) -> None"""
    def __iter__(self) -> EffectVectorIterator:
        """__iter__(self: opentimelineio._otio.EffectVector) -> opentimelineio._otio.EffectVectorIterator"""
    def __len__(self) -> int:
        """__len__(self: opentimelineio._otio.EffectVector) -> int"""

class EffectVectorIterator:
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def __iter__(self) -> EffectVectorIterator:
        """__iter__(self: opentimelineio._otio.EffectVectorIterator) -> opentimelineio._otio.EffectVectorIterator"""
    def __next__(self):
        """__next__(self: opentimelineio._otio.EffectVectorIterator) -> opentimelineio::v1_0::Effect"""

class ExternalReference(MediaReference):
    target_url: str
    def __init__(self, target_url: str = ..., available_range: opentimelineio._opentime.TimeRange | None = ..., metadata: object = ..., available_image_bounds: Box2d | None = ...) -> None:
        """__init__(self: opentimelineio._otio.ExternalReference, target_url: str = '', available_range: Optional[opentimelineio._opentime.TimeRange] = None, metadata: object = None, available_image_bounds: Optional[opentimelineio._otio.Box2d] = None) -> None"""

class FreezeFrame(LinearTimeWarp):
    """Hold the first frame of the clip for the duration of the clip."""
    def __init__(self, name: str = ..., metadata: object = ...) -> None:
        """__init__(self: opentimelineio._otio.FreezeFrame, name: str = '', metadata: object = None) -> None"""

class Gap(Item):
    @overload
    def __init__(self, name: str = ..., source_range: opentimelineio._opentime.TimeRange = ..., effects: list[Effect] | None = ..., markers: list[Marker] | None = ..., metadata: object = ...) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: opentimelineio._otio.Gap, name: str = '', source_range: opentimelineio._opentime.TimeRange = otio.opentime.TimeRange(start_time=otio.opentime.RationalTime(value=0, rate=1), duration=otio.opentime.RationalTime(value=0, rate=1)), effects: Optional[List[opentimelineio._otio.Effect]] = None, markers: Optional[List[opentimelineio._otio.Marker]] = None, metadata: object = None) -> None

        2. __init__(self: opentimelineio._otio.Gap, name: str = '', duration: opentimelineio._opentime.RationalTime = otio.opentime.RationalTime(value=0, rate=1), effects: Optional[List[opentimelineio._otio.Effect]] = None, markers: Optional[List[opentimelineio._otio.Marker]] = None, metadata: object = None) -> None
        """
    @overload
    def __init__(self, name: str = ..., duration: opentimelineio._opentime.RationalTime = ..., effects: list[Effect] | None = ..., markers: list[Marker] | None = ..., metadata: object = ...) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: opentimelineio._otio.Gap, name: str = '', source_range: opentimelineio._opentime.TimeRange = otio.opentime.TimeRange(start_time=otio.opentime.RationalTime(value=0, rate=1), duration=otio.opentime.RationalTime(value=0, rate=1)), effects: Optional[List[opentimelineio._otio.Effect]] = None, markers: Optional[List[opentimelineio._otio.Marker]] = None, metadata: object = None) -> None

        2. __init__(self: opentimelineio._otio.Gap, name: str = '', duration: opentimelineio._opentime.RationalTime = otio.opentime.RationalTime(value=0, rate=1), effects: Optional[List[opentimelineio._otio.Effect]] = None, markers: Optional[List[opentimelineio._otio.Marker]] = None, metadata: object = None) -> None
        """

class GeneratorReference(MediaReference):
    generator_kind: str
    def __init__(self, name: str = ..., generator_kind: str = ..., available_range: opentimelineio._opentime.TimeRange | None = ..., parameters: object = ..., metadata: object = ..., available_image_bounds: Box2d | None = ...) -> None:
        """__init__(self: opentimelineio._otio.GeneratorReference, name: str = '', generator_kind: str = '', available_range: Optional[opentimelineio._opentime.TimeRange] = None, parameters: object = None, metadata: object = None, available_image_bounds: Optional[opentimelineio._otio.Box2d] = None) -> None"""
    @property
    def parameters(self) -> AnyDictionary:
        """(arg0: opentimelineio._otio.GeneratorReference) -> opentimelineio._otio.AnyDictionary"""

class ImageSequenceReference(MediaReference):
    '''
    An ImageSequenceReference refers to a numbered series of single-frame image files. Each file can be referred to by a URL generated by the :class:`~ImageSequenceReference`.

    Image sequences can have URLs with discontinuous frame numbers, for instance if you\'ve only rendered every other frame in a sequence, your frame numbers may be 1, 3, 5, etc. This is configured using the ``frame_step`` attribute. In this case, the 0th image in the sequence is frame 1 and the 1st image in the sequence is frame 3. Because of this there are two numbering concepts in the image sequence, the image number and the frame number.

    Frame numbers are the integer numbers used in the frame file name. Image numbers are the 0-index based numbers of the frames available in the reference. Frame numbers can be discontinuous, image numbers will always be zero to the total count of frames minus 1.

    An example for 24fps media with a sample provided each frame numbered 1-1000 with a path ``/show/sequence/shot/sample_image_sequence.%04d.exr`` might be

    .. code-block:: json

        {
          "available_range": {
            "start_time": {
              "value": 0,
              "rate": 24
            },
            "duration": {
              "value": 1000,
              "rate": 24
            }
          },
          "start_frame": 1,
          "frame_step": 1,
          "rate": 24,
          "target_url_base": "file:///show/sequence/shot/",
          "name_prefix": "sample_image_sequence.",
          "name_suffix": ".exr"
          "frame_zero_padding": 4,
        }

    The same duration sequence but with only every 2nd frame available in the sequence would be

    .. code-block:: json

        {
          "available_range": {
            "start_time": {
              "value": 0,
              "rate": 24
            },
            "duration": {
              "value": 1000,
              "rate": 24
            }
          },
          "start_frame": 1,
          "frame_step": 2,
          "rate": 24,
          "target_url_base": "file:///show/sequence/shot/",
          "name_prefix": "sample_image_sequence.",
          "name_suffix": ".exr"
          "frame_zero_padding": 4,
        }

    A list of all the frame URLs in the sequence can be generated, regardless of frame step, with the following list comprehension

    .. code-block:: python

        [ref.target_url_for_image_number(i) for i in range(ref.number_of_images_in_sequence())]

    Negative ``start_frame`` is also handled. The above example with a ``start_frame`` of ``-1`` would yield the first three target urls as:

    - ``file:///show/sequence/shot/sample_image_sequence.-0001.exr``
    - ``file:///show/sequence/shot/sample_image_sequence.0000.exr``
    - ``file:///show/sequence/shot/sample_image_sequence.0001.exr``
    '''

    class MissingFramePolicy:
        """Behavior that should be used by applications when an image file in the sequence can't be found on disk.

        Members:

          error : Application should stop and raise an error.

          hold : Application should hold the last available frame before the missing frame.

          black : Application should use a black frame in place of the missing frame"""
        __members__: ClassVar[dict] = ...  # read-only
        __entries: ClassVar[dict] = ...
        black: ClassVar[ImageSequenceReference.MissingFramePolicy] = ...
        error: ClassVar[ImageSequenceReference.MissingFramePolicy] = ...
        hold: ClassVar[ImageSequenceReference.MissingFramePolicy] = ...
        def __init__(self, value: int) -> None:
            """__init__(self: opentimelineio._otio.ImageSequenceReference.MissingFramePolicy, value: int) -> None"""
        def __eq__(self, other: object) -> bool:
            """__eq__(self: object, other: object) -> bool"""
        def __hash__(self) -> int:
            """__hash__(self: object) -> int"""
        def __index__(self) -> int:
            """__index__(self: opentimelineio._otio.ImageSequenceReference.MissingFramePolicy) -> int"""
        def __int__(self) -> int:
            """__int__(self: opentimelineio._otio.ImageSequenceReference.MissingFramePolicy) -> int"""
        def __ne__(self, other: object) -> bool:
            """__ne__(self: object, other: object) -> bool"""
        @property
        def name(self) -> str:
            """name(self: handle) -> str

            name(self: handle) -> str
            """
        @property
        def value(self) -> int:
            """(arg0: opentimelineio._otio.ImageSequenceReference.MissingFramePolicy) -> int"""
    abstract_target_url: ClassVar[Callable] = ...
    frame_range_for_time_range: ClassVar[Callable] = ...
    frame_step: int
    frame_zero_padding: int
    missing_frame_policy: ImageSequenceReference.MissingFramePolicy
    name_prefix: str
    name_suffix: str
    rate: float
    start_frame: int
    target_url_base: str
    def __init__(self, target_url_base: str = ..., name_prefix: str = ..., name_suffix: str = ..., start_frame: int = ..., frame_step: int = ..., rate: float = ..., frame_zero_padding: int = ..., missing_frame_policy: ImageSequenceReference.MissingFramePolicy = ..., available_range: opentimelineio._opentime.TimeRange | None = ..., metadata: object = ..., available_image_bounds: Box2d | None = ...) -> None:
        """__init__(self: opentimelineio._otio.ImageSequenceReference, target_url_base: str = '', name_prefix: str = '', name_suffix: str = '', start_frame: int = 1, frame_step: int = 1, rate: float = 1, frame_zero_padding: int = 0, missing_frame_policy: opentimelineio._otio.ImageSequenceReference.MissingFramePolicy = <MissingFramePolicy.error: 0>, available_range: Optional[opentimelineio._opentime.TimeRange] = None, metadata: object = None, available_image_bounds: Optional[opentimelineio._otio.Box2d] = None) -> None"""
    def end_frame(self) -> int:
        """end_frame(self: opentimelineio._otio.ImageSequenceReference) -> int

        Last frame number in the sequence based on the :attr:`rate` and :attr:`.available_range`.
        """
    def frame_for_time(self, time: opentimelineio._opentime.RationalTime) -> int:
        """frame_for_time(self: opentimelineio._otio.ImageSequenceReference, time: opentimelineio._opentime.RationalTime) -> int

        Given a :class:`.RationalTime` within the available range, returns the frame number.
        """
    def number_of_images_in_sequence(self) -> int:
        """number_of_images_in_sequence(self: opentimelineio._otio.ImageSequenceReference) -> int

        Returns the number of images based on the :attr:`rate` and :attr:`.available_range`.
        """
    def presentation_time_for_image_number(self, image_number: int) -> opentimelineio._opentime.RationalTime:
        """presentation_time_for_image_number(self: opentimelineio._otio.ImageSequenceReference, image_number: int) -> opentimelineio._opentime.RationalTime

        Given an image number, returns the :class:`.RationalTime` at which that image should be shown in the space of :attr:`.available_range`.
        """
    def target_url_for_image_number(self, image_number: int) -> str:
        '''target_url_for_image_number(self: opentimelineio._otio.ImageSequenceReference, image_number: int) -> str

        Given an image number, returns the ``target_url`` for that image.

        This is roughly equivalent to:

        .. code-block:: python

           f"{target_url_prefix}{(start_frame + (image_number * frame_step)):0{value_zero_padding}}{target_url_postfix}"


        '''

class Item(Composable):
    enabled: bool
    source_range: opentimelineio._opentime.TimeRange | None
    def __init__(self, name: str = ..., source_range: opentimelineio._opentime.TimeRange | None = ..., effects: list[Effect] | None = ..., markers: list[Marker] | None = ..., enabled: bool = ..., metadata: object = ...) -> None:
        """__init__(self: opentimelineio._otio.Item, name: str = '', source_range: Optional[opentimelineio._opentime.TimeRange] = None, effects: Optional[List[opentimelineio._otio.Effect]] = None, markers: Optional[List[opentimelineio._otio.Marker]] = None, enabled: bool = True, metadata: object = None) -> None"""
    def available_range(self) -> opentimelineio._opentime.TimeRange:
        """available_range(self: opentimelineio._otio.Item) -> opentimelineio._opentime.TimeRange"""
    def duration(self) -> opentimelineio._opentime.RationalTime:
        """duration(self: opentimelineio._otio.Item) -> opentimelineio._opentime.RationalTime"""
    def range_in_parent(self) -> opentimelineio._opentime.TimeRange:
        """range_in_parent(self: opentimelineio._otio.Item) -> opentimelineio._opentime.TimeRange"""
    def transformed_time(self, time: opentimelineio._opentime.RationalTime, to_item: Item) -> opentimelineio._opentime.RationalTime:
        """transformed_time(self: opentimelineio._otio.Item, time: opentimelineio._opentime.RationalTime, to_item: opentimelineio._otio.Item) -> opentimelineio._opentime.RationalTime"""
    def transformed_time_range(self, time_range: opentimelineio._opentime.TimeRange, to_item: Item) -> opentimelineio._opentime.TimeRange:
        """transformed_time_range(self: opentimelineio._otio.Item, time_range: opentimelineio._opentime.TimeRange, to_item: opentimelineio._otio.Item) -> opentimelineio._opentime.TimeRange"""
    def trimmed_range(self) -> opentimelineio._opentime.TimeRange:
        """trimmed_range(self: opentimelineio._otio.Item) -> opentimelineio._opentime.TimeRange"""
    def trimmed_range_in_parent(self) -> opentimelineio._opentime.TimeRange | None:
        """trimmed_range_in_parent(self: opentimelineio._otio.Item) -> Optional[opentimelineio._opentime.TimeRange]"""
    def visible_range(self) -> opentimelineio._opentime.TimeRange:
        """visible_range(self: opentimelineio._otio.Item) -> opentimelineio._opentime.TimeRange"""
    @property
    def available_image_bounds(self) -> Box2d | None:
        """(arg0: opentimelineio._otio.Item) -> Optional[opentimelineio._otio.Box2d]"""
    @property
    def effects(self) -> EffectVector:
        """(arg0: opentimelineio._otio.Item) -> opentimelineio._otio.EffectVector"""
    @property
    def markers(self) -> MarkerVector:
        """(arg0: opentimelineio._otio.Item) -> opentimelineio._otio.MarkerVector"""

class LinearTimeWarp(TimeEffect):
    """
    A time warp that applies a linear speed up or slow down across the entire clip.
    """
    time_scalar: float
    def __init__(self, name: str = ..., time_scalar: float = ..., metadata: object = ...) -> None:
        """__init__(self: opentimelineio._otio.LinearTimeWarp, name: str = '', time_scalar: float = 1.0, metadata: object = None) -> None"""

class Marker(SerializableObjectWithMetadata):
    """
    A marker indicates a marked range of time on an item in a timeline, usually with a name, color or other metadata.

    The marked range may have a zero duration. The marked range is in the owning item's time coordinate system.
    """

    class Color:
        BLACK: ClassVar[str] = ...  # read-only
        BLUE: ClassVar[str] = ...  # read-only
        CYAN: ClassVar[str] = ...  # read-only
        GREEN: ClassVar[str] = ...  # read-only
        MAGENTA: ClassVar[str] = ...  # read-only
        ORANGE: ClassVar[str] = ...  # read-only
        PINK: ClassVar[str] = ...  # read-only
        PURPLE: ClassVar[str] = ...  # read-only
        RED: ClassVar[str] = ...  # read-only
        WHITE: ClassVar[str] = ...  # read-only
        YELLOW: ClassVar[str] = ...  # read-only
        def __init__(self, *args, **kwargs) -> None:
            """Initialize self.  See help(type(self)) for accurate signature."""
    color: str
    comment: str
    marked_range: opentimelineio._opentime.TimeRange
    def __init__(self, name: str = ..., marked_range: opentimelineio._opentime.TimeRange = ..., color: str = ..., metadata: object = ..., comment: str = ...) -> None:
        """__init__(self: opentimelineio._otio.Marker, name: str = '', marked_range: opentimelineio._opentime.TimeRange = otio.opentime.TimeRange(start_time=otio.opentime.RationalTime(value=0, rate=1), duration=otio.opentime.RationalTime(value=0, rate=1)), color: str = 'RED', metadata: object = None, comment: str = '') -> None"""

class MarkerVector:
    append: ClassVar[Callable] = ...
    clear: ClassVar[Callable] = ...
    count: ClassVar[Callable] = ...
    extend: ClassVar[Callable] = ...
    index: ClassVar[Callable] = ...
    insert: ClassVar[Callable] = ...
    pop: ClassVar[Callable] = ...
    remove: ClassVar[Callable] = ...
    reverse: ClassVar[Callable] = ...
    __add__: ClassVar[Callable] = ...
    __contains__: ClassVar[Callable] = ...
    __copy__: ClassVar[Callable] = ...
    __deepcopy__: ClassVar[Callable] = ...
    __delitem__: ClassVar[Callable] = ...
    __getitem__: ClassVar[Callable] = ...
    __iadd__: ClassVar[Callable] = ...
    __radd__: ClassVar[Callable] = ...
    __reversed__: ClassVar[Callable] = ...
    __setitem__: ClassVar[Callable] = ...
    def __init__(self) -> None:
        """__init__(self: opentimelineio._otio.MarkerVector) -> None"""
    def __internal_insert(self, index: int, item) -> None:
        """__internal_insert(self: opentimelineio._otio.MarkerVector, index: int, item: opentimelineio::v1_0::Marker) -> None"""
    def __internal_delitem__(self, index: int) -> None:
        """__internal_delitem__(self: opentimelineio._otio.MarkerVector, index: int) -> None"""
    def __internal_getitem__(self, *args, **kwargs):
        """__internal_getitem__(self: opentimelineio._otio.MarkerVector, index: int) -> opentimelineio::v1_0::Marker"""
    def __internal_setitem__(self, index: int, item) -> None:
        """__internal_setitem__(self: opentimelineio._otio.MarkerVector, index: int, item: opentimelineio::v1_0::Marker) -> None"""
    def __iter__(self) -> MarkerVectorIterator:
        """__iter__(self: opentimelineio._otio.MarkerVector) -> opentimelineio._otio.MarkerVectorIterator"""
    def __len__(self) -> int:
        """__len__(self: opentimelineio._otio.MarkerVector) -> int"""

class MarkerVectorIterator:
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def __iter__(self) -> MarkerVectorIterator:
        """__iter__(self: opentimelineio._otio.MarkerVectorIterator) -> opentimelineio._otio.MarkerVectorIterator"""
    def __next__(self):
        """__next__(self: opentimelineio._otio.MarkerVectorIterator) -> opentimelineio::v1_0::Marker"""

class MediaReference(SerializableObjectWithMetadata):
    available_image_bounds: Box2d | None
    available_range: opentimelineio._opentime.TimeRange | None
    def __init__(self, name: str = ..., available_range: opentimelineio._opentime.TimeRange | None = ..., metadata: object = ..., available_image_bounds: Box2d | None = ...) -> None:
        """__init__(self: opentimelineio._otio.MediaReference, name: str = '', available_range: Optional[opentimelineio._opentime.TimeRange] = None, metadata: object = None, available_image_bounds: Optional[opentimelineio._otio.Box2d] = None) -> None"""
    @property
    def is_missing_reference(self) -> bool:
        """(arg0: opentimelineio._otio.MediaReference) -> bool"""

class MissingReference(MediaReference):
    """
    Represents media for which a concrete reference is missing.

    Note that a :class:`~MissingReference` may have useful metadata, even if the location of the media is not known.
    """
    def __init__(self, name: str = ..., available_range: opentimelineio._opentime.TimeRange | None = ..., metadata: object = ..., available_image_bounds: Box2d | None = ...) -> None:
        """__init__(self: opentimelineio._otio.MissingReference, name: str = '', available_range: Optional[opentimelineio._opentime.TimeRange] = None, metadata: object = None, available_image_bounds: Optional[opentimelineio._otio.Box2d] = None) -> None"""

class NotAChildError(OTIOError): ...

class OTIOError(Exception): ...

class PyAny:
    @overload
    def __init__(self, arg0: bool) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: opentimelineio._otio.PyAny, arg0: bool) -> None

        2. __init__(self: opentimelineio._otio.PyAny, arg0: int) -> None

        3. __init__(self: opentimelineio._otio.PyAny, arg0: float) -> None

        4. __init__(self: opentimelineio._otio.PyAny, arg0: str) -> None

        5. __init__(self: opentimelineio._otio.PyAny, arg0: None) -> None

        6. __init__(self: opentimelineio._otio.PyAny, arg0: opentimelineio._otio.SerializableObject) -> None

        7. __init__(self: opentimelineio._otio.PyAny, arg0: opentimelineio._opentime.RationalTime) -> None

        8. __init__(self: opentimelineio._otio.PyAny, arg0: opentimelineio._opentime.TimeRange) -> None

        9. __init__(self: opentimelineio._otio.PyAny, arg0: opentimelineio._opentime.TimeTransform) -> None

        10. __init__(self: opentimelineio._otio.PyAny, arg0: opentimelineio._otio.AnyVector) -> None

        11. __init__(self: opentimelineio._otio.PyAny, arg0: opentimelineio._otio.AnyDictionary) -> None
        """
    @overload
    def __init__(self, arg0: int) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: opentimelineio._otio.PyAny, arg0: bool) -> None

        2. __init__(self: opentimelineio._otio.PyAny, arg0: int) -> None

        3. __init__(self: opentimelineio._otio.PyAny, arg0: float) -> None

        4. __init__(self: opentimelineio._otio.PyAny, arg0: str) -> None

        5. __init__(self: opentimelineio._otio.PyAny, arg0: None) -> None

        6. __init__(self: opentimelineio._otio.PyAny, arg0: opentimelineio._otio.SerializableObject) -> None

        7. __init__(self: opentimelineio._otio.PyAny, arg0: opentimelineio._opentime.RationalTime) -> None

        8. __init__(self: opentimelineio._otio.PyAny, arg0: opentimelineio._opentime.TimeRange) -> None

        9. __init__(self: opentimelineio._otio.PyAny, arg0: opentimelineio._opentime.TimeTransform) -> None

        10. __init__(self: opentimelineio._otio.PyAny, arg0: opentimelineio._otio.AnyVector) -> None

        11. __init__(self: opentimelineio._otio.PyAny, arg0: opentimelineio._otio.AnyDictionary) -> None
        """
    @overload
    def __init__(self, arg0: float) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: opentimelineio._otio.PyAny, arg0: bool) -> None

        2. __init__(self: opentimelineio._otio.PyAny, arg0: int) -> None

        3. __init__(self: opentimelineio._otio.PyAny, arg0: float) -> None

        4. __init__(self: opentimelineio._otio.PyAny, arg0: str) -> None

        5. __init__(self: opentimelineio._otio.PyAny, arg0: None) -> None

        6. __init__(self: opentimelineio._otio.PyAny, arg0: opentimelineio._otio.SerializableObject) -> None

        7. __init__(self: opentimelineio._otio.PyAny, arg0: opentimelineio._opentime.RationalTime) -> None

        8. __init__(self: opentimelineio._otio.PyAny, arg0: opentimelineio._opentime.TimeRange) -> None

        9. __init__(self: opentimelineio._otio.PyAny, arg0: opentimelineio._opentime.TimeTransform) -> None

        10. __init__(self: opentimelineio._otio.PyAny, arg0: opentimelineio._otio.AnyVector) -> None

        11. __init__(self: opentimelineio._otio.PyAny, arg0: opentimelineio._otio.AnyDictionary) -> None
        """
    @overload
    def __init__(self, arg0: str) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: opentimelineio._otio.PyAny, arg0: bool) -> None

        2. __init__(self: opentimelineio._otio.PyAny, arg0: int) -> None

        3. __init__(self: opentimelineio._otio.PyAny, arg0: float) -> None

        4. __init__(self: opentimelineio._otio.PyAny, arg0: str) -> None

        5. __init__(self: opentimelineio._otio.PyAny, arg0: None) -> None

        6. __init__(self: opentimelineio._otio.PyAny, arg0: opentimelineio._otio.SerializableObject) -> None

        7. __init__(self: opentimelineio._otio.PyAny, arg0: opentimelineio._opentime.RationalTime) -> None

        8. __init__(self: opentimelineio._otio.PyAny, arg0: opentimelineio._opentime.TimeRange) -> None

        9. __init__(self: opentimelineio._otio.PyAny, arg0: opentimelineio._opentime.TimeTransform) -> None

        10. __init__(self: opentimelineio._otio.PyAny, arg0: opentimelineio._otio.AnyVector) -> None

        11. __init__(self: opentimelineio._otio.PyAny, arg0: opentimelineio._otio.AnyDictionary) -> None
        """
    @overload
    def __init__(self, arg0: None) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: opentimelineio._otio.PyAny, arg0: bool) -> None

        2. __init__(self: opentimelineio._otio.PyAny, arg0: int) -> None

        3. __init__(self: opentimelineio._otio.PyAny, arg0: float) -> None

        4. __init__(self: opentimelineio._otio.PyAny, arg0: str) -> None

        5. __init__(self: opentimelineio._otio.PyAny, arg0: None) -> None

        6. __init__(self: opentimelineio._otio.PyAny, arg0: opentimelineio._otio.SerializableObject) -> None

        7. __init__(self: opentimelineio._otio.PyAny, arg0: opentimelineio._opentime.RationalTime) -> None

        8. __init__(self: opentimelineio._otio.PyAny, arg0: opentimelineio._opentime.TimeRange) -> None

        9. __init__(self: opentimelineio._otio.PyAny, arg0: opentimelineio._opentime.TimeTransform) -> None

        10. __init__(self: opentimelineio._otio.PyAny, arg0: opentimelineio._otio.AnyVector) -> None

        11. __init__(self: opentimelineio._otio.PyAny, arg0: opentimelineio._otio.AnyDictionary) -> None
        """
    @overload
    def __init__(self, arg0: SerializableObject) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: opentimelineio._otio.PyAny, arg0: bool) -> None

        2. __init__(self: opentimelineio._otio.PyAny, arg0: int) -> None

        3. __init__(self: opentimelineio._otio.PyAny, arg0: float) -> None

        4. __init__(self: opentimelineio._otio.PyAny, arg0: str) -> None

        5. __init__(self: opentimelineio._otio.PyAny, arg0: None) -> None

        6. __init__(self: opentimelineio._otio.PyAny, arg0: opentimelineio._otio.SerializableObject) -> None

        7. __init__(self: opentimelineio._otio.PyAny, arg0: opentimelineio._opentime.RationalTime) -> None

        8. __init__(self: opentimelineio._otio.PyAny, arg0: opentimelineio._opentime.TimeRange) -> None

        9. __init__(self: opentimelineio._otio.PyAny, arg0: opentimelineio._opentime.TimeTransform) -> None

        10. __init__(self: opentimelineio._otio.PyAny, arg0: opentimelineio._otio.AnyVector) -> None

        11. __init__(self: opentimelineio._otio.PyAny, arg0: opentimelineio._otio.AnyDictionary) -> None
        """
    @overload
    def __init__(self, arg0: opentimelineio._opentime.RationalTime) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: opentimelineio._otio.PyAny, arg0: bool) -> None

        2. __init__(self: opentimelineio._otio.PyAny, arg0: int) -> None

        3. __init__(self: opentimelineio._otio.PyAny, arg0: float) -> None

        4. __init__(self: opentimelineio._otio.PyAny, arg0: str) -> None

        5. __init__(self: opentimelineio._otio.PyAny, arg0: None) -> None

        6. __init__(self: opentimelineio._otio.PyAny, arg0: opentimelineio._otio.SerializableObject) -> None

        7. __init__(self: opentimelineio._otio.PyAny, arg0: opentimelineio._opentime.RationalTime) -> None

        8. __init__(self: opentimelineio._otio.PyAny, arg0: opentimelineio._opentime.TimeRange) -> None

        9. __init__(self: opentimelineio._otio.PyAny, arg0: opentimelineio._opentime.TimeTransform) -> None

        10. __init__(self: opentimelineio._otio.PyAny, arg0: opentimelineio._otio.AnyVector) -> None

        11. __init__(self: opentimelineio._otio.PyAny, arg0: opentimelineio._otio.AnyDictionary) -> None
        """
    @overload
    def __init__(self, arg0: opentimelineio._opentime.TimeRange) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: opentimelineio._otio.PyAny, arg0: bool) -> None

        2. __init__(self: opentimelineio._otio.PyAny, arg0: int) -> None

        3. __init__(self: opentimelineio._otio.PyAny, arg0: float) -> None

        4. __init__(self: opentimelineio._otio.PyAny, arg0: str) -> None

        5. __init__(self: opentimelineio._otio.PyAny, arg0: None) -> None

        6. __init__(self: opentimelineio._otio.PyAny, arg0: opentimelineio._otio.SerializableObject) -> None

        7. __init__(self: opentimelineio._otio.PyAny, arg0: opentimelineio._opentime.RationalTime) -> None

        8. __init__(self: opentimelineio._otio.PyAny, arg0: opentimelineio._opentime.TimeRange) -> None

        9. __init__(self: opentimelineio._otio.PyAny, arg0: opentimelineio._opentime.TimeTransform) -> None

        10. __init__(self: opentimelineio._otio.PyAny, arg0: opentimelineio._otio.AnyVector) -> None

        11. __init__(self: opentimelineio._otio.PyAny, arg0: opentimelineio._otio.AnyDictionary) -> None
        """
    @overload
    def __init__(self, arg0: opentimelineio._opentime.TimeTransform) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: opentimelineio._otio.PyAny, arg0: bool) -> None

        2. __init__(self: opentimelineio._otio.PyAny, arg0: int) -> None

        3. __init__(self: opentimelineio._otio.PyAny, arg0: float) -> None

        4. __init__(self: opentimelineio._otio.PyAny, arg0: str) -> None

        5. __init__(self: opentimelineio._otio.PyAny, arg0: None) -> None

        6. __init__(self: opentimelineio._otio.PyAny, arg0: opentimelineio._otio.SerializableObject) -> None

        7. __init__(self: opentimelineio._otio.PyAny, arg0: opentimelineio._opentime.RationalTime) -> None

        8. __init__(self: opentimelineio._otio.PyAny, arg0: opentimelineio._opentime.TimeRange) -> None

        9. __init__(self: opentimelineio._otio.PyAny, arg0: opentimelineio._opentime.TimeTransform) -> None

        10. __init__(self: opentimelineio._otio.PyAny, arg0: opentimelineio._otio.AnyVector) -> None

        11. __init__(self: opentimelineio._otio.PyAny, arg0: opentimelineio._otio.AnyDictionary) -> None
        """
    @overload
    def __init__(self, arg0: AnyVector) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: opentimelineio._otio.PyAny, arg0: bool) -> None

        2. __init__(self: opentimelineio._otio.PyAny, arg0: int) -> None

        3. __init__(self: opentimelineio._otio.PyAny, arg0: float) -> None

        4. __init__(self: opentimelineio._otio.PyAny, arg0: str) -> None

        5. __init__(self: opentimelineio._otio.PyAny, arg0: None) -> None

        6. __init__(self: opentimelineio._otio.PyAny, arg0: opentimelineio._otio.SerializableObject) -> None

        7. __init__(self: opentimelineio._otio.PyAny, arg0: opentimelineio._opentime.RationalTime) -> None

        8. __init__(self: opentimelineio._otio.PyAny, arg0: opentimelineio._opentime.TimeRange) -> None

        9. __init__(self: opentimelineio._otio.PyAny, arg0: opentimelineio._opentime.TimeTransform) -> None

        10. __init__(self: opentimelineio._otio.PyAny, arg0: opentimelineio._otio.AnyVector) -> None

        11. __init__(self: opentimelineio._otio.PyAny, arg0: opentimelineio._otio.AnyDictionary) -> None
        """
    @overload
    def __init__(self, arg0: AnyDictionary) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: opentimelineio._otio.PyAny, arg0: bool) -> None

        2. __init__(self: opentimelineio._otio.PyAny, arg0: int) -> None

        3. __init__(self: opentimelineio._otio.PyAny, arg0: float) -> None

        4. __init__(self: opentimelineio._otio.PyAny, arg0: str) -> None

        5. __init__(self: opentimelineio._otio.PyAny, arg0: None) -> None

        6. __init__(self: opentimelineio._otio.PyAny, arg0: opentimelineio._otio.SerializableObject) -> None

        7. __init__(self: opentimelineio._otio.PyAny, arg0: opentimelineio._opentime.RationalTime) -> None

        8. __init__(self: opentimelineio._otio.PyAny, arg0: opentimelineio._opentime.TimeRange) -> None

        9. __init__(self: opentimelineio._otio.PyAny, arg0: opentimelineio._opentime.TimeTransform) -> None

        10. __init__(self: opentimelineio._otio.PyAny, arg0: opentimelineio._otio.AnyVector) -> None

        11. __init__(self: opentimelineio._otio.PyAny, arg0: opentimelineio._otio.AnyDictionary) -> None
        """

class SerializableCollection(SerializableObjectWithMetadata):
    """
    A container which can hold an ordered list of any serializable objects. Note that this is not a :class:`.Composition` nor is it :class:`.Composable`.

    This container approximates the concept of a bin - a collection of :class:`.SerializableObject`\\s that do
    not have any compositional meaning, but can serialize to/from OTIO correctly, with metadata and
    a named collection.

    A :class:`~SerializableCollection` is useful for serializing multiple timelines, clips, or media references to a single file.
    """
    append: ClassVar[Callable] = ...
    clear: ClassVar[Callable] = ...
    count: ClassVar[Callable] = ...
    extend: ClassVar[Callable] = ...
    index: ClassVar[Callable] = ...
    insert: ClassVar[Callable] = ...
    pop: ClassVar[Callable] = ...
    remove: ClassVar[Callable] = ...
    reverse: ClassVar[Callable] = ...
    __add__: ClassVar[Callable] = ...
    __contains__: ClassVar[Callable] = ...
    __delitem__: ClassVar[Callable] = ...
    __getitem__: ClassVar[Callable] = ...
    __iadd__: ClassVar[Callable] = ...
    __radd__: ClassVar[Callable] = ...
    __reversed__: ClassVar[Callable] = ...
    __setitem__: ClassVar[Callable] = ...
    def __init__(self, name: str = ..., children: list[SerializableObject] | None = ..., metadata: object = ...) -> None:
        """__init__(self: opentimelineio._otio.SerializableCollection, name: str = '', children: Optional[List[opentimelineio._otio.SerializableObject]] = None, metadata: object = None) -> None"""
    def __internal_insert(self, index: int, item: SerializableObject) -> None:
        """__internal_insert(self: opentimelineio._otio.SerializableCollection, index: int, item: opentimelineio._otio.SerializableObject) -> None"""
    def find_children(self, descended_from_type: object = ..., search_range: opentimelineio._opentime.TimeRange | None = ..., shallow_search: bool = ...) -> list[SerializableObject]:
        """find_children(self: opentimelineio._otio.SerializableCollection, descended_from_type: object = None, search_range: Optional[opentimelineio._opentime.TimeRange] = None, shallow_search: bool = False) -> List[opentimelineio._otio.SerializableObject]"""
    def find_clips(self, search_range: opentimelineio._opentime.TimeRange | None = ..., shallow_search: bool = ...) -> list[SerializableObject]:
        """find_clips(self: opentimelineio._otio.SerializableCollection, search_range: Optional[opentimelineio._opentime.TimeRange] = None, shallow_search: bool = False) -> List[opentimelineio._otio.SerializableObject]"""
    def __internal_delitem__(self, index: int) -> None:
        """__internal_delitem__(self: opentimelineio._otio.SerializableCollection, index: int) -> None"""
    def __internal_getitem__(self, index: int) -> SerializableObject:
        """__internal_getitem__(self: opentimelineio._otio.SerializableCollection, index: int) -> opentimelineio._otio.SerializableObject"""
    def __internal_setitem__(self, index: int, item: SerializableObject) -> None:
        """__internal_setitem__(self: opentimelineio._otio.SerializableCollection, index: int, item: opentimelineio._otio.SerializableObject) -> None"""
    def __iter__(self) -> SerializableCollectionIterator:
        """__iter__(self: opentimelineio._otio.SerializableCollection) -> opentimelineio._otio.SerializableCollectionIterator"""
    def __len__(self) -> int:
        """__len__(self: opentimelineio._otio.SerializableCollection) -> int"""

class SerializableCollectionIterator:
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def __iter__(self) -> SerializableCollectionIterator:
        """__iter__(self: opentimelineio._otio.SerializableCollectionIterator) -> opentimelineio._otio.SerializableCollectionIterator"""
    def __next__(self) -> SerializableObject:
        """__next__(self: opentimelineio._otio.SerializableCollectionIterator) -> opentimelineio._otio.SerializableObject"""

class SerializableObject:
    """Superclass for all classes whose instances can be serialized."""
    deepcopy: ClassVar[Callable] = ...
    __copy__: ClassVar[Callable] = ...
    __deepcopy__: ClassVar[Callable] = ...
    __setattr__: ClassVar[Callable] = ...
    def __init__(self) -> None:
        """__init__(self: opentimelineio._otio.SerializableObject) -> None"""
    def clone(self) -> SerializableObject:
        """clone(self: opentimelineio._otio.SerializableObject) -> opentimelineio._otio.SerializableObject"""
    @staticmethod
    def from_json_file(file_name: str) -> SerializableObject:
        """from_json_file(file_name: str) -> opentimelineio._otio.SerializableObject"""
    @staticmethod
    def from_json_string(input: str) -> SerializableObject:
        """from_json_string(input: str) -> opentimelineio._otio.SerializableObject"""
    def is_equivalent_to(self, other: SerializableObject) -> bool:
        """is_equivalent_to(self: opentimelineio._otio.SerializableObject, other: opentimelineio._otio.SerializableObject) -> bool"""
    def schema_name(self) -> str:
        """schema_name(self: opentimelineio._otio.SerializableObject) -> str"""
    def schema_version(self) -> int:
        """schema_version(self: opentimelineio._otio.SerializableObject) -> int"""
    def to_json_file(self, file_name: str, indent: int = ...) -> bool:
        """to_json_file(self: opentimelineio._otio.SerializableObject, file_name: str, indent: int = 4) -> bool"""
    def to_json_string(self, indent: int = ...) -> str:
        """to_json_string(self: opentimelineio._otio.SerializableObject, indent: int = 4) -> str"""
    @property
    def _dynamic_fields(self) -> AnyDictionary:
        """(arg0: opentimelineio._otio.SerializableObject) -> opentimelineio._otio.AnyDictionary"""
    @property
    def is_unknown_schema(self) -> bool:
        """(arg0: opentimelineio._otio.SerializableObject) -> bool"""

class SerializableObjectWithMetadata(SerializableObject):
    name: object
    def __init__(self, name: str = ..., metadata: object = ...) -> None:
        """__init__(self: opentimelineio._otio.SerializableObjectWithMetadata, name: str = '', metadata: object = None) -> None"""
    @property
    def metadata(self) -> AnyDictionary:
        """(arg0: opentimelineio._otio.SerializableObjectWithMetadata) -> opentimelineio._otio.AnyDictionary"""

class Stack(Composition):
    def __init__(self, name: str = ..., children: list[Composable] | None = ..., source_range: opentimelineio._opentime.TimeRange | None = ..., markers: list[Marker] | None = ..., effects: list[Effect] | None = ..., metadata: object = ...) -> None:
        """__init__(self: opentimelineio._otio.Stack, name: str = '', children: Optional[List[opentimelineio._otio.Composable]] = None, source_range: Optional[opentimelineio._opentime.TimeRange] = None, markers: Optional[List[opentimelineio._otio.Marker]] = None, effects: Optional[List[opentimelineio._otio.Effect]] = None, metadata: object = None) -> None"""
    def find_clips(self, search_range: opentimelineio._opentime.TimeRange | None = ..., shallow_search: bool = ...) -> list[SerializableObject]:
        """find_clips(self: opentimelineio._otio.Stack, search_range: Optional[opentimelineio._opentime.TimeRange] = None, shallow_search: bool = False) -> List[opentimelineio._otio.SerializableObject]"""

class TestObject(SerializableObjectWithMetadata):
    def __init__(self, name: str) -> None:
        """__init__(self: opentimelineio._otio.TestObject, name: str) -> None"""
    def lookup(self, key: str) -> SerializableObject:
        """lookup(self: opentimelineio._otio.TestObject, key: str) -> opentimelineio._otio.SerializableObject"""

class TimeEffect(Effect):
    """Base class for all effects that alter the timing of an item."""
    def __init__(self, name: str = ..., effect_name: str = ..., metadata: object = ...) -> None:
        """__init__(self: opentimelineio._otio.TimeEffect, name: str = '', effect_name: str = '', metadata: object = None) -> None"""

class Timeline(SerializableObjectWithMetadata):
    global_start_time: opentimelineio._opentime.RationalTime | None
    tracks: Stack
    def __init__(self, name: str = ..., tracks: list[Composable] | None = ..., global_start_time: opentimelineio._opentime.RationalTime | None = ..., metadata: object = ...) -> None:
        """__init__(self: opentimelineio._otio.Timeline, name: str = '', tracks: Optional[List[opentimelineio._otio.Composable]] = None, global_start_time: Optional[opentimelineio._opentime.RationalTime] = None, metadata: object = None) -> None"""
    def audio_tracks(self) -> list[Track]:
        """audio_tracks(self: opentimelineio._otio.Timeline) -> List[opentimelineio._otio.Track]"""
    def duration(self) -> opentimelineio._opentime.RationalTime:
        """duration(self: opentimelineio._otio.Timeline) -> opentimelineio._opentime.RationalTime"""
    def find_children(self, descended_from_type: object = ..., search_range: opentimelineio._opentime.TimeRange | None = ..., shallow_search: bool = ...) -> list[SerializableObject]:
        """find_children(self: opentimelineio._otio.Timeline, descended_from_type: object = None, search_range: Optional[opentimelineio._opentime.TimeRange] = None, shallow_search: bool = False) -> List[opentimelineio._otio.SerializableObject]"""
    def find_clips(self, search_range: opentimelineio._opentime.TimeRange | None = ..., shallow_search: bool = ...) -> list[SerializableObject]:
        """find_clips(self: opentimelineio._otio.Timeline, search_range: Optional[opentimelineio._opentime.TimeRange] = None, shallow_search: bool = False) -> List[opentimelineio._otio.SerializableObject]"""
    def range_of_child(self, arg0: Composable) -> opentimelineio._opentime.TimeRange:
        """range_of_child(self: opentimelineio._otio.Timeline, arg0: opentimelineio._otio.Composable) -> opentimelineio._opentime.TimeRange"""
    def video_tracks(self) -> list[Track]:
        """video_tracks(self: opentimelineio._otio.Timeline) -> List[opentimelineio._otio.Track]"""

class Track(Composition):
    class Kind:
        Audio: ClassVar[str] = ...  # read-only
        Video: ClassVar[str] = ...  # read-only
        def __init__(self, *args, **kwargs) -> None:
            """Initialize self.  See help(type(self)) for accurate signature."""

    class NeighborGapPolicy:
        """Members:

          around_transitions

          never"""
        __members__: ClassVar[dict] = ...  # read-only
        __entries: ClassVar[dict] = ...
        around_transitions: ClassVar[Track.NeighborGapPolicy] = ...
        never: ClassVar[Track.NeighborGapPolicy] = ...
        def __init__(self, value: int) -> None:
            """__init__(self: opentimelineio._otio.Track.NeighborGapPolicy, value: int) -> None"""
        def __eq__(self, other: object) -> bool:
            """__eq__(self: object, other: object) -> bool"""
        def __hash__(self) -> int:
            """__hash__(self: object) -> int"""
        def __index__(self) -> int:
            """__index__(self: opentimelineio._otio.Track.NeighborGapPolicy) -> int"""
        def __int__(self) -> int:
            """__int__(self: opentimelineio._otio.Track.NeighborGapPolicy) -> int"""
        def __ne__(self, other: object) -> bool:
            """__ne__(self: object, other: object) -> bool"""
        @property
        def name(self) -> str:
            """name(self: handle) -> str

            name(self: handle) -> str
            """
        @property
        def value(self) -> int:
            """(arg0: opentimelineio._otio.Track.NeighborGapPolicy) -> int"""
    kind: str
    def __init__(self, name: str = ..., children: list[Composable] | None = ..., source_range: opentimelineio._opentime.TimeRange | None = ..., kind: str = ..., metadata: object = ...) -> None:
        """__init__(self: opentimelineio._otio.Track, name: str = '', children: Optional[List[opentimelineio._otio.Composable]] = None, source_range: Optional[opentimelineio._opentime.TimeRange] = None, kind: str = 'Video', metadata: object = None) -> None"""
    def find_clips(self, search_range: opentimelineio._opentime.TimeRange | None = ..., shallow_search: bool = ...) -> list[SerializableObject]:
        """find_clips(self: opentimelineio._otio.Track, search_range: Optional[opentimelineio._opentime.TimeRange] = None, shallow_search: bool = False) -> List[opentimelineio._otio.SerializableObject]"""
    def neighbors_of(self, item: Composable, policy: Track.NeighborGapPolicy = ...) -> tuple:
        """neighbors_of(self: opentimelineio._otio.Track, item: opentimelineio._otio.Composable, policy: opentimelineio._otio.Track.NeighborGapPolicy = <NeighborGapPolicy.never: 0>) -> tuple"""

class Transition(Composable):
    """Represents a transition between the two adjacent items in a :class:`.Track`. For example, a cross dissolve or wipe."""

    class Type:
        """
        Enum encoding types of transitions.

        Other effects are handled by the :class:`Effect` class.
        """
        Custom: ClassVar[str] = ...  # read-only
        SMPTE_Dissolve: ClassVar[str] = ...  # read-only
        def __init__(self, *args, **kwargs) -> None:
            """Initialize self.  See help(type(self)) for accurate signature."""
    in_offset: opentimelineio._opentime.RationalTime
    out_offset: opentimelineio._opentime.RationalTime
    transition_type: str
    def __init__(self, name: str = ..., transition_type: str = ..., in_offset: opentimelineio._opentime.RationalTime = ..., out_offset: opentimelineio._opentime.RationalTime = ..., metadata: object = ...) -> None:
        """__init__(self: opentimelineio._otio.Transition, name: str = '', transition_type: str = '', in_offset: opentimelineio._opentime.RationalTime = otio.opentime.RationalTime(value=0, rate=1), out_offset: opentimelineio._opentime.RationalTime = otio.opentime.RationalTime(value=0, rate=1), metadata: object = None) -> None"""
    def duration(self) -> opentimelineio._opentime.RationalTime:
        """duration(self: opentimelineio._otio.Transition) -> opentimelineio._opentime.RationalTime"""
    def range_in_parent(self) -> opentimelineio._opentime.TimeRange | None:
        """range_in_parent(self: opentimelineio._otio.Transition) -> Optional[opentimelineio._opentime.TimeRange]

        Find and return the range of this item in the parent.
        """
    def trimmed_range_in_parent(self) -> opentimelineio._opentime.TimeRange | None:
        """trimmed_range_in_parent(self: opentimelineio._otio.Transition) -> Optional[opentimelineio._opentime.TimeRange]

        Find and return the timmed range of this item in the parent.
        """

class UnknownSchema(SerializableObject):
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    @property
    def original_schema_name(self) -> str:
        """(arg0: opentimelineio._otio.UnknownSchema) -> str"""
    @property
    def original_schema_version(self) -> int:
        """(arg0: opentimelineio._otio.UnknownSchema) -> int"""

class UnsupportedSchemaError(OTIOError): ...

class V2d:
    x: float
    y: float
    @overload
    def __init__(self) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: opentimelineio._otio.V2d) -> None

        2. __init__(self: opentimelineio._otio.V2d, arg0: float) -> None

        3. __init__(self: opentimelineio._otio.V2d, arg0: float, arg1: float) -> None
        """
    @overload
    def __init__(self, arg0: float) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: opentimelineio._otio.V2d) -> None

        2. __init__(self: opentimelineio._otio.V2d, arg0: float) -> None

        3. __init__(self: opentimelineio._otio.V2d, arg0: float, arg1: float) -> None
        """
    @overload
    def __init__(self, arg0: float, arg1: float) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: opentimelineio._otio.V2d) -> None

        2. __init__(self: opentimelineio._otio.V2d, arg0: float) -> None

        3. __init__(self: opentimelineio._otio.V2d, arg0: float, arg1: float) -> None
        """
    @staticmethod
    def baseTypeEpsilon() -> float:
        """baseTypeEpsilon() -> float"""
    @staticmethod
    def baseTypeLowest() -> float:
        """baseTypeLowest() -> float"""
    @staticmethod
    def baseTypeMax() -> float:
        """baseTypeMax() -> float"""
    @staticmethod
    def baseTypeSmallest() -> float:
        """baseTypeSmallest() -> float"""
    def cross(self, arg0: V2d) -> float:
        """cross(self: opentimelineio._otio.V2d, arg0: opentimelineio._otio.V2d) -> float"""
    @staticmethod
    def dimensions() -> int:
        """dimensions() -> int"""
    def dot(self, arg0: V2d) -> float:
        """dot(self: opentimelineio._otio.V2d, arg0: opentimelineio._otio.V2d) -> float"""
    def equalWithAbsError(self, arg0: V2d, arg1: float) -> bool:
        """equalWithAbsError(self: opentimelineio._otio.V2d, arg0: opentimelineio._otio.V2d, arg1: float) -> bool"""
    def equalWithRelError(self, arg0: V2d, arg1: float) -> bool:
        """equalWithRelError(self: opentimelineio._otio.V2d, arg0: opentimelineio._otio.V2d, arg1: float) -> bool"""
    def length(self) -> float:
        """length(self: opentimelineio._otio.V2d) -> float"""
    def length2(self) -> float:
        """length2(self: opentimelineio._otio.V2d) -> float"""
    def normalize(self) -> V2d:
        """normalize(self: opentimelineio._otio.V2d) -> opentimelineio._otio.V2d"""
    def normalizeExc(self) -> V2d:
        """normalizeExc(self: opentimelineio._otio.V2d) -> opentimelineio._otio.V2d"""
    def normalizeNonNull(self) -> V2d:
        """normalizeNonNull(self: opentimelineio._otio.V2d) -> opentimelineio._otio.V2d"""
    def normalized(self) -> V2d:
        """normalized(self: opentimelineio._otio.V2d) -> opentimelineio._otio.V2d"""
    def normalizedExc(self) -> V2d:
        """normalizedExc(self: opentimelineio._otio.V2d) -> opentimelineio._otio.V2d"""
    def normalizedNonNull(self) -> V2d:
        """normalizedNonNull(self: opentimelineio._otio.V2d) -> opentimelineio._otio.V2d"""
    def __add__(self, arg0: V2d) -> V2d:
        """__add__(self: opentimelineio._otio.V2d, arg0: opentimelineio._otio.V2d) -> opentimelineio._otio.V2d"""
    def __eq__(self, arg0: object) -> bool:
        """__eq__(self: opentimelineio._otio.V2d, arg0: object) -> bool"""
    def __getitem__(self, arg0: int) -> float:
        """__getitem__(self: opentimelineio._otio.V2d, arg0: int) -> float"""
    def __iter__(self) -> typing.Iterator[float]:
        """def __iter__(self) -> typing.Iterator[float]"""
    def __iadd__(self, arg0: V2d) -> V2d:
        """__iadd__(self: opentimelineio._otio.V2d, arg0: opentimelineio._otio.V2d) -> opentimelineio._otio.V2d"""
    def __idiv__(self, arg0: V2d) -> V2d:
        """__idiv__(self: opentimelineio._otio.V2d, arg0: opentimelineio._otio.V2d) -> opentimelineio._otio.V2d"""
    def __imul__(self, arg0: V2d) -> V2d:
        """__imul__(self: opentimelineio._otio.V2d, arg0: opentimelineio._otio.V2d) -> opentimelineio._otio.V2d"""
    def __isub__(self, arg0: V2d) -> V2d:
        """__isub__(self: opentimelineio._otio.V2d, arg0: opentimelineio._otio.V2d) -> opentimelineio._otio.V2d"""
    def __mod__(self, arg0: object) -> float:
        """__mod__(self: opentimelineio._otio.V2d, arg0: object) -> float"""
    def __mul__(self, arg0: V2d) -> V2d:
        """__mul__(self: opentimelineio._otio.V2d, arg0: opentimelineio._otio.V2d) -> opentimelineio._otio.V2d"""
    def __ne__(self, arg0: object) -> bool:
        """__ne__(self: opentimelineio._otio.V2d, arg0: object) -> bool"""
    def __sub__(self, arg0: V2d) -> V2d:
        """__sub__(self: opentimelineio._otio.V2d, arg0: opentimelineio._otio.V2d) -> opentimelineio._otio.V2d"""
    def __truediv__(self, arg0: V2d) -> V2d:
        """__truediv__(self: opentimelineio._otio.V2d, arg0: opentimelineio._otio.V2d) -> opentimelineio._otio.V2d"""
    def __xor__(self, arg0: object) -> float:
        """__xor__(self: opentimelineio._otio.V2d, arg0: object) -> float"""

def _serialize_json_to_file(value: PyAny, filename: str, schema_version_targets: dict[str, int], indent: int) -> bool:
    """_serialize_json_to_file(value: PyAny, filename: str, schema_version_targets: Dict[str, int], indent: int) -> bool"""
def _serialize_json_to_string(value: PyAny, schema_version_targets: dict[str, int], indent: int) -> str:
    """_serialize_json_to_string(value: PyAny, schema_version_targets: Dict[str, int], indent: int) -> str"""
def deserialize_json_from_file(filename: str) -> object:
    """deserialize_json_from_file(filename: str) -> object

    Deserialize json file to in-memory objects.

    :param str filename: path to json file to read

    :returns: root object in the file (usually a Timeline or SerializableCollection)
    :rtype: SerializableObject


    """
def deserialize_json_from_string(input: str) -> object:
    """deserialize_json_from_string(input: str) -> object

    Deserialize json string to in-memory objects.

    :param str input: json string to deserialize

    :returns: root object in the string (usually a Timeline or SerializableCollection)
    :rtype: SerializableObject


    """
@overload
def flatten_stack(in_stack: Stack) -> Track:
    """flatten_stack(*args, **kwargs)
    Overloaded function.

    1. flatten_stack(in_stack: opentimelineio._otio.Stack) -> opentimelineio._otio.Track

    2. flatten_stack(tracks: List[opentimelineio._otio.Track]) -> opentimelineio._otio.Track
    """
@overload
def flatten_stack(tracks: list[Track]) -> Track:
    """flatten_stack(*args, **kwargs)
    Overloaded function.

    1. flatten_stack(in_stack: opentimelineio._otio.Stack) -> opentimelineio._otio.Track

    2. flatten_stack(tracks: List[opentimelineio._otio.Track]) -> opentimelineio._otio.Track
    """
def install_external_keepalive_monitor(so: SerializableObject, apply_now: bool) -> None:
    """install_external_keepalive_monitor(so: opentimelineio._otio.SerializableObject, apply_now: bool) -> None"""
def instance_from_schema(schema_name: str, schema_version: int, data: object) -> SerializableObject:
    """instance_from_schema(schema_name: str, schema_version: int, data: object) -> opentimelineio._otio.SerializableObject


    Return an instance of the schema from data in the data_dict.

    :raises UnsupportedSchemaError: when the requested schema version is greater than the registered schema version.

    """
def register_downgrade_function(schema_name: str, version_to_downgrade_from: int, downgrade_function: Callable[[AnyDictionary], None]) -> bool:
    """register_downgrade_function(schema_name: str, version_to_downgrade_from: int, downgrade_function: Callable[[opentimelineio._otio.AnyDictionary], None]) -> bool"""
def register_serializable_object_type(class_object: object, schema_name: str, schema_version: int) -> None:
    """register_serializable_object_type(class_object: object, schema_name: str, schema_version: int) -> None"""
def register_upgrade_function(schema_name: str, version_to_upgrade_to: int, upgrade_function: Callable[[AnyDictionary], None]) -> bool:
    """register_upgrade_function(schema_name: str, version_to_upgrade_to: int, upgrade_function: Callable[[opentimelineio._otio.AnyDictionary], None]) -> bool"""
def release_to_schema_version_map() -> dict[str, dict[str, int]]:
    '''release_to_schema_version_map() -> Dict[str, Dict[str, int]]

    Fetch the compiled in CORE_VERSION_MAP.  

    The CORE_VERSION_MAP maps OTIO release versions to maps of schema name to schema version and is autogenerated by the OpenTimelineIO build and release system.  For example: `{"0.15.0": {"Clip": 2, ...}}`

    :returns: dictionary mapping core version label to schema_version_map
    :rtype: dict[str, dict[str, int]]
    '''
def set_type_record(serializable_obejct: SerializableObject, schema_name: str) -> None:
    """set_type_record(serializable_obejct: opentimelineio._otio.SerializableObject, schema_name: str) -> None"""
def type_version_map() -> dict[str, int]:
    """type_version_map() -> Dict[str, int]

    Fetch the currently registered schemas and their versions.

    :returns: Map of all registered schema names to their current versions.
    :rtype: dict[str, int]
    """
