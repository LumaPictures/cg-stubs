# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyFnAttribute as FnAttribute
import PyOpenColorIO as OCIO
import PyFnGeolibProducers
import RenderingAPI as RenderingAPI
import typing
from _typeshed import Incomplete
from typing import Set, Tuple

def GetDefaultRendererSettingsAttr(outputType, producer: typing.Optional[PyFnGeolibProducers.GeometryProducer] = ..., producerBaseName: Incomplete | None = ...): ...
def GetRenderOutputs(client, includeMerge: bool = ...): ...
