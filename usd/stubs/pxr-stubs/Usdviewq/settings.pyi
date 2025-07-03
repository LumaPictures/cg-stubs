from _typeshed import Incomplete

class _StateProp:
    """Defines a state property on a StateSource object."""
    name: Incomplete
    default: Incomplete
    propType: Incomplete
    validator: Incomplete
    def __init__(self, name, default, propType, validator) -> None: ...

class ExclusiveFile:
    """Wraps around file objects to ensure process has locked writes"""
    _args: Incomplete
    _kwargs: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...
    _file: Incomplete
    def __enter__(self): ...
    def __exit__(self, *args) -> None: ...

class StateSource:
    """An object which has some savable application state."""
    _parentStateSource: Incomplete
    _childStateSources: Incomplete
    _stateSourceName: Incomplete
    _stateSourceProperties: Incomplete
    def __init__(self, parent, name) -> None: ...
    def _registerChildStateSource(self, child) -> None:
        """Registers a child StateSource with this source object."""
    def GetChildStateSource(self, childName):
        """Returns the child StateSource corresponding to childName, or None"""
    def _getState(self):
        """Get this source's state dict from its parent source."""
    def _getChildState(self, childName):
        """Get a child source's state dict. This method guarantees that a dict
        will be return but does not guarantee anything about the contents of
        the dict.
        """
    def _typeCheck(self, value, prop):
        """Validate a value against a StateProp."""
    def _saveState(self) -> None:
        """Saves the source's state to the settings object's state buffer."""
    def stateProperty(self, name, default, propType: Incomplete | None = None, validator=...):
        """Validates and creates a new StateProp for this source. The property's
        value is returned so this method can be used during StateSource
        initialization."""
    def onSaveState(self, state) -> None:
        """Save the source's state properties to a dict."""

class Settings(StateSource):
    """An object which encapsulates saving and loading of application state to
    a state file. When created, it loads state from a state file and stores it
    in a buffer. Its children sources can fetch their piece of state from the
    buffer. On save, this object tells its children to save their current
    states, then saves the buffer back to the state file.
    """
    _version: Incomplete
    _stateFilePath: Incomplete
    _versionsStateBuffer: Incomplete
    _stateBuffer: Incomplete
    _isEphemeral: Incomplete
    def __init__(self, version, stateFilePath: Incomplete | None = None) -> None: ...
    def _loadState(self) -> None:
        """Loads and returns application state from a state file. If the file is
        not found, contains invalid JSON, does not contain a dictionary, an
        empty state is returned instead.
        """
    def _getState(self):
        """Gets the buffered state rather than asking its parent for its state.
        """
    def save(self) -> None:
        """Inform all children to save their states, then write the state buffer
        back to the state file.
        """
    def onSaveState(self, state) -> None:
        """Settings object has no state properties."""

class ConfigManager:
    """
    Class used to manage, read, and write the different saved settings that
    represent the usdview application's current state.
    """
    EXTENSION: str
    defaultConfig: str
    settings: Incomplete
    _saveOnClose: bool
    _configDirPath: Incomplete
    _configPaths: Incomplete
    def __init__(self, configDirPath) -> None:
        """Creates the manager instance.

        Parameters
        ----------
        configDirPath : str
            The directory that contains the state files
        """
    def loadSettings(self, config, version, isEphemeral: bool = False) -> None:
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
    def _loadConfigPaths(self):
        """Private method to load the config names and associated paths"""
    def getConfigs(self):
        """Gets the list of config names

        Returns
        -------
        list[str]
            List of all the avaiable config names in the _configDirPath
        """
    def save(self, newName: Incomplete | None = None) -> None:
        """Saves the current state to the specified config

        Parameters
        ----------
        newName : str
            The name of the config we will be saving to (it may or may not
            exist in the _configDirPath). Iff same as defaultConfig, we save on
            application close.
        """
    def close(self) -> None:
        """Signal that application is closing"""
