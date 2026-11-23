from collections.abc import Callable, Mapping
from typing import Any, Never

from pdgjob import pdgcmd
from pdgjob.pdgjson import NativeWorkItem, WorkItem, _ServiceJobInfo, _ServiceResponse, _ServiceStatus

class PythonScriptService(pdgcmd.BaseService):
    CookTaskScript: str
    as_native: bool
    apply_wedges: bool
    local_dict: dict[str, Any]
    def __init__(
        self,
        client_name: str,
        listener_name: str | None,
        address: str,
        port: int,
        timeout: int,
        log_file: str | None,
        as_native: bool,
        apply_wedges: bool,
    ) -> None: ...
    def start(self) -> bool: ...
    def reset_service(self) -> None: ...
    def receive_job(self, job_info: _ServiceJobInfo) -> _ServiceResponse | _ServiceStatus | dict[str, Never]: ...
    @classmethod
    def extract_script(
        cls, job_info: _ServiceJobInfo, work_item: WorkItem | NativeWorkItem
    ) -> str | bytes | None: ...
    @classmethod
    def configure_path(cls, work_item: WorkItem | NativeWorkItem) -> None: ...
    @classmethod
    def run_job(
        cls,
        job_info: _ServiceJobInfo,
        local_dict: dict[str, Any],
        redirect: bool = ...,
        handlers: Mapping[str, Callable[[str], object]] | Mapping[bytes, Callable[[bytes], object]] | None = ...,
        as_native: bool = ...,
        apply_wedges: bool = ...,
    ) -> _ServiceResponse | _ServiceStatus | dict[str, Never]: ...

def main() -> None: ...
