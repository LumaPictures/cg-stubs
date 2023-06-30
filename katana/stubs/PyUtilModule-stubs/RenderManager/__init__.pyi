# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyUtilModule.RenderManager.Constants as Constants
import PyUtilModule.RenderManager.Exceptions as Exceptions
import PyUtilModule.RenderManager.InteractiveRenderDelegateManager as InteractiveRenderDelegateManager
import PyUtilModule.RenderManager.NodegraphUtils as NodegraphUtils
import PyUtilModule.RenderManager.RenderCore as RenderCore
import PyUtilModule.RenderManager.RenderGlobals as RenderGlobals
import PyUtilModule.RenderManager.RenderSettings as RenderSettings
import PyUtilModule.RenderManager.RenderTriggers as RenderTriggers
import PyUtilModule.RenderManager.ResolutionTableUtils as ResolutionTableUtils
import PyUtilModule.RenderManager.ScenegraphUtils as ScenegraphUtils
from PyUtilModule.RenderManager.Constants import RenderModes as RenderModes
from PyUtilModule.RenderManager.Exceptions import RenderingException as RenderingException, UnsupportedRenderMethodNameException as UnsupportedRenderMethodNameException
from PyUtilModule.RenderManager.RenderCore import CancelRender as CancelRender, CancelRendersByType as CancelRendersByType, StartRender as StartRender, StartRenderLegacy as StartRenderLegacy
from PyUtilModule.RenderManager.RenderGlobals import ClearSequenceIDMaps as ClearSequenceIDMaps, GetAvailableSampleRates as GetAvailableSampleRates, GetBuffer2DAutoLock as GetBuffer2DAutoLock, GetDefaultSampleRate as GetDefaultSampleRate, GetDiskCachingAllowed as GetDiskCachingAllowed, GetInteractiveSampleRate as GetInteractiveSampleRate, GetLiveRenderOpTreePath as GetLiveRenderOpTreePath, GetOverscanPadding as GetOverscanPadding, GetRenderIDPass as GetRenderIDPass, GetRenderMode as GetRenderMode, GetRenderNodeTypes as GetRenderNodeTypes, GetRenderROI as GetRenderROI, GetRenderRawROI as GetRenderRawROI, GetRenderUseROI as GetRenderUseROI, GetRenderViews as GetRenderViews, GetRenderViewsAutoUpdate as GetRenderViewsAutoUpdate, GetRerenderCamera as GetRerenderCamera, GetRerenderMode as GetRerenderMode, GetRerenderNodeName as GetRerenderNodeName, GetRerenderRenderProducer as GetRerenderRenderProducer, GetRerenderRendererName as GetRerenderRendererName, GetSampleRate as GetSampleRate, GetSequenceIDMap as GetSequenceIDMap, GetTilePrioritizer as GetTilePrioritizer, IsDefaultROIUsed as IsDefaultROIUsed, IsRenderNode as IsRenderNode, IsRenderROIAbsolute as IsRenderROIAbsolute, IsRerendering as IsRerendering, IsSceneGraphMaskEnabled as IsSceneGraphMaskEnabled, QueryRender as QueryRender, ResetRenderROI as ResetRenderROI, ResumeRender as ResumeRender, SetBuffer2DAutoLock as SetBuffer2DAutoLock, SetDiskCachingAllowed as SetDiskCachingAllowed, SetInteractiveSampleRate as SetInteractiveSampleRate, SetLiveRenderOpTreePath as SetLiveRenderOpTreePath, SetOverscanPadding as SetOverscanPadding, SetRenderIDPass as SetRenderIDPass, SetRenderMode as SetRenderMode, SetRenderROI as SetRenderROI, SetRenderROIAbsolute as SetRenderROIAbsolute, SetRenderRawROI as SetRenderRawROI, SetRenderUseROI as SetRenderUseROI, SetRenderViews as SetRenderViews, SetRenderViewsAutoUpdate as SetRenderViewsAutoUpdate, SetRerenderCamera as SetRerenderCamera, SetRerenderMode as SetRerenderMode, SetRerenderNodeName as SetRerenderNodeName, SetRerendering as SetRerendering, SetSampleRate as SetSampleRate, SetTilePrioritizer as SetTilePrioritizer, SuspendRender as SuspendRender, TriggerManualRender as TriggerManualRender, UpdateSequenceIDMap as UpdateSequenceIDMap
from PyUtilModule.RenderManager.RenderSettings import RenderingSettings as RenderingSettings
from PyUtilModule.RenderManager.RenderTriggers import DoesNodeTrigger2DRender as DoesNodeTrigger2DRender
from PyUtilModule.RenderManager.ResolutionTableUtils import GetTempResolutionTablePath as GetTempResolutionTablePath, SaveResolutionTables as SaveResolutionTables
from PyUtilModule.RenderManager.ScenegraphUtils import AddRenderSettingsToRecipe as AddRenderSettingsToRecipe

RENDERCAMERAPATH_VIEWER_BUILTIN: str
RENDERCAMERATYPES: tuple
RENDERCAMERATYPE_RENDERSETTINGS: int
RENDERCAMERATYPE_RENDERSETTINGS_LABEL: str
RENDERCAMERATYPE_SPECIFIC: int
RENDERCAMERATYPE_VIEWER: int
RENDERCAMERATYPE_VIEWER_LABEL: str
RENDERMODES: tuple
RENDERMODE_INTERACTIVE: int
RENDERMODE_LABELS: dict
RENDERMODE_OPTIONS: list
RENDERMODE_PENUP: int
RENDERMODE_PROCESS: int
TILE_PRIORITIZER_NONE: int
TILE_PRIORITIZER_SCANLINE: int
TILE_PRIORITIZER_SPIRAL: int