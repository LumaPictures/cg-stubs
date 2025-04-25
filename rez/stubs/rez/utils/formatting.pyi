import rez.utils.formatting
from _typeshed import Incomplete
from enum import Enum
from rez.exceptions import PackageRequestError as PackageRequestError
from rez.version import Requirement as Requirement
from string import Formatter
from typing import Any, Sequence

PACKAGE_NAME_REGSTR: str
PACKAGE_NAME_REGEX: Incomplete
ENV_VAR_REGSTR: str
ENV_VAR_REGEX: Incomplete
FORMAT_VAR_REGSTR: str
FORMAT_VAR_REGEX: Incomplete
invalid_package_names: Incomplete

def is_valid_package_name(name, raise_error: bool = False):
    """Test the validity of a package name string.

    Args:
        name (str): Name to test.
        raise_error (bool): If True, raise an exception on failure

    Returns:
        bool.
    """

class PackageRequest(Requirement):
    '''A package request parser.

    Valid requests include:

    * Any standard request, eg \'foo-1.2.3\', \'!foo-1\', etc
    * "Ephemeral" request, eg \'.foo-1.2.3\'

    Example:

        >>> pr = PackageRequest("foo-1.3+")
        >>> print(pr.name, pr.range)
        foo 1.3+
    '''
    ephemeral: bool
    def __init__(self, s) -> None: ...

class StringFormatType(Enum):
    """Behaviour of key expansion when using `ObjectStringFormatter`."""
    error = 1
    empty = 2
    unchanged = 3

class ObjectStringFormatter(Formatter):
    """String formatter for objects.

    This formatter will expand any reference to an object's attributes.
    """
    error: Incomplete
    empty: Incomplete
    unchanged: Incomplete
    instance: Any
    pretty: bool
    expand: rez.utils.formatting.StringFormatType
    def __init__(self, instance, pretty: bool = False, expand: StringFormatType = ...) -> None:
        """Create a formatter.

        Args:
            instance: The object to format with.
            pretty: If True, references to non-string attributes such as lists
                are converted to basic form, with characters such as brackets
                and parentheses removed.
            expand: `StringFormatType`.
        """
    def convert_field(self, value, conversion): ...
    def get_field(self, field_name, args, kwargs): ...
    def get_value(self, key, args, kwds): ...

class StringFormatMixin:
    """Turn any object into a string formatter.

    An object inheriting this mixin will have a `format` function added, that is
    able to format using attributes of the object.
    """
    format_expand: Incomplete
    format_pretty: bool
    def format(self, s, pretty: Incomplete | None = None, expand: Incomplete | None = None):
        '''Format a string.

        Args:
            s (str): String to format, eg "hello {name}"
            pretty (bool): If True, references to non-string attributes such as
                lists are converted to basic form, with characters such as
                brackets and parenthesis removed. If None, defaults to the
                object\'s \'format_pretty\' attribute.
            expand (`StringFormatType`): Expansion mode. If None, will default
                to the object\'s \'format_expand\' attribute.

        Returns:
            The formatting string.
        '''

def expand_abbreviations(txt, fields):
    '''Expand abbreviations in a format string.

    If an abbreviation does not match a field, or matches multiple fields, it
    is left unchanged.

    Example:

        >>> fields = ("hey", "there", "dude")
        >>> expand_abbreviations("hello {d}", fields)
        \'hello dude\'

    Args:
        txt (str): Format string.
        fields (list of str): Fields to expand to.

    Returns:
        Expanded string.
    '''
def expandvars(text: str, environ: Incomplete | None = None) -> str:
    """Expand shell variables of form $var and ${var}.

    Unknown variables are left unchanged.

    Args:
        text (str): String to expand.
        environ (dict): Environ dict to use for expansions, defaults to
            os.environ.

    Returns:
        The expanded string.
    """
def indent(txt: str):
    """Indent the given text by 4 spaces."""
def dict_to_attributes_code(dict_):
    """Given a nested dict, generate a python code equivalent.

    Example:
        >>> d = {'foo': 'bah', 'colors': {'red': 1, 'blue': 2}}
        >>> print(dict_to_attributes_code(d))
        foo = 'bah'
        colors.red = 1
        colors.blue = 2

    Returns:
        str.
    """
def columnise(rows: Sequence[Sequence[Any]], padding: int = 2) -> list[str]:
    """Print rows of entries in aligned columns."""
def print_colored_columns(printer, rows, padding: int = 2) -> None:
    """Like `columnise`, but with colored rows.

    Args:
        printer (`colorize.Printer`): Printer object.

    Note:
        The last entry in each row is the row color, or None for no coloring.
    """

time_divs: Incomplete

def readable_time_duration(secs):
    """Convert number of seconds into human readable form, eg '3.2 hours'.
    """

memory_divs: Incomplete

def readable_memory_size(bytes_):
    """Convert number of bytes into human-readable form.

    This method rounds to 1 decimal place eg '1.2 Kb'.
    """
def _readable_units(value, divs, plural_aware: bool = False): ...
def get_epoch_time_from_str(s):
    """Convert a string into epoch time. Examples of valid strings:

        1418350671  # already epoch time
        -12s        # 12 seconds ago
        -5.4m       # 5.4 minutes ago
    """

positional_suffix: Incomplete

def positional_number_string(n) -> str:
    """Print the position string equivalent of a positive integer. Examples:

        0: zeroeth
        1: first
        2: second
        14: 14th
        21: 21st
    """

EXPANDUSER_RE: Incomplete

def expanduser(path: str) -> str:
    """Expand '~' to home directory in the given string.

    Note that this function deliberately differs from the builtin
    os.path.expanduser() on Linux systems, which expands strings such as
    '~sclaus' to that user's homedir. This is problematic in rez because the
    string '~packagename' may inadvertently convert to a homedir, if a package
    happens to match a username.
    """
def as_block_string(txt) -> str:
    """Return a string formatted as a python block comment string, like the one
    you're currently reading. Special characters are escaped if necessary.
    """

_header_br: Incomplete
_header_br_minor: Incomplete

def header_comment(executor, txt: str) -> None:
    """Convenience for creating header-like comment in a rex executor.

    Args:
        executor (`RexExecutor`): Executor.
        txt (str): Comment text.
    """
def minor_header_comment(executor, txt: str) -> None: ...
