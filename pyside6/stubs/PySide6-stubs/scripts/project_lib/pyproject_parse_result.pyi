from dataclasses import dataclass, field
from pathlib import Path

@dataclass
class PyProjectParseResult:
    errors: list[str] = field(default_factory=list)
    files: list[Path] = field(default_factory=list)
