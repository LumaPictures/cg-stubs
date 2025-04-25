from _typeshed import Incomplete
from rez.exceptions import InvalidPackageError as InvalidPackageError
from rez.packages import Package as Package
from rez.utils.execution import Popen as Popen

def expand_requirement(request: str, paths: Incomplete | None = None) -> str:
    """Expands a requirement string like ``python-2.*``, ``foo-2.*+<*``, etc.

    Wildcards are expanded to the latest version that matches. There is also a
    special wildcard ``**`` that will expand to the full version, but it cannot
    be used in combination with ``*``.

    Wildcards MUST placehold a whole version token, not partial - while ``foo-2.*``
    is valid, ``foo-2.v*`` is not.

    Wildcards MUST appear at the end of version numbers - while ``foo-1.*.*`` is
    valid, ``foo-1.*.0`` is not.

    It is possible that an expansion will result in an invalid request string
    (such as ``foo-2+<2``). The appropriate exception will be raised if this
    happens.

    Examples:

        >>> print(expand_requirement('python-2.*'))
        python-2.7
        >>> print(expand_requirement('python==2.**'))
        python==2.7.12
        >>> print(expand_requirement('python<**'))
        python<3.0.5

    Args:
        request (str): Request to expand, eg ``python-2.*``
        paths (typing.Optional[list[str]]): paths to search for package families,
            defaults to :data:`packages_path`.

    Returns:
        str: Expanded request string.
    """
def expand_requires(*requests):
    '''Create an expanded requirements list.

    Example:

        >>> print(expand_requires(["boost-1.*.*"]))
        ["boost-1.55.0"]
        >>> print(expand_requires(["boost-1.*"]))
        ["boost-1.55"]

    Args:
        requests (list[str]): Requirements to expand. Each value may have
            trailing wildcards.

    Returns:
        list[str]: Expanded requirements.
    '''
def exec_command(attr: str, cmd: list[str]):
    """Runs a subprocess to calculate a package attribute.

    Args:
        attr (str): Package attribute
        cmd (list[str]): Command to run

    Returns:
        tuple(str): Returns a tuple of (stdout, stderr).
    """
def exec_python(attr, src, executable: str = 'python'):
    """Runs a python subproc to calculate a package attribute.

    Args:
        attr (str): Name of package attribute being created.
        src (list[str]): Python code to execute, will be converted into
            semicolon-delimited single line of code.

    Returns:
        str: Output of python process.
    """
def find_site_python(module_name: str, paths: list[str] | None = None) -> Package:
    """Find the rez native python package that contains the given module.

    This function is used by python 'native' rez installers to find the native
    rez python package that represents the python installation that this module
    is installed into.

    Note:
        This function is dependent on the behavior found in the python '_native'
        package found in the 'rez-recipes' repository. Specifically, it expects
        to find a python package with a '_site_paths' list attribute listing
        the site directories associated with the python installation.

    Args:
        module_name (str): Target python module.
        paths (typing.Optional[list[str]]): paths to search for packages,
            defaults to :data:`packages_path`.

    Returns:
        Package: Native python package containing the named module.
    """
