# Houdini stubs generated from Houdini 22.0.466

import hou
from autorigs.modules.base.autoRigsBaseBuilder import AutoRigsBaseBuilder as AutoRigsBaseBuilder, BuilderGroup as BuilderGroup
from autorigs.modules.basicFace.eye.buildEyeGuide import EyeGuide as EyeGuide
from autorigs.modules.basicFace.eye.eyeGuideModel import EyeGuideModel as EyeGuideModel
from autorigs.utils import buildGuideHelper as buildGuideHelper, captureutils as captureutils, geometryutils as geometryutils
from typing import Literal

from typing import TypeAlias
from typing import TypeAlias
_EyelidName: TypeAlias = Literal['eyelid_center', 'eyelid_inner', 'eyelid_outer']
class AutoRigsEyeBuilder(AutoRigsBaseBuilder[EyeGuide, EyeGuideModel]):
    mainside_grp: BuilderGroup
    mirrorside_grp: BuilderGroup
    master_lookat: hou.ObjNode
    EYELID_CENTER: Literal['eyelid_center']
    EYELID_INNER: Literal['eyelid_inner']
    EYELID_OUTER: Literal['eyelid_outer']
    UPPERLID: str
    LOWERLID: str
    CONTROL_MODE_MENU: list[str]
    NODES: dict[str, tuple[str]]
    INTERFACE: dict[str, tuple[str, str] | tuple[str, str, list[str]]]
    def createGroups(self) -> None: ...
    def createFolderTemplate(self) -> hou.FolderParmTemplate: ...
    def buildRigControls(self) -> None: ...
    def buildEyeRig(self, ismain: bool) -> hou.ObjNode:
        """
        Builds one side of the eye rig
        side: The side of the eye to build
        ismain: Whether the eye to build is the main side
        """
    def captureGeometry(self) -> None: ...
    def postCaptureEyeSetup(self, ismain: bool) -> None: ...
    def createEyeGeo(self, grp: BuilderGroup, geo_path: str, grp_path: str, mirror: bool = False) -> hou.ObjNode:
        """Creates a node reference to the eye geometry"""
    def overrideCaptureRegion(self, capture_guide: hou.ObjNode, eyelid_guide: hou.ObjNode, grp: BuilderGroup) -> hou.ObjNode | None: ...
    def createCaptureRegionSphere(self, grp: BuilderGroup, capture_guide: hou.ObjNode, eyelid_guide: hou.ObjNode) -> hou.ObjNode:
        """Recreates the eye capture sphere based on the capture guide"""
    def createLookAtCHOP(self, node: hou.ObjNode, lookat: hou.ObjNode, lookup: hou.ObjNode, blendvalue: float = 1, blendnode: hou.OpNode | None = None, blendparm: hou.Parm | None = None) -> hou.OpNode: ...
    def createEyelidBones(self, eyelid_position: _EyelidName, eyeroot_guide: hou.ObjNode, parent: hou.ObjNode, ismain: bool) -> tuple[hou.ObjNode, hou.ObjNode]:
        """
        Creates the upperlid and lowerlid bones for the given eyelid_guide
        eyelid_position: the position of the eyelidbones (ex.CENTER, INNER, OUTER)
        eyeroot_guide: the guide for the eyeroot
        """
    def createOrbitParentConstraint(self, lid_root: hou.ObjNode, orbit_root: hou.ObjNode) -> hou.OpNode: ...
    def linkRigInterfaceParms(self) -> None: ...
    def linkEyeInterface(self, ismain: bool) -> None:
        """Link the parm interface of individual eye elements"""
    def setupEyelidDriver(self, position: _EyelidName, grp: BuilderGroup, ismain: bool) -> None:
        """Set up expression for driving the open-close of eyelids"""
    def createEyeOpenCloseParm(self, key: str, grp: BuilderGroup) -> hou.FloatParmTemplate: ...
    def createLookAtTParm(self, parm_id: str, name: str) -> hou.FloatParmTemplate: ...
    def getSideGroup(self, ismain: bool) -> BuilderGroup: ...
    def getSidePrefix(self, side: int) -> str: ...
