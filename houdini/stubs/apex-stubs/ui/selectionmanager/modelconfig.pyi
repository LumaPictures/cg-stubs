import dbg
import hou
import statehud.config as config
from apex import geoconfig as geoconfig
from apex.animationcatalog import _ControlTree
from apex.geoconfig import GeometryConfig as GeometryConfig
from apex.ui.selectionmanager.model import SelectionManagerModel as SelectionManagerModel
from apex.ui.selectionmanager.modelimpl import ModelImpl as ModelImpl
from apex.ui.selectionmanager.modelitem import BaseItem as BaseItem, ImportRootFolderItem as ImportRootFolderItem
from collections.abc import Collection, Iterable, Sequence
from typing import Required, TypedDict, Unpack

from typing import TypeAlias
from typing import Literal
from typing import TypeAlias
_Model: TypeAlias = SelectionManagerModel | ModelImpl
_BoolTree: TypeAlias = dict[str, 'bool | _BoolTree']
_LabelTree: TypeAlias = dict[str, 'str | _LabelTree']
_ItemType: TypeAlias = Literal['Folder', 'Group', 'ControlGroup', 'Control', 'Character', 'Constraint', 'Rig', 'Geo', 'Tool', 'MultiCtrl']
class _ExportedSet(TypedDict, total=False):
    name: Required[str]
    type: Required[_ItemType]
    children: list['_ExportedSet']
    color: int
    active: bool
    id: int
    pin: bool
    isolate: bool
    properties: dict[str, bool]
    special: bool
    present: bool

class _SetDiff(TypedDict, total=False):
    name: Required[str]
    id: Required[int]
    rename_from: str
    rename_to: str
    children: list['_SetDiff'] | list[_ExportedSet]
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

class _States(TypedDict, total=False):
    visibility: _BoolTree
    selection: _ControlTree
    chars: _BoolTree
    hidden_sets: list[str]
    hidden_controls: list[str]

SEL_MGR_VERSION: int
CONFIG_SETS_KEY: str
CONFIG_VERSION_KEY: str
CONFIG_STATES_KEY: str
CONFIG_REMAP_KEY: str
CONFIG_LABELS_KEY: str
CONFIG_SEL_STATE_KEY: str
CONFIG_VIS_STATE_KEY: str
CONFIG_CHAR_STATE_KEY: str
CONFIG_PIN_STATE_KEY: str
CONFIG_HIDDEN_SETS_KEY: str
CONFIG_HIDDEN_CONTROLS_KEY: str
DEFAULT_CONFIG_KEYS: list[str]
EXPAND_PROPERTY: str

