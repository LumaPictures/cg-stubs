import re
from collections import OrderedDict
from collections.abc import Generator, Iterable
from typing import TypeAlias

from typing_extensions import TypedDict

from bookish.wiki.wikipages import WikiPages

# OrderedDicts with fixed keys, so a TypedDict can't describe them: symbol, label, description
# (str, or None from the docs), and keys (list[str]) when parsed from a hotkey file.
_HotkeyAction: TypeAlias = OrderedDict[str, str | list[str] | None]
# symbol, label, description, helppath (str) and actions.
_HotkeyContext: TypeAlias = OrderedDict[str, str | list[_HotkeyAction]]

# A context of the parsed hotkey files: its subcontexts by name, and the _file, _label, _desc
# and _actions of a context the files declare.
class _HotkeyContextNode(TypedDict, total=False, extra_items="_HotkeyContextNode"):  # type: ignore[call-arg]
    _file: str
    _label: str
    _desc: str
    _actions: list[_HotkeyAction]

class _HotkeyJson(TypedDict):
    contexts: list[_HotkeyContext]

shifted: dict[str, str]
xlate: dict[str, str]
key_expr: re.Pattern[str]

def parse_key(string: str) -> list[str]: ...
def hotkey_to_wiki(hotkey: str) -> list[str]: ...

class HotkeyFileParser:
    ctx_exp: re.Pattern[str]
    key_exp: re.Pattern[str]
    contexts: _HotkeyContextNode
    ctx_by_name: dict[str, _HotkeyContextNode]
    keycount: int
    def __init__(self) -> None: ...
    def parse_file(self, filepath: str) -> None: ...
    def parse_dir(self, dirpath: str) -> None: ...
    def json_obj(self) -> _HotkeyJson: ...
    def json_text(self) -> str: ...
    def print_json(self) -> None: ...

def hotkey_json_from_file(filepath: str) -> _HotkeyJson: ...
def find_actions(pages: WikiPages) -> Generator[tuple[str, str, str | None, str], None, None]: ...
def actions_to_json(
    actions: Iterable[tuple[str, str, str | None, str]],
) -> _HotkeyJson: ...
def hotkey_json_from_docs(pages: WikiPages) -> _HotkeyJson: ...
