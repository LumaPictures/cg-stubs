from hutil.Qt import QtWidgets

class uiParamOperator(QtWidgets.QWidget):
    default_operator: str
    current_operator: str
    operator_dialog: str
    def __init__(self, label: str | None, default_operator: str = '', operator_dialog: str = 'Choose Operator') -> None: ...
