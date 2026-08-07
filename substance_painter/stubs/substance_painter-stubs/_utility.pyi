def is_mock(obj):
    """Returns ``True`` if 'obj' is a mock, ``False`` otherwise.

    Just check if the unittest.moc.Mock.side_effect method exists.
    WARNING: don't try to use 'isinstance' because mock object
    appears as mocked object.
    """
def expose_private_obj(obj, module_name, fields=None, class_name=None):
    """This method allows for proper documentation generation when exposing
    an object form the private API through the public API. The corresponding
    object needs to be documented from python or sphinx files (doc strings
    from the private API wont be imported during documentation generation, but
    they will still be available at runtime to be used with the `help`
    builtin function).

    Returns 'obj' if not a mock object. Otherwise, inject a class with the same
    class name in the module 'module_name'. Optionally a list of 'fields' can
    be supplied if necessary for documention generation.
    """
def type_mismatch_error_message(argument_name: str, expected_argument_type) -> str:
    """Returns a formatted error message for TypeError exceptions.
    """
def flatten_attributes(src, dst, overrides=None) -> None:
    """Flatten all attributes from src hierarchy in dst."""
def unflatten_attributes(src, dst, overrides=None) -> None:
    """Load all attributes from src flat object into dst hierarchy."""
def is_power_of_two(val: int) -> bool:
    """Returns true if val is a power of 2, false otherwise"""
def restrict_float_range(name: str, lower_bound: float, upper_bound: float):
    """__set_attr__ decorator to enforce a lower and upper bound on a float value."""
def restrict_float_lower_bound(name: str, lower_bound: float):
    """__set_attr__ decorator to enforce a lower bound on a float value."""
def restrict_color(name: str):
    """
    __set_attr__ decorator to make sure the modified value is a list of 3 values always
    between 0 and 1.
    """
def restrict_resolution(name: str, lower_bound: int, upper_bound: int):
    """
    __set_attr__ decorator to make sure the resolution is always a power
    of 2 value and in range [lower_bound, upper_bound].
    """
def restrict_positive_rect(name: str):
    """__set_attr__ decorator to make sure the rect is positive."""

class ReadOnlyUid:
    """Class with a read-only uid"""
    def __init__(self, uid) -> None: ...
    def __setattr__(self, name, value) -> None: ...
    def __eq__(self, other): ...
    def uid(self) -> int:
        """
        Get the object internal uid.

        Returns:
            int: The internal identifier of the object as an integer.
        """

def make_callable(value):
    """Make value callable, usefull when migrating from getter to property."""
