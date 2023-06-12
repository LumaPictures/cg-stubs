# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import NodegraphAPI.NodeExtensions as NodeExtensions
import NodegraphAPI as NodegraphAPI
import NodegraphAPI.NodegraphGlobals as NodegraphGlobals
import NodegraphAPI.Util as Util
import Utils as Utils
from _typeshed import Incomplete

AllChangeEventTypes: set
EventType_nodegraph_changed: str
EventType_nodegraph_changed_affects2DRender: str
NodeActivationChangeEventTypes: set
NodeGraphLoadBeginEventTypes: set
NodeGraphLoadEndEventTypes: set
NodePortChangeEventTypes: set
ParameterChangeEventTypes: set
PortConnectionChangeEventTypes: set
__filter_nodegraph_changed_affects2DRender_contributingNodes: None
__filter_nodegraph_changed_affects2DRender_isEnabled: bool
__filter_nodegraph_changed_affects2DRender_isLoading: bool
__filter_nodegraph_changed_affects2DRender_isThrottled: bool

def DoesNodeEffectViewNodes(node) -> bool: ...
def __filter_nodegraph_changed(eventType, eventID, **kwargs): ...
def __filter_nodegraph_changed_affects2DRender(eventType, eventID, **kwargs): ...
def __on_event_idle(eventType, eventID, **kwargs): ...
def __on_node_setViewed(eventType, eventID, node: Incomplete | None = ...): ...