import dataclasses
from .colormanagement import Color as Color, ResourceColorSpace as ResourceColorSpace
from .properties import Property as Property, PropertyValue as PropertyValue
from _typeshed import Incomplete
from enum import Enum
from substance_painter import layerstack as layerstack, levels as levels
from substance_painter._utility import ReadOnlyUid as ReadOnlyUid
from substance_painter.levels import LevelsParams as LevelsParams
from substance_painter.resource import ResourceID as ResourceID
from substance_painter.textureset import ChannelType as ChannelType

from _substance_painter.source import SourceMode as SourceMode

class FontResolutionMode(Enum):
    """
    Members:

    ================= ================================================
    Name              Description
    ================= ================================================
    ``Auto``          Resolution is automatically computed.
    ``Manual``        Resolution is manually provided.
    ================= ================================================

    .. warning::
        Deprecated since 0.3.4, use :class:`~substance_painter.source.ResolutionMode` instead.
    """
    Auto = ...
    Manual = ...

from _substance_painter.source import HorizontalAlignment as HorizontalAlignment
from _substance_painter.source import VerticalAlignment as VerticalAlignment

class ResolutionMode(Enum):
    """
    Members:

    ================= ==================================================
    Name              Description
    ================= ==================================================
    ``Auto``          Resolution matches the parent context, such as the Texture Set
                      resolution in a fill layer, or 512 pixels in a brush tool.
    ``Asset``         Resolution uses the pixel size defined in the vector file.
                      Not applicable for Font resources.
    ``Custom``        Resolution is manually provided.
    ``TextureSet``    Resolution matches the parent textureset's resolution.
    ``UVTile``        Resolution matches the current uvtile's resolution.
    ``Document``      Deprecated since 0.3.4, use `Asset` instead.
    ``Manual``        Deprecated since 0.3.4, use `Custom` instead.
    ================= ==================================================
    """
    Auto = ...
    Asset = ...
    Custom = ...
    TextureSet = ...
    UVTile = ...
    Document = ...
    Manual = ...
VectorialResolutionMode = ResolutionMode
from _substance_painter.source import CropAreaMode as CropAreaMode
from _substance_painter.source import AlphaMatte as AlphaMatte

@dataclasses.dataclass
class ResolutionOverride:
    """
    Resolution override parameters.

    :param mode: Control how the resource rendering resolution is driven.
    :param value: The resolution to use when `mode` is
        :class:`ResolutionMode.Manual <ResolutionMode>`, as [width, height] in pixels.
        Values must be a power of 2, in range [128, 4096].
    :param log2_offset: Log2 resolution boost or reduce, applied on both width and height.
        Only used if `mode` is set to :class:`ResolutionMode.Auto <ResolutionMode>`.
    """
    mode: ResolutionMode
    value: tuple[int, int]
    log2_offset: int
    def __setattr__(self, __name: str, /, __value: dataclasses.Any) -> None: ...  # type: ignore[name-defined]

class _ResolutionOverrideDeprecated:
    """Helpers to add deprecated properties for retrocompatibility."""
    @property
    def resolution_mode(self):
        """
        :meta private:
        """
    @resolution_mode.setter
    def resolution_mode(self, value) -> None:
        """
        :meta private:
        """
    @property
    def resolution_value(self):
        """
        :meta private:
        """
    @resolution_value.setter
    def resolution_value(self, value) -> None:
        """
        :meta private:
        """

class ActiveChannelsMixin:
    """
    Mixin providing active channels property.

    :meta private:
    """
    @property
    def active_channels(self) -> set[ChannelType]:
        """
        The set of active channels of the source.

        :getter: Returns the active channels of the source. To get the list of channels
            for a given stack, see :meth:`substance_painter.textureset.Stack.all_channels`.
        :setter: Sets the active channels of the source, channels not listed will be
            disabled.
        """
    @active_channels.setter
    def active_channels(self, channels: set[ChannelType]) -> None: ...

