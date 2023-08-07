# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyQt5.QtGui as QtGui
from typing import Set, Tuple

def MakeGlobalContextCurrent() -> bool: ...
