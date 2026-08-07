import dataclasses

@dataclasses.dataclass
class LevelsParamsRGB:
    """
    A levels parameters, when in RGB color mode.

    :param input_min: The minimum input threshold.
    :param input_max: The maximum input threshold.
    :param gamma: Gamma.
    :param output_min: The minimum output threshold.
    :param output_max: The maximum output threshold.
    :param clamp: Wether the values should be clamped or not.
    """
    input_min: tuple[float, float, float] = ...
    input_max: tuple[float, float, float] = ...
    gamma: tuple[float, float, float] = ...
    output_min: tuple[float, float, float] = ...
    output_max: tuple[float, float, float] = ...
    clamp: bool = ...

@dataclasses.dataclass
class LevelsParamsMono:
    """
    A levels parameters, when in Luminance or only one color mode.

    :param input_min: The minimum input threshold.
    :param input_max: The maximum input threshold.
    :param gamma: Gamma.
    :param output_min: The minimum output threshold.
    :param output_max: The maximum output threshold.
    :param clamp: Wether the values should be clamped or not.
    """
    input_min: float = ...
    input_max: float = ...
    gamma: float = ...
    output_min: float = ...
    output_max: float = ...
    clamp: bool = ...
LevelsParams = LevelsParamsMono | LevelsParamsRGB