class SourceEditorMixin(ActiveChannelsMixin):
    """
    Mixin providing all necessary functions to edit sources.

    :meta private:
    """
    @property
    def source_mode(self) -> SourceMode:
        """
        The current context in which the source is edited:

        * ``Material``: only one source is used to write to several
          channels, see :func:`~get_material_source` and :func:`~set_material_source`.
        * ``Split``: each source write to a single channel, see :func:`~get_source` and
          :func:`~set_source`.
        * ``None``: the current context is not multi-channel (ex: a mask),
          see :func:`~get_source` and :func:`~set_source`.

        For more details, see :ref:`fill_example`.

        :getter: Returns the source mode.
        """
    def get_source(self, channeltype: ChannelType | None = None) -> Source:
        """
        Get the source for the given channel type.

        :param channeltype: Must be None in mono channel context.
        :raises EditionContextException: If the `channeltype` is not valid in the current context.
                See :attr:`active_channels`.
        :raises RuntimeError: If the source is in :class:`SourceMode.Material <SourceMode>`.
                See :attr:`source_mode`.
        :returns: the source at channel type.
        """
    def set_source(self, channeltype: ChannelType | None, source: ResourceID | Color | layerstack.AnchorPointEffectNode) -> Source:  # type: ignore[name-defined]
        """
        Set the source for the given channel type.

        :param channeltype: Must be None in mono channel context.
        :param source: the source parameter.
        :raises EditionContextException: If the `channeltype` is not valid in the current context.
                See :attr:`active_channels`.
        :raises ValueError: If the `source` parameter is not valid.
        :returns: the source at channel type.
        """
    def reset_source(self, channeltype: ChannelType | None = None) -> None:
        """
        Reset the source at channel type.

        :param channeltype: Must be None in mono channel context.
        :raises EditionContextException: If the `channeltype` is not valid in the current context.
                See :attr:`active_channels`.
        """
    def get_material_source(self) -> SourceSubstance | SourceReference:
        """
        Get the source in material mode.

        :raises RuntimeError: If the source is not in :class:`SourceMode.Material <SourceMode>`.
                See :attr:`source_mode`.
        :raises EditionContextException: If the current context in not multi-channel.
        :returns: the source.
        """
    def set_material_source(self, source: ResourceID | layerstack.AnchorPointEffectNode) -> SourceSubstance | SourceReference:  # type: ignore[name-defined]
        """
        Set the source in material mode.

        :param source: the source parameter.
        :raises ValueError: If the `source` parameter is not valid.
        :raises EditionContextException: If the current context in not multi-channel.
        :returns: the source.
        """
    def reset_material_source(self) -> None:
        """
        Reset the source in material mode.

        :raises EditionContextException: If the current context in not multi-channel.
        """
    def set_sources_from_preset(self, preset: ResourceID) -> None:
        """
        Setup the fill with the given preset.

        :param preset: the resource preset.
        :raises ValueError: If `preset` is not a valid resource preset.
        """

class SourceUniformColor(ReadOnlyUid):
    """
    A class that represents an uniform color source.
    """
    def get_color(self) -> Color:
        """
        Get the uniform color of the source.

        :returns: The uniform color used by the source.
        """
    def set_color(self, color: Color) -> None:
        """
        Set the uniform color of the source.

        :param color: The desired uniform color.
        """

class SourceBitmap(ReadOnlyUid):
    """
    A class that represents a bitmap source.
    """
    @property
    def resource_id(self) -> ResourceID:
        """
        The current bitmap used by the source.

        :getter: Returns the resource identifier of the bitmap used by the source.
        """
    def get_color_space(self) -> ResourceColorSpace:
        """
        Return the color space of the bitmap.

        :returns: The current color space.

        See also:
            :ref:`colormanagement_colorspaces` section.
        """
    def set_color_space(self, color_space: ResourceColorSpace):
        """
        Override the default color space of the bitmap.

        :param color_space: The color space to set.
        :raises ValueError: If the given color space is not supported in the current context
            or by the current color management engine.

        See also:
            :ref:`colormanagement_colorspaces` section, :func:`list_available_color_spaces`.
        """
    def reset_color_space(self) -> None:
        """
        Remove any override color space and go back to the default one.
        """
    def list_available_color_spaces(self) -> list[ResourceColorSpace]:
        """
        Get the list of available color spaces for the bitmap.

        :returns: The list of available color spaces.

        See also:
            :ref:`colormanagement_colorspaces` section.
        """

