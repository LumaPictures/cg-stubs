import _substance_painter.resource
import enum
import typing
from _typeshed import Incomplete

class ResourceLocation(enum.Enum):
    SESSION: Incomplete
    PROJECT: Incomplete
    SHELF: Incomplete

class ResourceID:
    context: str
    name: str
    version: str
    @classmethod
    def from_url(cls, url: str): ...
    @classmethod
    def from_project(cls, name: str, version: str = ...): ...
    @classmethod
    def from_session(cls, name: str, version: str = ...): ...
    def url(self) -> str: ...
    def location(self) -> ResourceLocation: ...
    def __init__(self, context, name, version) -> None: ...

class Usage(enum.Enum):
    BASE_MATERIAL: Incomplete
    ENVIRONMENT: Incomplete
    ALPHA: Incomplete
    TEXTURE: Incomplete
    FILTER: Incomplete
    EMITTER: Incomplete
    RECEIVER: Incomplete
    PROCEDURAL: Incomplete
    BRUSH: Incomplete
    PARTICLE: Incomplete
    TOOL: Incomplete
    SHADER: Incomplete
    EXPORT: Incomplete
    GENERATOR: Incomplete
    SMART_MATERIAL: Incomplete
    SMART_MASK: Incomplete
    COLOR_LUT: Incomplete

class Type(enum.Enum):
    SCRIPT: Incomplete
    PRESET: Incomplete
    SMART_MASK: Incomplete
    IMAGE: Incomplete
    SUBSTANCE: Incomplete
    SHADER: Incomplete
    EXPORT: Incomplete
    SMART_MATERIAL: Incomplete
    BRUSH: Incomplete
    RESOURCE: Incomplete
    SUBSTANCE_PACKAGE: Incomplete
    ABR_PACKAGE: Incomplete

class Resource:
    handle: _substance_painter.resource.ResourceHandle
    def __eq__(self, other): ...
    def __hash__(self): ...
    def identifier(self) -> ResourceID: ...
    def location(self) -> ResourceLocation: ...
    @staticmethod
    def retrieve(identifier: ResourceID): ...
    def set_custom_preview(self, preview_image: str) -> None: ...
    def category(self) -> str: ...
    def usages(self) -> typing.List[Usage]: ...
    def gui_name(self) -> str: ...
    def type(self) -> Type: ...
    def tags(self) -> typing.List[str]: ...
    def internal_properties(self) -> dict: ...
    def children(self) -> typing.List['Resource']: ...
    def parent(self) -> typing.Optional['Resource']: ...
    def reset_preview(self) -> None: ...
    def show_in_ui(self) -> None: ...
    def __init__(self, handle) -> None: ...

def show_resources_in_ui(resources: typing.List[Resource]) -> None: ...
def import_project_resource(file_path: str, resource_usage: Usage, name: str = ..., group: str = ...) -> Resource: ...
def import_session_resource(file_path: str, resource_usage: Usage, name: str = ..., group: str = ...) -> Resource: ...

class StandardQuery:
    ALL_RESOURCES: str
    PROJECT_RESOURCES: str
    SESSION_RESOURCES: str
    SHELVES_RESOURCES: str

def search(query: str) -> typing.List[Resource]: ...
def list_layer_stack_resources() -> typing.List[ResourceID]: ...
def update_layer_stack_resource(old_resource_id: ResourceID, new_resource: Resource) -> typing.List[ResourceID]: ...

class Shelf:
    def name(self) -> str: ...
    def path(self) -> str: ...
    def resources(self, query: str = ...) -> typing.List[Resource]: ...
    def can_import_resources(self) -> bool: ...
    def import_resource(self, file_path: str, resource_usage: Usage, name: str = ..., group: str = ..., uuid: str = ...) -> Resource: ...
    def is_crawling(self) -> bool: ...
    def __init__(self, _name) -> None: ...

class Shelves:
    @staticmethod
    def all() -> typing.List[Shelf]: ...
    @staticmethod
    def exists(name: str) -> bool: ...
    @staticmethod
    def add(name: str, path: str) -> Shelf: ...
    @staticmethod
    def remove(name: str): ...
    @staticmethod
    def refresh_all() -> None: ...
    @staticmethod
    def user_shelf() -> Shelf: ...
    @staticmethod
    def application_shelf() -> Shelf: ...
