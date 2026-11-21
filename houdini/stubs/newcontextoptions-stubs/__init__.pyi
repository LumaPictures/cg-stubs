# Houdini stubs generated from Houdini 22.0.466

import PySide6.QtCore
import PySide6.QtGui
import PySide6.QtQml
import PySide6.QtQuick
import PySide6.QtWidgets
from collections.abc import Sequence
from contextoptions import INV_SLIDER_SCALE as INV_SLIDER_SCALE, MenuItem as MenuItem, Option, SLIDER_SCALE as SLIDER_SCALE, field_types as field_types, float_value_types as float_value_types, slider_types as slider_types, string_value_types as string_value_types
from hutil.PySide import QtCore, QtWidgets
from hutil.qt.common import config, core as core, qmlviews
from hutil.qt.nodes import NodeModel as NodeModel, NodePathCompleter as NodePathCompleter
from hutil.qt.pluto import colors as colors
from types import TracebackType
from typing import Any, ClassVar, Literal, Self, TypedDict

class _OptionConfig(TypedDict, total=False):
    label: str
    typeName: str
    hidden: bool
    minimum: float
    maximum: float
    min_locked: bool
    max_locked: bool
    menu_source: str
    menu_items: list[list[str | int | float]]
    file_pattern: str
    safe_name: bool

class _ChangeConfig(TypedDict, total=False):
    type_name: str
    label: str
    order: int
    hidden: bool
    minimum: float
    maximum: float
    min_locked: bool
    max_locked: bool
    menu_items: Sequence[tuple[str, str | int | float]]
    menu_source: str
    file_pattern: str
    safe_name: bool

class _OptionData(TypedDict):
    name: str
    label: str
    typeName: str
    value: int | float | str
    comment: str
    order: int
    hidden: bool
    isAutomatic: bool
    minimum: float
    maximum: float
    minLocked: bool
    maxLocked: bool
    menuItems: list[tuple[str, str | int | float]]
    menuSource: str
    usesAutovalues: bool
    displayLabel: str
    effectiveMenuItems: list[list[Any]]
    safeName: bool
    sliderPos: float | None
    _option: Option

CONTEXT_OPTIONS_SOURCE_URL: str
DEBUG_QML: bool

class _SuppressUndoContext:
    """Context manager that suppresses both internal callbacks and Houdini's undo recording.

    This prevents context option changes from being recorded in Houdini's global undo stack,
    allowing the editor to manage its own undo/redo system without conflicts.
    """
    def __enter__(self) -> Self: ...
    def __exit__(self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None) -> Literal[False]: ...

suppress_undo: _SuppressUndoContext

def sanitize_option_name(name: str) -> str:
    """Sanitize option name to only include letters, numbers, and underscores.

    Any other character is replaced with an underscore.
    """

class Change:
    """Base class for undoable changes."""
    def undo(self, controller: ContextOptionsController) -> None: ...
    def redo(self, controller: ContextOptionsController) -> None: ...
    def canMergeWith(self, other: Change) -> bool:
        """Return True if this change can be merged with another."""
    def mergeWith(self, other: Change) -> None:
        """Merge another change into this one."""

class ValueChange(Change):
    """Change for setting an option's value."""
    name: str
    old_value: float | str | None
    new_value: float | str
    def __init__(self, name: str, old_value: float | str | None, new_value: float | str) -> None: ...
    def undo(self, controller: ContextOptionsController) -> None: ...
    def redo(self, controller: ContextOptionsController) -> None: ...
    def canMergeWith(self, other: Change) -> bool: ...
    def mergeWith(self, other: ValueChange) -> None: ...

class LabelChange(Change):
    """Change for setting an option's label."""
    name: str
    old_label: str
    new_label: str
    def __init__(self, name: str, old_label: str, new_label: str) -> None: ...
    def undo(self, controller: ContextOptionsController) -> None: ...
    def redo(self, controller: ContextOptionsController) -> None: ...

class RenameChange(Change):
    """Change for renaming an option."""
    old_name: str
    new_name: str
    value: float | str
    def __init__(self, old_name: str, new_name: str, value: float | str) -> None: ...
    def undo(self, controller: ContextOptionsController) -> None: ...
    def redo(self, controller: ContextOptionsController) -> None: ...

class AddOptionChange(Change):
    """Change for adding a new option."""
    name: str
    type_name: str
    value: float | str
    config_data: _ChangeConfig
    def __init__(self, name: str, type_name: str, value: float | str, config_data: _ChangeConfig) -> None: ...
    def undo(self, controller: ContextOptionsController) -> None: ...
    def redo(self, controller: ContextOptionsController) -> None: ...

class RemoveOptionChange(Change):
    """Change for removing an option."""
    name: str
    value: float | str
    config_data: _ChangeConfig
    def __init__(self, name: str, value: float | str, config_data: _ChangeConfig) -> None: ...
    def undo(self, controller: ContextOptionsController) -> None: ...
    def redo(self, controller: ContextOptionsController) -> None: ...

