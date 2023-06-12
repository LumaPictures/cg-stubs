# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyFnAttribute as FnAttribute
import PyOpenColorIO as OCIO
import RenderingAPI as RenderingAPI
from _typeshed import Incomplete

def GetDefaultImageInfoDict(outputAttrs, imageInfoDict): ...
def GetDefaultRendererSettingsAttr(outputType, producer: Incomplete | None = ..., producerBaseName: Incomplete | None = ...): ...
def GetRenderOutputs(client, includeMerge: bool = ...): ...