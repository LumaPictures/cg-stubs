import dbg
import hou
from apex.apexanimatemodules.base import ApexAnimateBaseModule as ApexAnimateBaseModule, _AnimateState as _BaseState
from apex.ui.selectionmanager import hudpanel as hudpanel, model as ssm, modelconfig as sscfg
from apex.ui.selectionmanager.model import SelectionManagerModel as SelectionManagerModel
from collections.abc import Iterable
from houtypes import ViewerStateCommandKwargs
from typing import Protocol

class _AnimateState(_BaseState, Protocol):
    """The members of the Animate viewer state (`viewer_states/apexanimate.py`) this module uses."""
    def channelListActive(self) -> bool: ...
    def _getVisibleCharacters(self) -> list[str]: ...
    def _getVisibleControlsList(self, include_internal: bool = ..., expand_multi_ctrls: bool = ...) -> list[str]: ...
    def resolvePathRefs(self, refs: Iterable[str]) -> list[str]: ...
    def _splitControlPaths(self, ctrl_paths: Iterable[str], expand_control_groups: bool = ..., ignore_control_groups: bool = ...) -> tuple[list[str], list[str], list[str]]: ...
    def selectAllControls(self) -> None: ...
    def selectDescendants(self) -> None: ...

class ApexAnimateSelectionSets(ApexAnimateBaseModule):
    """
    This class is owned by the APEX Animate state and has access to
    all of its variables

    This class implements all of the commands and helper functions related
    to the management of selection sets for the APEX Animate viewer state.
    """
    selection_manager_model_handle: ssm.SelectionManagerModelHandle | None
    temp_config: sscfg.ModelDictConfig
    def __init__(self, state: _AnimateState) -> None: ...
    @property
    def selection_manager_model(self) -> SelectionManagerModel | None: ...
    def onEnter(self) -> None:
        """ On viewer state enter event
        """
    def onExit(self) -> None:
        """ On viewer state exit event
        """
    def onActivateTool(self) -> None: ...
    def onDeactivateTool(self) -> None: ...
    def unloadTools(self) -> None: ...
    @dbg.ZoneScopedDecorator
    def loadFromGeo(self, chars_geo: hou.Geometry | None, sel_set_geo: hou.Geometry) -> None:
        """ Load everything from the geo into the model. """
    def saveToGeo(self, geo: hou.Geometry) -> None:
        """ Save everything from the model to the geo. """
    def addLabel(self, path: str, label: str) -> None:
        """ Adds a label to the selection sets
        """
    def removeLabel(self, path: str) -> None:
        """ Removes a label from the selection sets
        """
    @dbg.ZoneScopedDecorator
    def updateSelectionManagerModel(self) -> None:
        """ Update the selection manager model to reflect the
            up-to-date set of controls, selection, visible controls
            and visible characters.

            This should be called whenever the set of controls in
            the state changes, like when adding new characters
            or controls.
        """
    def updateControlTree(self) -> None:
        """ Updates the control tree in the selection sets
        """
    def updateSelection(self) -> None:
        """ Updates the selected controls in the selection sets
        """
    def updateVisibleControls(self) -> None:
        """ Updates the visible controls in the selection sets
        """
    def updateVisibleCharacters(self) -> None:
        """ Updates the visible characters in the selection sets
        """
    def updateVisibleConstraints(self) -> None:
        """ Updates the visible constraints in the selection sets
        """
    def updateLabels(self) -> None:
        """ Updates the labels in the selection manager model
        """
    def onCommand(self, kwargs: ViewerStateCommandKwargs) -> bool:
        """ Runs commands related to the selection sets.
            This returns True if it handles the command and False otherwise.
        """
    def _selectControlsCmd(self, ctrl_paths: Iterable[str], pick_modifier: hou.EnumValue[hou.pickModifier] | None, primary_control: str | None = None, update_channel_widget: bool = True, resolve_groups: bool = True, run_control_callbacks: bool = False) -> None: ...
    @property
    def state(self) -> _AnimateState: ...
