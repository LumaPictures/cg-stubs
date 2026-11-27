import hou
from PySide6.QtWidgets import QWidget

class TemplatePickerDialog:
    applied: bool
    # Menu tokens of the node's templatename / templatemapping parms.
    selected_template: str
    selected_mapping: str
    # The autorig builder SOP (autorigtool / autorigsubtools pass their node manager's node).
    def __init__(self, node: hou.SopNode, parent: QWidget | None = ..., lock_template: bool = ...) -> None: ...
