from _typeshed import Incomplete
from rez.exceptions import PackageRequestError as PackageRequestError
from rez.system import System as System
from rez.utils.logging_ import print_warning as print_warning
from rez.version import Requirement as Requirement, Version as Version, VersionRange as VersionRange

def pip_to_rez_package_name(dist_name):
    """Convert a distribution name to a rez compatible name.

    The rez package name can't be simply set to the dist name, because some
    pip packages have hyphen in the name. In rez this is not a valid package
    name (it would be interpreted as the start of the version).

    Example: my-pkg-1.2 is 'my', version 'pkg-1.2'.

    Args:
        dist_name (str): Distribution name to convert.

    Returns:
        str: Rez-compatible package name.
    """
def pip_to_rez_version(dist_version, allow_legacy: bool = True):
    """Convert a distribution version to a rez compatible version.

    TODO [AJ] needs a table of example conversions.

    The python version schema specification isn't 100% compatible with rez.

    1. version epochs (they make no sense to rez, so they'd just get stripped
       of the leading ``N!``;
    2. python versions are case insensitive, so they should probably be
       lowercased when converted to a rez version.
    3. local versions are also not compatible with rez

    The canonical public version identifiers MUST comply with the following scheme:
    ``[N!]N(.N)*[{a|b|rc}N][.postN][.devN]``

    Epoch segment: ``N!`` - skip
    Release segment: N(.N)* 0`` as is
    Pre-release segment: ``{a|b|c|rc|alpha|beta|pre|preview}N`` - always lowercase
    Post-release segment: ``.{post|rev|r}N`` - always lowercase
    Development release segment: ``.devN`` - always lowercase

    Local version identifiers MUST comply with the following scheme:
    ``<public version identifier>[+<local version label>]`` - use - instead of +

    Args:
        dist_version (str): The distribution version to be converted.
        allow_legacy (bool): Flag to allow/disallow PEP440 incompatibility.

    Returns:
        str: Rez-compatible equivalent version string.

    Raises:
        InvalidVersion: When legacy mode is not allowed and a PEP440
            incompatible version is detected.

    .. _PEP 440 (all possible matches):
        https://www.python.org/dev/peps/pep-0440/#appendix-b-parsing-version-strings-with-regular-expressions

    .. _Core utilities for Python packages:
        https://packaging.pypa.io/en/latest/version/

    """
def pip_specifier_to_rez_requirement(specifier):
    """Convert PEP440 version specifier to rez equivalent.

    See https://www.python.org/dev/peps/pep-0440/#version-specifiers

    Note that version numbers in the specifier are converted to rez equivalents
    at the same time. Thus a specifier like '<1.ALPHA2' becomes '<1.a2'.

    Note that the conversion is not necessarily exact - there are cases in
    PEP440 that have no equivalent in rez versioning. Most of these are
    specifiers that involve pre/post releases, which don't exist in rez (or
    rather, they do exist in the sense that '1.0.post1' is a valid rez version
    number, but it has no special meaning).

    Note also that the specifier is being converted into rez format, but in a
    way that still expresses how _pip_ interprets the specifier. For example,
    '==1' is a valid version range in rez, but '==1' has a different meaning to
    pip than it does to rez ('1.0' matches '==1' in pip, but not in rez). This
    is why '==1' is converted to '1+<1.1' in rez, rather than '==1'.

    Example conversions:

    ============== ===============
    PEP440         rez
    ============== ===============
    ``==1``        ``1+<1.1``
    ``==1.*``      ``1``
    ``>1``         ``1.1+``
    ``<1``         ``<1``
    ``>=1``        ``1+``
    ``<=1``        ``<1.1``
    ``~=1.2``      ``1.2+<2``
    ``~=1.2.3``    ``1.2.3+<1.3``
    ``!=1``        ``<1|1.1+``
    ``!=1.2``      ``<1.2|1.2.1+``
    ``!=1.*``      ``<1|2+``
    ``!=1.2.*``    ``<1.2|1.3+``
    ============== ===============

    Args:
        specifier (`package.SpecifierSet`): Pip specifier.

    Returns:
        `VersionRange`: Equivalent rez version range.
    """
def packaging_req_to_rez_req(packaging_req):
    """Convert packaging requirement object to equivalent rez requirement.

    Note that environment markers are ignored.

    Args:
        packaging_req (`packaging.requirements.Requirement`): Packaging requirement.

    Returns:
        `Requirement`: Equivalent rez requirement object.
    """
