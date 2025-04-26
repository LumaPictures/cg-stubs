import rez.package_test
from _typeshed import Incomplete
from rez.build_process import BuildProcessHelper
from rez.build_system import BuildResult as BuildResult
from rez.packages import Variant
from typing import Any

class LocalBuildProcess(BuildProcessHelper):
    """The default build process.

    This process builds a package's variants sequentially and on localhost.
    """
    tmpdir_manager: Incomplete
    @classmethod
    def name(cls) -> str: ...  # type: ignore[override]
    ran_test_names: set[Any]
    all_test_results: rez.package_test.PackageTestResults
    def __init__(self, *nargs, **kwargs) -> None: ...
    def build(self, install_path: str | None = None, clean: bool = False, install: bool = False, variants: list[int] | None = None) -> int: ...
    def release(self, release_message: Incomplete | None = None, variants: list[int] | None = None): ...
    def _build_variant_base(self, variant: Variant, build_type, install_path: str | None = None, clean: bool = False, install: bool = False, **kwargs) -> BuildResult: ...
    def _install_include_modules(self, install_path: str) -> None: ...
    def _rmtree(self, path) -> None: ...
    def _build_variant(self, variant: Variant, install_path: str | None = None, clean: bool = False, install: bool = False, **kwargs) -> str | None: ...
    def _release_variant(self, variant: Variant, release_message: Incomplete | None = None, **kwargs): ...
    def _run_tests(self, variant, run_on, package_install_path) -> None:
        """Possibly run package tests on the given variant.

        During an install/release, the following steps occur:
        1. The variant's payload is installed, but package.py is not yet updated
           (see `self._build_variant_base`)
        2. The variant is installed on its own, into a temp package.py
        3. Tests are run on this temp variant, whose root is patched to point
           at the real variant payload installation
        4. On success, the rest of the release process goes ahead, and the real
           package.py is updated appropriately
        5. On failure, the release is aborted.
        """

def register_plugin(): ...
