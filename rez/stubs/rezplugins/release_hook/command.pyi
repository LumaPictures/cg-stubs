from _typeshed import Incomplete
from rez.release_hook import ReleaseHook

class CommandReleaseHook(ReleaseHook):
    commands_schema: Incomplete
    schema_dict: Incomplete
    @classmethod
    def name(cls) -> str: ...  # type: ignore[override]
    def __init__(self, source_path) -> None: ...
    def execute_command(self, cmd_name, cmd_arguments, user, errors, env: Incomplete | None = None): ...
    def pre_build(self, user, install_path, variants: Incomplete | None = None, **kwargs) -> None: ...  # type: ignore[override]
    def pre_release(self, user, install_path, variants: Incomplete | None = None, **kwargs) -> None: ...  # type: ignore[override]
    def post_release(self, user, install_path, variants, **kwargs) -> None: ...  # type: ignore[override]
    def _execute_commands(self, commands, install_path, package, errors: Incomplete | None = None, variants: Incomplete | None = None) -> None: ...

def register_plugin(): ...
