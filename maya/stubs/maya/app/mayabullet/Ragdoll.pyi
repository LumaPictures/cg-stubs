import maya.app.mayabullet.CommandWithOptionVars as CommandWithOptionVars
from _typeshed import Incomplete
from maya.app.mayabullet.RigidBody import eAxisType as eAxisType, eBodyType as eBodyType, eShapeType as eShapeType
from maya.app.mayabullet.RigidBodyConstraint import eConstraintLimitType as eConstraintLimitType, eConstraintType as eConstraintType
from maya.app.mayabullet.Trace import Trace as Trace

RB_XFORM_PREFIX: str
ROTATE_MIN: int
ROTATE_MAX: int
DEFAULT_ANGULAR_DAMPING: float
DEFAULT_ANGULAR_SOFTNESS: float
DEFAULT_ANGULAR_RESTITUTION: float
DEFAULT_CAPSULE_LENGTH: float
DEFAULT_CAPSULE_RADIUS: float
DEFAULT_CAPSULE_MASS: float
DEFAULT_NAME_SEPARATOR: str

def addCapsulesToSkeleton(rootJointName: Incomplete | None = None, capsuleBoneRatio=..., capsuleRadiusRatio=...) -> None: ...

class AddColliders(CommandWithOptionVars.CommandWithOptionVars):
    commandName: str
    commandHelpTag: str
    l10nCommandName: Incomplete
    optionVarCategory: str
    optionVarPrefix: str
    optionVarDefaults: Incomplete
    def __init__(self) -> None: ...
    @staticmethod
    def command(**kwargs) -> None: ...
    def addOptionDialogWidgets(self): ...

def createRagdoll(rootJoint: Incomplete | None = None, angularDamping=..., angularSoftness=..., angularRestitution=..., capsuleBoneRatio=..., capsuleRadiusRatio=..., capsuleMass=..., jointNameSeparator=...) -> None: ...

class CreateRagdoll(CommandWithOptionVars.CommandWithOptionVars):
    commandName: str
    commandHelpTag: str
    l10nCommandName: Incomplete
    optionVarCategory: str
    optionVarPrefix: str
    optionVarDefaults: Incomplete
    def __init__(self) -> None: ...
    @staticmethod
    def command(**kwargs) -> None: ...
    def addOptionDialogWidgets(self): ...
