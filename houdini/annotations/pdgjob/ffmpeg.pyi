from typing import TypeAlias

from pdgjob import pdgjson

_WorkItem: TypeAlias = pdgjson.WorkItem | pdgjson.NativeWorkItem

FFMPEG_TOOL_NAME: str
SANITIZE_VARS: tuple[str, ...]

def extractimages(work_item: _WorkItem) -> None: ...
def encodevideo(work_item: _WorkItem) -> None: ...
def cook(work_item: _WorkItem) -> bool: ...
