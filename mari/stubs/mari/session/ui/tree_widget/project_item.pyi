from .mari_entity_item import MariEntityTreeWidgetItem as MariEntityTreeWidgetItem
from _typeshed import Incomplete

class ProjectTreeWidgetItem(MariEntityTreeWidgetItem):
    imagePath: Incomplete
    pixmap: Incomplete
    def updateIcons(self) -> None: ...
