import hou
from collections.abc import Iterable, Mapping, Sequence
from hutil.Qt import QtGui
from typing import NoReturn, NotRequired
from typing_extensions import TypedDict

class _AssetSettingsJson(TypedDict, closed=True):  # type: ignore[call-arg]
    name: str
    filepathoption: int
    filepath: str
    customiconpath: str
    hversion: NotRequired[str]
    savedate: NotRequired[str]
    savetime: NotRequired[str]

class _CaptureSettingsJson(TypedDict, closed=True):  # type: ignore[call-arg]
    network: bool
    type: int
    display: bool

class _GeoOperatorPlacementJson(TypedDict, closed=True):  # type: ignore[call-arg]
    option: int
    operatoroffsettranslate: tuple[float, float, float]
    operatoroffsetrotate: tuple[float, float, float]
    operatoroffsetscale: tuple[float, float, float]

class _GeoOperatorJson(TypedDict, closed=True):  # type: ignore[call-arg]
    operatornode: str
    group: str
    placement: _GeoOperatorPlacementJson

class _GeoStandinJson(TypedDict, closed=True):  # type: ignore[call-arg]
    option: int
    standinoffsettranslate: tuple[float, float, float]
    standinoffsetrotate: tuple[float, float, float]
    standinoffsetscale: tuple[float, float, float]

class _GeoFilePlacementJson(TypedDict, closed=True):  # type: ignore[call-arg]
    option: int
    fileoffsettranslate: tuple[float, float, float]
    fileoffsetrotate: tuple[float, float, float]
    fileoffsetscale: tuple[float, float, float]

class _GeoFileJson(TypedDict, closed=True):  # type: ignore[call-arg]
    filepath: str
    placement: _GeoFilePlacementJson

class _GeoSourceJson(TypedDict, closed=True):  # type: ignore[call-arg]
    option: int
    operator: _GeoOperatorJson
    standin: _GeoStandinJson
    file: _GeoFileJson

class _GeometrySettingsJson(TypedDict, closed=True):  # type: ignore[call-arg]
    name: str
    embed: bool
    source: _GeoSourceJson

class _SettingsJson(TypedDict, closed=True):  # type: ignore[call-arg]
    assetsettings: _AssetSettingsJson
    geometrysettings: _GeometrySettingsJson
    capturesettings: _CaptureSettingsJson

class AutoRigsSettings:
    assetname: str
    assettype: str
    assetpathoption: int
    assetpathfile: str
    asseticonpath: str
    asseticon: QtGui.QIcon
    geoname: str
    geoembed: bool
    geosourceoption: int
    geooperatorplacement: int
    geooperator: str
    geooperatorgroup: str
    geooperatoroffset: dict[str, Sequence[float]]
    geostandinoffset: dict[str, Sequence[float]]
    geofileplacement: int
    geofile: str
    geofileoffset: dict[str, Sequence[float]]
    capturenetwork: bool
    capturetype: int
    capturedisplay: bool
    assetnode: hou.ObjNode
    hversion: str
    date: str
    time: str
    ASSETNAME_DEFAULT: str
    ASSETTYPE_DEFAULT: str
    ASSET_PATH_EMBED_HIP: int
    ASSET_PATH_FILE: int
    ASSET_PATH_OPTION_DEFAULT: int
    ASSET_PATH_DEFAULT: str
    ASSET_ICON_PATH_DEFAULT: str
    GEO_NAME_DEFAULT: str
    GEO_SOURCE_NONE: int
    GEO_SOURCE_FROM_OPERATOR: int
    GEO_SOURCE_FROM_FILE: int
    GEO_SOURCE_STAND_IN: int
    GEO_SOURCE_DEFAULT: int
    GEO_SOURCE_EMBED: bool
    GEO_PLACEMENT_AS_IS: int
    GEO_PLACEMENT_AUTOPLACE: int
    GEO_PLACEMENT_LABELS: list[str]
    GEO_PLACEMENT_DEFAULT: int
    GEO_SOURCE_TRANSLATE_DEFAULT: tuple[int, int, int]
    GEO_SOURCE_ROTATE_DEFAULT: tuple[int, int, int]
    GEO_SOURCE_SCALE_DEFAULT: tuple[int, int, int]
    CAPTURE_SHOW_NETWORK_DEFAULT: bool
    CAPTURE_TYPE_DEFAULT: int
    CAPTURE_DISPLAY_DEFORM: bool
    def __init__(self) -> None: ...
    def reset(self) -> None: ...
    def setAssetName(self, assetname: str) -> None: ...
    def setAssetPathOption(self, option: int) -> None: ...
    def setAssetPathFile(self, filename: str) -> None: ...
    def setAssetIconPath(self, path: str) -> None: ...
    def setGeoName(self, geoname: str) -> None: ...
    def setGeoEmbed(self, embed: bool) -> None: ...
    def setGeoSourceOption(self, option: int) -> None: ...
    def setGeoOperatorPlacement(self, placement: int) -> None: ...
    def setGeoOperator(self, operator: str) -> None: ...
    def setGeoOperatorGroup(self, group: str) -> None: ...
    def setGeoOperatorOffset(self, translate: Iterable[float], rotate: Iterable[float], scale: Iterable[float]) -> None: ...
    def setGeoStandinOffset(self, translate: Iterable[float], rotate: Iterable[float], scale: Iterable[float]) -> None: ...
    def setGeoFilePlacement(self, placement: int) -> None: ...
    def setGeoFile(self, filename: str) -> None: ...
    def setGeoFileOffset(self, translate: Iterable[float], rotate: Iterable[float], scale: Iterable[float]) -> None: ...
    def setSimpleSettings(self, assetname: str, assettype: str, geosource: int, geodata: Mapping[str, str] | str | None, assetfilesource: int, assetfiledata: str, capturenetwork: bool, capturetype: int, displaydeform: bool, asseticonpath: str) -> None: ...
    def setCaptureNetwork(self, capturenetwork: bool) -> None: ...
    def setCaptureType(self, capturetype: int) -> None: ...
    def setCaptureDisplay(self, capturedisplay: bool) -> None: ...
    def getAssetName(self) -> str: ...
    def getAssetType(self) -> str: ...
    def getAssetPathOption(self) -> int: ...
    def getAssetPathFile(self) -> str: ...
    def getAssetIconPath(self) -> str: ...
    def getAssetIcon(self) -> QtGui.QIcon: ...
    def getGeoName(self) -> str: ...
    def getGeoEmbed(self) -> bool: ...
    def getGeoSourceOption(self) -> int: ...
    def getGeoOperatorPlacement(self) -> int: ...
    def getGeoOperator(self) -> str: ...
    def getGeoOperatorGroup(self) -> str: ...
    def getGeoOperatorOffset(self) -> dict[str, Sequence[float]]: ...
    def getGeoStandinOffset(self) -> dict[str, Sequence[float]]: ...
    def getGeoFilePlacement(self) -> int: ...
    def getGeoFile(self) -> str: ...
    def getGeoFileOffset(self) -> dict[str, Sequence[float]]: ...
    def getCaptureNetwork(self) -> bool: ...
    def getCaptureType(self) -> int: ...
    def getCaptureDisplay(self) -> bool: ...
    def getAutoPlacement(self) -> NoReturn: ...
    def toJSON(self, assetnode: hou.ObjNode) -> _SettingsJson: ...
    def fromJSON(self, json: _SettingsJson) -> bool: ...
