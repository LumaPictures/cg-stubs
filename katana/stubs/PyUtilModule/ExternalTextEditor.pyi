# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import ConfigurationAPI_cmodule as Configuration
import Utils as Utils
from Utils.Decorators import deprecated as deprecated

def GetExternalEditor(): ...
def GetExternalEditorName(): ...
def GetKatanaTempfile(prefix, suffix, maxInt: int = ...): ...
def OpenFileInExternalEditor(filename): ...