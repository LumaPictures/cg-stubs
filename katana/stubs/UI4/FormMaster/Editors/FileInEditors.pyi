# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import AssetAPI as AssetAPI
import NodegraphAPI as NodegraphAPI
import Nodes2DAPI as Nodes2DAPI
import PyQt5.QtCore
import QT4FormWidgets as QT4FormWidgets
import QT4Widgets as QT4Widgets
import PyQt5.QtCore as QtCore
import PyQt5.QtGui as QtGui
import PyQt5.QtWidgets as QtWidgets
import UI4.FormMaster.States as States
import UI4 as UI4
import Utils as Utils
from QT4FormWidgets.GroupFormWidget import GroupFormWidget
from QT4FormWidgets.PopupFormWidget import PopupFormWidget
from _typeshed import Incomplete
from typing import ClassVar, Set, Tuple

class CalculateInOutThread(PyQt5.QtCore.QThread):
    inOutSet: ClassVar[PyQt5.QtCore.pyqtSignal] = ...
    def __init__(self, nodeName, reportErrors: bool = ...) -> None: ...
    def run(self): ...

class ChannelGroupFormWidget(GroupFormWidget):
    def __init__(self, parent, policy, factory) -> None: ...
    def _ChannelGroupFormWidget__button_clicked_CB(self): ...

class ExrChannelFormWidget(PopupFormWidget):
    def __init__(self, parent, policy, factory) -> None: ...
    def _ExrChannelFormWidget__updateOptions(self): ...
    def _ExrChannelFormWidget__valueChanged(self, event): ...
    def _freeze(self): ...
    def _thaw(self): ...

class ExrGroupedChannelsFormWidget(PopupFormWidget):
    def __init__(self, parent, policy, factory) -> None: ...
    def _ExrGroupedChannelsFormWidget__setComponentValue(self, node: NodegraphAPI.Node, channelComponent, componentValue): ...
    def _ExrGroupedChannelsFormWidget__updateOptions(self): ...
    def _ExrGroupedChannelsFormWidget__valueChanged(self, event): ...
    def _freeze(self): ...
    def _thaw(self): ...
    def valueChangedEvent(self, event): ...

class FileInTimingEditorFormWidget(GroupFormWidget):
    def __init__(self, parent, policy, factory) -> None: ...
    def _FileInTimingEditorFormWidget__actionMenu_CB(self, menu): ...
    def _FileInTimingEditorFormWidget__autoCalc_CB(self): ...
    def _FileInTimingEditorFormWidget__fileValueChanged(self): ...
    def _FileInTimingEditorFormWidget__inOutSet(self, nodeName, errorMsg): ...
    def _FileInTimingEditorFormWidget__lockToGlobals_CB(self, *args): ...
    def _FileInTimingEditorFormWidget__paramChange(self, args): ...
    def _FileInTimingEditorFormWidget__setInOutModes(self): ...
    def _FileInTimingEditorFormWidget__setLockFrameRange(self): ...
    def _FileInTimingEditorFormWidget__updateFrameLabel(self, labelWidget, policy, labelText, errorValue, locked): ...
    def _FileInTimingEditorFormWidget__updateInOut(self, interactive: bool = ...): ...
    def _FileInTimingEditorFormWidget__updateInfo(self): ...
    def _FileInTimingEditorFormWidget__valueChanged(self, event): ...
    def _freeze(self): ...
    def _thaw(self): ...
    def addFormWidgetChild(self, child, atIndex: Incomplete | None = ...): ...

class SimpleChannelGroupFormWidget(GroupFormWidget):
    def __init__(self, parent, policy, factory) -> None: ...
