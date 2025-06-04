from _typeshed import Incomplete
from maya.app.ghosting.GhostingManager import GhostingManager as GhostingManager, string_to_frames as string_to_frames
from maya.app.ghosting.ghosting_optionvar_states import GHOSTING_MODE_CUSTOM_FRAMES as GHOSTING_MODE_CUSTOM_FRAMES, GHOSTING_MODE_KEYFRAMES as GHOSTING_MODE_KEYFRAMES, GHOSTING_MODE_POST_FRAMES as GHOSTING_MODE_POST_FRAMES, GHOSTING_MODE_PRE_AND_POST_FRAMES as GHOSTING_MODE_PRE_AND_POST_FRAMES, GHOSTING_MODE_PRE_FRAMES as GHOSTING_MODE_PRE_FRAMES, GHOSTING_PRESETS as GHOSTING_PRESETS, GHOSTING_PRESET_CUSTOM as GHOSTING_PRESET_CUSTOM, GhostingPreferenceAllInRange as GhostingPreferenceAllInRange, GhostingPreferenceCustomFrames as GhostingPreferenceCustomFrames, GhostingPreferenceEnabled as GhostingPreferenceEnabled, GhostingPreferenceFarOpacity as GhostingPreferenceFarOpacity, GhostingPreferenceGeometryFilter as GhostingPreferenceGeometryFilter, GhostingPreferenceGhostsStep as GhostingPreferenceGhostsStep, GhostingPreferenceHierarchy as GhostingPreferenceHierarchy, GhostingPreferenceJointFilter as GhostingPreferenceJointFilter, GhostingPreferenceLocatorFilter as GhostingPreferenceLocatorFilter, GhostingPreferenceMode as GhostingPreferenceMode, GhostingPreferenceNearOpacity as GhostingPreferenceNearOpacity, GhostingPreferencePostColour as GhostingPreferencePostColour, GhostingPreferencePostFrames as GhostingPreferencePostFrames, GhostingPreferencePreColour as GhostingPreferencePreColour, GhostingPreferencePreFrames as GhostingPreferencePreFrames, GhostingPreferencePreset as GhostingPreferencePreset, GhostingPreferenceUseDriver as GhostingPreferenceUseDriver, INDEX_ENUM_DATA as INDEX_ENUM_DATA, INDEX_ENUM_ID as INDEX_ENUM_ID, INDEX_ENUM_INFO as INDEX_ENUM_INFO, INDEX_ENUM_NAME as INDEX_ENUM_NAME
from maya.common.ui import LayoutManager as LayoutManager, callback_tool as callback_tool
from maya.common.utils import Singleton as Singleton

GHOSTING_EDITOR_TITLE: Incomplete

