# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import AssetAPI as AssetAPI
import NodegraphAPI as NodegraphAPI
import Nodes2DAPI as Nodes2DAPI
import Utils as Utils
from _typeshed import Incomplete
from typing import Set, Tuple

def CalculateInOut(node: Nodes2DAPI.Node2D): ...
def GetChannelNames(node: NodegraphAPI.Node, time: Incomplete | None = ...): ...
def GetDiskFrameRange(fileName, diskOnly: bool = ...): ...
def GetFileInSequence(node: NodegraphAPI.Node, time: Incomplete | None = ...): ...
def ResetToDefaultChannelMapping(node: NodegraphAPI.Node): ...
