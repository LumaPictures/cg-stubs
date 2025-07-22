from .. import core as core, exceptions as exceptions
from _typeshed import Incomplete

OTIO_PLUGIN_TYPES: Incomplete

def plugin_entry_points():
    """Returns the list of entry points for all available OpenTimelineIO
    plugins.
    """
def manifest_from_file(filepath):
    """Read the .json file at filepath into a :py:class:`Manifest` object."""
def manifest_from_string(input_string):
    """Deserialize the json string into a manifest object."""

class Manifest(core.SerializableObject):  # type: ignore[name-defined]
    """Defines an OTIO plugin Manifest.

    This is considered an internal OTIO implementation detail.

    A manifest tracks a collection of plugins and enables finding them by name
    or other features (in the case of adapters, what file suffixes they
    advertise support for).

    For more information, consult the documenation.
    """
    _serializable_label: str
    adapters: Incomplete
    schemadefs: Incomplete
    media_linkers: Incomplete
    source_files: Incomplete
    hooks: Incomplete
    hook_scripts: Incomplete
    version_manifests: Incomplete
    def __init__(self) -> None: ...
    def extend(self, another_manifest) -> None:
        """
        Aggregate another manifest's plugins into this one.

        During startup, OTIO will deserialize the individual manifest JSON files
        and use this function to concatenate them together.
        """
    def _update_plugin_source(self, path) -> None:
        """Set the source file path for the manifest."""
    def from_filepath(self, suffix):
        """Return the adapter object associated with a given file suffix."""
    def adapter_module_from_suffix(self, suffix):
        """Return the adapter module associated with a given file suffix."""
    def from_name(self, name, kind_list: str = 'adapters'):
        """Return the plugin object associated with a given plugin name."""
    def adapter_module_from_name(self, name):
        """Return the adapter module associated with a given adapter name."""
    def schemadef_module_from_name(self, name):
        """Return the schemadef module associated with a given schemadef name."""

_MANIFEST: Incomplete

def load_manifest():
    """Walk the plugin manifest discovery systems and accumulate manifests.

    The order of loading (and precedence) is:

       1. Manifests specified via the :term:`OTIO_PLUGIN_MANIFEST_PATH` variable
       2. Entrypoint based plugin manifests
       3. Builtin plugin manifest
    """
def ActiveManifest(force_reload: bool = False):
    """Return the fully resolved plugin manifest."""
