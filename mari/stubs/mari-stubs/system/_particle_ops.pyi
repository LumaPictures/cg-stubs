import PySide2
from _typeshed import Incomplete

version: str

class ParticleOpDialog(PySide2.QtWidgets.QDialog):
    op_widget: Incomplete
    ok_button: Incomplete
    cancel_button: Incomplete
    def __init__(self, op_name, parent: Incomplete | None = ...) -> None: ...
    def op(self): ...

def showDialog(op_name) -> None: ...

action_set: str
op_names: Incomplete
op_action: Incomplete
