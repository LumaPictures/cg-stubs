# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import NodegraphAPI as NodegraphAPI
import Nodes2DAPI as Nodes2DAPI
import Nodes3DAPI as Nodes3DAPI
import PyQt5.QtWidgets
import PyQt5.QtGui as QtGui
import PyQt5.QtWidgets as QtWidgets
import PyUtilModule.RenderManager as RenderManager
import Utils as Utils
from UI4.Util.IconManager import GetPixmap as GetPixmap
from UI4.Widgets.ToolbarButton import ToolbarButton as ToolbarButton
from _typeshed import Incomplete
from types import ModuleType
from typing import ClassVar, Set, Tuple

class UpdateModePopdownButton2D(_UpdateModePopdownButton):
    POPDOWN_MODE_ICONS: ClassVar[dict] = ...
    POPDOWN_OPTIONS: ClassVar[list] = ...
    POPDOWN_TOOLTIP: ClassVar[str] = ...
    UPDATE_MODE_ARG_KEY: ClassVar[str] = ...
    def _getGlobalUpdateMode(self): ...
    def _registerEventHandlers(self): ...
    def _setGlobalUpdateMode(self, updateMode): ...

class UpdateModePopdownButton3D(_UpdateModePopdownButton):
    POPDOWN_MODE_ICONS: ClassVar[dict] = ...
    POPDOWN_OPTIONS: ClassVar[list] = ...
    POPDOWN_TOOLTIP: ClassVar[str] = ...
    UPDATE_MODE_ARG_KEY: ClassVar[str] = ...
    UpdateModes: ClassVar[ModuleType] = ...
    def _getGlobalUpdateMode(self): ...
    def _registerEventHandlers(self): ...
    def _setGlobalUpdateMode(self, updateMode): ...

class UpdateModeWidget2D(_UpdateModeWidget):
    BUTTON_TOOLTIP: ClassVar[str] = ...
    def _UpdateModeWidget2D__on_parameter_setValue(self, args): ...
    def _createPopdownButton(self): ...
    @staticmethod
    def _isUpdateModeManual(updateMode): ...
    def _registerEventHandlers(self): ...
    def _triggerManualUpdate(self): ...

class UpdateModeWidget3D(_UpdateModeWidget):
    BUTTON_TOOLTIP: ClassVar[str] = ...
    def _createPopdownButton(self): ...
    def _isGlobalDirty(self): ...
    @staticmethod
    def _isUpdateModeManual(updateMode): ...
    def _registerEventHandlers(self): ...
    def _triggerManualUpdate(self): ...

class _UpdateModePopdownButton(ToolbarButton):
    POPDOWN_MODE_ICONS: ClassVar[dict] = ...
    POPDOWN_OPTIONS: ClassVar[list] = ...
    POPDOWN_TOOLTIP: ClassVar[str] = ...
    UPDATE_MODE_ARG_KEY: ClassVar[None] = ...
    _UpdateModePopdownButton__ICON_FILES: ClassVar[dict] = ...
    _UpdateModePopdownButton__ICON_PIXMAPS: ClassVar[None] = ...
    _UpdateModePopdownButton__MINIMUM_HEIGHT: ClassVar[int] = ...
    def __init__(self, parent, registerEventHandler: bool = ...) -> None: ...
    @classmethod
    def _UpdateModePopdownButton__getUpdateModePixmap(cls, updateMode): ...
    def _UpdateModePopdownButton__on_menu_aboutToShow(self): ...
    def _UpdateModePopdownButton__on_menu_triggered(self, action): ...
    def _getGlobalUpdateMode(self): ...
    def _on_updateModeChanged(self, *args, **kwargs): ...
    def _registerEventHandlers(self): ...
    def _setGlobalUpdateMode(self, updateMode): ...
    def getUpdateMode(self): ...
    def setUpdateMode(self, updateMode): ...

class _UpdateModeWidget(PyQt5.QtWidgets.QWidget):
    BUTTON_TOOLTIP: ClassVar[str] = ...
    IS_DIRTY_ARG_KEY: ClassVar[str] = ...
    _UpdateModeWidget__ACTIVE_HILITE_ICON_FILE: ClassVar[str] = ...
    _UpdateModeWidget__ACTIVE_ICON_FILE: ClassVar[str] = ...
    _UpdateModeWidget__DIRTY_HILITE_ICON_FILE: ClassVar[str] = ...
    _UpdateModeWidget__DIRTY_ICON_FILE: ClassVar[str] = ...
    _UpdateModeWidget__INACTIVE_ICON_FILE: ClassVar[str] = ...
    def __init__(self, parent, text: Incomplete | None = ...) -> None: ...
    def _createPopdownButton(self): ...
    def _isGlobalDirty(self): ...
    def _on_dirtyStateChanged(self, *args, **kwargs): ...
    def _on_updateButtonClicked(self, *args, **kwargs): ...
    def _on_updateModeChanged(self, *args, **kwargs): ...
    def _registerEventHandlers(self): ...
    def _triggerManualUpdate(self): ...
    def isDirty(self): ...
    def setButtonType(self, buttonType: Incomplete | None = ...): ...
    def setDirty(self, dirty): ...
    def updateState(self): ...
