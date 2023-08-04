# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyFnGeolibServices.ArgsFile as ArgsFile
import RenderingAPI as RenderingAPI
import Utils as Utils
import PyXmlIO as XmlIO
import typing
from typing import Set, Tuple

class Error(Exception): ...

def GetShaderArgsFileDirs(shaderName: str, rendererInfoPluginName: str) -> list[str]: ...
def GetShaderArgsFilePath(shaderName: str, rendererInfoPluginName: str) -> str | None: ...
def WriteArgsFileFromAttrAndHints(filePathOrObject: str | object, parameterNames: typing.Sequence[str], hintDict: dict[str, dict], containerHintDict: dict[str, dict], includePageInfo: bool = ...): ...
