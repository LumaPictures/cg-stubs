import re
from collections.abc import Sequence
from typing import TypeAlias

import hou
from pxr import Sdf, Usd, UsdLux, UsdShade

from .previewshadertranslator import PreviewShaderTranslator as PreviewTranslatorBase
from .previewshadertranslator import PreviewShaderTranslatorHelper as PreviewHelperBase
from .previewshadertranslator import UsdShaderInputInfo
from .shadertranslator import ShaderTranslator as TranslatorBase
from .shadertranslator import ShaderTranslatorHelper as HelperBase
from .shadertranslator import SimpleParmTranslator as SimpleParmTranslatorBase

_UsdShaderSchema: TypeAlias = UsdShade.Shader | UsdShade.NodeGraph | UsdLux.LightFilter
_UsdConnectable: TypeAlias = UsdShade.ConnectableAPI | UsdShade.Shader | UsdShade.NodeGraph | UsdLux.LightFilter

class MaterialXSimpleParmTranslator(SimpleParmTranslatorBase):
    def __init__(self, parm_tuple: hou.ParmTuple) -> None: ...
    def attribName(self) -> str: ...

class UsdShaderInputInfoMap:
    myUsdInputInfoMap: dict[tuple[hou.VopNode, str], tuple[UsdShade.Shader, str, Sdf.ValueTypeName]]
    myUsdExtraInputsMap: dict[Usd.Prim, tuple[str, Sequence[str]]]
    def __init__(self) -> None: ...
    def setInfo(
        self,
        shader_node: hou.VopNode,
        input_name: str,
        usd_shader: UsdShade.Shader,
        usd_shader_input_name: str,
        usd_shader_input_type: Sdf.ValueTypeName,
        usd_shader_extra_input_names: Sequence[str] | None = ...,
    ) -> None: ...
    def connectionInfo(
        self, shader_node: hou.VopNode, wire: hou.NodeConnection
    ) -> tuple[UsdShade.Shader | None, str | None, Sdf.ValueTypeName | None, hou.VopNode | None, str]: ...
    def extraInputs(
        self, usd_shader: UsdShade.Shader
    ) -> tuple[str, Sequence[str]] | tuple[None, None]: ...

class MaterialXShaderTranslatorHelper(HelperBase):
    myLegacyShaderInputInfoMap: UsdShaderInputInfoMap
    CHANNEL_COUNT_FROM_VOP_TYPE: dict[str, int]
    MTLX_TYPE_FROM_VOP_TYPE: dict[str, str]
    INDEX_FROM_CHANNEL: dict[str, int]
    CONST_FROM_CHANNEL: dict[str, float]
    def __init__(
        self,
        translator_id: int,
        usd_stage: Usd.Stage,
        usd_material_path: str | None,
        usd_time_code: Usd.TimeCode,
    ) -> None: ...
    def usdShaderAssetOrID(self, shader_node: hou.VopNode) -> str: ...
    def createAndConnectUsdTerminalShader(
        self,
        shader_node: hou.VopNode,
        requested_shader_type: hou.EnumValue[hou.shaderType],
        shader_node_output_name: str,
    ) -> Sdf.Path | None: ...
    def createUsdShader(
        self,
        shader_node: hou.VopNode,
        shader_node_output_name: str,
        usd_parent_connectable: _UsdConnectable,
        usd_shader_prim_name: str | None = ...,
    ) -> _UsdShaderSchema: ...
    def postCreateUsdShaderChain(
        self,
        shader_node: hou.VopNode,
        shader_node_output_name: str,
        usd_shader_output: UsdShade.Output,
    ) -> None: ...
    def inputConnectionInfo(
        self,
        usd_shader: _UsdShaderSchema,
        shader_node: hou.VopNode,
        wire: hou.NodeConnection,
    ) -> tuple[
        _UsdShaderSchema | None,
        str | None,
        Sdf.ValueTypeName | None,
        hou.VopNode | None,
        str | None,
    ]: ...
    def usdShaderInputName(self, shader_node: hou.VopNode, shader_node_input_name: str | None) -> str: ...
    def simpleParameterTranslator(self, parm_tuple: hou.ParmTuple) -> MaterialXSimpleParmTranslator: ...
    def createUsdVisualizerShader(
        self, usd_shader_output: UsdShade.Output, visualizer_node: hou.VopNode | None
    ) -> Sdf.Path: ...

class MaterialXPreviewShaderTranslatorHelper(PreviewHelperBase):
    def __init__(
        self,
        usd_stage: Usd.Stage,
        usd_material_path: str | Sdf.Path,
        usd_time_code: Usd.TimeCode | float,
    ) -> None: ...
    def usdPreviewShaderInputInfo(
        self,
        usd_main_shader: UsdShade.Shader,
        preview_input_name: str,
        preview_input_type: Sdf.ValueTypeName,
        info: UsdShaderInputInfo | None,
    ) -> UsdShaderInputInfo | None: ...

class MaterialXShaderTranslator(TranslatorBase):
    myPattern: re.Pattern[str]
    def __init__(self) -> None: ...
    def matchesRenderMask(self, render_mask: str) -> bool: ...
    def shaderTranslatorHelper(
        self,
        translator_id: int,
        usd_stage: Usd.Stage,
        usd_material_path: str | None,
        usd_time_code: Usd.TimeCode,
    ) -> MaterialXShaderTranslatorHelper: ...

class MaterialXPreviewShaderTranslator(PreviewTranslatorBase):
    def __init__(self) -> None: ...
    def matchesRenderContext(self, render_context: str) -> bool: ...
    def previewShaderTranslatorHelper(
        self,
        usd_stage: Usd.Stage,
        usd_material_path: str | Sdf.Path,
        usd_time_code: Usd.TimeCode | float,
    ) -> MaterialXPreviewShaderTranslatorHelper: ...
