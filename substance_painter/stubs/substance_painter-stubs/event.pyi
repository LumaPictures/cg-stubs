import dataclasses
import datetime
import enum
from typing import Union
from substance_painter.async_utils import StopSource as StopSource
from substance_painter.baking import BakingStatus as BakingStatus
from substance_painter.export import ExportStatus as ExportStatus
from substance_painter.textureset import ChannelType as ChannelType
from typing import Any, Callable

@dataclasses.dataclass(frozen=True)
class Event: ...

@dataclasses.dataclass(frozen=True)
class _TestEvent(Event):
    message: str

@dataclasses.dataclass(frozen=True)
class _DunamisEvent(Event):
    workflow: str
    subcategory: str
    type: str
    subtype: str
    values: list[tuple[str, str]]
    measures: list[tuple[str, Union[int, float]]]
    children: list[type[Event]]  # type: ignore[valid-type]

@dataclasses.dataclass(frozen=True)
class ProjectOpened(Event): ...
@dataclasses.dataclass(frozen=True)
class ProjectCreated(Event): ...
@dataclasses.dataclass(frozen=True)
class ProjectAboutToClose(Event): ...
@dataclasses.dataclass(frozen=True)
class ProjectClosed(Event): ...

@dataclasses.dataclass(frozen=True)
class ProjectAboutToSave(Event):
    file_path: str

@dataclasses.dataclass(frozen=True)
class ProjectSaved(Event): ...

@dataclasses.dataclass(frozen=True)
class ExportTexturesAboutToStart(Event):
    textures: dict[tuple[str, str], list[str]]

@dataclasses.dataclass(frozen=True)
class ExportTexturesEnded(Event):
    status: ExportStatus
    message: str
    textures: dict[tuple[str, str], list[str]]

@dataclasses.dataclass(frozen=True)
class ShelfCrawlingStarted(Event):
    shelf_name: str

@dataclasses.dataclass(frozen=True)
class ShelfCrawlingEnded(Event):
    shelf_name: str

@dataclasses.dataclass(frozen=True)
class _ProjectEditionEntered(Event): ...
@dataclasses.dataclass(frozen=True)
class _ProjectEditionLeft(Event): ...
@dataclasses.dataclass(frozen=True)
class ProjectEditionEntered(Event): ...
@dataclasses.dataclass(frozen=True)
class ProjectEditionLeft(Event): ...

@dataclasses.dataclass(frozen=True)
class BusyStatusChanged(Event):
    busy: bool

@dataclasses.dataclass(frozen=True)
class BakingProcessAboutToStart(Event):
    stop_source: StopSource

@dataclasses.dataclass(frozen=True)
class BakingProcessProgress(Event):
    progress: float

@dataclasses.dataclass(frozen=True)
class BakingProcessEnded(Event):
    status: BakingStatus

@dataclasses.dataclass(frozen=True)
class _LayerStacksModelDataChanged(Event): ...
@dataclasses.dataclass(frozen=True)
class LayerStacksModelDataChanged(Event): ...

@dataclasses.dataclass(frozen=True)
class EngineComputationsStatusChanged(Event):
    engine_computations_enabled: bool

from _substance_painter.event import TextureStateEventAction as TextureStateEventAction

@dataclasses.dataclass(frozen=True)
class TextureStateEvent(Event):
    @staticmethod
    def cache_key_invalidation_throttling_period() -> datetime.timedelta: ...
    @staticmethod
    def set_cache_key_invalidation_throttling_period(period: datetime.timedelta) -> None: ...
    action: TextureStateEventAction
    stack_id: int
    tile_indices: tuple[int, int]
    channel_type: ChannelType
    cache_key: int

@dataclasses.dataclass(frozen=True)
class CameraPropertiesChanged(Event):
    camera_id: int

class _ProjectEditionStateEventsGenerator:
    class _State(enum.Enum):
        EDITION_STOPPED = 1
        PRE_EDITION_STARTED = 2
        EDITION_STARTED = 3
    def __init__(self, dispatcher) -> None: ...

class Dispatcher:
    def __init__(self) -> None: ...
    def connect(self, event_cls: type[Event], callback: Callable[[Event], Any]) -> None: ...
    def connect_strong(self, event_cls: type[Event], callback: Callable[[Event], Any]) -> None: ...
    def disconnect(self, event_cls: type[Event], callback: Callable[[Event], Any]) -> None: ...

DISPATCHER: Dispatcher
