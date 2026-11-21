# Houdini stubs generated from Houdini 22.0.466

from collections.abc import Iterable, Sequence
from houtypes import ParmMenuScriptKwargs

def ensureExpressionsAreLoaded() -> None: ...
def buildExpressionsMenu(snippetnames: str | Iterable[str], multiparm_indices: Sequence[int] = ..., kwargs: ParmMenuScriptKwargs = ...) -> list[str]:
    """ Given a snippetname, determine what snippets should be generated.
        The snippetname can be a single string or an iterable of strings.
    """
