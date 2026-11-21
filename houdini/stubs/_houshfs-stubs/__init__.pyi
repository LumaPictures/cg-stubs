# Houdini stubs generated from Houdini 22.0.466

import asyncio
from collections.abc import Callable

import _haio
import _hwebserver
from typing import Any

__version__: str

def clearInstalledCache() -> None:
    """clearInstalledCache() -> None"""
def download(shfs_subpath: str, progress_callback: Callable[[str, int, int, str], object] | None = ..., debug_callback: Callable[[str, int, bytes], object] | None = ..., allow_launcher: bool = ...) -> asyncio.Future[tuple[_hwebserver.HTTPStatus, str, _haio.CppErrorCode, str]]:
    """download(shfs_subpath: str, progress_callback: object = None, debug_callback: object = None, allow_launcher: bool = True) -> object"""
def isInstalled(shfs_subpath: str) -> bool:
    """isInstalled(shfs_subpath: str) -> bool"""
def version_info() -> str:
    """version_info() -> str"""
