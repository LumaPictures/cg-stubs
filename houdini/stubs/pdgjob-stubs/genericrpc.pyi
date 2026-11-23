from collections.abc import Callable as Callable, Mapping as Mapping
from houtypes import JSONLike
from io import TextIOWrapper
from pdgjob import pdgcmd as pdgcmd, pdgjson as pdgjson
from typing import Any, Concatenate, NotRequired, TypedDict
from xmlrpc.server import SimpleXMLRPCServer

from typing import TypeVar
from typing import TypeVar
_R = TypeVar('_R')
class _BinaryCallArg(TypedDict):
    b64: str

class _CallArg(TypedDict):
    arg: JSONLike

class _ServerExtra(TypedDict, total=False):
    timeout: int | str
    connectionfile: str

class _ExecResult(TypedDict):
    status: str
    result: JSONLike
    calls: NotRequired['list[_CallRecord]']
    log: NotRequired[str]

class _CallRecord(TypedDict):
    fn: str
    args: list[_BinaryCallArg | _CallArg]

theCookResultServer: str | None
theCheckForPDGPeriod: int

class StdoutBuffer(TextIOWrapper):
    def write(self, string: str) -> int: ...

class RPCProxy:
    captured_calls: list[_CallRecord]
    def __init__(self) -> None: ...
    def call(self, fn_name: str, *args: object, **kwargs: object) -> int: ...
    def commitMulti(self, name: str) -> int: ...

class XMLRPCServer(SimpleXMLRPCServer):
    timedout: bool
    finished: bool
    def serve_forever(self) -> None: ...
    def handle_timeout(self) -> None: ...
    def shutdown(self) -> int: ...

class GenericPythonHandlerAPI:
    """API for a generic python-based xmlproc server"""
    server: XMLRPCServer | None
    globals: dict[str, Any]
    def __init__(self) -> None: ...
    def shutdown(self) -> str:
        """
        shutdown host app right away
        """
    def exec_scriptfile(self, script_path: str) -> str:
        """
        Exec the given script file
        DEPRECATED
        """
    def exec_script(self, scriptbase64: str | bytes, work_item_json: str | bytes | None = None, ctx: int = 0) -> str: ...
    def _exec_script(self, code_text: str, work_item_json: str | bytes | None = None, ctx: int = 0) -> _ExecResult:
        """
        Compiles and executes the given code with some globals pre-populated.
        Returns a 'result' dict with 'status' of 'fail' or 'success'.  In 
        the former the 'result' will be the exception traceback, in the latter
        it will be 0 or the value of a global variable 'result', which is 
        in any case ignored by sendcommand.
        """

def start_command_server(server_endpoint: tuple[str, int], handler_api: GenericPythonHandlerAPI, extra: _ServerExtra = ...) -> XMLRPCServer:
    """
    Start the XMLRPC server with the given handler object

    server_endpoint : (host, port)
    handler_api: object
    extra: dict of extra arguments.  This must be forwarded from argparser.
    """
def substitute_scheduler_vars(data: str) -> str: ...
def redirect_streams(log_fname: str) -> None: ...
def main(start_server: Callable[Concatenate[str, int, _ServerExtra, ...], _R], **kwargs: object) -> _R:
    """
    parse the command line and start the server using the given callback.
    start_server: fn(host:str, port:int, extra:dict, **kwargs)
    """
