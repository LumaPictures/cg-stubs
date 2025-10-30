from .pyproject_json import write_pyproject_json as write_pyproject_json
from .pyproject_toml import write_pyproject_toml as write_pyproject_toml
from dataclasses import dataclass
from enum import Enum
from pathlib import Path

_WIDGET_MAIN: str
_WIDGET_IMPORTS: str
_WIDGET_CLASS_DEFINITION: str
_WIDGET_SETUP_UI_CODE: str
_MAINWINDOW_FORM: str
_QUICK_FORM: str
_QUICK_MAIN: str
NewProjectFiles = list[tuple[str, str]]

@dataclass(frozen=True)
class NewProjectType:
    command: str
    description: str
    files: NewProjectFiles

def _write_project(directory: Path, files: NewProjectFiles, legacy_pyproject: bool): ...
def _widget_project() -> NewProjectFiles: ...
def _ui_form_project() -> NewProjectFiles: ...
def _qml_project() -> NewProjectFiles: ...

class NewProjectTypes(Enum):
    QUICK = ...
    WIDGET_FORM = ...
    WIDGET = ...
    @staticmethod
    def find_by_command(command: str) -> NewProjectType | None: ...

def new_project(project_dir: Path, project_type: NewProjectType, legacy_pyproject: bool) -> int: ...
