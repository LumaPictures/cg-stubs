from typing import Literal
import hou
from . import utils as utils
from .. import rtypes as rtypes
from enum import Enum
from typing import Any, Protocol

class _ParmEvaluator(Protocol):
    def __call__(self, parm: hou.Parm, evaluate: bool = ...) -> rtypes.LiteralData | None: ...

def evalGeometry(parm: hou.Parm, evaluate: bool = False) -> str: ...

class ParmValueLiteral:
    """
    Represents a parameter value that has no expression or keyframes.
    """
    eval_chooser: dict[hou.EnumValue[hou.parmTemplateType], _ParmEvaluator]
    def valueAsData(self, parm: hou.Parm, **opts: Any) -> rtypes.LiteralData | None:
        """
        Returns the literal value of the parameter.
        """
    def setFromData(self, parm: hou.Parm, data: rtypes.LiteralData) -> None: ...

class ParmValueExpression:
    """
    Represents a parameter value that has an expression.
    Rather oddly, expressions are set through hou.Keyframe object which can get confusing.
    """
    def valueAsData(self, parm: hou.Parm, **opts: Any) -> rtypes.ExpressionData:
        """
        Builds a dictionary for an expression.
        """
    def setFromData(self, parm: hou.Parm, data: rtypes.ExpressionData) -> None:
        """
        Sets the parameter value to an expression contained in the data
        """

class ParmValueKeyframes:
    """
    Represents a parameter value that has one or more keyframes.
    Rather oddly, expressions are set through hou.Keyframe object which can get confusing.
    In this case keyframes refer to keyed animated values set by the user.
    """
    def valueAsData(self, parm: hou.Parm, **opts: Any) -> rtypes.KeyframesData:
        """
        Builds a dictionary of keyframes or string keyframes
        This is taken out from the asData() C++ implementation for hou.Keyframe.
        """
    def dataToKeyframes(self, data: rtypes.KeyframesData) -> list[hou.Keyframe]:
        """
        Converts the data into a list of houdini keyframe objects.
        """
    def setFromData(self, parm: hou.Parm, data: rtypes.KeyframesData) -> None: ...

class ParmValueTypeEnum(Enum):
    Literal = 'literal'
    Expression = 'expression'
    Keyframes = 'keyframes'

def parmValueAsData(parmtuple: hou.ParmTuple, **opts: Any) -> rtypes.ParmValueData:
    """
    Retrieves the value of a parameter for all of its components.
    """
def setParmValueFromData(parmtuple: hou.ParmTuple, data: rtypes.ParmValueData | hou.Vector2 | hou.Vector3 | hou.Vector4, index: int = 0) -> None:
    """
    Sets the parameter's value for all of its components.
    """
