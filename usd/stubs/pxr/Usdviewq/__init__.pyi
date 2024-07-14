# mypy: disable-error-code="misc, override, no-redef"

import Boost.Python
import pxr.Ar
import pxr.Sdf
import pxr.Tf
import pxr.Tf as Tf
import pxr.Usd
import pxr.UsdAppUtils as UsdAppUtils
from . import adjustDefaultMaterial as adjustDefaultMaterial, adjustDefaultMaterialUI as adjustDefaultMaterialUI, adjustFreeCamera as adjustFreeCamera, adjustFreeCameraUI as adjustFreeCameraUI, appController as appController, attributeValueEditor as attributeValueEditor, attributeValueEditorUI as attributeValueEditorUI, attributeViewContextMenu as attributeViewContextMenu, common as common, configController as configController, customAttributes as customAttributes, frameSlider as frameSlider, freeCamera as freeCamera, headerContextMenu as headerContextMenu, layerStackContextMenu as layerStackContextMenu, legendUtil as legendUtil, mainWindowUI as mainWindowUI, plugin as plugin, preferences as preferences, preferencesUI as preferencesUI, prettyPrint as prettyPrint, primContextMenu as primContextMenu, primContextMenuItems as primContextMenuItems, primLegend as primLegend, primLegendUI as primLegendUI, primTreeWidget as primTreeWidget, primViewItem as primViewItem, propertyLegend as propertyLegend, propertyLegendUI as propertyLegendUI, pythonInterpreter as pythonInterpreter, qt as qt, rootDataModel as rootDataModel, scalarTypes as scalarTypes, selectionDataModel as selectionDataModel, settings as settings, stageView as stageView, usdviewApi as usdviewApi, usdviewContextMenuItem as usdviewContextMenuItem, variantComboBox as variantComboBox, viewSettingsDataModel as viewSettingsDataModel
from pxr.Usdviewq.appController import AppController as AppController
from pxr.Usdviewq.common import Timer as Timer
from pxr.Usdviewq.settings import ConfigManager as ConfigManager
from typing import Any, Callable, ClassVar, overload

__MFB_FULL_PACKAGE_NAME: str

class ContainerDataSource(Boost.Python.instance):
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """
    @overload
    def Get(self, arg2: object, /) -> Any: ...
    @overload
    def Get(self, arg2: DataSourceLocator, /) -> Any: ...
    def GetNames(self) -> list: ...

class DataSourceBase(Boost.Python.instance):
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """

class DataSourceLocator(Boost.Python.instance):
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, arg2: object, /) -> None: ...
    @overload
    def __init__(self, arg2: object, arg3: object, /) -> None: ...
    @overload
    def __init__(self, arg2: object, arg3: object, arg4: object, /) -> None: ...
    @overload
    def __init__(self, arg2: object, arg3: object, arg4: object, arg5: object, /) -> None: ...
    @overload
    def __init__(self, arg2: object, arg3: object, arg4: object, arg5: object, arg6: object, /) -> None: ...
    @overload
    def __init__(self, arg2: object, arg3: object, arg4: object, arg5: object, arg6: object, arg7: object, /) -> None: ...
    @overload
    def Append(self, arg2: object, /) -> DataSourceLocator: ...
    @overload
    def Append(self, arg2: DataSourceLocator, /) -> DataSourceLocator: ...
    def GetCommonPrefix(self, arg2: DataSourceLocator, /) -> DataSourceLocator: ...
    def GetElement(self, arg2: int, /) -> Any: ...
    def GetElementCount(self) -> int: ...
    def GetFirstElement(self) -> Any: ...
    def GetLastElement(self) -> Any: ...
    def GetString(self, arg2: str | pxr.Ar.ResolvedPath, /) -> str: ...
    def HasPrefix(self, arg2: DataSourceLocator, /) -> bool: ...
    def Intersects(self, arg2: DataSourceLocator, /) -> bool: ...
    def IsEmpty(self) -> bool: ...
    def RemoveFirstElement(self) -> DataSourceLocator: ...
    def RemoveLastElement(self) -> DataSourceLocator: ...
    def ReplaceLastElement(self, arg2: object, /) -> DataSourceLocator: ...
    def ReplacePrefix(self, arg2: DataSourceLocator, arg3: DataSourceLocator, /) -> DataSourceLocator: ...
    def __eq__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...

class DataSourceLocatorSet(Boost.Python.instance):
    __instance_size__: ClassVar[int] = ...
    def __init__(self) -> None: ...
    def AsString(self) -> str: ...
    def Contains(self, arg2: DataSourceLocator, /) -> bool: ...
    @overload
    def Intersects(self, arg2: DataSourceLocator, /) -> bool: ...
    @overload
    def Intersects(self, arg2: DataSourceLocatorSet, /) -> bool: ...
    def IsEmpty(self) -> bool: ...
    @overload
    def insert(self, arg2: DataSourceLocator, /) -> None: ...
    @overload
    def insert(self, arg2: DataSourceLocatorSet, /) -> None: ...

