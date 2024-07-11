# mypy: disable-error-code="misc, override, no-redef"

from typing import ClassVar

class RefinementComplexities:
    """
    An enum-like container of standard complexity settings.
    """

    class _RefinementComplexity:
        """
        Class which represents a level of mesh refinement complexity. Each
        level has a string identifier, a display name, and a float complexity
        value.
        """
        def __init__(self, compId, name, value) -> None: ...
        @property
        def id(self): ...
        @property
        def name(self): ...
        @property
        def value(self): ...
    HIGH: ClassVar[RefinementComplexities._RefinementComplexity] = ...
    LOW: ClassVar[RefinementComplexities._RefinementComplexity] = ...
    MEDIUM: ClassVar[RefinementComplexities._RefinementComplexity] = ...
    VERY_HIGH: ClassVar[RefinementComplexities._RefinementComplexity] = ...
    _ordered: ClassVar[tuple] = ...
    @classmethod
    def fromId(cls, compId):
        """
        Get a complexity from its identifier.
        """
    @classmethod
    def fromName(cls, name):
        """
        Get a complexity from its display name.
        """
    @classmethod
    def next(cls, comp):
        """
        Get the next highest level of complexity. If already at the highest
        level, return it.
        """
    @classmethod
    def ordered(cls):
        """
        Get a tuple of all complexity levels in order.
        """
    @classmethod
    def prev(cls, comp):
        """
        Get the next lowest level of complexity. If already at the lowest
        level, return it.
        """

def AddCmdlineArgs(argsParser, defaultValue: RefinementComplexities._RefinementComplexity = ..., altHelpText: str = ...):
    """
    Adds complexity-related command line arguments to argsParser.

    The resulting 'complexity' argument will be one of the standard
    RefinementComplexities.
    """
