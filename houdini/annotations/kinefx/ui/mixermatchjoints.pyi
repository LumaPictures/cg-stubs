from collections.abc import Callable, Sequence
from typing import Literal, Protocol, Required, TypedDict

import hou
from PySide6 import QtWidgets

# What the dialog passes its match callback (MixerPaneActions.onMatchJoints), which sets "ret",
# "errors" and, after a match, the matched "t"/"r"/"s"/"p"/"pr".
class _MatchJointsKwargs(TypedDict, total=False):
    match_name: Required[str]
    match_char: Required[str]
    undo_msg: Required[str]
    ret: Required[int]
    apply_transform: Required[Literal[0, 1]]
    t: Sequence[float] | hou.Vector3
    r: Sequence[float] | hou.Vector3
    s: Sequence[float] | hou.Vector3
    p: Sequence[float] | hou.Vector3
    pr: Sequence[float] | hou.Vector3
    match_pos: bool
    match_ori: bool
    only_rotate_around_y: bool
    match_using_current_frame: bool
    match_previous_track: bool
    errors: list[str]

# What the dialog passes its select callback (MixerPaneActions.onSelectJoints), which adds "node",
# "message" and "title" to make it the options of jointselection.selectMotionMixerJoint().
class _SelectJointsKwargs(TypedDict, total=False):
    node: hou.OpNode
    message: str
    title: str
    parmtuple: hou.ParmTuple | None
    add_prefix: bool
    use_path_attr: bool
    fxgroup: bool
    characters: str
    joints: str
    set_char_fn: Callable[[str], object]
    set_joints_fn: Callable[[str], object]
    ret: int

# The dialog's rows, classes local to MatchJointDialog.__init__.
class _JointRow(Protocol):
    row: QtWidgets.QHBoxLayout
    label: QtWidgets.QLabel
    group: QtWidgets.QLineEdit
    selector: QtWidgets.QPushButton

class _ButtonsRow(Protocol):
    row: QtWidgets.QHBoxLayout

class MatchJointDialog(QtWidgets.QDialog):
    layout: QtWidgets.QVBoxLayout
    # row, label, group and selector are those of __init__'s local row classes, not the dialog's.
    row: QtWidgets.QHBoxLayout
    label: QtWidgets.QLabel
    group: QtWidgets.QLineEdit
    selector: QtWidgets.QPushButton
    row0: _JointRow
    row1: _ButtonsRow
    row3: QtWidgets.QHBoxLayout
    spacer1: QtWidgets.QWidget
    only_rotate_around_y: QtWidgets.QCheckBox
    row4: QtWidgets.QHBoxLayout
    spacer2: QtWidgets.QWidget
    match_using_current_frame: QtWidgets.QCheckBox
    row5: QtWidgets.QVBoxLayout
    translate: hou.qt.InputField
    rotate: hou.qt.InputField
    scale: hou.qt.InputField
    pivot: hou.qt.InputField
    pivotrot: hou.qt.InputField
    bottom_row: QtWidgets.QHBoxLayout
    keep_toggle: QtWidgets.QCheckBox
    apply_button: QtWidgets.QPushButton
    reset_button: QtWidgets.QPushButton
    close_button: QtWidgets.QPushButton
    match_callback: Callable[[_MatchJointsKwargs], object]
    select_callback: Callable[[_SelectJointsKwargs], object]
    def __init__(
        self, match_cb: Callable[[_MatchJointsKwargs], object], select_cb: Callable[[_SelectJointsKwargs], object]
    ) -> None: ...
    def getCharacterAndJointFromRow(
        self, row: _JointRow | None
    ) -> tuple[str, str, Literal[True]] | tuple[None, None, Literal[False]]: ...
    def onMatchGroup(self, row: _JointRow | None, mode: Literal[0, 1, 2]) -> None: ...
    def onSelectGroup(self, row: _JointRow) -> None: ...