@dataclasses.dataclass
class SourceFontParams(_ResolutionOverrideDeprecated):
    '''
    The source font parameters.

    :param text: The text to render.
    :param auto_size: Automatically adjust size to fit the render resolution.
    :param size: Manual size of the font, normalized and proportional to the resolution.
        Value must be positive.
    :param horizontal_alignment: The horizontal position of the text (left, center, right).
    :param vertical_alignment: The vertical position of the text (top, middle, bottom).
    :param color: The text color as RGB values. Values must be in range [0, 1].
    :param background_color: The RGB background color. Values must be in range [0, 1].
    :param background_opacity: The background opacity value. Value must be in range [0, 1].
    :param line_spacing: Distance between lines of text ("leading") relative to the font size.
    :param character_spacing: The amount of space between adjacent characters relative to
        the font size. Can be negative to subtract spacing.
    :param offset: Horizontal and vertical offset of the text. Normalized to the font size.
    :param resolution: Resolution parameters of the resource.
    :param resolution_mode: Deprecated since 0.3.4. Use ``mode`` attribute from **resolution**
        parameter instead.
    :type resolution_mode: FontResolutionMode
    :param resolution_value: Deprecated since 0.3.4. Use ``value`` attribute from **resolution**
        parameter instead.
    :type resolution_value: Tuple[int, int]
    '''
    text: str | None
    auto_size: bool
    size: float | None
    horizontal_alignment: HorizontalAlignment
    vertical_alignment: VerticalAlignment
    color: Color
    background_color: Color
    background_opacity: float | None
    line_spacing: float
    character_spacing: float
    offset: tuple[float, float]
    resolution: ResolutionOverride
    def __setattr__(self, __name: str, /, __value: dataclasses.Any) -> None: ...  # type: ignore[name-defined]

class SourceFont(ReadOnlyUid):
    """
    A class that represents a text source.
    """
    @property
    def resource_id(self) -> ResourceID:
        """
        The current font resource of the source.

        :getter: Returns the resource identifier of the font used by the source.
        """
    def get_parameters(self) -> SourceFontParams:
        """
        Get the source parameters.

        :returns: The source parameters.
        """
    def set_parameters(self, params: SourceFontParams) -> None:
        """
        Set the source parameters.

        :param params: The source parameters.
        :raises ValueError: If the parameters requirements are not met,
            see :class:`SourceFontParams`.
        """

@dataclasses.dataclass
class SourceVectorialParams(_ResolutionOverrideDeprecated):
    """
    The source vectorial parameters.

    :param artboard_id: The artboard id, for .ai file.
    :param scope: The root element of the hierarchy you want to import.
    :param resolution: Resolution parameters of the resource.
    :param resolution_mode: Deprecated since 0.3.4. Use ``mode`` attribute from **resolution**
        parameter instead.
    :type resolution_mode: ResolutionMode
    :param resolution_value: Deprecated since 0.3.4. Use ``value`` attribute from **resolution**
        parameter instead.
    :type resolution_value: Tuple[int, int]
    :param crop_area_mode: The crop area mode.
    :param crop_area_value: The crop area to use when `crop_area_mode` is `CropAreaMode.Manual`,
        formatted as [left corner x, left corner y, crop area width, crop area height].
        `width` and `height` values must be positive.
    :param fit_to_square: Force the crop area to be square.
    """
    artboard_id: str | None
    scope: str | None
    resolution: ResolutionOverride
    crop_area_mode: CropAreaMode
    crop_area_value: tuple[float, float, float, float]
    fit_to_square: bool = ...
    def __setattr__(self, __name: str, /, __value: dataclasses.Any) -> None: ...  # type: ignore[name-defined]

class SourceVectorial(ReadOnlyUid):
    """
    A class that represents a vectorial source.
    """
    @property
    def resource_id(self) -> ResourceID:
        """
        The current vectorial resource of the source.

        :getter: Returns the resource identifier of the vectorial used by the source.
        """
    def get_parameters(self) -> SourceVectorialParams:
        """
        Get the source parameters.

        :returns: The source parameters.
        """
    def set_parameters(self, params: SourceVectorialParams) -> None:
        """
        Set the source parameters.

        :param params: The source parameters.
        :raises ValueError: If the parameters requirements are not met,
            see :class:`SourceVectorialParams`.
        """

