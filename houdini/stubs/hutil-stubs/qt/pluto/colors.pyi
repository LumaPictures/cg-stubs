import PySide6.QtCore
import PySide6.QtGui
import enum
import hou
from collections.abc import Iterator, Mapping
from contextlib import contextmanager
from hutil import oklch as oklch
from hutil.PySide import QtGui as QtGui, QtWidgets as QtWidgets
from hutil.PySide.QtCore import Qt as Qt
from hutil.qt.common import core as core
from hutil.qt.prefs import hcs as hcs
from typing import Callable, ClassVar, Self

from typing import TypeAlias
from typing import TypeAlias
_ThemeValue: TypeAlias = float | bool | PySide6.QtGui.QColor
BASE_BUTTON_ADJUST: int
BASE_FIELD_DELTA: int
PANE_EMPTY_BG_DELTA: int
PANE_DIVIDER_DELTA: int
STANDARD_TEXT_CONTRAST: int
SECONDARY_CHROMA_SCALE: float
NEUTRAL_CHROMA_SCALE: float
ICON_TINT_CHROMA_SCALE: float
ICON_ACCENT_CHROMA_SCALE: float
PROMINENT_ADJUST: int
DEFAULT_CUSTOM_ICON_ACCENT: str
PLATFORM_CONTRAST: float

def ensure(color: QtGui.QColor | str) -> QtGui.QColor: ...
def distance(h1: float, c1: float, t1: float, h2: float, c2: float, t2: float) -> float: ...
def similar(h1: float, c1: float, t1: float, h2: float, c2: float, t2: float, tolerance: float = 0.05) -> bool: ...
def separate(h1: float, c1: float, t1: float, h2: float, c2: float, t2: float, tone_delta: int = 8) -> tuple[float, float, float]: ...
def lerp(a: float, b: float, blend: float = 0.5) -> float: ...
def blend(c1: QtGui.QColor, c2: QtGui.QColor, pct: float = 0.5) -> QtGui.QColor: ...
def hslBlend(c1: QtGui.QColor, c2: QtGui.QColor, hue_blend: float = 1.0, sat_blend: float = 1.0, light_blend: float = 1.0) -> QtGui.QColor: ...
def qcolor_to_oklch(c: QtGui.QColor | str) -> oklch.OkLCH: ...
def qcolor_to_hct(c: QtGui.QColor | str) -> oklch.HCT: ...
def qcolor_to_lch_tuple(c: QtGui.QColor | str) -> tuple[float, float, float]: ...
def lch_to_qcolor(l: float, c: float, h: float) -> QtGui.QColor: ...
def oklch_to_qcolor(ok: oklch.OkLCH) -> QtGui.QColor: ...
def hct_color(hue: float, chroma: float, tone: float) -> QtGui.QColor: ...
def tone_fn(hue: float, chroma: float) -> Callable[[float], QtGui.QColor]: ...
def is_eq(a: object, b: object) -> bool: ...
def is_disliked(hue: float, chroma: float, tone: float) -> bool: ...
def likable(hue: float, chroma: float, tone: float) -> tuple[float, float, float]: ...

class Role(enum.Enum):
    bg = enum.auto()
    divider = enum.auto()
    paneDivider = enum.auto()
    paneTabEmptyBg = enum.auto()
    fg = enum.auto()
    prominentFg = enum.auto()
    label = enum.auto()
    fieldFg = enum.auto()
    dimFg = enum.auto()
    dimmerFg = enum.auto()
    field = enum.auto()
    fieldAlt = enum.auto()
    fieldButton = enum.auto()
    viewSurface = enum.auto()
    viewSurfaceAlt = enum.auto()
    surfaceHighest = enum.auto()
    surfaceHigher = enum.auto()
    surfaceHigh = enum.auto()
    surface = enum.auto()
    surfaceLow = enum.auto()
    surfaceLowest = enum.auto()
    tooltipSurface = enum.auto()
    tooltipFg = enum.auto()
    button = enum.auto()
    buttonHigh = enum.auto()
    buttonFg = enum.auto()
    pressed = enum.auto()
    pressedFg = enum.auto()
    uncheckedBase = enum.auto()
    checkedBase = enum.auto()
    checkedFg = enum.auto()
    checkedFull = enum.auto()
    checkedSurface = enum.auto()
    checkedSurfaceFg = enum.auto()
    primary = enum.auto()
    primaryFg = enum.auto()
    primarySurface = enum.auto()
    primarySurfaceFg = enum.auto()
    secondary = enum.auto()
    secondaryFg = enum.auto()
    secondarySurface = enum.auto()
    secondarySurfaceFg = enum.auto()
    header = enum.auto()
    headerAlt = enum.auto()
    paneTabBase = enum.auto()
    highlight = enum.auto()
    highlightFg = enum.auto()
    highlightSurface = enum.auto()
    highlightSurfaceFg = enum.auto()
    iconTint = enum.auto()
    iconAccent = enum.auto()

