# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyFnAttribute as FnAttribute
import PyFnGeolib as FnGeolib
import PyFnGeolibProducers as FnGeolibProducers
import PyUtilModule.LiveRenderAPI as LiveRenderAPI
import NodegraphAPI as NodegraphAPI
import Nodes3DAPI as Nodes3DAPI
import PyFnAttribute
import Utils as Utils
from typing import Set, Tuple

class ManipulatorBridge:
    def __init__(self) -> None: ...
    def _ManipulatorBridge__attrToDict(self, attrName, attr): ...
    def _ManipulatorBridge__createManipulatorPolicy(self, locationPath, attributes): ...
    def _ManipulatorBridge__getAttributeEditorAttr(self, locationPath: str) -> PyFnAttribute.GroupAttribute | None: ...
    def _ManipulatorBridge__getRootProducer(self): ...
    def _ManipulatorBridge__on_LiveAttributePolicyManager_flush(self, *args, **kwargs): ...
    def _ManipulatorBridge__requestManipulationCommitId(self): ...
    def _ManipulatorBridge__setManipulationCommitId(self, commitId): ...
    def cleanupLiveAttributes(self, locationPath: str): ...
    def closeManipulationGroup(self, locationPath): ...
    def getManipulationCommitId(self): ...
    @staticmethod
    def isNodeEditable(nodeName: str) -> bool: ...
    def openManipulationGroup(self, locationPath): ...
    def setValue(self, locationPath, attrName, attrValue, isFinal): ...
    def updateOp(self, opId: int): ...
    def __del__(self) -> None: ...
