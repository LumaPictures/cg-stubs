import os
from collections.abc import Iterable, Mapping
from typing import TypedDict

# The parts of a .keymap (version 1) and .keymap2 (version 2) file that this
# module reads; the files have more keys.
class _V1Action(TypedDict, total=False):
    symbol: str
    keys: list[str]

class _V1Context(TypedDict, total=False):
    symbol: str
    actions: list[_V1Action]
    contexts: list["_V1Context"]

class _V1Keymap(TypedDict, total=False):
    name: str
    version: int
    contexts: list[_V1Context]

class _V2Binding(TypedDict, total=False):
    action: str
    keys: list[str]

class _V2Context(TypedDict, total=False):
    symbol: str
    bindings: list[_V2Binding]
    contexts: list["_V2Context"]

class _V2Keymap(TypedDict, total=False):
    name: str
    version: int
    symbol: str
    contexts: list[_V2Context]

version_token: str
mappingLegacyShiftedUS: dict[str, str]
mappingUStoFRENCH: dict[str, str]

def applyMappingToKeyString(key_string: str, mapping: Mapping[str, str]) -> str: ...
def splitKeySequenceString(seq_string: str) -> list[str]: ...
def applyMappingToBindingString(binding_string: str, mapping: Mapping[str, str]) -> str: ...

class Version1KeymapImpl:
    name_token: str
    contexts_token: str
    actions_token: str
    keys_token: str
    def applyMappingOverActions(
        self, action_list: Iterable[_V1Action], mapping: Mapping[str, str]
    ) -> None: ...
    def applyMappingOverContexts(
        self, context_list: Iterable[_V1Context], mapping: Mapping[str, str]
    ) -> None: ...
    def applyMapping(self, keymap: _V1Keymap, mapping: Mapping[str, str]) -> None: ...

class Version2KeymapImpl:
    name_token: str
    contexts_token: str
    bindings_token: str
    keys_token: str
    def applyMappingOverBindings(
        self, binding_list: Iterable[_V2Binding], mapping: Mapping[str, str]
    ) -> None: ...
    def applyMappingOverContexts(
        self, context_list: Iterable[_V2Context], mapping: Mapping[str, str]
    ) -> None: ...
    def applyMapping(self, keymap: _V2Keymap, mapping: Mapping[str, str]) -> None: ...

def applyMappingToKeymapFile(
    src_keymap_filepath: str | os.PathLike[str], mapping: Mapping[str, str], dst_keymap_filepath: str | os.PathLike[str], dst_keymap_name: str = ...
) -> None: ...
def importV1KeymapBindingsToKeymapFile(
    src_keymap_filepath: str | os.PathLike[str], v1_keymap_filepath: str | os.PathLike[str], dst_keymap_filepath: str | os.PathLike[str], dst_keymap_name: str = ...
) -> None: ...
