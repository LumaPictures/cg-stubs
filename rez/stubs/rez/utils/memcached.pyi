from _typeshed import Incomplete
from contextlib import contextmanager
from rez.config import config as config
from rez.util import get_function_arg_names as get_function_arg_names
from rez.vendor.memcache.memcache import SERVER_MAX_KEY_LENGTH as SERVER_MAX_KEY_LENGTH  # type: ignore[import-not-found]
from threading import local
from typing import Any, Callable, Iterator

cache_interface_version: int

class Client:
    """Wrapper for memcache.Client instance.

    Adds the features:
    - unlimited key length;
    - hard/soft flushing;
    - ability to cache None.
    """
    class _Miss:
        def __bool__(self) -> bool: ...
    miss: Incomplete
    logger: Incomplete
    servers: list[str] | Any
    key_hasher: Callable[[Any], Any]
    _client: Any | None
    debug: bool
    current: str
    def __init__(self, servers, debug: bool = False) -> None:
        """Create a memcached client.

        Args:
            servers (str or list of str): Server URI(s), eg '127.0.0.1:11211'.
            debug (bool): If True, quasi human readable keys are used. This helps
                debugging - run 'memcached -vv' in the foreground to see the keys
                being get/set/stored.
        """
    def __bool__(self) -> bool: ...
    @property
    def client(self):
        """Get the native memcache client.

        Returns:
            `memcache.Client` instance.
        """
    def test_servers(self):
        """Test that memcached servers are servicing requests.

        Returns:
            set: URIs of servers that are responding.
        """
    def set(self, key, val, time: int = 0, min_compress_len: int = 0) -> None:
        """See memcache.Client."""
    def get(self, key):
        """See memcache.Client.

        Returns:
            object: A value if cached, else `self.miss`. Note that this differs
            from `memcache.Client`, which returns None on cache miss, and thus
            cannot cache the value None itself.
        """
    def delete(self, key) -> None:
        """See memcache.Client."""
    def flush(self, hard: bool = False) -> None:
        """Drop existing entries from the cache.

        Args:
            hard (bool): If True, all current entries are flushed from the
                server(s), which affects all users. If False, only the local
                process is affected.
        """
    def get_stats(self):
        """Get server statistics.

        Returns:
            A list of tuples (server_identifier, stats_dictionary).
        """
    def reset_stats(self) -> None:
        """Reset the server stats."""
    def disconnect(self) -> None:
        """Disconnect from server(s). Behaviour is undefined after this call."""
    def _qualified_key(self, key) -> str:
        """
        Qualify cache key so that:
        * changes to schemas don't break compatibility (cache_interface_version)
        * we're shielded from potential compatibility bugs in newer versions of
          python-memcached
        """
    def _get_stats(self, stat_args: Incomplete | None = None): ...
    @classmethod
    def _key_hash(cls, key): ...
    @classmethod
    def _debug_key_hash(cls, key): ...

class _ScopedInstanceManager(local):
    clients: dict[tuple[tuple[Any, ...], bool], list[Any]]
    def __init__(self) -> None: ...
    def acquire(self, servers, debug: bool = False) -> tuple[Client, tuple[tuple, bool]]: ...
    def release(self, key) -> None: ...

scoped_instance_manager: Incomplete

@contextmanager
def memcached_client(servers=..., debug=...) -> Iterator[Client]:
    """Get a shared memcached instance.

    This function shares the same memcached instance across nested invocations.
    This is done so that memcached connections can be kept to a minimum, but at
    the same time unnecessary extra reconnections are avoided. Typically an
    initial scope (using 'with' construct) is made around parts of code that hit
    the cache server many times - such as a resolve, or executing a context. On
    exit of the topmost scope, the memcached client is disconnected.

    Returns:
        `Client`: Memcached instance.
    """
def pool_memcached_connections(func):
    """Function decorator to pool memcached connections.

    Use this to wrap functions that might make multiple calls to memcached. This
    will cause a single memcached client to be shared for all connections.
    """
def memcached(servers, key: Incomplete | None = None, from_cache: Incomplete | None = None, to_cache: Incomplete | None = None, time: int = 0, min_compress_len: int = 0, debug: bool = False):
    '''memcached memoization function decorator.

    The wrapped function is expected to return a value that is stored to a
    memcached server, first translated by `to_cache` if provided. In the event
    of a cache hit, the data is translated by `from_cache` if provided, before
    being returned. If you do not want a result to be cached, wrap the return
    value of your function in a `DoNotCache` object.

    Examples:

    .. code-block:: python

        @memcached(\'127.0.0.1:11211\')
        def _listdir(path):
            return os.path.listdir(path)

    Note:
        If using the default key function, ensure that repr() is implemented on
        all your arguments and that they are hashable.

    Note:
        `from_cache` and `to_cache` both accept the value as first parameter,
        then the target function\'s arguments follow.

    Args:
        servers (str or list of str): memcached server uri(s), eg \'127.0.0.1:11211\'.
            This arg can be None also, in which case memcaching is disabled.
        key (typing.Optional[typing.Callable]): Function that, given the target function\'s args,
            returns the string key to use in memcached.
        from_cache (typing.Optional[typing.Callable]): If provided, and a cache hit occurs, the
            cached value will be translated by this function before being returned.
        to_cache (typing.Optional[typing.Callable]): If provided, and a cache miss occurs, the
            function\'s return value will be translated by this function before
            being cached.
        time (int): Tells memcached the time which this value should expire, either
            as a delta number of seconds, or an absolute unix time-since-the-epoch
            value. See the memcached protocol docs section "Storage Commands"
            for more info on <exptime>. We default to 0 == cache forever.
        min_compress_len (int): The threshold length to kick in auto-compression
            of the value using the zlib.compress() routine. If the value being cached is
            a string, then the length of the string is measured, else if the value is an
            object, then the length of the pickle result is measured. If the resulting
            attempt at compression yeilds a larger string than the input, then it is
            discarded. For backwards compatability, this parameter defaults to 0,
            indicating don\'t ever try to compress.
        debug (bool): If True, memcache keys are kept human readable, so you can
            read them if running a foreground memcached proc with \'memcached -vv\'.
            However this increases chances of key clashes so should not be left
            turned on.
    '''

class DoNotCache:
    result: Any
    def __init__(self, result) -> None: ...
