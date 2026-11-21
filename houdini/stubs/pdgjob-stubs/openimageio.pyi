# Houdini stubs generated from Houdini 22.0.466

from pdgjob import pdgcmd as pdgcmd, pdgjson as pdgjson

from typing import TypeAlias
from typing import TypeAlias
_WorkItem: TypeAlias = pdgjson.WorkItem | pdgjson.NativeWorkItem
OPENIMAGEIO_TOOL_NAME: str
SANITIZE_VARS: tuple[str, ...]
BATCH_MODE_OFF: int
BATCH_MODE_ALL: int
ALL_FRAMES: int
FIRST_FRAME: int

def run_item(work_item: _WorkItem) -> None: ...
def run_batch(item: _WorkItem) -> None: ...
def cook(work_item: _WorkItem) -> bool: ...