class OutputMappingIterator:
    """
    This class implements the iterator interface for class OutputMapping.

    :meta private:
    """
    keys: Incomplete
    iterator: Incomplete
    def __init__(self, uid) -> None: ...
    def __iter__(self): ...
    def __next__(self): ...

class OutputMapping(ReadOnlyUid):
    """
    This class gives access to the output mapping of a source procedural in a dict-like fashion.
    See :attr:`~substance_painter.source.SourceSubstance.output_mapping` property.

    Example:

    .. code-block:: python

        import substance_painter as sp
        mapping = a_substance_source.output_mapping
        mapping[sp.textureset.ChannelType.BaseColor] = sp.textureset.ChannelType.Specular
        for channel in mapping:
            print(mapping[channel])

    See also:
        For more technical informations, see the official `KeysView ABCs container
        <https://docs.python.org/3/library/collections.abc.html#collections.abc.KeysView>`_
        documentation as well as `__getitem__
        <https://docs.python.org/3/reference/datamodel.html#object.__getitem__>`_ and
        `__setitem__ <https://docs.python.org/3/reference/datamodel.html#object.__setitem__>`_
        methods.
    """
    def __getitem__(self, key: ChannelType) -> ChannelType: ...
    def __setitem__(self, key: ChannelType, value: str) -> None: ...
    def __len__(self) -> int: ...
    def __contains__(self, key: ChannelType) -> bool: ...
    def __iter__(self) -> OutputMappingIterator: ...

class SourceSubstance(ReadOnlyUid):
    """
    A class that represents a procedural source.
    """
    @property
    def resource_id(self) -> ResourceID:
        """
        The current substance resource of the source.

        :getter: Returns the resource of the source.
        """
    @property
    def output_mapping(self) -> OutputMapping:
        """
        The output mapping property in multiple output context.

        :getter: Returns the output mapping property.
        :setter: Sets the output mapping property.
        """
    @property
    def active_output(self) -> str:
        """
        The active output of the source in single output context.

        :getter: Returns the output identifier.
        :setter: Sets the output identifier.
        """
    @active_output.setter
    def active_output(self, identifier: str) -> None: ...
    @property
    def mask_output(self) -> str:
        """
        The mask output identifier of the source in multiple output context.

        :getter: Returns the mask output identifier.
        :setter: Sets the mask output identifier.
        """
    @mask_output.setter
    def mask_output(self, identifier: str) -> None: ...
    @property
    def image_inputs(self) -> list[str]:
        """
        The list of image inputs identifier from the current graph.

        :getter: Returns the list of image inputs identifier.

        See also:
            :class:`substance_painter.properties.Property`
        """
    @property
    def image_outputs(self) -> list[str]:
        """
        The list of image outputs identifier from the current graph.

        :getter: Returns the list of image outputs identifier.
        """
    def get_source(self, identifier: str) -> Source:
        """
        Get the source for the given input identifier.

        :param identifier: The input identifier.
        :returns: the source for the input.
        """
    def set_source(self, identifier: str, source: ResourceID | Color | layerstack.AnchorPointEffectNode) -> Source:  # type: ignore[name-defined]
        """
        Set the source for the given input identifier.

        :param identifier: The input identifier.
        :param source: The source parameter.
        :returns: The source for the input.
        """
    def reset_source(self, identifier: str) -> None:
        """
        Reset the source for the given input identifier.

        :param identifier: The input identifier.
        """
    def remove_source(self, identifier: str) -> None:
        """
        Remove the source for the given input identifier.

        :param identifier: The input identifier.
        """
    def get_parameters(self) -> dict[str, PropertyValue]:
        """
        Get source procedural parameters. For each property of the source,
        the resulting dictionnary holds an entry with the property name as key
        and the property value as value.

        :returns: The source procedural parameters.

        See also:
            :func:`substance_painter.source.SourceSubstance.get_properties`
        """
    def set_parameters(self, property_values: dict[str, PropertyValue]) -> None:
        """
        Set source procedural parameters.

        :param property_values: A dict of properties to be set with their corresponding values.

        Warning:
            Boolean parameters are treated as integer, if you use `True` or `False` you will get an
            error message:

            `>>> Bad value for property '<property_name>': expected value of type <int32> but got
            <bool>`
        """
    def get_properties(self) -> dict[str, Property]:
        """
        Get source procedural properties.

        :returns: The source procedural properties.

        See also:
            :class:`substance_painter.properties.Property`
        """
    def get_preset_list(self) -> list[str]:
        """
        Get the list of all available presets for this source.

        :returns: An array of all preset's names available.

        See also:
            :func:`substance_painter.source.SourceSubstance.apply_preset`
        """
    def apply_preset(self, name: str):
        """
        Apply a preset given its name. If no preset is found with this name nothing is done.

        :param name: The name of the preset to apply.

        See also:
            :func:`substance_painter.source.SourceSubstance.get_preset_list`
        """
    @property
    def resolution(self) -> ResolutionOverride:
        """
        The resolution parameters for this substance.

        :getter: Returns the resolution parameters.
        :setter: Sets the resolution parameters.
        :raises ValueError: if the source is used in a
            :class:`substance_painter.layerstack.FilterEffectNode`.
        """
    @resolution.setter
    def resolution(self, value): ...

