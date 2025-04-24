from rez.package_maker import make_package as make_package
from rez.system import system as system

def install_as_rez_package(repo_path) -> None:
    """Install the current rez installation as a rez package.

    Note: This is very similar to 'rez-bind rez', however rez-bind is intended
    for deprecation. Rez itself is a special case.

    Args:
        repo_path (str): Repository to install the rez package into.
    """
