import hou
from typing import Protocol

class _SupportsWriteStr(Protocol):
    def write(self, s: str, /) -> object: ...

SHADERHDA_OP_TABLE_NAME: str

class Shader:
    """ Abstracts the information about a shader as a whole and
        allows writing it out as an HDA.
    """
    myHDAName: str
    myHDALabel: str | None
    myHDAIcon: str | None
    myShaderName: str | None
    myShaderType: str | None
    myRenderMask: str | None
    myVopnetMask: str | None
    myHelpText: str | None
    myHelpURL: str | None
    myTabSubMenus: list[str]
    myToolKeywords: list[str]
    mySignatureSet: ShaderSignatureSet
    def __init__(self, hda_name: str) -> None: ...
    def hdaName(self) -> str:
        """ Returns the name of Houdini operator representing this shader.
        """
    def setHdaLabel(self, label: str | None) -> None:
        """ Sets the Houdini operator name for this shader.
        """
    def hdaLabel(self) -> str:
        """ Returns the label for this shader to be used in Houdini UI.
        """
    def hasHdaLabel(self) -> bool:
        """ Returns true if this shader has an explicitly set label.
        """
    def setHdaIcon(self, icon: str | None) -> None:
        """ Sets the name of the icon file for this HDA.
        """
    def hdaIcon(self) -> str | None:
        """ Returns the name of the icon file for this HDA.
        """
    def shaderName(self) -> str | None:
        """ Returns the name by which the shader is known to the renderer.
        """
    def setShaderName(self, shader_name: str | None) -> None:
        """ Sets the name by which the shader is known to the renderer.
        """
    def shaderType(self) -> str | None:
        """ Returns this shader's type (eg, surface, displacement, etc).
        """
    def setShaderType(self, shader_type: str | None) -> None:
        """ Sets the type for this shader (eg, surface, displacement, etc).
        """
    def renderMask(self) -> str | None:
        """ Returns the render mask used in Houdini to determine applicable
            renderers capable of handling this shader.
            In practice, this is really a shading language this shader
            belongs to.
        """
    def setRenderMask(self, render_mask: str | None) -> None:
        """ Sets the render mask. See renderMask() for mor info.
        """
    def vopnetMask(self) -> str | None:
        """ Returns the vopnet mask used in Houdini to filter the availability
            of the shader HDAs in various networks.
        """
    def setVopnetMask(self, vopnet_mask: str | None) -> None:
        """ Sets the vopnet mask. See vopnetMask() for more info.
        """
    def helpText(self) -> str | None:
        """ Returns the HDA documentation help text stored in HDA section.
        """
    def setHelpText(self, help_text: str | None) -> None:
        """ Sets the HDA documentation help text stored in HDA section.
        """
    def helpURL(self) -> str | None:
        """ Returns the HDA documentation help URL stored in HDA section.
        """
    def setHelpURL(self, help_url: str | None) -> None:
        """ Sets the HDA documentation help URL stored in HDA section.
        """
    def tabSubMenus(self) -> list[str]:
        """ Returns the Tab menu submenus under which the HDA is categorized.
        """
    def setTabSubMenus(self, submenus: str | list[str]) -> None:
        """ Sets the Tab menu submenus under which the HDA is categorized.
        """
    def toolKeywords(self) -> list[str]:
        """ Returns keywords for the shelf tool for this HDA.
        """
    def setToolKeywords(self, keywords: str | list[str]) -> None:
        """ Sets keywords for the shelf tool for this HDA.
        """
    def signatureSet(self) -> ShaderSignatureSet:
        """ Returns an object that manages shader signatures, ie, a set of
            input/output parameter groups that differ in their types.
        """
    def addHDAToFile(self, hda_file_name: str, should_append_hda: bool) -> None:
        """ Write this shader as an HDA to the given HDA file,
            appending to the file or overwriting it as requested thru the
            `should_append_hda` parameter.
        """
    def addHDAToExpandedDir(self, hda_dir_name: str, should_append_hda: bool) -> None:
        """ Write this shader as an expanded HDA to the given HDA directory,
            replading the directory or appending to it as requested
            thru the `should_append_hda` parameter.
        """
    def writeDSToFile(self, ds_file_name: str) -> None:
        """ Write the Houdini parameter Dialog Script for this shader
            to the file of a given name. Dialog Script defines node parameters.
        """

