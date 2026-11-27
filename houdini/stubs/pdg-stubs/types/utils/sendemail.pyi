import _pdg
import pdg.processor
from collections.abc import Iterator
from contextlib import contextmanager

@contextmanager
def ssl_verify_certs_mgr(enable: bool, verifysslcerts: bool) -> Iterator[None]:
    """
    Helper for pushing and popping _https_verify_certificates, also forces
    series execution of email server access.
    """

class SendEmail(pdg.processor.PyProcessor):
    SourceUpstream: int
    SourceFilePath: int
    SourceNone: int
    EncryptionNone: int
    EncryptionTLS: int
    AuthNone: int
    AuthParms: int
    AuthFile: int
    SubTypePlain: int
    SubTypeHtml: int
    @classmethod
    def templateName(cls) -> str: ...
    @classmethod
    def templateBody(cls) -> str: ...
    def onConfigureNode(self, node_options: _pdg.NodeOptions) -> _pdg.result: ...
    def onGenerate(self, item_holder: _pdg.WorkItemHolder, upstream_items: _pdg.WorkItemList, generation_type: _pdg.generationType) -> _pdg.result: ...
    def onCookTask(self, work_item: _pdg.WorkItem) -> _pdg.result: ...

def registerTypes(type_registry: _pdg.TypeRegistry) -> None: ...
