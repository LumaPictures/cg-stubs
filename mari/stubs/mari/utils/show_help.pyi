from _typeshed import Incomplete

class CustomHelp:
    def __new__(cls): ...
    def getURL(self, obj): ...
    def __call__(self, obj: Incomplete | None = ...) -> None: ...

def getAutoCompletionCandidates(expression): ...

help: Incomplete