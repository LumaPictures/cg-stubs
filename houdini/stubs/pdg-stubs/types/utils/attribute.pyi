import _pdg
from pdg.node import PyNode as PyNode
from pdg.processor import PyProcessor as PyProcessor

class AttributeCreate(PyProcessor):
    EmptyCreate: int
    EmptyIgnore: int
    EmptyWarning: int
    EmptyError: int
    Overwrite: int
    Update: int
    Warn: int
    Error: int
    Keep: int
    NoCheck: int
    ErrorCheck: int
    WarnCheck: int
    GenerateCheck: int
    CookCheck: int
    CreateFile: int
    CreateAttrib: int
    ScopeWorkItem: int
    ScopeGraphBound: int
    ScopeGraphGlobal: int
    CopyNever: int
    CopyAlways: int
    CopyConditional: int
    @classmethod
    def templateName(cls) -> str: ...
    @classmethod
    def templateBody(cls) -> str: ...
    def onConfigureNode(self, node_options: _pdg.NodeOptions) -> _pdg.result: ...
    def onGenerate(self, item_holder: _pdg.WorkItemHolder, upstream_items: _pdg.WorkItemList, generation_type: _pdg.generationType) -> _pdg.result: ...
    def onPostCookTask(self, work_item: _pdg.WorkItem) -> _pdg.result: ...

class PatternAttribParser:
    AttribFloat: int
    AttribInt: int
    AttribString: int
    AttribNone: int
    SimplePattern: int
    RegularExpression: int
    use_custom: bool
    infer_type: bool
    always_create: bool
    match_pattern: str
    match_attribs: list[tuple[str, str, int]]
    @staticmethod
    def attribNames(node: PyNode, pattern: str, use_custom: int) -> list[str]: ...
    def __init__(self, pattern: str, use_custom: bool, infer_type: bool, always_create: bool) -> None: ...
    def workItemsFromString(self, node: PyNode, source_string: str, item_holder: _pdg.WorkItemHolder, upstream_item: _pdg.WorkItem | None) -> tuple[_pdg.WorkItem | list[_pdg.WorkItem], list[str]]: ...

class DelimiterAttribParser:
    DelimString: int
    DelimChar: int
    DelimRegex: int
    StorageArray: int
    StorageWorkItem: int
    storage: int
    trim: bool
    pattern: str
    def __init__(self, delimiter: str, delimiter_type: int, storage: int, trim: bool) -> None: ...
    @staticmethod
    def attribNames(node: PyNode) -> list[str]: ...
    def workItemsFromString(self, node: PyNode, source_string: str, item_holder: _pdg.WorkItemHolder, upstream_item: _pdg.WorkItem | None) -> tuple[list[_pdg.WorkItem], list[str]]: ...

class AttributeFromString(PyProcessor):
    AttribFloat: int
    AttribInt: int
    AttribString: int
    AttribNone: int
    OpPattern: int
    OpDelimiter: int
    @classmethod
    def templateName(cls) -> str: ...
    @classmethod
    def templateBody(cls) -> str: ...
    def onConfigureNode(self, node_options: _pdg.NodeOptions) -> _pdg.result: ...
    def onGenerate(self, item_holder: _pdg.WorkItemHolder, upstream_items: _pdg.WorkItemList, generation_type: _pdg.generationType) -> _pdg.result: ...

class AttributeFromFile(PyProcessor):
    ReportNone: int
    ReportWarning: int
    ReportError: int
    @classmethod
    def templateName(cls) -> str: ...
    @classmethod
    def templateBody(cls) -> str: ...
    def onGenerate(self, item_holder: _pdg.WorkItemHolder, upstream_items: _pdg.WorkItemList, generation_type: _pdg.generationType) -> _pdg.result: ...
    def onConfigureNode(self, node_options: _pdg.NodeOptions) -> _pdg.result: ...

class AttributeRandomize(PyProcessor):
    Replace: int
    Update: int
    Append: int
    Prepend: int
    Warn: int
    Error: int
    Keep: int
    UniformContinuous: int
    UniformDiscrete: int
    TwoValues: int
    Normal: int
    Exponential: int
    LogNormal: int
    CustomDiscrete: int
    @classmethod
    def templateName(cls) -> str: ...
    @classmethod
    def templateBody(cls) -> str: ...
    def onConfigureNode(self, node_options: _pdg.NodeOptions) -> _pdg.result: ...
    def onGenerate(self, item_holder: _pdg.WorkItemHolder, upstream_items: _pdg.WorkItemList, generation_type: _pdg.generationType) -> _pdg.result: ...

def registerTypes(type_registry: _pdg.TypeRegistry) -> None: ...
