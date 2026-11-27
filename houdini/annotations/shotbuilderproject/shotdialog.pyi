from typing import type_check_only

import hou
from PySide6 import QtCore, QtGui, QtWidgets
from shotbuilderproject.panel import ShotBuilderProjectPanel, _Index


SIZE4: int
SIZE10: int
SIZE16: int
SIZE50: int
SIZE60: int
SIZE70: int
SIZE200: int
SIZE395: int
DIALOG_WIDTH: int
DIALOG_HEIGHT: int

class LayersTableFilterProxy(QtCore.QSortFilterProxyModel):
    showAll: bool
    def __init__(self) -> None: ...
    def setShowAll(self, show: bool) -> None: ...
    def filterAcceptsRow(self, rowIdx: int, parent: _Index) -> bool: ...
    # The dialogs always filter a LayersTableModel, whose placeholder names the filter reads.
    @type_check_only
    def sourceModel(self) -> "LayersTableModel": ...

class LayersTableModel(QtCore.QAbstractTableModel):
    totalRows: int
    parent: ShotBuilderProjectPanel
    unitType: str | None
    columnlabels: list[str]
    placeholderNames: list[str]
    # Sublayer (or placeholder unit type) -> the unit chosen for the placeholder, or "".
    sublayers: dict[str, str]
    def __init__(self, parent: ShotBuilderProjectPanel = ...) -> None: ...
    def setLayers(self, unitType: str, showAll: bool = ...) -> None: ...
    def setData(self, index: _Index, value: str, role: int = ...) -> bool: ...
    def rowCount(self, parent: _Index | None = ...) -> int: ...
    def columnCount(self, parent: _Index | None = ...) -> int: ...
    def data(self, index: _Index, role: int = ...) -> str | QtGui.QIcon | None: ...
    def headerData(self, section: int, orientation: QtCore.Qt.Orientation, role: int = ...) -> str | None: ...

class LayersTableView(QtWidgets.QTableView):
    comboBoxes: list[QtWidgets.QComboBox]
    parent: "CreateShotDialog | EditShotDialog"
    panel: ShotBuilderProjectPanel
    sourceModel: LayersTableModel
    def __init__(self, dialogWindow: "CreateShotDialog | EditShotDialog", panel: ShotBuilderProjectPanel) -> None: ...
    def updateLayersView(self, unitType: str, showAll: bool) -> None: ...
    # The unit layer paths of the placeholders' chosen units.
    def getPlaceholders(self) -> list[str]: ...
    def populateCombos(self, unitType: str) -> None: ...

class LayersTableHeader(QtWidgets.QHeaderView):
    def __init__(self, tableview: LayersTableView) -> None: ...
    def mouseMoveEvent(self, event: QtGui.QMouseEvent) -> None: ...
    def mousePressEvent(self, event: QtGui.QMouseEvent) -> None: ...
    def mouseReleaseEvent(self, event: QtGui.QMouseEvent) -> None: ...

class CreateShotDialog(QtWidgets.QDialog):
    parentRow: QtCore.QPersistentModelIndex | None
    panel: ShotBuilderProjectPanel
    showFrameData: bool
    isDirty: bool
    createModes: list[str]
    # (fps, start, end); _createShot() overwrites its items with the line edits' text.
    defaultFrameData: list[float]
    frameDataWidget: QtWidgets.QWidget
    modeWidget: QtWidgets.QWidget
    rangeModeWidget: QtWidgets.QWidget
    listModeWidget: QtWidgets.QWidget
    rangeModeGrid: QtWidgets.QGridLayout
    listModeGrid: QtWidgets.QGridLayout
    multiUnitGrid: QtWidgets.QGridLayout
    typeComboBox: hou.qt.ComboBox
    lineEdits: list[QtWidgets.QLineEdit]
    unitNameInput: QtWidgets.QLineEdit
    doubleValidator: QtGui.QDoubleValidator
    intValidator: QtGui.QIntValidator
    frameDataToggle: QtWidgets.QCheckBox
    createModeComboBox: hou.qt.ComboBox
    startInput: QtWidgets.QLineEdit
    endInput: QtWidgets.QLineEdit
    incrInput: QtWidgets.QLineEdit
    namePatternInput: QtWidgets.QLineEdit
    frameRateInput: QtWidgets.QLineEdit
    startFrameInput: QtWidgets.QLineEdit
    endFrameInput: QtWidgets.QLineEdit
    frame_rate_default: str
    start_frame_default: str
    end_frame_default: str
    showEditableOnlyToggle: QtWidgets.QCheckBox
    layersTableModel: LayersTableModel
    layersTableFilterProxy: LayersTableFilterProxy
    layerWidget: LayersTableView
    createButton: QtWidgets.QPushButton
    okButton: QtWidgets.QPushButton
    cancelButton: QtWidgets.QPushButton
    # parentRow: the view's (proxy) index of the unit type row to add to.
    def __init__(self, panel: ShotBuilderProjectPanel, parentRow: QtCore.QPersistentModelIndex | None = ...) -> None: ...
    def frameDataToggled(self) -> None: ...
    def updateLayersView(self) -> None: ...
    def accept(self) -> None: ...

class EditShotDialog(QtWidgets.QDialog):
    # The view's (proxy) index of the unit's row.
    unitRow: _Index
    panel: ShotBuilderProjectPanel
    # "<unit type>/<unit>"
    unitName: str
    unitType: str
    iconSelection: None
    summaryWidget: QtWidgets.QWidget
    frameDataWidget: QtWidgets.QWidget
    doubleValidator: QtGui.QDoubleValidator
    intValidator: QtGui.QIntValidator
    showEditableOnlyToggle: QtWidgets.QCheckBox
    layersTableModel: LayersTableModel
    layersTableFilterProxy: LayersTableFilterProxy
    layerWidget: LayersTableView
    okButton: QtWidgets.QPushButton
    cancelButton: QtWidgets.QPushButton
    iconButton: QtWidgets.QPushButton
    multiUnitGrid: QtWidgets.QGridLayout
    frameRateInput: QtWidgets.QLineEdit
    startFrameInput: QtWidgets.QLineEdit
    endFrameInput: QtWidgets.QLineEdit
    def __init__(self, panel: ShotBuilderProjectPanel, unitrow: _Index = ...) -> None: ...
    def frameDataToggled(self) -> None: ...
    def updateLayersView(self) -> None: ...
    def setIconButton(self, icon_label: str) -> None: ...
