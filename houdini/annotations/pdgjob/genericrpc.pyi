from collections.abc import Callable, Mapping
from io import TextIOWrapper
from typing import Any, Concatenate, NotRequired, TypedDict, TypeVar
from xmlrpc.server import SimpleXMLRPCServer

from houtypes import JSONLike

_R = TypeVar("_R")

class _BinaryCallArg(TypedDict):
    b64: str

class _CallArg(TypedDict):
    arg: JSONLike

class _ServerExtra(TypedDict, total=False):
    # --timeout is parsed without type=int, so it is a str when given on the command line.
    timeout: int | str
    connectionfile: str

class _ExecResult(TypedDict):
    status: str
    # 0, the traceback text, or the script's global `result`; json.dumps'd.
    result: JSONLike
    # Added by exec_script:
    calls: NotRequired["list[_CallRecord]"]
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
    finished: bool
    timedout: bool
    def serve_forever(self) -> None: ...
    def handle_timeout(self) -> None: ...
    def shutdown(self) -> int: ...

class GenericPythonHandlerAPI:
    server: XMLRPCServer | None
    globals: dict[str, Any]
    def __init__(self) -> None: ...
    def shutdown(self) -> str: ...
    def exec_scriptfile(self, script_path: str) -> str: ...
    def exec_script(
        self,
        scriptbase64: str | bytes,
        work_item_json: str | bytes | None = ...,
        ctx: int = ...,
    ) -> str: ...
    def _exec_script(
        self, code_text: str, work_item_json: str | bytes | None = ..., ctx: int = ...
    ) -> _ExecResult: ...

def start_command_server(
    server_endpoint: tuple[str, int], handler_api: GenericPythonHandlerAPI, extra: _ServerExtra = ...
) -> XMLRPCServer: ...
def substitute_scheduler_vars(data: str) -> str: ...
def redirect_streams(log_fname: str) -> None: ...
def main(start_server: Callable[Concatenate[str, int, _ServerExtra, ...], _R], **kwargs: object) -> _R: ...
