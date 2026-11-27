import _pdg
from lxml import etree as ET
from pdg.processor import PyProcessor as PyProcessor

def parse_xmlf(xmlf_local: str, parser: ET.XMLParser) -> ET._ElementTree: ...

class XmlInput(PyProcessor):
    FailModeWarn: int
    FailModeErr: int
    FailModeGenerateItem: int
    StoreStr: int
    StoreFile: int
    MatchElement: int
    MatchStr: int
    MatchInt: int
    MatchFloat: int
    MatchFile: int
    SourceUpstream: int
    SourceCustomFile: int
    SourceAttr: int
    SourceCustomStr: int
    QueryXPath: int
    QueryTagName: int
    ExtractElem: int
    ExtractText: int
    ExtractAttr: int
    MatchAny: int
    MatchChild: int
    def __init__(self, node: _pdg.Node) -> None: ...
    @classmethod
    def templateName(cls) -> str: ...
    @classmethod
    def templateBody(cls) -> str: ...
    def onConfigureNode(self, node_options: _pdg.NodeOptions) -> _pdg.result: ...
    def onGenerate(self, item_holder: _pdg.WorkItemHolder, upstream_items: _pdg.WorkItemList, generation_type: _pdg.generationType) -> _pdg.result: ...

def registerTypes(type_registry: _pdg.TypeRegistry) -> None: ...
