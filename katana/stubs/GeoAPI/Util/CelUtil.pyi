# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyFnAttribute as FnAttribute
import PyFnGeolib as FnGeolib
import GeoAPI as GeoAPI
from PyFnGeolibProducers import GeometryProducer as GeometryProducer
from _typeshed import Incomplete

def CollectPathsFromCELStatement(producerOrClient, celStatement, interruptCallback: Incomplete | None = ...): ...