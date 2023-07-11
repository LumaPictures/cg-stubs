# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import AssetAPI_cmodule as AssetAPI_cmodule
import KatanaResources as KatanaResources
import Utils as Utils
from AssetAPI_cmodule import AssetPlugin as AssetPlugin, AssetTransaction as AssetTransaction, FileSequence as FileSequence, FileSequencePlugin as FileSequencePlugin, GetAssetPlugin as GetAssetPlugin, GetAssetPluginNames as GetAssetPluginNames, GetDefaultAssetPlugin as GetDefaultAssetPlugin, GetDefaultAssetPluginName as GetDefaultAssetPluginName, GetDefaultFileSequencePlugin as GetDefaultFileSequencePlugin, GetDefaultFileSequencePluginName as GetDefaultFileSequencePluginName, GetFileSequencePlugin as GetFileSequencePlugin, GetFileSequencePluginNames as GetFileSequencePluginNames, ResetAllAssetAPIPlugins as ResetAllAssetAPIPlugins, SetDefaultAssetPluginName as SetDefaultAssetPluginName, SetDefaultFileSequencePluginName as SetDefaultFileSequencePluginName
from typing import Set, Tuple

kAssetContextAlembic: str
kAssetContextAttributeFile: str
kAssetContextCastingSheet: str
kAssetContextCatalog: str
kAssetContextFCurveFile: str
kAssetContextFarm: str
kAssetContextGafferThreeRig: str
kAssetContextImage: str
kAssetContextKatanaScene: str
kAssetContextLiveGroup: str
kAssetContextLookFile: str
kAssetContextLookFileMgrSettings: str
kAssetContextMacro: str
kAssetContextScenegraphBookmarks: str
kAssetContextShader: str
kAssetFieldName: str
kAssetFieldVersion: str
kAssetRelationArgsFile: str
kAssetTypeAlembic: str
kAssetTypeAttributeFile: str
kAssetTypeCastingSheet: str
kAssetTypeFCurveFile: str
kAssetTypeGafferThreeRig: str
kAssetTypeImage: str
kAssetTypeKatanaScene: str
kAssetTypeLiveGroup: str
kAssetTypeLookFile: str
kAssetTypeLookFileMgrSettings: str
kAssetTypeMacro: str
kAssetTypeScenegraphBookmarks: str
kAssetTypeShader: str
kFnAssetCreationOptionOutputFormat: str
kFnAssetOutputFormatArchive: str
kFnAssetOutputFormatDirectory: str

def ResolvePath(assetPath, frameTime): ...
