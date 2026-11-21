# Houdini stubs generated from Houdini 22.0.466

from _typeshed import SupportsWrite
from collections.abc import Iterator, Mapping, Sequence
from typing import Any, Never, Protocol

from typing import TypeAlias
from typing import TypeAlias
_Page: TypeAlias = tuple[list['RslParm | str'], dict[str, Any]]
_RampParmTags: TypeAlias = tuple[list['RslParm | str'], dict[str, dict[str, str]]]
_Default: TypeAlias = list[str] | list[float] | str
_ParmGroup: TypeAlias = tuple[list['RslParm'], dict[str, '_ParmGroup']]
class _XmlElement(Protocol):
    @property
    def attrib(self) -> Mapping[str, str]: ...
    @property
    def text(self) -> str | None: ...
    def find(self, path: str, /) -> _XmlElement | None: ...
    def iterfind(self, path: str, /) -> Iterator['_XmlElement']: ...

class ArgsOutput:
    """ Args output object
    """
    Type: str
    Name: str
    Label: str
    def __init__(self, outputType: str, outputName: str) -> None:
        """ Initialize output:
            outputType = output types: color, float, normal, point, vector, etc. 
            outputName = resultRGB, resultR, etc.
        """

class RslParm:
    """ An RslParm object describes the RSL parameter used in a
        shader.  The parameter default should *always* be a list
        object (even for scalars).
    """
    Type: str
    Name: str
    Page: str | None
    PageVisible: bool
    Label: str
    ArraySize: int
    Default: _Default | None
    Min: str | float | None
    Max: str | float | None
    HType: str
    HSize: int
    InputType: str
    Help: str | None
    HExtraUI: list[str] | None
    Visible: bool
    Connectable: bool | str
    IsMultiparm: bool
    IsRamp: bool
    RampParmTags: _RampParmTags
    HideRule: str | None
    DisableRule: str | None
    def __init__(self, rsl_type: str, rsl_name: str, rsl_default: _Default | None = None, rsl_arraysize: int = 1, rsl_help: str | None = None, ui_page: str | None = None, inputType: str | None = None, connectable: bool | str = True, rsl_min: str | float | None = None, rsl_max: str | float | None = None, hideRule: str | None = None, isRamp: bool = False, rampParmTags: _RampParmTags = ...) -> None:
        ''' Initiaize the RslParm:
            rsl_type      = The RSL type (e.g. "point" or "color")
            rsl_name      = The parameter name (e.g. "Kd")
            rsl_default   = The default value for the parameter.  The
                            defaults should always be specicified as
                            an array (list), even for scalar values.
                            For example: ["map.tx"] or [3] or [1,2,3]
            rsl_arraysize = The array size of the parameter
            rsl_help      = Help for the parameter
            ui_page       = Page for organizing the user interface
            inputType     = type for input connection
            connectable   = whether the parameter is connectable
            min/max       = min/max value of the parameter
            hideRule      = conditional rule for hiding the parameter
            isRamp        = whether it is a ramp parameter
            rampParmTags  = ramp parmTags
        '''
    def setLabel(self, label: str) -> None:
        """ The label shows up as the UI label for the parameter and
            may be different than the parameter name.
        """
    def setArraySize(self, size: int) -> None:
        """ Accessor method to set the array size for the parameter.
        """
    def setDefault(self, value: _Default | None) -> None:
        """ Accessor method to set the default value for the parameter.
        """
    def setMin(self, value: str | float | None) -> None:
        """ The min value for the parameter
        """
    def setMax(self, value: str | float | None) -> None:
        """ The max value for the parameter
        """
    def getHideOp(self, opName: str) -> str | None: ...
    def getDisableOp(self, opName: str) -> str | None: ...
    def setHideRule(self, visOp: str, visPath: str, visValue: str) -> None:
        """ Accessory method to set the hide-when rule.
        """
    def setDisableRule(self, lockOp: str, lockPath: str, lockValue: str) -> None:
        """ Accessory method to set the disable-when rule.
        """
    def setMultipleHideRule(self, visOp1: str, visPath1: str, visValue1: str, visOp: str | None, visOp2: str, visPath2: str, visValue2: str) -> None:
        """ Accessory method to set the multiple hide-when rule.
        """
    def setMultipleDisableRule(self, lockOp1: str, lockPath1: str, lockValue1: str, lockOp: str | None, lockOp2: str, lockPath2: str, lockValue2: str) -> None:
        """ Accessory method to set the multiple disable-when rule.
        """
    def processHideRule(self, hintdict: _XmlElement) -> None: ...
    def processDisableRule(self, hintdict: _XmlElement) -> None: ...
    def setHelp(self, rsl_help: str | None) -> None:
        """ Accessory method to set the help for the parameter.
        """
    def setUI(self, ui_type: str, meta: _XmlElement) -> None:
        """ Accessory method to set the Houdini UI widget.
        """
    def setVisibility(self, vis: bool) -> None:
        """ Accessory method to set the visibility state.
        """
    def isShaderParm(self) -> bool:
        """ Method to determine if the parameter is a shader parameter
        """
    def saveMultiparm(self, fp: SupportsWrite[str], parmName: str, parmLabel: str, indent: str = '') -> None: ...
    def numberToString(self, number: object) -> str: ...
    def save(self, fp: SupportsWrite[str], indent: str = '', ds: RslShader | None = None) -> None:
        """ Save the parameter in the format used by Houdini dialog
            script files.

            Ensure that the parmtag storing the RSL type information
            is saved as well.
        """

