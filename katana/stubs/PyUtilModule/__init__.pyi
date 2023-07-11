# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import CatalogAPI as CatalogAPI
import KatanaResources as KatanaResources
import KatanaResources as ResourceFiles
from . import AttrDump as AttrDump, ChildProcess as ChildProcess, ColorPaletteManager as ColorPaletteManager, Decorators as Decorators, Documentation as Documentation, EnvUtils as EnvUtils, FarmAPI as FarmAPI, FileUtils as FileUtils, Hints as Hints, IRFs as IRFs, KatanaFile as KatanaFile, LiveRenderAPI as LiveRenderAPI, NodeDebugOutput as NodeDebugOutput, NonUIPluginManager as NonUIPluginManager, OpDocumentationGenerator as OpDocumentationGenerator, ProjectSnapshot as ProjectSnapshot, RegisterToCamera as RegisterToCamera, RenderManager as RenderManager, RenderingCommon as RenderingCommon, ScenegraphBookmarkManager as ScenegraphBookmarkManager, ScenegraphUtils as ScenegraphUtils, Shelves as Shelves, StartupScripts as StartupScripts, SuperToolPlugins as SuperToolPlugins, UndoEntries as UndoEntries, UserNodes as UserNodes, WorkingSet as WorkingSet, WorkingSetClient as WorkingSetClient, WorkingSetManager as WorkingSetManager
from typing import Set, Tuple

def Initialize(): ...
