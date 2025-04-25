import rez.plugin_managers
import rez.utils.data_utils
import types
from _typeshed import Incomplete
from rez.config import _load_config_from_filepaths as _load_config_from_filepaths, config as config, expand_system_vars as expand_system_vars
from rez.exceptions import RezPluginError as RezPluginError
from rez.utils.data_utils import LazySingleton as LazySingleton, cached_property as cached_property, deep_update as deep_update
from rez.utils.formatting import columnise as columnise
from rez.utils.logging_ import print_debug as print_debug, print_warning as print_warning
from rez.utils.schema import dict_to_schema as dict_to_schema
from typing import Any, TypeVar, overload

T = TypeVar('T')

def extend_path(path, name):
    """Extend a package's path.

    Intended use is to place the following code in a package's __init__.py:

        from pkgutil import extend_path
        __path__ = extend_path(__path__, __name__)

    This will add to the package's __path__ all subdirectories of
    directories on 'config.plugin_path' named after the package.  This is
    useful if one wants to distribute different parts of a single logical
    package as multiple directories.

    If the input path is not a list (as is the case for frozen
    packages) it is returned unchanged.  The input path is not
    modified; an extended copy is returned.  Items are only appended
    to the copy at the end.

    It is assumed that 'plugin_path' is a sequence.  Items of 'plugin_path'
    that are not (unicode or 8-bit) strings referring to existing
    directories are ignored.  Unicode items of sys.path that cause
    errors when used as filenames may cause this function to raise an
    exception (in line with os.path.isdir() behavior).
    """
def uncache_rezplugins_module_paths(instance: Incomplete | None = None) -> None: ...

class RezPluginType:
    """An abstract base class representing a single type of plugin.

    'type_name' must correspond with one of the source directories found under
    the 'plugins' directory.
    """
    type_name: str
    pretty_type_name: str
    plugin_classes: dict[str, type]
    failed_plugins: dict[str, str]
    plugin_modules: dict[str, types.ModuleType]
    config_data: dict[Any, Any]
    def __init__(self) -> None: ...
    def __repr__(self) -> str: ...
    def register_plugin(self, plugin_name: str, plugin_class: type, plugin_module: types.ModuleType) -> None: ...
    def load_plugins(self) -> None: ...
    def get_plugin_class(self, plugin_name: str) -> type:
        """Returns the class registered under the given plugin name."""
    def get_plugin_module(self, plugin_name: str) -> types.ModuleType:
        """Returns the module containing the plugin of the given name."""
    @cached_property
    def config_schema(self):
        """Returns the merged configuration data schema for this plugin
        type."""
    def create_instance(self, plugin: str, **instance_kwargs) -> Any:
        """Create and return an instance of the given plugin."""

class RezPluginManager:
    """Primary interface for working with registered plugins.

    Custom plugins are organized under a python package named 'rezplugins'.
    The direct sub-packages of 'rezplugins' are the plugin types supported by
    rez, and the modules below that are individual custom plugins extending
    that type.

    For example, rez provides plugins of type 'build_system': 'cmake' and 'make'::

        rezplugins/
          __init__.py
          build_system/
            __init__.py
            cmake.py
            make.py
          ...

    Here is an example of how to provide your own plugin.  In the example,
    we'll be adding a plugin for the SCons build system.

    1.  Create the 'rezplugins/build_system' directory structure, add the empty
        '__init__.py' files, and then place your new 'scons.py' plugin module
        into the 'build_system' sub-package::

            rezplugins/
              __init__.py
              build_system/
                __init__.py
                scons.py

    2.  Write your 'scons.py' plugin module, sub-classing your
        `SConsBuildSystem` class from `rez.build_systems.BuildSystem` base
        class.

        At the bottom of the module add a `register_plugin` function that
        returns your plugin class::

            def register_plugin():
                return SConsBuildSystem

    3   Set or append the rez config setting `plugin_path` to point to the
        directory **above** your 'rezplugins' directory.

        All 'rezplugin' packages found on the search path will all be merged
        into a single python package.

        Note:
            Even though 'rezplugins' is a python package, your sparse copy of
            it should  not be on the `PYTHONPATH`, just the `REZ_PLUGIN_PATH`.
            This is important  because it ensures that rez's copy of
            'rezplugins' is always found first.
    """
    _plugin_types: dict[str, rez.utils.data_utils.LazySingleton[rez.plugin_managers.RezPluginType]]
    def __init__(self) -> None: ...
    @cached_property
    def rezplugins_module_paths(self): ...
    def _get_plugin_type(self, plugin_type: str) -> RezPluginType: ...
    def register_plugin_type(self, type_class: type[RezPluginType]) -> None: ...
    def get_plugin_types(self) -> list[str]:
        """Return a list of the registered plugin types."""
    def get_plugins(self, plugin_type: str) -> list[str]:
        """Return a list of the registered names available for the given plugin
        type."""
    @overload
    def get_plugin_class(self, plugin_type: str, plugin_name: str) -> type: ...
    @overload
    def get_plugin_class(self, plugin_type: str, plugin_name: str, expected_type: type[T]) -> type[T]: ...
    def get_plugin_module(self, plugin_type: str, plugin_name: str) -> types.ModuleType:
        """Return the module defining the class registered under the given
        plugin name."""
    def get_plugin_config_data(self, plugin_type: str):
        """Return the merged configuration data for the plugin type."""
    def get_plugin_config_schema(self, plugin_type: str): ...
    def get_failed_plugins(self, plugin_type: str) -> list[tuple[str, str]]:
        """Return a list of plugins for the given type that failed to load.

        Returns:
            tuple: List of 2-tuples:
            name (str): Name of the plugin.
            reason (str): Error message.
        """
    def create_instance(self, plugin_type: str, plugin_name, **instance_kwargs: Any) -> Any:
        """Create and return an instance of the given plugin."""
    def get_summary_string(self) -> str:
        """Get a formatted string summarising the plugins that were loaded."""

class ShellPluginType(RezPluginType):
    """Support for different types of target shells, such as bash, tcsh.
    """
    type_name: str

class ReleaseVCSPluginType(RezPluginType):
    """Support for different version control systems when releasing packages.
    """
    type_name: str

class ReleaseHookPluginType(RezPluginType):
    """Support for different version control systems when releasing packages.
    """
    type_name: str

class BuildSystemPluginType(RezPluginType):
    """Support for different build systems when building packages.
    """
    type_name: str

class PackageRepositoryPluginType(RezPluginType):
    """Support for different package repositories for loading packages.
    """
    type_name: str

class BuildProcessPluginType(RezPluginType):
    """Support for different build and release processes.
    """
    type_name: str

class CommandPluginType(RezPluginType):
    """Support for different custom Rez applications/subcommands.
    """
    type_name: str

plugin_manager: Incomplete
