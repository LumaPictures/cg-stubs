from pdgjob import pdgjson as pdgjson

from typing import TypeAlias
from typing import TypeAlias
_WorkItem: TypeAlias = pdgjson.WorkItem | pdgjson.NativeWorkItem
def cook(work_item: _WorkItem) -> bool: ...
