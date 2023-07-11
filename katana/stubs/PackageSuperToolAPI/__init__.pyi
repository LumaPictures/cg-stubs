# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

from . import BaseNode as BaseNode, NodeUtils as NodeUtils, Packages as Packages
from typing import Set, Tuple

def IsUIMode() -> bool: ...
