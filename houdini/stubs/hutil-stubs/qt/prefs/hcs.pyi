# Houdini stubs generated from Houdini 22.0.466

from . import utils as utils
from hutil import oklch as oklch
from hutil.PySide import QtCore as QtCore, QtGui as QtGui
from hutil.PySide.QtCore import Qt as Qt
from hutil.qt.pluto import colors as colors

REGISTRY: str
PROPERTY_PREFIX: str
PREF_PREFIX: str
DEFAULT_NETWORK_BG: QtGui.QColor
BLACK: QtGui.QColor
overrides: dict[str, str]
prefs: dict[str, str]
pref_pairs: tuple[tuple[str, str], ...]
anim_editor_bg_hcts: dict[str, oklch.HCT]
usd_view_colors: dict[str, tuple[str, bool]]

def override(app: QtCore.QCoreApplication, hcs_name: str, color: QtGui.QColor) -> None: ...
def getOverrideColor(app: QtCore.QCoreApplication, hcs_name: str) -> QtGui.QColor | None: ...
def overrideSimpleColors(app: QtCore.QCoreApplication) -> None: ...
def overrideNetworkBg(app: QtCore.QCoreApplication, theme: colors.Theme) -> None: ...
def overrideAnimEditorBg(app: QtCore.QCoreApplication, theme: colors.Theme) -> None: ...
def overrideSyntaxColors(app: QtCore.QCoreApplication, theme: colors.Theme) -> None: ...
def overrideUsdViewColors(app: QtCore.QCoreApplication, theme: colors.Theme) -> None: ...
def overrideFromPrefs(app: QtCore.QCoreApplication, theme: colors.Theme) -> None: ...
