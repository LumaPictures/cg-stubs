# Houdini stubs generated from Houdini 22.0.466

import hou
import re
from . import shaderutils as shaderutils
from .karmautils import AOV_CHANNELPREFIX as AOV_CHANNELPREFIX, AOV_FILTER as AOV_FILTER, AOV_FORMAT as AOV_FORMAT, AOV_NAME as AOV_NAME
from .previewshadertranslator import PreviewShaderTranslator as PreviewTranslatorBase, PreviewShaderTranslatorHelper as PreviewHelperBase, UsdShaderInputInfo as UsdShaderInputInfo
from .shadertranslator import ShaderTranslator as TranslatorBase, ShaderTranslatorHelper as HelperBase, SimpleParmTranslator as SimpleParmTranslatorBase
from collections.abc import Sequence
from pxr import Sdf, Usd, UsdShade

from typing import TypeAlias
from pxr import UsdLux
from typing import TypeAlias
_UsdShaderSchema: TypeAlias = UsdShade.Shader | UsdShade.NodeGraph | UsdLux.LightFilter
_UsdConnectable: TypeAlias = UsdShade.ConnectableAPI | UsdShade.Shader | UsdShade.NodeGraph | UsdLux.LightFilter
class MaterialXSimpleParmTranslator(SimpleParmTranslatorBase):
    def __init__(self, parm_tuple: hou.ParmTuple) -> None: ...
    def attribName(self) -> str:
        """ Returns the name of the attribute to create for this parameter.
        """

class UsdShaderInputInfoMap:
    """ Translation of a shader happens in a few stages: authoring a USD shader 
        primitive, determining which VOP node to continue the traversal on, 
        and on which USD input the traversal should make a connection.
        This map class passes the relvant info between the stages to ensure 
        that the complete translation is correct.
    """
    myUsdInputInfoMap: dict[tuple[hou.VopNode, str], tuple[UsdShade.Shader, str, Sdf.ValueTypeName]]
    myUsdExtraInputsMap: dict[Usd.Prim, tuple[str, Sequence[str]]]
    def __init__(self) -> None: ...
    def setInfo(self, shader_node: hou.VopNode, input_name: str, usd_shader: UsdShade.Shader, usd_shader_input_name: str, usd_shader_input_type: Sdf.ValueTypeName, usd_shader_extra_input_names: Sequence[str] | None = None) -> None:
        """ Adds an info that links a VOP node input to USD shader prim input.
            The interpretation is that translating the VOP wire connection 
            feeding into the given VOP input should result in authoring 
            a USD connection that feeds into the given USD shader input.
            The extra inputs parameter, if given, contains the names
            of additional USD inputs that should have the same connection 
            as the given main USD shader input.
        """
    def connectionInfo(self, shader_node: hou.VopNode, wire: hou.NodeConnection) -> tuple[UsdShade.Shader | None, str | None, Sdf.ValueTypeName | None, hou.VopNode | None, str]:
        """ Returns the info about the next step in the translation traversal.
            The returned tuple is (usd_shader, usd_input_name, usd_input_type,
            vop_node, vop_output_name). This tuple indicates that the
            translator should translate the vop_node and its output to a new 
            usd prim, which should be fed into the given usd shader's input.
        """
    def extraInputs(self, usd_shader: UsdShade.Shader) -> tuple[str, Sequence[str]] | tuple[None, None]:
        """ Returns a list of extra inputs that need to be connected
            after the shader translation.
            The tuple is (main_input, extra_inputs).
        """

