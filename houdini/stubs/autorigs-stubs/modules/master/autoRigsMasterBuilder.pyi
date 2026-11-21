import hou
from autorigs.asset.autoRigsAsset import AutoRigsAsset as AutoRigsAsset
from autorigs.modules.master.buildMasterGuide import MasterGuide as MasterGuide
from autorigs.modules.master.masterGuideOptions import ModuleOptionsWidget as ModuleOptionsWidget
from autorigs.modules.master.masterGuideParams import ModuleParamsWidget as ModuleParamsWidget
from collections.abc import Callable as Callable

class AutoRigsMasterBuilder:
    def __init__(self) -> None: ...
    posDict: dict[str, hou.Vector2]
    CTRLNAMES: dict[str, str]
    DISPLAY_ONOFF_MENU: list[str]
    DISPLAY_BDF_MENU: list[str]
    INTERFACE_NAME_LABEL: dict[str, tuple[str, str]]
    PARAM_ARRAY_SUFFIX: str
    DISPLAY_FCN_HEADER: str
    DISPLAY_PARAMS_NAME: str
    @classmethod
    def buildRig(cls, autorigs_asset: AutoRigsAsset, options: ModuleOptionsWidget, params: ModuleParamsWidget, masterguide: MasterGuide, geoskin: hou.ObjNode, modulename: str) -> dict[str, hou.ObjNode]: ...
    @classmethod
    def addGeoSection(cls, geoNode: hou.SopNode, geoName: str, assetnode: hou.OpNode) -> None: ...
    @classmethod
    def generatePrefixes(cls, autorigs_asset: AutoRigsAsset) -> list[str]: ...
    @classmethod
    def generateDisplayParamsStr(cls, autorigs_asset: AutoRigsAsset, param_type: str) -> str:
        """Generates a list containing the parameter names of param_type (controldisplay, bonedisplay, etc)
            for each module in autorigs_asset"""
    @classmethod
    def generateDisplayCallbackStr(cls, fn_header: str, parm_type: str, arr_suffix: str) -> str:
        """Generate the callbacks for the master display options"""
    @classmethod
    def generateSetToDefaultCallbackStr(cls) -> str:
        '''Callback for when the user presses the "Reset to Default" button'''
    @classmethod
    def generateSetToDefaultAllCallbackStr(cls, fn_header: str, parm_type: str, arr_suffix: str) -> str:
        '''Fires when we use the master "Reset to Default" '''
    @classmethod
    def generateSetKeyCallbackStr(cls) -> str: ...
    @classmethod
    def generateSetKeyAllCallbackStr(cls, fn_header: str, parm_type: str, arr_suffix: str) -> str:
        '''Fires when we use the master "Reset to Default" '''
    @classmethod
    def generateGetParmsFromFolderStr(cls) -> str: ...

class MasterCallbackGenerator:
    """Class used for generating the master controls necessary for triggering the display and action controls
        in each individual module at once"""
    base_fcn_header: str
    template: hou.ParmTemplate
    param_type: str
    generation_fn: Callable[[str, str, str], str]
    autorigs_asset: AutoRigsAsset
    fcn_prefix: str
    PARAM_ARRAY_SUFFIX: str
    def __init__(self, base_fcn_header: str, template: hou.ParmTemplate, param_type: str, generation_fn: Callable[[str, str, str], str], autorigs_asset: AutoRigsAsset, fcn_prefix: str = '') -> None:
        """
        @param base_fcn_header: string representing the base header for the generation_fn
        @param template: hou.parmTemplate linked to the callback
        @param fcn_prefix: string prefix to be appended to the base_fcn_header
        @param param_type: base name of the parameter eg: (setdefault, controldisplay, bonedisplay)
        @param generation_fn: function that returns the python module callback str
        @param autorigs_asset: autorigs_asset object
        """
    def getPrefixes(self) -> list[str]: ...
    def getParamsStr(self) -> str:
        """Generates a list containing the parameter names of param_type (controldisplay, bonedisplay, etc)
            for each module in autorigs_asset"""
    def getFnHeader(self) -> str: ...
    def getFnStr(self) -> str: ...
