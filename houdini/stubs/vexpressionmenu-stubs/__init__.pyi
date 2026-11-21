import hou
import re
from collections.abc import Sequence
from houtypes import ParmMenuScriptKwargs

def installInitialSnippets() -> None:
    """ Copies the initial snippets into _vexsnippets and adds
        the comment prefix.
    """
def ensureSnippetsAreLoaded() -> None: ...
def buildSnippetMenu(snippetname: str, multiparm_indices: Sequence[int] = ..., kwargs: ParmMenuScriptKwargs = ...) -> list[str]:
    """ Given a snippetname, determine what
        snippets should be generated.
        Optionally provide the kwargs dict to extend the list with available recipes.
    """
def buildSingleLineSnippetMenu(snippetname: str, multiparm_indices: Sequence[int] = ..., kwargs: ParmMenuScriptKwargs = ...) -> list[str]:
    """ Given a snippetname, determine what
        snippets should be generated.
        Optionally provide the kwargs dict to extend the list with available recipes.
    """

chcalls: list[str]
chcall_exp: re.Pattern[str]
ch_size: dict[str, int]
comment_or_string_exp: re.Pattern[str]

def remove_comments(match: re.Match[str]) -> str: ...
def createSpareParmsFromOCLBindings(node: hou.OpNode, parmname: str) -> None:
    """ 
    Parse the @BIND commands in an OpenCL kernel and create corresponding
    spare parameters
    """
def createSpareParmsFromChCalls(node: hou.OpNode, parmname: str) -> None:
    """
    For each ch() call in the given parm name, create a corresponding spare
    parameter on the node.
    """
