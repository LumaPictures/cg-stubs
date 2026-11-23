import subprocess
from collections.abc import Generator
from pdgjob import pdgjson as pdgjson

from typing import TypeAlias
from typing import TypeAlias
_WorkItem: TypeAlias = pdgjson.WorkItem | pdgjson.NativeWorkItem
def PipedLineGenerator(popen: subprocess.Popen[bytes]) -> Generator[bytes, None, None]: ...
def cook(work_item: _WorkItem, hfs: str = '$HFS') -> bool: ...
