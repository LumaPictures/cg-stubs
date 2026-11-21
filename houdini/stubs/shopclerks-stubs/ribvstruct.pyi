# Houdini stubs generated from Houdini 22.0.466

import hou
from . import clerkutil as clerkutil
from collections.abc import Callable as Callable, Collection
from typing import Protocol

from typing import TypeAlias
from typing import TypeAlias
_MemberAndParm: TypeAlias = tuple[str | None, str | None]
_ExprArg: TypeAlias = 'str | Expression'
_ShaderNode: TypeAlias = hou.VopNode | hou.ShopNode
class _VStructParmEvaluator(Protocol):
    def getParmValues(self, parm: hou.ParmTuple, values: str) -> list[tuple[str, str]]: ...
    def getVStructParmValues(self, parm: hou.ParmTuple, values: str) -> list[tuple[str, str]]: ...

class _VStructDataManager:
    """ Manager that parses and caches VStructs data.
    """
    myInputMembersLists: dict[tuple[str, str], list[_MemberAndParm] | None]
    myOutputMembersMaps: dict[tuple[str, str], dict[str | None, str | None] | None]
    myOutputExpressionsMaps: dict[tuple[str, str], dict[str | None, str | None] | None]
    myInputForParmMap: dict[tuple[str, str], tuple[str, str | None] | tuple[None, None]]
    def __init__(self) -> None: ...
    def getVStructInputPairs(self, node: _ShaderNode, input_name: str) -> list[_MemberAndParm] | None:
        """ Returns an array of (shader_parm_name, vstruct_member_name) pairs
            that define connections to be made thru the vstruct mechanism.
        """
    def getVStructOutputMap(self, node: _ShaderNode, output_name: str) -> dict[str | None, str | None] | None:
        """ Returns a map vstruct_member_name -> shader_parameter_name
            as it is defined by the vstruct encoding of the node output tag.
        """
    def getVStructExpressionMap(self, node: _ShaderNode, output_name: str) -> dict[str | None, str | None] | None:
        """ Returns a map from parameter name to an expression string,
            representing a condition under which connections can be made.
        """
    def findVStructInputForParm(self, node: _ShaderNode, parm_name: str) -> tuple[str, str | None] | tuple[None, None]:
        """ Returns a tuple (input_name, member_name) where input_name is
            the vstruct input containing virtual connection for parm_name
            via the vstruct's member_name.
        """

theVStructCache: _VStructDataManager

class Expression:
    """ Class that represents an expression object that can be evaluated.
    """
    myExprString: str
    myExprEvaluator: ExpressionParserAndDispatcher
    def __init__(self, expr_string: str, expr_evaluator: ExpressionParserAndDispatcher) -> None: ...
    def evaluate(self) -> ExpressionValue:
        """ Returns the evaluated expression value.
        """

class ExpressionValue:
    """ Represents result returned by the expression evaluation functions.
    """
    myType: int
    myValue: str | float | None
    NONE: int
    VALUE: int
    CONNECTION: int
    def __init__(self, type: int = ..., value: str | float | None = None) -> None: ...
    def type(self) -> int:
        """ Returns the value's type (kind).
        """
    def value(self) -> str | float | None:
        """ Returns the value's actual Python value.
        """
    def isTrue(self) -> bool:
        """ Returns true if value represents a boolean true value in some form.
        """
    def compare(self, other: ExpressionValue) -> int: ...
    def __add__(self, other: ExpressionValue) -> ExpressionValue: ...
    def __sub__(self, other: ExpressionValue) -> ExpressionValue: ...
    def __mul__(self, other: ExpressionValue) -> ExpressionValue: ...
    def __div__(self, other: ExpressionValue) -> ExpressionValue: ...

class BoolExpressionValue(ExpressionValue):
    """ Convenience class for representing boolean values.
    """
    def __init__(self, bool_val: object) -> None: ...

class ExpressionParserAndDispatcher:
    """ Parses the expression and dispatches it to a registered function.
        The expression is in the format
            function_name:argument1,argument2,argument3

        A subclass must provide a binding from function_name to actual
        function handler by setting myFunctionMap member.

        Nested expressions are allowed by using braces. Eg
            outer_fn:(inner1_fn:arg11,arg12),(inner2:arg21,arg22,arg23)
        this allows logical aggregators
            and:(is_set:foo),(is_set:bar),(is_connected:baz)

        This class implements just parsing and function call dispatching,
        but does not implement the actual evaluation functions, which is
        deferred to the subclasses.
    """
    myFunctionMap: dict[str, Callable[[list[_ExprArg]], ExpressionValue]]
    def __init__(self) -> None: ...
    def evaluateExpression(self, expr_string: str | None) -> ExpressionValue:
        """ Parses expr_string and dispatches a registered handle function.
            The handler should have just one parameter: an argument list.
            Returns whatever the function returns, but by convention
            the action functions should return an ExpressionValue object.
        """

class VStructExpressionEvaluator(ExpressionParserAndDispatcher):
    """ Evaluates vstruct's conditional expressions in Houdini.
    """
    myNode: _ShaderNode
    myFrame: float
    myFunctionMap: dict[str, Callable[[list[_ExprArg]], 'ExpressionValue']]
    def __init__(self, node: _ShaderNode, frame: float) -> None: ...

def processVStruct(shader_node: _ShaderNode, parameter_names: Collection[str], frame: float, parameter_evaluator: _VStructParmEvaluator) -> tuple[list[tuple[str, str]], list[str]]:
    ''' Checks the shader_node its given parameter_names for vstruct definition.

        It returns a tuple:
            - first element is the array of tuples representing the connections
              defined by a detected vstruct. Each tuple consists of a
              formated parameter name (along with type and reference keyword)
              and parameter value string (usually a reference string).
              Eg,  [(\'"reference color diffuseColor"\', 
                     \'/shop/risnet1/pxrlayer1:pxrMaterialOut_diffuseColor\')]
            - second element is the array of parameter names that still need
              the caller still needs to evaluate and format into shader string.
              These are the parameters that are not involved in vstructs,
              and are to be processed in a standard way.
    
        shader_node - the houdini node representing a shader
        parameter_names - array of parameter names that SOHO glue thinks
            should be evaluated and formatted into a shader string.
            These are usually parameters that are not at default value.
        frame - frame number at which parameters should be evaluated
        parameter_evaluator - evaluator object that can format the
            parameter name and its value into a synax acceptable by renderer
    '''
