COLORS: list[tuple[float, float, float]]

class ColorPicker:
    reference_color_palette: list[tuple[float, float, float]]
    color_palette: list[tuple[float, float, float]]
    index: int
    colors_max: int
    def __init__(self, color_palette: list[tuple[float, float, float]] | None = None) -> None: ...
    def getColor(self) -> tuple[float, float, float]: ...
    def reset(self) -> None: ...
