import typing
from bookish import search as search
from bookish.stores import _StoreSpec
from bookish.text import textify as textify
from bookish.wiki.config import Config as Config

from typing import TypeVar
from typing import TypeVar
import flask
_ConfigT = TypeVar('_ConfigT', bound=flask.Config | Config)
this_dir: str

def expandpath(path: str) -> str: ...
@typing.overload
def read_config(cfg: None = ..., config_file: str | None = ..., root_path: str = ..., config_obj: type[object] | str | None = ...) -> Config: ...
@typing.overload
def read_config(cfg: _ConfigT, config_file: str | None = ..., root_path: str = ..., config_obj: type[object] | str | None = ...) -> _ConfigT | Config: ...

class DefaultConfig:
    SECRET_KEY: str
    DEBUG: bool
    ICON_32: str
    ICON_144: str
    PYGMENTS_CSS: str
    SUPPORT_DOCUMENTS: list[_StoreSpec]
    DOCUMENTS: list[_StoreSpec]
    EXTRA_DOCUMENTS: list[_StoreSpec]
    SCSS_ASSET_DIR: str
    EDITABLE: bool
    EDIT_STORE: _StoreSpec | None
    WIKI_STYLE: str
    TEMPLATE: str
    SEARCH_TEMPLATE: str
    PAGES_CLASS: str
    CACHE_DIR: str
    INDEX_DIR: str
    SEARCHABLES: str
    ENABLE_BACKGROUND_INDEXING: bool
    BACKGROUND_INDEXING_INTERVAL: float
    AUTOSAVE: bool
    AUTOSAVE_SECONDS: float
    CHECKPOINT_MAX: int
    TEXTIFY_CLASS: type[textify.TextifierBase] | str
    INDEX_PAGE_NAME: str
    WIKI_EXT: str
    DEFAULT_LANGUAGE: str
    DEFAULT_LOCALE: str
    CATEGORIES: str
    SEARCH_SHORTCUTS: list[dict[str, str]]
