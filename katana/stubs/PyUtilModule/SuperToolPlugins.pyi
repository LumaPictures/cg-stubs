# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import KatanaResources as KatanaResources
import NodegraphAPI as NodegraphAPI
import Nodes3DAPI as Nodes3DAPI
import Utils as Utils
from typing import Set, Tuple

def GetSuperToolPluginEditor(name): ...
def GetSuperToolPluginNode(name): ...
def LoadSuperToolPlugins(loadEditors: bool = ...): ...
