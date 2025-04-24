from _typeshed import Incomplete

_default_pathext: str

def which(cmd, mode=..., path: Incomplete | None = None, env: Incomplete | None = None):
    """A replacement for shutil.which.

    Things we do that shutil.which does not:

        * Support specifying `env`
        * Take into account '%systemroot%' possible presence in `path` (windows)
        * Take into account symlinks to executables (windows)
    """
