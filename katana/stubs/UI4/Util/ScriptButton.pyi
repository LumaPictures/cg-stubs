# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import UI4.Widgets.MessageBox as MessageBox
import Utils as Utils
from typing import Set, Tuple

def ExecScript(valuePolicy, buttonText, scriptText): ...
def GetButtonAndScriptText(valuePolicy): ...
