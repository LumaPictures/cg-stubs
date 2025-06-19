from _typeshed import Incomplete
from rez.bind._utils import check_version as check_version, make_dirs as make_dirs
from rez.package_maker import make_package as make_package
from rez.utils.execution import ExecutableScriptMode as ExecutableScriptMode, create_executable_script as create_executable_script
from rez.utils.lint_helper import env as env  # type: ignore[attr-defined]
from rez.vendor.distlib.scripts import ScriptMaker as ScriptMaker  # type: ignore[import-not-found]
from rez.version import Version as Version

def commands() -> None: ...
def hello_world_source() -> None: ...
def bind(path, version_range: Incomplete | None = None, opts: Incomplete | None = None, parser: Incomplete | None = None): ...
