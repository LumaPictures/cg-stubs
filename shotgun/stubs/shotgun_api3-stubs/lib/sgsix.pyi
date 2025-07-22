import ssl
from _typeshed import Incomplete

file_types: Incomplete
ShotgunSSLError = ssl.SSLError

def normalize_platform(platform: str, python2: bool = True) -> str:
    """
    Normalize the return of sys.platform between Python 2 and 3.

    On Python 2 on linux hosts, sys.platform was 'linux' appended with the
    current kernel version that Python was built on.  In Python3, this was
    changed and sys.platform now returns 'linux' regardless of the kernel version.
    See https://bugs.python.org/issue12326
    This function will normalize platform strings to always conform to Python2 or
    Python3 behavior.

    :param str platform: The platform string to normalize
    :param bool python2: The python version behavior to target.  If True, a
        Python2-style platform string will be returned (i.e. 'linux2'), otherwise
        the modern 'linux' platform string will be returned.

    :returns: The normalized platform string.
    :rtype: str
    """

platform: Incomplete
