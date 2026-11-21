# Houdini stubs generated from Houdini 22.0.466

from typing import TextIO

class Log:
    log_to_standard_output: bool
    log_file: TextIO | None
    def __init__(self, /, *, log_to_standard_output: bool = False, log_file: TextIO | None = None) -> None: ...
    def write(self, s: str) -> None: ...
    def flush(self) -> None: ...
