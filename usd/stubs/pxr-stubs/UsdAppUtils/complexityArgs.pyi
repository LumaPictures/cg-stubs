from _typeshed import Incomplete

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
        _id: Incomplete
        _name: Incomplete
        _value: Incomplete
        def __init__(self, compId, name, value) -> None: ...
        def __repr__(self) -> str: ...
        @property
        def id(self): ...
        @property
        def name(self): ...
        @property
        def value(self): ...
    LOW: Incomplete
    MEDIUM: Incomplete
    HIGH: Incomplete
    VERY_HIGH: Incomplete
    _ordered: Incomplete
    @classmethod
    def ordered(cls):
        """
        Get a tuple of all complexity levels in order.
        """
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
    def prev(cls, comp):
        """
        Get the next lowest level of complexity. If already at the lowest
        level, return it.
        """

def AddCmdlineArgs(argsParser, defaultValue=..., altHelpText: str = '') -> None:
    """
    Adds complexity-related command line arguments to argsParser.

    The resulting 'complexity' argument will be one of the standard
    RefinementComplexities.
    """
