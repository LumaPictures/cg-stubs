import collections
from collections.abc import Iterable, Mapping, MutableMapping, MutableSequence, Sequence
from typing import Literal, Protocol, TypeAlias, TypedDict, TypeVar, overload

import hou
from autorigs.modules.base import buildBaseGuide
from autorigs.modules.extremity.extremityGuideModel import ModuleOptionModel
from autorigs.modules.limb.limbModule import LimbModule
from autorigs.modules.master.masterModule import MasterModule
from autorigs.modules.extremity.extremityGuideParams import _ExtremityParamJson, _ExtremityParamsJson
from autorigs.modules.extremity.extremityModule import _ExtremityModuleJson

# A side's {"<label>": guide node name, "fingers"/"toes": [{"root": ..., ...}, ...],
# "addfinger_nameformat"/"addtoe_nameformat": {"root": "finger_{}_root_guide", ...}}; the labels are
# the hand's or foot's JSON_LABELS.
_ExtremityGuideNamesJson: TypeAlias = dict[str, str | list[dict[str, str]] | dict[str, str]]

class _ExtremityGuideJson(TypedDict):
    guidenames: _ExtremityGuideNamesJson
    mirror_guidenames: _ExtremityGuideNamesJson
    digitspacing: float
    digitguidespacing: float
    digitinitialspacing: float

_GuideObject: TypeAlias = hou.ObjNode | hou.SopNode | list[hou.ObjNode] | list[list[hou.ObjNode]]

_ObjNodePart: TypeAlias = Literal[
    'root',
    'extremitystart',
    'extremityrot',
    'extremityroll',
    'digitroll',
    'digitrootguide',
    'metaguide',
    'bigdigitgeo',
    'guidecurve',
]
_SopNodePart: TypeAlias = Literal[
    'metaline',
    'metawristpts',
    'metaresample',
    'metaadd',
    'metabox',
    'metaends',
    'metapointcolor',
    'metacopy',
    'metaout',
    'metabigdigit',
    'metadeletecolor',
    'metacopybigdigit',
    'metacopynobigdigit',
    'metafirstpoint',
    'metamergebigdigit',
    'metaswitchbigdigit',
    'linepointline',
    'linepointmerge',
    'linemetaend',
    'linedigitend',
    'lineresample',
    'lineadddash',
    'guidecurve_merge',
    'guidecurve_add',
    'guidecurve_polywire',
    'guidecurve_out',
]
_ObjNodeKey: TypeAlias = Literal[
    'modulenode',
    'rootnode',
    'mainroot',
    'mainextremitystart',
    'mainextremityrot',
    'mainextremityroll',
    'maindigitroll',
    'maindigitrootguide',
    'mainmetaguide',
    'mainbigdigitgeo',
    'mainguidecurve',
    'mirrorroot',
    'mirrorextremitystart',
    'mirrorextremityrot',
    'mirrorextremityroll',
    'mirrordigitroll',
    'mirrordigitrootguide',
    'mirrormetaguide',
    'mirrorbigdigitgeo',
    'mirrorguidecurve',
]
_SopNodeKey: TypeAlias = Literal[
    'mainmetaline',
    'mainmetawristpts',
    'mainmetaresample',
    'mainmetaadd',
    'mainmetabox',
    'mainmetaends',
    'mainmetapointcolor',
    'mainmetacopy',
    'mainmetaout',
    'mainmetabigdigit',
    'mainmetadeletecolor',
    'mainmetacopybigdigit',
    'mainmetacopynobigdigit',
    'mainmetafirstpoint',
    'mainmetamergebigdigit',
    'mainmetaswitchbigdigit',
    'mainlinepointline',
    'mainlinepointmerge',
    'mainlinemetaend',
    'mainlinedigitend',
    'mainlineresample',
    'mainlineadddash',
    'mainguidecurve_merge',
    'mainguidecurve_add',
    'mainguidecurve_polywire',
    'mainguidecurve_out',
    'mirrormetaline',
    'mirrormetawristpts',
    'mirrormetaresample',
    'mirrormetaadd',
    'mirrormetabox',
    'mirrormetaends',
    'mirrormetapointcolor',
    'mirrormetacopy',
    'mirrormetaout',
    'mirrormetabigdigit',
    'mirrormetadeletecolor',
    'mirrormetacopybigdigit',
    'mirrormetacopynobigdigit',
    'mirrormetafirstpoint',
    'mirrormetamergebigdigit',
    'mirrormetaswitchbigdigit',
    'mirrorlinepointline',
    'mirrorlinepointmerge',
    'mirrorlinemetaend',
    'mirrorlinedigitend',
    'mirrorlineresample',
    'mirrorlineadddash',
    'mirrorguidecurve_merge',
    'mirrorguidecurve_add',
    'mirrorguidecurve_polywire',
    'mirrorguidecurve_out',
]

