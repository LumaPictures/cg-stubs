import hou
from .move_points import apply_drag_display_context as apply_drag_display_context, restore_drag_display_context as restore_drag_display_context
from .tool_helpers import anchor_ptnums_from_ptnums as anchor_ptnums_from_ptnums, point_group_string as point_group_string
from .undo_helpers import execute_with_undo as execute_with_undo
from apex import xformgadget as xg
from collections.abc import Callable as Callable, Mapping
from curvestate.curve3.controller import Curve3Controller as Curve3Controller
from curvestate.curve3.state import CurveState as CurveState
from dataclasses import dataclass, field
from houtypes import ViewerStateCommandKwargs, ViewerStateDrawKwargs, ViewerStateEnterKwargs, ViewerStateEventKwargs, ViewerStateKwargs, ViewerStateMenuActionKwargs, ViewerStateMenuPreOpenKwargs, ViewerStateParmChangeKwargs, ViewerStateVolatileClientKwargs
from typing import TypedDict

from typing import TypeAlias
from typing import TypeAlias
_XformHandleEvent: TypeAlias = xg._HandleUpdateKwargs | xg._HandleSettingsUpdateKwargs | xg._HandleCustomActionKwargs
class _HandleContext(TypedDict):
    controller: Curve3Controller
    geometry: hou.Geometry | None
    handle_manager: Curve3HandleManager

class _HandleInstanceContext(_HandleContext):
    new_instance: bool

class _HandleTargetMetadata(TypedDict, total=False):
    position: hou.Vector3
    visual_override: tuple[int, ...]
    active_handles: tuple[int, ...]
    command_source_ptnums: tuple[int, ...]

class _HandleDragState(TypedDict, total=False):
    target_key: str
    selected: tuple[int, ...]
    start_pos: hou.Vector3
    restore_group: str
    index: int
    restore_active_handles: list[int]
    start_xform_parms: dict[str, hou.Vector3]
    start_world_xform: hou.Matrix4
    start_world_center: hou.Vector3
    start_pivot_space_xform: hou.Matrix4
    active_handles: tuple[int, ...]
    visual_override: tuple[int, ...]
    command_source_ptnums: tuple[int, ...]
    orient_start_up: hou.Vector3
    orient_tangent: hou.Vector3
    change_relative: bool
    change_group: str
    current_value: float | hou.Vector3
    scale_start_value: float

class _PreservedXformState(TypedDict):
    parms: dict[str, hou.Vector3]
    base_xform: hou.Matrix4
    full_xform: hou.Matrix4
    local_full_delta: hou.Matrix4

def _mark_command_ret(command_args: object, handled: bool = True) -> None:
    """Mark state-command args as consumed for Houdini's command dispatcher."""

@dataclass(frozen=True)
class HandleTarget:
    """Provider-declared semantic handle target."""
    key: str
    point_numbers: tuple[int, ...] = field(default_factory=tuple)
    internal_point_numbers: tuple[int, ...] = field(default_factory=tuple)
    metadata: _HandleTargetMetadata = field(default_factory=dict)

class Curve3HandleProviderBase:
    """Provider contract for mode-specific handle behavior."""
    def provider_name(self) -> str:
        """Return a stable provider name used for tool-specific handle policies."""
    def is_enabled(self) -> bool:
        """Return whether this provider should currently supply handle targets."""
    def build_targets(self, context: _HandleContext) -> list[HandleTarget]:
        """Build the semantic handle targets for the active tool and geometry."""
    def configure_instance(self, manager: Curve3HandleManager, instance_index: int, target: HandleTarget, context: _HandleInstanceContext) -> None:
        """Configure one Apex gadget instance for a provider target."""
    def on_handle_start(self, event: xg._HandleStartUpdateKwargs, target: HandleTarget, context: _HandleContext) -> None:
        """React to the start of a handle drag for a target."""
    def on_handle_update(self, event: xg._HandleUpdateKwargs, target: HandleTarget, context: _HandleContext) -> None:
        """React to an interactive handle drag update for a target."""
    def on_handle_end(self, event: xg._HandleUpdateKwargs, target: HandleTarget, context: _HandleContext) -> None:
        """React to the end of a handle drag for a target."""
    def on_settings_update(self, event: xg._HandleSettingsUpdateKwargs, target: HandleTarget, context: _HandleContext) -> None:
        """React to Apex handle setting changes for a target."""
    def on_custom_action(self, event: xg._HandleCustomActionKwargs, target: HandleTarget, context: _HandleContext) -> None:
        """React to Apex handle custom menu/action events for a target."""
    def uses_custom_drag_lifecycle(self) -> bool:
        """
        Opt-in hook for non-transform handle workflows.

        Default manager behavior assumes transform preview/commit via
        translate/rotate/scale/pivot parms. Providers that need operation-
        specific drag semantics (e.g. orient/scale point controls) can opt in
        and fully own start/update/end drag handling.
        """

