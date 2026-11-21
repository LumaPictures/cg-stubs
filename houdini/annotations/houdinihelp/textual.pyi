from bookish.wiki.wikipages import WikiPages, _WikiBlock
from pygments.lexer import RegexLexer

ver_major: str
ver_minor: str
ver_build: str
houdini_version: str | None
env_var_help: dict[str, str] | None
load_time: float | None

class MinConfig:
    USE_HOU: bool
    HOUDINI_VERSION_MAJOR: str
    HOUDINI_VERSION_MINOR: str
    HOUDINI_VERSION_BUILD: str
    INDEX_DIR: str
    CACHE_DIR: str
    TEXTIFY_CLASS: str
    WIKI_STYLE: str
    TEMPLATE: str
    LEXERS: dict[str, type[RegexLexer]]
    SUPPORT_DOCUMENTS: list[dict[str, str]]
    DOCUMENTS: list[str | dict[str, str | dict[str, str]]]

def wikiPages() -> WikiPages: ...
def textify(blocks: list[_WikiBlock] | tuple[_WikiBlock, ...], width: int = ...) -> str: ...
def parseEnvVarWiki() -> dict[str, str]: ...
def textifiedHelp(path: str) -> str | None: ...
def commandTextHelp(name: str) -> str | None: ...
def expressionTextHelp(name: str) -> str | None: ...
def configTextHelp(name: str) -> str: ...
def allConfigTextHelp() -> dict[str, str]: ...
