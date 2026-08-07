import dataclasses
import datetime
import enum
from typing import Union
from substance_painter.async_utils import StopSource as StopSource
from substance_painter.baking import BakingStatus as BakingStatus
from substance_painter.export import ExportStatus as ExportStatus
from substance_painter.resource import ReloadResourcesFilter as ReloadResourcesFilter, ResourceID as ResourceID
from substance_painter.textureset import ChannelType as ChannelType
from typing import Any, Callable

@dataclasses.dataclass(frozen=True)
class Event:
    """Base event class."""

@dataclasses.dataclass(frozen=True)
class _TestEvent(Event):
    """Event for testing purpose only.

    This event is triggered by ``_substance_painter.event.trigger_test_event``.
    """
    message: str

@dataclasses.dataclass(frozen=True)
class _DunamisEvent(Event):
    """Event triggered when a dunamis event is sent.
    """
    json: str

@dataclasses.dataclass(frozen=True)
class _UpdateProjectResourcesEnded(Event):
    """Event triggered when the update of project resources has ended.
    """
@dataclasses.dataclass(frozen=True)
class ProjectOpened(Event):
    """Event triggered when an existing project has been opened.
    """
@dataclasses.dataclass(frozen=True)
class ProjectCreated(Event):
    """Event triggered when a new project has been created.
    """
@dataclasses.dataclass(frozen=True)
class ProjectAboutToClose(Event):
    """Event triggered just before closing the current project.
    """
@dataclasses.dataclass(frozen=True)
class ProjectClosed(Event):
    """Event triggered just before closing the current project.
    """

@dataclasses.dataclass(frozen=True)
class ProjectAboutToSave(Event):
    """Event triggered just before saving the current project.

    :param file_path: The destination file.
    """
    file_path: str

@dataclasses.dataclass(frozen=True)
class ProjectSaved(Event):
    """Event triggered once the current project is saved.
    """

@dataclasses.dataclass(frozen=True)
class ExportTexturesAboutToStart(Event):
    """Event triggered just before a textures export.

    :param textures: List of texture files
        to be written to disk, grouped by stack (Texture Set name, stack name).
    """
    textures: dict[tuple[str, str], list[str]]

@dataclasses.dataclass(frozen=True)
class ExportTexturesEnded(Event):
    """Event triggered after textures export is finished.

    :param status: Status code.
    :param message: Human readable status message.
    :param textures: List of texture files
        written to disk, grouped by stack (Texture Set name, stack name).
    """
    status: ExportStatus
    message: str
    textures: dict[tuple[str, str], list[str]]

@dataclasses.dataclass(frozen=True)
class ShelfCrawlingStarted(Event):
    """Event triggered when a shelf starts reading the file system to discover
    new resources.

    :param shelf_name: Name of the shelf discovering resources.

    See also:
        :meth:`Shelf.is_crawling`.
    """
    shelf_name: str

@dataclasses.dataclass(frozen=True)
class ShelfCrawlingEnded(Event):
    """Event triggered when a shelf has finished discovering new resources and
    loading their thumbnails.

    :param shelf_name: Name of the shelf that has finished discovering resources.

    See also:
        :meth:`Shelf.is_crawling`.
    """
    shelf_name: str

@dataclasses.dataclass(frozen=True)
class _ProjectEditionEntered(Event):
    """Event triggered when the paint editor enter in edition mode.
    """
@dataclasses.dataclass(frozen=True)
class _ProjectEditionLeft(Event):
    """Event triggered when the paint editor leaves the editon mode.
    """
@dataclasses.dataclass(frozen=True)
class ProjectEditionEntered(Event):
    """Event triggered when the project is fully loaded and ready to work with.

    When edition is entered, it is for example possible to query/edit the project
    properties, to bake textures or do project export.
    """
@dataclasses.dataclass(frozen=True)
class ProjectEditionLeft(Event):
    """Event triggered when the current project can non longer be edited.
    """

@dataclasses.dataclass(frozen=True)
class BusyStatusChanged(Event):
    """Event triggered when Substance 3D Painter busy state changed.

    :param busy: Whether Substance 3D Painter is busy now.

    See also:
        :func:`substance_painter.project.execute_when_not_busy`,
        :func:`substance_painter.project.is_busy`.
    """
    busy: bool

@dataclasses.dataclass(frozen=True)
class BakingProcessAboutToStart(Event):
    """Event triggered when a baking is about to start.

    :param stop_source: The baking stop source, can be compared with the StopSource
        returned from the baking launch methods to identify the baking process.

    See also:
        :func:`substance_painter.baking.bake_async`
        :func:`substance_painter.baking.bake_selected_textures_async`
    """
    stop_source: StopSource

@dataclasses.dataclass(frozen=True)
class BakingProcessProgress(Event):
    """Event triggered when baking process progress changes.

    :param progress: The baking progress, between [0.0, 1.0].

    See also:
        :func:`substance_painter.baking.bake_async`
        :func:`substance_painter.baking.bake_selected_textures_async`
    """
    progress: float

@dataclasses.dataclass(frozen=True)
class BakingProcessEnded(Event):
    """Event triggered after baking is finished.

    :param status: Status of the baking process.

    See also:
        :func:`substance_painter.baking.bake_async`
        :func:`substance_painter.baking.bake_selected_textures_async`
    """
    status: BakingStatus

@dataclasses.dataclass(frozen=True)
class _LayerStacksModelDataChanged(Event):
    """Private event triggered whenever the status of the Layer Stacks changes."""
@dataclasses.dataclass(frozen=True)
class LayerStacksModelDataChanged(Event):
    """
    Event triggered whenever the status of the Layer Stacks changes.

    See also:
        :mod:`substance_painter.layerstack`
    """

