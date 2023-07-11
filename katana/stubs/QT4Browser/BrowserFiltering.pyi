# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import re
from typing import Set, Tuple

__filter_re: re.Pattern

def Match(string, filter): ...
def MatchWithDescription(string, filter): ...
