from collections.abc import Container, Iterable, Mapping, Sequence
from typing import Literal, Protocol, TypeAlias

from typing_extensions import TypedDict

import hou
from houtypes import JSONLike
from pxr import Sdf, Usd

# An asset's blind data, which the asset catalog keeps as JSON.
class _AssetBlindData(TypedDict, total=False, extra_items=JSONLike):  # type: ignore[call-arg]
    # The prim to reference, for a material.
    refprimpath: str
    # A variant set name to variant name map, for an asset's variant.
    variants: dict[str, str]

_AssetEntry: TypeAlias = tuple[str, str, str, _AssetBlindData | None]

class _RenderThumbnailFromFileFunc(Protocol):
    def __call__(
        self,
        usdfile: str | None = ...,
        usdprimpath: str | None = ...,
        output: str = ...,
        focusprim: str | None = ...,
        res: Sequence[float] = ...,
        renderer: str = ...,
        extrasublayers: Iterable[str] = ...,
        timelimit: float = ...,
        debug: bool = ...,
        variants: Mapping[str, str] = ...,
    ) -> None: ...

class _AssetInfo(TypedDict):
    datasource: hou.AssetGalleryDataSource
    id: str
    datasourcetype: str
    assettype: str
    label: str
    srcpath: str
    srcprimpath: str
    dstprimpath: str
    data: bytes

class _AssetDataSourceInfo(TypedDict):
    datasource: hou.AssetGalleryDataSource
    id: str
    datasourcetype: tuple[str]
    assettype: str
    label: str
    srcpath: str
    srcprimpath: str
    dstprimpath: str
    data: bytes

class _NodeParmNames(TypedDict):
    folder: str
    parmnames: dict[str, str]
    extraparms: dict[str, object]

theThumbnailCameraPrimPath: str
theThumbnailFileName: str
theMaterialThumbnailFileName: str
theThumbnailSceneFileKey: str
theVariantDirectoryName: str
theVariantsBlindDataKey: Literal["variants"]
theComponentBuilderNodeTypes: list[str]
theAssetExtensions: list[str]
theNodeParmNames: dict[str, _NodeParmNames]

def debugPrint(*args: object) -> None: ...
def renderThumbnail_(
    rootlayer: Sdf.Layer,
    thumbnail_layers: Sequence[str],
    renderer: str,
    res: Sequence[float],
    timelimit: float,
    output: str,
    debug: bool,
) -> None: ...
def renderThumbnailFromFile_(
    usdfile: str | None = ...,
    usdprimpath: str | None = ...,
    output: str = ...,
    focusprim: str | None = ...,
    res: Sequence[float] = ...,
    renderer: str = ...,
    extrasublayers: Iterable[str] = ...,
    timelimit: float = ...,
    debug: bool = ...,
    variants: Mapping[str, str] = ...,
) -> None: ...
def renderMaterialThumbnailFromFile_(
    usdfile: str | None = ...,
    usdprimpath: str | None = ...,
    output: str = ...,
    focusprim: str | None = ...,
    res: Sequence[float] = ...,
    renderer: str = ...,
    extrasublayers: Iterable[str] = ...,
    timelimit: float = ...,
    debug: bool = ...,
    variants: Mapping[str, str] = ...,
) -> None: ...
def saveThumbnailFromViewer(
    sceneviewer: hou.SceneViewer | None = ...,
    output: str = ...,
    croptocamera: bool = ...,
    frame: float | None = ...,
    res: Sequence[int] = ...,
) -> None: ...
def saveAssetVariantLayers(
    assetname: str,
    assetdirectory: str,
    variantset: str,
    res: Sequence[float] = ...,
    auto_render_thumbnails: bool = ...,
    primpath: str | None = ...,
    scene_file: str | None = ...,
    debug: bool = ...,
) -> list[str]: ...

