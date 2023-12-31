# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import NodegraphAPI as NodegraphAPI
import Utils as Utils
import typing
from PyUtilModule.WorkingSet import WorkingSet as WorkingSet
from _typeshed import Incomplete
from typing import ClassVar, Set, Tuple

class WorkingSetManager:
    LiveRenderUpdatesWorkingSetName: ClassVar[str] = ...
    RenderWorkingSetName: ClassVar[str] = ...
    ViewerVisibilityWorkingSetName: ClassVar[str] = ...
    _SystemWorkingSetNames: ClassVar[tuple] = ...
    _WorkingSetManager__ClearOnSceneChange: ClassVar[set] = ...
    _WorkingSetManager__OnSceneChangeCallbackRegistered: ClassVar[bool] = ...
    _WorkingSetManager__PersistentWorkingSetNames: ClassVar[set] = ...
    _WorkingSetManager__UserOnSceneChangeCallback: ClassVar[None] = ...
    _WorkingSetManager__WorkingSets: ClassVar[dict] = ...
    @classmethod
    def _WorkingSetManager__onSceneLoadOrNewScene(cls, **kwargs): ...
    @classmethod
    def clearOnSceneChangeCallback(cls): ...
    @classmethod
    def clearWorkingSetOnSceneChange(cls, workingSetName: str): ...
    @staticmethod
    def deleteWorkingSet(name: str): ...
    @staticmethod
    def getOrCreateWorkingSet(name: str, sender: Incomplete | None = ...) -> WorkingSet: ...
    @staticmethod
    def getPersistentWorkingSetNames() -> list[str]: ...
    @staticmethod
    def getWorkingSetNames() -> list[str]: ...
    @staticmethod
    def isWorkingSetPersistent(name: str) -> bool: ...
    @classmethod
    def setOnSceneChangeCallback(cls, callback: typing.Callable): ...
    @staticmethod
    def setOpArgs(op: FnGeolibOp, opArgName: str, workingSetName: str, txn: Incomplete | None = ..., opType: Incomplete | None = ..., opArgs: Incomplete | None = ..., updateOnWorkingSetChanges: bool = ...): ...
    @staticmethod
    def setWorkingSetPersistent(name: str, persistent: bool = ...): ...
