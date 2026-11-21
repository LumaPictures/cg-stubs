import re
from collections.abc import Generator

from bookish.search import Searchables
from bookish.wiki.wikipages import _WikiBlock
from whoosh import fields

vexcontexts: str

class DoNotIndex(Exception): ...

def find_parms(block: _WikiBlock) -> Generator[_WikiBlock, None, None]: ...

ws_exp: re.Pattern[str]
dir_to_subject: dict[str, str]
houdini_fields: dict[str, fields.FieldType | type[fields.FieldType]]

class HoudiniSearchables(Searchables):
    def schema(self) -> fields.Schema: ...

def usages_for_otl(otlpath: str | None) -> set[str] | tuple[()]: ...
