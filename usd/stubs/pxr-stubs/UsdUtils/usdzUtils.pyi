from _typeshed import Incomplete
from collections.abc import Generator
from contextlib import contextmanager as contextmanager

def _Print(msg) -> None: ...
def _Err(msg) -> None: ...
def _AllowedUsdzExtensions(): ...
def _AllowedUsdExtensions(): ...
def ExtractUsdzPackage(usdzFile, extractDir, recurse, verbose, force):
    """
    Given a usdz package usdzFile, extracts the contents of the archive under
    the extractDir directory. Since usdz packages can contain other usdz
    packages, recurse flag can be used to extract the nested structure
    appropriately.
    """

class UsdzAssetIterator:
    """
    Class that provides an iterator for usdz assets. Within context, it
    extracts the contents of the usdz package, provides generators for all usd
    files and all assets and on exit packs the extracted files back recursively 
    into a usdz package.
    Note that root layer of the usdz package might not be compliant which can
    cause UsdzAssetIterator to raise an exception while repacking on exit.
    """
    _tmpDir: Incomplete
    extractDir: Incomplete
    usdzFile: Incomplete
    verbose: Incomplete
    def __init__(self, usdzFile, verbose, parentDir: Incomplete | None = None) -> None: ...
    def _ExtractedFiles(self): ...
    @staticmethod
    def _CreateUsdzPackage(usdzFile, filesToAdd, verbose): ...
    def __enter__(self): ...
    def __exit__(self, excType: type[BaseException] | None, excVal: BaseException | None, excTB: types.TracebackType | None) -> None: ...  # type: ignore[name-defined]
    def UsdAssets(self) -> Generator[Incomplete, Incomplete]:
        """
        Generator for UsdAssets respecting nested usdz assets.
        """
    def AllAssets(self) -> Generator[Incomplete, Incomplete]:
        """
        Generator for all assets packed in the usdz package, respecting nested
        usdz assets.
        """