class NamedColor(enum.IntEnum):
    red = enum.auto()
    orange = enum.auto()
    amber = enum.auto()
    yellow = enum.auto()
    lime = enum.auto()
    green = enum.auto()
    emerald = enum.auto()
    teal = enum.auto()
    cyan = enum.auto()
    sky = enum.auto()
    blue = enum.auto()
    indigo = enum.auto()
    violet = enum.auto()
    purple = enum.auto()
    fuchsia = enum.auto()
    pink = enum.auto()
    rose = enum.auto()
    stone = enum.auto()
    gray = enum.auto()
    zinc = enum.auto()
    steel = enum.auto()
    slate = enum.auto()
    heather = enum.auto()
    success = enum.auto()
    warning = enum.auto()
    error = enum.auto()

class Subtype(enum.IntEnum):
    base = 0
    fg = 1
    surface = 2
    surfaceFg = 3

class AppTheme:
    app: PySide6.QtCore.QCoreApplication | None
    @staticmethod
    def isDark() -> bool: ...
    @staticmethod
    def namedColor(color: NamedColor | str, subtype: Subtype = ...) -> PySide6.QtGui.QColor: ...
    @staticmethod
    def hcsColor(name: str) -> QtGui.QColor: ...
    @staticmethod
    def bg() -> QtGui.QColor: ...
    @staticmethod
    def fg() -> QtGui.QColor: ...
    @staticmethod
    def prominentFg() -> QtGui.QColor: ...
    @staticmethod
    def divider() -> QtGui.QColor: ...
    @staticmethod
    def paneDivider() -> QtGui.QColor: ...
    @staticmethod
    def paneTabEmptyBg() -> QtGui.QColor: ...
    @staticmethod
    def fieldFg() -> QtGui.QColor: ...
    @staticmethod
    def dimFg() -> QtGui.QColor: ...
    @staticmethod
    def dimmerFg() -> QtGui.QColor: ...
    @staticmethod
    def label() -> QtGui.QColor: ...
    @staticmethod
    def field() -> QtGui.QColor: ...
    @staticmethod
    def fieldAlt() -> QtGui.QColor: ...
    @staticmethod
    def fieldButton() -> QtGui.QColor: ...
    @staticmethod
    def viewSurface() -> QtGui.QColor: ...
    @staticmethod
    def viewSurfaceAlt() -> QtGui.QColor: ...
    @staticmethod
    def surfaceHighest() -> QtGui.QColor: ...
    @staticmethod
    def surfaceHigher() -> QtGui.QColor: ...
    @staticmethod
    def surfaceHigh() -> QtGui.QColor: ...
    @staticmethod
    def surface() -> QtGui.QColor: ...
    @staticmethod
    def surfaceLow() -> QtGui.QColor: ...
    @staticmethod
    def surfaceLowest() -> QtGui.QColor: ...
    @staticmethod
    def tooltipSurface() -> QtGui.QColor: ...
    @staticmethod
    def tooltipFg() -> QtGui.QColor: ...
    @staticmethod
    def primaryButton() -> QtGui.QColor: ...
    @staticmethod
    def primaryButtonFg() -> QtGui.QColor: ...
    @staticmethod
    def button() -> QtGui.QColor: ...
    @staticmethod
    def buttonHigh() -> QtGui.QColor: ...
    @staticmethod
    def buttonFg() -> QtGui.QColor: ...
    @staticmethod
    def pressed() -> QtGui.QColor: ...
    @staticmethod
    def pressedFg() -> QtGui.QColor: ...
    @staticmethod
    def uncheckedBase() -> QtGui.QColor: ...
    @staticmethod
    def checkedBase() -> QtGui.QColor: ...
    @staticmethod
    def checkedFg() -> QtGui.QColor: ...
    @staticmethod
    def checkedFull() -> QtGui.QColor: ...
    @staticmethod
    def checkedSurface() -> QtGui.QColor: ...
    @staticmethod
    def checkedSurfaceFg() -> QtGui.QColor: ...
    @staticmethod
    def primary() -> QtGui.QColor: ...
    @staticmethod
    def primaryFg() -> QtGui.QColor: ...
    @staticmethod
    def primarySurface() -> QtGui.QColor: ...
    @staticmethod
    def primarySurfaceFg() -> QtGui.QColor: ...
    @staticmethod
    def secondary() -> QtGui.QColor: ...
    @staticmethod
    def secondaryFg() -> QtGui.QColor: ...
    @staticmethod
    def secondarySurface() -> QtGui.QColor: ...
    @staticmethod
    def header() -> QtGui.QColor: ...
    @staticmethod
    def headerAlt() -> QtGui.QColor: ...
    @staticmethod
    def paneTabBase() -> QtGui.QColor: ...
    @staticmethod
    def secondarySurfaceFg() -> QtGui.QColor: ...
    @staticmethod
    def highlight() -> QtGui.QColor: ...
    @staticmethod
    def highlightFg() -> QtGui.QColor: ...
    @staticmethod
    def highlightSurface() -> QtGui.QColor: ...
    @staticmethod
    def highlightSurfaceFg() -> QtGui.QColor: ...
    @staticmethod
    def iconTint() -> QtGui.QColor: ...
    @staticmethod
    def iconAccent() -> QtGui.QColor: ...
    @staticmethod
    def varyingValue() -> QtGui.QColor: ...
    @staticmethod
    def disabledAlpha() -> float: ...
    @staticmethod
    def paneTabFg() -> QtGui.QColor: ...
    @staticmethod
    def value() -> QtGui.QColor: ...
    @staticmethod
    def menuSurface() -> QtGui.QColor: ...

