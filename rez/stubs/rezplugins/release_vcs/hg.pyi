from _typeshed import Incomplete
from rez.exceptions import ReleaseVCSError
from rez.release_vcs import ReleaseVCS
from typing import Any

class HgReleaseVCSError(ReleaseVCSError): ...

class HgReleaseVCS(ReleaseVCS):
    @classmethod
    def name(cls) -> str: ...  # type: ignore[override]
    executable: Any
    patch_path: str
    def __init__(self, pkg_root, vcs_root: Incomplete | None = None) -> None: ...
    @classmethod
    def is_valid_root(cls, path): ...
    @classmethod
    def search_parents_for_root(cls) -> bool: ...  # type: ignore[override]
    def hg(self, *nargs, **kwargs): ...
    def _create_tag_highlevel(self, tag_name, message: Incomplete | None = None):
        """Create a tag on the toplevel repo if there is no patch repo,
        or a tag on the patch repo and bookmark on the top repo if there is a
        patch repo

        Returns a list where each entry is a dict for each bookmark or tag
        created, which looks like {'type': ('bookmark' or 'tag'), 'patch': bool}
        """
    def _create_tag_lowlevel(self, tag_name, message: Incomplete | None = None, force: bool = True, patch: bool = False) -> bool:
        """Create a tag on the toplevel or patch repo

        If the tag exists, and force is False, no tag is made. If force is True,
        and a tag exists, but it is a direct ancestor of the current commit,
        and there is no difference in filestate between the current commit
        and the tagged commit, no tag is made. Otherwise, the old tag is
        overwritten to point at the current commit.

        Returns True or False indicating whether the tag was actually committed
        """
    def get_tags(self, patch: bool = False): ...
    def tag_exists(self, tag_name) -> bool: ...
    def is_ancestor(self, commit1, commit2, patch: bool = False) -> bool:
        """Returns True if commit1 is a direct ancestor of commit2, or False
        otherwise.

        This method considers a commit to be a direct ancestor of itself"""
    def get_paths(self, patch: bool = False): ...
    def get_default_url(self, patch: bool = False): ...
    def validate_repostate(self) -> None: ...
    def get_current_revision(self): ...
    def get_changelog(self, previous_revision: Incomplete | None = None, max_revisions: Incomplete | None = None): ...
    def create_release_tag(self, tag_name, message: Incomplete | None = None) -> None: ...

def register_plugin(): ...
