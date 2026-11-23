import re
from bookish.search import Searchables, default_fields as default_fields
from bookish.wiki.wikipages import _WikiBlock
from collections.abc import Generator
from whoosh import fields

vexcontexts: str

class DoNotIndex(Exception): ...

def find_parms(block: _WikiBlock) -> Generator[_WikiBlock, None, None]:
    """
    Recursively finds dt blocks inside containers (but doesn't recurse inside
    the dt blocks). This is necessary because for bad historical reasons nodes
    docs don't mark parameters as items like they should.
    """

ws_exp: re.Pattern[str]
dir_to_subject: dict[str, str]
houdini_fields: dict[str, fields.FieldType | type[fields.FieldType]]

class HoudiniSearchables(Searchables):
    def schema(self) -> fields.Schema: ...

def usages_for_otl(otlpath: str | None) -> set[str] | tuple[()]: ...
