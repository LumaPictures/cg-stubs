import hou
from dataclasses import dataclass as dataclass
from hutil.PySide import QtCore, QtGui, QtWidgets
from shotbuilderproject.panel import ShotBuilderProjectPanel as ShotBuilderProjectPanel, _Index

SIZE4: int
SIZE10: int
SIZE16: int
SIZE50: int
SIZE60: int
SIZE70: int
SIZE200: int
SIZE395: int
SMALL_FONT = SIZE10
LARGE_FONT = SIZE16
SIZE_PADDING = SIZE4
ICON_PADDING = SIZE4
ICON_PREVIEW_SIZE = SIZE50
COLUMN_SIZE = SIZE200
LINE_EDIT_WIDTH = SIZE395
DIALOG_WIDTH: int
DIALOG_HEIGHT: int
UNIT_ICON: str
SUBLAYER_ICON: str
START_DEFAULT: int
END_DEFAULT: int
INCR_DEFAULT: int

class LayersTableFilterProxy(QtCore.QSortFilterProxyModel):
    """Filter based on configurability of sublayer row"""
    showAll: bool
    def __init__(self) -> None: ...
    def setShowAll(self, show: bool) -> None: ...
    def filterAcceptsRow(self, rowIdx: int, parent: _Index) -> bool: ...
    def sourceModel(self) -> LayersTableModel: ...

class LayersTableModel(QtCore.QAbstractTableModel):
    totalRows: int
    parent: ShotBuilderProjectPanel
    unitType: str | None
    columnlabels: list[str]
    placeholderNames: list[str]
    sublayers: dict[str, str]
    SublayerNameColumn: int
    ValueColumn: int
    def __init__(self, parent: ShotBuilderProjectPanel | None = None) -> None: ...
    def setLayers(self, unitType: str, showAll: bool = True) -> None: ...
    def setData(self, index: _Index, value: str, role: int = ...) -> bool: ...
    def rowCount(self, parent: _Index | None = None) -> int: ...
    def columnCount(self, parent: _Index | None = None) -> int: ...
    def data(self, index: _Index, role: int = ...) -> str | QtGui.QIcon | None: ...
    def headerData(self, section: int, orientation: QtCore.Qt.Orientation, role: int = ...) -> str | None: ...

class LayersTableView(QtWidgets.QTableView):
    comboBoxes: list[QtWidgets.QComboBox]
    parent: CreateShotDialog | EditShotDialog
    panel: ShotBuilderProjectPanel
    sourceModel: LayersTableModel
    def __init__(self, dialogWindow: CreateShotDialog | EditShotDialog, panel: ShotBuilderProjectPanel) -> None: ...
    def updateLayersView(self, unitType: str, showAll: bool) -> None: ...
    def getPlaceholders(self) -> list[str]: ...
    def populateCombos(self, unitType: str) -> None: ...

class LayersTableHeader(QtWidgets.QHeaderView):
    """ Set the header styling for the layers list view, removing default styling on click and other unwanted visuals"""
    def __init__(self, tableview: LayersTableView) -> None: ...
    def mouseMoveEvent(self, event: QtGui.QMouseEvent) -> None: ...
    def mousePressEvent(self, event: QtGui.QMouseEvent) -> None: ...
    def mouseReleaseEvent(self, event: QtGui.QMouseEvent) -> None: ...

class CreateShotDialog(QtWidgets.QDialog):
    """A dialog for creating units, per the current shot builder project config."""
    parentRow: QtCore.QPersistentModelIndex | None
    panel: ShotBuilderProjectPanel
    showFrameData: bool
    isDirty: bool
    createModes: list[str]
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
    SingleCreate: int
    RangeCreate: int
    ListCreate: int
    def __init__(self, panel: ShotBuilderProjectPanel, parentRow: QtCore.QPersistentModelIndex | None = None) -> None: ...
    def frameDataToggled(self) -> None: ...
    def updateLayersView(self) -> None: ...
    def accept(self) -> None: ...

class EditShotDialog(QtWidgets.QDialog):
    """A dialog for edit unit selected."""
    unitRow: _Index
    panel: ShotBuilderProjectPanel
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
    def __init__(self, panel: ShotBuilderProjectPanel, unitrow: _Index | None = None) -> None: ...
    def frameDataToggled(self) -> None: ...
    def updateLayersView(self) -> None: ...
    def setIconButton(self, icon_label: str) -> None: ...
