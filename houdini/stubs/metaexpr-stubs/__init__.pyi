from collections.abc import Sequence

MAGIC_NUMBER: int
OP_SUM: int
OP_MAX: int
OP_MIN: int

class expr:
    """
       The expr class is used to represent the metaball expression.  Each node
       in the graph has:
        - self.Op:  the operation
        - self.Kids:  children (or operands)
       Each child will either be a sub-expression (i.e. an instance of an expr
       object) or an integer representing a primitive number.
    """
    Op: int
    Kids: list[expr | int]
    def __init__(self, opcode: int) -> None:
        """
           Initialize the expr object with the given opcode (one of OP_SUM,
           OP_MIN, or OP_MAX).  The expr object has a list object named Kids.
           Children should be added to thist list (where children are either
           other instances of expr objects or integers representing primitive
           numbers).
        """
    def serialize(self, opcodes: list[int], id: int) -> int:
        """
            Serialize into an array of opcodes (i.e. the opposite of the build
            function).
        """
    def jsonString(self) -> str:
        """
            Serialize into a JSON string where the form for each node in the
            graph is [opcode,[children]] where children is a list of either
            primitive numbers or other child expressions.
        """

def build(opcodes: Sequence[int]) -> expr | None:
    """
        Given an array of opcodes, build an expr
    """
def serialize(expr: expr, first_id: int) -> list[int]:
    '''
        Given an expression and a "first_id", generate a serialization of the
        expression.  The first_id is usually set to the number of primitives in
        the geometry.
    '''
def test() -> None:
    """ Self-test """
