# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import UI4.Util.NotificationManager as NotificationManager
import Utils as Utils
from typing import Set, Tuple

def _TooNewFileOpenedListener(eventType, eventID, sourceFile, sourceVersion, currentVersion): ...
