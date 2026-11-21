import subprocess
from types import ModuleType
from typing import NoReturn

eExitCodeError: int
eExitCodeWarn: int
eExitCodeRetry: int
eExitCodeIgnore: int
pdgcmd: ModuleType | None
proc: subprocess.Popen[bytes] | None

def main() -> NoReturn: ...
