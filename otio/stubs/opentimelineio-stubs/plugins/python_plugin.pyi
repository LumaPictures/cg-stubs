from . import manifest as manifest
from .. import core as core, exceptions as exceptions
from _typeshed import Incomplete

def plugin_info_map(): ...

class PythonPlugin(core.SerializableObject):  # type: ignore[name-defined]
    """A class of plugin that is encoded in a python module, exposed via a
    manifest.
    """
    _serializable_label: str
    name: Incomplete
    filepath: Incomplete
    _json_path: Incomplete
    _module: Incomplete
    def __init__(self, name=None, filepath=None) -> None: ...
    def plugin_info_map(self):
        """Returns a map with information about the plugin."""
    def module_abs_path(self):
        """Return an absolute path to the module implementing this adapter."""
    def _imported_module(self, namespace):
        """Load the module this plugin points at."""
    def module(self):
        """Return the module object for this adapter. """
    def _execute_function(self, func_name, **kwargs):
        """Execute func_name on this adapter with error checking."""
