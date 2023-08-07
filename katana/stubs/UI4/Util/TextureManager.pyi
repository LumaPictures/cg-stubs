# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import Nodes2DAPI as Nodes2DAPI
import PyQt5.QtCore as QtCore
import Utils as Utils
from typing import Set, Tuple

def DirtyBufferRects(frameBufferObj, updateRects): ...
def DrawBuffers(widget, buffers, drawWindow, displayRequest, overlayMode, additionalTileCacheIDsToLock): ...
def FlushTexturePool(): ...
def GetTexturePoolSizeMB(): ...
