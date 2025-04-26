from _typeshed import Incomplete
from collections.abc import Generator
from contextlib import contextmanager
from rez import __version__ as __version__, module_root_path as module_root_path
from rez.exceptions import ConfigurationError as ConfigurationError
from rez.system import system as system
from rez.utils.data_utils import AttrDictWrapper as AttrDictWrapper, DelayLoad as DelayLoad, LazyAttributeMeta as LazyAttributeMeta, ModifyList as ModifyList, RO_AttrDictWrapper as RO_AttrDictWrapper, cached_class_property as cached_class_property, cached_property as cached_property, convert_dicts as convert_dicts, deep_update as deep_update
from rez.utils.formatting import expanduser as expanduser, expandvars as expandvars
from rez.utils.logging_ import get_debug_printer as get_debug_printer
from rez.utils.scope import scoped_format as scoped_format
from rez.utils.typing import Protocol as Protocol  # type: ignore[attr-defined]
from rez.vendor import yaml as yaml  # type: ignore[import-not-found]
from rez.vendor.schema.schema import And as And, Or as Or, Schema as Schema, SchemaError as SchemaError, Use as Use  # type: ignore[import-not-found]
from rez.vendor.yaml.error import YAMLError as YAMLError  # type: ignore[import-not-found]
from typing import Any, TypeVar

T = TypeVar('T')

class Validatable(Protocol):
    def validate(self, data: T) -> T: ...

class _Deprecation:
    __removed_in: Any
    __extra: Any | str
    def __init__(self, removed_in, extra: Incomplete | None = None) -> None: ...
    def get_message(self, name: str, env_var: bool | str = False): ...

class Setting:
    """Setting subclasses implement lazy setting validators.

    Note that lazy setting validation only happens on main configuration
    settings - plugin settings are validated on load only.
    """
    schema: Validatable
    config: Any
    key: Any
    def __init__(self, config, key) -> None: ...
    @property
    def _env_var_name(self) -> str: ...
    def _parse_env_var(self, value) -> None: ...
    def validate(self, data: Any) -> Any: ...
    def _validate(self, data): ...

class Str(Setting):
    schema: Validatable
    def _parse_env_var(self, value): ...

class Char(Setting):
    schema: Incomplete
    def _parse_env_var(self, value): ...

class OptionalStr(Str):
    schema: Incomplete

class StrList(Setting):
    schema: Validatable
    sep: str
    def _parse_env_var(self, value): ...

class PipInstallRemaps(Setting):
    """Ordered, pip install remappings."""
    PARDIR: Incomplete
    SEP: Incomplete
    RE_TOKENS: Incomplete
    TOKENS: Incomplete
    KEYS: Incomplete
    schema: Incomplete
    def validate(self, data: list) -> list:
        """Extended to substitute regex-escaped path tokens."""

class OptionalStrList(StrList):
    schema: Incomplete

class PathList(StrList):
    sep: Incomplete
    def _parse_env_var(self, value): ...

class Int(Setting):
    schema: Incomplete
    def _parse_env_var(self, value): ...

class Float(Setting):
    schema: Incomplete
    def _parse_env_var(self, value): ...

class Bool(Setting):
    schema: Validatable
    true_words: Incomplete
    false_words: Incomplete
    all_words = true_words | false_words
    def _parse_env_var(self, value) -> bool: ...  # type: ignore[override]

class OptionalBool(Bool):
    schema: Incomplete

class ForceOrBool(Bool):
    FORCE_STR: str
    schema: Incomplete
    all_words: Incomplete
    def _parse_env_var(self, value): ...

class Dict(Setting):
    schema: Validatable
    def _parse_env_var(self, value): ...

class OptionalDict(Dict):
    schema: Incomplete

class OptionalDictOrDictList(Setting):
    schema: Incomplete

class SuiteVisibility_(Str):
    @cached_class_property
    def schema(cls): ...

class VariantSelectMode_(Str):
    @cached_class_property
    def schema(cls): ...

class RezToolsVisibility_(Str):
    @cached_class_property
    def schema(cls): ...

class ExecutableScriptMode_(Str):
    @cached_class_property
    def schema(cls): ...

class OptionalStrOrFunction(Setting):
    schema: Incomplete
    def _parse_env_var(self, value): ...

class PreprocessMode_(Str):
    @cached_class_property
    def schema(cls): ...

class BuildThreadCount_(Setting):
    @cached_class_property
    def schema(cls): ...
    def _parse_env_var(self, value): ...

config_schema: Incomplete
_deprecated_settings: Incomplete
_plugin_config_dict: Incomplete

