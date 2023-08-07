# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import UI4.FormMaster.EnableableParameterPolicy as EnableableParameterPolicy
import UI4.FormMaster.HintsDelegate as HintsDelegate
import UI4.FormMaster.ParameterPolicy as ParameterPolicy
from UI4.FormMaster.NodeHints.Common2D import AddCommon2DToNodeHints as AddCommon2DToNodeHints, GetFgBgCombinerStringDict as GetFgBgCombinerStringDict, GetNormalizedCenterNumberDict as GetNormalizedCenterNumberDict
from typing import Set, Tuple

_NodeHints: dict
_NodeName: str
