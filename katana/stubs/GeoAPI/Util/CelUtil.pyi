# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyFnAttribute as FnAttribute
import PyFnGeolib as FnGeolib
import GeoAPI as GeoAPI
import typing
from PyFnGeolibProducers import GeometryProducer as GeometryProducer
from _typeshed import Incomplete
from typing import Set, Tuple

def CollectPathsFromCELStatement(producerOrClient, celStatement, interruptCallback: typing.Optional[typing.Callable] = ...): ...
