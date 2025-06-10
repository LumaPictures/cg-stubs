from _typeshed import Incomplete
from maya.app.renderSetup.lightEditor.model.editor import LightEditor as LightEditor
from maya.app.renderSetup.lightEditor.model.group import LightGroup as LightGroup
from maya.app.renderSetup.lightEditor.model.item import LightItemBase as LightItemBase
from maya.app.renderSetup.lightEditor.model.light import LightItem as LightItem

kRegisterFailed: Incomplete
kUnregisterFailed: Incomplete
nodeTypes: Incomplete
invisibleNodeTypes: Incomplete

def initialize(mplugin) -> None: ...
def uninitialize(mplugin) -> None: ...
