# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

from . import Manifest as Manifest, Utility as Utility
from NodeGraphView.Utility import CreateNodeAtActiveConnection as CreateNodeAtActiveConnection, FitBackdropAroundNodes as FitBackdropAroundNodes, UpdateShadingGroupConnection as UpdateShadingGroupConnection
from typing import Set, Tuple

NodeAdded: int
NodeDimmingModeConnected: int
NodeDimmingModeContributing: int
NodeDisconnected: int
NodeEdited: int
NodeUnchanged: int
NodeViewStateCount: int
