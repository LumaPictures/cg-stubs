from collections.abc import Collection, Iterable, Sequence
from typing import Literal, Required, TypeAlias, TypedDict, Unpack, type_check_only

import hou
from apex.animationcatalog import _ControlTree
from apex.geoconfig import GeometryConfig
from apex.ui.selectionmanager.model import SelectionManagerModel
from apex.ui.selectionmanager.modelimpl import ModelImpl
from apex.ui.selectionmanager.modelitem import BaseItem, ImportRootFolderItem
from statehud import config

# The selection sets model: the Qt one, or its Qt-less implementation (which a
# SelectionManagerModel wraps, and which loads geometry configs into itself).
_Model: TypeAlias = SelectionManagerModel | ModelImpl

# A control tree whose leaves say whether each control is included (True) or not.
_BoolTree: TypeAlias = dict[str, "bool | _BoolTree"]
# A control tree whose nodes may hold a label for the control under utils.LABEL_KEY
# ("__label__"); a rig's controls are under its utils.getAltSubtreeName() (":tree") key.
_LabelTree: TypeAlias = dict[str, "str | _LabelTree"]

# The modelitem TYPE_* values: an item's "type" in its exported JSON.
_ItemType: TypeAlias = Literal[
    "Folder", "Group", "ControlGroup", "Control", "Character", "Constraint", "Rig", "Geo", "Tool", "MultiCtrl"
]

# An item as BaseItem.export() writes it (and loadSelectionSets() reads it).
class _ExportedSet(TypedDict, total=False):
    name: Required[str]
    type: Required[_ItemType]
    children: list["_ExportedSet"]
    color: int
    active: bool
    id: int
    pin: bool
    isolate: bool
    # Extra item properties (modelconfig.EXPAND_PROPERTY: whether it is expanded in the view).
    properties: dict[str, bool]
    special: bool
    present: bool

# An entry of modelimpl.computeSavedTreeDiff(), which BaseItem.applyDiff() applies: a
# renamed item (rename_from/rename_to) or one whose children changed (children: their
# diff), or a whole exported set that was added (removed False, moved_to) or removed
# (removed True, moved_from), whose children are exported sets.
class _SetDiff(TypedDict, total=False):
    name: Required[str]
    id: Required[int]
    rename_from: str
    rename_to: str
    children: list["_SetDiff"] | list[_ExportedSet]
    removed: bool
    moved_to: int
    moved_from: int
    type: _ItemType
    color: int
    active: bool
    pin: bool
    isolate: bool
    properties: dict[str, bool]
    special: bool
    present: bool

class _PrefixKwargs(TypedDict, total=False):
    prefix: str | None

class _FileConfigKwargs(_PrefixKwargs, total=False):
    read: bool
    write: bool

# What ModelImpl.exportStates() returns (and the "states" config key, or a tool's key, holds).
class _States(TypedDict, total=False):
    visibility: _BoolTree
    selection: _ControlTree
    chars: _BoolTree
    hidden_sets: list[str]
    hidden_controls: list[str]

DEFAULT_CONFIG_KEYS: list[str]

