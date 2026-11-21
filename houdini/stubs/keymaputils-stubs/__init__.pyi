# Houdini stubs generated from Houdini 22.0.466

import os
from collections.abc import Iterable, Mapping
from typing import TypedDict

class _V1Action(TypedDict, total=False):
    symbol: str
    keys: list[str]

class _V1Context(TypedDict, total=False):
    symbol: str
    actions: list[_V1Action]
    contexts: list['_V1Context']

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
    contexts: list['_V2Context']

class _V2Keymap(TypedDict, total=False):
    name: str
    version: int
    symbol: str
    contexts: list[_V2Context]

version_token: str
mappingLegacyShiftedUS: dict[str, str]
mappingUStoFRENCH: dict[str, str]

def applyMappingToKeyString(key_string: str, mapping: Mapping[str, str]) -> str:
    """
    Apply the specified mapping to a string representing a key binding, and
    return the resulting string.
    """
def splitKeySequenceString(seq_string: str) -> list[str]:
    """
    Split a key sequence string into a list of the individual key strings
    and return that list.  Returns an empty list if the string does not
    represent a key sequence.
    """
def applyMappingToBindingString(binding_string: str, mapping: Mapping[str, str]) -> str:
    """
    Apply the specified mapping to a string representing a binding, and
    return the resulting string.  This binding can be a key string, a
    key sequence string, or a binding reference string.
    """

class Version1KeymapImpl:
    name_token: str
    contexts_token: str
    actions_token: str
    keys_token: str
    def applyMappingOverActions(self, action_list: Iterable[_V1Action], mapping: Mapping[str, str]) -> None: ...
    def applyMappingOverContexts(self, context_list: Iterable[_V1Context], mapping: Mapping[str, str]) -> None: ...
    def applyMapping(self, keymap: _V1Keymap, mapping: Mapping[str, str]) -> None: ...

class Version2KeymapImpl:
    name_token: str
    contexts_token: str
    bindings_token: str
    keys_token: str
    def applyMappingOverBindings(self, binding_list: Iterable[_V2Binding], mapping: Mapping[str, str]) -> None: ...
    def applyMappingOverContexts(self, context_list: Iterable[_V2Context], mapping: Mapping[str, str]) -> None: ...
    def applyMapping(self, keymap: _V2Keymap, mapping: Mapping[str, str]) -> None: ...

def applyMappingToKeymapFile(src_keymap_filepath: str | os.PathLike[str], mapping: Mapping[str, str], dst_keymap_filepath: str | os.PathLike[str], dst_keymap_name: str = '') -> None:
    """
    Load a source keymap (.keymap or .keymap2) file, apply a mapping to update
    its key bindings, and save the updated keymap (.keymap or .keymap2) file.

    The pair 'any' : '' can be included in the mapping dictionary to clear
    all bindings to any keys not otherwise mapped.
    """
def importV1KeymapBindingsToKeymapFile(src_keymap_filepath: str | os.PathLike[str], v1_keymap_filepath: str | os.PathLike[str], dst_keymap_filepath: str | os.PathLike[str], dst_keymap_name: str = '') -> None:
    """
    Load a source .keymap2 file and update its key bindings with those from an
    old .keymap file, and save the updated .keymap2 file. 
    """
