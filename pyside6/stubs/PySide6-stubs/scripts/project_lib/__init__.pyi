from .design_studio_project import DesignStudioProject as DesignStudioProject
from .newproject import NewProjectTypes as NewProjectTypes, new_project as new_project
from .project_data import ProjectData as ProjectData, QmlProjectData as QmlProjectData, check_qml_decorators as check_qml_decorators, is_python_file as is_python_file
from .pyproject_json import parse_pyproject_json as parse_pyproject_json
from .pyproject_toml import migrate_pyproject as migrate_pyproject, parse_pyproject_toml as parse_pyproject_toml, write_pyproject_toml as write_pyproject_toml
from .utils import package_dir as package_dir, qt_metatype_json_dir as qt_metatype_json_dir, qtpaths as qtpaths, remove_path as remove_path, requires_rebuild as requires_rebuild, resolve_valid_project_file as resolve_valid_project_file, run_command as run_command
from _typeshed import Incomplete
from dataclasses import dataclass

QTPATHS_CMD: str
MOD_CMD: str
PYPROJECT_TOML_PATTERN: str
PYPROJECT_JSON_PATTERN: str
PYPROJECT_FILE_PATTERNS: Incomplete
QMLDIR_FILE: str
QML_IMPORT_NAME: str
QML_IMPORT_MAJOR_VERSION: str
QML_IMPORT_MINOR_VERSION: str
QT_MODULES: str
METATYPES_JSON_SUFFIX: str
TRANSLATION_SUFFIX: str
SHADER_SUFFIXES: Incomplete

class Singleton(type):
    _instances: Incomplete
    def __call__(cls, *args, **kwargs): ...

@dataclass(frozen=True)
class ClOptions(metaclass=Singleton):
    dry_run: bool
    quiet: bool
    force: bool
    qml_module: bool
