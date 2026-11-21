from collections.abc import Mapping
from typing import Any

import flask

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
    **kwargs: Any,
) -> int | None: ...
def start_dev_server(
    host: str = ...,
    port: int = ...,
    debug: bool | None = ...,
    bgindex: bool | None = ...,
    config_file: str | None = ...,
    **kwargs: Any,
) -> int | None: ...
def start_app_server(
    host: str = ...,
    port: int = ...,
    debug: bool | None = ...,
    bgindex: bool | None = ...,
    config_file: str | None = ...,
    **kwargs: Any,
) -> int | None: ...
