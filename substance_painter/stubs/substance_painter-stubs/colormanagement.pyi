from enum import Enum

class GenericColorSpace(Enum):
    """
    Generic color spaces valid with any color space engine used.

    Can be used for :class:`Color.color_space <Color>` or resources.

    Members:

    ================= ===========================
    Name              Description
    ================= ===========================
    ``sRGB``          sRGB color space (IEC 61966-2-1:1999 in legacy mode)
    ``Working``       working space used in the current project (Linear sRGB in legacy mode).
    ``Raw``           Raw (no color space conversion).
    ================= ===========================
    """
    sRGB = ...
    Working = ...
    Raw = ...

class LegacyColorSpace(Enum):
    """
    Legacy color spaces.

    Don't use them to override your resource's color spaces, use
    :class:`GenericColorSpace.Working <GenericColorSpace>` or
    :class:`GenericColorSpace.sRGB <GenericColorSpace>` instead.

    Can be used for resources only. Can't be used for :class:`Color.color_space <Color>`.

    Members:

    ================= ===========================
    Name              Description
    ================= ===========================
    ``Linear``        Linear sRGB color space.
    ``sRGB``          sRGB color space (IEC 61966-2-1:1999).
    ================= ===========================
    """
    Linear = ...
    sRGB = ...

class DataColorSpace(Enum):
    """
    Data color spaces.

    Color spaces used for not color managed channels such as metallic or height.

    Can be used for resources only. Can't be used for :class:`Color.color_space <Color>`.

    Members:

    ================= ===========================
    Name              Description
    ================= ===========================
    ``Data``          Data values, unsigned normalized or float.
    ``DataSigned``    Signed -1..1 data values stored as 0..1 normalized values.
    ================= ===========================
    """
    Data = ...
    DataSigned = ...

class NormalColorSpace(Enum):
    """
    Normal color spaces.

    Color spaces used for normal channels to specify how to interpret normal data.

    Can be used for resources only. Can't be used for :class:`Color.color_space <Color>`.

    Members:

    ================== ===========================
    Name               Description
    ================== ===========================
    ``NormalXYZRight`` Normal map in OpenGL format.
    ``NormalXYZLeft``  Normal map in Direct3D format.
    ================== ===========================
    """
    NormalXYZRight = ...
    NormalXYZLeft = ...
ColorColorSpace = GenericColorSpace | str
ResourceColorSpace = GenericColorSpace | LegacyColorSpace | DataColorSpace | NormalColorSpace | str

class Color:
    """
    Describe a color (with a color space).

    If you are not confortable with color spaces, you can create a color without
    specifying the colorspace of the data. In this case the color space will be
    deduced depending on the context where this color is used
    (:class:`GenericColorSpace.sRGB <GenericColorSpace>` when used on a color managed
    channel, :class:`GenericColorSpace.Raw <GenericColorSpace>` otherwise).

    On color managed channel, we assume sRGB because it is the most common
    color space used for computer screens, this is why many color pickers will give you
    sRGB data. sRGB is also the standard color space for the web, so a lot of color
    data you can get from the web will be sRGB encoded.

    *A color object returned by the different accessor of our API will always have a
    defined colorspace.*

    :ivar value_raw: raw r,g,b data encoded in `color_space`.
    :vartype value_raw: Tuple[float, float, float]
    :ivar color_space: Color space in which `value_raw`
        is encoded. If None, will be deduced depending on the context where this color
        is used (:class:`GenericColorSpace.sRGB <GenericColorSpace>` when used on
        a color managed channel, :class:`GenericColorSpace.Raw <GenericColorSpace>`
        otherwise).
    :vartype color_space: GenericColorSpace | str
    :param r: Red component
    :param g: Green component
    :param b: Blue component
    :param color_space: Color space in which the data are encoded.
        If not specified, it will be deduced depending on the context where the color
        is used (:class:`GenericColorSpace.sRGB <GenericColorSpace>` when used on
        a color managed channel, :class:`GenericColorSpace.Raw <GenericColorSpace>`
        otherwise) (default: None).
    """
    value_raw: tuple[float, float, float]
    color_space: ColorColorSpace
    def __init__(self, r: float, g: float, b: float, color_space: ColorColorSpace = None) -> None:  # type: ignore[assignment]
        """
        Color constructor
        """
    def convert(self, color_space: ColorColorSpace) -> tuple[float, float, float]:
        """
        Get r,g,b values encoded in the given color space

        Args:
            color_space: Color space in which you want the data encoded to.

        Returns:
            Tuple[float, float, float]: r,g,b data encoded in the given color space

        Raises:
            RuntimeError: if :class:`Color.color_space <Color>` is None
        """
    @property
    def value(self) -> tuple[float, float, float]:
        """
        color value

        :getter: Returns the color encoded in sRGB if :class:`Color.color_space <Color>`
            is defined and not :class:`GenericColorSpace.Raw <GenericColorSpace>`,
            otherwise return :class:`Color.value_raw <Color>`.
        :type: Tuple[float, float, float]
        """
    @property
    def sRGB(self) -> tuple[float, float, float]:
        """
        color value in sRGB space

        :getter: Returns the color value encoded in sRGB
        :setter: Set the color value as sRGB encoded value
        :type: Tuple[float, float, float]
        :Raises: RuntimeError: if :class:`Color.color_space <Color>` is None
        """
    @sRGB.setter
    def sRGB(self, value: tuple[float, float, float]) -> None: ...
    @property
    def working(self) -> tuple[float, float, float]:
        """
        color value in working space

        :getter: Returns the color value encoded in working space
        :setter: Set the color value as working space encoded value
        :type: Tuple[float, float, float]
        :Raises: RuntimeError: if :class:`Color.color_space <Color>` is None
        """
    @working.setter
    def working(self, value: tuple[float, float, float]) -> None: ...
