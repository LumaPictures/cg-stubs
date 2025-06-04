from _typeshed import Incomplete
from maya import cmds as cmds

ROOT_NAMESPACE: str

class NamespaceGuard:
    namespace: Incomplete
    previous: Incomplete
    isSame: Incomplete
    def __init__(self, namespace) -> None: ...
    def __enter__(self) -> None: ...
    def __exit__(self, type: type[BaseException] | None, value: BaseException | None, traceback: types.TracebackType | None) -> None: ...

def guard(name): ...

root: Incomplete

def RootNamespaceGuard(): ...
