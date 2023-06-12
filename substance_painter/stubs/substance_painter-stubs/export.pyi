import typing
from _typeshed import Incomplete

from _substance_painter.export import ExportStatus as ExportStatus

def list_project_textures(json_config: dict) -> typing.Dict[typing.Tuple[str, str], typing.List[str]]: ...

class TextureExportResult:
    status: ExportStatus
    message: str
    textures: typing.Dict[typing.Tuple[str, str], typing.List[str]]
    def __init__(self, status, message, textures) -> None: ...

def export_project_textures(json_config: dict) -> TextureExportResult: ...
