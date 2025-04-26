import _thread
from _typeshed import Incomplete
from collections.abc import MutableMapping
from rez.vendor.schema.schema import Optional as Optional, Schema as Schema  # type: ignore[import-not-found]
from typing import Any, Generic, TypeVar

T = TypeVar('T')

class ModifyList:
    """List modifier, used in `deep_update`.

    This can be used in configs to add to list-based settings, rather than
    overwriting them.
    """
    prepend: Any
    append: Any
    def __init__(self, append: Incomplete | None = None, prepend: Incomplete | None = None) -> None: ...
    def apply(self, v): ...

class DelayLoad:
    """Used in config to delay load a config value from anothe file.

    Supported formats:

    - yaml (``*.yaml``, ``*.yml``)
    - json (``*.json``)
    """
    filepath: Any
    def __init__(self, filepath) -> None: ...
    def __str__(self) -> str: ...
    def get_value(self): ...

def remove_nones(**kwargs):
    """Return diict copy with nones removed.
    """
def deep_update(dict1, dict2) -> None:
    """Perform a deep merge of `dict2` into `dict1`.

    Note that `dict2` and any nested dicts are unchanged.

    Supports `ModifyList` instances.
    """
def deep_del(data, fn):
    """Create dict copy with removed items.

    Recursively remove items where fn(value) is True.

    Returns:
        dict: New dict with matching items removed.
    """
def get_dict_diff(d1, d2):
    """Get added/removed/changed keys between two dicts.

    Each key in the return value is a list, which is the namespaced key that
    was affected.

    Returns:
        tuple: 3-tuple:
        - list of added keys;
        - list of removed key;
        - list of changed keys.
    """
def get_dict_diff_str(d1, d2, title):
    """Returns same as `get_dict_diff`, but as a readable string.
    """
cached_property = property

class cached_class_property:
    """Simple class property caching descriptor.

    Example:

        >>> class Foo(object):
        >>>     @cached_class_property
        >>>     def bah(cls):
        >>>         print('bah')
        >>>         return 1
        >>>
        >>> Foo.bah
        bah
        1
        >>> Foo.bah
        1
    """
    func: Any
    def __init__(self, func, name: Incomplete | None = None) -> None: ...
    def __get__(self, instance, owner: Incomplete | None = None): ...

class LazySingleton(Generic[T]):
    """A threadsafe singleton that initialises when first referenced."""
    instance_class: type[T]
    nargs: tuple[Any, ...]
    kwargs: dict[str, Any]
    lock: _thread.LockType
    instance: T | None
    def __init__(self, instance_class: type[T], *nargs, **kwargs) -> None: ...
    def __call__(self) -> T: ...

class AttrDictWrapper(MutableMapping):
    """Wrap a custom dictionary with attribute-based lookup::

        >>> d = {'one': 1}
        >>> dd = AttrDictWrapper(d)
        >>> assert dd.one == 1
        >>> ddd = dd.copy()
        >>> ddd.one = 2
        >>> assert ddd.one == 2
        >>> assert dd.one == 1
        >>> assert d['one'] == 1
    """
    def __init__(self, data: Incomplete | None = None) -> None: ...
    @property
    def _data(self): ...
    def __getattr__(self, attr): ...
    def __setattr__(self, attr, value) -> None: ...
    def __getitem__(self, key): ...
    def __setitem__(self, key, value) -> None: ...
    def __delitem__(self, key) -> None: ...
    def __contains__(self, key) -> bool: ...
    def __iter__(self): ...
    def __len__(self) -> int: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def copy(self): ...

class RO_AttrDictWrapper(AttrDictWrapper):
    """Read-only version of AttrDictWrapper."""
    def __setattr__(self, attr, value) -> None: ...

def convert_dicts(d, to_class=..., from_class=...):
    """Recursively convert dict and UserDict types.

    Note that `d` is unchanged.

    Args:
        to_class (type): Dict-like type to convert values to, usually UserDict
            subclass, or dict.
        from_class (type): Dict-like type to convert values from. If a tuple,
            multiple types are converted.

    Returns:
        Converted data as `to_class` instance.
    """
def get_object_completions(instance, prefix, types: Incomplete | None = None, instance_types: Incomplete | None = None):
    """Get completion strings based on an object's attributes/keys.

    Completion also works on dynamic attributes (eg implemented via __getattr__)
    if they are iterable.

    Args:
        instance (object): Object to introspect.
        prefix (str): Prefix to match, can be dot-separated to access nested
            attributes.
        types (tuple): Attribute types to match, any if None.
        instance_types (tuple): Class types to recurse into when a dotted
            prefix is given, any if None.

    Returns:
        List of strings.
    """
def convert_json_safe(value):
    """Convert data to JSON safe values.

    Anything not representable (eg python objects) will be stringified.
    """

class AttributeForwardMeta(type):
    '''Metaclass for forwarding attributes of class member `wrapped` onto the
    parent class.

    If the parent class already contains an attribute of the same name,
    forwarding is skipped for that attribute. If the wrapped object does not
    contain an attribute, the forwarded value will be None.

    If the parent class contains method \'_wrap_forwarded\', then forwarded values
    are passed to this function, and the return value becomes the attribute
    value.

    The class must contain:
    - keys (list of str): The attributes to be forwarded.

    Example:

        >>> class Foo(object):
        >>>     def __init__(self):
        >>>         self.a = "a_from_foo"
        >>>         self.b = "b_from_foo"
        >>>
        >>> class Bah(object, metaclass=AttributeForwardMeta):
        >>>     keys = ["a", "b", "c"]
        >>>
        >>>     @property
        >>>     def a(self):
        >>>         return "a_from_bah"
        >>>
        >>>     def __init__(self, child):
        >>>         self.wrapped = child
        >>>
        >>> x = Foo()
        >>> y = Bah(x)
        >>> print(y.a)
        a_from_bah
        >>> print(y.b)
        b_from_foo
        >>> print(y.c)
        None
    '''
    def __new__(cls, name, parents, members): ...
    @classmethod
    def _make_forwarder(cls, key): ...

class LazyAttributeMeta(type):
    """Metaclass for adding properties to a class for accessing top-level keys
    in its `_data` dictionary, and validating them on first reference.

    Property names are derived from the keys of the class's `schema` object.
    If a schema key is optional, then the class property will evaluate to None
    if the key is not present in `_data`.

    The attribute getters created by this metaclass will perform lazy data
    validation, OR, if the class has a `_validate_key` method, will call this
    method, passing the key, key value and key schema.

    This metaclass creates the following attributes:
        - for each key in cls.schema, creates an attribute of the same name,
          unless that attribute already exists;
        - for each key in cls.schema, if the attribute already exists on cls,
          then creates an attribute with the same name but prefixed with '_';
        - 'validate_data' (function): A method that validates all keys;
        - 'validated_data' (function): A method that returns the entire
          validated dict, or None if there is no schema;
        - '_validate_key_impl' (function): Validation function used when
          '_validate_key' is not provided, it is here so you can use it in
          your own '_validate_key' function;
        - '_schema_keys' (frozenset): Keys in the schema.
    """
    def __new__(cls, name, parents, members): ...
    @classmethod
    def _make_validate_data(cls): ...
    @classmethod
    def _make_validated_data(cls): ...
    @classmethod
    def _make_validate_key_impl(cls): ...
    @classmethod
    def _make_getter(cls, key, attribute, optional, key_schema): ...
