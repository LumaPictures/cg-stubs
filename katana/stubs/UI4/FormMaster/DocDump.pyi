# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import ConfigurationAPI_cmodule as Configuration
import NodegraphAPI as NodegraphAPI
from UI4.FormMaster.ParameterPolicy import CreateParameterPolicy as CreateParameterPolicy
from _typeshed import Incomplete
from typing import Set, Tuple

def DocDump(names: Incomplete | None = ..., outputdir: Incomplete | None = ...): ...
def DoxyTemplate(name, outputdir): ...
def DumpHelp(policy, indent: int = ...): ...
