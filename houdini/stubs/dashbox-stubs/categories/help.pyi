import datetime
import hou
from ..common import BLANK_ICON as BLANK_ICON, Category as Category, Hit as Hit, SearchSpec as SearchSpec, Sug as Sug, Tag as Tag
from ..ui import DashWindow as DashWindow
from typing import NotRequired, TypedDict
from whoosh import query as query, sorting as sorting

from typing import TypeAlias
from typing import TypeAlias
_InstantDoc: TypeAlias = None | bool | int | float | str | list['_InstantDoc'] | tuple['_InstantDoc', ...] | dict[str, '_InstantDoc']
class _StoredHelpDoc(TypedDict):
    path: str
    title: NotRequired[str]
    type: NotRequired[str]
    tags: NotRequired[str]
    modified: NotRequired[datetime.datetime]
    subject: NotRequired[str]
    summary: NotRequired[str]
    icon: NotRequired[str]
    container: NotRequired[bool]
    instant_doc: NotRequired[_InstantDoc]
    status: NotRequired[str]
    superclass: NotRequired[str]
    replaces: NotRequired[str]
    context: NotRequired[str]
    examplefile: NotRequired[str]
    examplefor: NotRequired[str]
    group: NotRequired[str]

HELP_TAG_NAME: str
HELP_TAG: Tag
FIELD_BOOSTS: dict[str, float]
DOCS_BY_PATH: dict[str, _StoredHelpDoc]
HELP_ICON: hou.qt.Icon

def buildDocsByPath() -> dict[str, _StoredHelpDoc]: ...
def getDocsByPath() -> dict[str, _StoredHelpDoc]: ...

class HelpCategory(Category):
    limit: int
    def __init__(self) -> None: ...
    def knownTags(self) -> list[Tag]: ...
    def label(self) -> str: ...
    def icon(self) -> hou.qt.Icon: ...
    def suggestedInputs(self) -> list[str]: ...
    def initialSuggestions(self) -> list[Sug | HelpHit]: ...
    def hits(self, search: SearchSpec) -> tuple[float, list[Hit]]: ...

class HelpHit(Hit):
    score: float
    def __init__(self, path: str, title: str, helpcat: str, iconname: str | None) -> None: ...
    def label(self) -> str: ...
    def secondaryLabel(self) -> str: ...
    def icon(self) -> hou.qt.Icon: ...
    def action(self, dashbox: DashWindow) -> None: ...
