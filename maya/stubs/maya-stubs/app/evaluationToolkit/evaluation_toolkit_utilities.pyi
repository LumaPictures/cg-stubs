__all__ = ['section_layout', 'set_gpu_override_active', 'BUTTON_WIDTH', 'COLUMN_SPACING', 'ROW_SPACING', 'FILE_TEXT_FIELD_WIDTH', 'EvaluationToolkitSection', 'EvaluationToolkitSubsection']

BUTTON_WIDTH: int
COLUMN_SPACING: int
ROW_SPACING: int
FILE_TEXT_FIELD_WIDTH: int

class EvaluationToolkitSection:
    def update_ui(self) -> None: ...

class EvaluationToolkitSubsection:
    def update_ui(self) -> None: ...

def section_layout(start_closed): ...
def set_gpu_override_active(state) -> None: ...
