# Houdini stubs generated from Houdini 22.0.466

import MaterialX as mx
from collections.abc import Iterable

def defaultPath() -> str: ...
def standardLibrariesDoc(library_path: str | None = None) -> mx.Document:
    """ Returns a MaterialX document object with loaded with the .mtlx files
        found in Houdini distribution.
    """
def shaderNodeNames(mtlx_doc: mx.Document) -> list[str]:
    """ Returns the names of the MaterialX shaders available in the given
        document.
    """
def createHDAs(mtlx_doc: mx.Document, mtlx_node_names: Iterable[str], hda_file_or_dir_name: str | None, should_append_hda: bool = True, should_output_dir: bool = False, should_create_metadata_parms: bool = True, should_output_ds_only: bool = False) -> None:
    """ Creates HDAs for the specified MaterialX shaders and saves them
        in a file or an expanded directory format.

        The MaterialX shaders must be found in the Houdini distribution.
    """
def createHDA(hda_name: str, hda_label: str, mtlx_doc: mx.Document, mtlx_node_or_nodedef_name: str | Iterable[str], hda_file_or_dir_name: str | None, should_append_hda: bool = True, should_output_dir: bool = False, should_create_metadata_parms: bool = True, should_output_ds_only: bool = False) -> None:
    """ Create an HDA for the given MaterialX shader node name,
        that can be found in the given MaterialX document object,
        and save it in the given file or expanded directory.

        The `mtlx_node_or_nodedef_name` can be a shader name, in which case 
        all its node definitions become signatures of the HDA, or it can be a
        node definition name, in which case the HDA will represent just that
        definition, or it can be a list of node definition names, in which case
        only these explicit definitions will become the signatures of the HDA.
    """
def main() -> None:
    """ Main function. Parses the command line arguments and calls
        appropriate functions to execute it.
    """
