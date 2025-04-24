from _typeshed import Incomplete
from rez.exceptions import RezSystemError as RezSystemError

def _mkdirs(*dirs): ...
def convert_name(name):
    """ Convert a python distribution name into a rez-safe package name."""
def convert_version(version):
    """Convert a python distribution version into a rez-safe version string."""
def convert_requirement(req):
    """
    Converts a pkg_resources.Requirement object into a list of Rez package
    request strings.
    """
def get_dist_dependencies(name, recurse: bool = True):
    """
    Get the dependencies of the given, already installed distribution.
    @param recurse If True, recursively find all dependencies.
    @returns A set of package names.
    @note The first entry in the list is always the top-level package itself.
    """
def convert_dist(name, dest_path, make_variant: bool = True, ignore_dirs: Incomplete | None = None, python_requirement: str = 'major_minor'):
    '''Convert an already installed python distribution into a rez package.

    Args:
        dest_path (str): Where to put the rez package. The package will be
            created under dest_path/<NAME>/<VERSION>/.
        make_variant (bool): If True, makes a single variant in the rez package
            based on the MAJOR.MINOR version of python.
        ignore_dirs (bool): List of directory names to not copy from the dist.
        python_requirement (str): How the package should depend on python.
            One of:

            - "major": depend on python-X
            - "major_minor": depend on python-X.X
            - any other value: this string is used as the literal version
              range string.

    Returns:
        Install path of the new Rez package.
    '''
