# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import Nodes3DAPI.AbstractTransform as AT
import ConfigurationAPI_cmodule as Configuration
import PyFnAttribute as FnAttribute
import Nodes3DAPI.Node3D as Node3D
import NodegraphAPI as NodegraphAPI
import PyFnGeolibProducers
import Nodes3DAPI.TransformUtil as TransformUtil
from Nodes3DAPI.AbstractTransform import AbstractTransform
from typing import Set, Tuple

_ExtraHints: dict
_Parameter_XML: str
_resource_path: str

class BlockerCreate(AbstractTransform):
    def __init__(self) -> None: ...
    def _BlockerCreate__addOverride(self, producer: PyFnGeolibProducers.GeometryProducer, coordSysName, attrType, name, value): ...
    def addParameterHints(self, attrName, inputDict): ...
    def getScenegraphLocation(self): ...
    def setInteractiveTransform(self, path, absScale, absRotate, absTranslate, time): ...
