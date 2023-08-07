# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import UI4 as UI4
from _typeshed import Incomplete
from typing import Set, Tuple

POLICY_STATE_CURVE_FLOATING: int
POLICY_STATE_CURVE_KEY: int
POLICY_STATE_CURVE_NO_KEY: int
POLICY_STATE_DEFAULT: int
POLICY_STATE_EXPRESSION: int
POLICY_STATE_LOCKED: int
POLICY_STATE_NORMAL: int

def GetPolicyState(valuePolicy): ...
def GetPolicyStateColor(state: Incomplete | None = ...): ...