class GhostingEditor(Incomplete):
    ID_ADD_FRAME: str
    ID_ALL_IN_RANGE: str
    ID_CUSTOM_FRAMES: str
    ID_DISPLAY: str
    ID_ENABLED: str
    ID_FAR_OPACITY: str
    ID_GHOSTS_STEP: str
    ID_GHOSTS_POST: str
    ID_GHOSTS_PRE: str
    ID_GHOST_LIST: str
    ID_HIERARCHY: str
    ID_MODES: str
    ID_NEAR_OPACITY: str
    ID_OBJECTS: str
    ID_OBJ_ALL: str
    ID_GEOMETRY_FILTER: str
    ID_JOINT_FILTER: str
    ID_LOCATOR_FILTER: str
    ID_PRE_COLOUR: str
    ID_PRESET_PREFIX: str
    ID_PRESETS: str
    ID_POST_COLOUR: str
    ID_SELECTED: str
    ID_UNGHOST: str
    ID_UNGHOST_ALL: str
    ID_USE_DRIVER: str
    ID_MENUBAR: str
    ID_WORKSPACE_CONTROL: str
    ID_LAYOUT_DISPLAY: str
    ID_LAYOUT_GHOSTED_OBJECTS: str
    ID_LAYOUT_FILTERS: str
    ID_LAYOUT_FRAME_PARAMETERS: str
    ID_LAYOUT_MODES: str
    ID_LAYOUT_PRESETS: str
    ID_LAYOUT_ROOT: str
    ID_LAYOUT_SELECTED: str
    ID_LAYOUT_SETTINGS: str
    ID_LAYOUT_SETTINGS_ROWS: str
    ID_LAYOUT_UNGHOST: str
    ID_LABEL_GHOSTS_STEP: str
    ID_LABEL_HIERARCHY: str
    ID_LABEL_LAYOUT_PRESETS: str
    ID_LABEL_OBJECT_TYPES: str
    ID_MODE_POST_FRAMES: str
    ID_MODE_PRE_FRAMES: str
    ID_MODE_PRE_POST_FRAMES: str
    ID_MODE_CUSTOM_FRAMES: str
    ID_MODE_KEYFRAMES: str
    MODE_INFO: Incomplete
    class DisableUiUpdateScope:
        paused_callbacks: Incomplete
        was_enabled: Incomplete
        def __enter__(self) -> None: ...
        def __exit__(self, exit_type: type[BaseException] | None, value: BaseException | None, traceback: types.TracebackType | None) -> None: ...
        def __init__(self) -> None: ...
    preference_callbacks: Incomplete
    update_ui_from_values: bool
    widgets: Incomplete
    selection_change_job: Incomplete
    ghost_list_change_job: Incomplete
    delayed_update_job: Incomplete
    def __init__(self) -> None: ...
    def build_editor(self) -> None: ...
    def create_controls(self): ...
    def frame_parameter_visibility(self): ...
    def delayed_ui_build_ghost_frame_parameters(self) -> None: ...
    def ui_build_ghost_frame_parameters(self, populate_values) -> None: ...
    def ui_update_mode_selection(self) -> None: ...
    @staticmethod
    def callback_ui_update_ghosted_objects(tool) -> None: ...
    @staticmethod
    def callback_reset_all(tool) -> None: ...
    @staticmethod
    def callback_add_frame_pressed(tool) -> None: ...
    @staticmethod
    def callback_custom_frames_ui_changed(tool) -> None: ...
    @staticmethod
    def callback_enabled_ui_changed(tool, new_enabled_value) -> None: ...
    @staticmethod
    def callback_far_opacity_ui_changed(tool) -> None: ...
    @staticmethod
    def callback_geometry_filter_ui_changed(tool, new_filter_value) -> None: ...
    @staticmethod
    def callback_post_frames_ui_changed(tool) -> None: ...
    @staticmethod
    def callback_pre_frames_ui_changed(tool) -> None: ...
    @staticmethod
    def callback_ghosts_step_ui_changed(tool) -> None: ...
    @staticmethod
    def callback_hierarchy_ui_changed(tool, new_hierarchy_value) -> None: ...
    @staticmethod
    def callback_joint_filter_ui_changed(tool, new_filter_value) -> None: ...
    @staticmethod
    def callback_locator_filter_ui_changed(tool, new_filter_value) -> None: ...
    @staticmethod
    def callback_mode_ui_changed(tool, mode) -> None: ...
    @staticmethod
    def callback_near_opacity_ui_changed(tool) -> None: ...
    @staticmethod
    def callback_post_colour_ui_changed(tool) -> None: ...
    @staticmethod
    def callback_node_selected_ui_changed(tool) -> None: ...
    @staticmethod
    def callback_pre_colour_ui_changed(tool) -> None: ...
    @staticmethod
    def callback_all_in_range_ui_changed(tool) -> None: ...
    @staticmethod
    def callback_preset_ui_changed(tool, preset) -> None: ...
    def widget_should_update(self, widget_to_check, widget_id): ...
    @staticmethod
    def update_widget(tool, widget_id) -> None: ...
    @staticmethod
    def callback_pref_changed_mode(tool) -> None: ...
    @staticmethod
    def callback_pref_changed_preset(tool) -> None: ...
    @staticmethod
    def callback_pref_changed_all_in_range(tool) -> None: ...
    def monitor_preference(self, preference, callback_function) -> None: ...
    def pause_preference_callback(self): ...
    def resume_preference_callback(self, callbacks) -> None: ...
    def window_closed(self) -> None: ...
