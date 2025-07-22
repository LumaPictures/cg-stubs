from . import file_bundle_utils as file_bundle_utils, otio_json as otio_json
from .adapter import Adapter as Adapter

__all__ = ['Adapter', 'otio_json', 'file_bundle_utils', 'suffixes_with_defined_adapters', 'available_adapter_names', 'from_filepath', 'from_name', 'read_from_file', 'read_from_string', 'write_to_file', 'write_to_string']

def suffixes_with_defined_adapters(read: bool = False, write: bool = False):
    """Return a set of all the suffixes that have adapters defined for them."""
def available_adapter_names():
    """Return a string list of the available adapters."""
def from_filepath(filepath):
    """Guess the adapter object to use for a given filepath.

    For example, ``foo.otio`` returns the ``otio_json`` adapter.
    """
def from_name(name):
    """Fetch the adapter object by the name of the adapter directly."""
def read_from_file(filepath, adapter_name=None, media_linker_name=..., media_linker_argument_map=None, **adapter_argument_map):
    '''Read filepath using adapter_name.

    If adapter_name is None, try and infer the adapter name from the filepath.

    .. code-block:: python
       :caption: Example

        timeline = read_from_file("example_trailer.otio")
        timeline = read_from_file("file_with_no_extension", "cmx_3600")
    '''
def read_from_string(input_str, adapter_name: str = 'otio_json', media_linker_name=..., media_linker_argument_map=None, **adapter_argument_map):
    '''Read a timeline from input_str using adapter_name.

    This is useful if you obtain a timeline from someplace other than the
    filesystem.

    .. code-block:: python
       :caption: Example

        raw_text = urlopen(my_url).read()
        timeline = read_from_string(raw_text, "otio_json")
    '''
def write_to_file(input_otio, filepath, adapter_name=None, **adapter_argument_map):
    '''Write input_otio to filepath using adapter_name.

    If adapter_name is None, infer the adapter_name to use based on the
    filepath.

    .. code-block:: python
       :caption: Example

        otio.adapters.write_to_file(my_timeline, "output.otio")
    '''
def write_to_string(input_otio, adapter_name: str = 'otio_json', **adapter_argument_map):
    '''Return input_otio written to a string using adapter_name.

    .. code-block:: python
       :caption: Example

        raw_text = otio.adapters.write_to_string(my_timeline, "otio_json")
    '''
