# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import ConfigurationAPI_cmodule as Configuration
import PyUtilModule.Documentation as Documentation
import KatanaResources as KatanaResources
import MachineInfo as MachineInfo
import NodegraphAPI as NodegraphAPI
import Nodes3DAPI as Nodes3DAPI
import PyUtilModule as PyUtilModule
import PyQt5.QtGui as QtGui
import PyUtilModule.RenderManager.RenderGlobals as RenderGlobals
import PyUtilModule.RenderManager as RenderManager
from . import KatanaPrefsObject as KatanaPrefsObject, PrefNames as PrefNames
from UI4.KatanaPrefs.KatanaPrefsObject import Prefs as Prefs
from typing import Set, Tuple

class __AvailableFonts:
    def __init__(self, codeFontsOnly: bool = ...) -> None: ...
    def __iter__(self) -> __AvailableFonts: ...
    def __next__(self) -> tuple: ...

def GetAvailableFontFamilies(codeFontsOnly: bool = ...) -> list[str]: ...