class RemoveOptionsChange(Change):
    """Change for removing multiple options as a batch."""
    options_data: Sequence[tuple[str, float | str, _ChangeConfig]]
    def __init__(self, options_data: Sequence[tuple[str, float | str, _ChangeConfig]]) -> None: ...
    def undo(self, controller: ContextOptionsController) -> None: ...
    def redo(self, controller: ContextOptionsController) -> None: ...

class ConfigChange(Change):
    """Change for modifying an option's config (from Config Editor)."""
    name: str
    old_config: _ChangeConfig
    new_config: _ChangeConfig
    def __init__(self, name: str, old_config: _ChangeConfig, new_config: _ChangeConfig) -> None: ...
    def undo(self, controller: ContextOptionsController) -> None: ...
    def redo(self, controller: ContextOptionsController) -> None: ...

class MoveOptionChange(Change):
    """Change for moving an option's position."""
    from_index: int
    to_index: int
    def __init__(self, from_index: int, to_index: int) -> None: ...
    def undo(self, controller: ContextOptionsController) -> None: ...
    def redo(self, controller: ContextOptionsController) -> None: ...

class ContextOptionsListModel(QtCore.QAbstractListModel):
    """List model exposing context options to QML.

    Stores option data directly in dictionaries for reliable access.
    Values are read fresh from Houdini at reload time.
    """
    NameRole: int
    LabelRole: int
    TypeNameRole: int
    ValueRole: int
    CommentRole: int
    OrderRole: int
    HiddenRole: int
    IsAutomaticRole: int
    MinimumRole: int
    MaximumRole: int
    MinLockedRole: int
    MaxLockedRole: int
    MenuItemsRole: int
    MenuSourceRole: int
    UsesAutovaluesRole: int
    DisplayLabelRole: int
    EffectiveMenuItemsRole: int
    SafeNameRole: int
    SliderPosRole: int
    _options: list[_OptionData]
    _filtered_options: list[_OptionData]
    def __init__(self, parent: PySide6.QtCore.QObject | None = None) -> None: ...
    def setController(self, controller: ContextOptionsController) -> None:
        """Set the controller reference for undo support."""
    def _readOptionData(self, name: str) -> _OptionData:
        """Read all data for a context option directly from Houdini."""
    def reload(self) -> None:
        """Reload all context options from Houdini."""
    def rowCount(self, parent: PySide6.QtCore.QModelIndex | PySide6.QtCore.QPersistentModelIndex = ...) -> int: ...
    def roleNames(self) -> dict[int, bytes]: ...
    def data(self, index: PySide6.QtCore.QModelIndex | PySide6.QtCore.QPersistentModelIndex, role: int = ...) -> str | int | float | bool | list[tuple[str, str | int | float]] | list[list[Any]] | None: ...
    def setShowAutomatic(self, show: bool) -> None: ...
    def setShowHidden(self, show: bool) -> None: ...
    def setFilterText(self, text: str) -> None: ...
    countsChanged: PySide6.QtCore.Signal
    def userCount(self) -> int:
        """Count of visible user-generated (non-automatic) context options."""
    def automaticCount(self) -> int:
        """Count of automatic context options."""
    def hiddenCount(self) -> int:
        """Count of hidden context options."""
    def getOptionAtIndex(self, index: int) -> _OptionData | None:
        """Get the option data dict at the given filtered index."""
    def getOptionNameAtIndex(self, index: int) -> str:
        """Get the option name at the given filtered index."""
    def notifyValueChanged(self, name: str) -> None:
        """Update the stored value and notify QML that a value changed."""
    def notifySliderPosChanged(self, name: str, pos: float) -> None:
        """Update the stored slider position and notify QML."""
    def moveOption(self, fromIndex: int, toIndex: int, record_undo: bool = True) -> None:
        """Move an option from one position to another in the filtered list."""

