# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyFnGeolibProducers as FnGeolibProducers
import NodegraphAPI as NodegraphAPI
import NodegraphAPI_cmodule
import Utils as Utils
import re
from _typeshed import Incomplete
from typing import ClassVar, Set, Tuple

REFMTL_ROOT: str
_DefaultShapeAttrs: tuple
_ExtraHints: dict
_Parameter_XML: str

class MaterialStackNode(NodegraphAPI_cmodule.PythonGroupNode):
    _MaterialStackNode__nodeReferenceRegex: ClassVar[re.Pattern] = ...
    def __init__(self) -> None: ...
    def _MaterialStackNode__conformAdoptedMaterials(self, parent, childList): ...
    def _MaterialStackNode__createMergeNode(self): ...
    def _MaterialStackNode__extractOrderedChildNodes(self, childList, resultList: Incomplete | None = ...): ...
    def _MaterialStackNode__findMaterialNodesInList(self, nodeList, resultList: Incomplete | None = ..., exceptionType: type[RuntimeError] = ...): ...
    def _MaterialStackNode__findReferencedMaterialNode(self, path): ...
    def _MaterialStackNode__getAppendedMergeInputPort(self, mergeNode: Incomplete | None = ...): ...
    def _MaterialStackNode__getMaterialParent(self, node): ...
    def _MaterialStackNode__getMergeInputIndexForNode(self, node, mergeNode: Incomplete | None = ...): ...
    def _MaterialStackNode__getMergeNode(self, create: bool = ...): ...
    def _MaterialStackNode__getReferenceGroupNode(self, create: bool = ...): ...
    def _MaterialStackNode__getReferenceGroupPruneNode(self): ...
    def _MaterialStackNode__getReferenceGroupTerminalPort(self): ...
    def _MaterialStackNode__layoutMaterialList(self, childList, state, depth: int = ...): ...
    def _MaterialStackNode__setReferencedMaterialInclusionSet(self, paths): ...
    def _MaterialStackNode__walkMaterialTree(self, node, materials): ...
    def addChildMaterial(self, parentNode): ...
    def addGeometryMaterial(self): ...
    def addLightMaterial(self): ...
    def addLookFileInReference(self, spref): ...
    def addLookFileMaterial(self): ...
    def addMaterial(self): ...
    def addParameterHints(self, attrName, inputDict): ...
    def addReferencedMaterial(self, path): ...
    def adoptMaterialNodes(self, nodeList, index: int = ..., exceptionType: type[RuntimeError] = ...): ...
    def deleteLookFileInReference(self, index): ...
    def deleteMaterialNode(self, node): ...
    def duplicateMaterial(self, node): ...
    def getAllChildMaterials(self, node): ...
    def getAllMaterialNodes(self): ...
    def getDefaultNodeShapeAttrs(self): ...
    def getLookFileInReferenceNodes(self): ...
    def getMaterialHierarchy(self, startAtNodeName: Incomplete | None = ...): ...
    def getReferenceGroupNode(self, create: bool = ...): ...
    def getReferenceGroupTerminalPort(self): ...
    def getReferenceMaterialDict(self): ...
    def getReferencedMaterialInclusionSet(self): ...
    def getReferencedMaterialNodeForPath(self, path): ...
    def layoutInternalGraph(self): ...
    def reorderLookFileInReference(self, fromIndex, toIndex): ...
    def reorderNode(self, node, parent, index): ...

def MiniPaste(element, parent): ...
