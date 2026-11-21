# Houdini stubs generated from Houdini 22.0.466

from .common import Category as Category, ResultItem as ResultItem
from .expression import Expression as Expression
from .help import Help as Help
from .hotkeys import Hotkeys as Hotkeys
from .panetabs import PaneTabs as PaneTabs
from .parms import Parms as Parms
from .paths import Nodes as Nodes
from .preferences import Preferences as Preferences
from .radialmenus import RadialMenus as RadialMenus
from .solaris import Solaris as Solaris
from .tools import Tools as Tools
from .viewport_settings import DisplayOptions as DisplayOptions
from collections.abc import Collection

class RootCategories(Category):
    '''
    A list of categories shown when the dash box is called with no
    category specified. In other words, it shows available searches.

    This essentially acts as "tabs" to switch between different
    categories. Selecting an item will limit the search to one category.

    Matching is NOT fuzzy. As soon as the user starts typing actual
    search text, these default categories should disappear.
    '''
    class Item(ResultItem):
        def __init__(self, category: type[Category]) -> None: ...
        def label(self) -> str: ...
        def hasNext(self) -> bool: ...
        def next(self) -> list[Category]: ...
        def hasAction(self) -> bool: ...
    def __init__(self, categories: Collection[type[Category]], label: str) -> None: ...
    def label(self) -> str: ...
    def filter(self, text: str) -> tuple[float, list['RootCategories.Item']]: ...

def defaultCategories() -> list[Category]: ...
