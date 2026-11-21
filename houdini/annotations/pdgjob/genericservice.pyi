import subprocess
from typing import Never

from pdgjob import pdgcmd
from pdgjob.pdgjson import _ServiceJobInfo, _ServiceResponse, _ServiceStatus

class GenericService(pdgcmd.BaseService):
    END_TOKEN: str
    SANITIZE_VARS: tuple[str, ...]
    SANITIZE_NONE: int
    SANITIZE_SPECIFIC: int
    SANITIZE_ALL: int
    executable: str
    script: str | None
    child: subprocess.Popen[bytes] | None
    clean_env: int
    def __init__(
        self,
        executable: str,
        script: str | None,
        client_name: str,
        listener_name: str | None,
        address: str,
        port: int,
        timeout: int,
        log_file: str | None,
        clean_env: int,
    ) -> None: ...
    def start(self) -> bool: ...
    def reset_service(self) -> None: ...
    def stop_service(self) -> None: ...
    def receive_job(self, job_info: _ServiceJobInfo) -> _ServiceResponse | _ServiceStatus | dict[str, Never]: ...

def main() -> None: ...
