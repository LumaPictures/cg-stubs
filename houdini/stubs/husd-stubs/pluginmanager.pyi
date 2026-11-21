from typing import Generic

from typing import TypeVar
from typing import TypeVar
_P = TypeVar('_P')
class PluginManager(Generic[_P]):
    """ Maintains a list of the discovered plugins.
    """
    myPlugins: list[_P]
    def __init__(self, dir_name: str, factory_function_name: str, include_shadowed: bool = False, reverse: bool = False) -> None:
        """ Initialize the plugin manager.

            Looks for the python plugins that provide the given factory
            function, and calls it, storing the result in the plugin array.

            :param dir_name: The name of the subdirectory that contains
                the python plugin modules.

            :param factory_function_name: The name of the API function name
                in plugin modules that creates a plugin object.
        """
    def pluginCount(self) -> int:
        """ Returns the number of discovered plugins.
        """
    def plugins(self) -> list[_P]:
        """ Returns the array of discovered plugins.
        """
    def plugin(self, index: int) -> _P | None:
        """ Returns the plugin at the given index.

            :param: non-negative index (ie, handle) to the internal array.
        """

class ShaderTranslatorManager(PluginManager[_P]):
    """ Maintains a list of all the discovered python shader translator plugins.
    """
    def __init__(self, factory_function_name: str) -> None:
        """ Initialize the shader translators manager.

            :param factory_function_name: The name of the API function name
                in shader translator python modules that creates a python
                instance object of the actual shader translator.
        """
    def translator(self, index: int) -> _P | None:
        """ Returns the shader translator at the given index.

            :param: non-negative index (ie, handle) to the internal array.
        """
    def translatorIndexOfClass(self, class_name: str) -> int:
        """ Returns an index to the shader translator that matches 
            the given class name.
        """
    def translatorIndicesOfNonClass(self, class_name: str) -> list[int]:
        """ Returns an array of indices of shader translators that don't match
            the given class name.
        """
