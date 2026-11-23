import hou
from collections.abc import Container, Iterable, Mapping, Sequence
from houtypes import JSONLike
from husd.utils import createFramedCameraToBounds as createFramedCameraToBounds
from pxr import Sdf, Usd
from typing import Any, Literal, Protocol
from typing_extensions import TypedDict

from typing import TypeAlias
from typing import TypeAlias
_AssetEntry: TypeAlias = tuple[str, str, str, _AssetBlindData | None]
class _AssetBlindData(TypedDict, total=False, extra_items=JSONLike):  # type: ignore[call-arg]
    refprimpath: str
    variants: dict[str, str]

class _RenderThumbnailFromFileFunc(Protocol):
    def __call__(self, usdfile: str | None = ..., usdprimpath: str | None = ..., output: str = ..., focusprim: str | None = ..., res: Sequence[float] = ..., renderer: str = ..., extrasublayers: Iterable[str] = ..., timelimit: float = ..., debug: bool = ..., variants: Mapping[str, str] = ...) -> None: ...

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
    extraparms: dict[str, Any]

theThumbnailCameraPrimPath: str
theThumbnailFileName: str
theMaterialThumbnailFileName: str
theThumbnailSceneFileKey: str
theVariantDirectoryName: str
theVariantsBlindDataKey: Literal['variants']
theComponentBuilderNodeTypes: list[str]
theAssetExtensions: list[str]

def debugPrint(*args: object) -> None: ...
def renderThumbnail_(rootlayer: Sdf.Layer, thumbnail_layers: Sequence[str], renderer: str, res: Sequence[float], timelimit: float, output: str, debug: bool) -> None: ...
def renderThumbnailFromFile_(usdfile: str | None = None, usdprimpath: str | None = None, output: str = '$HIP/thumbnail.png', focusprim: str | None = None, res: Sequence[float] = (256, 256), renderer: str = 'Karma', extrasublayers: Iterable[str] = ..., timelimit: float = -1, debug: bool = False, variants: Mapping[str, str] = ...) -> None:
    """
    Run an external process to generate a thumbnail from a usdlayer. When
    passed a primitive to focus, creates a framed camera view on the bounds to
    that prim.

    Any 'Thumbnail.usd' files found on HOUDINI_PATH as well as 'extrasublayers'
    can be used to customize the thumbnail renders with light rigs, backgrounds
    etc...
    """
def renderMaterialThumbnailFromFile_(usdfile: str | None = None, usdprimpath: str | None = None, output: str = '$HIP/thumbnail.png', focusprim: str | None = None, res: Sequence[float] = (128, 128), renderer: str = 'Karma', extrasublayers: Iterable[str] = ..., timelimit: float = -1, debug: bool = False, variants: Mapping[str, str] = ...) -> None:
    """
    Run an external process to generate a material thumbnail.

    Any 'extrasublayers' can be used to customize the thumbnail renders with
    light rigs, backgrounds etc...
    """
def saveThumbnailFromViewer(sceneviewer: hou.SceneViewer | None = None, output: str = '$HIP/thumbnail.png', croptocamera: bool = True, frame: float | None = None, res: Sequence[int] = (256, 256)) -> None:
    """
    Saves the current viewport to disk as a thumbnail.
    """
def saveAssetVariantLayers(assetname: str, assetdirectory: str, variantset: str, res: Sequence[float] = (256, 256), auto_render_thumbnails: bool = False, primpath: str | None = None, scene_file: str | None = None, debug: bool = False) -> list[str]:
    """
    Generates a variant layer for each variant of an asset. This layer is
    suitable to be referenced directly, as it is the same as the asset layer,
    but has the given variant selection set. It also has its own thumbnail.
    """

