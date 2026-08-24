import _substance_painter.data_tweak
import dataclasses
import typing
from .colormanagement import Color as Color

PropertyValue = bool | int | tuple[int, int] | tuple[int, int, int] | tuple[int, int, int, int] | float | tuple[float, float] | tuple[float, float, float] | Color | tuple[Color, float] | tuple[float, float, float, float] | str

@dataclasses.dataclass(frozen=True)
class Property:
    """
    Read only access to a property data.
    """
    handle: _substance_painter.data_tweak.PythonTweak
    def value(self) -> PropertyValue:
        """
        Get the current property value.

        Returns:
            PropertyValue: the current value.
        """
    def name(self) -> str:
        """
        Get the property name.

        Returns:
            str: The property name.
        """
    def short_name(self) -> str:
        """
        Get the shortened property name.

        Returns:
            str: The property short name.
        """
    def label(self) -> str:
        """
        Get the property label.

        Returns:
            str: The property label.
        """
    def widget_type(self) -> str:
        """
        Get the widget type that should be used to edit the property.

        Returns:
            str: One of: 'Slider', 'Angle', 'Color', 'Togglebutton',
            'Combobox', 'RandomSeed', 'File', 'FileList', 'LineEdit',
            'Resource', 'TextEdit'.
        """
    def enum_values(self) -> dict[str, int]:
        """
        The possible enum values with corresponding text for 'Combobox'
        widget type.

        Returns:
            typing.Dict[str, int]: Enum label to enum value dictionary.
        """
    def enum_value(self, enum_label: str) -> int:
        """
        Get the enum value for the given enum label for 'Combobox'
        widget type.

        Args:
            enum_label (str): A valid enum label.

        Returns:
            typing.Dict[str, int]: The enum value for the corresponding label.
        """
    def properties(self) -> dict[str, typing.Any]:
        """
        Get a json object that describes all available meta properties of this
        property. For example: value range, editor step, possible values, tooltip, etc.

        Returns:
            typing.Dict[str, typing.Any]: A json object.
        """
