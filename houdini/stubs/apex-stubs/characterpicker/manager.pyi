import apex.stateutils_2 as asu
from apex.characterpicker.autogen import projectControls as projectControls, projectRigControls as projectRigControls
from apex.characterpicker.commands import Commands as Commands, ControlsFilter as ControlsFilter, ProjectionDirection as ProjectionDirection
from collections.abc import MutableMapping
from typing import Any, Protocol

class _AnimateState(asu._AnimateState, Protocol):
    """The members of the Animate viewer state (`viewer_states/apexanimate.py`) this module uses."""
    def saveCharacterPickerLayout(self) -> None: ...

APEX_CHARPICKER_ATTRIB_NAME: str
SCENE_PICKER_PATH: str

class CharacterPickerManager:
    """
    Handles communication between the APEX Animate State and the
    Character Picker Panels
    """
    def __init__(self) -> None: ...
    def load(self, state: _AnimateState) -> None: ...
    @property
    def state(self) -> _AnimateState | None: ...
    def unload(self) -> None: ...
    def onCommand(self, name: str, args: MutableMapping[str, Any]) -> bool: ...
