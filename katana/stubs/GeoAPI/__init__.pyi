# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import ConfigurationAPI_cmodule as Configuration
import PyFnGeolibServices as FnGeolibServices
import KatanaResources as KatanaResources
import PluginSystemAPI as PluginSystemAPI
import PyFnGeolibProducers as PyFnGeolibProducers
import PyFnGeolibProducers.RendererOutputUtil as RendererOutputUtil
from . import Lookfiles as Lookfiles, Transform as Transform, Util as Util
from GeoAPI.Transform import ProducerLocalTransform as ProducerLocalTransform, ProducerWorldBounds as ProducerWorldBounds, ProducerWorldTransform as ProducerWorldTransform, UnionBounds as UnionBounds
from PyFnGeolibProducers import GeometryProducer as GeometryProducer
from PyFnGeolibProducers.RendererOutputUtil import __GetCameraInfoUnwrapped as __GetCameraInfoUnwrapped, __GetLocalToScreenMatrixUnwrapped as __GetLocalToScreenMatrixUnwrapped, __GetProjectionMatrixUnwrapped as __GetProjectionMatrixUnwrapped
from typing import Set, Tuple

Geolib3BaseDir: str
secondaryPluginPaths: list
usingFlags: bool

def __GetCameraInfoWrapped(*args): ...
def __GetLocalToScreenMatrixWrapped(): ...
def __GetProjectionMatrixWrapped(): ...
