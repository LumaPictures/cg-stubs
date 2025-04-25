import rez.developer_package
from _typeshed import Incomplete
from rez.exceptions import ReleaseVCSError as ReleaseVCSError
from rez.packages import get_developer_package as get_developer_package
from rez.util import which as which
from rez.utils.execution import Popen as Popen
from rez.utils.filesystem import walk_up_dirs as walk_up_dirs
from rez.utils.logging_ import print_debug as print_debug
from typing import Any

def get_release_vcs_types():
    """Returns the available VCS implementations - git, hg etc."""
def create_release_vcs(path, vcs_name: Incomplete | None = None):
    """Return a new release VCS that can release from this source path."""

class ReleaseVCS:
    """A version control system (VCS) used to release Rez packages.
    """
    vcs_root: Any
    pkg_root: str
    package: rez.developer_package.DeveloperPackage
    type_settings: Any
    settings: Any
    def __init__(self, pkg_root: str, vcs_root: Incomplete | None = None) -> None: ...
    @classmethod
    def name(cls) -> None:
        """Return the name of the VCS type, eg 'git'."""
    @classmethod
    def find_executable(cls, name: str): ...
    @classmethod
    def is_valid_root(cls, path: str):
        """Return True if the given path is a valid root directory for this
        version control system.

        Note that this is different than whether the path is under the
        control of this type of vcs; to answer that question,
        use find_vcs_root
        """
    @classmethod
    def search_parents_for_root(cls) -> None:
        """Return True if this vcs type should check parent directories to
        find the root directory
        """
    @classmethod
    def find_vcs_root(cls, path: str):
        """Try to find a version control root directory of this type for the
        given path.

        If successful, returns (vcs_root, levels_up), where vcs_root is the
        path to the version control root directory it found, and levels_up is an
        integer indicating how many parent directories it had to search through
        to find it, where 0 means it was found in the indicated path, 1 means it
        was found in that path's parent, etc. If not sucessful, returns None
        """
    def validate_repostate(self) -> None:
        """Ensure that the VCS working copy is up-to-date."""
    def get_current_revision(self) -> object:
        """Get the current revision, this can be any type (str, dict etc)
        appropriate to your VCS implementation.

        Note:
            You must ensure that a revision contains enough information to
            clone/export/checkout the repo elsewhere - otherwise you will not
            be able to implement `export`.
        """
    def get_changelog(self, previous_revision: Incomplete | None = None, max_revisions: Incomplete | None = None) -> str:
        """Get the changelog text since the given revision.

        If previous_revision is not an ancestor (for example, the last release
        was from a different branch) you should still return a meaningful
        changelog - perhaps include a warning, and give changelog back to the
        last common ancestor.

        Args:
            previous_revision: The revision to give the changelog since. If
                None, give the entire changelog.

        Returns:
            Changelog, as a string.
        """
    def tag_exists(self, tag_name: str) -> bool:
        """Test if a tag exists in the repo.

        Args:
            tag_name (str): Tag name to check for.

        Returns:
            bool: True if the tag exists, False otherwise.
        """
    def create_release_tag(self, tag_name: str, message: Incomplete | None = None):
        """Create a tag in the repo.

        Create a tag in the repository representing the release of the
        given version.

        Args:
            tag_name (str): Tag name to write to the repo.
            message (str): Message string to associate with the release.
        """
    @classmethod
    def export(cls, revision, path: str):
        """Export the repository to the given path at the given revision.

        Note:
            The directory at `path` must not exist, but the parent directory
            must exist.

        Args:
            revision (object): Revision to export; current revision if None.
            path (str): Directory to export the repository to.
        """
    def _cmd(self, *nargs):
        """Convenience function for executing a program such as 'git' etc."""
