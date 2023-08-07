# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import Utils.EventModule as EventModule
import PyUtilModule.FarmAPI as FarmAPI
import PyUtilModule.RenderManager.InteractiveRenderDelegateManager as InteractiveRenderDelegateManager
import PyUtilModule.NodeDebugOutput as NodeDebugOutput
import UI4.Util.NodeErrors as NodeErrors
import NodegraphAPI as NodegraphAPI
import Nodes2DAPI as Nodes2DAPI
import Nodes3DAPI as Nodes3DAPI
import UI4.KatanaPrefs.PrefNames as PrefNames
import QT4FormWidgets as QT4FormWidgets
import PyQt5.QtWidgets as QtWidgets
import PyUtilModule.RenderManager.RenderGlobals as RenderGlobals
import PyUtilModule.RenderManager as RenderManager
import RenderingAPI as RenderingAPI
import Nodes3DAPI.ScenegraphMask as ScenegraphMask
import UI4 as UI4
import Utils as Utils
import logging
import typing
from UI4.KatanaPrefs.KatanaPrefsObject import Prefs as Prefs
from UI4.Util.ClientManager import ClientManager as ClientManager
from typing import ClassVar, Set, Tuple

class PreviousRenderCommand:
    callback: ClassVar[None] = ...
    @staticmethod
    def isSet(): ...
    @staticmethod
    def render(): ...
    @staticmethod
    def reset(): ...
    @staticmethod
    def set(function, node: NodegraphAPI.Node, renderMethodKey, renderMethodName, label): ...

class __RenderMenuClientManager(ClientManager):
    def __init__(self, node: NodegraphAPI.Node, callback: typing.Callable) -> None: ...
    def _RenderMenuClientManager__addOrUpdateLocationCallback(self, event, key): ...

def AddRenderItemsToMenu(menu, node: NodegraphAPI.Node, port: NodegraphAPI.Port, log: logging.Logger = ..., addTop: bool = ..., addBottom: bool = ...): ...
def GetFirstLiveRenderMethodNameAndText() -> None | None: ...
def GetFirstPreviewRenderMethodNameAndText() -> None | None: ...
def SetPreviousRenderCommand(renderMethodName: str, node: NodegraphAPI.Node): ...
