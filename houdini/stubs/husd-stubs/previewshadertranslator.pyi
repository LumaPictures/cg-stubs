import typing
from . import shaderutils as shaderutils
from collections.abc import Iterable, Sequence
from husd.typeutils import _SdfValue
from pxr import Sdf, Usd, UsdShade

from typing import TypeAlias
from typing import TypeVar
from typing import TypeAlias
from typing_extensions import TypeVar
_T = TypeVar('_T')
_D = TypeVar('_D', default=None)
_TimeCode: TypeAlias = Usd.TimeCode | float
_SdfPath: TypeAlias = Sdf.Path | str
_StdSource: TypeAlias = UsdShade.Input | UsdShade.Output
_PreviewValue: TypeAlias = _SdfValue | tuple[float, ...]
_TexVec: TypeAlias = _SdfValue | Sequence[float]
class UsdShaderInputInfo:
    """ A class encapsulating information about a USD shader input setup
        to be authored. Eg, the value to be used for the input, and
        a texture file to drive the input value (if applicable), etc.
        This info is used to author input attribute value for the shader,
        create UV Texutre or Primvar Reader primitives that feed into it, etc.
    """
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
    def __init__(self, main_shader_input_name: str | None, input_type: Sdf.ValueTypeName, input_name: str, value: _PreviewValue | None = None, value_src: _StdSource | None = None, texture_file: _SdfValue | None = None, texture_src: _StdSource | None = None, tex_wrap_s: str | None = None, tex_wrap_t: str | None = None, tex_scale: _TexVec | None = None, tex_offset: _TexVec | None = None, tex_color_space: str | None = None, val_opacity_input_name: str | None = None) -> None:
        """ Packages the info into an object of this class.
        """

def evalAttribute(attrib: Usd.Property | None, usd_time_code: _TimeCode) -> _SdfValue | None:
    """ Returns the attribute's value.
    """
def standardAttributeSource(attrib: Usd.Property | None) -> _StdSource | None:
    """ Returns a standard USD input/output source for the given attribute, 
        if any. Eg, Material/NodeGraph input or USD primvar reader's output.
    """
def findAttribute(usd_shader: UsdShade.Shader, tag_name: str | None) -> Usd.Property | None:
    """ Returns a USD attribute that has the given tag, if found; else None.
    """
def findAttributeValue(usd_shader: UsdShade.Shader, usd_time_code: _TimeCode, tag_name: str | None, default_value: _D | None = None) -> _SdfValue | _D | None:
    """ Returns a value of a node parameter that has the given tag.
    """
def scaledValue(value: _T, scale: float | None) -> _T | float | tuple[float, ...]:
    """ Returns the scaled value, if applicable.
    """
def offsetValue(value: _T, offset: float | None) -> _T | float | tuple[float, ...]:
    """ Returns the ofset value, if applicable.
    """
def usdPreviewShaderInputInfoFromOGLTags(usd_main_shader: UsdShade.Shader, usd_time_code: _TimeCode, preview_input_name: str, preview_input_type: Sdf.ValueTypeName, val_tag: str | None, val_scale_tag: str | None, val_default: float | tuple[float, ...], use_texture_tag: str | None, texture_tag: str | None, wrap_s_tag: str | None, wrap_t_tag: str | None, val_scale: float | None = None, val_offset: float | None = None, val_opacity_input_name: str | None = None, use_texture_alpha_for_opacity_tag: str | None = None, tex_scale_val_or_tag: str | float | Sequence[float] | None = None, tex_offset_val_or_tag: str | float | Sequence[float] | None = None, tex_color_space: str | None = None) -> UsdShaderInputInfo | None:
    """ Returns a UsdShaderInputInfo object that describes a USD shader input
        to be created for the given set of attribute metadata tags.

        The function uses the given USD attribute tags to find the main shader
        attributes that can provide information about the USD shader input.

        May return None, if no suitable USD attribute could be found,
        meaning that no meaningful USD preview shader input attribute 
        can be authored for the given metadata tags.
    """
@typing.overload
def textureWrapValue(wrap_choice: str) -> str: ...
@typing.overload
def textureWrapValue(wrap_choice: None) -> None: ...
@typing.overload
def textureWrapValue(wrap_choice: str | None) -> str | None: ...
def textureVecValue(vec_size: int, value: _T, def_comp_val: float) -> tuple[_T, ...] | tuple[float, ...] | None:
    """ Returns a vector of the given size, whose components are the same 
        as the given value.  If value is a scalar, then all tuple components 
        are set to that value, else given default value is used for missing 
        components.
    """

