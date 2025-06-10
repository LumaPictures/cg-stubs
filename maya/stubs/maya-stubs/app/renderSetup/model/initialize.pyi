from _typeshed import Incomplete
from maya.app.renderSetup.model.applyOverride import getAllApplyOverrideClasses as getAllApplyOverrideClasses
from maya.app.renderSetup.model.collection import getAllCollectionClasses as getAllCollectionClasses
from maya.app.renderSetup.model.group import getAllGroupClasses as getAllGroupClasses
from maya.app.renderSetup.model.overrideUtils import getAllOverrideClasses as getAllOverrideClasses
from maya.app.renderSetup.model.renderLayer import RenderLayer as RenderLayer
from maya.app.renderSetup.model.selector import BasicSelector as BasicSelector, LightsCollectionSelector as LightsCollectionSelector, Selector as Selector, SimpleSelector as SimpleSelector

nodeTypes: Incomplete
renderSetupNodeNamesToShowInOutliner: Incomplete
commands: Incomplete
syntaxCommands: Incomplete
nodeDragAndDropBehaviors: Incomplete

def setVisibilityNodes(val, nodeTypeNamesList) -> None: ...
def initialize(mplugin) -> None: ...
def uninitialize(mplugin) -> None: ...