class ContextOptionsController(QtCore.QObject):
    """Controller for managing context options from QML."""
    optionsChanged: PySide6.QtCore.Signal
    optionTypesChanged: PySide6.QtCore.Signal
    canUndoChanged: PySide6.QtCore.Signal
    canRedoChanged: PySide6.QtCore.Signal
    def __init__(self, parent: PySide6.QtCore.QObject | None = None) -> None: ...
    def canUndo(self) -> bool: ...
    def canRedo(self) -> bool: ...
    def undo(self) -> None:
        """Undo the last change."""
    def redo(self) -> None:
        """Redo the last undone change."""
    def clearUndoStack(self) -> None:
        """Clear the undo/redo stack."""
    def setContinuous(self, continuous: bool, optionName: str = '') -> None:
        """Set continuous edit mode (for slider dragging, etc.).

        When entering continuous mode, saves the current value of the option.
        When exiting continuous mode, creates a single undo entry if the value changed.
        """
    def model(self) -> ContextOptionsListModel: ...
    def optionTypes(self) -> list[dict[str, str]]: ...
    def reload(self) -> None:
        """Reload all context options."""
    def addOption(self, typeName: str, baseName: str = '') -> None:
        """Add a new context option of the given type."""
    def addOptionAndScroll(self, typeName: str, baseName: str = '') -> int:
        """Add a new context option at the bottom and return its index for scrolling."""
    def removeOption(self, name: str) -> None:
        """Remove a context option by name."""
    def removeOptionAtIndex(self, index: int) -> None:
        """Remove the option at the given index."""
    def removeOptions(self, names: Sequence[str]) -> None:
        """Remove multiple context options as a single undoable operation."""
    def setValue(self, name: str, value: float | str) -> None:
        """Set the value of a context option, clamping to locked min/max if applicable."""
    def setSliderPos(self, name: str, pos: float) -> None:
        """Set the slider position (0-1) for a slider option."""
    def setLabel(self, name: str, label: str) -> None:
        """Set the label of a context option."""
    def renameOption(self, oldName: str, newName: str) -> bool:
        """Rename a context option.

        If the option has safe_name=True, the new name will be sanitized to
        only include letters, numbers, and underscores.
        """
    def setShowAutomatic(self, show: bool) -> None: ...
    def setShowHidden(self, show: bool) -> None: ...
    def setFilterText(self, text: str) -> None: ...
    def getOptionNameAtIndex(self, index: int) -> str:
        """Get the name of the option at the given index."""
    def moveOption(self, fromIndex: int, toIndex: int) -> None:
        """Move an option from one position to another."""
    def selectFile(self, name: str) -> None:
        """Open file chooser dialog and set the value for a file_path option."""
    def copyToClipboard(self, text: str) -> None:
        """Copy text to the system clipboard."""
    def getFilePathCompletions(self, path: str) -> list[str]:
        """Get file path completions for the given partial path."""
    def getNodePathCompletions(self, path: str) -> list[str]:
        """Get node path completions for the given partial path."""
    def setupPythonHighlighter(self, textDocument: PySide6.QtQuick.QQuickTextDocument | None) -> None:
        """Set up Python syntax highlighting on a QML TextArea's textDocument."""
    def openTestWindow(self) -> None:
        """Create a standalone test window for the context options editor."""
    def exportJson(self) -> None:
        """Export context options to a JSON file.

        Uses the same file dialog and export logic as the original
        OptionsEditor._export_json_file / contextoptions.exportJson.
        """
    def importJson(self) -> None:
        """Import context options from a JSON file.

        Uses the same file dialog, merge/replace prompt, and import logic
        as the original OptionsEditor._import_file / contextoptions.importJson.
        """
    def getOptionConfig(self, optionName: str) -> _OptionConfig:
        """Get the configuration for an option (for the config editor)."""
    def saveOptionConfig(self, config_json: str) -> str:
        """Save the configuration for an option.

        Accepts a JSON string with keys: optionName, label, typeName, hidden,
        minimum, maximum, minLocked, maxLocked, menuSource, menuItems,
        filePattern, safeName.

        Returns empty string on success, or an error message on failure.
        """

class ContextOptionsConfig(config.BaseConfig):
    """Configuration for context options editor."""
    showAutomatic: bool
    showHidden: bool

class ContextOptionsState(qmlviews.SharedState[ContextOptionsConfig]):
    """Shared state for the QML context options editor."""
    def __init__(self, **kwargs: object) -> None: ...
    @property
    def controller(self) -> ContextOptionsController: ...
    def setupEngine(self, engine: PySide6.QtQml.QQmlEngine, **kwargs: object) -> None: ...

class ContextOptionsWidget(qmlviews.BaseQmlWidget[ContextOptionsState]):
    """QML-based widget for the context options editor."""
    SOURCE_URL: str
    def __init__(self, parent: PySide6.QtWidgets.QWidget | None = None) -> None: ...
    def showEvent(self, event: PySide6.QtGui.QShowEvent) -> None: ...
    def hideEvent(self, event: PySide6.QtGui.QHideEvent) -> None: ...

class ContextOptionsPanel(QtWidgets.QWidget):
    """Panel wrapper for the context options widget."""
    context_options_window: ClassVar[ContextOptionsPanel | None]
    def __init__(self, parent: PySide6.QtWidgets.QWidget | None = None, as_window: bool = False) -> None: ...
    def resizeEvent(self, event: PySide6.QtGui.QResizeEvent) -> None: ...
    def mousePressEvent(self, event: PySide6.QtGui.QMouseEvent) -> None: ...
    def mouseDoubleClickEvent(self, event: PySide6.QtGui.QMouseEvent) -> None: ...
    @classmethod
    def getContextOptionsWindow(cls) -> ContextOptionsPanel: ...

def createQmlOptionsEditor() -> ContextOptionsPanel:
    """Factory function to create the QML options editor widget."""

class TestWindow(QtWidgets.QMainWindow):
    """Standalone window for testing the Context Options Editor outside of a Python Panel."""
    def __init__(self, parent: PySide6.QtWidgets.QWidget | None = None) -> None: ...

def createTestWindow() -> PySide6.QtWidgets.QMainWindow | None:
    """
    Create and show a standalone test window for the Context Options Editor.

    This creates the editor in a standalone window rather than a Python Panel,
    which can be useful for testing and debugging.

    Usage:
        import newcontextoptions
        newcontextoptions.createTestWindow()

    Returns:
        The test window (when running standalone) or None (when deferred inside Houdini).
    """