class ShaderSignatureSet:
    """ A class holding and managing a group of signatures for a shader,
        keeping track of the default signature.

        A shader can have mutliple signatures, each operating on a different
        data types. In Houdini, a shader HDA VOP can have different signatures
        can have different input/output types, but the number of inputs
        and outputs must be the same, and so must be their names; only
        their types can be different.

        Eg, an 'add' shader can operate on 'float' or 'vector' inputs.
        This is represented as one HDA that can switch between the types
        depending on wired inputs (or explicit choice in Signature menu).
        While a renderer may (or may not) implement it as two separately inamed
        functions add_float() and add_vector(), etc.
    """
    mySignatures: list['ShaderSignature']
    myDefaultSignatureIndex: int
    def __init__(self) -> None: ...
    def signatures(self) -> list['ShaderSignature']:
        """ Returns an array of signatures for a shader.
        """
    def signaturesSortedByLabel(self) -> list['ShaderSignature']:
        """ Returns signatures  sorted in an ascending order of the signature label.
         """
    def defaultSignature(self) -> ShaderSignature | None:
        """ Returns the default shader signature, or None if it was not
            determined yet.
        """
    def sortSignatures(self) -> None:
        """ Sorts the signatures in an ascending order of the signature label.
        """
    def setBestDefaultSignature(self) -> None:
        """ Determine the default signature among the set of currently held
            signatures, and record it as the default one for future use.
        """
    def addSignature(self, shader_signature: ShaderSignature) -> tuple[bool, str | None]:
        """ Add a new signature to this set.

            A new signature must have the the same number of inputs and outputs
            as the already added signatures, and their names must mach.
            The other aspects such as type or UI parameter can differ.

            Returns a pair of status and error message (which can be None).
        """
    def writeToDialogScript(self, fp: _SupportsWriteStr) -> None:
        """ Write the information about all the signatures to the Dialog Script.

            In addition to node parameters, it writes the node input information
        """
    def hdaParmTemplateGroup(self) -> hou.ParmTemplateGroup:
        """ Returns a Houdini ParmTemplateGroup object describing the node
            parameters for all the signatures.

            This is for the multi-signature shader VOP HDAs that are able to
            handle several signatures, and to switch between them using the
            Signature drop-down menu parameter, changing their input/output
            types, and revealing/hiding various node parameters accordingly.
        """

class ShaderSignature:
    """ A class holding and managing a goup of shader parameters belonging
        to a single signature. This usually corresponds to a single
        shader function name.
    """
    myName: str
    myLabel: str
    myShaderName: str | None
    myInputs: list['ShaderParameter']
    myInputFromName: dict[str, 'ShaderParameter'] | None
    myOutputs: list['ShaderParameter']
    myOutputFromName: dict[str, 'ShaderParameter'] | None
    def __init__(self, name: str, label: str, shader_name: str | None, inputs: list['ShaderParameter'], outputs: list['ShaderParameter']) -> None: ...
    def name(self) -> str:
        """ Returns the signature's name.
        """
    def label(self) -> str:
        """ Returns the signature's label.
        """
    def shaderName(self) -> str | None:
        """ Returns the signature's shader function name.
        """
    def inputs(self) -> list['ShaderParameter']:
        """ Returns the list of signature's shader input parameters.
        """
    def connectableInputs(self) -> list['ShaderParameter']:
        """ Returns the list of signature's shader inputs that are connectable.
        """
    def inputNames(self) -> list[str]:
        """ Returns the names of the shader inputs present in this signature.
        """
    def findInput(self, input_name: str) -> ShaderParameter | None:
        """ Returns the shader input parameter of a given name, or None.
        """
    def outputs(self) -> list['ShaderParameter']:
        """ Returns the list of signature's shader output parameters.
        """
    def connectableOutputs(self) -> list['ShaderParameter']:
        """ Returns the list of signature's shader outputs that are connectable.
        """
    def outputNames(self) -> list[str]:
        """ Returns the names of the shader outputs present in this signature.
        """
    def findOutput(self, output_name: str) -> ShaderParameter | None:
        """ Returns the shader output parameter of a given name, or None.
        """
    def getCompatibilityError(self, other: ShaderSignature) -> str | None:
        """ Returns error message if this signature is incomptible with the
            given one. Otherwise, returns None.
        """
    def writeInputsToDialogScript(self, fp: _SupportsWriteStr) -> None:
        """ Write the shader input port definitions to the dialog
            script file given by the file descriptor object parameter.
        """
    def writeOutputsToDialogScript(self, fp: _SupportsWriteStr) -> None:
        """ Write the shader output port definitions to the dialog
            script file given by the file descriptor object parameter.
        """
    def writeSignatureToDialogScript(self, fp: _SupportsWriteStr, default_signature: ShaderSignature | None = None) -> None:
        """ Write the signature information (name, label, input/output types,
            and the shader function name) to the dialog script file
            given by the file descriptor object parameter.
        """
    def updateUIParms(self, is_default_signature: bool) -> None:
        """ Update the node parameters in this signature, depending on
            and according to whether this signature is being designated
            as a default one or not.

            Eg, node parameters in the default signature don't have any
            suffixes, while parameters in non-default signature require
            to have name suffix identifying the signature.
        """
    def buildParmTemplates(self, parm_group: hou.ParmTemplateGroup, default_signature: ShaderSignature | None = None) -> None:
        """ Add Houdini node parameter templates for the shader parameters
            from this signature to the given Houdini ParmTemplateGroup object.

            Essentially, this buids up the HDA parameters.
        """
    def buildInputParmTemplate(self, parm_group: hou.ParmTemplateGroup, input_name: str, default_signature: ShaderSignature | None = None) -> None:
        """ Adds Houdini node parameter template for the shader input parameter
            by the given name to the given Houdini ParmTemplteGroup object.
        """
    def buildOutputParmTemplate(self, parm_group: hou.ParmTemplateGroup, output_name: str, default_signature: ShaderSignature | None = None) -> None:
        """ Adds Houdini node parameter template for the shader input parameter
            by the given name to the given Houdini ParmTemplteGroup object.
        """

