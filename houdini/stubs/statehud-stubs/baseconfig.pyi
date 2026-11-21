# Houdini stubs generated from Houdini 22.0.466

import hou
from collections.abc import Collection, Iterable
from typing import Any

class AbstractConfig:
    """ The base config class. """
    prefix: str
    def __init__(self, prefix: str | None = None) -> None: ...
    def getPrefix(self) -> str:
        """ Get the prefix that is attached to all keys when storing
            and loading values from the config.
        """
    def canStore(self) -> bool:
        """ Whether is it able to store the config. """
    def canLoad(self) -> bool:
        """ Whether it is able to load the config. """
    def store(self, key: str, data: object, compress: bool = False) -> None:
        """ Store 'data' with the associated 'key', and optionally
            compress the 'data' first.
            If compress, then 'data' must be JSON compatible.
        """
    def load(self, key: str, compress: bool = False) -> Any:
        """ Load the data stored with 'key', and optionally decompress it. """
    def storeInt(self, key: str, val: int) -> None: ...
    def loadInt(self, key: str) -> int | None: ...
    def storeBool(self, key: str, val: bool) -> None: ...
    def loadBool(self, key: str) -> bool | None: ...
    def storeFloat(self, key: str, val: float) -> None: ...
    def loadFloat(self, key: str) -> float | None: ...
    def keys(self) -> Collection[str]:
        """ Override to provide method for retrieving keys in config. """
    def _storeDefault(self, prefixed_key: str, data: object) -> None:
        """ Override to change the way configs are stored. """
    def _loadDefault(self, prefixed_key: str) -> Any:
        """ Override to change the way configs are loaded. """
    def copyFrom(self, other_config: AbstractConfig, compress: bool = False, copy_keys: Collection[str] | None = None, exclude_keys: Iterable[str] | None = None) -> None:
        """
        Copy stored items from one config object to another.
        If copy_keys is given, only keys in this collection are copied.
        If exclude_keys is given, only keys NOT in this collection are copied.
        Both copy_keys and exclude_keys can be used at the same time.
        """

class ConfigWrapper(AbstractConfig):
    """ A config wrapper letting you sub class this to add other
        methods, but swap out the internal config type.
    """
    def __init__(self, internal_config: AbstractConfig) -> None: ...
    def internalConfig(self) -> AbstractConfig:
        """ Get the internal config that this wraps. """
    def load(self, key: str, compress: bool = False) -> Any:
        """ Use the internal config to load the data. """
    def store(self, key: str, data: object, compress: bool = False) -> None:
        """ Use the internal config to store the data. """
    def getPrefix(self) -> str:
        """ Get the prefix that is attached to all keys when storing
            and loading values from the config.
        """
    def canStore(self) -> bool:
        """ Whether is it able to store the config. """
    def canLoad(self) -> bool:
        """ Whether it is able to load the config. """
    def keys(self) -> Collection[str]:
        """ Override to provide implementation. """

class BaseNodeConfig(AbstractConfig):
    """ The base config class. """
    node: hou.Node | None
    def __init__(self, node: hou.Node | None, prefix: str | None = None) -> None: ...
    def setNode(self, node: hou.Node | None) -> None:
        """ Set the node used for reference. Config information is pulled
            from this node.
        """
    def getNode(self) -> hou.Node | None:
        """ Get the node used for reference. Config information is pulled
            from this node.
        """
    def canStore(self) -> bool:
        """ Whether is it able to store the config. """
