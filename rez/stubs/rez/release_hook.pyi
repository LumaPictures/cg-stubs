import rez.developer_package
from _typeshed import Incomplete
from enum import Enum
from rez.packages import get_developer_package as get_developer_package
from rez.utils.logging_ import print_debug as print_debug, print_warning as print_warning
from typing import Any

def get_release_hook_types():
    """Returns the available release hook implementations."""
def create_release_hook(name, source_path):
    """Return a new release hook of the given type."""
def create_release_hooks(names, source_path): ...

class ReleaseHook:
    """An object that allows for custom behaviour during releases.

    A release hook provides methods that you implement to inject custom
    behaviour during parts of the release process. For example, the builtin
    'email' hook sends a post-release email to a configured address.
    """
    @classmethod
    def name(cls) -> None:
        """ Return name of source retriever, eg 'git'"""
    source_path: Any
    package: rez.developer_package.DeveloperPackage
    type_settings: Any
    settings: Any
    def __init__(self, source_path) -> None:
        """Create a release hook.

        Args:
            source_path: Path containing source that was released.
        """
    def pre_build(self, user, install_path, variants: Incomplete | None = None, release_message: Incomplete | None = None, changelog: Incomplete | None = None, previous_version: Incomplete | None = None, previous_revision: Incomplete | None = None, **kwargs) -> None:
        """Pre-build hook.

        Args:
            user: Name of person who did the release.
            install_path: Directory the package was installed into.
            variants: List of variant indices we are attempting to build, or
                None
            release_message: User-supplied release message.
            changelog: List of strings describing changes since last release.
            previous_version: Version object - previously-release package, or
                None if no previous release.
            previous_revision: Revision of previously-released package (type
                depends on repo - see ReleaseVCS.get_current_revision().
            kwargs: Reserved.

        Note:
            This method should raise a `ReleaseHookCancellingError` if the
            release process should be cancelled.
        """
    def pre_release(self, user, install_path, variants: Incomplete | None = None, release_message: Incomplete | None = None, changelog: Incomplete | None = None, previous_version: Incomplete | None = None, previous_revision: Incomplete | None = None, **kwargs) -> None:
        """Pre-release hook.

        This is called before any package variants are released.

        Args:
            user: Name of person who did the release.
            install_path: Directory the package was installed into.
            variants: List of variant indices we are attempting to release, or
                None
            release_message: User-supplied release message.
            changelog: List of strings describing changes since last release.
            previous_version: Version object - previously-release package, or
                None if no previous release.
            previous_revision: Revision of previously-releaved package (type
                depends on repo - see ReleaseVCS.get_current_revision().
            kwargs: Reserved.

        Note:
            This method should raise a `ReleaseHookCancellingError` if the
            release process should be cancelled.
        """
    def post_release(self, user, install_path, variants, release_message: Incomplete | None = None, changelog: Incomplete | None = None, previous_version: Incomplete | None = None, previous_revision: Incomplete | None = None, **kwargs) -> None:
        """Post-release hook.

        This is called after all package variants have been released.

        Args:
            user: Name of person who did the release.
            install_path: Directory the package was installed into.
            variants (list of `Variant`): The variants that have been released.
            release_message: User-supplied release message.
            changelog: List of strings describing changes since last release.
            previous_version: Version of previously-release package, None if
                no previous release.
            previous_revision: Revision of previously-releaved package (type
                depends on repo - see ReleaseVCS.get_current_revision().
            kwargs: Reserved.
        """

class ReleaseHookEvent(Enum):
    """Enum to help manage release hooks."""
    pre_build = ('pre-build', 'build', 'pre_build')
    pre_release = ('pre-release', 'release', 'pre_release')
    post_release = ('post-release', 'release', 'post_release')
    label: Any
    noun: Any
    __name__: Any
    def __init__(self, label, noun, func_name) -> None: ...