class ModelConfig(config.ConfigWrapper):
    def storeSets(self, json_string: str) -> None: ...
    def storeSetsUnpacked(self, json_obj: Sequence[_ExportedSet]) -> None: ...
    def storeRemapPatterns(
        self, left_pattern: str, right_pattern: str, left_set_pattern: str, right_set_pattern: str
    ) -> None: ...
    def storeVersion(self) -> None: ...
    def storeStates(self, json_string: str) -> None: ...
    def storeStatesUnpacked(self, json_obj: _States) -> None: ...
    def storeLabels(self, labels_tree: _LabelTree) -> None: ...
    def storeSetsFromModel(
        self,
        model_obj: _Model,
        items: Sequence[BaseItem | None] | None = ...,
        unpacked_json: bool = ...,
        store_properties: Collection[str] | None = ...,
        store_persistant: bool = ...,
        unique_ids: bool = ...,
    ) -> None: ...
    def storeLabelsFromModel(self, model_obj: _Model) -> None: ...
    def storeRemapFromModel(self, model_obj: _Model) -> None: ...
    def storeStatesFromModel(
        self, model_obj: _Model, unpacked_json: bool = ..., override_chars: Iterable[str] | None = ...
    ) -> None: ...
    def storeAllFromModel(
        self,
        model_obj: _Model,
        unpacked_json: bool = ...,
        store_version: bool = ...,
        store_remap: bool = ...,
        store_sets: bool = ...,
        store_states: bool = ...,
        store_persistant: bool = ...,
        store_labels: bool = ...,
        override_chars: Iterable[str] | None = ...,
        unique_ids: bool = ...,
    ) -> None: ...
    # A JSON string in configs stored packed.
    def loadSets(self) -> list[_ExportedSet] | str | None: ...
    def loadRemapPatterns(self) -> list[str] | None: ...
    def loadVersion(self) -> int | None: ...
    def loadStates(self) -> _States | str | None: ...
    def loadHiddenSets(self) -> list[str] | None: ...
    def loadHiddenControls(self) -> list[str] | None: ...
    def loadLabels(self) -> _LabelTree | None: ...
    def loadLabelsToModel(self, model_obj: _Model) -> None: ...
    def loadSetsToModel(
        self,
        model_obj: _Model,
        clear: bool = ...,
        editable: bool = ...,
        remap: bool = ...,
        undo: bool = ...,
        replace_char: str | None = ...,
        parent_item: BaseItem | None = ...,
    ) -> list[BaseItem]: ...
    def loadSetsForCharToModel(
        self,
        model_obj: _Model,
        char_name: str,
        editable: bool = ...,
        undo: bool = ...,
        make_folder: bool = ...,
        new_folder_name: str | None = ...,
        parent_item: BaseItem | None = ...,
    ) -> ImportRootFolderItem: ...
    def loadStatesToModel(
        self,
        model_obj: _Model,
        load_selection: bool = ...,
        load_char_vis: bool = ...,
        load_ctrl_vis: bool = ...,
        load_pinned: bool = ...,
        load_ctrls_from_vis: bool = ...,
        in_animate_state: bool = ...,
    ) -> None: ...
    def loadAllToModel(
        self,
        model_obj: _Model,
        clear: bool = ...,
        editable: bool = ...,
        remap: bool = ...,
        undo: bool = ...,
        load_states: bool = ...,
        load_selection: bool = ...,
        load_char_vis: bool = ...,
        load_ctrl_vis: bool = ...,
        load_pinned: bool = ...,
        load_ctrls_from_vis: bool = ...,
        load_labels: bool = ...,
        in_animate_state: bool = ...,
        parent_item: BaseItem | None = ...,
    ) -> None: ...
    # paths_tree is unused.
    def loadToolSpecificToModel(
        self,
        model_obj: _Model,
        tool_key: str,
        paths_tree: _ControlTree,
        default_visible: bool = ...,
        in_animate_state: bool = ...,
    ) -> None: ...
    def saveToolSpecificFromModel(
        self, model_obj: _Model, tool_key: str, paths_tree: _ControlTree, unpacked_json: bool = ...
    ) -> None: ...

class ModelGeometryConfig(ModelConfig):
    # GeometryConfig's (geo, attrib_name, prefix=None).
    def __init__(self, *args: Unpack[tuple[hou.Geometry | None, str]], **kwargs: Unpack[_PrefixKwargs]) -> None: ...
    @type_check_only
    def internalConfig(self) -> GeometryConfig: ...

class ModelFileConfig(ModelConfig):
    # FileConfig's (file_path, read=False, write=False, prefix=None).
    def __init__(self, *args: Unpack[tuple[str]], **kwargs: Unpack[_FileConfigKwargs]) -> None: ...
    def writeOut(self) -> None: ...
    @type_check_only
    def internalConfig(self) -> config.FileConfig: ...

class ModelDictConfig(ModelConfig):
    # DictConfig's (prefix=None).
    def __init__(self, *args: str | None, **kwargs: str | None) -> None: ...
    @type_check_only
    def internalConfig(self) -> config.DictConfig: ...
