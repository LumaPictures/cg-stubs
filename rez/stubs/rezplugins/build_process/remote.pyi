from _typeshed import Incomplete
from rez.build_process import BuildProcessHelper

class RemoteBuildProcess(BuildProcessHelper):
    """The default build process.

    This process builds a package's variants sequentially, on remote hosts.
    """
    @classmethod
    def name(cls): ...
    def build(self, install_path: Incomplete | None = None, clean: bool = False, install: bool = False, variants: Incomplete | None = None) -> None: ...
    def release(self, release_message: Incomplete | None = None, variants: Incomplete | None = None) -> None: ...

def register_plugin(): ...
