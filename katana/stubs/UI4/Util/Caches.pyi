# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import CacheManager as CacheManager
import RenderingAPI as RenderingAPI
import Nodes3DAPI.ScenegraphManager as ScenegraphManager
import Utils as Utils
from typing import Set, Tuple

g_flushing_in_progress: bool

def FlushCaches(): ...
