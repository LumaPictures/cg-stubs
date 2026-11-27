import hou
from collections.abc import KeysView
from statehud.baseconfig import AbstractConfig

class GeometryConfig(AbstractConfig):
    """ A config class used for loading and storing geometry directly
        to and from a geometry.
    """
    def __init__(self, geo: hou.Geometry | None, attrib_name: str, prefix: str | None = None) -> None: ...
    def setGeo(self, geo: hou.Geometry | None) -> None:
        """ Set the geometry used for saving and loading. """
    def setAttribName(self, name: str) -> None:
        """ Set the attribute name used for saving and loading. """
    def getGeo(self) -> hou.Geometry | None:
        """ Get the geometry. """
    def getAttribName(self) -> str:
        """ Get the attribute name we load and store to. """
    def getAttrib(self) -> hou.Attrib | None:
        """ Get the attribute we load and store to. """
    def canStore(self) -> bool:
        """ Whether we can store to the attribute. """
    def canLoad(self) -> bool:
        """ Whether we can load from the attribute. """
    def _storeDefault(self, prefixed_key: str, data: object) -> None:
        """ Overridden to change the way the config if stored. """
    def _loadDefault(self, prefixed_key: str) -> hou._OptionValue | None:
        """ Overridden to change how the config is loaded. """
    def keys(self) -> list[str] | KeysView[str]:
        """ Override to provide implementation. """
