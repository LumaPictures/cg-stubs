# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyUtilModule.KatanaFile as KatanaFile
import UI4.KatanaPrefs.PrefNames as PrefNames
import PyQt5.QtCore as QtCore
import PyQt5.QtWidgets as QtWidgets
import Utils as Utils
import typing
from UI4.KatanaPrefs.KatanaPrefsObject import Prefs as Prefs
from typing import Set, Tuple

_AutoSaveIntervalSeconds: int
_LastUndoEventTime: float
_MinimumSecondsBetweenUndoEvents: float
_MinutesBeforeAutoSave: int
_MinutesBeforeAutoSavePrefKey: str
_NumberOfActionsBeforeAutoSave: int
_NumberOfActionsBeforeAutoSavePrefKey: str
_autoSaveTimer: None

def Initialize(): ...
def _AutoSave(): ...
def __on_autosaveTimer_timeout(): ...
def __on_pref_changed(eventType: str | None, eventID: typing.Hashable, prefKey: str, prefValue: object): ...
def __on_undoStack_change(): ...
