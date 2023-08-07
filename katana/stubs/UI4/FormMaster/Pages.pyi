# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyQt5.QtCore as QtCore
from typing import Set, Tuple

class PageEntry:
    def __init__(self, name, fullname, childnames, subpages) -> None: ...

def ProcessPageEntryList(entries): ...
def SortByPage(names, getPageFnc, includeUnpaged: bool = ...): ...
