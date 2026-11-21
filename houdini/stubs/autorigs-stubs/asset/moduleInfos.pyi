from PySide6 import QtGui as QtGui
from autorigs.asset.autoRigsAsset import AutoRigsAsset as AutoRigsAsset
from autorigs.modules.advancedFace.advancedFaceModule import AdvancedFaceModule as AdvancedFaceModule
from autorigs.modules.arm.armModule import ArmModule as ArmModule
from autorigs.modules.base.rootModule import Module as Module
from autorigs.modules.basicFace.basicFaceModule import BasicFaceModule as BasicFaceModule
from autorigs.modules.foot.footModule import FootModule as FootModule
from autorigs.modules.hand.handModule import HandModule as HandModule
from autorigs.modules.head.headModule import HeadModule as HeadModule
from autorigs.modules.leg.legModule import LegModule as LegModule
from autorigs.modules.master.masterModule import MasterModule as MasterModule
from autorigs.modules.quadFoot.quadFootModule import QuadFootModule as QuadFootModule
from autorigs.modules.quadHead.quadHeadModule import QuadHeadModule as QuadHeadModule
from autorigs.modules.quadleg.quadLegModule import QuadLegModule as QuadLegModule
from autorigs.modules.spine.spineModule import SpineModule as SpineModule
from autorigs.modules.tail.tailModule import TailModule as TailModule
from collections.abc import Callable as Callable

ICON_SIZE: int
ARM_ICON: QtGui.QIcon
LEG_ICON: QtGui.QIcon
HAND_ICON: QtGui.QIcon
HEAD_ICON: QtGui.QIcon
QUADRUPED_HEAD_ICON: QtGui.QIcon
FOOT_ICON: QtGui.QIcon
SPINE_ICON: QtGui.QIcon
BLANK_RIG_ICON: QtGui.QIcon
QUADRUPED_ICON: QtGui.QIcon
NULL_ICON: QtGui.QIcon
ADD_ICON: QtGui.QIcon
FILE_ICON: QtGui.QIcon
BIPED_ICON: QtGui.QIcon
QUADRUPED_LEG_ICON: QtGui.QIcon
QUADRUPED_ARM_ICON: QtGui.QIcon
TAIL_ICON: QtGui.QIcon
QUADRUPED_FOOT_ICON: QtGui.QIcon
HIDDEN_DEFAULT_MODULES: list[tuple[QtGui.QIcon, str]]
BIPED_MODULES_DATA: list[tuple[str, str, QtGui.QIcon]]
QUAD_MODULES_DATA: list[tuple[str, str, QtGui.QIcon]]
FACE_MODULES_DATA: list[tuple[str, str, QtGui.QIcon]]
CREATE_MODULE_CLASS: dict[str, Callable[[AutoRigsAsset], Module]]
BUILD_MODULE_ORDER: list[str]
DEFAULT_ADD_PRESETS: tuple[str, str, QtGui.QIcon]
DEFAULT_IMPORT_PRESETS: tuple[str, str, QtGui.QIcon]
DEFAULT_PRESET_BIPED: str
DEFAULT_PRESET_QUADRUPED: str
DEFAULT_PRESETS: list[tuple[str, str, QtGui.QIcon]]
