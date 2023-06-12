from . import event as event
from _typeshed import Incomplete

class ProjectExecutor:
    def __init__(self, dispatcher) -> None: ...
    def execute_when_not_busy(self, callback) -> None: ...

PROJECT_EXECUTOR: Incomplete
