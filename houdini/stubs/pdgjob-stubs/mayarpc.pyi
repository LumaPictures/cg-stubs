from genericrpc import GenericPythonHandlerAPI
from pdgjob import pdgcmd as pdgcmd, pdgjson as pdgjson
from pdgjob.genericrpc import _ServerExtra

class MayaHandlerAPI(GenericPythonHandlerAPI):
    """API for Maya xmlproc server"""
    def shutdown(self) -> str: ...

def start_maya_server(address: str, port: int, extra: _ServerExtra = ...) -> int: ...
