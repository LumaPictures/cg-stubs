import hou
from collections.abc import Callable, Sequence
from hutil.PySide import QtCore, QtGui, QtWidgets
from kinefx.mixer import _MixerItemType
from typing import ClassVar, Literal, Required, TypedDict

from typing import TypeAlias
from typing import TypeAlias
_BakeMode: TypeAlias = Literal['Bake to Stash SOP', 'Bake to Scene Animate SOP', 'Bake to Track', 'Bake to Override FX']
class _BakeCommandArgs(TypedDict, total=False):
    command: Required[Literal['getMixerNode', 'getBakeInfo', 'updateFramesFromMixer', 'bake', 'clear']]
    ret: Required[int]
    node: hou.SopNode | None
    info: str
    sel: Sequence[tuple[hou.OpNode | None, _MixerItemType, tuple[int, ...] | list[int]]]
    undo_msg: str
    log: str
    log_cb: Callable[[_BakeCommandArgs], object]
    end_cb: Callable[[_BakeCommandArgs], object]
    mode: _BakeMode
    stash_sop: str
    animate_sop: str
    bake_track: str
    bake_fx: str
    anim_path: str
    track_blend: bool
    keep_anim: bool
    keep_tracks: bool
    current_frame: bool
    start_frame: float
    end_frame: float
    step_frame: float

class BakeDialog(QtWidgets.QDialog):
    """ A dialog holding the Motion Mixer Bake Selection settings."""
    bake_callback: Callable[[_BakeCommandArgs], object]
    layout: QtWidgets.QVBoxLayout
    value_widgets: list[tuple[str, QtWidgets.QCheckBox | hou.qt.ComboBox | hou.qt.InputField]]
    show_log: QtWidgets.QCheckBox
    spacer_log: QtWidgets.QSpacerItem
    bottom_row: QtWidgets.QHBoxLayout
    keep_toggle: QtWidgets.QCheckBox
    bake_button: QtWidgets.QPushButton
    clear_button: QtWidgets.QPushButton
    close_button: QtWidgets.QPushButton
    info: QtWidgets.QLabel
    sep1: hou.qt.Separator
    sep2: hou.qt.Separator
    sep3: hou.qt.Separator
    mode: hou.qt.ComboBox
    stash_sop: hou.qt.InputField
    animate_sop: hou.qt.InputField
    bake_track: hou.qt.InputField
    bake_fx: hou.qt.InputField
    anim_path: hou.qt.InputField
    track_blend: QtWidgets.QCheckBox
    keep_anim: QtWidgets.QCheckBox
    keep_tracks: QtWidgets.QCheckBox
    current_frame: QtWidgets.QCheckBox
    start_frame: hou.qt.InputField
    end_frame: hou.qt.InputField
    step_frame: hou.qt.InputField
    update_frames: QtWidgets.QWidget
    mixer_but: QtWidgets.QPushButton
    playbar_but: QtWidgets.QPushButton
    global_but: QtWidgets.QPushButton
    log: QtWidgets.QTextEdit
    MODE_STASH_SOP: ClassVar[Literal['Bake to Stash SOP']]
    MODE_ANIMATE_SOP: ClassVar[Literal['Bake to Scene Animate SOP']]
    MODE_TRACK: ClassVar[Literal['Bake to Track']]
    MODE_FX: ClassVar[Literal['Bake to Override FX']]
    MODES: ClassVar[list[_BakeMode]]
    bake_info_tooltip: str
    mode_tooltip: str
    track_blend_tooltip: str
    anim_path_tooltip: str
    stash_sop_tooltip: str
    animate_sop_tooltip: str
    bake_track_tooltip: str
    keep_tracks_tooltip: str
    keep_anim_tooltip: str
    current_frame_tooltip: str
    start_frame_tooltip: str
    end_frame_tooltip: str
    mixer_but_tooltip: str
    playbar_but_tooltip: str
    global_but_tooltip: str
    def __init__(self, bake_cb: Callable[[_BakeCommandArgs], object], sel_changed_signal: QtCore.SignalInstance) -> None:
        """
            Construct a BakeDialog.
            Try not to do hard coupling with the mixerpane class so we use a
            callback and only the data members we need.
            @bake_cb is a bake command callback.
            @sel_changed_signal is signal to connect.
        """
    def onMixerSelectionChange(self) -> None:
        """ Select change callback to update the bake info label from the
            current selection.
        """
    def onSetStartFrameToCurrent(self) -> None:
        """Set Start To Current button callback"""
    def onSetEndFrameToCurrent(self) -> None:
        """Set End To Current button callback"""
    def updateFramesFromMixer(self) -> None:
        """ Button callback to update the start/end frames from the MotionMixer
            selection."""
    def updateFramesFromPlaybar(self) -> None:
        """ Button callback to update the start/end frames from the playbar"""
    def updateFramesFromGlobal(self) -> None:
        """ Button callback to update the start/end frames from the global
            range."""
    def onShowLogChanged(self, check: QtCore.Qt.CheckState) -> None:
        """ Update the parameter visibility based on show_log toggle"""
    def onCurrentFrameToggleChanged(self, check: QtCore.Qt.CheckState | None) -> None:
        """ Update the parameter visibility based on current frame"""
    def onModeChanged(self, index: int | None) -> None:
        """ Update the parameter visibility based on the mode value"""
    def onClose(self) -> None:
        """ Close button callback """
    def onClear(self) -> None:
        """ Clear button callback """
    def onBake(self) -> None:
        """ Bake button callback."""
    def bake(self, command: Literal['bake', 'clear']) -> None:
        """ Bake button callback."""
    def keyPressEvent(self, event: QtGui.QKeyEvent) -> None:
        """ Override the QDialog keyPressEvent to prevent the dialog from
            closing when pressing escape."""