class HydraObserver(Boost.Python.instance):
    """
    Abstracts pieces necessary for implementing a Hydra Scene Browser in a
    manner convenient for exposing to python.


    For C++ code, this offers no benefits over directly implementing an
    HdSceneIndexObserver. It exists solely in service of the python
    implementation of Hydra Scene Browser present in usdview.

    See extras/imaging/examples/hdui for an example of a C++ direct
    implementation.
    """
    __instance_size__: ClassVar[int] = ...
    def __init__(self) -> None: ...
    def ClearPendingNotices(self) -> None:
        """
        Clears any accumulated scene change notices.
        """
    def GetChildPrimPaths(self, _primPath: pxr.Sdf.Path | str, /) -> list[pxr.Sdf.Path]:
        """
        Returns the paths of the immediate children of the specified
        C{primPath} for the actively observer scene index.
        """
    def GetDisplayName(self) -> str:
        """
        Returns the display name of the actively targeted scene index.


        This display name is currently derived from the C++ typename.
        """
    def GetInputDisplayNames(self, _inputIndices: IndexList, /) -> list[str]:
        """
        Starting from the currently targeted HdSceneIndex, each value in the
        C{inputIndices} is treated as an index into the result of
        HdFilteringSceneIndexBase::GetInputScenes.


        If the scene index reached is a subclass of HdFilteringSceneIndexBase,
        the display names of the return value of GetInputScenes is returned.
        Otherwise, the return value is empty.
        """
    def GetPendingNotices(self) -> list[NoticeEntry]:
        """
        Returns (and clears) any accumulated scene change notices.


        Consumers of this follow a polling rather than callback pattern.
        """
    def GetPrim(self, _primPath: pxr.Sdf.Path | str, /) -> HdSceneIndexPrim:
        """
        Returns the prim type and data source for the specified C{primPath}
        for the actively observer scene index.
        """
    @staticmethod
    def GetRegisteredSceneIndexNames() -> list[str]:
        """
        Returns the names of scene indices previously registered with
        HdSceneIndexNameRegistry.


        It allows a browser to retrieve available instances without direct
        interaction with the application.
        """
    def HasPendingNotices(self) -> bool:
        """
        Returns true if there are pending scene change notices.


        Consumers of this follow a polling rather than callback pattern.
        """
    def TargetToInputSceneIndex(self, _inputIndices: IndexList, /) -> bool:
        """
        Starting from the currently targeted HdSceneIndex, each value in the
        C{inputIndices} is treated as an index into the result of
        HdFilteringSceneIndexBase::GetInputScenes.


        Returns true if each followed index maps to a valid index into the
        input scenes of the previous.
        """
    def TargetToNamedSceneIndex(self, _name: str | pxr.Ar.ResolvedPath, /) -> bool:
        """
        Target this observer to a scene index with the given name previously
        registered via HdSceneIndexNameRegistry.
        """

class InvalidUsdviewOption(Exception):
    """Raised when an invalid Usdview option is found in
    Launcher.ValidateOptions or any methods which override it.
    """

class Launcher:
    """
    Base class for argument parsing, validation, and initialization for UsdView

    Subclasses can choose to override
      -- GetHelpDescription()
      -- RegisterOptions()
      -- ParseOptions()
      -- ValidateOptions()
      -- GetResolverContext()
    """
    __init__: ClassVar[Callable] = ...
    GetHelpDescription: ClassVar[Callable] = ...
    GetResolverContext: ClassVar[Callable] = ...
    LaunchPreamble: ClassVar[Callable] = ...
    ParseOptions: ClassVar[Callable] = ...
    RegisterOptions: ClassVar[Callable] = ...
    RegisterPositionals: ClassVar[Callable] = ...
    Run: ClassVar[Callable] = ...
    ValidateOptions: ClassVar[Callable] = ...
    _Launcher__LaunchProcess: ClassVar[Callable] = ...

class SampledDataSource(Boost.Python.instance):
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """
    def GetTypeString(self) -> str: ...
    def GetValue(self, arg2: float, /) -> Any: ...

class Utils(Boost.Python.instance):
    """
    Performance enhancing utilities for usdview.
    """
    __instance_size__: ClassVar[int] = ...
    def __init__(self) -> None: ...
    @staticmethod
    def GetPrimInfo(_prim: pxr.Usd.Prim, _time: pxr.Usd.TimeCode | float | pxr.Sdf.TimeCode, /) -> tuple:
        """
        Fetch prim-related data in batch to to speed up Qt treeview item
        population.


        Takes a time argument so that we can evaluate the prim's visibiity if
        it is imageable.
        """
    @staticmethod
    def _GetAllPrimsOfType(_stage: pxr.Usd.Stage, _schemaType: pxr.Tf.Type, /) -> list[pxr.Usd.Prim]:
        """
        For the given C{stage} and C{schemaType}, return all active, defined
        prims that either match the schemaType exactly or are a descendant
        type.
        """

class VectorDataSource(Boost.Python.instance):
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """
    def GetElement(self, arg2: int, /) -> Any: ...
    def GetNumElements(self) -> int: ...