def applyItemViewPalette(view: QtWidgets.QAbstractItemView) -> None: ...
def refreshItemViewPalettes() -> None: ...
def setApplicationTheme(theme: Theme, redraw: bool = True) -> None: ...

dark_colors: dict[NamedColor, QtGui.QColor]
dark_lchs: dict[NamedColor, tuple[float, float, float]]
light_colors: dict[NamedColor, QtGui.QColor]
light_lchs: dict[NamedColor, tuple[float, float, float]]

def namedColor(is_dark: bool, nc: NamedColor, subtype: Subtype = ..., *, dark_tone: float | None = None) -> PySide6.QtGui.QColor: ...

theme_settings: dict[str, float | bool | PySide6.QtGui.QColor]

class Theme(core.Info):
    isDark: bool
    holo: bool
    globalContrast: float
    baseHue: float
    baseChroma: float
    baseTone: float
    primaryHue: float
    primaryChroma: float
    primaryTone: float
    highlightHue: float
    highlightChroma: float
    highlightTone: float
    secondaryChromaScale: float
    neutralChromaScale: float
    iconTintChromaScale: float
    iconAccentChromaScale: float
    contrast: float
    textAdjust: float
    textDeltaTolerance: float
    buttonAdjust: float
    fieldAdjust: float
    paneDividerAdjust: float
    uncheckedUseField: bool
    checkedUsePrimary: bool
    checkedInverted: bool
    tabsUsePrimary: bool
    iconsUsePrimary: bool
    customIconAccent: QtGui.QColor
    useCustomIconAccent: bool
    bg: QtGui.QColor
    divider: QtGui.QColor
    paneDivider: QtGui.QColor
    paneTabEmptyBg: QtGui.QColor
    fg: QtGui.QColor
    prominentFg: QtGui.QColor
    label: QtGui.QColor
    fieldFg: QtGui.QColor
    dimFg: QtGui.QColor
    dimmerFg: QtGui.QColor
    field: QtGui.QColor
    fieldAlt: QtGui.QColor
    fieldButton: QtGui.QColor
    viewSurface: QtGui.QColor
    viewSurfaceAlt: QtGui.QColor
    surfaceHighest: QtGui.QColor
    surfaceHigher: QtGui.QColor
    surfaceHigh: QtGui.QColor
    surface: QtGui.QColor
    surfaceLow: QtGui.QColor
    surfaceLowest: QtGui.QColor
    tooltipSurface: QtGui.QColor
    tooltipFg: QtGui.QColor
    button: QtGui.QColor
    buttonHigh: QtGui.QColor
    buttonFg: QtGui.QColor
    primary: QtGui.QColor
    originalPrimary: QtGui.QColor
    primaryFg: QtGui.QColor
    primarySurface: QtGui.QColor
    primarySurfaceFg: QtGui.QColor
    primaryButton: QtGui.QColor
    primaryButtonFg: QtGui.QColor
    secondary: QtGui.QColor
    secondaryFg: QtGui.QColor
    secondarySurface: QtGui.QColor
    secondarySurfaceFg: QtGui.QColor
    header: QtGui.QColor
    headerAlt: QtGui.QColor
    highlight: QtGui.QColor
    highlightFg: QtGui.QColor
    highlightSurface: QtGui.QColor
    highlightSurfaceFg: QtGui.QColor
    iconTint: QtGui.QColor
    iconAccent: QtGui.QColor
    uncheckedBase: QtGui.QColor
    checkedBase: QtGui.QColor
    checkedFg: QtGui.QColor
    checkedFull: QtGui.QColor
    checkedSurface: QtGui.QColor
    checkedSurfaceFg: QtGui.QColor
    error: QtGui.QColor
    errorFg: QtGui.QColor
    errorSurface: QtGui.QColor
    errorSurfaceFg: QtGui.QColor
    warning: QtGui.QColor
    warningFg: QtGui.QColor
    warningSurface: QtGui.QColor
    warningSurfaceFg: QtGui.QColor
    success: QtGui.QColor
    successFg: QtGui.QColor
    successSurface: QtGui.QColor
    successSurfaceFg: QtGui.QColor
    paneTabBase: QtGui.QColor
    varyingValue: QtGui.QColor
    value: QtGui.QColor
    menuSurface: QtGui.QColor
    pressed: QtGui.QColor
    pressedFg: QtGui.QColor
    red: QtGui.QColor
    orange: QtGui.QColor
    amber: QtGui.QColor
    yellow: QtGui.QColor
    lime: QtGui.QColor
    green: QtGui.QColor
    emerald: QtGui.QColor
    teal: QtGui.QColor
    cyan: QtGui.QColor
    sky: QtGui.QColor
    blue: QtGui.QColor
    indigo: QtGui.QColor
    violet: QtGui.QColor
    purple: QtGui.QColor
    fuchsia: QtGui.QColor
    pink: QtGui.QColor
    rose: QtGui.QColor
    stone: QtGui.QColor
    gray: QtGui.QColor
    zinc: QtGui.QColor
    steel: QtGui.QColor
    slate: QtGui.QColor
    heather: QtGui.QColor
    redFg: QtGui.QColor
    orangeFg: QtGui.QColor
    amberFg: QtGui.QColor
    yellowFg: QtGui.QColor
    limeFg: QtGui.QColor
    greenFg: QtGui.QColor
    emeraldFg: QtGui.QColor
    tealFg: QtGui.QColor
    cyanFg: QtGui.QColor
    skyFg: QtGui.QColor
    blueFg: QtGui.QColor
    indigoFg: QtGui.QColor
    violetFg: QtGui.QColor
    purpleFg: QtGui.QColor
    fuchsiaFg: QtGui.QColor
    pinkFg: QtGui.QColor
    roseFg: QtGui.QColor
    stoneFg: QtGui.QColor
    grayFg: QtGui.QColor
    zincFg: QtGui.QColor
    steelFg: QtGui.QColor
    slateFg: QtGui.QColor
    heatherFg: QtGui.QColor
    redSurface: QtGui.QColor
    orangeSurface: QtGui.QColor
    amberSurface: QtGui.QColor
    yellowSurface: QtGui.QColor
    limeSurface: QtGui.QColor
    greenSurface: QtGui.QColor
    emeraldSurface: QtGui.QColor
    tealSurface: QtGui.QColor
    cyanSurface: QtGui.QColor
    skySurface: QtGui.QColor
    blueSurface: QtGui.QColor
    indigoSurface: QtGui.QColor
    violetSurface: QtGui.QColor
    purpleSurface: QtGui.QColor
    fuchsiaSurface: QtGui.QColor
    pinkSurface: QtGui.QColor
    roseSurface: QtGui.QColor
    stoneSurface: QtGui.QColor
    graySurface: QtGui.QColor
    zincSurface: QtGui.QColor
    steelSurface: QtGui.QColor
    slateSurface: QtGui.QColor
    heatherSurface: QtGui.QColor
    redSurfaceFg: QtGui.QColor
    orangeSurfaceFg: QtGui.QColor
    amberSurfaceFg: QtGui.QColor
    yellowSurfaceFg: QtGui.QColor
    limeSurfaceFg: QtGui.QColor
    greenSurfaceFg: QtGui.QColor
    emeraldSurfaceFg: QtGui.QColor
    tealSurfaceFg: QtGui.QColor
    cyanSurfaceFg: QtGui.QColor
    skySurfaceFg: QtGui.QColor
    blueSurfaceFg: QtGui.QColor
    indigoSurfaceFg: QtGui.QColor
    violetSurfaceFg: QtGui.QColor
    purpleSurfaceFg: QtGui.QColor
    fuchsiaSurfaceFg: QtGui.QColor
    pinkSurfaceFg: QtGui.QColor
    roseSurfaceFg: QtGui.QColor
    stoneSurfaceFg: QtGui.QColor
    graySurfaceFg: QtGui.QColor
    zincSurfaceFg: QtGui.QColor
    steelSurfaceFg: QtGui.QColor
    slateSurfaceFg: QtGui.QColor
    heatherSurfaceFg: QtGui.QColor
    colorCycle: list[QtGui.QColor]
    nonRedColorCycle: list[QtGui.QColor]
    isDarkChanged: ClassVar[PySide6.QtCore.Signal]
    themeChanged: ClassVar[PySide6.QtCore.Signal]
    disabledAlphaChanged: ClassVar[PySide6.QtCore.Signal]
    def __init__(self, defer: bool = False, **kwargs: _ThemeValue) -> None: ...
    def effectiveContrast(self) -> float: ...
    def prepare(self) -> None: ...
    def copy(self) -> Theme: ...
    @contextmanager
    def updatePaused(self) -> Iterator[Self]: ...
    def asDict(self) -> dict[str, list[float] | str | float | bool]: ...
    def updateFrom(self, theme: Theme) -> None: ...
    def updateFromDict(self, d: Mapping[str, object]) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def dumpDiff(self, other: Theme) -> None: ...
    def setBaseHCT(self, hue: float, chroma: float, tone: float) -> None: ...
    def setPrimaryHCT(self, hue: float, chroma: float, tone: float) -> None: ...
    def setHighlightHCT(self, hue: float, chroma: float, tone: float) -> None: ...
    def setBaseColor(self, color: str | QtGui.QColor) -> None: ...
    def setBaseRGB(self, r: float, g: float, b: float) -> None: ...
    def setBaseHoudiniColor(self, hcolor: hou.Color) -> None: ...
    def setPrimaryColor(self, color: str | QtGui.QColor) -> None: ...
    def setPrimaryRGB(self, r: float, g: float, b: float) -> None: ...
    def setPrimaryHoudiniColor(self, hcolor: hou.Color) -> None: ...
    def setHighlightColor(self, color: str | QtGui.QColor) -> None: ...
    def setHighlightRGB(self, r: float, g: float, b: float) -> None: ...
    def setHighlightHoudiniColor(self, hcolor: hou.Color) -> None: ...
    def palette(self) -> QtGui.QPalette: ...
    def colorForRole(self, role: Role) -> QtGui.QColor: ...
    def getColor(self, color: NamedColor | str | PySide6.QtGui.QColor) -> PySide6.QtGui.QColor: ...
    def constrastingColor(self, hue: float, chroma: float, bg_tone: float, delta: float = ..., min_delta: float | None = None) -> PySide6.QtGui.QColor: ...
    def foregroundColor(self, bg_color: PySide6.QtGui.QColor, delta: float = ...) -> PySide6.QtGui.QColor: ...
    def setForceGray(self, force_gray: bool) -> None: ...
    def update(self) -> None: ...
    def editorHighlight(self, editor_bg: QtGui.QColor) -> QtGui.QColor: ...
    def computeToggleColors(self, hue: float, chroma: float, tone: float) -> tuple[QtGui.QColor, QtGui.QColor]: ...
    def computeTabColors(self, hue: float, chroma: float, tone: float) -> None: ...
    def disabledAlpha(self) -> float: ...
    @staticmethod
    def hctToColor(hue: float, chroma: float, tone: float) -> QtGui.QColor: ...
    @staticmethod
    def colorToHCT(color: QtGui.QColor) -> dict[str, float]: ...

