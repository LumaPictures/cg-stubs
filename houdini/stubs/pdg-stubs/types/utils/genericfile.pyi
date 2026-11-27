import _pdg
import ssl
from collections.abc import Callable as Callable
from pdg import PyProcessor as PyProcessor

def indexed_str(s: str, index: int) -> str:
    '''
    String-append the index to the string s.

    s: string
    index: integer

    eg. indexed_str("foobar", 1) -> "foobar1"
    '''

class FilePattern(PyProcessor):
    '''
    Generates generic workitems from files based on a glob pattern.
    Each matching file path results in a workitem which has a
    "file" tagged result data.
    '''
    def __init__(self, node: _pdg.Node) -> None: ...
    @classmethod
    def templateName(cls) -> str: ...
    @classmethod
    def templateBody(cls) -> str: ...
    def onConfigureNode(self, node_options: _pdg.NodeOptions) -> _pdg.result: ...
    def onGenerate(self, item_holder: _pdg.WorkItemHolder, upstream_items: _pdg.WorkItemList, generation_type: _pdg.generationType) -> _pdg.result: ...

class FileCopy(PyProcessor):
    """
    Copies a file.
    """
    SourceUpstream: int
    SourceCustom: int
    DestDir: int
    DestFile: int
    def __init__(self, node: _pdg.Node) -> None: ...
    @classmethod
    def templateName(cls) -> str: ...
    @classmethod
    def templateBody(cls) -> str: ...
    def onConfigureNode(self, node_options: _pdg.NodeOptions) -> _pdg.result: ...
    def onGenerate(self, item_holder: _pdg.WorkItemHolder, upstream_items: _pdg.WorkItemList, generation_type: _pdg.generationType) -> _pdg.result: ...
    def onPrepareTask(self, work_item: _pdg.WorkItem) -> None: ...

class FileRemove(PyProcessor):
    """
    Removes files or directories.
    """
    ALL_INPUTS: int
    DELETED_FILES: int
    EXTANT_INPUTS: int
    NO_FILES: int
    FILEPATH: int
    RESULTDATA: int
    @classmethod
    def templateName(cls) -> str: ...
    @classmethod
    def templateBody(cls) -> str: ...
    def onConfigureNode(self, node_options: _pdg.NodeOptions) -> _pdg.result: ...
    def onGenerate(self, item_holder: _pdg.WorkItemHolder, upstream_items: _pdg.WorkItemList, generation_type: _pdg.generationType) -> _pdg.result: ...
    def onCookTask(self, work_item: _pdg.WorkItem) -> _pdg.result: ...

class MakeDir(PyProcessor):
    OutputsKeep: int
    OutputsAppend: int
    OutputsReplace: int
    @classmethod
    def templateName(cls) -> str: ...
    @classmethod
    def templateBody(cls) -> str: ...
    def onGenerate(self, item_holder: _pdg.WorkItemHolder, upstream_items: _pdg.WorkItemList, generation_type: _pdg.generationType) -> _pdg.result: ...

class ScopedSSLVerify:
    """
    Helper for pushing and popping _https_verify_certificates
    """
    saved_cdc: Callable[..., ssl.SSLContext]
    verifysslcerts: int | None
    def __init__(self, work_item: _pdg.WorkItem) -> None: ...
    def __del__(self) -> None: ...

class DownloadFile(PyProcessor):
    verifysslcerts: bool
    def __init__(self, node: _pdg.Node) -> None: ...
    @classmethod
    def templateName(cls) -> str: ...
    @classmethod
    def templateBody(cls) -> str: ...
    def onConfigureNode(self, node_options: _pdg.NodeOptions) -> _pdg.result: ...
    def onGenerate(self, item_holder: _pdg.WorkItemHolder, upstream_items: _pdg.WorkItemList, generation_type: _pdg.generationType) -> _pdg.result: ...
    def onCookTask(self, work_item: _pdg.WorkItem) -> None: ...
    def addUrl(self, url: str, filename: str = '', _data_tag: str | None = None) -> None:
        """
        Add a url to the list to be downloaded.

        url      - string url of file
        filename - filename to use for the downloaded file.
                   None means guess from the URL.
        data_tag - string like 'file/image'.
                   None means guess from extension.
        """

class FileRename(PyProcessor):
    SourceUpstream: int
    SourceCustom: int
    def __init__(self, node: _pdg.Node) -> None: ...
    @classmethod
    def templateName(cls) -> str: ...
    @classmethod
    def templateBody(cls) -> str: ...
    def onConfigureNode(self, node_options: _pdg.NodeOptions) -> _pdg.result: ...
    def onGenerate(self, item_holder: _pdg.WorkItemHolder, upstream_items: _pdg.WorkItemList, generation_type: _pdg.generationType) -> _pdg.result: ...
    def onPrepareTask(self, work_item: _pdg.WorkItem) -> None: ...

def registerTypes(type_registry: _pdg.TypeRegistry) -> None: ...
