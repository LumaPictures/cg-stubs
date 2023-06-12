# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"


NodegraphEventTypes: dict
kManualUpdateEventsKey: int
kNodePortChangeEventsKey: int
kNodegraphEventsKey: int
kParamChangedEventsKey: int
kParamPenUpEventsExclusionsKey: int
kPortConnectionEventsKey: int

def GetNodegraphEventTypes(): ...