# mypy: disable-error-code="misc, override, no-redef"

import types
from _typeshed import Incomplete

class UsdzAssetIterator:
    """
    Class that provides an iterator for usdz assets. Within context, it
    extracts the contents of the usdz package, provides generators for all usd
    files and all assets and on exit packs the extracted files back recursively 
    into a usdz package.
    Note that root layer of the usdz package might not be compliant which can
    cause UsdzAssetIterator to raise an exception while repacking on exit.
    """
    def __init__(self, usdzFile, verbose, parentDir: Incomplete | None = ...) -> None: ...
    def AllAssets(self):
        """
        Generator for all assets packed in the usdz package, respecting nested
        usdz assets.
        """
    def UsdAssets(self):
        """
        Generator for UsdAssets respecting nested usdz assets.
        """
    @staticmethod
    def _CreateUsdzPackage(usdzFile, filesToAdd, verbose): ...
    def _ExtractedFiles(self): ...
    def __enter__(self): ...
    def __exit__(self, excType: type[BaseException] | None, excVal: BaseException | None, excTB: types.TracebackType | None): ...

def ExtractUsdzPackage(usdzFile, extractDir, recurse, verbose, force):
    """
    Given a usdz package usdzFile, extracts the contents of the archive under
    the extractDir directory. Since usdz packages can contain other usdz
    packages, recurse flag can be used to extract the nested structure
    appropriately.
    """
def _AllowedUsdExtensions(): ...
def _AllowedUsdzExtensions(): ...
def _Err(msg): ...
def _Print(msg): ...
