# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import UI4.FormMaster.EnableableParameterPolicy as EnableableParameterPolicy
import UI4.FormMaster.HintsDelegate as HintsDelegate
import UI4.FormMaster.ParameterPolicy as ParameterPolicy
from UI4.FormMaster.NodeHints.Common2D import AddCommon2DToNodeHints as AddCommon2DToNodeHints
from typing import Set, Tuple

AnisotropicParamHints: dict
BorderExtendParamHints: dict
BorderOverscanParamHints: dict
ClampOutputParamHints: dict
FilterParamHints: dict
GroupFilterParamHints: dict
HighlightCompensationParamHints: dict
_NodeHints: dict
_NodeName: str
