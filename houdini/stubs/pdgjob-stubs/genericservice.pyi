# Houdini stubs generated from Houdini 22.0.466

import subprocess
from pdgjob import pdgcmd as pdgcmd, pdgjson as pdgjson
from pdgjob.pdgjson import _ServiceJobInfo, _ServiceResponse, _ServiceStatus
from typing import Never

class GenericService(pdgcmd.BaseService):
    SANITIZE_NONE: int
    SANITIZE_SPECIFIC: int
    SANITIZE_ALL: int
    executable: str
    script: str | None
    child: subprocess.Popen[bytes] | None
    clean_env: int
    END_TOKEN: str
    SANITIZE_VARS: tuple[str, ...]
    def __init__(self, executable: str, script: str | None, client_name: str, listener_name: str | None, address: str, port: int, timeout: int, log_file: str | None, clean_env: int) -> None: ...
    def start(self) -> bool: ...
    def reset_service(self) -> None: ...
    def stop_service(self) -> None: ...
    def receive_job(self, job_info: _ServiceJobInfo) -> _ServiceResponse | _ServiceStatus | dict[str, Never]: ...

def main() -> None: ...
