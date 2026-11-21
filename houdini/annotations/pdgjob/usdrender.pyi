import subprocess
from collections.abc import Generator
from typing import TypeAlias

from pdgjob import pdgjson

_WorkItem: TypeAlias = pdgjson.WorkItem | pdgjson.NativeWorkItem

def PipedLineGenerator(popen: subprocess.Popen[bytes]) -> Generator[bytes, None, None]: ...
def cook(work_item: _WorkItem, hfs: str = ...) -> bool: ...
