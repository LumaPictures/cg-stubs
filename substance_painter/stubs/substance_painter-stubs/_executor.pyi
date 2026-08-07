from . import event as event
from _typeshed import Incomplete

class ProjectExecutor:
    """
    Execute code at specific project dependant times.
    """
    def __init__(self, dispatcher) -> None: ...
    def execute_when_not_busy(self, callback) -> None:
        """
        Execute code when the application is not in a busy state.
        """

PROJECT_EXECUTOR: Incomplete
