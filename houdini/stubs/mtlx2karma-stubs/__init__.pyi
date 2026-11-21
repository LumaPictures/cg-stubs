import MaterialX as mx
from collections.abc import Collection, Iterable

VERBOSE: bool | int | None

def defaultPath() -> str: ...
def standardLibrariesDoc(library_path: str | None = None) -> mx.Document:
    """ Returns a MaterialX document object with loaded with the .mtlx files
        found in Houdini distribution.
    """
def findNewNodeGraphs(base_path: str, add_path: str) -> list[str]:
    """ Given two mtlx paths, find all the node graphs that only exist in
        add_path.  These are the nodes that should be saved out in the JSON
        file.
    """
def saveKarmaNodeGraphs(mtlx_doc: mx.Document, save_path: str, nodes: Collection[str], indent: int | None = None) -> None: ...
def doMerge(source_files: Iterable[str], output_file: str, indent: int | None = None) -> None: ...
def main() -> None:
    """ Main function. Parses the command line arguments and calls
        appropriate functions to execute it.
    """
