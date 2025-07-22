from .. import core as core, exceptions as exceptions, plugins as plugins, schemadef as schemadef
from _typeshed import Incomplete

class SchemaDef(plugins.PythonPlugin):  # type: ignore[name-defined]
    _serializable_label: str
    def __init__(self, name=None, filepath=None) -> None: ...
    _module: Incomplete
    def module(self):
        """
        Return the module object for this schemadef plugin.
        If the module hasn't already been imported, it is imported and
        injected into the otio.schemadefs namespace as a side-effect.

        Redefines :py:meth:`.PythonPlugin.module`.
        """
    def plugin_info_map(self):
        """Adds extra schemadef-specific information to call to the parent fn.
        """
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...

def available_schemadef_names():
    """Return a string list of the available schemadefs."""
def from_name(name):
    """Fetch the schemadef plugin object by the name of the schema directly."""
def module_from_name(name):
    """Fetch the plugin's module by the name of the schemadef.

    Will load the plugin if it has not already been loaded.  Reading a file that
    contains the schemadef will also trigger a load of the plugin.
    """
