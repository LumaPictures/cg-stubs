from collections.abc import Sequence
from typing import Any, Literal, TypedDict, overload

from typing_extensions import TypeVar

from houtypes import JSONLike, JSONValue

_D = TypeVar("_D", default=None)

class _AttrConfig(TypedDict, total=False):
    default: float | str | Sequence[float]
    identity: float | Sequence[float]
    min: float
    max: float
    type: str
    component_type: str
    modify: str
    scale: str
    precision: float
    # One of husdui.constants' *_TYPE values.
    uitype: int
    label: str
    component_labels: Sequence[str]
    # Keyword arguments for the hou.ParmTemplate.
    kwargs: dict[str, Any]

class Prefs:
    def __init__(self, pref_filename: str) -> None: ...
    # readPrefs() sets these keys' defaults; the others come from the JSON pref files.
    @overload
    def pref(
        self,
        pref_name: Literal["lights.search", "collections.search", "sheet.show_attributes", "mixer.show_attributes"],
        default: object = ...,
    ) -> list[str]: ...
    @overload
    def pref(self, pref_name: Literal["attributes.config"], default: object = ...) -> dict[str, _AttrConfig]: ...
    @overload
    def pref(self, pref_name: Literal["main.default_tab"], default: object = ...) -> int: ...
    @overload
    def pref(self, pref_name: str, default: _D = ...) -> JSONValue | _D: ...
    def writePrefs(self) -> None: ...
    def readPrefs(self) -> None: ...
    def setAttrAllConfig(self, attr_name: str, attr_config: _AttrConfig) -> None: ...
    def attrAllConfig(self, attr_name: str) -> _AttrConfig: ...
    # A list value comes back as a tuple.
    @overload
    def attrConfig(
        self,
        attr_name: str,
        config_name: Literal["type", "component_type", "modify", "scale", "label"],
        default: _D = ...,
    ) -> str | _D: ...
    @overload
    def attrConfig(
        self, attr_name: str, config_name: Literal["min", "max", "precision"], default: _D = ...
    ) -> float | _D: ...
    @overload
    def attrConfig(self, attr_name: str, config_name: Literal["uitype"], default: _D = ...) -> int | _D: ...
    @overload
    def attrConfig(
        self, attr_name: str, config_name: Literal["default"], default: _D = ...
    ) -> float | str | Sequence[float] | _D: ...
    @overload
    def attrConfig(
        self, attr_name: str, config_name: Literal["identity"], default: _D = ...
    ) -> float | Sequence[float] | _D: ...
    @overload
    def attrConfig(
        self, attr_name: str, config_name: Literal["component_labels"], default: _D = ...
    ) -> Sequence[str] | _D: ...
    @overload
    def attrConfig(self, attr_name: str, config_name: Literal["kwargs"], default: _D = ...) -> dict[str, Any] | _D: ...
    @overload
    def attrConfig(self, attr_name: str, config_name: str, default: _D = ...) -> JSONValue | tuple[JSONValue, ...] | _D: ...

class SimplePrefs:
    def __init__(self, filename: str) -> None: ...
    def setPref(self, name: str, value: JSONLike) -> None: ...
    def getPref(self, name: str, default: _D = ...) -> JSONValue | _D: ...
