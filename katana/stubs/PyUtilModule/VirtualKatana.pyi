# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import AssetAPI as AssetAPI
import AssetBrowser as AssetBrowser
import CacheManager as CacheManager
import CatalogAPI as CatalogAPI
import CatalogAPI as CatalogManager
import ConfigurationAPI_cmodule as Configuration
import DrawingModule as DrawingModule
import PyFnGeolibServices.ExpressionMath as ExpressionMath
import PyFnAttribute as FnAttribute
import PyFnGeolib as FnGeolib
import PyFnGeolibProducers as FnGeolibProducers
import PyFnGeolibServices as FnGeolibServices
import GeoAPI as GeoAPI
import KatanaResources as KatanaResources
import LookFileBakeAPI as LookFileBakeAPI
import MachineInfo as MachineInfo
import MediaCacheHandler as MediaCacheHandler
import Naming as Naming
import NodeGraphView as NodeGraphView
import NodegraphAPI as NodegraphAPI
import Nodes2DAPI as Nodes2DAPI
import Nodes3DAPI as Nodes3DAPI
import PyOpenColorIO as OCIO
import PluginSystemAPI as PluginSystemAPI
import UI4.KatanaPrefs.PrefNames as PrefNames
import PyFCurve as PyFCurve
import PyXmlIO as PyXmlIO
import QT4Browser as QT4Browser
import QT4Color as QT4Color
import QT4FormWidgets as QT4FormWidgets
import QT4GLLayerStack as QT4GLLayerStack
import QT4Panels as QT4Panels
import QT4Widgets as QT4Widgets
import QTFCurve as QTFCurve
import RenderingAPI as RenderingAPI
import RerenderEventMapper as RerenderEventMapper
import PyResolutionTableFn as ResolutionTable
import KatanaResources as ResourceFiles
import UI4 as UI4
import Naming as UniqueName
import Utils as Utils
import ViewerAPI as ViewerAPI
import WorkQueue as WorkQueue
from Callbacks.Callbacks import Callbacks as Callbacks
from PyUtilModule import Initialize as Initialize
from PyUtilModule.VirtualKatana import AttrDump as AttrDump, ChildProcess as ChildProcess, ColorPaletteManager as ColorPaletteManager, Decorators as Decorators, FaceSelectionManager as FaceSelectionManager, FarmAPI as FarmAPI, FarmManager as FarmManager, FormMaster as FormMaster, Hints as Hints, IRFs as IRFs, KatanaFile as KatanaFile, LayeredMenuAPI as LayeredMenuAPI, LiveRenderAPI as LiveRenderAPI, NodeDebugOutput as NodeDebugOutput, NodeMaster as NodeMaster, NonUIPluginManager as NonUIPluginManager, OpDocumentationGenerator as OpDocumentationGenerator, ProjectSnapshot as ProjectSnapshot, Qt as Qt, QtCore as QtCore, QtGui as QtGui, QtNetwork as QtNetwork, QtOpenGL as QtOpenGL, QtSql as QtSql, QtSvg as QtSvg, QtTest as QtTest, QtWidgets as QtWidgets, QtXml as QtXml, QtXmlPatterns as QtXmlPatterns, RegisterToCamera as RegisterToCamera, RenderManager as RenderManager, RenderingCommon as RenderingCommon, ScenegraphBookmarkManager as ScenegraphBookmarkManager, ScenegraphManager as ScenegraphManager, ScenegraphUtils as ScenegraphUtils, Shelves as Shelves, SuperToolPlugins as SuperToolPlugins, UserNodes as UserNodes, Widgets as Widgets, WorkingSet as WorkingSet, WorkingSetClient as WorkingSetClient, WorkingSetManager as WorkingSetManager
from UI4.KatanaPrefs.KatanaPrefsObject import KatanaPrefs as KatanaPrefs
from typing import Callable, Set, Tuple

LogGLHandlersOldLevel: int
update: Callable
version: tuple
