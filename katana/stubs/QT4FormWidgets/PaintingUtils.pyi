# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import QT4FormWidgets
import QtGui
import QtWidgets
import ResourceFiles as ResourceFiles
from ResourceFiles.IconManager import ResourceManager as ResourceManager
from _typeshed import Incomplete

HIGHLIGHTSTYLE_ALWAYS: int
HIGHLIGHTSTYLE_NONE: int
HIGHLIGHTSTYLE_ROLLOVER: int
HIGHLIGHTSTYLE_TRANSPARENT: int
PALETTE_COLOR_ROLES_BEVEL: list
PALETTE_COLOR_ROLES_POLICY: list
PALETTE_COLOR_ROLES_READ_ONLY: list
STATE_BADGE_DEFAULT_SIZE: int
TOGGLE_STATE_BADGE_DEFAULT_SIZE: int
_DefaultPalette: None
_DefaultPaletteByWidgetType: dict
_FONT_FIXEDPITCH: int
_FONT_LABELBASE: int
_FONT_LABELBOLD: int
_FONT_LABELSECONDARY: int
_Fonts: dict
_PolicyPalettes: dict
_ReadOnlyPalette: None
_ScaledFonts: dict
__DisclosureTriangleBaseBrush: None
__DisclosureTriangleBasePen: None
__DisclosureTrianglePolys: dict
__Fonts: dict
__HIGHLIGHTSTYLE_FIRST: int
__HIGHLIGHTSTYLE_LAST: int

def ApplyPolicyPalette(policy: QT4FormWidgets.AbstractValuePolicy, widget: QtWidgets.QWidget, locked: Incomplete | None = ...): ...
def GetDefaultBoldLabelFont(): ...
def GetDefaultFixedPitchFont(): ...
def GetDefaultLabelFont(scale: Incomplete | None = ...): ...
def GetDefaultSecondaryLabelFont(): ...
def GetGroupLabelColor(palette: Incomplete | None = ...): ...
def GetHighlightColor(palette, on: bool = ..., active: bool = ...): ...
def GetPolicyPalette(policy: QT4FormWidgets.AbstractValuePolicy, locked: Incomplete | None = ...) -> QtGui.QPalette: ...
def GetReadOnlyPalette(locked: bool) -> QtGui.QPalette: ...
def GetStateBadgePixmap(letter, color, palette: Incomplete | None = ...): ...
def HighlightStyleValid(style): ...
def PaintBicolorRect(painter, rect, ulColor, lrColor): ...
def PaintCheckers(painter, rect, size: int = ..., lightValue: int = ..., darkValue: int = ...): ...
def PaintDisclosureTriangle(painter, _width, height, aspect, palette, rotation: Incomplete | None = ..., size: Incomplete | None = ..., outlineColor: Incomplete | None = ..., color: Incomplete | None = ..., hovered: bool = ...): ...
def PaintDragBar(painter, rect, multiplier: float = ...): ...
def PaintGroupCorner(painter, fullRect, color, sidebarWidth: int = ..., open: bool = ...): ...
def PaintGroupEnclosureSidebar(painter, fullRect, color, end: bool = ..., sidebarWidth: int = ...): ...
def PaintHighlightBar(painter, fullRect, color, roundTop: bool = ..., roundBottom: bool = ...): ...
def PaintQLineEditText(painter, option, flags, text, leftAlignUnderflow: bool = ...): ...
def PaintStateBadge(painter, width, height, letter, color, palette: Incomplete | None = ..., glow: bool = ..., textColor: Incomplete | None = ..., size: int = ...): ...
def PaintToggleStateBadge(painter, width, height, color, palette: Incomplete | None = ..., glow: bool = ..., size: int = ...): ...
def UpdateFontCache(font): ...
def _BuildFonts(baseFont: Incomplete | None = ..., forceUpdate: bool = ...): ...
def _MakePalettes(r, g, b): ...
def _RemoveBevelEffect(palette: QtGui.QPalette): ...
def _ScaleFont(baseFont, scale): ...