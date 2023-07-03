# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import QT4FormWidgets.FWidget
import ResourceFiles as ResourceFiles
from QT4FormWidgets.FWidget import FBoxLayout as FBoxLayout, FButton as FButton, FDisclosureTriangle as FDisclosureTriangle, FLabel as FLabel, FLockIcon as FLockIcon, FMenu as FMenu, FPixmap as FPixmap, FSpacer as FSpacer, FStateBadge as FStateBadge, FSvgIcon as FSvgIcon, FToggleStateBadge as FToggleStateBadge, FWidget as FWidget
from ResourceFiles.IconManager import ResourceManager as ResourceManager

class EditWrench(QT4FormWidgets.FWidget.FMenu):
    def __init__(self, parent): ...
    def fillMenu(self, menu): ...