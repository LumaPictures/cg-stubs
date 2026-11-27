COLORS: list[tuple[float, float, float]]

class ColorPicker:
    colors_max: int
    reference_color_palette: list[tuple[float, float, float]]
    color_palette: list[tuple[float, float, float]]
    index: int
    def __init__(self, color_palette: list[tuple[float, float, float]] | None = ...) -> None: ...
    def getColor(self) -> tuple[float, float, float]: ...
    def reset(self) -> None: ...
