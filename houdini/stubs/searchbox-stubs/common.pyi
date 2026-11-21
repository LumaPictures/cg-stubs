# Houdini stubs generated from Houdini 22.0.466

import collections.abc
import hou
import typing
from PySide6 import QtGui as QtGui
from collections.abc import Callable as Callable, Iterable, Sequence

from typing import TypeVar
from typing import TypeVar
_K = TypeVar('_K')
_V = TypeVar('_V')
class Category:
    '''
    Search category that generates list of ResultItem

    To specify names/aliases used in the default catogory list,
    use class attributes (optional):

    - cls.NAME:    String.          Example: "Preferences"
    - cls.ALIASES: List of aliases, Example: ["prefs", "settings"]

    See: categories.defaultCategories()
    '''
    @classmethod
    def isCategory(cls) -> bool: ...
    @classmethod
    def isDefault(cls) -> bool:
        """
        Whether this category is enabled by default. Slow search should
        return False, so that it's not used in categories.defaultCategories().
        """
    def label(self) -> str: ...
    def secondaryLabel(self) -> str | None: ...
    def score(self) -> float: ...
    def allowBlank(self, allow: bool) -> None: ...
    def acceptText(self, text: str) -> bool:
        """
        Returns True if search text is accepted and should be processed
        by this category. By default, text must be non blank. If the category
        shows default suggestions (blank without typing), True should be
        returned unconditionally. Alternatively, call allowBlank(True).
        """
    def filter(self, text: str) -> tuple[float, Sequence['ResultItem']]:
        """
        Returns a tuple of (score, [item]) according to the specified
        search text, where score is the rating in [0, 1.0] range. The score
        of the first item is typically used.
        This method may be called on a non-UI thread, so call UI related
        stuff in __init__() instead if necessary.
        """
    def hasNext(self) -> bool: ...

class ResultItem:
    """
    Action items or section label
    """
    @classmethod
    def isCategory(cls) -> bool: ...
    def label(self) -> str:
        '''
        The "main" string representing this item in the results list.
        '''
    def secondaryLabel(self) -> str | None:
        '''
        If this is not None, it is displayed next to the "main" label in the
        results list as a bit of extra information.
        '''
    def icon(self) -> QtGui.QIcon | None:
        """
        A QIcon instance to display as the decoration for this item in the
        results list, or None if the item has no icon.
        """
    def feedback(self) -> str | None:
        """
        This string replaces the content of the search box when the user
        highlights this item in the result list. The default implementation just
        returns the label.
        """
    def hasNext(self) -> bool:
        '''
        Should return True if this item will push a "next" context when the user
        presses Tab, or False if it will not.
        '''
    def next(self) -> list[Category]:
        """
        When the user presses Tab on this item, push a new context using this
        list of Category provider objects.
        """
    def nextPrompt(self) -> str | None:
        """
        When the user presses Tab on this item, display this string in a header
        above the search box for the new context. This is useful for displaying
        a helpful prompt. The default implementation returns the same value as
        feedback().
        """
    def nextPlaceholder(self) -> str:
        '''
        When the user presses Tab on this item, display this as the "placeholder
        text" in the search box for the new context. This is useful for telling
        the user what kind of thing they can type. The default implementation
        returns "Search".
        '''
    def nextSearch(self) -> str:
        '''
        When the user presses Tab on this item, fill this in as the "search
        text" in the new context. This may be useful for re-running a search in
        the new context. The default implementation returns an empty string.
        '''
    def completion(self) -> str | None:
        '''
        The text that will "complete" the search text for this item, when this
        item is selected. If the user presses Right Arrow, this text is added
        to the end of the search text. Compare with displayCompletion().
        '''
    def displayCompletion(self) -> str | None:
        """
        The text displayed after the search text, when this item is selected.
        If the user presses Right Arrow, the search box adds the text returned
        by completion(), not this text. This text is for display only.
        """
    def hasAction(self) -> bool:
        """
        Should return True when this item has an action (click/enter). Otherwise,
        this item may only have the next() flow, and selecting should fall back
        to nexting.
        """
    def action(self) -> str | None:
        """
        Default action that is called when the item is clicked/entered.
        """

@typing.overload
def findMatches(text: str, samples: collections.abc.Mapping[_K, str], key: None = ...) -> list[tuple[float, _K]]: ...  # type: ignore[overload-overlap]
@typing.overload
def findMatches(text: str, samples: collections.abc.Mapping[_K, _V], key: Callable[[_V], str]) -> list[tuple[float, _K]]: ...  # type: ignore[overload-overlap]
@typing.overload
def findMatches(text: str, samples: Iterable[str], key: None = ...) -> list[tuple[float, int]]: ...
@typing.overload
def findMatches(text: str, samples: Iterable[_V], key: Callable[[_V], str]) -> list[tuple[float, int]]: ...
@typing.overload
def findMatches2(text: str, samples: collections.abc.Mapping[_K, _V], key1: Callable[[_V], str], key2: Callable[[_V], str]) -> list[tuple[float, _K]]: ...  # type: ignore[overload-overlap]
@typing.overload
def findMatches2(text: str, samples: Iterable[_V], key1: Callable[[_V], str], key2: Callable[[_V], str]) -> list[tuple[float, int]]: ...
def findPaneTab(pt_type: hou.EnumValue[hou.paneTabType], cond: Callable[[hou.PaneTab], object] = ...) -> hou.PaneTab | None: ...
def findParmDialog() -> hou.ParameterEditor | hou.NetworkEditor | None:
    '''
    Find the "current" parm dialog (pane tab), which includes
    network editors with parm dialog shown. Pane tab under
    cursor is always preferred.
    '''
def findPathBasedPaneTab() -> hou.PathBasedPaneTab | None:
    '''
    Find the "current" path-based pane tab. Network Editor is
    preferred
    '''
