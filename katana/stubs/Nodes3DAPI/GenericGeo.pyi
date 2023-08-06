# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyFnAttribute as FnAttribute
import NodegraphAPI as NodegraphAPI
import PyFnGeolibProducers
from Nodes3DAPI.Node3D import Node3D as Node3D
from typing import Set, Tuple

_ExtraHints: dict
_Parameter_XML: str

class GenericGeo(Node3D):
    def __init__(self) -> None: ...
    def addParameterHints(self, attrName, inputDict): ...

def BuildChild(root, childPath, childType): ...
def _AddChild(producer: PyFnGeolibProducers.GeometryProducer, childName): ...