class Config(metaclass=LazyAttributeMeta):
    """Rez configuration settings.

    You should call the `create_config` function, rather than constructing a
    `Config` object directly.

    Config files are merged with other config files to create a `Config`
    instance. The 'rezconfig' file in rez acts as the primary - other config
    files update the primary configuration to create the final config. See the
    comments at the top of 'rezconfig' for more details.
    """
    schema = config_schema
    schema_error = ConfigurationError
    def __getattr__(self, item: str) -> Any: ...
    filepaths: list[str]
    _sourced_filepaths: list[str] | None
    overrides: Any | dict[Any, Any]
    locked: bool
    def __init__(self, filepaths: list[str], overrides: Incomplete | None = None, locked: bool = False) -> None:
        """Create a config.

        Args:
            filepaths (list of str): List of config files to load.
            overrides (dict): A dict containing settings that override all
                others. Nested settings are overridden with nested dicts.
            locked: If True, settings overrides in environment variables are
                ignored.
        """
    def get(self, key, default: Incomplete | None = None):
        """Get the value of a setting."""
    def copy(self, overrides: Incomplete | None = None, locked: bool = False) -> Config:
        """Create a separate copy of this config."""
    def override(self, key: str, value):
        """Set a setting to the given value.

        Note that `key` can be in dotted form, eg
        'plugins.release_hook.emailer.sender'.
        """
    def is_overridden(self, key: str) -> bool: ...
    def remove_override(self, key: str):
        """Remove a setting override, if one exists."""
    def warn(self, key: str):
        """Returns True if the warning setting is enabled."""
    def debug(self, key: str):
        """Returns True if the debug setting is enabled."""
    def debug_printer(self, key: str):
        """Returns a printer object suitably enabled based on the given key."""
    @cached_property
    def sourced_filepaths(self):
        """Get the list of files actually sourced to create the config.

        Note:
            `self.filepaths` refers to the filepaths used to search for the
            configs, which does dot necessarily match the files used. For example,
            some files may not exist, while others are chosen as rezconfig.py in
            preference to rezconfig, rezconfig.yaml.

        Returns:
            List of str: The sourced files.
        """
    @cached_property
    def plugins(self):
        """Plugin settings are loaded lazily, to avoid loading the plugins
        until necessary."""
    @property
    def data(self):
        """Returns the entire configuration as a dict.

        Note that this will force all plugins to be loaded.
        """
    @property
    def nonlocal_packages_path(self):
        """Returns package search paths with local path removed."""
    def get_completions(self, prefix): ...
    def _uncache(self, key: Incomplete | None = None) -> None: ...
    def _swap(self, other) -> None:
        """Swap this config with another.

        This is used by the unit tests to swap the config to one that is
        shielded from any user config updates. Do not use this method unless
        you have good reason.
        """
    def _validate_key(self, key, value, key_schema): ...
    @cached_property
    def _data_without_overrides(self): ...
    @cached_property
    def _data(self): ...
    @classmethod
    def _create_main_config(cls, overrides: Incomplete | None = None) -> Config:
        """See comment block at top of 'rezconfig' describing how the main
        config is assembled."""
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def _get_tmpdir(self): ...
    def _get_context_tmpdir(self): ...
    def _get_image_viewer(self): ...
    def _get_editor(self): ...
    def _get_difftool(self): ...
    def _get_terminal_emulator_command(self): ...
    def _get_new_session_popen_args(self): ...

class _PluginConfigs:
    """Lazy config loading for plugins."""
    def __init__(self, plugin_data) -> None: ...
    def __setattr__(self, attr, value) -> None: ...
    def __getattr__(self, attr: str) -> Any: ...
    def __iter__(self): ...
    def override(self, key, value) -> None: ...
    def data(self): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...

def expand_system_vars(data: T) -> T:
    """Expands any strings within `data` such as '{system.user}'."""
def create_config(overrides: Incomplete | None = None) -> Config:
    """Create a configuration based on the global config.
    """
def _create_locked_config(overrides: Incomplete | None = None):
    """Create a locked config.

    The config created by this function only reads settings from the main
    rezconfig file, and from plugin rezconfig files. All other files normally
    used by the main config (~/.rezconfig etc) are ignored, as are environment
    variable overrides.

    Returns:
        `Config` object.
    """
@contextmanager
def _replace_config(other) -> Generator[None]:
    """Temporarily replace the global config.
    """
def _load_config_py(filepath: str) -> dict[str, Any]: ...
def _load_config_yaml(filepath: str) -> dict[str, Any]: ...
def _load_config_from_filepaths(filepaths: list[str]) -> tuple[dict[str, Any], list[str]]: ...
def get_module_root_config() -> str: ...

config: Incomplete
