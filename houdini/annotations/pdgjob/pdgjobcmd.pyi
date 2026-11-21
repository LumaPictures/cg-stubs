import subprocess
from types import ModuleType
from typing import NoReturn

pdgcmd: ModuleType | None
eExitCodeError: int
eExitCodeWarn: int
eExitCodeRetry: int
eExitCodeIgnore: int
proc: subprocess.Popen[bytes] | None

def main() -> NoReturn: ...