class MaterialXShaderTranslatorHelper(HelperBase):
    myLegacyShaderInputInfoMap: UsdShaderInputInfoMap
    def __init__(self, translator_id: int, usd_stage: Usd.Stage, usd_material_path: str | None, usd_time_code: Usd.TimeCode) -> None:
        """ Saves the common pieces of data as member variables.
        """
    def usdShaderAssetOrID(self, shader_node: hou.VopNode) -> str: ...
    def createAndConnectUsdTerminalShader(self, shader_node: hou.VopNode, requested_shader_type: hou.EnumValue[hou.shaderType], shader_node_output_name: str) -> Sdf.Path | None:
        """ Creates and configures a USD shader primitive based on the
            given Houdini node, and links it to the USD material primitive 

            Returns the path to the terminal output attribute of the material 
            primitive to which the terminal shader has been connected.
        """
    def createUsdShader(self, shader_node: hou.VopNode, shader_node_output_name: str, usd_parent_connectable: _UsdConnectable, usd_shader_prim_name: str | None = None) -> _UsdShaderSchema:
        """ Creates and configures a single USD shader primitive 
            based on the given Houdini shader node.
            Returns a USD shader schema for the created USD primitive.
        """
    def postCreateUsdShaderChain(self, shader_node: hou.VopNode, shader_node_output_name: str, usd_shader_output: UsdShade.Output) -> None:
        """ This method is run after the shader chain has been authored
            based on the given shader VOP node for its given output.
        """
    def inputConnectionInfo(self, usd_shader: _UsdShaderSchema, shader_node: hou.VopNode, wire: hou.NodeConnection) -> tuple[_UsdShaderSchema | None, str | None, Sdf.ValueTypeName | None, hou.VopNode | None, str | None]:
        """ Returns a tuple describing how to continue the traversal
            of the input connection given by the wire.
        """
    def usdShaderInputName(self, shader_node: hou.VopNode, shader_node_input_name: str | None) -> str:
        """ Returns the name of an input attribute of the USD shader prim, 
            given the shader node and its input name.
        """
    def simpleParameterTranslator(self, parm_tuple: hou.ParmTuple) -> MaterialXSimpleParmTranslator:
        """ Returns a translator for simple parameters.
        """
    def createUsdVisualizerShader(self, usd_shader_output: UsdShade.Output, visualizer_node: hou.VopNode | None) -> Sdf.Path:
        """ Creates a USD shader primitive that visualizes the value 
            of a given output of another (pattern/utility) shader.
        """
    CHANNEL_COUNT_FROM_VOP_TYPE: dict[str, int]
    MTLX_TYPE_FROM_VOP_TYPE: dict[str, str]
    INDEX_FROM_CHANNEL: dict[str, int]
    CONST_FROM_CHANNEL: dict[str, float]

class MaterialXPreviewShaderTranslatorHelper(PreviewHelperBase):
    def __init__(self, usd_stage: Usd.Stage, usd_material_path: str | Sdf.Path, usd_time_code: Usd.TimeCode | float) -> None: ...
    def usdPreviewShaderInputInfo(self, usd_main_shader: UsdShade.Shader, preview_input_name: str, preview_input_type: Sdf.ValueTypeName, info: UsdShaderInputInfo | None) -> UsdShaderInputInfo | None:
        """ Base class relies on shader VOP node parameter tags.
            MaterialX VOPs have tagged color parameters (eg, ogl_diff'), 
            but do not have texture file parameters to tag (eg, 'ogl_tex1').
            We provide textue info here, based on USD shader input connections.
        """

class MaterialXShaderTranslator(TranslatorBase):
    """ Translates MaterialX Houdini shader nodes into USD shader primitives.
        See husd.shadertranslator.ShaderTranslator for details.
    """
    myPattern: re.Pattern[str]
    def __init__(self) -> None: ...
    def matchesRenderMask(self, render_mask: str) -> bool: ...
    def shaderTranslatorHelper(self, translator_id: int, usd_stage: Usd.Stage, usd_material_path: str | None, usd_time_code: Usd.TimeCode) -> MaterialXShaderTranslatorHelper: ...

class MaterialXPreviewShaderTranslator(PreviewTranslatorBase):
    """ Translates MaterialX USD shader into USD standard preview shader.
    """
    def __init__(self) -> None: ...
    def matchesRenderContext(self, render_context: str) -> bool: ...
    def previewShaderTranslatorHelper(self, usd_stage: Usd.Stage, usd_material_path: str | Sdf.Path, usd_time_code: Usd.TimeCode | float) -> MaterialXPreviewShaderTranslatorHelper: ...