defaults: dict[str, int | bool]

def defaultTheme(**kwargs: _ThemeValue) -> Theme: ...
def defaultHoloTheme() -> Theme: ...
def transp(c: QtGui.QColor, pct: float = 0.5) -> QtGui.QColor: ...
def stripes(color1: PySide6.QtGui.QColor, color2: PySide6.QtGui.QColor | PySide6.QtCore.Qt.GlobalColor = ..., width: float = 2.5, width2: float | None = None, flipped: bool = False) -> PySide6.QtGui.QLinearGradient: ...
def deltaFn(base_tone: float, contrast: float, maximum: float = 100.0, minimum: float = 0.0) -> Callable[[float], float]: ...
def contrastingTone(bg_tone: float, delta: float = 55.0, *, scale: float = 1.0, prefer_direction: int = 0, min_delta: float = 45.0) -> float: ...

class _Colors(core.Constants):
    slate050: QtGui.QColor
    slate100: QtGui.QColor
    slate150: QtGui.QColor
    slate200: QtGui.QColor
    slate250: QtGui.QColor
    slate300: QtGui.QColor
    slate350: QtGui.QColor
    slate400: QtGui.QColor
    slate450: QtGui.QColor
    slate500: QtGui.QColor
    slate550: QtGui.QColor
    slate600: QtGui.QColor
    slate650: QtGui.QColor
    slate700: QtGui.QColor
    slate750: QtGui.QColor
    slate800: QtGui.QColor
    slate850: QtGui.QColor
    slate900: QtGui.QColor
    slate950: QtGui.QColor
    steel050: QtGui.QColor
    steel100: QtGui.QColor
    steel150: QtGui.QColor
    steel200: QtGui.QColor
    steel250: QtGui.QColor
    steel300: QtGui.QColor
    steel350: QtGui.QColor
    steel400: QtGui.QColor
    steel450: QtGui.QColor
    steel500: QtGui.QColor
    steel550: QtGui.QColor
    steel600: QtGui.QColor
    steel650: QtGui.QColor
    steel700: QtGui.QColor
    steel750: QtGui.QColor
    steel800: QtGui.QColor
    steel850: QtGui.QColor
    steel900: QtGui.QColor
    steel950: QtGui.QColor
    zinc050: QtGui.QColor
    zinc100: QtGui.QColor
    zinc150: QtGui.QColor
    zinc200: QtGui.QColor
    zinc250: QtGui.QColor
    zinc300: QtGui.QColor
    zinc350: QtGui.QColor
    zinc400: QtGui.QColor
    zinc450: QtGui.QColor
    zinc500: QtGui.QColor
    zinc550: QtGui.QColor
    zinc600: QtGui.QColor
    zinc650: QtGui.QColor
    zinc700: QtGui.QColor
    zinc750: QtGui.QColor
    zinc800: QtGui.QColor
    zinc850: QtGui.QColor
    zinc900: QtGui.QColor
    zinc950: QtGui.QColor
    gray050: QtGui.QColor
    gray100: QtGui.QColor
    gray150: QtGui.QColor
    gray200: QtGui.QColor
    gray250: QtGui.QColor
    gray300: QtGui.QColor
    gray350: QtGui.QColor
    gray400: QtGui.QColor
    gray450: QtGui.QColor
    gray500: QtGui.QColor
    gray550: QtGui.QColor
    gray600: QtGui.QColor
    gray650: QtGui.QColor
    gray700: QtGui.QColor
    gray750: QtGui.QColor
    gray800: QtGui.QColor
    gray850: QtGui.QColor
    gray900: QtGui.QColor
    gray950: QtGui.QColor
    stone050: QtGui.QColor
    stone100: QtGui.QColor
    stone150: QtGui.QColor
    stone200: QtGui.QColor
    stone250: QtGui.QColor
    stone300: QtGui.QColor
    stone350: QtGui.QColor
    stone400: QtGui.QColor
    stone450: QtGui.QColor
    stone500: QtGui.QColor
    stone550: QtGui.QColor
    stone600: QtGui.QColor
    stone650: QtGui.QColor
    stone700: QtGui.QColor
    stone750: QtGui.QColor
    stone800: QtGui.QColor
    stone850: QtGui.QColor
    stone900: QtGui.QColor
    stone950: QtGui.QColor
    red050: QtGui.QColor
    red100: QtGui.QColor
    red150: QtGui.QColor
    red200: QtGui.QColor
    red250: QtGui.QColor
    red300: QtGui.QColor
    red350: QtGui.QColor
    red400: QtGui.QColor
    red450: QtGui.QColor
    red500: QtGui.QColor
    red550: QtGui.QColor
    red600: QtGui.QColor
    red650: QtGui.QColor
    red700: QtGui.QColor
    red750: QtGui.QColor
    red800: QtGui.QColor
    red850: QtGui.QColor
    red900: QtGui.QColor
    red950: QtGui.QColor
    orange050: QtGui.QColor
    orange100: QtGui.QColor
    orange150: QtGui.QColor
    orange200: QtGui.QColor
    orange250: QtGui.QColor
    orange300: QtGui.QColor
    orange350: QtGui.QColor
    orange400: QtGui.QColor
    orange450: QtGui.QColor
    orange500: QtGui.QColor
    orange550: QtGui.QColor
    orange600: QtGui.QColor
    orange650: QtGui.QColor
    orange700: QtGui.QColor
    orange750: QtGui.QColor
    orange800: QtGui.QColor
    orange850: QtGui.QColor
    orange900: QtGui.QColor
    orange950: QtGui.QColor
    amber050: QtGui.QColor
    amber100: QtGui.QColor
    amber150: QtGui.QColor
    amber200: QtGui.QColor
    amber250: QtGui.QColor
    amber300: QtGui.QColor
    amber350: QtGui.QColor
    amber400: QtGui.QColor
    amber450: QtGui.QColor
    amber500: QtGui.QColor
    amber550: QtGui.QColor
    amber600: QtGui.QColor
    amber650: QtGui.QColor
    amber700: QtGui.QColor
    amber750: QtGui.QColor
    amber800: QtGui.QColor
    amber850: QtGui.QColor
    amber900: QtGui.QColor
    amber950: QtGui.QColor
    yellow050: QtGui.QColor
    yellow100: QtGui.QColor
    yellow150: QtGui.QColor
    yellow200: QtGui.QColor
    yellow250: QtGui.QColor
    yellow300: QtGui.QColor
    yellow350: QtGui.QColor
    yellow400: QtGui.QColor
    yellow450: QtGui.QColor
    yellow500: QtGui.QColor
    yellow550: QtGui.QColor
    yellow600: QtGui.QColor
    yellow650: QtGui.QColor
    yellow700: QtGui.QColor
    yellow750: QtGui.QColor
    yellow800: QtGui.QColor
    yellow850: QtGui.QColor
    yellow900: QtGui.QColor
    yellow950: QtGui.QColor
    lime050: QtGui.QColor
    lime100: QtGui.QColor
    lime150: QtGui.QColor
    lime200: QtGui.QColor
    lime250: QtGui.QColor
    lime300: QtGui.QColor
    lime350: QtGui.QColor
    lime400: QtGui.QColor
    lime450: QtGui.QColor
    lime500: QtGui.QColor
    lime550: QtGui.QColor
    lime600: QtGui.QColor
    lime650: QtGui.QColor
    lime700: QtGui.QColor
    lime750: QtGui.QColor
    lime800: QtGui.QColor
    lime850: QtGui.QColor
    lime900: QtGui.QColor
    lime950: QtGui.QColor
    green050: QtGui.QColor
    green100: QtGui.QColor
    green150: QtGui.QColor
    green200: QtGui.QColor
    green250: QtGui.QColor
    green300: QtGui.QColor
    green350: QtGui.QColor
    green400: QtGui.QColor
    green450: QtGui.QColor
    green500: QtGui.QColor
    green550: QtGui.QColor
    green600: QtGui.QColor
    green650: QtGui.QColor
    green700: QtGui.QColor
    green750: QtGui.QColor
    green800: QtGui.QColor
    green850: QtGui.QColor
    green900: QtGui.QColor
    green950: QtGui.QColor
    emerald050: QtGui.QColor
    emerald100: QtGui.QColor
    emerald150: QtGui.QColor
    emerald200: QtGui.QColor
    emerald250: QtGui.QColor
    emerald300: QtGui.QColor
    emerald350: QtGui.QColor
    emerald400: QtGui.QColor
    emerald450: QtGui.QColor
    emerald500: QtGui.QColor
    emerald550: QtGui.QColor
    emerald600: QtGui.QColor
    emerald650: QtGui.QColor
    emerald700: QtGui.QColor
    emerald750: QtGui.QColor
    emerald800: QtGui.QColor
    emerald850: QtGui.QColor
    emerald900: QtGui.QColor
    emerald950: QtGui.QColor
    teal050: QtGui.QColor
    teal100: QtGui.QColor
    teal150: QtGui.QColor
    teal200: QtGui.QColor
    teal250: QtGui.QColor
    teal300: QtGui.QColor
    teal350: QtGui.QColor
    teal400: QtGui.QColor
    teal450: QtGui.QColor
    teal500: QtGui.QColor
    teal550: QtGui.QColor
    teal600: QtGui.QColor
    teal650: QtGui.QColor
    teal700: QtGui.QColor
    teal750: QtGui.QColor
    teal800: QtGui.QColor
    teal850: QtGui.QColor
    teal900: QtGui.QColor
    teal950: QtGui.QColor
    cyan050: QtGui.QColor
    cyan100: QtGui.QColor
    cyan150: QtGui.QColor
    cyan200: QtGui.QColor
    cyan250: QtGui.QColor
    cyan300: QtGui.QColor
    cyan350: QtGui.QColor
    cyan400: QtGui.QColor
    cyan450: QtGui.QColor
    cyan500: QtGui.QColor
    cyan550: QtGui.QColor
    cyan600: QtGui.QColor
    cyan650: QtGui.QColor
    cyan700: QtGui.QColor
    cyan750: QtGui.QColor
    cyan800: QtGui.QColor
    cyan850: QtGui.QColor
    cyan900: QtGui.QColor
    cyan950: QtGui.QColor
    sky050: QtGui.QColor
    sky100: QtGui.QColor
    sky150: QtGui.QColor
    sky200: QtGui.QColor
    sky250: QtGui.QColor
    sky300: QtGui.QColor
    sky350: QtGui.QColor
    sky400: QtGui.QColor
    sky450: QtGui.QColor
    sky500: QtGui.QColor
    sky550: QtGui.QColor
    sky600: QtGui.QColor
    sky650: QtGui.QColor
    sky700: QtGui.QColor
    sky750: QtGui.QColor
    sky800: QtGui.QColor
    sky850: QtGui.QColor
    sky900: QtGui.QColor
    sky950: QtGui.QColor
    blue050: QtGui.QColor
    blue100: QtGui.QColor
    blue150: QtGui.QColor
    blue200: QtGui.QColor
    blue250: QtGui.QColor
    blue300: QtGui.QColor
    blue350: QtGui.QColor
    blue400: QtGui.QColor
    blue450: QtGui.QColor
    blue500: QtGui.QColor
    blue550: QtGui.QColor
    blue600: QtGui.QColor
    blue650: QtGui.QColor
    blue700: QtGui.QColor
    blue750: QtGui.QColor
    blue800: QtGui.QColor
    blue850: QtGui.QColor
    blue900: QtGui.QColor
    blue950: QtGui.QColor
    indigo050: QtGui.QColor
    indigo100: QtGui.QColor
    indigo150: QtGui.QColor
    indigo200: QtGui.QColor
    indigo250: QtGui.QColor
    indigo300: QtGui.QColor
    indigo350: QtGui.QColor
    indigo400: QtGui.QColor
    indigo450: QtGui.QColor
    indigo500: QtGui.QColor
    indigo550: QtGui.QColor
    indigo600: QtGui.QColor
    indigo650: QtGui.QColor
    indigo700: QtGui.QColor
    indigo750: QtGui.QColor
    indigo800: QtGui.QColor
    indigo850: QtGui.QColor
    indigo900: QtGui.QColor
    indigo950: QtGui.QColor
    violet050: QtGui.QColor
    violet100: QtGui.QColor
    violet150: QtGui.QColor
    violet200: QtGui.QColor
    violet250: QtGui.QColor
    violet300: QtGui.QColor
    violet350: QtGui.QColor
    violet400: QtGui.QColor
    violet450: QtGui.QColor
    violet500: QtGui.QColor
    violet550: QtGui.QColor
    violet600: QtGui.QColor
    violet650: QtGui.QColor
    violet700: QtGui.QColor
    violet750: QtGui.QColor
    violet800: QtGui.QColor
    violet850: QtGui.QColor
    violet900: QtGui.QColor
    violet950: QtGui.QColor
    purple050: QtGui.QColor
    purple100: QtGui.QColor
    purple150: QtGui.QColor
    purple200: QtGui.QColor
    purple250: QtGui.QColor
    purple300: QtGui.QColor
    purple350: QtGui.QColor
    purple400: QtGui.QColor
    purple450: QtGui.QColor
    purple500: QtGui.QColor
    purple550: QtGui.QColor
    purple600: QtGui.QColor
    purple650: QtGui.QColor
    purple700: QtGui.QColor
    purple750: QtGui.QColor
    purple800: QtGui.QColor
    purple850: QtGui.QColor
    purple900: QtGui.QColor
    purple950: QtGui.QColor
    fuchsia050: QtGui.QColor
    fuchsia100: QtGui.QColor
    fuchsia150: QtGui.QColor
    fuchsia200: QtGui.QColor
    fuchsia250: QtGui.QColor
    fuchsia300: QtGui.QColor
    fuchsia350: QtGui.QColor
    fuchsia400: QtGui.QColor
    fuchsia450: QtGui.QColor
    fuchsia500: QtGui.QColor
    fuchsia550: QtGui.QColor
    fuchsia600: QtGui.QColor
    fuchsia650: QtGui.QColor
    fuchsia700: QtGui.QColor
    fuchsia750: QtGui.QColor
    fuchsia800: QtGui.QColor
    fuchsia850: QtGui.QColor
    fuchsia900: QtGui.QColor
    fuchsia950: QtGui.QColor
    pink050: QtGui.QColor
    pink100: QtGui.QColor
    pink150: QtGui.QColor
    pink200: QtGui.QColor
    pink250: QtGui.QColor
    pink300: QtGui.QColor
    pink350: QtGui.QColor
    pink400: QtGui.QColor
    pink450: QtGui.QColor
    pink500: QtGui.QColor
    pink550: QtGui.QColor
    pink600: QtGui.QColor
    pink650: QtGui.QColor
    pink700: QtGui.QColor
    pink750: QtGui.QColor
    pink800: QtGui.QColor
    pink850: QtGui.QColor
    pink900: QtGui.QColor
    pink950: QtGui.QColor
    rose050: QtGui.QColor
    rose100: QtGui.QColor
    rose150: QtGui.QColor
    rose200: QtGui.QColor
    rose250: QtGui.QColor
    rose300: QtGui.QColor
    rose350: QtGui.QColor
    rose400: QtGui.QColor
    rose450: QtGui.QColor
    rose500: QtGui.QColor
    rose550: QtGui.QColor
    rose600: QtGui.QColor
    rose650: QtGui.QColor
    rose700: QtGui.QColor
    rose750: QtGui.QColor
    rose800: QtGui.QColor
    rose850: QtGui.QColor
    rose900: QtGui.QColor
    rose950: QtGui.QColor

Colors: _Colors
color_cycle: tuple[QtGui.QColor, ...]