class ShaderParameter:
    """ A class that encapsulates all the relevant information about
        a shader parameter. This includes any Houdini traits, 
        such as a node parameter label or an input port name 
        (a resulting HDA may have both of them or just one of them), 
        but also includes aspects relevant to the renderer
        and shader evaluation engine, such as color space metadata.
    """
    myName: str
    myVopType: str
    myParmTemplate: hou.ParmTemplate | None
    myParmFolder: str | None
    myMultiParmMemberNames: list[str]
    myExtraInfos: ShaderParameterExtraInfos | None
    myIsConnectable: bool
    def __init__(self, name: str, vop_type: str, ui_parm: hou.ParmTemplate | None, ui_folder_path: str | None = None, is_connectable: bool = True, extra_infos: ShaderParameterExtraInfos | None = None) -> None: ...
    def vopType(self) -> str:
        """ Returns the shader parameter type, expressed as a VOP data type.
        """
    def name(self) -> str:
        """ Returns the shader parameter name.
        """
    def label(self) -> str:
        """ Returns the shader parameter label.
        """
    def parmTemplate(self) -> hou.ParmTemplate | None:
        """ Returns the Houdini node parameter template that holds the
            value for the shader parameter.
        """
    def parmTemplateFolder(self) -> str | None:
        """ Returns the folder in which the Houdini node parameter should
            appear in.
        """
    def extraInfos(self) -> ShaderParameterExtraInfos | None:
        """ Returns a ShaderParameterExtraInfos object containing
            information about metadata for this shader parameter.
        """
    def isConnectable(self) -> bool:
        """ Returns true if the parameter should have a corresponding 
            node connector port.
        """
    def getSignatureCompatibilityError(self, other: ShaderParameter) -> str | None:
        """ Returns error message if this shader parameter is incompatible 
            with the another one, with respect to being able to describe the 
            same shader parameter in the HDA signature set (ie, the same 
            shader parameter in different signatures belonging to the same set).
            Otherwise, returns None.
        """
    def updateParmTemplates(self, signature_name: str | None) -> None:
        """ Update the node parameter template for this shader parameter,
            depending on and according to whether it belongs to the
            default signature or not (given the signature name parameter).

            Eg, node parameters in the default signature don't have any
            suffixes, while parameters in non-default signature require
            to have name suffix identifying the signature.
        """
    def buildParmTemplates(self, parm_group: hou.ParmTemplateGroup) -> None:
        """ Add Houdini node parameter template for this shader parameter
            to the given Houdini ParmTemplateGroup object.
            This allows users to specify the shader parm value thru node parm.

            Essentially, this buids up the HDA parameters.
        """

