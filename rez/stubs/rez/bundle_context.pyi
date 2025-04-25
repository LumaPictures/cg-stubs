from _typeshed import Incomplete
from rez.exceptions import ContextBundleError as ContextBundleError
from rez.package_copy import copy_package as copy_package
from rez.util import which as which
from rez.utils.filesystem import is_subdirectory as is_subdirectory
from rez.utils.logging_ import print_info as print_info, print_warning as print_warning
from rez.utils.platform_ import platform_ as platform_
from rez.utils.yaml import save_yaml as save_yaml
from typing import Any

def bundle_context(context, dest_dir, force: bool = False, skip_non_relocatable: bool = False, quiet: bool = False, patch_libs: bool = False, verbose: bool = False) -> None:
    """Bundle a context and its variants into a relocatable dir.

    This creates a copy of a context with its variants retargeted to a local
    package repository containing only the variants the context uses. The
    generated file structure looks like so::

        /dest_dir/
            /context.rxt
            /packages/
                /foo/1.1.1/package.py
                          /...(payload)...
                /bah/4.5.6/package.py
                          /...(payload)...

    Args:
        context (`ResolvedContext`): Context to bundle
        dest_dir (str): Destination directory. Must not exist.
        force (bool): If True, relocate package even if non-relocatable. Use at
            your own risk. Overrides `skip_non_relocatable`.
        skip_non_relocatable (bool): If True, leave non-relocatable packages
            unchanged. Normally this will raise a `PackageCopyError`.
        quiet (bool): Suppress all output
        patch_libs (bool): If True, modify libs and executables within the
            bundle to patch any references to external packages back to their
            equivalents within the bundle. See
            https://rez.readthedocs.io/en/stable/context_bundles.html#patching-libraries
            for more details on this.
        verbose (bool): Verbose mode (quiet will override)
    """

class _ContextBundler:
    """Performs context bundling.
    """
    context: Any
    dest_dir: Any
    force: bool
    skip_non_relocatable: bool
    quiet: bool
    patch_libs: bool
    verbose: bool
    logs: list[Any]
    copied_variants: dict[Any, Any]
    def __init__(self, context, dest_dir, force: bool = False, skip_non_relocatable: bool = False, quiet: bool = False, patch_libs: bool = False, verbose: bool = False) -> None: ...
    def bundle(self) -> None: ...
    @property
    def _repo_path(self): ...
    def _info(self, msg, *nargs) -> None: ...
    def _verbose_info(self, msg, *nargs) -> None: ...
    def _warning(self, msg, *nargs) -> None: ...
    def _init_bundle(self) -> None: ...
    def _finalize_bundle(self) -> None: ...
    def _copy_variants(self): ...
    def _write_retargeted_context(self, relocated_package_names) -> None: ...
    def _patch_libs(self) -> None: ...
    def _patch_libs_linux(self) -> None:
        '''Fix elfs that reference elfs outside of the bundle.

        Finds elf files, inspects their runpath/rpath, then looks to see if
        those paths map to packages also inside the bundle. If they do, those
        rpath entries are remapped to form "$ORIGIN/{relative-path}".
        '''
    def _find_files(self, executable: bool = False, filename_substrs: Incomplete | None = None): ...
