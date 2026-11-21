from typing import TypeAlias

from pdgjob import pdgjson

_WorkItem: TypeAlias = pdgjson.WorkItem | pdgjson.NativeWorkItem

IMAGEMAGICK_TOOL_NAME: str
SANITIZE_VARS: tuple[str, ...]
USE_SYSTEM_PATH: int
USE_PDG_IMAGEMAGICK_DIR: int
USE_PDG_IMAGEMAGICK: int
USE_CUSTOM_PATH: int
BATCH_MODE_OFF: int
BATCH_MODE_ALL: int
IM_MONTAGE: int
IM_CONVERT: int
IM_COMPOSITE: int
IM_COMPARE: int
IM_IMPORT: int
IM_CONJURE: int
ALL_FRAMES: int
FIRST_FRAME: int

def imOpCodeToString(op: int | None) -> str: ...
def findImageMagick(work_item: _WorkItem) -> tuple[str | None, bool]: ...
def run_item(work_item: _WorkItem, imagemagick_path: str | None, add_op_arg: bool) -> None: ...
def run_batch(item: _WorkItem) -> bool: ...
def cook(work_item: _WorkItem) -> None: ...
