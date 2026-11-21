# Houdini stubs generated from Houdini 22.0.466

from pxr import UsdRender
from collections.abc import Callable as Callable
from pxr import Gf, Sdf, Usd, UsdGeom, UsdLux

from typing import TypeVar
from typing import TypeVar
_SchemaT = TypeVar('_SchemaT', bound=Usd.SchemaBase)
LIGHT_PRIM_TYPES: tuple[type[UsdLux.LightAPI], type[UsdLux.BoundableLightBase], type[UsdLux.NonboundableLightBase]]

def getAllDescendants(prim: Usd.Prim) -> list[Usd.Prim]: ...
def isLightPath(stage: Usd.Stage | None, path: str | Sdf.Path) -> bool:
    """
    Returns True if the given path refers to a light type of object on the
    given stage.  This is generally a prim that has the API UsdLuxLightAPI
    applied.

    Returns False if no stage is given.
    """
def isCollectionPath(path: str | Sdf.Path) -> bool:
    '''
    Returns True if the given path has the proper format (e.g. attribute
    namespacing) to represent a USD collection. This is just a wrapper for
    Usd.CollectionAPI.IsCollectionAPIPath() that may be a little easier to
    remember/type.

    An example collection path is "/foo/bar.collection:baz"
    '''
def expandCollectionPath(stage: Usd.Stage | None, path: str | Sdf.Path) -> tuple[Sdf.Path, str]:
    """
    Returns a tuple of the collection's primitive's path and the collection's
    name.
    """
def getCollection(stage: Usd.Stage | None, prim_path: str | Sdf.Path, name: str | None = None) -> Usd.CollectionAPI | None:
    """
    Returns a collection object for the given primitive and collection name.

    Note that USD's collection API treats a non-existant collection property
    exactly the same as an empty collection. If you want to check if a
    collection exists you need to use the lower-level attribute API.

    :param stage: the USD stage to look for the collection in.
    :param prim_path: path to the primitive on which the collection exists.
                      Or a path to a collection.
    :param name: name of the collection if prim_path is just a path to a prim.
    :return: A USD CollectionAPI object or None if no object or prim was found.
    """
def pathsInCollection(stage: Usd.Stage | None, collection: Usd.CollectionAPI | None, force_compute: bool = False) -> list[Sdf.Path] | None:
    """
    Returns a list of SdfPath objects representing the paths included in the
    given collection.

    :param stage: the USD stage the collection is on.
    :param collection: the USD CollectionAPI object to query for included paths.
    :return: a list of SdfPath objects.
    """
def pathsInCollectionAt(stage: Usd.Stage | None, prim_path: str | Sdf.Path, name: str | None = None) -> list[Sdf.Path] | None:
    """
    Returns a list of SdfPath objects representing the paths included in the
    collection for the given primitive and collection name.

    Raises KeyError if the primitive does not exist.

    :param stage: the USD stage the collection is on.
    :param prim_path: path to the primitive on which the collection exists.
                      Or a path to a collection.
    :param name: name of the collection if prim_path is just a path to a prim.
    :return: a list of SdfPath objects.
    """
def collectionsOnPrim(stage: Usd.Stage | None, prim_path: str | Sdf.Path) -> list[Usd.CollectionAPI]:
    """
    Returns a list of USD CollectionAPI objects for the collections on the
    primitive at the given path.

    Raises KeyError if the primitive does not exist.

    :param stage: the USD stage the primitive is on.
    :param prim_path: the path to the USD primitive.
    :return: list of CollectionAPI objects.
    """
def isPrimValid(stage: Usd.Stage | None, prim_path: str | Sdf.Path) -> bool:
    """
    Returns True if the prim exists and is valid.

    :param stage: the USD stage the primitive is on.
    :param prim_path: the path to the USD primitive.
    """
def isCollectionNameValid(name: str) -> bool:
    """
    Returns True if `name` is valid for a collection.

    :name: the name to check.
    """
def getHoudiniLayerInfoPrimPath() -> Sdf.Path:
    """
    Returns the path where the HoudiniLayerInfo prim lives.
    """
def getHoudiniLayerInfoPrim(layer: Sdf.Layer) -> Sdf.PrimSpec | None:
    """
    Returns the special HoudiniLayerInfo prim from the layer, if there is one.

    :param layer: the Sdf layer the primitive is on.
    :return: the Sdf.PrimSpec of the HoudiniLayerInfo prim, or None
    """
def getMetersPerUnit(stage: Usd.Stage | None) -> float:
    """
    Returns the meters per unit value of the supplied stage.

    :param stage: None, or the USD stage to use for determining unit size
    :return: the meters per unit of the stage, or the default if stage is None
    """
def convertFromMillimetersToCameraUnits(stage: Usd.Stage | None, mmvalue: float) -> float:
    """
    Returns a numeric value scaled from a representation in mm to a
    representation in 1/10 stage units (for example, if stage units are
    m-based then this function applies a 0.01 scaling; if stage units
    are cm-based then this function applies a 1.0 scaling).

    :param stage: the USD stage to use for determining unit size
    :param mmvalue: a numeric value as expressed in mm
    :return: the equivalent numeric value as expressed in 1/10 stage units
    """
def convertFromCameraUnitsToMillimeters(stage: Usd.Stage | None, value: float) -> float:
    """
    Returns a numeric value scaled from a representation in 1/10 stage
    units to to a representation in mm (for example, if stage units are
    m-based then this function applies a 100.0 scaling; if stage units
    are cm-based then this function applies a 1.0 scaling).

    :param stage: the USD stage to use for determining unit size
    :param value: a numeric value as expressed in 1/10 stage units
    :return: the equivalent numeric value as expressed in mm
    """
def createFramedCameraToBounds(stage: Usd.Stage, bounds: Gf.Range3d, cameraprimpath: str | Sdf.Path, rotatez: float = 0, rotatex: float = 25, rotatey: float = -35, fitbounds: float = 1.3, focallength: float = 35, horizontal_aperture: float = 10, vertical_aperture: float = 10, offsetdistance: float = 0) -> UsdGeom.Camera:
    """
    Returns a USD camera on the stage which frames the given bounds. Default
    settings for generating square thumbnails. Heavily copied from framing code
    in usdview.
    """
def addPrim(stage: Usd.Stage, prim_path: str | Sdf.Path, define_func: Callable[[Usd.Stage, str], _SchemaT], parent_type: str = 'Xform') -> _SchemaT:
    '''
    Defines the parent prims, in the way many LOP nodes do.

    `define_func` is the function that defines a prim on the stage, such 
    as \'UsdRender.Settings.Define\'.

    Typically `parent_type` is either \'Xform\' or \'Scope\'.

    Returns the class of object corresponding to the "define_prim_func" used.
    '''
