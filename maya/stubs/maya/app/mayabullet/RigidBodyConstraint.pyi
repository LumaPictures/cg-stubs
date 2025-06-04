from . import CommandWithOptionVars as CommandWithOptionVars
from _typeshed import Incomplete
from maya.app.mayabullet import logger as logger
from maya.app.mayabullet.Trace import Trace as Trace

class eConstraintType:
    kRBConstraintPoint: int
    kRBConstraintHinge: int
    kRBConstraintSlider: int
    kRBConstraintConeTwist: int
    kRBConstraintSixDOF: int
    kRBConstraintSixDOF2: int
    kRBConstraintHinge2: int

class eConstraintLimitType:
    kRBConstraintLimitFree: int
    kRBConstraintLimitLocked: int
    kRBConstraintLimitLimited: int

class eReferenceFrame:
    kRigidBodyA: int
    kRigidBodyB: int

dictConstraintAttributes: Incomplete

class CreateRigidBodyConstraint(CommandWithOptionVars.CommandWithOptionVars):
    commandName: str
    commandHelpTag: str
    l10nCommandName: Incomplete
    optionVarCategory: str
    optionVarPrefix: str
    optionVarDefaults: Incomplete
    def __init__(self) -> None: ...
    def addOptionDialogWidgets(self): ...
    @staticmethod
    def command(rigidBodyA: Incomplete | None = None, rigidBodyB: Incomplete | None = None, parent: Incomplete | None = None, constraintType: Incomplete | None = None, useReferenceFrame: Incomplete | None = None, linearDamping: Incomplete | None = None, linearSoftness: Incomplete | None = None, linearRestitution: Incomplete | None = None, angularDamping: Incomplete | None = None, angularSoftness: Incomplete | None = None, angularRestitution: Incomplete | None = None, linearConstraintX: Incomplete | None = None, linearConstraintY: Incomplete | None = None, linearConstraintZ: Incomplete | None = None, linearConstraintMin: Incomplete | None = None, linearConstraintMax: Incomplete | None = None, angularConstraintX: Incomplete | None = None, angularConstraintY: Incomplete | None = None, angularConstraintZ: Incomplete | None = None, angularConstraintMin: Incomplete | None = None, angularConstraintMax: Incomplete | None = None, linearLimitSoftness: Incomplete | None = None, linearLimitBias: Incomplete | None = None, linearLimitRelaxation: Incomplete | None = None, angularLimitSoftness: Incomplete | None = None, angularLimitBias: Incomplete | None = None, angularLimitRelaxation: Incomplete | None = None, linearMotorEnabled: Incomplete | None = None, linearMotorTargetSpeed: Incomplete | None = None, linearMotorMaxForce: Incomplete | None = None, angularMotorEnabled: Incomplete | None = None, angularMotorTargetSpeed: Incomplete | None = None, angularMotorMaxForce: Incomplete | None = None, linearSpringEnabledX: Incomplete | None = None, linearSpringEnabledY: Incomplete | None = None, linearSpringEnabledZ: Incomplete | None = None, linearSpringStiffness: Incomplete | None = None, linearSpringDamping: Incomplete | None = None, angularSpringEnabledX: Incomplete | None = None, angularSpringEnabledY: Incomplete | None = None, angularSpringEnabledZ: Incomplete | None = None, angularSpringStiffness: Incomplete | None = None, angularSpringDamping: Incomplete | None = None, breakable: Incomplete | None = None, breakingThreshold: Incomplete | None = None): ...
    def linearMotorEnabledCB(self, enable) -> None: ...
    def angularMotorEnabledCB(self, enable) -> None: ...
