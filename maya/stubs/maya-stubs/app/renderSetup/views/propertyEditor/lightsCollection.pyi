from maya.app.renderSetup.views.propertyEditor.collectionPropertyEditorStrings import *
import maya.app.renderSetup.views.propertyEditor.collection as collection

hSpc: int

class LightsCollection(collection.Collection):
    def __init__(self, item, parent) -> None: ...
    def postSelector(self) -> None: ...
