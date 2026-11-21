# Houdini stubs generated from Houdini 22.0.466

import threading
from pdgjob import pdgcmd as pdgcmd, pdgjson as pdgjson
from typing import Any

from typing import TypeAlias
from typing import TypeAlias
_WorkItem: TypeAlias = pdgjson.WorkItem | pdgjson.NativeWorkItem
class SimTrackerThread(threading.Thread):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...

def initTracker(work_item: _WorkItem, port: int, webport: int, verbosity: bool, use_ip: bool) -> None: ...
def stopTracker(tracker_host: str, tracker_port: int) -> None: ...
def cook(work_item: _WorkItem) -> None: ...
