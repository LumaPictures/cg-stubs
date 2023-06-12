from typing import Any

onUserCreates: Any

def addOnUserCreate(call, args=..., kwargs=..., nodeClass: str = ...) -> None: ...
def removeOnUserCreate(call, args=..., kwargs=..., nodeClass: str = ...) -> None: ...
def onUserCreate() -> None: ...

onCreates: Any

def addOnCreate(call, args=..., kwargs=..., nodeClass: str = ...) -> None: ...
def removeOnCreate(call, args=..., kwargs=..., nodeClass: str = ...) -> None: ...
def onCreate() -> None: ...

onScriptLoads: Any

def addOnScriptLoad(call, args=..., kwargs=..., nodeClass: str = ...) -> None: ...
def removeOnScriptLoad(call, args=..., kwargs=..., nodeClass: str = ...) -> None: ...
def onScriptLoad() -> None: ...

onScriptSaves: Any

def addOnScriptSave(call, args=..., kwargs=..., nodeClass: str = ...) -> None: ...
def removeOnScriptSave(call, args=..., kwargs=..., nodeClass: str = ...) -> None: ...
def onScriptSave() -> None: ...

onScriptCloses: Any

def addOnScriptClose(call, args=..., kwargs=..., nodeClass: str = ...) -> None: ...
def removeOnScriptClose(call, args=..., kwargs=..., nodeClass: str = ...) -> None: ...
def onScriptClose() -> None: ...

onDestroys: Any

def addOnDestroy(call, args=..., kwargs=..., nodeClass: str = ...) -> None: ...
def removeOnDestroy(call, args=..., kwargs=..., nodeClass: str = ...) -> None: ...
def onDestroy() -> None: ...

knobChangeds: Any

def addKnobChanged(call, args=..., kwargs=..., nodeClass: str = ..., node: Any | None = ...) -> None: ...
def removeKnobChanged(call, args=..., kwargs=..., nodeClass: str = ..., node: Any | None = ...) -> None: ...
def knobChanged() -> None: ...

updateUIs: Any

def addUpdateUI(call, args=..., kwargs=..., nodeClass: str = ...) -> None: ...
def removeUpdateUI(call, args=..., kwargs=..., nodeClass: str = ...) -> None: ...
def updateUI() -> None: ...

autolabels: Any

def addAutolabel(call, args=..., kwargs=..., nodeClass: str = ...) -> None: ...
def removeAutolabel(call, args=..., kwargs=..., nodeClass: str = ...) -> None: ...
def autolabel(): ...

beforeRenders: Any

def addBeforeRender(call, args=..., kwargs=..., nodeClass: str = ...) -> None: ...
def removeBeforeRender(call, args=..., kwargs=..., nodeClass: str = ...) -> None: ...
def beforeRender() -> None: ...

beforeFrameRenders: Any

def addBeforeFrameRender(call, args=..., kwargs=..., nodeClass: str = ...) -> None: ...
def removeBeforeFrameRender(call, args=..., kwargs=..., nodeClass: str = ...) -> None: ...
def beforeFrameRender() -> None: ...

afterFrameRenders: Any

def addAfterFrameRender(call, args=..., kwargs=..., nodeClass: str = ...) -> None: ...
def removeAfterFrameRender(call, args=..., kwargs=..., nodeClass: str = ...) -> None: ...
def afterFrameRender() -> None: ...

afterRenders: Any

def addAfterRender(call, args=..., kwargs=..., nodeClass: str = ...) -> None: ...
def removeAfterRender(call, args=..., kwargs=..., nodeClass: str = ...) -> None: ...
def afterRender() -> None: ...

renderProgresses: Any

def addRenderProgress(call, args=..., kwargs=..., nodeClass: str = ...) -> None: ...
def removeRenderProgress(call, args=..., kwargs=..., nodeClass: str = ...) -> None: ...
def renderProgress() -> None: ...
def addBeforeRecording(call, args=..., kwargs=..., nodeClass: str = ...) -> None: ...
def removeBeforeRecording(call, args=..., kwargs=..., nodeClass: str = ...) -> None: ...
def beforeRecording() -> None: ...
def addAfterRecording(call, args=..., kwargs=..., nodeClass: str = ...) -> None: ...
def removeAfterRecording(call, args=..., kwargs=..., nodeClass: str = ...) -> None: ...
def afterRecording() -> None: ...
def addBeforeReplay(call, args=..., kwargs=..., nodeClass: str = ...) -> None: ...
def removeBeforeReplay(call, args=..., kwargs=..., nodeClass: str = ...) -> None: ...
def beforeReplay() -> None: ...
def addAfterReplay(call, args=..., kwargs=..., nodeClass: str = ...) -> None: ...
def removeAfterReplay(call, args=..., kwargs=..., nodeClass: str = ...) -> None: ...
def afterReplay() -> None: ...

beforeBackgroundRenders: Any

def addBeforeBackgroundRender(call, args=..., kwargs=...) -> None: ...
def removeBeforeBackgroundRender(call, args=..., kwargs=...) -> None: ...
def beforeBackgroundRender(context) -> None: ...

afterBackgroundFrameRenders: Any

def addAfterBackgroundFrameRender(call, args=..., kwargs=...) -> None: ...
def removeAfterBackgroundFrameRender(call, args=..., kwargs=...) -> None: ...
def afterBackgroundFrameRender(context) -> None: ...

afterBackgroundRenders: Any

def addAfterBackgroundRender(call, args=..., kwargs=...) -> None: ...
def removeAfterBackgroundRender(call, args=..., kwargs=...) -> None: ...
def afterBackgroundRender(context) -> None: ...

filenameFilters: Any

def addFilenameFilter(call, args=..., kwargs=..., nodeClass: str = ...) -> None: ...
def removeFilenameFilter(call, args=..., kwargs=..., nodeClass: str = ...) -> None: ...
def filenameFilter(filename): ...

validateFilenames: Any

def addValidateFilename(call, args=..., kwargs=..., nodeClass: str = ...) -> None: ...
def removeFilenameValidate(call, args=..., kwargs=..., nodeClass: str = ...) -> None: ...
def validateFilename(filename): ...

autoSaveFilters: Any

def addAutoSaveFilter(filter) -> None: ...
def removeAutoSaveFilter(filter) -> None: ...
def autoSaveFilter(filename): ...

autoSaveRestoreFilters: Any

def addAutoSaveRestoreFilter(filter) -> None: ...
def removeAutoSaveRestoreFilter(filter) -> None: ...
def autoSaveRestoreFilter(filename): ...

autoSaveDeleteFilters: Any

def addAutoSaveDeleteFilter(filter) -> None: ...
def removeAutoSaveDeleteFilter(filter) -> None: ...
def autoSaveDeleteFilter(filename): ...
