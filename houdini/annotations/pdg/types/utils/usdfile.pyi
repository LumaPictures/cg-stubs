import threading

import _pdg
from pdg.processor import PyProcessor

USDs: int
NonUSDs: int
Both: int
Flattened: int
Recursive: int
Single: int
CustomFilePath: int
UpstreamFile: int

generate_lock: threading.Lock

class LayerVisitor:
    mode: int
    recurse: bool
    node: PyProcessor
    def __init__(self, mode: int, node: PyProcessor) -> None: ...
    def collect(self, usdfile: str) -> None: ...

class PrimVisitor(LayerVisitor):
    prims: list[tuple[str, str]]
    def __init__(self, mode: int, node: PyProcessor) -> None: ...
    def collect(self, usdfile: str) -> None: ...

class FileCollector(LayerVisitor):
    asset_paths: set[str]
    layer_paths: set[str]
    usdfilepath: str | None
    filetypes: int
    time: float | None
    collect_usds: bool
    collect_assetpaths: bool
    def __init__(
        self, mode: int, filetypes: int, node: PyProcessor, time: float | None = ...
    ) -> None: ...
    def collect(self, usdfile: str) -> None: ...

class USDImportFiles(PyProcessor):
    @classmethod
    def templateName(cls) -> str: ...
    @classmethod
    def templateBody(cls) -> str: ...
    def onConfigureNode(self, node_options: _pdg.NodeOptions) -> _pdg.result: ...
    def onGenerate(
        self,
        item_holder: _pdg.WorkItemHolder,
        upstream_items: _pdg.WorkItemList,
        generation_type: _pdg.generationType,
    ) -> _pdg.result: ...

class USDImportPrimitives(PyProcessor):
    @classmethod
    def templateName(cls) -> str: ...
    @classmethod
    def templateBody(cls) -> str: ...
    def onConfigureNode(self, node_options: _pdg.NodeOptions) -> _pdg.result: ...
    def onGenerate(
        self,
        item_holder: _pdg.WorkItemHolder,
        upstream_items: _pdg.WorkItemList,
        generation_type: _pdg.generationType,
    ) -> _pdg.result: ...

def registerTypes(type_registry: _pdg.TypeRegistry) -> None: ...
