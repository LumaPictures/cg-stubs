from .mari_entity_item import MariEntityTreeWidgetItem as MariEntityTreeWidgetItem
from _typeshed import Incomplete

class ProjectorTreeWidgetItem(MariEntityTreeWidgetItem):
    imagePath: Incomplete
    pixmap: Incomplete
    def __init__(self, parent, mariEntity, dragEnabled: bool = ..., dropEnabled: bool = ..., selectable: bool = ..., userCheckable: bool = ..., tristate: bool = ...) -> None: ...