class ChannelMappingIterator:
    """
    This class implements the iterator interface for class ChannelMapping.

    :meta private:
    """
    keys: Incomplete
    iterator: Incomplete
    def __init__(self, uid) -> None: ...
    def __iter__(self): ...
    def __next__(self): ...

class ChannelMapping(ReadOnlyUid):
    """
    This class gives access to the active channels of a source reference in a dict-like fashion.
    See :attr:`~substance_painter.source.SourceReference.channel_mapping` property.

    Example:

    .. code-block:: python

        import substance_painter as sp
        mapping = some_SourceReference_object.channel_mapping
        mapping[sp.textureset.ChannelType.BaseColor] = sp.textureset.ChannelType.Specular
        for channel in mapping:
            print(mapping[channel])

    See also:
        For more technical informations, see the official `KeysView ABCs container
        <https://docs.python.org/3/library/collections.abc.html#collections.abc.KeysView>`_
        documentation as well as `__getitem__
        <https://docs.python.org/3/reference/datamodel.html#object.__getitem__>`_ and
        `__setitem__ <https://docs.python.org/3/reference/datamodel.html#object.__setitem__>`_
        methods.
    """
    def __getitem__(self, key: ChannelType) -> ChannelType: ...
    def __setitem__(self, key: ChannelType, value: ChannelType) -> None: ...
    def __len__(self) -> int: ...
    def __contains__(self, key: ChannelType) -> bool: ...
    def __iter__(self) -> ChannelMappingIterator: ...

class SourceReference(ReadOnlyUid):
    """
    A class that represents an reference to an anchor point.
    """
    @property
    def channel_mapping(self) -> ChannelMapping:
        """
        The channels mapping property.

        :getter: Returns the channel mapping property.
        :raises EditionContextException: If the current context of the reference is not
                multi-channel.
        """
    @property
    def referenced_channel(self) -> ChannelType:
        """
        The referenced channel of the source.

        :getter: Returns the referenced channel of the source.
        :setter: Set the referenced channel of the source.
        :raises EditionContextException: If the current context of the reference is not
                single-channel or if the context of the target anchor point is not
                multi-channel.
        """
    @referenced_channel.setter
    def referenced_channel(self, channeltype: ChannelType) -> None: ...
    @property
    def anchor(self) -> layerstack.AnchorPointEffectNode:  # type: ignore[name-defined]
        """
        The anchor used by this source.

        :getter: Returns the anchor used by the source.
        """
    @property
    def alpha_matte(self) -> AlphaMatte:
        """
        The alpha matte used by this source.

        :getter: Returns the alpha matte of the source.
        :setter: Set the alpha matte of the source.
        """
    @alpha_matte.setter
    def alpha_matte(self, alpha_matte: AlphaMatte): ...
    def get_levels(self) -> LevelsParams:
        """
        Get the parameters used by the levels of this source.

        :returns: The parameters used by the levels of this source.
        """
    def set_levels(self, params: LevelsParams) -> None:
        """
        Set the parameters used by the levels of this source.

        :param params: The parameters used by the levels of this source.
        """
Source = SourceUniformColor | SourceBitmap | SourceVectorial | SourceSubstance | SourceReference | SourceFont
