import PySide6.QtGui
from hutil.PySide.QtCore import Qt as Qt
from hutil.PySide.QtGui import QBrush as QBrush, QColor as QColor, QPalette as QPalette

from typing import TypeAlias
from typing import TypeAlias
_ColorKey: TypeAlias = 'PySide6.QtGui.QColor | ColorSlot | str'
nord11: PySide6.QtGui.QColor
nord12: PySide6.QtGui.QColor
nord13: PySide6.QtGui.QColor
nord14: PySide6.QtGui.QColor
nord15: PySide6.QtGui.QColor
nord_red: PySide6.QtGui.QColor
nord_orange: PySide6.QtGui.QColor
nord_yellow: PySide6.QtGui.QColor
nord_green: PySide6.QtGui.QColor
nord_purple: PySide6.QtGui.QColor
blue_light: PySide6.QtGui.QColor
green_light: PySide6.QtGui.QColor
indigo_light: PySide6.QtGui.QColor
orange_light: PySide6.QtGui.QColor
magenta_light: PySide6.QtGui.QColor
purple_light: PySide6.QtGui.QColor
red_light: PySide6.QtGui.QColor
cyan_light: PySide6.QtGui.QColor
yellow_light: PySide6.QtGui.QColor
kiwi_light: PySide6.QtGui.QColor
peach_light: PySide6.QtGui.QColor
pink_light: PySide6.QtGui.QColor
steel_light: PySide6.QtGui.QColor
tan_light: PySide6.QtGui.QColor
mint_light: PySide6.QtGui.QColor
grey_light: PySide6.QtGui.QColor
blue_dark: PySide6.QtGui.QColor
green_dark: PySide6.QtGui.QColor
indigo_dark: PySide6.QtGui.QColor
orange_dark: PySide6.QtGui.QColor
magenta_dark: PySide6.QtGui.QColor
purple_dark: PySide6.QtGui.QColor
red_dark: PySide6.QtGui.QColor
cyan_dark: PySide6.QtGui.QColor
yellow_dark: PySide6.QtGui.QColor
kiwi_dark: PySide6.QtGui.QColor
peach_dark: PySide6.QtGui.QColor
pink_dark: PySide6.QtGui.QColor
steel_dark: PySide6.QtGui.QColor
tan_dark: PySide6.QtGui.QColor
mint_dark: PySide6.QtGui.QColor
grey_dark: PySide6.QtGui.QColor
chart_cycle_light: tuple[PySide6.QtGui.QColor, ...]
chart_cycle_dark: tuple[PySide6.QtGui.QColor, ...]

class ColorSlot:
    name: str
    def __init__(self, name: str) -> None: ...
    def __hash__(self) -> int: ...

Blue: ColorSlot
Green: ColorSlot
Indigo: ColorSlot
Orange: ColorSlot
Magenta: ColorSlot
Purple: ColorSlot
Red: ColorSlot
Cyan: ColorSlot
Yellow: ColorSlot
Kiwi: ColorSlot
Peach: ColorSlot
Pink: ColorSlot
Steel: ColorSlot
Tan: ColorSlot
Mint: ColorSlot
Gray: ColorSlot
SuccessBackground: ColorSlot
SuccessText: ColorSlot
WarningBackground: ColorSlot
WarningText: ColorSlot
ErrorBackground: ColorSlot
ErrorText: ColorSlot

def blend(c1: PySide6.QtGui.QColor, c2: PySide6.QtGui.QColor, pct: float = 0.5) -> PySide6.QtGui.QColor: ...
def complement(c: PySide6.QtGui.QColor, angle: float = 180.0) -> PySide6.QtGui.QColor: ...
def tint(c1: PySide6.QtGui.QColor, c2: PySide6.QtGui.QColor, pct: float = 1.0) -> PySide6.QtGui.QColor: ...
def transp(c: PySide6.QtGui.QColor, pct: float = 0.5) -> PySide6.QtGui.QColor: ...
def stripes(color1: PySide6.QtGui.QColor, color2: PySide6.QtGui.QColor = ..., width: float = 2.5, width2: float | None = None) -> PySide6.QtGui.QLinearGradient: ...
def success_brush(color1: PySide6.QtGui.QColor = ..., color2: PySide6.QtGui.QColor = ...) -> PySide6.QtGui.QBrush: ...
def warning_brush(color1: PySide6.QtGui.QColor = ..., color2: PySide6.QtGui.QColor = ...) -> PySide6.QtGui.QBrush: ...
def error_brush(color1: PySide6.QtGui.QColor = ..., color2: PySide6.QtGui.QColor = ...) -> PySide6.QtGui.QBrush: ...

class ColorSet:
    name: str
    colors: dict[str, PySide6.QtGui.QColor]
    def __init__(self, name: str, **colors: PySide6.QtGui.QColor) -> None: ...
    def color(self, key: _ColorKey) -> PySide6.QtGui.QColor: ...
    def __getattr__(self, key: str) -> PySide6.QtGui.QColor: ...

light_colors: ColorSet
dark_colors: ColorSet

def get_color(palette: PySide6.QtGui.QPalette, key: _ColorKey) -> PySide6.QtGui.QColor: ...
def get_color_cycle(palette: PySide6.QtGui.QPalette) -> tuple[PySide6.QtGui.QColor, ...]: ...
def make_palette(background: PySide6.QtGui.QColor, text: _ColorKey, accent: PySide6.QtGui.QColor, tint: float = 0.0) -> PySide6.QtGui.QPalette: ...
def blue_mint_palette(accent: PySide6.QtGui.QColor, tint: float = 0.0) -> PySide6.QtGui.QPalette: ...
def gentle_palette(accent: PySide6.QtGui.QColor, tint: float = 0.0) -> PySide6.QtGui.QPalette: ...
def charcoal_palette(accent: PySide6.QtGui.QColor, tint: float = 0.0) -> PySide6.QtGui.QPalette: ...
def black_palette(accent: PySide6.QtGui.QColor, tint: float = 0.0) -> PySide6.QtGui.QPalette: ...
def silver_palette(accent: PySide6.QtGui.QColor, tint: float = 0.0) -> PySide6.QtGui.QPalette: ...
def white_palette(accent: PySide6.QtGui.QColor, tint: float = 0.0) -> PySide6.QtGui.QPalette: ...

nord00: PySide6.QtGui.QColor
nord01: PySide6.QtGui.QColor
nord02: PySide6.QtGui.QColor
nord03: PySide6.QtGui.QColor
nord04: PySide6.QtGui.QColor
nord05: PySide6.QtGui.QColor
nord06: PySide6.QtGui.QColor
nord07: PySide6.QtGui.QColor
nord08: PySide6.QtGui.QColor
nord09: PySide6.QtGui.QColor
nord10: PySide6.QtGui.QColor
dracula_window: PySide6.QtGui.QColor
dracula_lighter: PySide6.QtGui.QColor
dracula_windowtext: PySide6.QtGui.QColor
dracula_placeholder: PySide6.QtGui.QColor
dracula_cyan: PySide6.QtGui.QColor
dracula_green: PySide6.QtGui.QColor
dracula_orange: PySide6.QtGui.QColor
dracula_pink: PySide6.QtGui.QColor
dracula_purple: PySide6.QtGui.QColor
dracula_red: PySide6.QtGui.QColor
dracula_yellow: PySide6.QtGui.QColor
