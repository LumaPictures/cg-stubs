# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyFnAttribute as FnAttribute
import KatanaResources as KatanaResources
import NodegraphAPI as NodegraphAPI
import Utils as Utils
import PyXmlIO as XmlIO
from Utils.Decorators import deprecated as deprecated
from _typeshed import Incomplete
from typing import Set, Tuple

def BuildAttrFromParsedEntry(element, refDict: Incomplete | None = ...): ...
def GetGenericAppenderLocations(): ...
def InitGenericAppenders(path: Incomplete | None = ...): ...
def ParseArgsFile(filename): ...
def ParseArgsString(xmlString): ...
def RegisterAppenderNodeTypes(searchPath: Incomplete | None = ...): ...