class AssetGallery:
    """ Provides an API functions for interacting with a USD asset catalog.
    """
    theDatabaseDefaultFile: str
    theDatabaseDefaultEnvVar: str
    theFallbackDatabaseDefaultEnvVar: str
    theCatalogParentPathCustomData: str
    def __init__(self, dbfile: str | None = None) -> None: ...
    def addAssetToGalleryDataSource(self, asset_file_path: str, thumbnail_file_path: str, asset_name: str, blind_data: _AssetBlindData | None) -> None:
        """ Low level method for adding an asset item to the asset catalog's
            data source. The parameters to this method should be the ones
            returned by a call to assetsInFileOrDirectory.

            This method just manipulates the database. It will not render a
            thumbnail, calculate missing values, or examine the asset for
            variants. The only data that can be left blank is the blind_data.
        """
    def addAsset(self, asset_file_or_dir_path: str, thumbnail_file_path: str | None = None, asset_name: str | None = None, variant_sets: Sequence[str] = ...) -> None:
        """ Adds a USD asset to the asset catalog, given the
            asset file or directory, and optionally the thumbnail file and
            asset name.

            If thumbnail file is not provided or does not exist (either as an
            explicitly specified file path or implicitly in the
            given asset directory), a temporary thumbnail is rendered and
            added to the gallery, so that the gallery entry always has an icon.

            If asset name is not provided, it is deduced from the file/dir name.

            variant_sets is a list of strings containing the names of the
            variant sets that exist on this asset. For each variant set name
            provided, this method will find all the variant values, and create
            a separate asset for each variant choice within that set. If
            multiple variant set names are provided, this procedure is
            performed recursively. Suppose variant_sets = ['geo', 'mtl'], and
            the asset has 'geo' variant choices 'high' and 'low'. With the
            'high' geo variant, there are 'mtl' variants 'clean' and 'dirty'.
            With the 'low' geo variant, there is only 'mtl' variant 'default'.
            This will result in 3 asset entries in the database, with variant
            choices for ('geo', 'mtl') being ('high', 'clean'),
            ('high', 'dirty'), and ('low', 'default'). These variant selections
            will be made automatically when these different asset variations
            are instantiated in your scene.
        """
    def addAssetsFromDirectory(self, dir_path: str, variant_sets: Sequence[str] = ..., stash_thumbnails_dir: str | None = None) -> None:
        """ Scans the given directory recursively for sub-directories that
            contain USD asset files, and adds these assets to the asset catalog.
        """
    def assetNamesAndFiles(self) -> list[tuple[str, str]]:
        """ Returns array of tuples (asset name, asset file path) found
            in the gallery.
        """
    def renderThumbnailForAsset(self, asset_file_path: str, thumbnail_file_path: str | None = None, variants: Mapping[str, str] = ..., blind_data: _AssetBlindData | None = ...) -> str | None:
        """ Renders a thumbnail image for the given USD asset file.
            If thumbnail file path is provided, it is used, otherwise
            a temporary file is created.
            Returns the file path to the rendered thumbnail image.
        """
    def removeThumbnailFile(self, thumbnail_file_path: str) -> None:
        """ Deletes the given thumbnail file.
        """
    def assetFileRootNameFromPath(self, asset_file_or_dir_path: str) -> str:
        """ Returns an asset name for the given asset file/dir path.
        """
    def assetsInFileOrDirectory(self, asset_file_or_dir_path: str, thumbnail_file_path: str | None = None, asset_name: str | None = None, variant_sets: Sequence[str] = ...) -> list[_AssetEntry]:
        """ Function for checking the USD asset in the given file or directory.
            Returns a list of infos that describe what assets should be added
            to the gallery (eg, a main asset, or a list of variants),
            given that file or dir path.

            Returns a list of triplets (asset file, thumbnail file, asset name).
        """
    def getVariantSetDictionaries_(self, prim: Usd.Prim, variant_sets: Sequence[str], vset_idx: int, variant_choices: dict[str, str]) -> list[dict[str, str]]: ...
    def assetsInDirectoryTree_(self, dir_path: str, variant_sets: Sequence[str]) -> list[_AssetEntry]:
        """ Recursive function for scanning a directory and its subdirectories
            in search of USD assets.

            Returns a list of triplets (asset file, thumbnail file, asset name),
            describing the assets in the given dir and its subdirs.
        """
    def addAssetToGallery_(self, datasource: hou.AssetGalleryDataSource, asset_file_path: str, thumbnail_file_path: str | None, asset_name: str, blind_data: _AssetBlindData | None, stash_thumbnails_dir: str | None = None, asset_parent_id: str | None = None) -> None:
        """ Adds the given USD asset to the asset catalog database.

            If the thumbnail file does not exist, a temporary thumbnail is
            rendered and added to the gallery.
        """
    def addAssetToDB_(self, datasource: hou.AssetGalleryDataSource, asset_file_path: str, thumbnail_file_path: str | None, asset_name: str, blind_data: _AssetBlindData | None, asset_parent_id: str | None = None) -> None:
        """ Inserts an asset row into the asset catalog database.
        """
    def assetNamesAndFilesInDB_(self, datasource: hou.AssetGalleryDataSource) -> list[tuple[str, str]]:
        """ Returns array of tuples (asset name, asset file path) found
            in the gallery.
        """
    def getRenderThumbnailFromFileFunc_(self) -> _RenderThumbnailFromFileFunc: ...
    def getAssetTypeName_(self) -> str: ...
    def getDataSource_(self) -> hou.AssetGalleryDataSource:
        """ Returns the asset catalog data source.
        """

