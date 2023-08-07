# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

from . import PolicyHelpers as PolicyHelpers
from UI4.FormMaster.Editors.Layers.LayerWithTransform import LayerWithTransform as LayerWithTransform
from UI4.FormMaster.Editors.Layers.PolicyHelpers import GetPolicyState as GetPolicyState, GetPolicyStateColor as GetPolicyStateColor
from typing import Set, Tuple

POLICY_STATE_CURVE_FLOATING: int
POLICY_STATE_CURVE_KEY: int
POLICY_STATE_CURVE_NO_KEY: int
POLICY_STATE_DEFAULT: int
POLICY_STATE_EXPRESSION: int
POLICY_STATE_LOCKED: int
POLICY_STATE_NORMAL: int
