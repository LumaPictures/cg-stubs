# Houdini stubs generated from Houdini 22.0.466

import typing
from bookish.config import DefaultConfig
from bookish.stores import _StoreSpec
from bookish.text import textify as textify
from bookish.wiki.config import Config
from houdinihelp.hcoloring import HScriptLexer as HScriptLexer, OpenCLLexer as OpenCLLexer, VexLexer as VexLexer
from houdinihelp.usd import UsdLexer as UsdLexer
from pygments.lexer import RegexLexer as RegexLexer

from typing import TypeVar
from typing import TypeVar
import flask
_ConfigT = TypeVar('_ConfigT', bound=flask.Config | Config)
ver_major: str
ver_minor: str
ver_build: str
houdini_version: str | None

class HoudniBaseConfig(DefaultConfig):
    USE_HOU: bool
    DEBUG: bool
    LOGLEVEL: str
    PYGMENTS_CSS: str
    HOUDINI_VERSION_MAJOR: str
    HOUDINI_VERSION_MINOR: str
    HOUDINI_VERSION_BUILD: str
    EXTRA_DOCUMENTS: list[_StoreSpec]
    CACHE_DIR: str
    INDEX_DIR: str
    INDEX_USAGES: bool
    INDEX_IGNORE_FILE: str | None
    ENABLE_BACKGROUND_INDEXING: bool
    BACKGROUND_INDEXING_INTERVAL: float
    PAGES_CLASS: str
    SEARCHABLES: str
    TEXTIFY_CLASS: type[textify.TextifierBase] | str
    MARKDOWN_CLASS: str
    WIKI_STYLE: str
    TEMPLATE: str
    SEARCH_TEMPLATE: str
    LEXERS: dict[str, type[RegexLexer]]
    SHORTCUTS: list[dict[str, str]]
    EXTRA_SHORTCUTS: list[dict[str, str]]
    CATEGORIES: str
    AUTO_COMPILE_SCSS: bool

class HoudiniHfsConfig(HoudniBaseConfig):
    SUPPORT_DOCUMENTS: list[_StoreSpec]
    DOCUMENTS: list[_StoreSpec]
    STATIC_DIRS: dict[str, str]
    STATIC_LOCATIONS: tuple[str, ...]
    ARCHIVE_DIRS: dict[str, str]

class HoudiniShdConfig(HoudniBaseConfig):
    SUPPORT_DOCUMENTS: list[_StoreSpec]
    DOCUMENTS: list[_StoreSpec]
    STATIC_LOCATIONS: tuple[str, ...]
    ARCHIVE_DIRS: dict[str, str]

@typing.overload
def read_houdini_config(cfg: None = ..., config_file: str | None = ..., root_path: str = ..., use_houdini_path: bool = ..., with_source: bool = ...) -> Config: ...
@typing.overload
def read_houdini_config(cfg: _ConfigT, config_file: str | None = ..., root_path: str = ..., use_houdini_path: bool = ..., with_source: bool = ...) -> _ConfigT | Config: ...
