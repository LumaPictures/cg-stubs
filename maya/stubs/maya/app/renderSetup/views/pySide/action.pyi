from PySide6.QtGui import QAction
from _typeshed import Incomplete
from collections.abc import Generator
from contextlib import contextmanager

@contextmanager
def excepthookGuard(consumer) -> Generator[None]: ...

class Action(QAction):
    exceptionRaised: Incomplete
    def excepthook(self, type, value, traceback) -> None: ...
    def trigger(self) -> None: ...