class _MetaThumbNodes(TypedDict):
    bigdigitgeo: hou.ObjNode
    linepointline: hou.SopNode
    linepointmerge: hou.SopNode
    linemetaend: hou.SopNode
    linedigitend: hou.SopNode
    lineresample: hou.SopNode
    lineadddash: hou.SopNode

# A hand's or foot's factory, whose createFromJsonNew createFromDefault calls.
_Guide_co = TypeVar("_Guide_co", bound="ExtremityGuide", covariant=True)
_Guide = TypeVar("_Guide", bound="ExtremityGuide")

class _CreatesFromJsonNew(Protocol[_Guide_co]):
    @classmethod
    def createFromJsonNew(
        cls, json: _ExtremityModuleJson, assetnode: hou.ObjNode, model: ModuleOptionModel, parent: hou.ObjNode | None = ...
    ) -> _Guide_co: ...

class ExtremityFactory(buildBaseGuide.BaseFactory):
    @classmethod
    def createFromDefault(
        cls: type[_CreatesFromJsonNew[_Guide]],
        json: _ExtremityModuleJson,
        assetnode: hou.ObjNode,
        model: ModuleOptionModel,
        parent: hou.ObjNode | None = ...,
    ) -> _Guide: ...

class ExtremityGuide(buildBaseGuide.BaseGuide[_ExtremityGuideJson]):
    TYPE_FULL: int
    TYPE_DIGITS: int
    TYPE_DEFAULT: int
    SIDE_LEFT: int
    SIDE_RIGHT: int
    SIDE_DEFAULT: int
    DISPLAY_ALL: int
    DISPLAY_BASE: int
    DISPLAY_DIGITS: int
    DISPLAY_DEFAULT: int

    display: bool
    guidenodesdata: dict[str, list[_GuideObject | bool | int]]
    parent: hou.ObjNode | None
    assetnode: hou.ObjNode
    model: ModuleOptionModel
    assetnodecontents: hou.ObjNode
    current_mirror: bool | int
    current_extremitytype: int
    current_side: int
    current_display: int
    current_hasbigdigit: bool | int
    current_metadigit: bool | int
    show_extremity_root: bool
    show_extremity_start: bool
    json: _ExtremityModuleJson
    extremitytype: str
    hversion: str | None

    modulenode: hou.ObjNode
    mainroot: hou.ObjNode
    mainextremitystart: hou.ObjNode
    mainextremityrot: hou.ObjNode
    mainextremityroll: hou.ObjNode
    maindigitroll: hou.ObjNode
    mirrorroot: hou.ObjNode
    mirrorextremitystart: hou.ObjNode
    mirrorextremityrot: hou.ObjNode
    mirrorextremityroll: hou.ObjNode
    mirrordigitroll: hou.ObjNode
    digitrootguide: hou.ObjNode
    mirror_digitrootguide: hou.ObjNode
    bigdigitguides: list[hou.ObjNode]
    digitsguides: list[list[hou.ObjNode]]
    mirrorbigdigitguides: list[hou.ObjNode]
    mirrordigitsguides: list[list[hou.ObjNode]]

    metaguide: hou.ObjNode
    metaline: hou.SopNode
    metaresample: hou.SopNode
    metaswitch: hou.SopNode
    metapointcolor: hou.SopNode
    metaswitchbigdigit: hou.SopNode
    mirrormetaguide: hou.ObjNode
    mirrormetaline: hou.SopNode
    mirrormetapointcolor: hou.SopNode
    mirrormetaswitchbigdigit: hou.SopNode
    metabigdigitgeo: hou.ObjNode
    mirrorbigdigitgeo: hou.ObjNode

    mainguidecurve: hou.ObjNode
    mainguidecurve_merge: hou.SopNode
    mainguidecurve_add: hou.SopNode
    mainguidecurve_polywire: hou.SopNode
    mainguidecurve_out: hou.SopNode
    mirrorguidecurve: hou.ObjNode
    mirrorguidecurve_merge: hou.SopNode
    mirrorguidecurve_add: hou.SopNode
    mirrorguidecurve_polywire: hou.SopNode
    mirrorguidecurve_out: hou.SopNode

    @classmethod
    def getGuideJsonLabels(cls) -> dict[str, str | list[str]]: ...
    def __init__(self, assetnode: hou.ObjNode, model: ModuleOptionModel, parent: hou.ObjNode | None = ...) -> None: ...
    def toJSON(self) -> _ExtremityGuideJson: ...
    def toJsonGuidename(
        self,
        jsonobj: MutableMapping[str, str | list[collections.OrderedDict[str, str]] | dict[str, str]],
        ismain: bool,
    ) -> None: ...
    def existingFromJson(self, json: _ExtremityModuleJson) -> None: ...
    def existingDigitsFromJson(
        self, digits_json: Sequence[Mapping[str, str]]
    ) -> tuple[list[hou.ObjNode], list[list[hou.ObjNode]]]: ...
    def createFromJson(self, json: _ExtremityModuleJson) -> None: ...
    def createMetaThumbGeo(
        self, guidenames: Mapping[str, str], metafirstpoint: hou.SopNode, bigdigitroot: hou.ObjNode
    ) -> _MetaThumbNodes: ...
    def setBigDigitParent(self, bigdigitguides: Sequence[hou.ObjNode], ismain: bool) -> None: ...
    @overload
    def getGuideObject(self, guidename: _ObjNodeKey) -> hou.ObjNode: ...
    @overload
    def getGuideObject(self, guidename: _SopNodeKey) -> hou.SopNode: ...
    @overload
    def getGuideObject(
        self, guidename: Literal['mainbigdigitguides', 'mirrorbigdigitguides']
    ) -> list[hou.ObjNode]: ...
    @overload
    def getGuideObject(
        self, guidename: Literal['maindigitsguides', 'mirrordigitsguides']
    ) -> list[list[hou.ObjNode]]: ...
    @overload
    def getGuideObject(self, guidename: str) -> _GuideObject: ...
    def getGuideObjectData(self, guidename: str) -> list[_GuideObject | bool | int] | None: ...
    @overload
    def getGuideObjectSide(self, ismain: bool, guidename: _ObjNodePart) -> hou.ObjNode: ...
    @overload
    def getGuideObjectSide(self, ismain: bool, guidename: _SopNodePart) -> hou.SopNode: ...
    @overload
    def getGuideObjectSide(self, ismain: bool, guidename: Literal['bigdigitguides']) -> list[hou.ObjNode]: ...
    @overload
    def getGuideObjectSide(self, ismain: bool, guidename: Literal['digitsguides']) -> list[list[hou.ObjNode]]: ...
    @overload
    def getGuideObjectSide(self, ismain: bool, guidename: str) -> _GuideObject: ...
    def getGuideObjectDataSide(self, ismain: bool, guidepart: str) -> list[_GuideObject | bool | int] | None: ...
    @overload
    def getDigitsGuidesObjectSide(self, ismain: bool, guidepart: Literal['bigdigit']) -> list[hou.ObjNode]: ...
    @overload
    def getDigitsGuidesObjectSide(
        self, ismain: bool, guidepart: Literal['digits', 'alldigit']
    ) -> list[list[hou.ObjNode]]: ...
    def deleteGuides(self) -> None: ...
    def displayGuides(self, display: bool) -> None: ...
    def lockGuides(self, lock: bool) -> None: ...
    def createMirrorFullExtremity(
        self, json: _ExtremityModuleJson, display: bool, parent: hou.ObjNode, extremitytype: str
    ) -> None: ...
    def createFullExtremity(
        self,
        json: _ExtremityModuleJson,
        guidejson: _ExtremityParamsJson,
        assetnode: hou.ObjNode,
        parent: hou.ObjNode,
        extremitytype: str,
    ) -> None: ...
    def buildAdditionalGuides(
        self, json: _ExtremityModuleJson, guidejson: _ExtremityParamsJson, assetnode: hou.ObjNode
    ) -> None: ...
    def parentExtremities(self) -> None: ...
    def createMirrorDigitGuidesFromJson(
        self, digitguides: Sequence[hou.ObjNode], jsonobj: Mapping[str, str], parent: hou.ObjNode, display: bool
    ) -> list[hou.ObjNode] | None: ...
    def createMirrorDigitGuides(
        self, digitguides: Sequence[hou.ObjNode], guidenames: Sequence[str], parent: hou.ObjNode, display: bool
    ) -> list[hou.ObjNode] | None: ...
    def createMirrorDigitsGuidesFromJson(
        self,
        digitsguides: Sequence[Sequence[hou.ObjNode]],
        jsonobjs: Sequence[Mapping[str, str]],
        parent: hou.ObjNode,
        display: bool,
    ) -> list[list[hou.ObjNode] | None]: ...
    def createDigitGuideNull(self, name: str, color: Sequence[float], display: bool) -> hou.ObjNode: ...
    def createGuideNamesFromJson(self, idx: int, json_nameformat: Mapping[str, str]) -> list[str]: ...
    def createGuidePositionsFromJson(
        self, idx: int, prev_tx: float, json: _ExtremityModuleJson
    ) -> list[tuple[float, float, float]]: ...
    def createDigitGuidesFromJson(
        self,
        parent: hou.ObjNode,
        digit_json: Mapping[str, str],
        digit_params_json: Mapping[str, _ExtremityParamJson],
        digitidx: int,
        display: bool,
    ) -> list[hou.ObjNode]: ...
    def createDigitGuides(
        self,
        parent: hou.ObjNode,
        guidenames: Sequence[str],
        guidepositions: Sequence[Sequence[float]],
        rootrotate: Sequence[float],
        color: Sequence[float],
        index: int,
        display: bool = ...,
    ) -> list[hou.ObjNode]: ...
    def makemetaGuideLine(self, parentnode: hou.ObjNode, name: str, negatedir: bool = ...) -> hou.SopNode: ...
    def makemetaGuideResample(self, node: hou.ObjNode, linewristwidth: hou.SopNode, name: str) -> hou.SopNode: ...
    def makemetaGuideAdd(self, node: hou.ObjNode, name: str) -> hou.SopNode: ...
    def makemetaGuideSwitch(
        self, node: hou.ObjNode, metaresample: hou.SopNode, metaonefing: hou.SopNode, name: str
    ) -> hou.SopNode: ...
    def makemetaGuideBox(self, node: hou.ObjNode, extremityrootguide: hou.ObjNode, name: str) -> hou.SopNode: ...
    def makemetaGuideEnds(self, node: hou.ObjNode, metabox: hou.SopNode, name: str) -> hou.SopNode: ...
    def makemetaPointColor(
        self,
        ismain: bool,
        node: hou.ObjNode,
        metawristpts: hou.SopNode,
        alldigits: Sequence[Sequence[hou.ObjNode]],
        name: str,
    ) -> hou.SopNode: ...
    def setPointColor(self, pointcolorsop: hou.SopNode, alldigits: Iterable[Sequence[hou.ObjNode]]) -> None: ...
    def getPointColorExp(self, pointcolor: hou.SopNode, alldigits: Iterable[Sequence[hou.ObjNode]]) -> list[str]: ...
    def makemetaGuideCopy(
        self, node: hou.ObjNode, metaends: hou.SopNode, metapointcolor: hou.SopNode, name: str
    ) -> hou.SopNode: ...
    def makemetaGuideOut(self, node: hou.ObjNode, metamerge: hou.SopNode, name: str) -> hou.SopNode: ...
    def toggleDisplayOfGuides(self, guides: Iterable[hou.ObjNode] | None, toggle: bool | int) -> None: ...
    def toggleDisplayOfDigitsGuides(
        self, digitroot: hou.ObjNode, digitsguides: Iterable[Iterable[hou.ObjNode]], toggle: bool
    ) -> None: ...
    def toggleDisplayOfAllDigitsGuides(self, toggle: bool) -> None: ...
    def setDisplayOfBigDigitsGuides(self, display: bool = ...) -> None: ...
    def setDefaultDisplayOfAllDigitsGuides(self, display: bool) -> None: ...
    def setDefaultDisplayOfBigDigitsGuides(self, display: bool) -> None: ...
    def toggleDisplayOfAllMirrorDigitsGuides(self, toggle: bool) -> None: ...
    def toggleDisplayOfBigMirrorDigitsGuides(self, toggle: bool) -> None: ...
    def toggleDisplayAndDisplayableOfAllBaseGuides(self, toggle: bool) -> None: ...
    def setDefaultDisplayOfAllMirrorDigitsGuides(self, display: bool) -> None: ...
    def setDefaultDisplayOfBigMirrorDigitsGuides(self, display: bool) -> None: ...
    def toggleDisplayAndDisplayableOfGuide(self, guidename: str, toggle: bool | int) -> None: ...
    def updateMirror(self, toggle: bool | int) -> None: ...
    def updateSide(self, side: int) -> None: ...
    def updateType(self, extremitytype: int) -> None: ...
    def updateDisplay(self, displayid: int) -> None: ...
    def updateHasBigDigit(self, hasbigdigit: bool | int) -> None: ...
    def updateMetaBigDigitGeo(self) -> None: ...
    def setBigDigitGuides(self, display: bool) -> None: ...
    def updateMetaPointColor(self) -> None: ...
    def updateMetaSide(self, side: int) -> None: ...
    def getInitialPrevTx(self) -> float: ...
    def updateNumDigits(self, numdigits: int) -> None: ...
    def updateMetaresample(self, numdigits: int, hasbigdigit: bool | int) -> None: ...
    def updateMetadigit(self, toggle: bool | int) -> None: ...
    def deleteDigitGuidesMirrorPair(
        self,
        digitguides: MutableSequence[hou.ObjNode] | None,
        mirrordigitguides: MutableSequence[hou.ObjNode] | None,
    ) -> None: ...
    def deleteDigitGuides(self, digitguides: MutableSequence[hou.ObjNode] | None) -> None: ...
    def removePreTransform(self, node: hou.ObjNode) -> None: ...
    def updateToLimbParent(self, node: hou.ObjNode, mirrornode: hou.ObjNode) -> None: ...
    def updateToMasterParent(self, node: hou.ObjNode, module: MasterModule) -> None: ...
    def updateToLimbParentSide(self, parent: hou.ObjNode, ismain: bool, rootkey: str, module: LimbModule) -> None: ...
    def updateToSpineParent(self, node: hou.ObjNode) -> None: ...
