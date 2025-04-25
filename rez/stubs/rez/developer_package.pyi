from enum import Enum
from rez.config import config as config
from rez.exceptions import InvalidPackageError as InvalidPackageError, PackageMetadataError as PackageMetadataError
from rez.packages import Package as Package, create_package as create_package
from rez.serialise import FileFormat as FileFormat, load_from_file as load_from_file, set_objects as set_objects
from rez.utils.execution import add_sys_paths as add_sys_paths
from rez.utils.logging_ import print_error as print_error, print_info as print_info
from rez.utils.sourcecode import SourceCode as SourceCode

class PreprocessMode(Enum):
    """Defines when a package preprocess will be executed.
    """
    before = 0
    after = 1
    override = 2

class DeveloperPackage(Package):
    """A developer package.

    This is a package in a source directory that is subsequently built or
    released.
    """
    filepath: str | None
    includes: set[str] | None
    def __init__(self, resource) -> None: ...
    @property
    def root(self): ...
    @classmethod
    def from_path(cls, path, format: FileFormat | None = None):
        """Load a developer package.

        A developer package may for example be a package.yaml or package.py in a
        user's source directory.

        Args:
            path: Directory containing the package definition file, or file
                path for the package file itself
            format: which FileFormat to use, or None to check both .py and .yaml

        Returns:
            `Package` object.
        """
    def get_reevaluated(self, objects):
        """Get a newly loaded and re-evaluated package.

        Values in `objects` are made available to early-bound package
        attributes. For example, a re-evaluated package might return a different
        value for an early-bound 'private_build_requires', depending on the
        variant currently being built.

        Args:
            objects (`dict`): Variables to expose to early-bound package attribs.

        Returns:
            `DeveloperPackage`: New package.
        """
    def _validate_includes(self) -> None: ...
    def _get_preprocessed(self, data):
        """
        Returns:
            (DeveloperPackage, new_data) 2-tuple IF the preprocess function
            changed the package; otherwise None.
        """
