import hou
from .debug import log as log
from .tool_helpers import anchor_point_for as anchor_point_for, is_curve_prim as is_curve_prim, node_handle_is_alive as node_handle_is_alive, point_group_string as point_group_string
from curvestate.curve3.controller import Curve3Controller as Curve3Controller

class Curve3ChannelManager:
    scene_viewer: hou.SceneViewer
    controller: Curve3Controller
    channel_list: hou.ChannelList | None
    last_channel_id: tuple[int, ...] | None
    posted_channel_update: bool
    channels_added: bool
    last_group: str
    is_updating_channels: bool
    def __init__(self, scene_viewer: hou.SceneViewer, controller: Curve3Controller) -> None:
        """
        Create the channel manager that mirrors Curve3 selection into /animation.

        The manager owns the playbar channel-list collection, Houdini callback
        registration state, and a small amount of deferred-refresh bookkeeping
        used to keep animation channels synchronized with selection and SOP
        changes without creating undo noise.
        """
    def on_enter(self, node: hou.OpNode | None) -> None:
        """
        Initialize channel-list state and register Houdini callbacks on state entry.

        When animation geometry and a current point selection both exist, this
        seeds the playbar channel collection immediately, records the current
        data id/group snapshot, and registers node/playbar callbacks so later
        SOP changes, selection changes, and animation edits can stay in sync.
        """
    def on_exit(self) -> None:
        """
        Tear down callback registration and remove the Curve3 channel collection.

        Exit cleanup is defensive against node deletion and stale deferred event
        callbacks. It unregisters any active geometry/node/playbar callbacks,
        invalidates posted deferred work, clears the playbar collection, and
        resets all cached synchronization state.
        """
    def on_selection_changed(self) -> None:
        """
        React to explicit Curve3 selection changes.

        Most selection changes should rebuild the animation channel list to match
        the new selected points/curves. During drags this rebuild is deferred
        until the drag ends so the animation editor does not thrash while the
        user is interactively moving points.
        """
    def suspend_updates_for_drag(self) -> None:
        """
        Temporarily suppress channel-list refreshes during interactive drags.

        Drag updates can change geometry/selection repeatedly; instead of
        rebuilding channels every event, the manager increments a nesting count
        and remembers whether a refresh is needed once the drag completes.
        """
    def resume_updates_after_drag(self) -> None:
        """
        End one level of drag-time suppression and flush a pending refresh.

        When the outermost drag suspension is released, any deferred channel
        synchronization request is executed by reusing the normal node-change
        callback path.
        """
    def invalidate_channel_list_cache(self) -> None:
        """
        Forget cached animation-collection identity so the next refresh rebuilds.

        This is used when external events invalidate assumptions about whether
        the playbar still contains our collection or whether the current data id
        still matches the registered animation geometry.
        """
    def refresh_channel_list_after_undo_or_redo(self) -> None:
        """
        Rebuild the playbar channel collection from current SOP state after undo/redo.

        Undo and redo can replace both the animation geometry and the selected
        point group underneath the manager. This method recomputes the current
        animation pattern, recreates or removes the collection as needed, and
        rebinds the geometry change callback to the fresh collection.
        """
    def on_controller_commit(self) -> None:
        """
        React to a controller-side geometry commit.

        Commits are treated the same as node/selection changes for channel-list
        synchronization. During drags the refresh is deferred; otherwise it
        routes through the standard node-change callback path.
        """
    def selected_point_target_numbers(self, group_string: str | None = None) -> set[int]:
        """Return the point targets that would be shown in the animation editor."""
    def rename_channel_bases_in_geometry(self, geo: hou.Geometry, base_renames: dict[str, str]) -> bool:
        """Rename packed /animation channel primitive names inside `geo`."""
    def rename_channel_bases(self, base_renames: dict[str, str]) -> bool:
        """
        Rename animation-channel primitive names for changed point channel bases.

        Point `channel_name` stores the base name. Animation primitives store
        concrete per-component names as `<base>_<suffix>`, so renaming a point
        channel base must rename each matching animation primitive to keep the
        same channel data associated with the renamed point.
        """
    def animation_target_group_string(self, synchronize_keys_per_curve: bool) -> str:
        """
        Return the point-group string that animation commands should operate on.

        Depending on `synchronize_keys_per_curve`, this either returns the
        point-target set for the current selection or the curve-wide target set
        used when key operations should affect whole curves.
        """
    def anchor_group_string_for_group(self, group_string: str) -> str:
        """Return `group_string` with Bezier control/tangent points remapped to anchors."""
    def animation_targets_already_fully_selected(self) -> bool:
        """
        Return whether point-target selection already covers whole selected curves.

        This is used by UI/command logic to know whether a curve-wide key
        operation would change the effective target set or is already implied by
        the current point selection.
        """
    def selected_point_channel_prims(self, anim_geo: hou.Geometry | None = None) -> list[hou.ChannelPrim]:
        """
        Return animation-channel primitives for the current point-target selection.

        If `anim_geo` is omitted the current unpacked animation geometry is used.
        This is a convenience wrapper for editing keys on selected point targets.
        """
    def selected_curve_channel_prims(self, anim_geo: hou.Geometry | None = None) -> list[hou.ChannelPrim]:
        """
        Return animation-channel primitives for the current curve-wide selection.

        If `anim_geo` is omitted the current unpacked animation geometry is used.
        This is the curve-synchronized counterpart to
        `selected_point_channel_prims()`.
        """
    def selected_targets_key_status(self, synchronize_keys_per_curve: bool) -> str:
        '''
        Return the HUD key status string for the current selection.

        The result is `""` when nothing is selected, `Keyed` when every target
        point has channel wiring, `Unkeyed` when none do, and `Partially Keyed`
        when the selection mixes both states.
        '''
    def remove_keyframes_at_current_frame(self, synchronize_keys_per_curve: bool) -> bool:
        """
        Remove keys at the current frame from the current animation target set.

        The method copies the unpacked animation geometry, removes keys from the
        relevant channel primitives, reapplies the edited animation payload to
        the controller, and triggers normal channel-list synchronization.
        Returns `True` only when at least one key was actually removed.
        """
