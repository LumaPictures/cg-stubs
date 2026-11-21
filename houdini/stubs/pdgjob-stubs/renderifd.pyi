# Houdini stubs generated from Houdini 22.0.466

from pdgjob import pdgcmd as pdgcmd, pdgjson as pdgjson

from typing import TypeAlias
from typing import TypeAlias
_WorkItem: TypeAlias = pdgjson.WorkItem | pdgjson.NativeWorkItem
def cook(work_item: _WorkItem, hfs: str = '$HFS') -> bool: ...
