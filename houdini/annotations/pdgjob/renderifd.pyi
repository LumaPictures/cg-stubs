from typing import TypeAlias

from pdgjob import pdgjson

_WorkItem: TypeAlias = pdgjson.WorkItem | pdgjson.NativeWorkItem

def cook(work_item: _WorkItem, hfs: str = ...) -> bool: ...
