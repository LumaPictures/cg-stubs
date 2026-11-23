import re
from collections.abc import Callable, Collection, Container, Iterable, Mapping, Sequence
from typing import Literal, Protocol, TypeAlias, TypeVar, overload

import hou
from PySide6 import QtGui
from typing_extensions import NotRequired, TypedDict
from statehud.baseconfig import AbstractConfig
from statehud.utils import ActionButtonManager, KeyState
from statehud.parmutils import _HUDParmValue
from statehud.window import WidgetBundleWindow

_T = TypeVar("_T")

class _TokenLabelItem(Protocol):
    def token(self) -> str: ...
    def label(self) -> str: ...

class _IconLabelItem(Protocol):
    def label(self) -> str: ...
    def icon(self) -> str | tuple[str, str]: ...

# A value bindParm() takes for a parm, as its bind*Parm() method for the parm's type does.
_HUDParmInput: TypeAlias = bool | int | float | str | Sequence[float] | None

class _MenuItem(TypedDict):
    token: str
    label: str
    icon: NotRequired[str]
    off_icon: NotRequired[str]

# A parm template, as hrecipes serializes one (rtypes.ParmTemplateData), with the type also as a
# WidgetParmType, and the HUD's own keys: a tooltip, the button strip's button tooltips and the
# float sliders' style settings.
class _HUDParmTemplate(TypedDict, total=False):
    type: "str | WidgetParmType"
    label: str
    label_hidden: bool
    num_components: int
    help: str
    tooltip: str
    hidden: bool
    joins_with_next: bool
    disable_when: str
    hide_when: str
    no_cook_when: str
    tags: dict[str, str]
    script_callback: str
    script_callback_language: str
    default_value: _HUDParmInput
    min_value: float
    max_value: float
    strict_min: bool
    strict_max: bool
    menu_items: list[_MenuItem]
    icon_names: str
    item_generator_script: str
    item_generator_script_language: str
    menu_type: str
    menu_use_token: bool
    column_labels: list[str]
    show_controls: bool
    color_type: str
    folder_names: str
    tab_group_end: bool
    tab_conditionals: str
    ordering_index: int
    parmtemplates: "dict[str, _HUDParmTemplate]"
    button_tooltips: list[str]
    decimals: int
    mouse_hotkeys: Mapping[tuple[int, int], str] | None
    hide_slider: bool
    keep_slider_space: bool
    slider_width: int | None
    create_widget_shadow: bool
    action_buttons: bool
    normal_key_color: QtGui.QColor | None
    selectable: bool

# The parm templates of a recipe: {"parmtemplates": {"parmtemplates": {name: template}}}.
class _HUDParmTemplateGroup(TypedDict, total=False):
    parmtemplates: dict[str, _HUDParmTemplate]

class _HUDParmTemplates(TypedDict, total=False):
    parmtemplates: _HUDParmTemplateGroup

# The style settings, for every parm type (the *_SETTING keys), and by parm type ("float",
# "toggle", "int", "menu", ...).
class _StyleSettingValues(TypedDict, total=False):
    use_label: bool
    slider_width: int | None
    hide_slider: bool
    keep_slider_space: bool
    mouse_hotkeys: Mapping[tuple[int, int], str] | None
    create_widget_shadow: bool
    action_buttons: bool
    normal_key_color: QtGui.QColor | None
    decimals: int
    use_front_label: bool
    selectable: bool

class _StyleSettings(_StyleSettingValues, total=False, extra_items=_StyleSettingValues):  # type: ignore[call-arg]
    pass

_StyleValue: TypeAlias = bool | int | QtGui.QColor | Mapping[tuple[int, int], str] | None

# The keywords getFloatStyleKwargs() gives bindFloatSlider(); "demicals" is SideFX's misspelling.
class _FloatStyleKwargs(TypedDict, closed=True):  # type: ignore[call-arg]
    demicals: int
    mouse_hotkeys: Mapping[tuple[int, int], str] | None
    hide_slider: bool
    keep_slider_space: bool
    value_width: int | None
    create_widget_shadow: bool
    action_buttons: bool
    normal_key_color: QtGui.QColor | None
    selectable: bool