class Curve3HandleManager:
    """Controller-owned shared handle orchestration point."""
    controller: Curve3Controller
    _drag_state: _HandleDragState | None
    def __init__(self, controller: Curve3Controller) -> None:
        """Create a manager that owns one shared Apex xform gadget instance."""
    def get_xform_gadget(self) -> xg.ApexXformHandle | None:
        """ Return a reference to the Apex Xform Gadget. """
    def reset_gadget_instance_xform_parms(self, index: int) -> None:
        """Reset one Apex gadget instance's local xform parms to identity."""
    def _reset_gadget_instance_scale_parm(self, index: int) -> None:
        """Reset only one Apex gadget instance's local scale parm to identity."""
    def set_provider(self, provider: Curve3HandleProviderBase | None) -> None:
        """Set the active tool's handle provider and rebuild handle instances."""
    def set_state_owner(self, state_owner: CurveState | None) -> None:
        """Set the viewer state object used for Apex gadget construction and undo refresh."""
    def set_hotkey_context(self, hotkey_context: str) -> None:
        """Set the viewer-state hotkey context used by the Apex xform gadget."""
    def initialize(self) -> None:
        """Initialize the shared ApexXformHandle instance eagerly."""
    def provider(self) -> Curve3HandleProviderBase | None:
        """Return the active handle provider, if any."""
    def set_visible(self, visible: bool) -> None:
        """Set global handle visibility and synchronize the Apex instances."""
    def is_visible(self) -> bool:
        """Return whether the manager wants handles visible."""
    def on_enter(self, kwargs: ViewerStateEnterKwargs) -> None:
        """
        Activate the shared Apex gadget when the viewer state enters.

        The gadget is created once, activated on entry, and then shown or hidden
        based on Curve3's handle visibility setting. Instance geometry is
        refreshed after activation so the first draw sees correct targets.
        """
    def on_exit(self, kwargs: ViewerStateKwargs) -> None:
        """Deactivate the Apex gadget and clear all target bookkeeping on exit."""
    def on_resume(self, kwargs: ViewerStateKwargs) -> None:
        """Resume the Apex gadget after viewer-state resume and rebuild instances."""
    def on_interrupt(self, kwargs: ViewerStateKwargs) -> None:
        """Forward viewer-state interrupt events to the Apex gadget."""
    def on_draw_setup(self, kwargs: ViewerStateDrawKwargs) -> None:
        """Run the Apex draw setup phase when handle drawing is enabled."""
    def on_draw_opaque(self, kwargs: ViewerStateDrawKwargs) -> None:
        """Draw the Apex gadget's opaque components when handles are visible."""
    def on_draw_transparent(self, kwargs: ViewerStateDrawKwargs) -> None:
        """Draw the Apex gadget's transparent components when handles are visible."""
    def on_draw(self, kwargs: ViewerStateDrawKwargs) -> None:
        """Run the full Apex draw sequence for the shared handle gadget."""
    def on_draw_interrupt(self, kwargs: ViewerStateDrawKwargs) -> None:
        """Draw the Apex gadget during a viewer interrupt draw pass."""
    def on_mouse_event(self, kwargs: ViewerStateEventKwargs) -> bool:
        """Forward mouse events to the Apex gadget and report whether it handled them."""
    def on_key_event(self, kwargs: ViewerStateEventKwargs) -> bool:
        """Forward key events to the Apex gadget and report whether it handled them."""
    def on_key_transit_event(self, kwargs: ViewerStateEventKwargs) -> bool:
        """Forward key transit events to the Apex gadget."""
    def on_parm_change_event(self, kwargs: ViewerStateParmChangeKwargs) -> None:
        """Forward viewer-state parm change events to the Apex gadget."""
    def on_volatile_client_event(self, kwargs: ViewerStateVolatileClientKwargs) -> None:
        """Forward volatile client events to the Apex gadget."""
    def on_command(self, kwargs: ViewerStateCommandKwargs) -> bool:
        """Forward viewer-state commands to the Apex gadget."""
    def _prepare_edit_handle_switch(self, kwargs: ViewerStateCommandKwargs) -> None:
        """Switch to edit mode and show the edit handle before gadget tool cycling."""
    def _ensure_edit_handle_visible(self, kwargs: ViewerStateCommandKwargs) -> None:
        """Show the edit handle while keeping the settings HUD state in sync."""
    def on_menu_pre_open(self, kwargs: ViewerStateMenuPreOpenKwargs) -> bool:
        """Let the Apex gadget update its context-menu item states."""
    def on_menu_action(self, kwargs: ViewerStateMenuActionKwargs) -> bool:
        """Let the Apex gadget handle context-menu actions."""
    def _context(self) -> _HandleContext:
        """Build the provider context passed to all handle provider hooks."""
    def drag_state(self) -> _HandleDragState | None:
        """Provider-facing read access to current handle drag state."""
    def active_tangent_drag_for_command(self) -> bool:
        """Return whether a point-type command is interrupting a focused tangent handle drag."""
    def active_tangent_drag_group_for_command(self) -> str:
        """Return the focused tangent plus its command-side anchor while handle-dragging."""
    def commit_active_drag_for_command(self, command: str, sync_fn: Callable[[], object] | None = None) -> bool:
        """Bake the live standard handle transform before a shared edit command runs."""
    def rebase_active_drag_after_command(self) -> bool:
        """Re-establish transform-drag context after a point-type command cooks."""
    def event_xform_parms(self, event: _XformHandleEvent) -> dict[str, hou.Vector3]:
        """Provider-facing accessor for current gadget xform parms by event index."""
    def _external_pick(self, kwargs: ViewerStateEventKwargs) -> xg._ExternalPick | None:
        """Let Apex xform picking target Curve3 drawable points and tangent lines."""
    def _sync_instances(self, targets: list[HandleTarget], context: _HandleContext, *, preserved_xform_state_by_key: Mapping[str, _PreservedXformState] | None = None) -> None:
        """
        Match Apex gadget instances to provider targets and configure each one.

        This grows or shrinks the Apex instance count, resets per-component
        enable flags to avoid leakage between tools, then asks the provider to
        place and mask each instance for its semantic target.
        """
    def refresh_instances(self, force: bool = False) -> None:
        """
        Rebuild or refresh handle instances from the active provider.

        The manager clears instances when handles are hidden, no provider is
        active, or no targets are available. Otherwise it asks the provider for
        current targets and only fully reconfigures Apex instances when target
        identity changes or `force` requires it. A forced refresh must always
        reconfigure instances because the same semantic target key can now have
        a different geometry-derived position after undo, redo, or cook sync.
        """
    def _target_from_event(self, event: _XformHandleEvent) -> HandleTarget:
        """Resolve the semantic target associated with an Apex callback event."""
    def _event_position(self, event: _XformHandleEvent) -> hou.Vector3:
        """Return the world-space handle position for an Apex callback event."""
    def _on_handle_start(self, event: xg._HandleStartUpdateKwargs) -> None:
        """
        Initialize Curve3 drag state for an Apex handle drag.

        The start callback records the semantic target, selected points, start
        transforms, and selection/visual state to restore later. It also saves
        the Apex handle parms for the manually grouped handle undo. Providers
        with custom lifecycles receive control after the shared bookkeeping;
        standard transform providers additionally enter transient transform
        preview mode.
        """
    def _on_handle_update(self, event: xg._HandleUpdateKwargs) -> None:
        """
        Apply interactive handle-drag preview for the active target.

        Standard transform providers convert the current Apex handle transform
        into curve3core transform parms and push them as transient preview
        values. Custom providers receive the raw event and own their preview
        behavior completely.
        """
    def _on_handle_end(self, event: xg._HandleUpdateKwargs) -> None:
        """
        Commit or finish an Apex handle drag.

        Standard transform drags compute the final curve3core transform payload
        and group the manually committed Apex handle parm undo with the curve
        operation. Undo replay events are identified by `in_undo` and skip the
        geometry commit because Houdini is restoring the grouped action. The
        method always clears preview parms and restores the pre-drag selection
        display state before returning control to the provider.
        """
    def _on_handle_settings_update(self, event: xg._HandleSettingsUpdateKwargs) -> None:
        """Dispatch Apex handle setting updates to the active provider."""
    def _on_handle_custom_action(self, event: xg._HandleCustomActionKwargs) -> None:
        """Dispatch Apex handle custom actions to the active provider."""
    def _on_handle_visibility(self, event: xg._HandleVisEvent) -> None:
        """Receive Apex visibility callbacks; Curve3 currently owns visibility state."""
