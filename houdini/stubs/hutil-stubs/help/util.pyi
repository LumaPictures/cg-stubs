import pathlib
from typing import Any, Collection

def find_object(name: str, blacklist: Collection[str] | None = None, whitelist: Collection[str] | None = None) -> Any:
    '''
    Imports and returns an object given a fully qualified name.

    >>> find_object("whoosh.analysis.StopFilter")
    <class \'whoosh.analysis.StopFilter\'>
    '''
def expandpath(path: pathlib.Path | str) -> pathlib.Path: ...
