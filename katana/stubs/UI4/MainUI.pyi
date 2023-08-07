# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import AssetAPI as AssetAPI
import CatalogAPI as CatalogAPI
import ConfigurationAPI_cmodule as Configuration
import KatanaResources as KatanaResources
import PyUtilModule as PyUtilModule
import PyQt5.QtCore as QtCore
import PyQt5.QtWidgets as QtWidgets
import KatanaResources as ResourceFiles
import Utils as Utils
from typing import Set, Tuple

QuitState: object
_InterfaceIsBeingInitialized: bool

def InitializeInterface(options, args): ...
def IsInterfaceBeingInitialized() -> bool: ...
def IterativeInitializeInterface(app, options, splashScreen): ...
def Main(options, args): ...
def VerifyFontPreferences(): ...
