import hou
from collections.abc import Callable as Callable, Sequence
from hutil.PySide import QtWidgets
from typing import Literal, Protocol, Required, TypedDict

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

class _JointRow(Protocol):
    row: QtWidgets.QHBoxLayout
    label: QtWidgets.QLabel
    group: QtWidgets.QLineEdit
    selector: QtWidgets.QPushButton

class _ButtonsRow(Protocol):
    row: QtWidgets.QHBoxLayout

class MatchJointDialog(QtWidgets.QDialog):
    """ A dialog holding the Motion Mixer Match Joints Settings."""
    layout: QtWidgets.QVBoxLayout
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
    def __init__(self, match_cb: Callable[[_MatchJointsKwargs], object], select_cb: Callable[[_SelectJointsKwargs], object]) -> None: ...
    def onClose(self) -> None: ...
    def getCharacterAndJointFromRow(self, row: _JointRow | None) -> tuple[str, str, Literal[True]] | tuple[None, None, Literal[False]]: ...
    def onApply(self) -> None: ...
    def onReset(self) -> None: ...
    def onMatchGroup(self, row: _JointRow | None, mode: Literal[0, 1, 2]) -> None: ...
    def onMatchGroup0(self) -> None: ...
    def onMatchGroup1(self) -> None: ...
    def onMatchGroup2(self) -> None: ...
    def onSelectGroup(self, row: _JointRow) -> None: ...
    def onSelectGroup0(self) -> None: ...
