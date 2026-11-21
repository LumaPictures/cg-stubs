from collections.abc import Iterable, Sequence
from typing import TypeAlias, overload

from typing_extensions import TypeVar

from husd.typeutils import _SdfValue
from pxr import Sdf, Usd, UsdShade

_T = TypeVar("_T")
_D = TypeVar("_D", default=None)

_TimeCode: TypeAlias = Usd.TimeCode | float
_SdfPath: TypeAlias = Sdf.Path | str
_StdSource: TypeAlias = UsdShade.Input | UsdShade.Output
# A preview input's value: an attribute's, maybe scaled or offset.
_PreviewValue: TypeAlias = _SdfValue | tuple[float, ...]
# A texture scale or offset: an attribute's value, or the one a translator gives.
_TexVec: TypeAlias = _SdfValue | Sequence[float]

class UsdShaderInputInfo:
    myName: str
    myType: Sdf.ValueTypeName
    myMainShaderInputName: str | None
    myValue: _PreviewValue | None
    myTexFile: _SdfValue | None
    myValueStdSrc: _StdSource | None
    myTexFileStdSrc: _StdSource | None
    myValuePrimvarName: str | None
    myTexWrapS: str | None
    myTexWrapT: str | None
    myTexScale: _TexVec | None
    myTexOffset: _TexVec | None
    myTexAutoScaleFlag: bool
    myTexColorSpace: str | None
    myValueOpacityInputName: str | None
    def __init__(
        self,
        main_shader_input_name: str | None,
        input_type: Sdf.ValueTypeName,
        input_name: str,
        value: _PreviewValue | None = ...,
        value_src: _StdSource | None = ...,
        texture_file: _SdfValue | None = ...,
        texture_src: _StdSource | None = ...,
        tex_wrap_s: str | None = ...,
        tex_wrap_t: str | None = ...,
        tex_scale: _TexVec | None = ...,
        tex_offset: _TexVec | None = ...,
        tex_color_space: str | None = ...,
        val_opacity_input_name: str | None = ...,
    ) -> None: ...

def evalAttribute(attrib: Usd.Property | None, usd_time_code: _TimeCode) -> _SdfValue | None: ...
def standardAttributeSource(attrib: Usd.Property | None) -> _StdSource | None: ...
def findAttribute(usd_shader: UsdShade.Shader, tag_name: str | None) -> Usd.Property | None: ...
def findAttributeValue(
    usd_shader: UsdShade.Shader, usd_time_code: _TimeCode, tag_name: str | None, default_value: _D = ...
) -> _SdfValue | _D | None: ...
# A tuple-like value is scaled (offset) per component.
def scaledValue(value: _T, scale: float | None) -> _T | float | tuple[float, ...]: ...
def offsetValue(value: _T, offset: float | None) -> _T | float | tuple[float, ...]: ...
def usdPreviewShaderInputInfoFromOGLTags(
    usd_main_shader: UsdShade.Shader,
    usd_time_code: _TimeCode,
    preview_input_name: str,
    preview_input_type: Sdf.ValueTypeName,
    val_tag: str | None,
    val_scale_tag: str | None,
    val_default: float | tuple[float, ...],
    use_texture_tag: str | None,
    texture_tag: str | None,
    wrap_s_tag: str | None,
    wrap_t_tag: str | None,
    val_scale: float | None = ...,
    val_offset: float | None = ...,
    val_opacity_input_name: str | None = ...,
    use_texture_alpha_for_opacity_tag: str | None = ...,
    tex_scale_val_or_tag: str | float | Sequence[float] | None = ...,
    tex_offset_val_or_tag: str | float | Sequence[float] | None = ...,
    tex_color_space: str | None = ...,
) -> UsdShaderInputInfo | None: ...
@overload
def textureWrapValue(wrap_choice: str) -> str: ...
@overload
def textureWrapValue(wrap_choice: None) -> None: ...
@overload
def textureWrapValue(wrap_choice: str | None) -> str | None: ...
# A scalar value is repeated; a tuple-like one is padded with def_comp_val.
def textureVecValue(vec_size: int, value: _T, def_comp_val: float) -> tuple[_T, ...] | tuple[float, ...] | None: ...

