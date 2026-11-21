from collections.abc import Callable, MutableMapping
from typing import Any

import hou

def setStateEventCallback(
    self: hou.hda,
    hda_globals: MutableMapping[str, Any],
    state_name: str,
    event_name: str,
    callback: Callable[..., object],
) -> None: ...
def reloadHDAModule(self: hou.hda, hda_module: hou.HDAModule) -> None: ...
def reloadHDAViewerStateModule(self: hou.hda, hda_module: hou.HDAViewerStateModule) -> None: ...
def reloadHDAViewerHandleModule(self: hou.hda, hda_module: hou.HDAViewerHandleModule) -> None: ...
