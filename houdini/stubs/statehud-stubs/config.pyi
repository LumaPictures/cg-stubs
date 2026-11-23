from collections.abc import KeysView
from houtypes import JSONValue
from statehud import baseconfig as baseconfig

def getBoolPref(pref: str, default_value: bool = False) -> bool:
    """ Get a boolean preference value. """
def setBoolPref(pref: str, val: bool) -> bool:
    """ Set a boolean preference value. """
def getFloatPref(pref: str, default_value: float = 0.0) -> float:
    """ Get a float preference value. """
def setFloatPref(pref: str, val: float) -> bool:
    """ Set a float preference value. """
def getIntPref(pref: str, default_value: int = 0) -> int:
    """ Get an int preference value. """
def setIntPref(pref: str, val: int) -> bool:
    """ Set an int preference value. """
AbstractConfig = baseconfig.AbstractConfig
BaseNodeConfig = baseconfig.BaseNodeConfig
ConfigWrapper = baseconfig.ConfigWrapper

class UserDataConfig(BaseNodeConfig):
    """ A config class for storing config information in the user data on
        the node.
    """
    def keys(self) -> KeysView[str] | list[str]:
        """ Override to provide implementation. """

class DictConfig(AbstractConfig):
    """ Wrapper to use a dictionary as a config object. """
    def __init__(self, *args: str | None, **kwargs: str | None) -> None: ...
    def canStore(self) -> bool:
        """ Whether is it able to store the config. """
    def keys(self) -> KeysView[str]:
        """ Override to provide implementation. """

class FileConfig(AbstractConfig):
    """ A config used to store and load data from files. """
    _json_data: dict[str, JSONValue]
    def __init__(self, file_path: str, read: bool = False, write: bool = False, prefix: str | None = None) -> None: ...
    def loadJsonData(self) -> None:
        """ Load the json data from the file. """
    def canStore(self) -> bool | str:
        """ Whether is it able to store the config. """
    def canLoad(self) -> bool | str:
        """ Whether it is able to load the config. """
    def keys(self) -> KeysView[str]:
        """ Override to provide implementation. """
    def writeOut(self) -> None:
        """ Write out the collected data to the file. """