class _InlineToggleKwargs(TypedDict, total=False, closed=True):  # type: ignore[call-arg]
    toggle_name: str
    toggle_callback: Callable[..., None] | None
    toggle_value: bool | None

class _ParmInfo(TypedDict):
    type: str
    tags: dict[str, str] | None

TOP_FOLDER: str


USE_LABEL_SETTING: Literal["use_label"]
HIDE_SLIDER_SETTING: Literal["hide_slider"]
EXPAND_VECTORS: Literal["hide_slider"]
KEEP_SLIDER_SPACE_SETTING: Literal["keep_slider_space"]
MOUSE_HOTKEYS_SETTING: Literal["mouse_hotkeys"]
DECIMAL_SETTING: Literal["decimals"]
USE_FRONT_LABEL: Literal["use_front_label"]
FIELD_WIDTH: Literal["slider_width"]
SELECTABLE_SETTING: Literal["selectable"]
SHADOW_SETTING: Literal["create_widget_shadow"]
ACTION_BUTTONS_SETTING: Literal["action_buttons"]
ACTION_KEY_SYMBOL: Literal["key"]
ACTION_RESET_SYMBOL: Literal["reset"]
NORMAL_KEY_COLOR_SETTING: Literal["normal_key_color"]

FLOAT_SLIDER_SETTINGS: _StyleSettingValues
TOGGLE_SETTINGS: _StyleSettingValues
STYLE_SETTINGS: _StyleSettings

def menuItems(d: Mapping[str, str]) -> list[dict[str, str]]: ...
def iconMenuItems(d: Mapping[str, str | tuple[str, str]]) -> list[dict[str, str]]: ...
def menuItemsFromEnum(enum: Iterable[_TokenLabelItem]) -> list[dict[str, str]]: ...
def iconMenuItemsFromEnum(enum: Iterable[_IconLabelItem]) -> list[dict[str, str]]: ...

class CondPair:
    name: str
    op: ParmConditionalOp
    val: str
    def __init__(self, parm_name: str, op: ParmConditionalOp, val: str) -> None: ...

class ConditionalInfo:
    cond_pairs: list[CondPair]
    def __init__(self) -> None: ...
    def addCond(self, cond_pair: CondPair) -> None: ...
    def eval(self, parms: Mapping[str, tuple[WidgetParmType, object]]) -> bool | None: ...

class ParmConditional:
    term_pattern: re.Pattern[str]
    cond_pair_pattern: re.Pattern[str]
    terms: list[ConditionalInfo]
    def __init__(self, cond_str: str) -> None: ...
    def eval(self, parms: Mapping[str, tuple[WidgetParmType, object]]) -> bool | None: ...

