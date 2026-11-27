from .model import AnimationLayerItem as AnimationLayerItem, AnimationLayersModel as AnimationLayersModel, Column as Column, WeightChangeType as WeightChangeType, toHouColor as toHouColor, toQtColor as toQtColor
from .slider import ChangeType as ChangeType, KeyableSlider as KeyableSlider
from apex.ui.animationlayers.model import _WeightChangeType
from collections.abc import Callable as Callable
from hutil.PySide import QtCore, QtGui, QtWidgets
from poselib.itemlibrary import IdentityProxyModel
from typing import Literal, TypedDict, Unpack

class _ViewKwargs(TypedDict):
    model: AnimationLayersModel

class _DelegateKwargs(TypedDict, total=False):
    objectName: str
    destroyed: Callable[[], object] | Callable[[QtCore.QObject | None], object]
    objectNameChanged: Callable[[], object] | Callable[[str], object]
    closeEditor: Callable[[], object] | Callable[[QtWidgets.QWidget], object] | Callable[[QtWidgets.QWidget, QtWidgets.QAbstractItemDelegate.EndEditHint], object]
    commitData: Callable[[], object] | Callable[[QtWidgets.QWidget], object]
    sizeHintChanged: Callable[[], object] | Callable[[QtCore.QModelIndex], object]

class ReverseProxyModel(IdentityProxyModel):
    def index(self, row: int, column: int, parent: QtCore.QModelIndex | QtCore.QPersistentModelIndex = ...) -> QtCore.QModelIndex: ...
    def rowCount(self, parent: QtCore.QModelIndex | QtCore.QPersistentModelIndex = ...) -> int: ...
    def columnCount(self, parent: QtCore.QModelIndex | QtCore.QPersistentModelIndex = ...) -> int: ...
    def mapFromSource(self, source_index: QtCore.QModelIndex | QtCore.QPersistentModelIndex, filtered: bool = True) -> QtCore.QModelIndex: ...
    def mapToSource(self, proxy_index: QtCore.QModelIndex | QtCore.QPersistentModelIndex) -> QtCore.QModelIndex: ...
    def __init__(self, parent: QtCore.QObject | None, model: AnimationLayersModel) -> None: ...

class NameDelegate(QtWidgets.QStyledItemDelegate):
    """
    A delegate for drawing the name column.

    Will first draw the background as usual, then draw the icon,
    then draw the colour circle, then the name text, then the
    description label.
    """
    ICON_SIZE: int
    NAME_SPACING_X: int
    ICON_SPACING_X: int
    COLOR_CHIP_SIZE: int
    def __init__(self, parent: AnimationLayersView, **kwargs: Unpack[_DelegateKwargs]) -> None: ...
    def numIcons(self, index: QtCore.QModelIndex | QtCore.QPersistentModelIndex) -> int:
        """The number of icons drawn before this items name."""
    def updateEditorGeometry(self, editor: QtWidgets.QWidget, option: QtWidgets.QStyleOptionViewItem, index: QtCore.QModelIndex | QtCore.QPersistentModelIndex) -> None:
        """Qt callback to set the size and position of the editor."""
    def initStyleOption(self, option: QtWidgets.QStyleOptionViewItem, index: QtCore.QModelIndex | QtCore.QPersistentModelIndex) -> None:
        """
        Qt Override to customize what the base class paint method does.
        """
    def paint(self, painter: QtGui.QPainter, option: QtWidgets.QStyleOptionViewItem, index: QtCore.QModelIndex | QtCore.QPersistentModelIndex) -> None:
        """Qt override to draw the name column."""

class TypeDelegate(QtWidgets.QStyledItemDelegate):
    """
    A delegate for drawing the type column.

    Draws the type in a smaller, colored font.
    """
    PADDING_X: int
    def __init__(self, parent: AnimationLayersView, **kwargs: Unpack[_DelegateKwargs]) -> None: ...
    def initStyleOption(self, option: QtWidgets.QStyleOptionViewItem, index: QtCore.QModelIndex | QtCore.QPersistentModelIndex) -> None:
        """
        Qt Override to customize what the base class paint method does.
        """
    def paint(self, painter: QtGui.QPainter, option: QtWidgets.QStyleOptionViewItem, index: QtCore.QModelIndex | QtCore.QPersistentModelIndex) -> None:
        """Qt override to draw the type column."""