class RslMethod:
    """ An RslMethod object describes an RSL method on a class.
    """
    Return: str | None
    Name: str
    IsVariadic: bool
    Args: Sequence[Any] | None
    Help: str | None
    def __init__(self, rsl_return: str | None, rsl_name: str, rsl_isvariadic: bool = False, rsl_arguments: Sequence[object] | None = None, rsl_help: str | None = None) -> None:
        ''' Initialize the RslMethod:
            rsl_return = The return type of the method (e.g. "point" or "float")
            rsl_name = The name of the method
            rsl_isvariadic = True if the method is variadic
            rsl_arguments = List of arguments for the method
            rsl_help = Help string for the method
        '''
    def setHelp(self, rsl_help: str | None) -> None:
        """ Accessory method to set the help for the parameter.
        """
    def save(self, fp: SupportsWrite[str], indent: str = '') -> None:
        """ Save the method in the json format used in the VopTypeDefinitions 
            file.
        """

class RslShader:
    ''' The RslShader class stores the information about a shader.
        This consists of
            shader_type = RSL shader type (i.e. "surface", "light")
            shader_name = The name of the shader (i.e. "plastic")

        The shader has additional attributes which can be set
            Label = The text which appears in the SHOP menu
            Help  = A help string
            Icon  = The icon used on the SHOP tile

        After the shader is constructed, parameters may be added.
    '''
    Type: str
    Name: str
    Path: str
    Label: str
    label: str
    Help: Sequence[str] | None
    Icon: str | None
    Parms: _ParmGroup
    RampParmTags: _RampParmTags
    ParmPages: _Page
    currentPage: _Page
    PageVisible: bool
    ParmNames: dict[str, bool]
    VstructDict: dict[str, list[str]]
    Outputs: tuple[list[ArgsOutput], dict[Never, Never]]
    OutputNames: dict[str, bool]
    Methods: list[RslMethod]
    HType: str | None
    Table: str
    MinInputCount: int
    MaxInputCount: int
    def __init__(self, shader_type: str, shader_name: str, shader_path: str | None = None) -> None: ...
    def isValid(self) -> bool:
        """The RSL shader is only valid if there's a corresponding
           SHOP type for the shader.
        """
    def setName(self, name: str | None) -> None:
        """ Set operator name (overriding shader name for some reason)
        """
    def setLabel(self, label: str | None) -> None:
        """ Set the label (text which shows up in the SHOP menu) for
            the shader.
        """
    def setPath(self, path: str | None) -> None:
        """ Set the path (text to resolve the shader in rib)
        """
    def setIcon(self, icon: str | None) -> None:
        """ Set the icon for the SHOP
        """
    def setHelp(self, help: Sequence[str] | None) -> None:
        ''' Set the help for the SHOP.  The help should be an array of
            strings.  Each element of the array will be a separate
            line of help text.  For example:

            shader.setHelp(["line one", "line two"])
        '''
    def addParm(self, parm: RslParm) -> None:
        """ Add a parameter.  The parameter should be an RslParm
        """
    def beginPage(self, pageName: str) -> None:
        """Each page is stored as a (list,dict) tuple. Child pages names are
            stored as a string in the list of the parent (the child page's name)
            and the child page itself is then stored in the dict of
            its parent. The dict has a pointer back to its parent node
            which is a tuple of (parentpage, 'child name')"""
    def endPage(self) -> None: ...
    def getPagePath(self, page: _Page) -> str | None:
        """ build a pathname to the current page replacing spaces with _
            and using _ as a joining char"""
    def addOutput(self, output: ArgsOutput) -> None:
        """ Add output
        """
    def addMethod(self, method: RslMethod) -> None:
        """ Add a method.
        """
    def saveRampParmTags(self, fp: SupportsWrite[str], parmName: str, indent: str = '') -> None: ...
    def savePage(self, fp: SupportsWrite[str], pageName: str, node: _Page, indent: str = '') -> None: ...
    def saveRoot(self, fp: SupportsWrite[str], node: _Page, indent: str = '') -> None: ...
    def saveDialogScript(self, fp: SupportsWrite[str]) -> bool:
        """ Save the dialog script to the file passed in.  This is the
            primary component of the OTL.
        """
    def saveVopTypeDefinitions(self, fp: SupportsWrite[str]) -> bool:
        """ Save the vop type defintions file. This file allows other classes
            to introspect methods on the shader class.
        """
    def makeOTL(self, otl_path: str) -> bool:
        ''' An OTL consists of several components.  The most important
            for SHOPs is the dialog script (which defines the UI).

            This part of the program relies on being able to create an
            expanded view of the OTL (consisting of all the
            components).

            When the expanded view has been created, the "hotl"
            application is invoked to bundle the components into the
            OTL.
        '''
    def addToOTL(self, otl_path: str, force: bool = True) -> bool:
        """ This method will add the shader definition to an OTL. 

            If the OTL already contains a definition for the shader,
            the force parameter can be used to ensure that this shader
            is included (instead of leaving the previous definition).
            This is the default behaviour.
        """
