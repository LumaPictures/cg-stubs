# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import NodeGraphView.Manifest as Manifest
import NodeGraphView.Utility as Utility
from NodeGraphView.Utility import CreateNodeAtActiveConnection as CreateNodeAtActiveConnection, FitBackdropAroundNodes as FitBackdropAroundNodes, UpdateShadingGroupConnection as UpdateShadingGroupConnection

NodeAdded: int
NodeDimmingModeConnected: int
NodeDimmingModeContributing: int
NodeDisconnected: int
NodeEdited: int
NodeUnchanged: int
NodeViewStateCount: int