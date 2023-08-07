# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import logging
from UI4.Util.Record import Record as Record
from typing import Set, Tuple

ICON_PREFIX: str
LEVEL_NAMES: dict

class LogRecord(Record):
    def __init__(self, index: int, logRecord: logging.LogRecord) -> None: ...
    @staticmethod
    def getLevelIconName(level: int, bigger: bool = ..., highlight: bool = ...) -> str: ...
    def getLogRecord(self): ...
    def getLogRecordName(self) -> str: ...
