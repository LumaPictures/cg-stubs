from collections.abc import Callable

import hou

from autorigs.asset.autoRigsAsset import AutoRigsAsset
from autorigs.modules.master.buildMasterGuide import MasterGuide
from autorigs.modules.master.masterGuideOptions import ModuleOptionsWidget
from autorigs.modules.master.masterGuideParams import ModuleParamsWidget

class AutoRigsMasterBuilder:
    posDict: dict[str, hou.Vector2]
    CTRLNAMES: dict[str, str]
    DISPLAY_ONOFF_MENU: list[str]
    DISPLAY_BDF_MENU: list[str]
    INTERFACE_NAME_LABEL: dict[str, tuple[str, str]]
    PARAM_ARRAY_SUFFIX: str
    DISPLAY_FCN_HEADER: str
    DISPLAY_PARAMS_NAME: str

    def __init__(self) -> None: ...
    @classmethod
    def buildRig(
        cls,
        autorigs_asset: AutoRigsAsset,
        options: ModuleOptionsWidget,
        params: ModuleParamsWidget,
        masterguide: MasterGuide,
        geoskin: hou.ObjNode,
        modulename: str,
    ) -> dict[str, hou.ObjNode]: ...
    @classmethod
    def addGeoSection(cls, geoNode: hou.SopNode, geoName: str, assetnode: hou.OpNode) -> None: ...
    @classmethod
    def generatePrefixes(cls, autorigs_asset: AutoRigsAsset) -> list[str]: ...
    @classmethod
    def generateDisplayParamsStr(cls, autorigs_asset: AutoRigsAsset, param_type: str) -> str: ...
    @classmethod
    def generateDisplayCallbackStr(cls, fn_header: str, parm_type: str, arr_suffix: str) -> str: ...
    @classmethod
    def generateSetToDefaultCallbackStr(cls) -> str: ...
    @classmethod
    def generateSetToDefaultAllCallbackStr(cls, fn_header: str, parm_type: str, arr_suffix: str) -> str: ...
    @classmethod
    def generateSetKeyCallbackStr(cls) -> str: ...
    @classmethod
    def generateSetKeyAllCallbackStr(cls, fn_header: str, parm_type: str, arr_suffix: str) -> str: ...
    @classmethod
    def generateGetParmsFromFolderStr(cls) -> str: ...

class MasterCallbackGenerator:
    PARAM_ARRAY_SUFFIX: str
    base_fcn_header: str
    template: hou.ParmTemplate
    param_type: str
    generation_fn: Callable[[str, str, str], str]
    autorigs_asset: AutoRigsAsset
    fcn_prefix: str

    def __init__(
        self,
        base_fcn_header: str,
        template: hou.ParmTemplate,
        param_type: str,
        generation_fn: Callable[[str, str, str], str],
        autorigs_asset: AutoRigsAsset,
        fcn_prefix: str = ...,
    ) -> None: ...
    def getPrefixes(self) -> list[str]: ...
    def getParamsStr(self) -> str: ...
    def getFnHeader(self) -> str: ...
    def getFnStr(self) -> str: ...
