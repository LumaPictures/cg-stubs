from collections.abc import Collection
from typing import TypeAlias

import hou
from pxr import Sdf, Usd, UsdLux, UsdShade

from .mtlxshadertranslator import MaterialXPreviewShaderTranslator as PreviewTranslatorBase
from .mtlxshadertranslator import MaterialXPreviewShaderTranslatorHelper as PreviewHelperBase
from .mtlxshadertranslator import MaterialXShaderTranslator as TranslatorBase
from .mtlxshadertranslator import MaterialXShaderTranslatorHelper as HelperBase
from .shadertranslator import RampParmTranslator as RampParmTranslatorBase

_UsdShaderSchema: TypeAlias = UsdShade.Shader | UsdShade.NodeGraph | UsdLux.LightFilter

RAMP_VARIABLE_NAME: str

class RampParmTranslator(RampParmTranslatorBase):
    def __init__(self, parm_tuple: hou.ParmTuple) -> None: ...
    def createBasisAttrib(self, usd_shader: _UsdShaderSchema) -> Usd.Attribute: ...
    def rampBasisMap(self) -> dict[hou.EnumValue[hou.rampBasis], str]: ...
    def rampBasisValue(self, ramp_val: hou.Ramp) -> list[str | None]: ...
    def setCustomDataOnAttrib(self, usd_attrib: Usd.Attribute) -> None: ...

class KarmaShaderTranslatorHelper(HelperBase):
    def __init__(
        self,
        translator_id: int,
        usd_stage: Usd.Stage,
        usd_material_path: str | None,
        usd_time_code: Usd.TimeCode,
    ) -> None: ...
    def createUsdShaderAttributes(self, shader_node: hou.VopNode, usd_shader: _UsdShaderSchema) -> None: ...
    def updateUsdShaderAttributes(
        self,
        shader_node: hou.VopNode,
        shader_node_parameter_names: Collection[str],
        usd_shader_path: str | Sdf.Path,
    ) -> None: ...
    def usdShaderInputName(self, shader_node: hou.VopNode, shader_node_input_name: str | None) -> str: ...
    def usdShaderOutputName(self, shader_node: hou.VopNode, shader_node_output_name: str | None) -> str: ...
    def sdfTypeFromNodeOutput(
        self, shader_node: hou.VopNode, shader_node_output_name: str | None
    ) -> Sdf.ValueTypeName: ...
    def createKarmaRampShaderAttributes(self, shader_node: hou.VopNode, usd_shader: _UsdShaderSchema) -> None: ...
    def updateKarmaRampShaderAttributes(
        self, shader_node: hou.VopNode, usd_shader_path: str | Sdf.Path
    ) -> None: ...
    def rampParameterTranslator(self, parm_tuple: hou.ParmTuple) -> RampParmTranslator: ...

class KarmaPreviewShaderTranslatorHelper(PreviewHelperBase):
    def __init__(
        self,
        usd_stage: Usd.Stage,
        usd_material_path: str | Sdf.Path,
        usd_time_code: Usd.TimeCode | float,
    ) -> None: ...

class KarmaShaderTranslator(TranslatorBase):
    def __init__(self) -> None: ...
    def matchesRenderMask(self, render_mask: str) -> bool: ...
    def shaderTranslatorHelper(
        self,
        translator_id: int,
        usd_stage: Usd.Stage,
        usd_material_path: str | None,
        usd_time_code: Usd.TimeCode,
    ) -> KarmaShaderTranslatorHelper: ...

class KarmaPreviewShaderTranslator(PreviewTranslatorBase):
    def __init__(self) -> None: ...
    def matchesRenderContext(self, render_context: str) -> bool: ...
    def previewShaderTranslatorHelper(
        self,
        usd_stage: Usd.Stage,
        usd_material_path: str | Sdf.Path,
        usd_time_code: Usd.TimeCode | float,
    ) -> KarmaPreviewShaderTranslatorHelper: ...