class ModelConfig(config.ConfigWrapper):
    """ Encapsulate storing and loading of the model's sets
        from configs.
    """
    def storeSets(self, json_string: str) -> None:
        """ Store the json_string encoding the selection sets. """
    def storeSetsUnpacked(self, json_obj: Sequence[_ExportedSet]) -> None:
        """ Store the json object not converted to a string. """
    def storeRemapPatterns(self, left_pattern: str, right_pattern: str, left_set_pattern: str, right_set_pattern: str) -> None:
        """ Store the remap patterns used to mirror sets. """
    def storeVersion(self) -> None:
        """ Store the config version. This may be useful in the future. """
    def storeStates(self, json_string: str) -> None:
        """ Store the json_string encding the states of the controls and
            characters.
        """
    def storeStatesUnpacked(self, json_obj: _States) -> None:
        """ Store the states in an unpacked dictionary. """
    def storeLabels(self, labels_tree: _LabelTree) -> None:
        """ Store the labels set on the items in the tree. """
    def storeSetsFromModel(self, model_obj: _Model, items: Sequence[BaseItem | None] | None = None, unpacked_json: bool = True, store_properties: Collection[str] | None = None, store_persistant: bool = False, unique_ids: bool = False) -> None:
        """ Get the selection set json from the model and store it. """
    def storeLabelsFromModel(self, model_obj: _Model) -> None: ...
    def storeRemapFromModel(self, model_obj: _Model) -> None:
        """ Store the remap options from the model. """
    def storeStatesFromModel(self, model_obj: _Model, unpacked_json: bool = True, override_chars: Iterable[str] | None = None) -> None:
        """ Store the states from the model. """
    def storeAllFromModel(self, model_obj: _Model, unpacked_json: bool = True, store_version: bool = True, store_remap: bool = True, store_sets: bool = True, store_states: bool = True, store_persistant: bool = True, store_labels: bool = True, override_chars: Iterable[str] | None = None, unique_ids: bool = False) -> None:
        """ Store all from the model. """
    def loadSets(self) -> list[_ExportedSet] | str | None:
        """ Load the selection set json string from the selection set key. """
    def loadRemapPatterns(self) -> list[str] | None:
        """ Load in the remap patterns used for mirroring sets. """
    def loadVersion(self) -> int | None:
        """ Load the stored version number. This may be helpful in the future
            if we change how the config works.
        """
    def loadStates(self) -> _States | str | None:
        """ Load the json_string encoding the state of the controls and
            characters.
        """
    def loadHiddenSets(self) -> list[str] | None:
        """ Load the list of selection set names to hide by default.
            Returns a list of strings, or None.
        """
    def loadHiddenControls(self) -> list[str] | None:
        """ Load the list of control names to hide by default.
            Returns a list of strings, or None.
        """
    def loadLabels(self) -> _LabelTree | None:
        """ Load the labels tree. """
    def loadLabelsToModel(self, model_obj: _Model) -> None: ...
    def loadSetsToModel(self, model_obj: _Model, clear: bool = True, editable: bool = True, remap: bool = True, undo: bool = False, replace_char: str | None = None, parent_item: BaseItem | None = None) -> list[BaseItem]:
        """ Load the selection sets from the config and import them
            into the model.
        """
    def loadSetsForCharToModel(self, model_obj: _Model, char_name: str, editable: bool = False, undo: bool = False, make_folder: bool = True, new_folder_name: str | None = None, parent_item: BaseItem | None = None) -> ImportRootFolderItem:
        """ Load the sets on an individual character geometry
            into the model as a special immutable set.
        """
    def loadStatesToModel(self, model_obj: _Model, load_selection: bool = True, load_char_vis: bool = True, load_ctrl_vis: bool = True, load_pinned: bool = True, load_ctrls_from_vis: bool = False, in_animate_state: bool = True) -> None:
        """ Load the states of the controls and characters. """
    @dbg.ZoneScopedDecorator
    def loadAllToModel(self, model_obj: _Model, clear: bool = True, editable: bool = True, remap: bool = True, undo: bool = False, load_states: bool = True, load_selection: bool = True, load_char_vis: bool = True, load_ctrl_vis: bool = True, load_pinned: bool = True, load_ctrls_from_vis: bool = False, load_labels: bool = True, in_animate_state: bool = True, parent_item: BaseItem | None = None) -> None:
        """ Load the states and the sets to the model using this config. """
    def loadToolSpecificToModel(self, model_obj: _Model, tool_key: str, paths_tree: _ControlTree, default_visible: bool = True, in_animate_state: bool = True) -> None:
        """ Load states from a tool specific state dictionary. """
    def saveToolSpecificFromModel(self, model_obj: _Model, tool_key: str, paths_tree: _ControlTree, unpacked_json: bool = True) -> None:
        """
        Save a subset of the states to a tool specific state dictionary
        on the config.
        """

class ModelGeometryConfig(ModelConfig):
    """ For loading and storing models to a geometry. """
    def __init__(self, *args: Unpack[tuple[hou.Geometry | None, str]], **kwargs: Unpack[_PrefixKwargs]) -> None: ...
    def internalConfig(self) -> GeometryConfig: ...

class ModelFileConfig(ModelConfig):
    """ For loading and storing model to a file. """
    def __init__(self, *args: Unpack[tuple[str]], **kwargs: Unpack[_FileConfigKwargs]) -> None: ...
    def writeOut(self) -> None:
        """ Write out the data to the file. """
    def internalConfig(self) -> config.FileConfig: ...

class ModelDictConfig(ModelConfig):
    """ For loading and storing model data to a dictionary. """
    def __init__(self, *args: str | None, **kwargs: str | None) -> None: ...
    def internalConfig(self) -> config.DictConfig: ...
