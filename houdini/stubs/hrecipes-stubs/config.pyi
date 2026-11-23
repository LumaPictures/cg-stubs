import pathlib
from . import utils as utils
from collections.abc import Generator, Mapping
from houtypes import JSONLike
from typing import Iterable, TypedDict

from typing import TypeVar
from typing import TypeVar
_T = TypeVar('_T')
class ConfigDict(TypedDict, total=True):
    permanent_nodetype_defaults: dict[str, str]

CONFIG_FILE_NAME: str
USER_PREFS_DIR: str

def configFilePath() -> pathlib.Path: ...

ADDITIVE_LIST_CONFIG_KEYS: set[str]
ADDITIVE_DICT_CONFIG_KEYS: set[str]

def defaultConfig() -> ConfigDict: ...
def freshConfig() -> ConfigDict: ...
def saveUserConfig(config: ConfigDict | Mapping[str, JSONLike]) -> None: ...
def loadUserConfig() -> ConfigDict: ...
def loadConfig() -> ConfigDict: ...
def dedup(items: Iterable[_T]) -> Generator[_T, None, None]: ...
