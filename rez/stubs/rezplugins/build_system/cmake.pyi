import argparse
from _typeshed import Incomplete
from rez.build_system import BuildResult, BuildSystem
from rez.exceptions import BuildSystemError
from rez.packages import Variant
from rez.resolved_context import ResolvedContext
from typing import Any

class RezCMakeError(BuildSystemError): ...

class CMakeBuildSystem(BuildSystem):
    """The CMake build system.

    The 'cmake' executable is run within the build environment. Rez supplies a
    library of cmake macros in the 'cmake_files' directory; these are added to
    cmake's searchpath and are available to use in your own CMakeLists.txt
    file.

    The following CMake variables are available:
    - REZ_BUILD_TYPE: One of 'local', 'central'. Describes whether an install
      is going to the local packages path, or the release packages path.
    - REZ_BUILD_INSTALL: One of 0 or 1. If 1, an installation is taking place;
      if 0, just a build is occurring.
    """
    build_systems: Incomplete
    build_targets: Incomplete
    schema_dict: Incomplete
    @classmethod
    def name(cls) -> str: ...
    @classmethod
    def child_build_system(cls) -> str: ...
    @classmethod
    def is_valid_root(cls, path, package: Incomplete | None = None): ...
    @classmethod
    def bind_cli(cls, parser: argparse.ArgumentParser, group: argparse._ArgumentGroup) -> None: ...
    settings: Any
    build_target: Any
    cmake_build_system: Any
    def __init__(self, working_dir: str, opts: Incomplete | None = None, package: Incomplete | None = None, write_build_scripts: bool = False, verbose: bool = False, build_args=[], child_build_args=[]) -> None: ...
    def build(self, context: ResolvedContext, variant: Variant, build_path: str, install_path: str, install: bool = False, build_type=...) -> BuildResult: ...
    @classmethod
    def _add_build_actions(cls, executor, context, package, variant, build_type, install, build_path, install_path: Incomplete | None = None) -> None: ...

def _FWD__spawn_build_shell(working_dir, build_path, variant_index, install, install_path: Incomplete | None = None) -> None: ...
def register_plugin(): ...
