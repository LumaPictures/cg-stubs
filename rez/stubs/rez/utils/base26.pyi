from _typeshed import Incomplete
from rez.utils.filesystem import find_matching_symlink as find_matching_symlink

def get_next_base26(prev: Incomplete | None = None):
    """Increment letter-based IDs.

    Generates IDs like ['a', 'b', ..., 'z', 'aa', ab', ..., 'az', 'ba', ...]

    Returns:
        str: Next base-26 ID.
    """
def create_unique_base26_symlink(path, source):
    """Create a base-26 symlink in `path` pointing to `source`.

    If such a symlink already exists, it is returned. Note that there is a small
    chance that this function may create a new symlink when there is already one
    pointed at `source`.

    Assumes `path` only contains base26 symlinks.

    Returns:
        str: Path to created symlink.
    """
