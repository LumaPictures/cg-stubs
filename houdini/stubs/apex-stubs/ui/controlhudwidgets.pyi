import _apex
import apex.stateparmutils as apu
import apex.ui.animationhudwidgets as apexhud
import apex.ui.apexparmdata as apexparms
import hou
import statehud.parmwidgetset as ws
from collections.abc import KeysView, Mapping, Sequence
from houtypes import ViewerStateKwargs, ViewerStatePlaybackChangeKwargs
from hutil.PySide.QtCore import Qt as Qt
from statehud.parmutils import _HUDParmValue
from statehud.utils import StepSizeButton
from statehud.window import WidgetBundleWindow
from typing import Protocol

class _AnimateState(apu._AnimateState, Protocol):
    """The members of the Animate viewer state (`viewer_states/apexanimate.py`) this module uses
    (it also hands the state to `apex.stateparmutils`)."""
    def handleControlCallback(self, control_path: str, event_type: str | None = ..., maintain_selection: bool = ...) -> bool: ...

VECTOR3_LABEL_MAP: dict[str, str]
FLOAT_SLIDER_SETTINGS: ws._StyleSettingValues
TOGGLE_SETTINGS: ws._StyleSettingValues

class ControlChannelWidget(apexhud.BaseHudWidget[_AnimateState, WidgetBundleWindow]):
    """
    The channel view for parameters of selected APEX controls
    """
    hud_window: WidgetBundleWindow
    mute_value_update: int
    control_parm_manager: apexparms.ControlParmdataManager | None
    control_parm_set: ws.ParmWidgetSet
    step_size_btn: StepSizeButton
    toolbar: apexhud.ToolbarWidget
    parm_limits: dict[str, list[float | hou.Vector3 | None]]
    default_parms: dict[str, _apex._PlainValue | None]
    shown_control: str | None
    in_multi_change: bool
    multi_change_parms: list[str]
    multi_change_edits: list[tuple[str, _HUDParmValue, bool]]
    DEFAULT_WIDTH: int
    LABEL_WIDTH: int
    MOUSE_OFFSET: int
    FIELD_WIDTH: int
    def __init__(self, state: _AnimateState, hud_window: WidgetBundleWindow | None = None, tab_widget_name: str | None = None, tab_name: str | None = None) -> None: ...
    def setupToolbar(self) -> None:
        """
        adds the standard toolbar for control parms to the control widget
        this allows the user to quickly snap controls, reset all parm values, copy parm values
        and paste parm values
        """
    def onExit(self, kwargs: ViewerStateKwargs) -> None: ...
    def onSelectionChanged(self) -> None: ...
    def updateControlParmList(self) -> None:
        """
        recreates the control parm list interface based on the current selected
        primary control. 
        """
    def onControlParmChangedEvent(self, name: str) -> bool: ...
    def onSliderStartEvent(self, name: str) -> None: ...
    def onSliderEndEvent(self, name: str) -> None: ...
    def onActionButtonEvent(self, name: str) -> None: ...
    def onHotkeyEvent(self, name: str, hk: str | None = None) -> bool:
        """Handles hotkeys for bound widgets."""
    def snap(self) -> bool:
        """snaps the selected controls to the current selected primary control"""
    def copyValues(self) -> None:
        """copies the current parm values of the control widget. We can then later re"""
    def selectedParms(self) -> list[str] | KeysView[str]: ...
    def pasteValues(self) -> None:
        """
        pastes the parm values that have been previously stored an applies them to the 
        current parameters
        """
    def resetValuesPressed(self, val: bool) -> None: ...
    def resetValues(self, names: Sequence[str] | None = None) -> None:
        """
        Reset parameter values back to their stored defaults.

        When `names` is given (or there is a slider selection) only those
        channels are reset. With no names and no slider selection, all the
        parms of each selected control are reset, including channels that
        aren't shown in the UI. The primary control of a multi-selection often
        hides some t/r/s components, but we still want the reset button to put
        every selected control back to their individual defaults.
        """
    def resetValue(self, name: str) -> None:
        """
        pastes the parm values that have been previously stored an applies them to the
        current parameters
        """
    def _updateFromControls(self) -> bool:
        """
        updates the parm list interfaces and the title and al
        all data about default parms, the latest parm values and the
        parm limits, and the channel widget tile get updated accordingly as well
        """
    def updateDefaultValues(self, ctrl_path: str | None) -> None:
        """
        collects the current default values of the parameters of the given control.
        For control groups, all subcontrols are assumed to share the rig of the
        group, so a single rig defaults lookup covers every key.
        """
    def clearKeyFrameHandlers(self) -> None:
        """
        removes the channel status feedback for all current parms
        """
    def bindKeyframeHandler(self, control: str | None) -> None:
        """
        adds channelprim feedback information about the status of the current channels
        of a given control - aka keyed, pending, no keys
        """
    def setTitleFromControl(self, control: str | None, multi_selection: bool = False, use_namespace: bool = False) -> str | None:
        """sets the title of the widget based on the name off the currently selected controls

        :param control: the name of the current control path
        :param multi_selection: defines if multi selections should be indicated or not, defaults to False
        :param use_namespace: defines if a namespace of the character name is to be attached 
        to the title, defaults to False
        :return: the generated title string
        """
    def valuesFromControl(self, control_path: str | None) -> None:
        """set the current widget parm values based on the current parm values of a given control"""
    def onParmChangedEvent(self, kwargs: Mapping[str, object]) -> bool | None: ...
    def onPlaybackChangeEvent(self, kwargs: ViewerStatePlaybackChangeKwargs) -> bool | None: ...
    def contextMenuCallback(self, action: str, slider_names: Sequence[str]) -> bool:
        """
        Callback for a context menu action on the given slider.
        """
    def selectedWidgetIndices(self) -> tuple[list[str] | KeysView[str], dict[str, list[int]]]: ...
    def setKeyframes(self, names: Sequence[str], remove_keys: bool = False) -> None:
        """ Set or remove keyframes on multiple channels. """
    def setKeyframe(self, name: str | None = None, remove_keys: bool = False) -> None:
        """ Set or remove keyframe on a single channel. """
    def removeAllKeysMulti(self, names: Sequence[str]) -> None:
        """ Removes all keys on multiple channels. """
    def removeAllKeys(self, name: str) -> None:
        """ Remove All Keys. """
    def onMultiParmValueChange(self, driver_name: str, begin: bool, names: Sequence[str] | None = None) -> None: ...
    def handleControlCallback(self, parm_name: str, control: str | None = None, event_type: str = 'enddrag', force: bool = False) -> None:
        """evecutes a  controlcallback from a given selected parm. 

        :param parm_name: name name of the parameter that we currently interact with. its important
        to take that into account in case of control groups. because only the callback of the curently used sub
        control should be kicking in
        :param event_type: the callback type to be triggered, defaults to 'enddrag'
        """
    def onParmValueChange(self, parm_name: str, value: _HUDParmValue | None = None, relative: bool = True) -> bool: ...
    def clampSlider(self, value: _HUDParmValue, name: str) -> _HUDParmValue:
        """clamps a given numerical slider values based on the current parm limit"""
    def updateParmLimits(self, ctrl_path: str | None) -> None:
        """updates the list of parameter limits based on the current specified control"""
    def setValues(self, name: str, values: _HUDParmValue, relative: bool = False) -> None:
        """
        applies the current channel values of a given parm to the animate state 
        and updates the channels accordingly
        """