class PreviewShaderTranslatorHelper:
    """ A class that authors a USD standard preview surface shader primitive
        for a given shader VOP node. 
        
        This allows approximating a render-specific shader in other renderers
        if they support the USD Preview Surface standard,
        (eg, Storm or Houdini GL, which do support preview shaders)
    """
    myUsdStage: Usd.Stage
    myUsdMaterial: UsdShade.Material
    myUsdTimeCode: _TimeCode
    def __init__(self, usd_stage: Usd.Stage, usd_material_path: _SdfPath, usd_time_code: _TimeCode) -> None:
        """ Saves the common pieces of data as member variables.
        """
    def createAndConnectUsdTerminalPreviewShader(self, usd_main_shader_path: _SdfPath) -> None:
        """ Creates a USD universal preview surface shader from the given 
            render-specific shader, sets its input attributes, 
            and connects it to the output of a USD material passed in 
            constructor.
        """
    def deleteAndDisconnectUsdTerminalPreviewShader(self) -> None:
        """ Deletes the USD universal preview shader from the material.
        """
    def updateUsdPreviewShaderAttributes(self, usd_preview_shader_path: _SdfPath, usd_main_shader_path: _SdfPath) -> None:
        """ Re-translate the main shader attributes to the preview shader ones.
        """
    def createUsdShader(self, usd_shader_path: _SdfPath) -> UsdShade.Shader:
        """ Creates a shader primitive, and tags it with an auto-created
            metadata flag.
        """
    def createUsdPreviewShader(self, usd_main_shader: UsdShade.Shader, parent_path: Sdf.Path) -> UsdShade.Shader:
        """ Creates a standard USD surface preview shader primitive.
        """
    def createAndConnectUsdTextureShader(self, shader_attrib: Usd.Attribute, time_code: _TimeCode, attrib_value: _PreviewValue | None, tex_auto_scale_flag: bool, texture_file: _SdfValue | None, tex_wrap_s: str | None, tex_wrap_t: str | None, tex_scale: _TexVec | None, tex_offset: _TexVec | None, val_opacity_input_name: str | None, color_space: str | None, uv_reader_shader: UsdShade.Shader) -> UsdShade.Shader:
        """ Creates a texture shader primitive and connects its output
            to the given shader attribute.
        """
    def createAndConnectPrimvarReaderShader(self, shader_attrib: Usd.Attribute, time_code: _TimeCode, primvar_name: str, primvar_sdf_type: Sdf.ValueTypeName, fallback_value: _PreviewValue | None) -> None:
        """ Creates a primvar reader shader primitive,
            and connects it to the given attribute.
        """
    def createUVReaderShader(self, parent_path: Sdf.Path, prim_name: str, time_code: _TimeCode) -> UsdShade.Shader:
        """ Creates a UV Reader shader primitive.
        """
    def connectUsdMaterialOutput(self, usd_shader: UsdShade.Shader) -> None:
        """ Connects the USD material output to the USD preview surface shader.
        """
    def usdPreviewShaderInputInfo(self, usd_main_shader: UsdShade.Shader, preview_input_name: str, preview_input_type: Sdf.ValueTypeName, info: UsdShaderInputInfo | None) -> UsdShaderInputInfo | None:
        """ Offers the subclass a chance to create a new or adjust the default
            shader input attribute info. 
            The 'info', if not None, is a default info created from OGL tags.
        """
    def usdPreviewShaderInputInfos(self, usd_main_shader: UsdShade.Shader) -> list[UsdShaderInputInfo]:
        """ Returns a list of UsdShaderInputInfo objects that describes 
            input attributs to be authored on the USD preview shader.
        """
    def createUsdPreviewShaderInputs(self, usd_shader: UsdShade.Shader, input_infos: Iterable[UsdShaderInputInfo]) -> None:
        """ Creates and sets the USD shader input attributes 
            on the usd preview shader, given the list of input infos.

            Potentially creates USD input shaders and connect them to the
            inputs of the USD preview surface shader. 
        """
    def deleteUsdPreviewShaderInputs(self, usd_shader: UsdShade.Shader) -> None:
        """ Clears the input attributes of the given USD shader, 
            and deletes any input primitives. This prepares the USD stage
            for re-authoring of the preview shader input attributes.
        """
    def connectUsdPreviewShaderInput(self, usd_attrib: Usd.Attribute, usd_src: _StdSource) -> None:
        """ Connects the attribute to a material or parent graph input.
        """

class PreviewShaderTranslator:
    """ Authors a USD Preview Surface shader for a render-specific USD shader.
    """
    def matchesRenderContext(self, render_context: str) -> bool:
        """ Returns true if the given USD render context name matches 
            the USD render context for which this translator creates the 
            preview shaders. Render context is determined by the name of the
            terminal output of a Material primitive.
            Otherwise, returns false.
        """
    def createMaterialPreviewShader(self, usd_stage: Usd.Stage, usd_material_path: _SdfPath, usd_shader_path: _SdfPath, usd_time_code: _TimeCode) -> None:
        """ Creates a USD Preview Surface shader primitive for the given
            USD shader in the given USD material.

            usd_stage - UsdStage object on which to create the shader.
            usd_material_path - Path to the material primitive 
                in which to create the shader.
            usd_shader_path - path to a specific render context shader primitive
                based on which the universal render context preview shader 
                should be created.
            usd_time_code - time code (frame) at which to evaluate shader 
                parameters and at which to set the primitive attributes.
        """
    def deleteMaterialPreviewShader(self, usd_stage: Usd.Stage, usd_material_path: _SdfPath) -> None:
        """ Destroys a USD Preview Surface shader primitive for the given
            USD material.
        
            usd_stage - UsdStage object on which to create the shader.
            usd_material_path - Path to the material primitive 
                from which to remove the universal preview shader.
        """
    def updateMaterialPreviewShaderParameters(self, usd_stage: Usd.Stage, usd_main_shader_path: _SdfPath, usd_time_code: _TimeCode) -> None:
        """ Re-translates the attributes for the given shader.
            It allows targeted updates of USD shader primitives when
            a corresponding Houdini shader node's parameters changed,
            without the need to re-create the whole USD shader graph.

            usd_main_shader_path - USD path to the main shader primitive 
                that changed, and based on which the preview shader
                should be updated.
        """
    def previewShaderTranslatorHelper(self, usd_stage: Usd.Stage, usd_material_path: _SdfPath, usd_time_code: _TimeCode) -> PreviewShaderTranslatorHelper:
        """ Returns a translator helper that implements the actual logic
            of translating Houdini nodes into USD preview shaders.

            This is a convenience method to make it easier to derive
            custom preview shader translators from this class, without 
            the need to repeat the main API entry point methods such as 
            createMaterialPreviewShader(). 
            Ie, it should suffice to override only this method (and 
            matchesRenderMask() method too), and then
            implement the custom logic in the custom helper class 
            (usually derived from PreviewShaderTranslatorHelper).
        """
