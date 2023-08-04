# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

from _typeshed import Incomplete
from typing import Set, Tuple

def GetParser(): ...
def ParseAndBuildHintDict(inputString, prefix: str = ..., secondaryPrefix: Incomplete | None = ...): ...
