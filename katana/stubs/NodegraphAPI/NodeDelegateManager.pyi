# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import NodegraphAPI as NodegraphAPI
from typing import Set, Tuple

_SuperDelegates: list

class SuperDelegate:
    def processNodeCreate(self, node): ...

def ProcessNodeCreate(node): ...
def RegisterSuperDelegate(delegate): ...
