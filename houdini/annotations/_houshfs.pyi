import asyncio
from collections.abc import Callable

import _haio
import _hwebserver

# progress_callback(tag, downloaded, total, message) and debug_callback(tag, message_type, message).
# The result is (status, saved file name, error_code, error_message).
def download(shfs_subpath: str, progress_callback: Callable[[str, int, int, str], object] | None = ..., debug_callback: Callable[[str, int, bytes], object] | None = ..., allow_launcher: bool = ...) -> asyncio.Future[tuple[_hwebserver.HTTPStatus, str, _haio.CppErrorCode, str]]: ...
