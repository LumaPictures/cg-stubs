# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

from QT4FormWidgets.FormWidget import AlignChildLabelWidths as AlignChildLabelWidths, AlignLeftControlWidths as AlignLeftControlWidths, FormWidget as FormWidget, ScrubbingStates as ScrubbingStates

__init__: list

class NullFormWidget(FormWidget):
    def __init__(self, parent, policy, factory): ...
    def _participatesInLabelAlignment(self): ...
    def setVisible(self, state, checkVisOps: bool = ...): ...