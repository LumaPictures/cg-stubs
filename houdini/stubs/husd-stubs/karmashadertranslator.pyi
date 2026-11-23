import hou
from . import shaderutils as shaderutils
from .mtlxshadertranslator import MaterialXPreviewShaderTranslator as PreviewTranslatorBase, MaterialXPreviewShaderTranslatorHelper as PreviewHelperBase, MaterialXShaderTranslator as TranslatorBase, MaterialXShaderTranslatorHelper as HelperBase
from .shadertranslator import RampParmTranslator as RampParmTranslatorBase
from collections.abc import Collection
from pxr import Sdf, Usd as Usd

from typing import TypeAlias
from pxr import UsdLux
from pxr import UsdShade
from typing import TypeAlias
_UsdShaderSchema: TypeAlias = UsdShade.Shader | UsdShade.NodeGraph | UsdLux.LightFilter
RAMP_VARIABLE_NAME: str

class RampParmTranslator(RampParmTranslatorBase):
    def __init__(self, parm_tuple: hou.ParmTuple) -> None: ...
    def createBasisAttrib(self, usd_shader: _UsdShaderSchema) -> Usd.Attribute:
        """ Creates an input attribute (on the given USD shader schema)
            for the ramp basis component.
        """
    def rampBasisMap(self) -> dict[hou.EnumValue[hou.rampBasis], str]:
        """ Returns a map from enumerated values of ramp interpolation
            to the string names of such interpolation.
        """
    def rampBasisValue(self, ramp_val: hou.Ramp) -> list[str | None]:
        """ Returns the value of the ramp basis given the ramp.
        """
    def setCustomDataOnAttrib(self, usd_attrib: Usd.Attribute) -> None:
        """ Sets custom data on every ramp-related parameter that ties it to
            all the other ramp parameters so that we can create the correct
            parameter interface for the ramp.
        """

class KarmaShaderTranslatorHelper(HelperBase):
    def __init__(self, translator_id: int, usd_stage: Usd.Stage, usd_material_path: str | None, usd_time_code: Usd.TimeCode) -> None:
        """ Saves the common pieces of data as member variables.
        """
    def createUsdShaderAttributes(self, shader_node: hou.VopNode, usd_shader: _UsdShaderSchema) -> None:
        """ Creates and sets the shader input parameter attributes
            on the USD shader, given the Houdini shader node.
        """
    def updateUsdShaderAttributes(self, shader_node: hou.VopNode, shader_node_parameter_names: Collection[str], usd_shader_path: str | Sdf.Path) -> None:
        """ Re-translate the shader node parameters into USD shader attributes.
        """
    def usdShaderInputName(self, shader_node: hou.VopNode, shader_node_input_name: str | None) -> str:
        """ Returns the name of an input attribute of the USD shader prim, 
            given the shader node and its input name.
        """
    def usdShaderOutputName(self, shader_node: hou.VopNode, shader_node_output_name: str | None) -> str:
        """ Returns the name of an output attribute on the USD shader prim,
            given the shader node and its output name.
        """
    def sdfTypeFromNodeOutput(self, shader_node: hou.VopNode, shader_node_output_name: str | None) -> Sdf.ValueTypeName:
        """ Returns the USD type given the node output.
        """
    def createKarmaRampShaderAttributes(self, shader_node: hou.VopNode, usd_shader: _UsdShaderSchema) -> None:
        """ Creates and sets the ramp shader input parameter attributes
            on the USD shader, given the Houdini shader node.
        """
    def updateKarmaRampShaderAttributes(self, shader_node: hou.VopNode, usd_shader_path: str | Sdf.Path) -> None:
        """ Updates the ramp shader input parameter attributes
            on the USD shader, given the Houdini shader node.
        """
    def rampParameterTranslator(self, parm_tuple: hou.ParmTuple) -> RampParmTranslator:
        """ Returns a translator for ramp parameters which overrides specific 
            methods of basic class functionality
        """

class KarmaPreviewShaderTranslatorHelper(PreviewHelperBase):
    def __init__(self, usd_stage: Usd.Stage, usd_material_path: str | Sdf.Path, usd_time_code: Usd.TimeCode | float) -> None: ...

class KarmaShaderTranslator(TranslatorBase):
    """ Translates Karma USD shader.
    """
    def __init__(self) -> None: ...
    def matchesRenderMask(self, render_mask: str) -> bool: ...
    def shaderTranslatorHelper(self, translator_id: int, usd_stage: Usd.Stage, usd_material_path: str | None, usd_time_code: Usd.TimeCode) -> KarmaShaderTranslatorHelper: ...

class KarmaPreviewShaderTranslator(PreviewTranslatorBase):
    """ Translates MaterialX USD shader into USD standard preview shader.
    """
    def __init__(self) -> None: ...
    def matchesRenderContext(self, render_context: str) -> bool: ...
    def previewShaderTranslatorHelper(self, usd_stage: Usd.Stage, usd_material_path: str | Sdf.Path, usd_time_code: Usd.TimeCode | float) -> KarmaPreviewShaderTranslatorHelper: ...