@dataclasses.dataclass(frozen=True)
class EngineComputationsStatusChanged(Event):
    """
    Event triggered whenever the status of the engine computations changes.

    See also:
        :func:`substance_painter.application.engine_computations_status`
    """
    engine_computations_enabled: bool

@dataclasses.dataclass(frozen=True)
class GraphicalUserInterfaceStarted(Event):
    """
    Event triggered when the GUI has finished to initialize itself.

    If you want to make sure every widget part of the UI is instanciated,
    wait for this event before anything.
    """

from _substance_painter.event import TextureStateEventAction as TextureStateEventAction

@dataclasses.dataclass(frozen=True)
class TextureStateEvent(Event):
    """Event triggered when a document texture is added, removed or updated.

    :param action: Performed action (add, remove, update).
    :param stack_id: The stack the texture bellongs to, can be used to create a
        :class:`substance_painter.textureset.Stack` instance.
    :param tile_indices: The uv tile indices.
    :param channel_type: The document channel type.
    :param cache_key: The texture current cache key. Those cache keys are persistent across
        sessions.
    """
    @staticmethod
    def cache_key_invalidation_throttling_period() -> datetime.timedelta:
        """Get the minimum duration between two texture update events (for a given texture).

        Returns:
            datetime.timedelta: The minimum duration between two update events.
        """
    @staticmethod
    def set_cache_key_invalidation_throttling_period(period: datetime.timedelta) -> None:
        """Set the minimum duration between two texture update events (for a given texture).

        Warning: this setting is global and every work made in a callback associated to this event
        may greatly hurt the painting experience.

        Args:
            period (datetime.timedelta): The minimum duration between two update events, can't
                be lower than 500ms.

        Raises:
            ValueError: If period is below 500ms.
        """
    action: TextureStateEventAction
    stack_id: int
    tile_indices: tuple[int, int]
    channel_type: ChannelType
    cache_key: int

@dataclasses.dataclass(frozen=True)
class CameraPropertiesChanged(Event):
    """Event triggered when the camera properties change.

    See also:
        :class:`substance_painter.display.Camera`
    """
    camera_id: int

@dataclasses.dataclass(frozen=True)
class ReloadResourcesStarted(Event):
    """Event triggered when a resource reload operation has started.

    :param filter: The filter object used to choose the resources that are being reloaded.

    See also:
        :func:`substance_painter.resource.reload_modified_resources_async`
    """
    filter: ReloadResourcesFilter

@dataclasses.dataclass(frozen=True)
class ReloadedResourceResult:
    """Per resource result of a succesfull resource reload operation.

    :param old_resource_id: The ResourceID of the resource that was asked to be reloaded.
    :param new_resource_id: The ResourceID of the newly added resource.

    See also:
        :class:`ReloadResourcesEnded`
        :func:`substance_painter.resource.reload_modified_resources_async`
    """
    old_resource_id: ResourceID
    new_resource_id: ResourceID

@dataclasses.dataclass(frozen=True)
class ReloadedResourceError:
    """Per resource result of an unsuccesfull resource reload operation.

    :param resource_id: The ResourceID of the resource that was asked to be reloaded.
    :param error_msg: The error message detailing what prevented the resource from being reloaded.

    See also:
        :class:`ReloadResourcesEnded`
        :func:`substance_painter.resource.reload_modified_resources_async`
    """
    resource_id: ResourceID
    error_msg: str

@dataclasses.dataclass(frozen=True)
class ReloadResourcesEnded(Event):
    """Event triggered when a resource reload operation has completed.

    :param filter: The filter object used to choose which resources to reload.
    :param reloaded_resources: The list of resources that were successfully reloaded.
    :param resource_errors: The list of resources that could not be reloaded, along with the
        corresponding reason.

    See also:
        :func:`substance_painter.resource.reload_modified_resources_async`
    """
    filter: ReloadResourcesFilter
    reloaded_resources: list[ReloadedResourceResult]
    resource_errors: list[ReloadedResourceError]

class _ProjectEditionStateEventsGenerator:
    """Generate public 'ProjectEditionEntered' and 'ProjectEditionLeft' events."""
    class _State(enum.Enum):
        """Internal state."""
        EDITION_STOPPED = 1
        PRE_EDITION_STARTED = 2
        EDITION_STARTED = 3
    def __init__(self, dispatcher) -> None: ...

class Dispatcher:
    """The Event Dispatcher."""
    def __init__(self) -> None: ...
    def connect(self, event_cls: type[Event], callback: Callable[[Event], Any]) -> None:
        """Connect a callback to handle the given event type.

        The callback is stored as a weak reference, it is automatically disconnected
        once the callback gets garbage collected.

        Args:
            event_cls (Type[Event]): An event class.
            callback (Callable[[Event], Any]): A method or a bound method that will be called when
                an instance of the given event class is triggered.
        """
    def connect_strong(self, event_cls: type[Event], callback: Callable[[Event], Any]) -> None:
        """Connect a callback to handle the given event type.

        The callback is stored as a strong reference, it is never automatically disconnected.

        Args:
            event_cls (Type[Event]): An event class.
            callback (Callable[[Event], Any]): A method or a bound method that will be called when
                an instance of the given event class is triggered.
        """
    def disconnect(self, event_cls: type[Event], callback: Callable[[Event], Any]) -> None:
        """Disconnect a previously connected callback.

        This method can be called to explicitly disconnect a callback.

        Args:
            event_cls (Type[Event]): An event class.
            callback (Callable[[Event], Any]): A method or a bound method that has been connected
                to the given event class.
        """

DISPATCHER: Dispatcher
