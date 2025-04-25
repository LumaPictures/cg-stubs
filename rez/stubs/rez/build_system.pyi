import argparse
import rez.developer_package
import typing
from _typeshed import Incomplete
from rez.build_process import BuildType as BuildType
from rez.developer_package import DeveloperPackage as DeveloperPackage
from rez.exceptions import BuildSystemError as BuildSystemError
from rez.packages import Package as Package, Variant as Variant, get_developer_package as get_developer_package
from rez.resolved_context import ResolvedContext as ResolvedContext
from rez.rex import RexExecutor as RexExecutor
from rez.rex_bindings import VariantBinding as VariantBinding
from typing import Sequence, TypedDict

class BuildResult(TypedDict, total=False):
    success: bool
    extra_files: list[str]
    build_env_script: str

def get_buildsys_types() -> list[str]:
    """Returns the available build system implementations - cmake, make etc."""
def get_valid_build_systems(working_dir: str, package: DeveloperPackage | None = None) -> list[type[BuildSystem]]:
    """Returns the build system classes that could build the source in given dir.

    Args:
        working_dir (str): Dir containing the package definition and potentially
            build files.
        package (`Package`): Package to be built. This may or may not be needed
            to determine the build system. For eg, cmake just has to look for
            a CMakeLists.txt file, whereas the 'build_command' package field
            must be present for the 'custom' build system type.

    Returns:
        list[type[BuildSystem]]: Valid build system class types.
    """
def create_build_system(working_dir: str, buildsys_type: str | None = None, package: DeveloperPackage | None = None, opts: argparse.Namespace | None = None, write_build_scripts: bool = False, verbose: bool = False, build_args=[], child_build_args=[]) -> BuildSystem:
    """Return a new build system that can build the source in working_dir."""

class BuildSystem:
    """A build system, such as cmake, make, Scons etc.
    """
    @classmethod
    def name(cls) -> str:
        """Return the name of the build system, eg 'make'."""
    working_dir: str
    package: rez.developer_package.DeveloperPackage
    write_build_scripts: bool
    build_args: typing.Sequence[str]
    child_build_args: list[str]
    verbose: bool
    opts: argparse.Namespace | None
    def __init__(self, working_dir: str, opts: argparse.Namespace | None = None, package: DeveloperPackage | None = None, write_build_scripts: bool = False, verbose: bool = False, build_args: Sequence[str] = [], child_build_args: list[str] = []) -> None:
        """Create a build system instance.

        Args:
            working_dir: Directory to build source from.
            opts: argparse.Namespace object which may contain constructor
                params, as set by our bind_cli() classmethod.
            package (`DeveloperPackage`): Package to build. If None, defaults to
                the package in the working directory.
            write_build_scripts: If True, create build scripts rather than
                perform the full build. The user can then run these scripts to
                place themselves into a build environment and invoke the build
                system directly.
            build_args: Extra cli build arguments.
            child_build_args: Extra cli args for child build system, ignored if
                there is no child build system.
        """
    @classmethod
    def is_valid_root(cls, path: str, package: Incomplete | None = None) -> bool:
        """Return True if this build system can build the source in path."""
    @classmethod
    def child_build_system(cls) -> str | None:
        """Returns the child build system.

        Some build systems, such as cmake, don't build the source directly.
        Instead, they build an interim set of build scripts that are then
        consumed by a second build system (such as make). You should implement
        this method if that's the case.

        Returns:
            Name of build system (corresponding to the plugin name) if this
            system has a child system, or None otherwise.
        """
    @classmethod
    def bind_cli(cls, parser: argparse.ArgumentParser, group: argparse._ArgumentGroup) -> None:
        """Expose parameters to an argparse.ArgumentParser that are specific
        to this build system.

        Args:
            parser (`ArgumentParser`): Arg parser.
            group (`_ArgumentGroup`): Arg parser group - you should add args to
                this, NOT to `parser`.
        """
    def build(self, context: ResolvedContext, variant: Variant, build_path: str, install_path: str, install: bool = False, build_type=...) -> BuildResult:
        """Implement this method to perform the actual build.

        Args:
            context: A ResolvedContext object that the build process must be
                executed within.
            variant (`Variant`): The variant being built.
            build_path: Where to write temporary build files. May be absolute
                or relative to working_dir.
            install_path (str): The package repository path to install the
                package to, if installing. If None, defaults to
                `config.local_packages_path`.
            install: If True, install the build.
            build_type: A BuildType (i.e local or central).

        Returns:
            dict: A dict containing the following information:

            - success: Bool indicating if the build was successful.
            - extra_files: List of created files of interest, not including
              build targets. A good example is the interpreted context file,
              usually named 'build.rxt.sh' or similar. These files should be
              located under build_path. Rez may install them for debugging
              purposes.
            - build_env_script: If this instance was created with write_build_scripts
              as True, then the build should generate a script which, when run
              by the user, places them in the build environment.
        """
    @classmethod
    def set_standard_vars(cls, executor: RexExecutor, context: ResolvedContext, variant: Variant, build_type: BuildType, install: bool, build_path: str, install_path: str | None = None) -> None:
        """Set some standard env vars that all build systems can rely on.
        """
    @classmethod
    def add_pre_build_commands(cls, executor, variant, build_type, install, build_path, install_path: Incomplete | None = None) -> None:
        """Execute pre_build_commands function if present."""
    @classmethod
    def add_standard_build_actions(cls, executor: RexExecutor, context: ResolvedContext, variant: Variant, build_type: BuildType, install: bool, build_path: str, install_path: str | None = None) -> None:
        """Perform build actions common to every build system.
        """
