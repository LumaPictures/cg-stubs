import ssl
from collections.abc import Iterable, Mapping
from typing import Any, Literal

import flask
from typing_extensions import TypedDict, Unpack
from werkzeug.serving import WSGIRequestHandler

# The keywords start_server forwards to Flask.run (and on to werkzeug's run_simple); threaded is
# always passed explicitly.
class _RunKwargs(TypedDict, total=False):
    load_dotenv: bool
    use_reloader: bool
    use_debugger: bool
    use_evalex: bool
    extra_files: Iterable[str] | None
    exclude_patterns: Iterable[str] | None
    reloader_interval: int
    reloader_type: str
    processes: int
    request_handler: type[WSGIRequestHandler] | None
    static_files: dict[str, str | tuple[str, str]] | None
    passthrough_errors: bool
    ssl_context: ssl.SSLContext | tuple[str, str | None] | Literal["adhoc"] | None

class _StartServerKwargs(_RunKwargs, total=False):
    override_config: Mapping[str, Any] | None
    use_houdini_path: bool
    auto_compile_scss: bool | None
    use_waitress: bool

def default_houdini_app(override_config: Mapping[str, Any] | None = ..., config_file: str | None = ...) -> flask.Flask: ...
def get_houdini_app(
    override_config: Mapping[str, Any] | None = ...,
    use_houdini_path: bool = ...,
    config_file: str | None = ...,
    auto_compile_scss: bool | None = ...,
    bgindex: bool | None = ...,
    logfile: str | None = ...,
    loglevel: str | None = ...,
    debug: bool | None = ...,
) -> flask.Flask: ...
def start_server(
    host: str = ...,
    port: int = ...,
    override_config: Mapping[str, Any] | None = ...,
    debug: bool | None = ...,
    bgindex: bool | None = ...,
    config_file: str | None = ...,
    use_houdini_path: bool = ...,
    auto_compile_scss: bool | None = ...,
    use_waitress: bool = ...,
    **kwargs: Unpack[_RunKwargs],
) -> int | None: ...
def start_dev_server(
    host: str = ...,
    port: int = ...,
    debug: bool | None = ...,
    bgindex: bool | None = ...,
    config_file: str | None = ...,
    **kwargs: Unpack[_StartServerKwargs],
) -> int | None: ...
def start_app_server(
    host: str = ...,
    port: int = ...,
    debug: bool | None = ...,
    bgindex: bool | None = ...,
    config_file: str | None = ...,
    **kwargs: Unpack[_StartServerKwargs],
) -> int | None: ...
