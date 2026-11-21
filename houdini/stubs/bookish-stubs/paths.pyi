# Houdini stubs generated from Houdini 22.0.466

from collections.abc import Generator

def is_abs(path: str) -> bool: ...
def parts(path: str) -> Generator[str, None, None]:
    '''
    Yields the parts of the given path string::

    >>> list(parts("/a/b/c"))
    ["/", "a/", "b/", "c"]
    '''
def norm_parts(path: str, out: list[str] | None = None) -> list[str]:
    '''
    Returns a list of the *normalized* parts of the given path string.
    This means that special names such as "." and ".." are applied, and
    multiple adjacent slashes are replaced with a single slash.

    >>> norm_parts("/a/b//c/../d")
    ["/", "a/", "b/", "d"]
    '''
def normalize(path: str) -> str:
    '''
    Returns a *normalized* version of the given path string.
    This means that special names such as "." and ".." are applied, and
    multiple adjacent slashes are replaced with a single slash.

    >>> normalize("/a/b//c/../d")
    "/a/b/d"
    '''
def normalize_abs(path: str) -> str:
    """
    Like normalize() but raises an error if the given path is not absolute.
    """
def parent(path: str) -> str:
    '''
    Returns the parent directory path of the given resource.

    >>> parent("/a/b/c")
    "/a/"
    >>> parent("/a/b/")
    "/a/"
    >>> parent("/")
    "/"
    '''
def directory(path: str) -> str:
    '''
    If the given path is a directory resource (ends with a slash), this returns
    the path unchanged. If it\'s a file resource, returns the path of the file\'s
    parent directory.

    >>> parent("/a/b/")
    "/a/b/"
    >>> parent("/a/b")
    "/a/"
    '''
def join(basepath: str, relpath: str) -> str:
    '''
    Joins two path strings intelligently. If the first path specifies a file,
    the second path will be joined to the first path\'s *directory*.

    >>> join("/a/b", "c")
    "/a/b/c"
    >>> join("/a/b/c", "d")
    "/a/b/d"
    >>> join("/a/b/c/", "../d")
    "/a/b/d"
    '''
def relativize(basepath: str, targetpath: str) -> str:
    '''
    Returns a relative path from the "base" resource to the "target" resource.

    >>> relativize("/a/b", "c")
    "c"
    >>> relativize("/a/b/c", "/a/b/d/e")
    "d/e"
    >>> relativize("/a/b/c", "/d/e/f")
    "../../d/e/f"
    '''
def basepath(path: str) -> str:
    """
    Removes the extension from the end of a path.
    """
def basename(path: str) -> str:
    '''
    Returns the base name of the file named by the path.
    If the resource is a directory, the base name is the empty string ("").

    >>> basename("/a/b")
    "b"
    >>> basename("/a/b/")
    ""
    '''
def barename(path: str) -> str:
    '''
    Returns the base name of the file named by the path, with any extension
    removed.
    If the resource is a directory, the base name is the empty string ("").

    >>> basename("/a/b.txt")
    "b"
    >>> basename("/a/b")
    "b"
    >>> basename("/a/b/")
    ""
    '''
def extension(path: str) -> str:
    '''
    Returns the "extension" part of the base name of a resource path.

    >>> extension("/a/b/foo.bar")
    "bar"
    >>> extension("/a/b/foo")
    ""
    >>> extension("/a/b/foo.")
    ""
    '''
def strip_extension(name: str, ext: str | None = None) -> str:
    """
    Removes a specific extension (if given), or any extension, from the given
    string.
    """
def split_path_parts(path: str) -> list[str]:
    '''
    Returns a list of the names in the path.

    >>> split_path_parts("/a/b/c")
    ["a", "b", "c"]
    '''
def split_dirpath(path: str) -> tuple[str, str]:
    '''
    Returns the parent path and the file name of a resource path.

    >>> split_dirpath("/a/b/foo.bar")
    ("/a/b/", "foo.bar")
    '''
def split_extension(path: str) -> tuple[str, str]:
    '''
    Returns the base part and the extension part of the base name of a resource
    path.

    >>> split_extension("/a/b/foo.bar")
    ("foo", "bar")
    '''
def split_fragment(path: str) -> tuple[str, str]:
    '''
    Returns the path and the fragment of a path/fragment combo.

    >>> split_fragment("/a/b/foo#bar")
    ("/a/b/foo", "#bar")
    '''
