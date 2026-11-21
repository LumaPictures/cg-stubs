import shotgun_api3
from pdgjob.genericrpc import GenericPythonHandlerAPI, _ServerExtra

api_path: str


def report_result_data(result_server: str | None, item_name: str | None, data: object, tag: str) -> None: ...

class ShotgunHandlerAPI(GenericPythonHandlerAPI):
    sg: shotgun_api3.Shotgun
    def __init__(self, sg: shotgun_api3.Shotgun) -> None: ...
    def shutdown(self) -> str: ...

def start_shotgun_server(
    address: str,
    port: int,
    extra: _ServerExtra,
    shotgun_url: str,
    httpproxy: str | None = ...,
    cacerts: str | None = ...,
) -> None: ...
