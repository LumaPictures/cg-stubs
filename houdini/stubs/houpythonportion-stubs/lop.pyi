import hou

class TraversalDemands:
    Active: int
    Defined: int
    Loaded: int
    NonAbstract: int
    AllowInstanceProxies: int
    Default: int
    NoDemands: int

def stageVariableExpression(self: hou.lop, expr: str) -> str:
    '''
stageVariableExpression(expr) -> str

    This helper method makes it easier to author stage variable
    expressions for use in USD files. Stage variable expressions are
    evaluated by USD at stage composition time. They contain a limited
    set of functions, and allow accessing stage variables which can be
    set using a Configure Layer node. The full capabilities and syntax
    of such stage variable expressions is described in the USD
    documentation, but it is enough to know that the format closely
    resembles Houdini\'s hscript expression language. As such, it can be
    difficult to specify a stage variable expression in a Houdini
    parameter without using complex sequences of escape characters.

    Take for example the case where you want to reference in a texture
    map using the following very simple stage variable expression:

  > `"/project/car/${textureLOD}/decal.exr"`

    Note that the backticks around the expression are required to let
    USD identify this as a stage variable expression. The double quotes
    indicate that the value of the stage variable expression is a simple
    string constant, not using any expression functions. Further suppose
    that your hip file is in /project/car, and you\'d like to use the
    Houdini $HIP variable to express this part of the path. To get this
    stage variable expression into your USD file, the texture path
    parameter on a VOP node would need to be:

  > \\`"$HIP/\\${textureLOD}/decal.exr"\\`

    The escape characters make this string somewhat difficult to read,
    and it may be hard to remember the all the required formatting. The
    stageVariableExpression python function allows you to set the
    parameter to evaluate as the following python expression:

  > hou.lop.stageVariableExpression(\'"`$HIP`/${textureLOD}/decal.exr"\')

    The final expression will be identical but note that there are no
    escape characters, and no need to remember the surrounding back
    ticks. Instead, the back ticks are used to tell the
    stageVariableExpression method which parts of the string should be
    evaluated as hscript expressions.

    The sve method also exists as an alias for this funciton, making the
    resulting python expression much more compact.

'''
def sve(self: hou.lop, expr: str) -> str:
    """
sve(expr) -> str

    This method is simply a shorter alias for the
    stageVariableExpression method. See help on that method for a full
    description of its operation.

"""
