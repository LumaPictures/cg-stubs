# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

from typing import ClassVar

class OutputFormat:
    AS_ARCHIVE: ClassVar[str] = ...
    AS_DIRECTORY: ClassVar[str] = ...
    DEFAULT: ClassVar[str] = ...