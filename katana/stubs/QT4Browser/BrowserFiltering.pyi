# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import re

__filter_re: re.Pattern

def Match(string, filter): ...
def MatchWithDescription(string, filter): ...