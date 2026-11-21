from collections.abc import Iterable

import MaterialX as mx

def defaultPath() -> str: ...
def standardLibrariesDoc(library_path: str | None = ...) -> mx.Document: ...
def shaderNodeNames(mtlx_doc: mx.Document) -> list[str]: ...
def createHDAs(
    mtlx_doc: mx.Document,
    mtlx_node_names: Iterable[str],
    hda_file_or_dir_name: str | None,
    should_append_hda: bool = ...,
    should_output_dir: bool = ...,
    should_create_metadata_parms: bool = ...,
    should_output_ds_only: bool = ...,
) -> None: ...
def createHDA(
    hda_name: str,
    hda_label: str,
    mtlx_doc: mx.Document,
    mtlx_node_or_nodedef_name: str | Iterable[str],
    hda_file_or_dir_name: str | None,
    should_append_hda: bool = ...,
    should_output_dir: bool = ...,
    should_create_metadata_parms: bool = ...,
    should_output_ds_only: bool = ...,
) -> None: ...
def main() -> None: ...
