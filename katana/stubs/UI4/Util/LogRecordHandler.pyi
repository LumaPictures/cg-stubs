# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import ConfigurationAPI_cmodule as Configuration
import logging
from UI4.Util.LogRecord import LogRecord as LogRecord
from typing import Set, Tuple

gLogRecordItemModel: None

class LogRecordHandler(logging.Handler):
    def __init__(self, logRecordItemModel: LogRecordItemModel) -> None: ...
    def emit(self, record: logging.LogRecord): ...
