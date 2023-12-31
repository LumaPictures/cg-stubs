from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from ._particle_transfer import *
from _typeshed import Incomplete

version: str
SOURCE_LAYER_TRANSFER_USER_ROLE: int
DESTINATION_LAYER_TRANSFER_USER_ROLE: Incomplete

class LayerOptionsTab(OptionsTab):
    sourceLayersChanged: Incomplete
    source_channel: Incomplete
    destination_channel: Incomplete
    source_tree: Incomplete
    transfer_tree: Incomplete
    def __init__(self, parent: Incomplete | None = ...) -> None: ...
    def sourceChannel(self): ...
    def destinationChannel(self): ...
    def sourceLayers(self): ...
    def createIncompleteGroups(self, source_layers, destination_layers, destination_channel, destination_version_name) -> None: ...

class LayerTransferDialog(TransferDialog):
    options_tab: Incomplete
    advanced_options_tab: Incomplete
    def __init__(self, parent: Incomplete | None = ...) -> None: ...

class LayerTransferTreeWidgetItem(QTreeWidgetItem):
    def __init__(self, source_layer) -> None: ...
    def sourceLayer(self): ...
    def destinationLayer(self): ...
    def hasSelectedChildren(self): ...
    def hasHiddenChildren(self): ...
    def isIncompleteGroup(self): ...
    def showAll(self) -> None: ...
    def showSelected(self, source) -> None: ...
    def hideSelected(self) -> None: ...
    def hideAll(self) -> None: ...
    def sourceLayers(self): ...
    def createEmptyIncompleteGroups(self, source_layers, destination_layers, destination_parent_stack, destination_version_name) -> None: ...
    def populateIncompleteGroups(self) -> None: ...
    def moveIncompleteGroups(self, parent_stack, ref_layer) -> None: ...

class LayerTransferTreeWidget(QTreeWidget):
    def __init__(self, parent: Incomplete | None = ...) -> None: ...
    def populateSourceLayers(self, source_channel) -> None: ...
    def showAll(self) -> None: ...
    def showSelected(self, source) -> None: ...
    def hideSelected(self) -> None: ...
    def hideAll(self) -> None: ...
    def sourceLayers(self): ...
    def createIncompleteGroups(self, source_layers, destination_layers, destination_channel, destination_version_name) -> None: ...

def showDialog() -> None: ...

transfer: Incomplete
