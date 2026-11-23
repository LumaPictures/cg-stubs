import hou

class TraversalDemands:
    Active: int
    Defined: int
    Loaded: int
    NonAbstract: int
    AllowInstanceProxies: int
    Default: int
    NoDemands: int

def stageVariableExpression(self: hou.lop, expr: str) -> str: ...
def sve(self: hou.lop, expr: str) -> str: ...
