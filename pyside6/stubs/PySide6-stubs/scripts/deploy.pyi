from _typeshed import Incomplete
from pathlib import Path

TOOL_DESCRIPTION: Incomplete
HELP_MODE: Incomplete

def main(main_file: Path = None, name: str = None, config_file: Path = None, init: bool = False, loglevel=..., dry_run: bool = False, keep_deployment_files: bool = False, force: bool = False, extra_ignore_dirs: str = None, extra_modules_grouped: str = None, mode: str = None) -> str | None: ...  # type: ignore[assignment]
