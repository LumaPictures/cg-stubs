# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyFnAttribute as FnAttribute
import PyFnGeolib as FnGeolib
import FnGeolibProducers as FnGeolibProducers
import PyFnGeolib
import typing
from LookFileBakeAPI.Exceptions import LookFileBakeException as LookFileBakeException
from _typeshed import Incomplete
from typing import Set, Tuple

def CheckRootLocations(rootLocations: typing.Iterable[str], op: PyFnGeolib.GeolibRuntime.Op, rootLocationProducers: Incomplete | None = ...): ...
def FindSharedLodGroupLocations(rootLocations, origProducer) -> dict: ...
def GetLookFileProducerRootId(producer) -> str: ...
def GetProducerFromOp(op: PyFnGeolib.GeolibRuntime.Op) -> FnGeolibProducers.GeometryProducer: ...
