from _typeshed import Incomplete

PATH_SEP: str
ALL_PLUGINS_TEXT: str
PUBLIC_ONLY_TEXT: str
DOCUMENT_HEADER: str
MANIFEST_CONTENT_TEMPLATE: str
LOCAL_MANIFEST_TEMPLATE: str
PLUGIN_TEMPLATE: str
ADAPTER_TEMPLATE: str
SCHEMADEF_TEMPLATE: str

def _parsed_args():
    """ parse commandline arguments with argparse """
def _format_plugin(plugin_map, extra_stuff, sanitized_paths): ...
def _format_doc(docstring, prefix):
    """Use textwrap to format a docstring for markdown."""
def _format_adapters(plugin_map): ...
def _format_schemadefs(plugin_map): ...

_PLUGIN_FORMAT_MAP: Incomplete

def _manifest_formatted(plugin_info_map, manifest_paths=None, sanitized_paths: bool = False): ...
def generate_and_write_documentation_plugins(public_only: bool = False, sanitized_paths: bool = False): ...
def main() -> None:
    """  main entry point  """