class WeightDelegate(QtWidgets.QStyledItemDelegate):
    """Custom Drawing for the slider in the weight column."""
    def __init__(self, parent: AnimationLayersView, model: AnimationLayersModel, show_sliders: bool, **kwargs: Unpack[_DelegateKwargs]) -> None: ...
    def clear(self) -> None: ...
    def createEditor(self, parent: QtWidgets.QWidget | None, option: QtWidgets.QStyleOptionViewItem, index: QtCore.QModelIndex | QtCore.QPersistentModelIndex) -> KeyableSlider: ...
    def setEditorData(self, editor: KeyableSlider, index: QtCore.QModelIndex | QtCore.QPersistentModelIndex) -> None: ...
    def setModelData(self, editor: QtWidgets.QWidget, proxy_model: QtCore.QAbstractItemModel, proxy_index: QtCore.QModelIndex | QtCore.QPersistentModelIndex) -> None: ...

class IconDelegate(QtWidgets.QStyledItemDelegate):
    """Custom drawing for the icons in the icon columns."""
    def __init__(self, parent: AnimationLayersView, **kwargs: Unpack[_DelegateKwargs]) -> None: ...
    def initStyleOption(self, option: QtWidgets.QStyleOptionViewItem, index: QtCore.QModelIndex | QtCore.QPersistentModelIndex) -> None:
        """ Qt Override to customize what the base class paint
            method does.
        """
    def paint(self, painter: QtGui.QPainter, option: QtWidgets.QStyleOptionViewItem, index: QtCore.QModelIndex | QtCore.QPersistentModelIndex) -> None:
        """ Qt override to draw the icon columns. """

class AnimationLayersView(QtWidgets.QTableView):
    """
    Tree view used for the Animation Layers panel.
    """
    ROW_HEIGHT: int
    WEIGHT_COLUMN_WIDTH: int
    SLIDER_FIELD_WIDTH: int
    def __init__(self, *args: QtWidgets.QWidget | None, **kwargs: Unpack[_ViewKwargs]) -> None: ...
    def isLayerDisabled(self, index: QtCore.QModelIndex) -> bool:
        """Returns whether the layer associated with the index is disabled."""
    def resetModel(self, new_model: AnimationLayersModel | None) -> None:
        """
        Swap the model that the view uses to the new_model.
        Will first disconnect the selectionChanged from the current
        selection model, then change the model, then reset the view,
        then connect the selectionChanged signal for the new model.
        """
    def getModel(self) -> AnimationLayersModel:
        """
        Return the source model used internally.
        Note that this is not the proxy model.
        """
    def toggleWeightSliders(self, shown: bool) -> None: ...
    def toggleColumn(self, column: Column, shown: bool) -> None: ...
    def setSelectedIndex(self, source_index: QtCore.QModelIndex | QtCore.QPersistentModelIndex) -> None: ...
    def getSelectedIndex(self) -> QtCore.QModelIndex: ...
    def getSelectedIndexes(self) -> list[QtCore.QModelIndex]:
        """Returns all selected indexes."""
    def getSelectedRows(self) -> list[QtCore.QModelIndex]: ...
    def mapIndexToSource(self, proxy_index: QtCore.QModelIndex | QtCore.QPersistentModelIndex) -> QtCore.QModelIndex: ...
    def mapIndexFromSource(self, source_index: QtCore.QModelIndex | QtCore.QPersistentModelIndex) -> QtCore.QModelIndex: ...
    def setWeightKeyframe(self, proxy_index: QtCore.QModelIndex) -> None: ...
    def removeWeightKeyframe(self, proxy_index: QtCore.QModelIndex) -> None: ...
    def addWeightToChannelList(self, proxy_index: QtCore.QModelIndex) -> None: ...
    def resetWeights(self, proxy_index: QtCore.QModelIndex) -> None: ...
    def deleteWeightChannels(self, proxy_index: QtCore.QModelIndex) -> None: ...
    def setLayerWeights(self, proxy_index: QtCore.QModelIndex, weight: float, change_type: _WeightChangeType) -> None: ...
    def contextMenuEvent(self, event: QtGui.QContextMenuEvent) -> None: ...
    def openColorEditor(self, index: QtCore.QModelIndex, full_editor: bool | QtCore.Qt.KeyboardModifier = False) -> None: ...
    def isSelectable(self, index: QtCore.QModelIndex) -> bool: ...
    def mousePressEvent(self, event: QtGui.QMouseEvent) -> None:
        """
        Override to handle mouse events. Used to prevent selection when
        clicking on the columns with buttons.
        """
    def keyPressEvent(self, event: QtGui.QKeyEvent) -> Literal[False]:
        """
        Override to ignore keyboard events on this view. Otherwise, this view
        would block keyboard events for keying channels etc.
        """
