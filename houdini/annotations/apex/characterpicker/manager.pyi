from collections.abc import MutableMapping
from typing import Any, Protocol

import apex.stateutils_2 as asu

class _AnimateState(asu._AnimateState, Protocol):
    """The members of the Animate viewer state (`viewer_states/apexanimate.py`) this module uses."""

    def saveCharacterPickerLayout(self) -> None: ...

class CharacterPickerManager:
    def load(self, state: _AnimateState) -> None: ...
    @property
    def state(self) -> _AnimateState | None: ...
    def onCommand(self, name: str, args: MutableMapping[str, Any]) -> bool: ...
