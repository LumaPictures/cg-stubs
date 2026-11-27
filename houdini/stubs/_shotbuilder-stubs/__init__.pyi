from collections.abc import Callable
import collections.abc
from typing import overload

class HprUri:
    @overload
    def __init__(self, arg: str) -> None:
        """__init__(self, arg: str, /) -> None
        __init__(self, arg: _shotbuilder.HprUri) -> None"""
    @overload
    def __init__(self, arg: HprUri) -> None:
        """__init__(self, arg: str, /) -> None
        __init__(self, arg: _shotbuilder.HprUri) -> None"""
    def baseUri(self) -> str:
        """baseUri(self) -> str"""
    def extension(self) -> str:
        """extension(self) -> str"""
    def isValid(self) -> bool:
        """isValid(self) -> bool"""
    def latestVersion(self) -> int:
        """latestVersion(self) -> int"""
    def name(self) -> str:
        """name(self) -> str"""
    def nextVersion(self) -> int:
        """nextVersion(self) -> int"""
    def path(self) -> str:
        """path(self) -> str"""
    def resolvedPath(self, newAsset: bool = ...) -> str:
        """resolvedPath(self, newAsset: bool = False) -> str"""
    def setVersion(self, arg: int | str) -> None:
        """setVersion(self, arg: int, /) -> None"""
    def uri(self) -> str:
        """uri(self) -> str"""
    def version(self) -> str:
        """version(self) -> str"""
    def versions(self) -> list[int]:
        """versions(self) -> list[int]"""
    def __hash__(self) -> int:
        """__hash__(self) -> int"""

class ProjectConfig:
    @overload
    def __init__(self) -> None:
        """__init__(self) -> None
        __init__(self, arg: str, /) -> None"""
    @overload
    def __init__(self, arg: str) -> None:
        """__init__(self) -> None
        __init__(self, arg: str, /) -> None"""
    @staticmethod
    def addProjectChangedCallback(arg: Callable[[int], object]) -> int:
        """addProjectChangedCallback(arg: collections.abc.Callable[[int], None], /) -> int"""
    def defaultFrameData(self) -> list[float]:
        """defaultFrameData(self) -> list[float]"""
    def extensionForType(self, arg: str) -> str:
        """extensionForType(self, arg: str, /) -> str"""
    def iconForSubLayer(self, arg0: str, arg1: str) -> str:
        """iconForSubLayer(self, arg0: str, arg1: str, /) -> str"""
    def iconForType(self, arg: str) -> str:
        """iconForType(self, arg: str, /) -> str"""
    def isValid(self) -> bool:
        """isValid(self) -> bool"""
    def isValidUnit(self, arg0: str, arg1: str) -> bool:
        """isValidUnit(self, arg0: str, arg1: str, /) -> bool"""
    def isValidUnitType(self, arg: str) -> bool:
        """isValidUnitType(self, arg: str, /) -> bool"""
    def nameTemplateForType(self, arg: str) -> str:
        """nameTemplateForType(self, arg: str, /) -> str"""
    def placeholdersForType(self, arg: str) -> list[str]:
        """placeholdersForType(self, arg: str, /) -> list[str]"""
    @staticmethod
    def projectChangedCallback(arg: int) -> None:
        """projectChangedCallback(arg: int, /) -> None"""
    def projectDirectory(self) -> str:
        """projectDirectory(self) -> str"""
    def projectPath(self) -> str:
        """projectPath(self) -> str"""
    def reload(self) -> None:
        """reload(self) -> None"""
    @staticmethod
    def removeProjectChangedCallback(arg: int) -> None:
        """removeProjectChangedCallback(arg: int, /) -> None"""
    def setIconForType(self, arg0: str, arg1: str) -> bool:
        """setIconForType(self, arg0: str, arg1: str, /) -> bool"""
    def subLayerFormatForType(self, arg: str) -> str:
        """subLayerFormatForType(self, arg: str, /) -> str"""
    def subLayersForType(self, arg: str) -> list[str]:
        """subLayersForType(self, arg: str, /) -> list[str]"""
    def unitContextOption(self) -> str:
        """unitContextOption(self) -> str"""
    @overload
    def unitLayerPath(self, arg: str) -> str:
        """unitLayerPath(self, arg: str, /) -> str
        unitLayerPath(self, arg0: str, arg1: str, /) -> str"""
    @overload
    def unitLayerPath(self, arg0: str, arg1: str) -> str:
        """unitLayerPath(self, arg: str, /) -> str
        unitLayerPath(self, arg0: str, arg1: str, /) -> str"""
    def unitTypes(self) -> list[str]:
        """unitTypes(self) -> list[str]"""
    def units(self, arg: str) -> list[str]:
        """units(self, arg: str, /) -> list[str]"""
    def unitsForType(self, arg: str) -> list[str]:
        """unitsForType(self, arg: str, /) -> list[str]"""
