import dataclasses
import substance_painter.resource
import substance_painter.textureset
from _typeshed import Incomplete

from _substance_painter.export import ExportStatus as ExportStatus

def list_project_textures(json_config: dict) -> dict[tuple[str, str], list[str]]: ...

@dataclasses.dataclass(frozen=True)
class TextureExportResult:
    status: ExportStatus
    message: str
    textures: dict[tuple[str, str], list[str]]

def export_project_textures(json_config: dict) -> TextureExportResult: ...
def get_default_export_path() -> str: ...

@dataclasses.dataclass(frozen=True)
class PredefinedExportPreset:
    name: str
    url: str
    def list_output_maps(self, stack: substance_painter.textureset.Stack) -> list: ...

def list_predefined_export_presets() -> list[PredefinedExportPreset]: ...

@dataclasses.dataclass(frozen=True)
class ResourceExportPreset:
    resource_id: substance_painter.resource.ResourceID
    def list_output_maps(self) -> list: ...

def list_resource_export_presets() -> list[ResourceExportPreset]: ...

from _substance_painter.export import MeshExportOption as MeshExportOption

def scene_is_triangulated() -> bool: ...
def scene_has_tessellation() -> bool: ...

@dataclasses.dataclass(frozen=True)
class MeshExportResult:
    status: ExportStatus
    message: str

def export_mesh(file_path: str, option: MeshExportOption) -> MeshExportResult: ...
