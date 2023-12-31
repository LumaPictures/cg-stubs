from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from ._particle_transfer import *
from _typeshed import Incomplete

version: str
CHANNEL_TRANSFER_USER_ROLE: int

class ChannelOptionsTab(OptionsTab):
    sourceChannelsChanged: Incomplete
    source_list: Incomplete
    transfer_list: Incomplete
    destination_size_label: Incomplete
    destination_size: Incomplete
    destination_size_index: int
    def __init__(self, parent: Incomplete | None = ...) -> None: ...
    def sourceChannels(self): ...
    def destinationSize(self): ...

class ChannelTransferDialog(TransferDialog):
    options_tab: Incomplete
    advanced_options_tab: Incomplete
    def __init__(self, parent: Incomplete | None = ...) -> None: ...

class ChannelTransferListWidgetItem(QListWidgetItem):
    def __init__(self, channel) -> None: ...
    def channel(self): ...

class ChannelTransferListWidget(QListWidget):
    def __init__(self) -> None: ...
    def populateChannels(self, channels) -> None: ...
    def showAll(self) -> None: ...
    def showSelected(self, source) -> None: ...
    def hideSelected(self) -> None: ...
    def hideAll(self) -> None: ...
    def channels(self): ...

def showDialog() -> None: ...

transfer: Incomplete