class AssetGallery:
    theDatabaseDefaultFile: str
    theDatabaseDefaultEnvVar: str
    theFallbackDatabaseDefaultEnvVar: str
    theCatalogParentPathCustomData: str
    def __init__(self, dbfile: str | None = ...) -> None: ...
    def addAssetToGalleryDataSource(
        self,
        asset_file_path: str,
        thumbnail_file_path: str,
        asset_name: str,
        blind_data: _AssetBlindData | None,
    ) -> None: ...
    def addAsset(
        self,
        asset_file_or_dir_path: str,
        thumbnail_file_path: str | None = ...,
        asset_name: str | None = ...,
        variant_sets: Sequence[str] = ...,
    ) -> None: ...
    def addAssetsFromDirectory(
        self,
        dir_path: str,
        variant_sets: Sequence[str] = ...,
        stash_thumbnails_dir: str | None = ...,
    ) -> None: ...
    def assetNamesAndFiles(self) -> list[tuple[str, str]]: ...
    def renderThumbnailForAsset(
        self,
        asset_file_path: str,
        thumbnail_file_path: str | None = ...,
        variants: Mapping[str, str] = ...,
        blind_data: _AssetBlindData | None = ...,
    ) -> str | None: ...
    def removeThumbnailFile(self, thumbnail_file_path: str) -> None: ...
    def assetFileRootNameFromPath(self, asset_file_or_dir_path: str) -> str: ...
    def assetsInFileOrDirectory(
        self,
        asset_file_or_dir_path: str,
        thumbnail_file_path: str | None = ...,
        asset_name: str | None = ...,
        variant_sets: Sequence[str] = ...,
    ) -> list[_AssetEntry]: ...
    def getVariantSetDictionaries_(
        self,
        prim: Usd.Prim,
        variant_sets: Sequence[str],
        vset_idx: int,
        variant_choices: dict[str, str],
    ) -> list[dict[str, str]]: ...
    def assetsInDirectoryTree_(self, dir_path: str, variant_sets: Sequence[str]) -> list[_AssetEntry]: ...
    def addAssetToGallery_(
        self,
        datasource: hou.AssetGalleryDataSource,
        asset_file_path: str,
        thumbnail_file_path: str | None,
        asset_name: str,
        blind_data: _AssetBlindData | None,
        stash_thumbnails_dir: str | None = ...,
        asset_parent_id: str | None = ...,
    ) -> None: ...
    def addAssetToDB_(
        self,
        datasource: hou.AssetGalleryDataSource,
        asset_file_path: str,
        thumbnail_file_path: str | None,
        asset_name: str,
        blind_data: _AssetBlindData | None,
        asset_parent_id: str | None = ...,
    ) -> None: ...
    def assetNamesAndFilesInDB_(self, datasource: hou.AssetGalleryDataSource) -> list[tuple[str, str]]: ...
    def getRenderThumbnailFromFileFunc_(self) -> _RenderThumbnailFromFileFunc: ...
    def getAssetTypeName_(self) -> str: ...
    def getDataSource_(self) -> hou.AssetGalleryDataSource: ...

class MaterialGallery(AssetGallery):
    theDefaultPattern: str
    def __init__(self, dbfile: str | None = ...) -> None: ...
    def addMaterialsFromFile(
        self,
        file_path: str,
        stash_thumbnails_dir: str | None = ...,
        pattern: str = ...,
    ) -> None: ...
    def getRenderThumbnailFromFileFunc_(self) -> _RenderThumbnailFromFileFunc: ...
    def getAssetTypeName_(self) -> str: ...

def makeUniquePrimPath(node: hou.LopNode | None, primpath: str) -> str: ...
def addAssetReferenceToNode(
    node: hou.OpNode,
    srcpath: str,
    srcprimpath: str,
    dstprimpath: str,
    enabled: bool = ...,
    unique: bool = ...,
) -> str | None: ...
def removeAssetReferencesFromNode(node: hou.OpNode, primpath: str) -> bool: ...
def renameAssetReferenceOnNode(node: hou.OpNode, primpath: str, dstprimpath: str) -> bool: ...
def moveAssetReferencesOnNode(
    node: hou.OpNode,
    primpath: str,
    dstprimpath: str,
    primlist: Container[Sdf.Path] | None = ...,
) -> bool: ...
def getInfoFromAssetJsonData(jsondata: str | bytes) -> list[_AssetInfo]: ...
def getInfoFromAssetDataSource(ident: str, datasource: hou.AssetGalleryDataSource) -> _AssetDataSourceInfo: ...
def getLinkerParmMatchingPrimPath(node: hou.OpNode, primpath: str) -> hou.Parm | None: ...
