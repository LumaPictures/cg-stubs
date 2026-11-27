import _pdg
from .commandchain import GenerativeSendCommand as GenerativeSendCommand

class ShotgunUpload(GenerativeSendCommand):
    """A node for uploading files to Shotgun."""
    def __init__(self, node: _pdg.Node) -> None: ...
    @classmethod
    def templateName(cls) -> str:
        """Template name of this node."""
    @classmethod
    def templateBody(cls) -> str:
        """Template that defines the interface for this node."""
    def getCommandString(self, work_item: _pdg.WorkItem) -> str: ...

class ShotgunCreate(GenerativeSendCommand):
    """A node for creating Shotgun entities."""
    def __init__(self, node: _pdg.Node) -> None: ...
    @classmethod
    def templateName(cls) -> str:
        """Template name of this node."""
    @classmethod
    def templateBody(cls) -> str:
        """Template that defines the interface for this node."""
    def getCommandString(self, work_item: _pdg.WorkItem) -> str: ...

class ShotgunFind(GenerativeSendCommand):
    """A node for finding Shotgun entities."""
    def __init__(self, node: _pdg.Node) -> None: ...
    @classmethod
    def templateName(cls) -> str:
        """Template name of this node."""
    @classmethod
    def templateBody(cls) -> str:
        """Template that defines the interface for this node."""
    def getCommandString(self, work_item: _pdg.WorkItem) -> str: ...

class ShotgunDownload(GenerativeSendCommand):
    """A node for downloading files from Shotgun."""
    def __init__(self, node: _pdg.Node) -> None: ...
    @classmethod
    def templateName(cls) -> str:
        """Template name of this node."""
    @classmethod
    def templateBody(cls) -> str:
        """Template that defines the interface for this node."""
    def getCommandString(self, work_item: _pdg.WorkItem) -> str: ...

class ShotgunUpdate(GenerativeSendCommand):
    """A node for updating Shotgun entities."""
    def __init__(self, node: _pdg.Node) -> None: ...
    @classmethod
    def templateName(cls) -> str:
        """Template name of this node."""
    @classmethod
    def templateBody(cls) -> str:
        """Template that defines the interface for this node."""
    def getCommandString(self, work_item: _pdg.WorkItem) -> str: ...

class ShotgunDelete(GenerativeSendCommand):
    """A node for updating Shotgun entities."""
    def __init__(self, node: _pdg.Node) -> None: ...
    @classmethod
    def templateName(cls) -> str:
        """Template name of this node."""
    @classmethod
    def templateBody(cls) -> str:
        """Template that defines the interface for this node."""
    def getCommandString(self, work_item: _pdg.WorkItem) -> str: ...

def registerTypes(type_registry: _pdg.TypeRegistry) -> None:
    """Register all types defined in this module with the type registry."""