class ParmWidgetSet:
    TYPE_COMPONENTS: dict[str, str]
    hud_window: WidgetBundleWindow
    label_width: int
    prefix: str
    expand_vectors: bool
    callback: Callable[[str], object] | None
    action_button_callback: Callable[[str], object] | None
    slider_start_callback: Callable[[str], object] | None
    slider_end_callback: Callable[[str], object] | None
    active_slider_start_values: dict[str, _HUDParmValue]
    hotkey_callback: Callable[[str, str], object] | None
    parms: dict[str, _ParmInfo]
    menu_tokens: dict[str, list[str]]
    animatable_parms: list[str]
    style_settings: _StyleSettings
    _inline_toggle_kwargs: _InlineToggleKwargs
    parm_conds: dict[str, dict[ParmConditionType, ParmConditional]]
    @staticmethod
    def buildMenuFromList(items: Iterable[str]) -> list[dict[str, str]]: ...
    @staticmethod
    def buildMenuFromDict(d: Mapping[str, str]) -> list[dict[str, str]]: ...
    @staticmethod
    def getNumericProperties(parm_dict: _HUDParmTemplate) -> tuple[float, float, bool, bool]: ...
    def __init__(
        self,
        hud_window: WidgetBundleWindow,
        label_width: int,
        tab_widget: str,
        tab_name: str | None,
        *ignore: object,
        prefix: str = ...,
        folder_name: str | None = ...,
        folder_collapsible: bool = ...,
        folder_collapsed: bool = ...,
        folder_label: str | None = ...,
        callback: Callable[[str], object] | None = ...,
        expand_vectors: bool = ...,
        slider_start_callback: Callable[[str], object] | None = ...,
        slider_end_callback: Callable[[str], object] | None = ...,
        action_button_callback: Callable[[str], object] | None = ...,
        hotkey_callback: Callable[[str, str], object] | None = ...,
        disable_parm_conditionals: bool = ...,
    ) -> None: ...
    def __del__(self) -> None: ...
    def __getitem__(self, parm_name: str) -> _HUDParmValue: ...
    def __setitem__(self, parm_name: str, value: object) -> None: ...
    @property
    def tab_widget(self) -> str: ...
    @property
    def tab_name(self) -> str | None: ...
    def animatableParms(self) -> list[str]: ...
    def clear(self) -> None: ...
    def removeParm(self, name: str) -> None: ...
    @overload
    def setStyleSettings(self, settings: _StyleSettings, parm_type: None = ..., override: bool = ...) -> None: ...
    @overload
    def setStyleSettings(self, settings: _StyleSettingValues, parm_type: str, override: bool = ...) -> None: ...
    def setStyleSettings(
        self, settings: _StyleSettings | _StyleSettingValues, parm_type: str | None = ..., override: bool = ...
    ) -> None: ...
    @overload
    def getStyleSetting(
        self, key: Literal["use_label", "hide_slider", "keep_slider_space", "create_widget_shadow", "action_buttons", "use_front_label", "selectable"], default: _T, parm_type: str | None = ...
    ) -> bool | _T: ...
    @overload
    def getStyleSetting(
        self, key: Literal["use_label", "hide_slider", "keep_slider_space", "create_widget_shadow", "action_buttons", "use_front_label", "selectable"], default: None = ..., parm_type: str | None = ...
    ) -> bool | None: ...
    @overload
    def getStyleSetting(self, key: Literal["decimals"], default: _T, parm_type: str | None = ...) -> int | _T: ...
    @overload
    def getStyleSetting(self, key: Literal["decimals", "slider_width"], default: None = ..., parm_type: str | None = ...) -> int | None: ...
    @overload
    def getStyleSetting(self, key: Literal["slider_width"], default: _T, parm_type: str | None = ...) -> int | None | _T: ...
    @overload
    def getStyleSetting(
        self, key: Literal["mouse_hotkeys"], default: _T, parm_type: str | None = ...
    ) -> Mapping[tuple[int, int], str] | None | _T: ...
    @overload
    def getStyleSetting(
        self, key: Literal["mouse_hotkeys"], default: None = ..., parm_type: str | None = ...
    ) -> Mapping[tuple[int, int], str] | None: ...
    @overload
    def getStyleSetting(self, key: Literal["normal_key_color"], default: _T, parm_type: str | None = ...) -> QtGui.QColor | None | _T: ...
    @overload
    def getStyleSetting(
        self, key: Literal["normal_key_color"], default: None = ..., parm_type: str | None = ...
    ) -> QtGui.QColor | None: ...
    @overload
    def getStyleSetting(self, key: str, default: _T, parm_type: str | None = ...) -> _StyleValue | _T: ...
    @overload
    def getStyleSetting(self, key: str, default: None = ..., parm_type: str | None = ...) -> _StyleValue: ...
    def getStyleSetting(self, key: str, default: object = ..., parm_type: str | None = ...) -> object: ...
    def applyToValueFields(self, stylesheet: str) -> None: ...
    def applySliderStyleTemplate(self, template: str) -> None: ...
    def findParmInfo(self, parm_name: str) -> _ParmInfo | None: ...
    def isSliderActive(self, name: str) -> bool: ...
    def sliderStartValue(self, name: str) -> _HUDParmValue: ...
    def loadFromConfig(self, config: AbstractConfig, prefix: str = ..., trigger_callback: bool = ...) -> None: ...
    def loadParmFromConfig(self, config: AbstractConfig, name: str, prefix: str = ...) -> None: ...
    def saveToConfig(self, config: AbstractConfig, prefix: str = ...) -> None: ...
    def saveParmToConfig(self, config: AbstractConfig, name: str, prefix: str = ...) -> None: ...
    def getParms(self, menus_as_int: bool = ...) -> dict[str, _HUDParmValue]: ...
    def getParm(self, name: str, menus_as_int: bool = ...) -> _HUDParmValue: ...
    def getParmTags(self, name: str) -> dict[str, str] | None: ...
    def setParms(self, parms: Mapping[str, object]) -> None: ...
    def setParm(self, name: str, value: object, refresh_hide_disable: bool = ...) -> None: ...
    def bindParms(
        self,
        parms: _HUDParmTemplates | None,
        parm_values: Mapping[str, _HUDParmInput] | None = ...,
        pattern: str = ...,
        bind_parm_preprocess: Callable[[str, _HUDParmTemplate], _HUDParmTemplate] | None = ...,
    ) -> bool: ...
    def bindParmsFromDict(self, parm_defn: Mapping[str, _HUDParmTemplate], pattern: str = ...) -> None: ...
    def bindParmsWithFolders(
        self,
        parms: _HUDParmTemplates | None,
        parm_values: Mapping[str, _HUDParmInput] | None = ...,
        pattern: str = ...,
        bind_parm_preprocess: Callable[[str, _HUDParmTemplate], _HUDParmTemplate] | None = ...,
        whitelist: Collection[str] | None = ...,
    ) -> bool: ...
    def bindParm(
        self, name: str, value: _HUDParmInput, parm_dict: _HUDParmTemplate, refresh_hide_disable: bool = ...
    ) -> None: ...
    def getParmWidgetNames(self, name: str) -> list[str] | tuple[()]: ...
    def getWidgetNames(self) -> list[str]: ...
    def getUniversalProperties(
        self, name: str, parm_dict: _HUDParmTemplate, get_action_button: bool = ...
    ) -> tuple[str, str, str | None, ActionButtonManager | None]: ...
    def getActionButtonFromProperties(self, name: str, parm_dict: _HUDParmTemplate) -> ActionButtonManager | None: ...
    def addInlineToggle(self, name: str, value: bool | None, tags: dict[str, str] | None = ...) -> None: ...
    def getInlineToggle(self) -> _InlineToggleKwargs: ...
    def bindMenuParm(self, name: str, value: int | str | None, parm_dict: _HUDParmTemplate) -> None: ...
    def bindButtonStrip(self, name: str, value: int | None, parm_dict: _HUDParmTemplate) -> Literal[False] | None: ...
    def bindToggleParm(self, name: str, value: bool | None, parm_dict: _HUDParmTemplate) -> None: ...
    def bindIntParm(self, name: str, value: int | Sequence[int] | None, parm_dict: _HUDParmTemplate) -> None: ...
    def getFloatStyleKwargs(self, parm_dict: _HUDParmTemplate) -> _FloatStyleKwargs: ...
    def bindFloatParm(self, name: str, value: float | Sequence[float] | None, parm_dict: _HUDParmTemplate) -> None: ...
    def bindStringParm(self, name: str, value: str | None, parm_dict: _HUDParmTemplate) -> None: ...
    def bindLabel(self, name: str, parm_dict: _HUDParmTemplate) -> None: ...
    def bindButton(self, name: str, parm_dict: _HUDParmTemplate) -> None: ...
    def setParmColor(self, name: str, key_state: KeyState, comp: str | None = ...) -> None: ...
    def setParmColorNormal(self, name: str, comp: str | None = ...) -> None: ...
    def setParmColorPending(self, name: str, comp: str | None = ...) -> None: ...
    def setParmColorKey(self, name: str, comp: str | None = ...) -> None: ...
    def setParmColorHasKeys(self, name: str, comp: str | None = ...) -> None: ...
    def updateParmColorsFromChannelGeo(
        self,
        parm_map: Mapping[str, str],
        channel_geo: hou.Geometry,
        frame: float | None = ...,
        pending_channels: Container[str] | None = ...,
    ) -> None: ...
    def clearParmColors(self, parm_names: Iterable[str]) -> None: ...