class ShaderParameterExtraInfos:
    """ A class encapsulating all the pieces of custom information
        for a single shader parameter.
    """
    myExtraInfos: list['ShaderParameterExtraInfo']
    def __init__(self, infos: list['ShaderParameterExtraInfo'] | None = None) -> None: ...
    def addExtraInfo(self, info: ShaderParameterExtraInfo) -> None:
        """ Adds a new piece of extra info to this object.
        """
    def updateParmTemplates(self, signature_name: str | None, target_parm_name: str) -> None:
        """ Update the metatada information due to a change in a designation
            of the default signature in the signature set, which may have
            caused a change in parameter names, which need to be reflected
            in the references held by the metadata.
        """
    def buildParmTemplates(self, parm_group: hou.ParmTemplateGroup, folder_path: str | None) -> None:
        """ Add Houdini node parameter templates for all extra pieces of info
            held in this class (and relating to a single shader parameter)
            to the given Houdini ParmTemplateGroup object.
            This allows users to specify the metadata values thru node parms.

            Essentially, this buids up the HDA parameters.
        """

class ShaderParameterExtraInfo:
    """ Base class for any extra information for a shader parameter.
    """
    def updateParmTemplates(self, signature_name: str | None, target_parm_name: str) -> None:
        """ Update the extra information due to a change in a designation
            of the default signature in the signature set, which may have
            caused a change in parameter names, which need to be reflected
            in the references held by the info.
        """
    def buildParmTemplates(self, parm_group: hou.ParmTemplateGroup, folder_path: str | None) -> None:
        """ Add Houdini node parameter template for this piece of info
            to the given Houdini ParmTemplateGroup object.
            This allows users to specify the values relevant to this piece 
            of information thru node parms.

            Essentially, this buids up the HDA parameters.
        """

class ShaderParameterExtraParmInfo(ShaderParameterExtraInfo):
    """ An extra info that involves an extra node parameter UI.
    """
    myExtraParmTemplate: hou.ParmTemplate
    myExtraParmOriginalName: str
    def __init__(self, extra_parm_template: hou.ParmTemplate) -> None: ...
    def extraParmTemplate(self) -> hou.ParmTemplate:
        """ Returns the Houdini node parameter template for this piece of
            extra info.
        """
    def extraParmOriginalName(self) -> str:
        """ Returns the original name of the Houdini node parameter template.
        """
    def updateParmTemplates(self, signature_name: str | None, target_parm_name: str) -> None:
        """ Update the extra information due to a change in a designation
            of the default signature in the signature set, which may have
            caused a change in parameter names, which need to be reflected
            in the references held by the info.
        """
    def buildParmTemplates(self, parm_group: hou.ParmTemplateGroup, folder_path: str | None) -> None:
        """ Add Houdini node parameter template for this piece of info
            to the given Houdini ParmTemplateGroup object.
            This allows users to specify the values relevant to this piece 
            of information thru node parms.

            Essentially, this buids up the HDA parameters.
        """

class ShaderParameterExtraMetadataInfo(ShaderParameterExtraParmInfo):
    """ A class representing a piece of metadata for shader parameter.

        In HDA, metadata is represented by a spare parameter that specifies
        metadata value, and parameter tags are used to link it to the desired
        HDA parameter corresponding to a formal shader parameter.

        Shader translators resolve the values and author them as metadata
        on the shader parameter, ready for renderer's consumption.
    """
    myMetadataKeyPath: str
    def __init__(self, keypath: str, meta_parm_template: hou.ParmTemplate) -> None: ...
    def metadataKeyPath(self) -> str:
        """ Returns the metadata name (or colon-separated dictionary path)
            at which the shader translator should author the metadata value
            for the renderer's consumption.
        """
    def metaParmTemplate(self) -> hou.ParmTemplate:
        """ Returns the Houdini node parameter template for this piece of
            metadata.
        """
    def updateParmTemplates(self, signature_name: str | None, target_parm_name: str) -> None:
        """ Update the metatada information due to a change in a designation
            of the default signature in the signature set, which may have
            caused a change in parameter names, which need to be reflected
            in the references held by the metadata.
        """

class ShaderParameterExtraMenuInfo(ShaderParameterExtraParmInfo):
    """ A class representing an extra node parameter (a menu) that controlls 
        the value of the main shader parameter.
    """
    def __init__(self, menu_parm_template: hou.ParmTemplate) -> None: ...
    def menuParmTemplate(self) -> hou.ParmTemplate:
        """ Returns the Houdini node parameter template that controlls 
            the value of the main shader parameter.
        """

TMP_FILE_PREFIX: str
TOOL_PROLOGUE_TEMPLATE: str
TOOL_SCRIPT_TEMPLATE: str
TOOL_EPILOGUE_TEMPLATE: str
