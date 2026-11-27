from collections.abc import Callable, Sequence
from typing import ClassVar, Literal, Required, TypeAlias, TypedDict

import hou
from kinefx.mixer import _MixerItemType
from PySide6 import QtCore, QtGui, QtWidgets

_BakeMode: TypeAlias = Literal[
    "Bake to Stash SOP", "Bake to Scene Animate SOP", "Bake to Track", "Bake to Override FX"
]

# The dictionary the dialog passes its bake callback (the mixer pane's onBakeCommand) to run a
# command; the pane writes ret and the command's results (node, info/sel, start/end_frame, log)
# back into it. bake and clear also get the dialog's widget values, by widget name.
class _BakeCommandArgs(TypedDict, total=False):
    command: Required[Literal["getMixerNode", "getBakeInfo", "updateFramesFromMixer", "bake", "clear"]]
    ret: Required[int]
    node: hou.SopNode | None
    info: str
    # (parm node, item type, ids) of the selected mixer items to bake; onBake() bakes tracks one
    # by one with a list of one track id.
    sel: Sequence[tuple[hou.OpNode | None, _MixerItemType, tuple[int, ...] | list[int]]]
    undo_msg: str
    log: str
    log_cb: Callable[["_BakeCommandArgs"], object]
    end_cb: Callable[["_BakeCommandArgs"], object]
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
    MODE_STASH_SOP: ClassVar[Literal["Bake to Stash SOP"]]
    MODE_ANIMATE_SOP: ClassVar[Literal["Bake to Scene Animate SOP"]]
    MODE_TRACK: ClassVar[Literal["Bake to Track"]]
    MODE_FX: ClassVar[Literal["Bake to Override FX"]]
    MODES: ClassVar[list[_BakeMode]]
    bake_callback: Callable[[_BakeCommandArgs], object]
    layout: QtWidgets.QVBoxLayout
    # (name of the attribute holding the widget, widget) of the widgets whose values bake() sends.
    value_widgets: list[tuple[str, QtWidgets.QCheckBox | hou.qt.ComboBox | hou.qt.InputField]]
    show_log: QtWidgets.QCheckBox
    spacer_log: QtWidgets.QSpacerItem
    bottom_row: QtWidgets.QHBoxLayout
    keep_toggle: QtWidgets.QCheckBox
    bake_button: QtWidgets.QPushButton
    clear_button: QtWidgets.QPushButton
    close_button: QtWidgets.QPushButton
    # The widgets __init__ sets by name.
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
    def __init__(self, bake_cb: Callable[[_BakeCommandArgs], object], sel_changed_signal: QtCore.SignalInstance) -> None: ...
    def onShowLogChanged(self, check: QtCore.Qt.CheckState) -> None: ...
    def onCurrentFrameToggleChanged(self, check: QtCore.Qt.CheckState | None) -> None: ...
    def onModeChanged(self, index: int | None) -> None: ...
    def bake(self, command: Literal["bake", "clear"]) -> None: ...
    def keyPressEvent(self, event: QtGui.QKeyEvent) -> None: ...
