# Houdini stubs generated from Houdini 22.0.466

import shotgun_api3
from pdgjob import pdgcmd as pdgcmd
from pdgjob.genericrpc import GenericPythonHandlerAPI as GenericPythonHandlerAPI, _ServerExtra, main as main, start_command_server as start_command_server

api_path: str

def report_result_data(result_server: str | None, item_name: str | None, data: object, tag: str) -> None: ...

class ShotgunHandlerAPI(GenericPythonHandlerAPI):
    """API for Shotgun xmlproc server"""
    sg: shotgun_api3.Shotgun
    def __init__(self, sg: shotgun_api3.Shotgun) -> None: ...
    def shutdown(self) -> str: ...

def start_shotgun_server(address: str, port: int, extra: _ServerExtra, shotgun_url: str, httpproxy: str | None = None, cacerts: str | None = None) -> None: ...
