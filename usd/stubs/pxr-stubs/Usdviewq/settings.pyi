# mypy: disable-error-code="misc, override, no-redef"

from _typeshed import Incomplete
from typing import Callable, ClassVar

class ConfigManager:
    """
    Class used to manage, read, and write the different saved settings that
    represent the usdview application's current state.
    """
    EXTENSION: ClassVar[str] = ...
    defaultConfig: ClassVar[str] = ...
    def __init__(self, configDirPath) -> None:
        """Creates the manager instance.

                Parameters
                ----------
                configDirPath : str
                    The directory that contains the state files
        """
    def _loadConfigPaths(self):
        """Private method to load the config names and associated paths"""
    def close(self):
        """Signal that application is closing"""
    def getConfigs(self):
        """Gets the list of config names

                Returns
                -------
                list[str]
                    List of all the avaiable config names in the _configDirPath
        """
    def loadSettings(self, config, version, isEphemeral: bool = ...):
        """
        Loads the specified config. We wait to do this instead of loading in
        init to allow the manager to be created and read the list of available
        configs without actually doing the more expensive settings loading.

        Paramters
        ---------
        config : str
            The name of the config
        version : int
            Version number (used by the State class)
        isEphemeral : bool
            Usually when we use the default config we save all settings on app
            close (expected behavior of usdview before the advent of
            ConfigManager). If isEphemeral, we won't save no matter what
        """
    def save(self, newName: Incomplete | None = ...):
        """Saves the current state to the specified config

                Parameters
                ----------
                newName : str
                    The name of the config we will be saving to (it may or may not
                    exist in the _configDirPath). Iff same as defaultConfig, we save on
                    application close.
        """

class ExclusiveFile:
    """Wraps around file objects to ensure process has locked writes"""
    def __init__(self, *args, **kwargs) -> None: ...
    def __enter__(self): ...
    def __exit__(self, *args): ...

class Settings(StateSource):
    """An object which encapsulates saving and loading of application state to
    a state file. When created, it loads state from a state file and stores it
    in a buffer. Its children sources can fetch their piece of state from the
    buffer. On save, this object tells its children to save their current
    states, then saves the buffer back to the state file.
    """
    def __init__(self, version, stateFilePath: Incomplete | None = ...) -> None: ...
    def _getState(self):
        """Gets the buffered state rather than asking its parent for its state.
        """
    def _loadState(self):
        """Loads and returns application state from a state file. If the file is
                not found, contains invalid JSON, does not contain a dictionary, an
                empty state is returned instead.
        """
    def onSaveState(self, state):
        """Settings object has no state properties."""
    def save(self):
        """Inform all children to save their states, then write the state buffer
                back to the state file.
        """

class StateSource:
    """An object which has some savable application state."""
    def __init__(self, parent, name) -> None: ...
    def GetChildStateSource(self, childName):
        """Returns the child StateSource corresponding to childName, or None"""
    def _getChildState(self, childName):
        """Get a child source's state dict. This method guarantees that a dict
                will be return but does not guarantee anything about the contents of
                the dict.
        """
    def _getState(self):
        """Get this source's state dict from its parent source."""
    def _registerChildStateSource(self, child):
        """Registers a child StateSource with this source object."""
    def _saveState(self):
        """Saves the source's state to the settings object's state buffer."""
    def _typeCheck(self, value, prop):
        """Validate a value against a StateProp."""
    def onSaveState(self, state):
        """Save the source's state properties to a dict."""
    def stateProperty(self, name, default, propType: Incomplete | None = ..., validator: Callable = ...):
        """Validates and creates a new StateProp for this source. The property's
                value is returned so this method can be used during StateSource
                initialization."""

class _StateProp:
    """Defines a state property on a StateSource object."""
    def __init__(self, name, default, propType, validator) -> None: ...