class PreviewShaderTranslatorHelper:
    myUsdStage: Usd.Stage
    myUsdMaterial: UsdShade.Material
    myUsdTimeCode: _TimeCode
    def __init__(self, usd_stage: Usd.Stage, usd_material_path: _SdfPath, usd_time_code: _TimeCode) -> None: ...
    def createAndConnectUsdTerminalPreviewShader(self, usd_main_shader_path: _SdfPath) -> None: ...
    def deleteAndDisconnectUsdTerminalPreviewShader(self) -> None: ...
    def updateUsdPreviewShaderAttributes(self, usd_preview_shader_path: _SdfPath, usd_main_shader_path: _SdfPath) -> None: ...
    def createUsdShader(self, usd_shader_path: _SdfPath) -> UsdShade.Shader: ...
    def createUsdPreviewShader(self, usd_main_shader: UsdShade.Shader, parent_path: Sdf.Path) -> UsdShade.Shader: ...
    def createAndConnectUsdTextureShader(
        self,
        shader_attrib: Usd.Attribute,
        time_code: _TimeCode,
        attrib_value: _PreviewValue | None,
        tex_auto_scale_flag: bool,
        texture_file: _SdfValue | None,
        tex_wrap_s: str | None,
        tex_wrap_t: str | None,
        tex_scale: _TexVec | None,
        tex_offset: _TexVec | None,
        val_opacity_input_name: str | None,
        color_space: str | None,
        uv_reader_shader: UsdShade.Shader,
    ) -> UsdShade.Shader: ...
    def createAndConnectPrimvarReaderShader(
        self,
        shader_attrib: Usd.Attribute,
        time_code: _TimeCode,
        primvar_name: str,
        primvar_sdf_type: Sdf.ValueTypeName,
        fallback_value: _PreviewValue | None,
    ) -> None: ...
    def createUVReaderShader(self, parent_path: Sdf.Path, prim_name: str, time_code: _TimeCode) -> UsdShade.Shader: ...
    def connectUsdMaterialOutput(self, usd_shader: UsdShade.Shader) -> None: ...
    def usdPreviewShaderInputInfo(
        self,
        usd_main_shader: UsdShade.Shader,
        preview_input_name: str,
        preview_input_type: Sdf.ValueTypeName,
        info: UsdShaderInputInfo | None,
    ) -> UsdShaderInputInfo | None: ...
    def usdPreviewShaderInputInfos(self, usd_main_shader: UsdShade.Shader) -> list[UsdShaderInputInfo]: ...
    def createUsdPreviewShaderInputs(self, usd_shader: UsdShade.Shader, input_infos: Iterable[UsdShaderInputInfo]) -> None: ...
    def deleteUsdPreviewShaderInputs(self, usd_shader: UsdShade.Shader) -> None: ...
    def connectUsdPreviewShaderInput(self, usd_attrib: Usd.Attribute, usd_src: _StdSource) -> None: ...

class PreviewShaderTranslator:
    def matchesRenderContext(self, render_context: str) -> bool: ...
    def createMaterialPreviewShader(
        self, usd_stage: Usd.Stage, usd_material_path: _SdfPath, usd_shader_path: _SdfPath, usd_time_code: _TimeCode
    ) -> None: ...
    def deleteMaterialPreviewShader(self, usd_stage: Usd.Stage, usd_material_path: _SdfPath) -> None: ...
    def updateMaterialPreviewShaderParameters(
        self, usd_stage: Usd.Stage, usd_main_shader_path: _SdfPath, usd_time_code: _TimeCode
    ) -> None: ...
    def previewShaderTranslatorHelper(
        self, usd_stage: Usd.Stage, usd_material_path: _SdfPath, usd_time_code: _TimeCode
    ) -> PreviewShaderTranslatorHelper: ...