class MaterialGallery(AssetGallery):
    """ Provides an API functions for interacting with a USD material catalog.
    """
    theDatabaseDefaultFile: str
    theDatabaseDefaultEnvVar: str
    theFallbackDatabaseDefaultEnvVar: str
    theDefaultPattern: str
    def __init__(self, dbfile: str | None = None) -> None: ...
    def addMaterialsFromFile(self, file_path: str, stash_thumbnails_dir: str | None = None, pattern: str = ...) -> None:
        """ Scans the given file for material primitives, and adds these
            materials to the material catalog.
        """
    def getRenderThumbnailFromFileFunc_(self) -> _RenderThumbnailFromFileFunc: ...
    def getAssetTypeName_(self) -> str: ...

theNodeParmNames: dict[str, _NodeParmNames]

def makeUniquePrimPath(node: hou.LopNode | None, primpath: str) -> str: ...
def addAssetReferenceToNode(node: hou.OpNode, srcpath: str, srcprimpath: str, dstprimpath: str, enabled: bool = True, unique: bool = False) -> str | None:
    """ Add an asset reference to the specified node  Currently
        supported LOP node types is 'materiallinker'.
    """
def removeAssetReferencesFromNode(node: hou.OpNode, primpath: str) -> bool:
    """ Search for asset references on a node and remove them.
        Currently supported LOP node types is 'materiallinker'.
    """
def renameAssetReferenceOnNode(node: hou.OpNode, primpath: str, dstprimpath: str) -> bool:
    """ Search for asset references on a node and rename the created prim
        path for the patching reference.
        Currently supported LOP node types is 'materiallinker'.
    """
def moveAssetReferencesOnNode(node: hou.OpNode, primpath: str, dstprimpath: str, primlist: Container[Sdf.Path] | None = None) -> bool:
    """ Search for asset references on a node that are under 'primpath'
        and rename them to be under 'dstprimpath' instead.
        Currently supported LOP node types is 'materiallinker'.
    """
def getInfoFromAssetJsonData(jsondata: str | bytes) -> list[_AssetInfo]: ...
def getInfoFromAssetDataSource(ident: str, datasource: hou.AssetGalleryDataSource) -> _AssetDataSourceInfo: ...
def getLinkerParmMatchingPrimPath(node: hou.OpNode, primpath: str) -> hou.Parm | None: ...
