# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import RenderingAPI as RenderingAPI
from RenderingAPI.RenderPlugins import GetRenderMethodsForRenderer as GetRenderMethodsForRenderer
from typing import Set, Tuple

class RenderingException(Exception):
    def __init__(self, sequenceID, errorCode, nodeName, message): ...

class UnsupportedRenderMethodNameException(Exception):
    def __init__(self, rendererName, renderMethodName): ...
