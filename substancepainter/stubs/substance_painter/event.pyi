import enum
from typing import Union
from substance_painter.baking import BakingStatus as BakingStatus
from substance_painter.export import ExportStatus as ExportStatus
from substance_painter.textureset import ChannelType as ChannelType
from typing import Any, Callable, Dict, List, Tuple, Type

class Event: ...

class _TestEvent(Event):
    message: str
    def __init__(self, message) -> None: ...

class _DunamisEvent(Event):
    workflow: str
    subcategory: str
    type: str
    subtype: str
    values: List[Tuple[str, str]]
    measures: List[Tuple[str, Union[int, float]]]
    children: List[Type[Event]]
    def __init__(self, workflow, subcategory, type, subtype, values, measures, children) -> None: ...

class ProjectOpened(Event): ...
class ProjectCreated(Event): ...
class ProjectAboutToClose(Event): ...

class ProjectAboutToSave(Event):
    file_path: str
    def __init__(self, file_path) -> None: ...

class ProjectSaved(Event): ...

class ExportTexturesAboutToStart(Event):
    textures: Dict[Tuple[str, str], List[str]]
    def __init__(self, textures) -> None: ...

class ExportTexturesEnded(Event):
    status: ExportStatus
    message: str
    textures: Dict[Tuple[str, str], List[str]]
    def __init__(self, status, message, textures) -> None: ...

class ShelfCrawlingStarted(Event):
    shelf_name: str
    def __init__(self, shelf_name) -> None: ...

class ShelfCrawlingEnded(Event):
    shelf_name: str
    def __init__(self, shelf_name) -> None: ...

class _ProjectEditionEntered(Event): ...
class _ProjectEditionLeft(Event): ...
class ProjectEditionEntered(Event): ...
class ProjectEditionLeft(Event): ...

class BusyStatusChanged(Event):
    busy: bool
    def __init__(self, busy) -> None: ...

class BakingProcessEnded(Event):
    status: BakingStatus
    def __init__(self, status) -> None: ...

from _substance_painter.event import TextureStateEventAction

class TextureStateEvent(Event):
    action: TextureStateEventAction
    stack_id: int
    tile_indices: Tuple[int, int]
    channel_type: ChannelType
    cache_key: int
    def __init__(self, action, stack_id, tile_indices, channel_type, cache_key) -> None: ...

class _ProjectEdtionStateEventsGenerator:
    class _State(enum.Enum):
        EDITION_STOPPED: int
        PRE_EDITION_STARTED: int
        EDITION_STARTED: int
    def __init__(self, dispatcher) -> None: ...

class Dispatcher:
    def __init__(self) -> None: ...
    def connect(self, event_cls: Type[Event], callback: Callable[[Event], Any]) -> None: ...
    def connect_strong(self, event_cls: Type[Event], callback: Callable[[Event], Any]) -> None: ...
    def disconnect(self, event_cls: Type[Event], callback: Callable[[Event], Any]) -> None: ...

DISPATCHER: Dispatcher
