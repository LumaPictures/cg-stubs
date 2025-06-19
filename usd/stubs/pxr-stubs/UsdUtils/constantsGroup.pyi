# mypy: disable-error-code="misc, override, no-redef"

class ConstantsGroup:
    """The base constant group class, intended to be inherited by actual groups
    of constants.
    """
    @classmethod
    def __init__(cls, *args, **kwargs) -> None: ...

class _MetaConstantsGroup(type):
    """A meta-class which handles the creation and behavior of ConstantsGroups.
    """
    def __init__(self, metacls, cls, bases, classdict) -> None:
        """Discover constants and create a new ConstantsGroup class."""
    def __contains__(self, value) -> bool:
        """Check if a constant exists in the group."""
    @classmethod
    def __delattr__(cls, name):
        """Prevent deletion of properties after a group is created."""
    def __iter__(self):
        """Iterate over each constant in the group."""
    def __len__(self) -> int:
        """Get the number of constants in the group."""
    @classmethod
    def __setattr__(cls, name, value):
        """Prevent modification of properties after a group is created."""
