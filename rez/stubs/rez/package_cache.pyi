from _typeshed import Incomplete
from collections.abc import Generator
from contextlib import contextmanager
from rez.config import config as config
from rez.exceptions import PackageCacheError as PackageCacheError
from rez.packages import Variant as Variant, get_variant as get_variant
from rez.system import system as system
from rez.utils.colorize import ColorizedStreamHandler as ColorizedStreamHandler
from rez.utils.filesystem import forceful_rmtree as forceful_rmtree, rename as rename, safe_listdir as safe_listdir, safe_makedirs as safe_makedirs, safe_remove as safe_remove
from rez.utils.logging_ import print_warning as print_warning
from rez.vendor.lockfile import LockFile as LockFile, NotLocked as NotLocked  # type: ignore[import-not-found]
from rez.vendor.progress.spinner import PixelSpinner as PixelSpinner  # type: ignore[import-not-found]
from typing import Iterable

class PackageCache:
    """Package cache.

    A package cache is responsible for storing copies of variant payloads into a
    location that would typically be on local disk. The intent is to avoid
    fetching a package's files over shared storage at runtime.

    A package cache is used like so:

    * A rez-env is performed;
    * The context is resolved;
    * For each variant in the context, we check to see if it's present in the current package cache;
    * If it is, the variant's root is remapped to this location.

    A package cache is **not** a package repository. It just stores copies of
    variant payloads - no package definitions are stored.

    Payloads are stored into the following structure::

        /<cache_dir>/foo/1.0.0/af8d/a/<payload>
                                   /a.json

    Here, 'af8d' is the first 4 chars of the SHA1 hash of the variant's 'handle',
    which is a dict of fields that uniquely identify the variant. To avoid
    hash collisions, the variant is then stored under a subdir that is incrementally
    named ('a', 'b', ..., 'aa', 'ab', ...). The 'a.json' file is used to find the
    correct variant within the hash subdir. The intent is to keep cached paths
    short, and avoid having to search too many variant.json files to find the
    matching variant.
    """
    VARIANT_NOT_FOUND: int
    VARIANT_FOUND: int
    VARIANT_CREATED: int
    VARIANT_COPYING: int
    VARIANT_COPY_STALLED: int
    VARIANT_PENDING: int
    VARIANT_REMOVED: int
    STATUS_DESCRIPTIONS: Incomplete
    _FILELOCK_TIMEOUT: int
    _COPYING_TIME_INC: float
    _COPYING_TIME_MAX: float
    path: str
    def __init__(self, path: str) -> None:
        """Create a package cache.

        Args:
            path (str): Path on disk, must exist.
        """
    def get_cached_root(self, variant: Variant) -> str | None:
        """Get location of variant payload copy.

        Args:
            variant (`Variant`): Variant to search for.

        Returns:
            str: Cached variant root path, or None if not found.
        """
    def add_variant(self, variant, force: bool = False, wait_for_copying: bool = False, logger: Incomplete | None = None):
        """Copy a variant's payload into the cache.

        The following steps are taken to ensure muti-thread/proc safety, and to
        guarantee that a partially-copied variant payload is never able to be
        used:

        1. The hash dir (eg '/<cache_dir>/foo/1.0.0/af8d') is created;
        2. A file lock mutex ('/<cache_dir>/.lock') is acquired;
        3. The file '/<cache_dir>/foo/1.0.0/af8d/.copying-a' (or -b, -c etc) is
           created. This tells rez that this variant is being copied and cannot
           be used yet;
        4. The file '/<cache_dir>/foo/1.0.0/af8d/a.json' is created. Now
           another proc/thread can't create the same local variant;
        5. The file lock is released;
        6. The variant payload is copied to '/<cache_dir>/foo/1.0.0/af8d/a';
        7. The '.copying-a' file is removed.

        Note that the variant will not be cached in the following circumstances,
        unless `force` is True:

        - The variant is not cachable as determined by `Variant.is_cachable`;
        - The variant is from a local package, and 'config.package_cache_local'
          is False;
        - The variant is stored on the same disk device as this cache, and
          config.package_cache_same_device' is False.

        Args:
            variant (Variant): The variant to copy into this cache
            force (bool): Copy the variant regardless. Use at your own risk (there
                is no guarantee the resulting variant payload will be functional).
            wait_for_copying (bool): Whether the caching step should block when one of the
                pending variants is marked as already copying.
            logger (None | Logger): If a logger is provided, log information to it.

        Returns:
            tuple: 2-tuple:
            - str: Path to cached payload
            - int: One of VARIANT_FOUND, VARIANT_CREATED, VARIANT_COPYING, VARIANT_COPY_STALLED
        """
    def remove_variant(self, variant: Variant):
        """Remove a variant from the cache.

        Since this removes the associated cached variant payload, there is no
        guarantee that this will not break packages currently in use by a
        context.

        Note that this does not actually free up associated disk space - you
        must call clean() to do that.

        Returns:
            int: One of:
            - VARIANT_REMOVED
            - VARIANT_NOT_FOUND
            - VARIANT_COPYING
        """
    def add_variants_async(self, variants):
        """Update the package cache by adding some or all of the given variants.

        This method is called when a context is created or sourced. Variants
        are then added to the cache in a separate process.

        .. deprecated:: 3.2.0
           Use :method:`add_variants` instead.
        """
    def add_variants(self, variants: Iterable[Variant], package_cache_async: bool = True):
        """Add the given variants to the package payload cache.
        """
    @staticmethod
    def _subprocess_package_caching_daemon(path):
        """
        Run the package cache in a daemon process

        Returns:
            subprocess.Popen : The package caching daemon process
        """
    def get_variants(self):
        """Get variants and their current statuses from the cache.

        Returns:
            tuple: List of 3-tuple:

            - `Variant`: The cached variant
            - str: Local cache path for variant, if determined ('' otherwise)
            - int: Status. One of:
              - VARIANT_FOUND
              - VARIANT_COPYING
              - VARIANT_COPY_STALLED
              - VARIANT_PENDING
        """
    def run_daemon(self) -> None:
        """Run as daemon and copy pending variants.

        Called via `rez-pkg-cache --daemon`.
        """
    def _run_caching_operation(self, wait_for_copying: bool = True):
        """Copy pending variants.

        Args:
            wait_for_copying (bool): Whether the caching step should block when one of the
                pending variants is marked as already copying.
        """
    def clean(self, time_limit: Incomplete | None = None) -> None:
        """Delete unused package cache files.

        This should be run periodically via 'rez-pkg-cache --clean'.

        This removes:

        - Variants that have not been used in more than 'config.package_cache_max_variant_days' days;
        - Variants that have stalled;
        - Variants that are already pending deletion (remove_variant() was used).

        Args:
            time_limit (float): Perform cleaning operations only up until this
                limit, resulting in a possibly incomplete cleanup. This is used
                to keep the cache size down without having to periodically
                run 'rez-pkg-cache --clean'.
        """
    @contextmanager
    def _lock(self) -> Generator[None]: ...
    def _run_caching_step(self, state, wait_for_copying: bool = False) -> bool: ...
    def _init_logging(self):
        """
        Creates logger that logs to file and stdout. Used for:
        - adding variants in daemonized proc;
        - clean(), which would typically be run as a cron, but can also be run
          manually (hence the logging to stdout also)
        """
    @property
    def _sys_dir(self): ...
    @property
    def _log_dir(self): ...
    @property
    def _pending_dir(self): ...
    @property
    def _remove_dir(self): ...
    def _get_cached_root(self, variant: Variant) -> tuple[int, str]: ...
    def _get_hash_path(self, variant: Variant) -> str: ...
