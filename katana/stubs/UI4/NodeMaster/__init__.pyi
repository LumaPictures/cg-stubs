# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyUtilModule.UserNodes as UserNodes
from . import NodeInteractionDelegateManager as NodeInteractionDelegateManager, NodeInteractionDelegates as NodeInteractionDelegates
from typing import Set, Tuple

_Initialized: bool

def Initialize(): ...
