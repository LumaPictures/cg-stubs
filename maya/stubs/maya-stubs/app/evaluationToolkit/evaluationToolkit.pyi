from _typeshed import Incomplete

__all__ = ['OpenEvaluationToolkitUI']

class EvaluationToolkit:
    windowTitle: Incomplete
    windowName: Incomplete
    sections: Incomplete
    def __init__(self, windowName=...) -> None: ...
    checkboxUseSystemGraphviz: Incomplete
    evaluationModeList: Incomplete
    checkboxGPUOverride: Incomplete
    checkboxControllerPrepopulate: Incomplete
    layoutModesAdvanced: Incomplete
    checkboxManipulation: Incomplete
    checkboxManipulationPrevalidation: Incomplete
    checkboxReduceGraphRebuild: Incomplete
    idleActionList: Incomplete
    layoutEvaluators: Incomplete
    dynamicsModeList: Incomplete
    layoutDynamicsAdvanced: Incomplete
    listDynamics: Incomplete
    checkboxTransitiveReductionFullGraph: Incomplete
    checkboxMarkClusters: Incomplete
    cyclesList: Incomplete
    fieldCycleSizeThreshold: Incomplete
    textfieldSourceNode: Incomplete
    textfieldDestinationNode: Incomplete
    checkboxOnlyShortestPath: Incomplete
    checkboxTransitiveReductionCycleGraph: Incomplete
    upstreamNodesList: Incomplete
    downstreamNodesList: Incomplete
    checkboxTransitiveReductionDependenciesGraph: Incomplete
    performance_result_fields: Incomplete
    correctness_result_fields: Incomplete
    checkboxReports: Incomplete
    checkboxFreezePropagation: Incomplete
    freezeDownstreamModeList: Incomplete
    freezeUpstreamModeList: Incomplete
    checkboxFreezeInvisible: Incomplete
    schedulingTypeList: Incomplete
    nodeTypesList: Incomplete
    invisibilityModeList: Incomplete
    invisibilityInvalidateButton: Incomplete
    layoutInvisibilityAdvanced: Incomplete
    invisibilityNotificationModeList: Incomplete
    motionTrailsManipCheckbox: Incomplete
    motionTrailsInvalidateButton: Incomplete
    scriptJobDeleteAll: Incomplete
    scriptJobDbTraceChanged: Incomplete
    scriptJobCustomEvaluatorChanged: Incomplete
    scriptJobFreezeOptionsChanged: Incomplete
    def create(self) -> None: ...
    def updateUI(self) -> None: ...

def OpenEvaluationToolkitUI(): ...
