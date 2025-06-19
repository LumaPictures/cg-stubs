import argparse
from _typeshed import Incomplete
from rez.build_system import BuildResult, BuildSystem
from rez.packages import Variant
from rez.resolved_context import ResolvedContext
from rez.rex import RexExecutor

class CustomBuildSystem(BuildSystem):
    '''This build system runs the \'build_command\' defined in a package.py.

    For example, consider the package.py snippet:

        build_commands = "bash {root}/build.sh {install}"

    This will run the given bash command in the build path - this is typically
    located somewhere under the \'build\' dir under the root dir containing the
    package.py.

    The following variables are available for expansion:

    * root: The source directory (the one containing the package.py).
    * install: \'install\' if an install is occurring, or the empty string (\'\')
      otherwise;
    * build_path: The build path (this will also be the cwd);
    * install_path: Full path to install destination;
    * name: Name of the package getting built;
    * variant_index: Index of the current variant getting built, or an empty
      string (\'\') if no variants are present.
    * version: Package version currently getting built.
    '''
    @classmethod
    def name(cls) -> str: ...
    @classmethod
    def is_valid_root(cls, path, package: Incomplete | None = None) -> bool: ...
    def __init__(self, working_dir, opts: Incomplete | None = None, package: Incomplete | None = None, write_build_scripts: bool = False, verbose: bool = False, build_args=[], child_build_args=[]) -> None: ...
    @classmethod
    def bind_cli(cls, parser: argparse.ArgumentParser, group: argparse._ArgumentGroup) -> None:
        """
        Uses a 'parse_build_args.py' file to add options, if found.
        """
    def build(self, context: ResolvedContext, variant: Variant, build_path: str, install_path: str, install: bool = False, build_type=...) -> BuildResult:
        """Perform the build.

        Note that most of the func args aren't used here - that's because this
        info is already passed to the custom build command via environment
        variables.
        """
    @classmethod
    def _add_build_actions(cls, executor: RexExecutor, context: ResolvedContext, package, variant, build_type, install, build_path, install_path: Incomplete | None = None) -> None: ...

def _FWD__spawn_build_shell(working_dir, build_path, variant_index, install, install_path: Incomplete | None = None) -> None: ...
def register_plugin(): ...
