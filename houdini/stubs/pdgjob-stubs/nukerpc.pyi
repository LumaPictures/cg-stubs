# Houdini stubs generated from Houdini 22.0.466

from genericrpc import GenericPythonHandlerAPI
from pdgjob.genericrpc import _ServerExtra

class NukeHandlerAPI(GenericPythonHandlerAPI):
    """API for Nuke xmlproc server"""
    def shutdown(self) -> str: ...

def start_nuke_server(address: str, port: int, extra: _ServerExtra = ...) -> int: ...
