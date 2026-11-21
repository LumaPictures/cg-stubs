# Houdini stubs generated from Houdini 22.0.466

import re
from bookish import paths as paths

PREFIX: str
LANG_REGEX: re.Pattern[str]

def has_lang(path: str) -> bool: ...
def split_lang_and_path(path: str) -> tuple[str, str]:
    '''
    Takes a language-aware path and returns two strings: the language name and
    the language-naive path. For example, `split_lang_and_path("/+en/foo")`
    returns a tuple of `"en"` and `"/foo"`.
    '''
def lang_name(path: str) -> str: ...
def is_lang_root(path: str) -> bool:
    '''
    Returns True if the given path refers to a language root (and NOT anything
    under the language root). For example `"/+en"` or `"/+jp/"`.
    '''
def delang(path: str) -> str:
    '''
    Takes a language-aware path (e.g. `"/+en/foo/bar"`) and returns the
    equivalent language-naive path (e.g. `"/foo/bar"`).
    '''
def safe_delang(path: str) -> str: ...
def enlang(name: str, path: str) -> str:
    '''
    Takes a language name and a language-naive path (for example, `"en"` and
    `"/foo/bar"`) and returns the equivalent language-aware path (e.g.
    `"/+en/foo/bar"`).
    '''