def is_pure_python_package(installed_dist):
    """Determine if a dist is pure python.

    Args:
        installed_dist (`distlib.database.InstalledDistribution`): Distribution
            to test.

    Returns:
        bool: True if dist is pure python
    """
def is_entry_points_scripts_package(installed_dist):
    """Determine if a dist has generated entry point scripts.

    Args:
        installed_dist (`distlib.database.InstalledDistribution`): Distribution
            to test.

    Returns:
        bool: True if dist has generated entry point scripts
    """
def get_rez_requirements(installed_dist, python_version, name_casings: Incomplete | None = None):
    '''Get requirements of the given dist, in rez-compatible format.

    Example result:

    .. code-block:: python

       {
           "requires": ["foo-1.2+<2"],
           "variant_requires": ["future", "python-2.7"],
           "metadata": {
               # metadata pertinent to rez
               ...
           }
       }

    Each requirement has had its package name converted to the rez equivalent.
    The \'variant_requires\' key contains requirements specific to the current
    variant.

    TODO: Currently there is no way to reflect extras that may have been chosen
    for this pip package. We need to wait for rez "package features" before this
    will be possible. You probably shouldn\'t use extras presently.

    Args:
        installed_dist (`distlib.database.InstalledDistribution`): Distribution
            to convert.
        python_version (`Version`): Python version used to perform the
            installation.
        name_casings (list of str): A list of pip package names in their correct
            casings (eg, \'Foo\' rather than \'foo\'). Any requirement whose name
            case-insensitive-matches a name in this list, is set to that name.
            This is needed because pip package names are case insensitive, but
            rez is case-sensitive. So a package may list a requirement for package
            \'foo\', when in fact the package that pip has downloaded is called \'Foo\'.
            Be sure to provide names in PIP format, not REZ format (the pip package
            \'foo-bah\' will be converted to \'foo_bah\' in rez).

    Returns:
        Dict: See example above.
    '''
def convert_distlib_to_setuptools(installed_dist):
    """Get the setuptools equivalent of a distlib installed dist.

    Args:
        installed_dist (`distlib.database.InstalledDistribution`: Distribution
            to convert.

    Returns:
        `pkg_resources.DistInfoDistribution`: Equivalent setuptools dist object.
    """
def get_marker_sys_requirements(marker):
    '''Get the system requirements that an environment marker introduces.

    Consider:

        \'foo (>1.2) ; python_version == "3" and platform_machine == "x86_64"\'

    This example would cause a requirement on python, platform, and arch
    (platform as a consequence of requirement on arch).

    See:
    * vendor/packaging/markers.py:line=76
    * https://www.python.org/dev/peps/pep-0508/#id23

    Args:
        marker (str): Environment marker string, eg \'python_version == "3"\'.

    Returns:
        List of str: System requirements (unversioned).
    '''
def normalize_requirement(requirement):
    """Normalize a package requirement.

    Requirements from distlib packages can be a mix of string- or dict- based
    formats, as shown here:

    * https://www.python.org/dev/peps/pep-0508/#environment-markers
    * https://legacy.python.org/dev/peps/pep-0426/#environment-markers

    There's another confusing case that this code deals with. Consider these two
    requirements:

        # means: reportlab is a requirement of this package when the 'pdf' extra is requested
        Requires-Dist: reportlab; extra == 'pdf'

        means: this package requires libexample, with its 'test' extras
        Requires-Dist: libexample[test]

    See https://packaging.python.org/specifications/core-metadata/#provides-extra-multiple-use

    The packaging lib doesn't do a good job of expressing this - the first form
    of extras use just gets embedded in the environment marker. This function
    parses the extra from the marker, and stores it onto the resulting
    `packaging.Requirement` object in a 'conditional_extras' attribute. It also
    removes the extra from the marker (otherwise the marker cannot evaluate).
    Even though you can specify `environment` in `packaging.Marker.evaluate`,
    you can only supply a single 'extra' key in the env, so this can't be used
    to correctly evaluate if multiple extras were requested.

    Args:
        requirement (str or dict): Requirement, for eg from
            `distlib.database.InstalledDistribution.run_requires`.

    Returns:
        List of `packaging.requirements.Requirement`: Normalized requirements.
        Note that a list is returned, because the PEP426 format can define
        multiple requirements.
    """
