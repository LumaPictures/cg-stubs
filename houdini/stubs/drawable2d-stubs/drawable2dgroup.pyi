import hou
from . import utils as utils
from collections.abc import Callable as Callable
from typing import Any
from typing_extensions import TypeIs

from typing import TypeAlias
from typing import TypeAlias
_Item: TypeAlias = 'hou.Drawable2D | Drawable2DGroup'
class Drawable2DGroup:
    """ Generic container class for organizing `Drawable2D` objects 
        and nested `Drawable2DGroup` instances. 

        Supports hierarchical grouping, transform propagation, 
        visibility management, and recursive search operations by 
        name.
    """
    @staticmethod
    def _isGroup(item: object) -> TypeIs['Drawable2DGroup']:
        """ Return True if the given item is a `Drawable2DGroup`.
            This is determined by checking whether the item has a 
            `group()` method.
        """
    def __init__(self, name: str, items: list[_Item], shared: bool = False) -> None:
        """ Initialize the group with a name and a list of items.

            Each item must be either a `Drawable2D` or another 
            `Drawable2DGroup`. Items are automatically marked as 
            enabled and assigned this group as their parent.
        """
    def enable(self, name: str | None = None, value: bool = True, sync_visibility: bool = False) -> None:
        """
        Enable or disable a group or item by name.

        If name is None or matches this group, enable/disable the 
        group and all children (unless the group is marked as 
        _shared). Shared groups are skipped when disabling.

        Args:
            name (str or None): The name of the group/item to enable, 
                or None for all.
            value (bool): True to enable, False to disable.
            sync_visibility (bool): If True, also show/hide the 
                item alongside the enable/disable.
        """
    def isEnabled(self, name: str | None = None) -> bool:
        """ Check if the group or a specific item by name is 
            enabled.

        - If name is None or matches this group: return True if 
          any child is enabled.
        - If name matches a child item: return its enabled state.
        """
    def freeze(self, value: bool) -> None: ...
    def items(self) -> list[_Item]: ...
    def group(self) -> Drawable2DGroup | None:
        """ Return the parent group of this group, if any.
        """
    def groupByName(self, name: str) -> Drawable2DGroup | None:
        """ Recursively search for a group with the given name.
            Searches only among groups (not leaf drawables) and 
            returns the first match found.
        """
    def containingGroup(self, name: str) -> Drawable2DGroup | None:
        """ Recursively search for the group that contains the 
            drawable or group with the given name.
        """
    def topGroup(self) -> Drawable2DGroup:
        """ Return the top-level parent group in the hierarchy.
        """
    def addItem(self, item: _Item, shared: bool = False) -> None:
        """ 
        Add an existing Drawable2D or Drawable2DGroup to this group.

        Args:
            item: The Drawable2D or Drawable2DGroup to add.
            shared (bool): If True and the item is a group, it will not 
                           be disabled when this group is disabled.
        """
    def addGroup(self, name: str, items: list[_Item] | None = None, shared: bool = False) -> Drawable2DGroup:
        """ Create a new sub-group with the given name and items, 
            and add it to this group.

            name: Name of the new group.
            items: 
                A list of Drawable2D or Drawable2DGroup instances 
                to add.
            
            Returns The newly created group (Drawable2DGroup).
        """
    def addToGroup(self, group_name: str, *items: _Item) -> bool:
        """Add one or more items to an existing group by name.

            group_name (str): The name of the group to add items to.
            *items: One or more Drawable2D or Drawable2DGroup 
                    instances to add.

            Returns True if the group was found and items were 
            added, False otherwise.
        """
    def clearGroup(self, group_name: str) -> bool:
        """ Remove items from a group.
        """
    def setTransform(self, t: hou.Matrix4) -> None:
        """ Set the transformation matrix for the group and apply 
            it to all child items.
        """
    def setParams(self, params: dict[str, Any]) -> None:
        """ Set the params on all group items.
        """
    def params(self) -> dict[str, Any]:
        """ Return the params stored in this group
        """
    def preMulTransform(self, t: hou.Matrix4) -> None:
        """ Apply a pre-multiplied transformation to each item.
        """
    def postMulTransform(self, t: hou.Matrix4) -> None:
        """ Apply a post-multiplied transformation to each item.
        """
    def transform(self) -> hou.Matrix4:
        """ Return the current transform matrix of the group.
        """
    def drawTransform(self) -> hou.Matrix4:
        """ Return the current post transform matrix of the group.
        """
    def postTransform(self) -> hou.Matrix4: ...
    def layerTransform(self) -> hou.Matrix4: ...
    def postScale(self) -> hou.Vector3: ...
    def draw(self, draw_handle: hou.Handle) -> None:
        """ Draw all enabled items in the group.
        """
    def show(self, value: bool) -> None:
        """ 
        Show or hide all enabled items in the group, including 
        nested groups.

        - Recursively call show(value) on nested Drawable2DGroups.
        - Show individual drawables only if they are enabled.
        - Force-hide disabled drawables regardless of the 'value' 
          argument.
        """
    def isVisible(self) -> bool: ...
    def solo(self) -> None:
        """ Show only this group, hiding all sibling groups within 
            the top-level parent group.
        """
    def find(self, name: str) -> _Item | None:
        """ 
        Recursively find a drawable or group by name.

        Returns:
            - The matching `Drawable2D` or `Drawable2DGroup` object.
            - None if no match is found.
        """
    def name(self) -> str:
        """ Return the name of the group.
        """
    def log(self, full: bool = False, max_items: int = 10) -> str:
        """ Return a hierarchy layout describing the group content.

            full:
                If True, print all items.
                If False, print only up to max_items items per group
                when a group has more than max_items items.

            max_items:
                Maximum number of items to print per group when full=False.
        """
    def forEach(self, fn: Callable[[_Item], object], include_groups: bool = True, max_items: int | None = 10) -> None:
        """ 
        Recursively iterate over all items in this group.

        Args:
            fn (callable):
                Function called with each item as argument.
            include_groups (bool):
                If True, also call fn on nested Drawable2DGroup instances.
            max_items (int | None):
                If set, do not recurse into sub-groups with more than
                max_items direct children.
        """
