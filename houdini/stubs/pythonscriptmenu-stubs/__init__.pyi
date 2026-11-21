from collections.abc import Sequence
from houtypes import ParmMenuScriptKwargs

def ensureSnippetsAreLoaded() -> None: ...
def buildSnippetMenu(snippetname: str, multiparm_indices: Sequence[int] = ..., kwargs: ParmMenuScriptKwargs = ...) -> list[str]:
    """ Given a snippetname, determine what
        snippets should be generated
    """
def buildSingleLineSnippetMenu(snippetname: str, multiparm_indices: Sequence[int] = ..., kwargs: ParmMenuScriptKwargs = ...) -> list[str]:
    """ Given a snippetname, determine what
        snippets should be generated
    """
