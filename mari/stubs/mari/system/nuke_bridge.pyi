from _typeshed import Incomplete

widgets: Incomplete

class CancelledError(RuntimeError): ...

class FromNuke:
    name: Incomplete
    data_dir: Incomplete
    lut: Incomplete
    geo_list: Incomplete
    projector_data: Incomplete
    def __init__(self, data_src) -> None: ...
    def startNewProject(self, channel_desc=..., meta_options=...): ...
    @staticmethod
    def getDefaultProjectorSize(image_data): ...
    def createProjectors(self) -> None: ...

class ProjectionSettingsUI(widgets.QDialog):
    res_x: Incomplete
    res_y: Incomplete
    name: Incomplete
    mapping_scheme: Incomplete
    have_new_geo: bool
    def_proj_index: Incomplete
    def __init__(self, projector_data, geo_list) -> None: ...
    def addOption(self, label, widget, tooltip) -> None: ...
    def addSeparator(self): ...

def errorMsg(message) -> None: ...
def debugMsg(message) -> None: ...
def setDebug(enabled) -> None: ...
def getNukeHostAndPort(): ...
def getMariHostAndPort(): ...
def hostNamesMatch(host1, host2): ...
def setNukeHost(name, port, pid) -> None: ...
def disconnectFromNuke(notify_nuke) -> None: ...
def sendToNuke(nuke_cmd, ignore_failure: bool = ...): ...
def setCurrentMariFor(nuke_pid, is_current, nuke_version: str = ...) -> None: ...
def processResponse(nuke_version) -> None: ...
def getNumericVersion(version_str): ...
def responseTimerExpired() -> None: ...
def checkAndCall(function_call_text) -> None: ...
def exportUVPatchTextures(obj_chan_list, use_socket, output_path: Incomplete | None = ...) -> None: ...
def exportAllChannelsUVPatchTextures(use_socket, output_path: Incomplete | None = ...) -> None: ...
def exportCurrentChannelUVPatchTextures(use_socket, output_path: Incomplete | None = ...) -> None: ...
def exportUnproject(projector, output_path: Incomplete | None = ..., use_socket: bool = ..., unique: bool = ...): ...
def getDataDir(): ...
def loadImages(img_list) -> None: ...
def getCamData(projector): ...
def exportProjectors(export_all: bool = ..., use_socket: bool = ...) -> None: ...
def createProjectorForCurrentView(): ...
def exportCurrentView(use_socket: bool = ...) -> None: ...
def setLUT(lut) -> None: ...
def importNMBFile() -> None: ...
def exportUnprojectCurrent(use_socket, unique: bool = ...) -> None: ...
def launchNuke(): ...
def registerPreferences() -> None: ...
def loadPreferences() -> None: ...
def savePreferences() -> None: ...
def updateAndSavePreferences() -> None: ...
def hostPreferenceChanged() -> None: ...
def portPreferenceChanged() -> None: ...
def pathPreferenceChanged() -> None: ...
def flatLightingPreferenceChanged() -> None: ...
def init(): ...
