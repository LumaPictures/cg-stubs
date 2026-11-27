import flask
import ssl
from collections.abc import Iterable, Mapping
from typing import Any, Literal
from typing_extensions import TypedDict, Unpack
from werkzeug.serving import WSGIRequestHandler as WSGIRequestHandler

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
    ssl_context: ssl.SSLContext | tuple[str, str | None] | Literal['adhoc'] | None

class _StartServerKwargs(_RunKwargs, total=False):
    override_config: Mapping[str, Any] | None
    use_houdini_path: bool
    auto_compile_scss: bool | None
    use_waitress: bool

def default_houdini_app(override_config: Mapping[str, Any] | None = None, config_file: str | None = None) -> flask.Flask: ...
def get_houdini_app(override_config: Mapping[str, Any] | None = None, use_houdini_path: bool = True, config_file: str | None = None, auto_compile_scss: bool | None = None, bgindex: bool | None = None, logfile: str | None = None, loglevel: str | None = None, debug: bool | None = None) -> flask.Flask: ...
def start_server(host: str = '0.0.0.0', port: int = 8080, override_config: Mapping[str, Any] | None = None, debug: bool | None = False, bgindex: bool | None = None, config_file: str | None = None, use_houdini_path: bool = True, auto_compile_scss: bool | None = None, use_waitress: bool = False, **kwargs: Unpack[_RunKwargs]) -> int | None: ...
def start_dev_server(host: str = '0.0.0.0', port: int = 8080, debug: bool | None = True, bgindex: bool | None = None, config_file: str | None = None, **kwargs: Unpack[_StartServerKwargs]) -> int | None: ...
def start_app_server(host: str = '0.0.0.0', port: int = 48626, debug: bool | None = None, bgindex: bool | None = None, config_file: str | None = None, **kwargs: Unpack[_StartServerKwargs]) -> int | None: ...
