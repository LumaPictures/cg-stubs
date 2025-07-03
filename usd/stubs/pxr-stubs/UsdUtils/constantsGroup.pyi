class _MetaConstantsGroup(type):
    """A meta-class which handles the creation and behavior of ConstantsGroups.
    """
    def __new__(metacls, cls, bases, classdict):
        """Discover constants and create a new ConstantsGroup class."""
    def __setattr__(cls, name, value) -> None:
        """Prevent modification of properties after a group is created."""
    def __delattr__(cls, name) -> None:
        """Prevent deletion of properties after a group is created."""
    def __len__(self) -> int:
        """Get the number of constants in the group."""
    def __contains__(self, value) -> bool:
        """Check if a constant exists in the group."""
    def __iter__(self):
        """Iterate over each constant in the group."""

class ConstantsGroup(metaclass=_MetaConstantsGroup):
    """The base constant group class, intended to be inherited by actual groups
    of constants.
    """
    def __new__(cls, *args, **kwargs) -> None: ...  # type: ignore[misc]
