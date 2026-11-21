# Houdini stubs generated from Houdini 22.0.466

import builtins
from collections.abc import Mapping
from dataclasses import dataclass
from houtypes import JSONValue
from typing import Callable as Callable

from typing import TypeVar
from typing import TypeVar
_T = TypeVar('_T')
_V = TypeVar('_V', bound=JSONValue)
@dataclass
class MergeRule:
    """
    This class allows to specify a rule for a data type under a specific keys or paths.

    This rule ensures that any integer value under 'counter' key, or under '/root/digits' key will be added together.
    MergeRule(int, 'add', ['counter', '/root/digits'])

    :param type: The type of the value this rule applies to. (dict, list, int, float, str, bool)
    :param name: The name of the registered function in DataMerge class to be used for the merging.
    :param keys: This rule will apply to the values under this key. Use full path if you want to be specific about what key this should affect.
    """
    type: builtins.type[object]
    name: str
    keys: list[str]
    def matches(self, key: str) -> bool:
        """
        Returns whether a key applies to this rule.
        :param key: The string key to look for.
        :return: whether this rule matches this key
        """

class DataMerger:
    def __init__(self, rules: list[MergeRule] = ...) -> None:
        """
        Init function for Data Merger.
        :param rules: A list of rules that modify what the rule used for certain values in the data.
        """
    def merge(self, base: JSONValue, new: JSONValue) -> JSONValue:
        """
        This function merges new into base.
        :param base: The dict, list, int, float, str, bool values to merge with new.
        :param new: The dict, list, int, float, str, bool values to merge with base.
        :return: The result of base and new merged together.
        """
    def addMergeRuleFunction(self, rule_type: builtins.type[_V], rule_name: str, func: Callable[[DataMerger, _V, _V, str], JSONValue]) -> None:
        """
        Adds a new or overwrites an existing rule function.
        :param rule_type: The type for which this rule applies to. (dict, list, str, float, int, bool)
        :param rule_name: The name by which to register this rule ('override', 'append', etc...)
        :param func: The function that does the merge operation with the following inputs: (data_merger: DataMerger, base: Any, new: Any, path: str) -> Any:
        :return: None
        """
    def stringSeparator(self) -> str:
        """
        Returns the string separator used when strings are appended to each other.
        :return: the string separator.
        """
    def setStringSeparator(self, separator: str = ';') -> None:
        """
        Sets the string separator that is used when strings are appended to each other.
        :param separator:
        :return:
        """
    def process(self, base: JSONValue, new: JSONValue, path: str = '') -> JSONValue: ...

def rule_override(data_merger: DataMerger, base: object, new: _T, path: str) -> _T: ...
def rule_use_existing(data_merger: DataMerger, base: _T, new: object, path: str) -> _T: ...
def rule_list_prepend(data_merger: DataMerger, base: list[_T], new: list[_T], path: str) -> list[_T]: ...
def rule_list_append(data_merger: DataMerger, base: list[_T], new: list[_T], path: str) -> list[_T]: ...
def rule_list_append_unique(data_merger: DataMerger, base: list[_T], new: list[_T], path: str) -> list[_T]: ...
def rule_dict_update(data_merger: DataMerger, base: dict[str, JSONValue], new: Mapping[str, JSONValue], path: str) -> dict[str, JSONValue]: ...
def rule_str_append(data_merger: DataMerger, base: str, new: str, path: str) -> str: ...
def rule_str_prepend(data_merger: DataMerger, base: str, new: str, path: str) -> str: ...
def rule_digit_add(data_merger: DataMerger, base: int | float, new: int | float, path: str) -> int | float: ...
def rule_digit_subtract(data_merger: DataMerger, base: int | float, new: int | float, path: str) -> int | float: ...
def rule_digit_multiply(data_merger: DataMerger, base: int | float, new: int | float, path: str) -> int | float: ...
