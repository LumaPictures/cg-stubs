from _typeshed import Incomplete
from rez.config import config as config
from rez.exceptions import PackageFamilyNotFoundError as PackageFamilyNotFoundError, ResourceContentError as ResourceContentError
from rez.packages import get_latest_package as get_latest_package, iter_package_families as iter_package_families, iter_packages as iter_packages
from rez.util import ProgressBar as ProgressBar
from rez.utils.colorize import Printer as Printer, critical as critical, error as error, info as info
from rez.utils.formatting import expand_abbreviations as expand_abbreviations
from rez.vendor.pygraph.classes.digraph import digraph as digraph  # type: ignore[import-not-found]
from rez.version import Requirement as Requirement
from typing import Any

def get_reverse_dependency_tree(package_name, depth: Incomplete | None = None, paths: Incomplete | None = None, build_requires: bool = False, private_build_requires: bool = False):
    """Find packages that depend on the given package.

    This is a reverse dependency lookup. A tree is constructed, showing what
    packages depend on the given package, with an optional depth limit. A
    resolve does not occur. Only the latest version of each package is used,
    and requirements from all variants of that package are used.

    Args:
        package_name (str): Name of the package depended on.
        depth (int): Tree depth limit, unlimited if None.
        paths (list of str): paths to search for packages, defaults to
            `config.packages_path`.
        build_requires (bool): If True, includes packages' build_requires.
        private_build_requires (bool): If True, include `package_name`'s
            private_build_requires.

    Returns:
        tuple: A 2-tuple:

        - (list of list of str): Lists of package names, where each list is a
          single depth in the tree. The first list is always [`package_name`].
        - `pygraph.digraph` object, where nodes are package names, and
          `package_name` is always the leaf node.
    """
def get_plugins(package_name, paths: Incomplete | None = None):
    """Find packages that are plugins of the given package.

    Args:
        package_name (str): Name of the package.
        paths (list of str): Paths to search for packages, defaults to
            `config.packages_path`.

    Returns:
        list of str: The packages that are plugins of the given package.
    """

class ResourceSearchResult:
    """Items from a search.

    Will contain either a package, variant, or name of a package family (str).
    """
    resource: Any
    resource_type: Any
    validation_error: Any
    def __init__(self, resource, resource_type, validation_error: Incomplete | None = None) -> None: ...

class ResourceSearcher:
    """Search for resources (packages, variants or package families).
    """
    resource_type: Any
    no_local: bool
    latest: bool
    after_time: Any
    before_time: Any
    validate: bool
    package_paths: Any
    def __init__(self, package_paths: Incomplete | None = None, resource_type: Incomplete | None = None, no_local: bool = False, latest: bool = False, after_time: Incomplete | None = None, before_time: Incomplete | None = None, validate: bool = False) -> None:
        '''Create resource search.

        Args:
            package_paths (list of str): Package search path
            resource_type (str): type of resource to search for. One of "family",
                "package" or "variant". If None, is determined based on format of
                `resources_request`.
            no_local (bool): Do not look in local paths
            latest (bool): Only return latest version if resource type is
                package or variant
            after_time (int): Only show packages released after the given
                epoch time
            before_time (int): Only show packages released before the given
                epoch time
            validate (bool): Validate each resource that is found. If False,
                results are not validated (ie, `validation_error` is None).

        Returns:
            List of `ResourceSearchResult` objects
        '''
    def iter_resources(self, resources_request: Incomplete | None = None) -> None:
        """Iterate over matching resources.

        Args:
            resources_request (str): Resource to search, glob-style patterns
                are supported. If None, returns all matching resource types.

        Returns:
            tuple: 2-tuple:

            - str: resource type (family, package, variant);
            - Iterator of `ResourceSearchResult`: Matching resources. Will be
              in alphabetical order if families, and version ascending for
              packages or variants.
        """
    def search(self, resources_request: Incomplete | None = None):
        """Search for resources.

        Args:
            resources_request (str): Resource to search, glob-style patterns
                are supported. If None, returns all matching resource types.

        Returns:
            tuple: 2-tuple:

            - str: resource type (family, package, variant);
            - List of `ResourceSearchResult`: Matching resources. Will be in
              alphabetical order if families, and version ascending for
              packages or variants.
        """
    @classmethod
    def _parse_request(cls, resources_request): ...

class ResourceSearchResultFormatter:
    """Formats search results.
    """
    fields: Incomplete
    output_format: Any
    suppress_newlines: bool
    def __init__(self, output_format: Incomplete | None = None, suppress_newlines: bool = False) -> None:
        '''
        Args:
            output_format (str): String that can contain keywords such as
                "{base}". These (or their appreviations) will be expanded into
                the matching resource attribute, or left unexpanded if the
                attribute does not exist. The \'\\n\' literal will be converted
                into newlines. Defaults to qualified name.
            suppress_newlines (bool): If True, replace newlines with \'\\n\'.
        '''
    def print_search_results(self, search_results, buf=...) -> None:
        """Print formatted search results.

        Args:
            search_results (list of `ResourceSearchResult`): Search to format.
        """
    def format_search_results(self, search_results):
        """Format search results.

        Args:
            search_results (list of `ResourceSearchResult`): Search to format.

        Returns:
            tuple: List of 2-tuple: Text and color to print in.
        """
    def _format_search_result(self, resource_search_result): ...
