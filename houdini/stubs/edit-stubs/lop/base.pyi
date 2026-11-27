import hou
import pxr.Usd
import pxr.UsdGeom
from collections.abc import Container, Iterable, Mapping, Sequence
from edit import common as common
from edit.base import BaseState as BaseState
from houtypes import ViewerStateMenuActionKwargs
from husd import typeutils as typeutils
from pxr import Usd as Usd

EventRecorder: type[BaseState.EventRecorder]

class LopBaseState(BaseState):
    selstr: str
    physprimpattern: str
    dragprimpath: str | None
    dragprimchildnums: list[int]
    prompt: str | None
    @staticmethod
    def bindMenu(template: hou.ViewerStateTemplate, menu: hou.ViewerStateMenu) -> None: ...
    def __init__(self, state_name: str, scene_viewer: hou.SceneViewer) -> None: ...
    def getUnexpandedNodeSelection(self) -> list[str]: ...
    def getPrimaryDescriptor(self) -> str | None:
        """
            Override of BaseState.getPrimaryDescriptor
        """
    def getSelectionPattern(self) -> list[str]:
        """
            Override of BaseState.getSelectionPattern
        """
    def setSelectionPattern(self, selection_pattern: str) -> None:
        """
            Override of BaseState.setSelectionPattern

            Normalizes the selection so that:
             * nested point-instance paths are trimmed to the top-most
               point instance (Edit can't transform nested point instances), and
             * instance-proxy prims are replaced with their containing instance
               (USD ignores opinions authored on instance proxies).
        """
    def normalizePhysicsPaths(self, paths: Iterable[str]) -> list[str]:
        """
            Override of BaseState.normalizePhysicsPaths.

            Apply the same canonicalization as setSelectionPattern so the
            entries we write into physprimpattern never include nested
            point-instance paths or instance-proxy prims.
        """
    def getPivotFromSelection(self) -> tuple[hou.Vector3, hou.Vector3, hou.Vector3 | None, hou.Vector3 | None]:
        """ Abstract method to get the handle parms for the current selection.
        This is called when the selection changes, or some other aspect of the
        node that might affect the initial handle position changes. If multiple
        prims/instances are selected, just return the pivot to the centroid of
        the selected prims. If one prim is selected, the returned values should
        be populated from the selected item. Returns a tuple of:
        (t, r, s, sh, p, pr) - all values are hou.Vector3.
        """
    modifyingselection: bool
    def setViewportSelection(self, selection: Sequence[str]) -> None:
        """
            Overrides BaseState.setViewportSelection
        """
    def buildSopInstances(self, protogeo: hou.Geometry, stage: pxr.Usd.Stage, pi: pxr.UsdGeom.PointInstancer, instance_ids: Container[int] | None = None) -> None: ...
    def getAncestorSimProxyOwner(self, prim: pxr.Usd.Prim) -> pxr.Usd.Prim | None: ...
    def initSimGeo(self, simgeo: hou.Geometry) -> None:
        """
            Overrides BaseState.initSimGeo
        """
    def getAncestorOfKind(self, prim: pxr.Usd.Prim, kind: str) -> pxr.Usd.Prim | None: ...
    def getInstancePrim(self, prim: pxr.Usd.Prim) -> pxr.Usd.Prim | None: ...
    def locateObject(self, uievent: hou.UIEvent, get_selection_kind: bool = True) -> tuple[float, str]:
        """
            Overrides BaseState.locateObject.
        """
    def getCorrectDescriptor(self, descriptor: str) -> str:
        """
        Override of BaseState.getCorrectDescriptor
        """
    def handleDescriptorDNE(self, simgeo: hou.Geometry, primpath: str) -> str:
        """
        Override of BaseState.handleDescriptorDNE
        """
    def getWorldXformWithoutDelta(self, descriptor: str, deltapointdict: Mapping[str, hou.Point]) -> hou.Matrix4:
        """ Overrides BaseState.getWorldXformWithoutDelta
        """
    @EventRecorder.recordEvent
    def onMenuAction(self, kwargs: ViewerStateMenuActionKwargs) -> None: ...
    def validatePhysicsSelection(self) -> None:
        """
            Overrides BaseState.validatePhysicsSelection
        """
