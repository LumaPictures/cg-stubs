import hou
from collections.abc import Iterable
from husd.typeutils import _SdfScalarValue, _SdfValue
from pxr import Gf, Sdf, Usd, UsdShade
from typing import Protocol

from typing import TypeVar
from typing import TypeVar
_T = TypeVar('_T')
class _InputCreator(Protocol):
    def CreateInput(self, name: str, typeName: Sdf.ValueTypeName, /) -> UsdShade.Input: ...

class _OutputCreator(Protocol):
    def CreateOutput(self, name: str, typeName: Sdf.ValueTypeName, /) -> UsdShade.Output: ...

class _InputGetter(Protocol):
    def GetInput(self, name: str, /) -> UsdShade.Input: ...

class _OutputGetter(Protocol):
    def GetOutput(self, name: str, /) -> UsdShade.Output: ...

class _InputsLister(Protocol):
    def GetInputs(self) -> list[UsdShade.Input]: ...

Prm_RenderContextName: str
Prm_ShaderName: str
Prm_ShaderNameKind: str
Prm_ShaderSourceType: str
Prm_ShaderPrimName: str
Prm_PrimPath: str
Prm_PrimType: str
Prm_AssumeAllShaderParms: str
Prm_SkipDefValParms: str
Prm_ForceChildren: str
Prm_IsMatSibling: str
Prm_ReferenceType: str
Prm_BasePrimPath: str
Prm_BaseAssetPath: str
Prm_IsInstanceable: str
Prm_PropertiesContextName: str
Prm_RenderVarContextName: str
Tag_IsShaderParm: str
Tag_ForceShaderParmVal: str
Tag_ShaderParmName: str
Tag_ShaderParmType: str
Tag_ShaderParmRenderType: str
Tag_ShaderParmMetadata: str
Tag_ShaderMakeControlParm: str
Meta_PreviewShaderTagsKey: str
Meta_PreviewDefaultValueKey: str
Meta_PreviewShaderTags: set[str]
Meta_IsAutoCreatedShaderKey: str
Meta_HasAutoPreviewShaderKey: str

def isTuple(parm_value: object) -> bool:
    """ Returns true if value is a tuple-like.
    """

theScalarTypeSet: set[Sdf.ValueTypeName]

def isSdfScalar(usd_type: Sdf.ValueTypeName) -> bool:
    """ Returns true if usd_type name is a scalar.
    """
def isSdfArray(usd_type: Sdf.ValueTypeName) -> bool:
    """ Returns true if usd_type name is an array.
    """
def convertValueIfNeeded(value: _T, usd_type: Sdf.ValueTypeName) -> _T | int | Gf.Vec2i | Gf.Vec3i | Gf.Vec4i | Gf.Vec3f | Gf.Vec4f | Gf.Matrix2d | Gf.Matrix3d | Gf.Matrix4d:
    """ Tries to perform a trivial conversion if the types don't match.

        Value can be either of Usd type (eg, Gf.Vec3f, which come from USD
        attributes), or basic python type (eg, list(), which come from node 
        parameter values).
    """
def sdfValueFromValue(value: _T, usd_type: Sdf.ValueTypeName) -> _T | _SdfScalarValue | list[_SdfScalarValue]:
    """ Converts the given generic value (python or USD types) to format 
        acceptable by USD, based on the given Sdf type.
    """
def setUsdAttribFromUsdValue(usd_attrib: Usd.Attribute | UsdShade.Input | UsdShade.Output, usd_value: object, usd_time_code: Usd.TimeCode | float = ...) -> None:
    """ Sets the given USD attribute to the given USD-based value.
    """
def sdfValueFromParmValue(parm_value: _T, usd_type: Sdf.ValueTypeName) -> _T | _SdfScalarValue | list[_SdfScalarValue]:
    """ Converts the given parameter value to format acceptable by USD,
        based on the given Sdf type.
    """
def setUsdAttribFromParmValue(usd_attrib: Usd.Attribute | UsdShade.Input | UsdShade.Output, parm_value: object, usd_time_code: Usd.TimeCode | float = ...) -> None:
    """ Sets the given USD attribute to the given node parameter value.
    """
def createUsdInput(usd_shader: _InputCreator, input_name: str, usd_type: Sdf.ValueTypeName) -> UsdShade.Input:
    """ Creates and returns an input on the given USD shader schema.
    """
def createUsdInputAttrib(usd_shader: _InputCreator, input_name: str, usd_type: Sdf.ValueTypeName) -> Usd.Attribute:
    """ Creates an input on the given USD shader schema and returns
        an attribute for it.
    """
def usdInputAttrib(usd_shader: _InputGetter, input_name: str) -> Usd.Attribute:
    """ Returns an input attribute of the given USD shader schema.
    """
def createUsdOutput(usd_shader: _OutputCreator, output_name: str, usd_type: Sdf.ValueTypeName) -> UsdShade.Output:
    """ Creates and returns an output on the given USD shader schema.
    """
def createUsdOutputAttrib(usd_shader: _OutputCreator, output_name: str, usd_type: Sdf.ValueTypeName) -> Usd.Attribute:
    """ Creates an output on the given USD shader schema and returns
        an attribute for it.
    """
def usdOutputAttrib(usd_shader: _OutputGetter, output_name: str) -> Usd.Attribute:
    """ Returns an output attribute of the given USD shader schema.
    """
def usdGraphInputNames(usd_graph: _InputsLister) -> set[str]:
    """ Inspects the given USD graph schema and returns a set of input names.
    """
def usdAttribNameFromParm(parm_tuple: hou.ParmTuple) -> str:
    """ Returns the name of the attribute to create for this parameter.
    """
def usdAttribNameFromNodeConnector(node: hou.OpNode, name: str) -> str:
    """ Returns the name of the attribute to create based on node's connector
        port (ie, input or output) name.
    """
def usdAttribNameFromNodeInput(node: hou.OpNode, name: str) -> str:
    """ Returns the name of the attribute to create based on node's input name.
    """
def usdAttribNameFromNodeOutput(node: hou.OpNode, name: str) -> str:
    """ Returns the name of the attribute to create based on node's output name.
    """
def usdRampBasisAttribNameFromParmTemplate(parm_template: hou.ParmTemplate, default_root_name: str | None) -> str:
    ''' Returns the name of the ramp basis attribute to create for the given
        ramp parameter template."
    '''
def usdRampKeysAttribNameFromParmTemplate(parm_template: hou.ParmTemplate, default_root_name: str | None) -> str:
    ''' Returns the name of the ramp keys attribute to create for the given
        ramp parameter template."
    '''
def usdRampValuesAttribNameFromParmTemplate(parm_template: hou.ParmTemplate, default_root_name: str | None) -> str:
    ''' Returns the name of the ramp keys attribute to create for the given
        ramp parameter template."
    '''
def usdSetRampComponentsInfoOnAttrib(usd_attrib: Usd.Attribute, count_name: str | None, is_basis_array: bool, basis_name: str | None, keys_name: str | None, values_name: str | None) -> None:
    """ Sets custom data on the given ramp-related attribute that ties it to
        all the other shader input attribues (shader parameters) that represent
        a ramp. Used for creating the correct parameter interfaces for ramps.
        The parameters to this function represent count, basis, keys, and values
        attribute names, as well a boolean indicating if basis is an array.
    """
def usdShaderInputRenderTypeFromParm(parm_tuple: hou.ParmTuple | None) -> str | None:
    """ Returns the render type for the shader parametr, if any.
    """
def usdShaderOutputRenderType(node: hou.VopNode, output_name: str) -> str | None:
    """ Returns the USD shader output render type metadata to author.
    """
def sdfTypeFromParmTemplate(parm_template: hou.ParmTemplate) -> Sdf.ValueTypeName:
    """ Returns a usd value type name given the node's parameter type and size.
    """
def sdfTypeFromParmTypeAndSize(parm_tuple: hou.ParmTuple) -> Sdf.ValueTypeName:
    """ Returns a usd value type name given the node's parameter type and size.
    """
def sdfTypeFromParmTag(parm_tuple: hou.ParmTuple) -> Sdf.ValueTypeName:
    """ Returns a usd value type name given the node's parameter tag value.
    """
def sdfTypeFromParm(parm_tuple: hou.ParmTuple | None) -> Sdf.ValueTypeName:
    """ Returns a usd value type name given the node's parameter tags
        or (if tag is not found) its type and size
    """
def sdfTypeFromVopTypeName(vop_type_name: str | None) -> Sdf.ValueTypeName:
    """ Returns usd value type name given the vop data type name (a string).
    """
def sdfTypeFromSubnetInput(subnet: hou.OpNode | None, subnet_input_node: hou.VopNode, subnet_input_node_output_name: str) -> Sdf.ValueTypeName:
    """ Returns the USD type given the subnet input information.
    """
def sdfTypeFromNodeInput(node: hou.VopNode, input_name: str) -> Sdf.ValueTypeName:
    """ Returns the USD type given the node input.
    """
def sdfTypeFromNodeOutput(node: hou.VopNode, output_name: str) -> Sdf.ValueTypeName:
    """ Returns the USD type given the node output.
    """
def sdfTypeFromNodeConnector(node: hou.VopNode, name: str, vop_type_name: str | None) -> Sdf.ValueTypeName:
    """ Figures out and returns the USD type given the connector info
    """
def sdfTypeFromTypeMenuChoice(type_choice: str) -> Sdf.ValueTypeName:
    """ Returns usd value type name given the entry from standard type menu.
    """
def sdfTypeFromTypeParm(vop_node: hou.OpNode, type_parm_name: str) -> Sdf.ValueTypeName:
    """ Returns usd value type name, given the name of the (menu) parameter
        that specifies the VOP data type of the value.
    """
def valueParmTupleFromTypeParm(vop_node: hou.OpNode, type_parm_name: str) -> hou.ParmTuple | None:
    """ Returns the parameter that holds the value, given the name 
        of a (menu) parameter that specifies the VOP data type of the value.
    """
def sdfTypeFromParmDefinerTag(vop_node: hou.OpNode) -> Sdf.ValueTypeName:
    """ Returns usd value type name from tags available on the given 
        vop node that defines the parm.
    """
def sdfTypeFromParmDefiner(vop_node: hou.OpNode) -> Sdf.ValueTypeName:
    """ Returns usd value type name given the vop node that defines the parm.
    """
def sdfTypeFromPrimvarDefiner(vop_node: hou.OpNode) -> Sdf.ValueTypeName:
    """ Returns an Sdf value type allowed by USD Primvar Reader shader spec
        given the VOP node (Bind VOP) that represents the Primvar Reader.
    """
def usdShaderOutputTypeFromPrimvarSdfType(sdf_type: Sdf.ValueTypeName) -> Sdf.ValueTypeName:
    """ Returns a proper output type for the USD Primvar Reader shader primitive
        given the base Sdf type (primvar's type or the type of the shader input 
        it drives).
    """
def usdShaderIDFromPrimvarSdfType(sdf_type: Sdf.ValueTypeName) -> str:
    """ Returns a proper shader ID for the USD Primvar Reader shader primitive
        given the base Sdf type (primvar's type or the type of the shader input 
        it drives).
    """
def usdShaderIDFromPrimvarDefiner(vop_node: hou.OpNode) -> str:
    """ Returns a proper shader ID for the USD Primvar Reader shader primitive
        given the VOP node (Bind VOP).
    """
def primvarNameFromPrimvarDefiner(vop_node: hou.OpNode) -> str:
    """ Returns a primvar name to be used for the USD Primvar Reader shader's
        'primvar' attribute, given the VOP node (Bind VOP) that represents 
        the Primvar Reader.
    """
def fallbackValueFromPrimvarDefiner(vop_node: hou.OpNode) -> tuple[int, ...] | tuple[float, ...] | tuple[str, ...] | hou.Ramp:
    """ Returns usd value for theUSD Primvar Reader shader 'fallback' attrib,
        given the vop node that represents that primvar reader (ie Bind VOP).
    """
def valueFromConstantNode(vop_node: hou.OpNode) -> tuple[int, ...] | tuple[float, ...] | tuple[str, ...] | hou.Ramp:
    """ Returns USD value represented by the Constant VOP.
    """
def evalParmAsInt(vop_node: hou.OpNode, parm_name: str) -> int | None:
    """ Returns the value of the spare property parameter if it exists, or None.
    """
def evalParmAsString(vop_node: hou.OpNode, parm_name: str) -> str | None:
    """ Returns the value of the spare property parameter if it exists, or None.
    """
def isInputDefiner(vop_node: hou.OpNode) -> bool:
    """ Returns true if the VOP node defines a material parameter.
    """
def isPrimvarBinding(vop_node: hou.OpNode) -> bool:
    """ Returns true if the VOP node defines binding from geometry primvar
        to shader input (ie, can be translated to a USD Primvar Reader prim.
    """
def isSubnetInputDefiner(vop_node: hou.VopNode) -> bool:
    """ Returns true if the VOP node defines a material parameter.
    """
def isConstantNode(vop_node: hou.OpNode) -> bool:
    """ Returns ture if the VOP node is a constant node.
    """
def isColorRampVopTypeName(type_name: str | None) -> bool:
    """ Returns ture if the given vop data (port) type name is a color ramp.
    """
def isFloatRampVopTypeName(type_name: str | None) -> bool:
    """ Returns ture if the given vop data (port) type name is a float ramp.
    """
def isRampVopTypeName(type_name: str | None) -> bool:
    """ Returns true if the given VOP data (port) type name is a ramp.
    """
def subnetInputsToFollow(vop_subnet: hou.VopNode, usd_graph: _InputsLister) -> list[str]:
    """ Returns list of subnet node input names that the translator should
        translate and connect to the node graph primitive.
        These are the subnet input ports that already got translated to the
        usd graph, but have not been connected to, because the input node
        has not been translated yet.
    """
def subnetInputName(name: str) -> str:
    """ Returns the name of the subnet input given the connection name 
        inside the subnet.
    """
def nodeInputTypeName(vop_node: hou.VopNode, input_name: str) -> str | None:
    """ Returns the vop type (string) of the given VOP node input.
    """
def nodeOutputTypeName(vop_node: hou.VopNode, output_name: str) -> str | None:
    """ Returns the vop type (string) of the given VOP node output.
    """
def wireToSubnetOutputNode(subnet_node: hou.VopNode, subnet_node_output_name: str | None) -> hou.NodeConnection | None:
    """ Returns the connection wire inside the subnet that connects to 
        subnet output node which corresponds to the given subnet output name.
    """
def wireToNodeInput(node: hou.Node, input_name: str) -> hou.NodeConnection | None:
    """ Returns a connection to the given node input,
        or None if input is not connected.

    """
def parmNameFromNodeInput(node: hou.VopNode, input_name: str) -> str:
    """ Returns the parameter name holding the value corresponding
        to the given input.
    """
def isUsdShaderNetwork(vop_node: hou.VopNode) -> bool:
    """ Returns true if the node is considered a container for shaders.
    """
def usdShaderSourceType(vop_node: hou.OpNode) -> str | None:
    """ Returns the name that identifies the type of a shader source,
        eg, 'glsl', 'vex', 'osl' (effectively the language name). 
        Used in constructing the shader source property.
    """
def findParentSubnetOutputIndex(child_node: hou.Node, child_node_output_name: str) -> int:
    """ Returns the index of the subnet's output that corresponds to the
        output of the given child node, if the child defines the subnet output
    """
def parentSubnetOutputName(child_node: hou.Node, child_node_output_name: str) -> str | None:
    """ Returns the name of the subnet's output that corresponds to the
        output of the given child node, if the child defines the subnet output.
    """
def parentSubnetOutputVopTypeName(child_node: hou.Node, child_node_output_name: str) -> str | None:
    """ Returns the VOP type name of the subnet's outputs that corresponds
        to the output of the given child node, if the child defines one.
    """
def parentSubnetOutputSdfType(child_node: hou.Node, child_node_output_name: str) -> Sdf.ValueTypeName:
    """ Returns the Sdf type of the subnet's outputs that corresponds
        to the output of the given child node, if the child defines one.
    """
def isShaderVopTypeName(vop_type_name: str | None) -> bool:
    """ Returns ture if the given vop type is one of the known shader types.
    """
def shaderTypeNameFromVopType(shader_type: hou.EnumValue[hou.shaderType]) -> str | None:
    """ Returns the name of the given enumerated shader type.
    """
def vopTypeFromShaderTypeName(type_name: str) -> hou.EnumValue[hou.shaderType] | None:
    """ Returns the name of the given enumerated shader type.
    """
def usdShaderTypeFromVopTypeName(vop_type_name: str) -> str:
    """ Returns USD shader type (as used in material output name) 
        for the given VOP shader/data type name.
    """
def usdShaderTypeFromHouShaderType(requested_shader_type: hou.EnumValue[hou.shaderType]) -> str:
    """ Returns USD shader type (as used in material output name) 
        for the given HOU shader enum type.
    """
def isShaderParmForced(parm_tuple: hou.ParmTuple) -> bool:
    """ Returns true if the parameter tuple has a tag indicating that
        the value should be authored on the USD primitive even if
        the node parameter is at default.
    """
def isShaderParmActive(parm_tuple: hou.ParmTuple, default_value: bool = True) -> int | float | str:
    """ Checks if the given parameter should be translated, based on
        an accompanyin activation toggle parameter. If the activation
        parameter exists and is toggled off, the parameter translation
        is considered disabled, and the parm should not be translated.
        Returns the value of the activation parameter if it exists,
        otherwise returns the default value passed in as parameter.
    """
def disconnectUsdAttribIfActivated(usd_attrib: Usd.Attribute, parm_tuple: hou.ParmTuple) -> None:
    """ Disconnects the given USD attribute if it is explicitly activated
    """
def usdShaderPrimNameFromNode(vop_node: hou.OpNode) -> str:
    """ Returns the name of the USD shader primitive based on the
        given shader node.
    """
def usdPrimPathFromNode(vop_node: hou.OpNode) -> str | None:
    """ Returns the USD primitive path that the given node specifies.
        May be None if the node does not explicitly spefity it.
        It's commonly used to specify Material and NodeGraph to author. 
    """

theSchemaNameFromShaderIdMap: dict[str, str] | None

def usdPrimTypeFromShaderName(shader_id: str, render_context_name: str | None = None) -> str | None:
    """ Returns the prim type (typed schema) name for the given shader id.
    """
def usdPrimTypeFromNode(vop_node: hou.VopNode, default_type_name: str) -> str:
    """ Returns the primitive type name (a string), if the node explicitly 
        specifies one, or None if it does not.
    """
def usdSchemaPyClassFromTypeName(usd_type_name: str | None) -> type[Usd.SchemaBase] | None:
    """ Returns schema python class object given the USD primitive schema
        type name or its alias. May return a base class if the given type
        refers to a codeless schema.
    """
def authorMissingAncestors(usd_stage: Usd.Stage, path: str | Sdf.Path, usd_prim_type_name: str) -> Sdf.Path:
    """ Authors primitives of the given type if they are missing
        in the given usd path.
    """
def shouldAuthorAsUsdMaterialSibling(vop_node: hou.OpNode) -> bool:
    """ Returns true if the vop node is convigured to be authored
        as a sibling of the material rather than a child.
    """
def shouldSkipTranslationOfChildren(vop_subnet_node: hou.OpNode) -> bool:
    """ Returns true if the translator should not translate the children
        of the given VOP subnet.
    """
def splitUsdConnectionSourcePath(source_path: str | Sdf.Path) -> tuple[Sdf.Path, str]:
    """ Returns a pair (a prim path and input/output name) given the 
        full source (input/output) path.
    """
def joinUsdConnectionSourcePath(prim: Usd.Prim | Usd.SchemaBase, source_name: str, is_input: bool) -> Sdf.Path:
    """ Returns a property path for the given input/output.
    """
def explicitRenderContextName(vop_node: hou.OpNode) -> str | None:
    """ Returns a render context name for the shader node, if it's explicitly
        stated in a spare parameter. None otherwise.
    """
def explicitPropertiesContextName(vop_node: hou.OpNode) -> str | None:
    """ Returns the render context name of a shader on which the translator
        should author the rendering properties for the material,
        if such context name is explicitly stated in a spare parameter.
        Otherwise, returns None.
    """
def explicitRenderVarContextName(vop_node: hou.OpNode) -> str | None:
    """ Returns the render context name of a shader to which the translator
        should link (connect) the render var (AOV) pattern output.
        Such connection allows the renderer to discover the other shaders
        that it should evaluate as render vars (AOVs).
    """
def shaderName(vop_node: hou.OpNode) -> str | None:
    """ Returns the value of the shader name spare parameter.
    """
def shaderNameInterpretation(vop_node: hou.OpNode) -> str | None:
    """ Returns whether the USD shader is identified by an ID, asset path,
        or a source code.
    """
def basePrimReferenceType(vop_node: hou.OpNode) -> str | None:
    """ Returns how a shader should reference an existing (base) primitive.
        Eg, 'reference', 'inherit', or 'specialize'.
    """
def basePrimPath(vop_node: hou.OpNode) -> str | None:
    """ Returns the USD path to the primitive to reference, specialize, or
        inherit from.
    """
def baseAssetPath(vop_node: hou.OpNode) -> str | None:
    """ Returns the file path to the asset containing a primitive to reference.
    """
def isBasePrimParmIn(parameter_names: Iterable[str]) -> bool:
    """ Returns true if the parameter_names list contains any parameter
        related to the primitive referencing (inheritance, specilization, etc).
    """
def isInsatanceable(vop_node: hou.OpNode) -> bool:
    """ Returns true if translated primitive should be flagged as instanceable.
    """
def isPreviewTag(tag_name: str) -> bool:
    """ Returns true if the tag name is used for preview shader attribute.
    """
def setPreviewTagsMetadata(usd_attrib: Usd.Attribute, parm_tuple: hou.ParmTuple) -> None:
    """ Sets the preview shader metadata on a USD attribute, given the 
        node parameter and it's OGL tags.
    """
def isPreviewTagMetadataSet(usd_attrib: Usd.Property, tag_name: str) -> str | bool | None:
    """ Returns true if the given tag is set to true on the given USD attribute.
    """
def setPreviewDefaultValueFromParmValue(usd_attrib: Usd.Attribute, parm_value: object) -> None:
    """ Sets the parm value as an attribute metadata, 
        for use in authoring preview shader USD attributes.
    """
def getPreviewValueFromAttrib(usd_attrib: Usd.Attribute, usd_time_code: Usd.TimeCode | float = ...) -> _SdfValue | None:
    """ Returns a value for the preview shader input attribute from
        the given main shader attribute.
    """
def setAutoCreatedShaderMetadataFlag(usd_prim: Usd.Prim) -> None:
    """ Authors a primitive metadata indicating that the primitive
        was automatically created for shader preview purposes.
    """
def isAutoCreatedShader(usd_prim: Usd.Prim) -> bool | None:
    """ Returns true if the primitive metadata indicates that the primitive
        was auto-created for preview shader purposes.
    """
def hasAutoPreviewShader(usd_prim: Usd.Prim) -> bool | None:
    """ Returns true if the given USD shader primitive is used to auto-create
        a preview shader.
    """
def usdAttribMetadataInfoString(parm_tuple: hou.ParmTuple) -> str | None:
    """ Returns the JSON string that encodes metadata information for the
        USD attribute to which the parm tuple will translate to.
    """
def setAttribMetadata(usd_attrib: Usd.Attribute, key_path: str, parm_value: object, usd_type: Sdf.ValueTypeName) -> None:
    """ Sets the metadata value on a USD attribute at a given key path.
    """
def shouldAuthorControlParm(parm_tuple: hou.ParmTemplate) -> bool:
    """Returns true if the given parm tuple does not prevent the creation of
       a control parm. Set this to '0' on both an explicitly authored control
       and it's corresponding parm_tuple.
    """
def shouldAuthorRenderVar(vop_node: hou.OpNode) -> bool:
    """ Returns true if the given vop node does not inhibit authoring
        of the RenderVar primitive in the material.
    """
def renderVarName(vop_node: hou.VopNode) -> str | None:
    """ Returns the name of the render variable given the node that represents
        or configures such a render var (AOV).
    """
def renderVarFilter(vop_node: hou.VopNode) -> str | None:
    """ Returns the filter string specification for a render variable 
        given the node that represents or configures such render var (AOV).
    """
def getSdrDefaultValueFromAttrib(usd_attrib: Usd.Attribute) -> _SdfValue | None:
    """ Returns a default value for a shader parameter corresponding
        to the given USD shader input attribute. 
    """
def usdFirstConnectedSourceInfo(usd_input_or_output: UsdShade.Input | UsdShade.Output | None) -> UsdShade.ConnectionSourceInfo | None:
    """ Returns the first UsdShadeConnectionSourceInfo struct connected
        to the given input/output.
    """
def usdFirstConnectedSourcePrim(usd_input_or_output: UsdShade.Input | UsdShade.Output | None) -> Usd.Prim | None:
    """ Returns the first primitive connected to the given input/output.
    """
def usdFirstConnectedSource(usd_input_or_output: UsdShade.Input | UsdShade.Output | None) -> UsdShade.Input | UsdShade.Output | None:
    """ Returns the first source (an input or output) connected to the given
        target.
    """
def usdFirstConnectedOriginatorSourcePrim(usd_input_or_output: UsdShade.Input | UsdShade.Output | None) -> Usd.Prim | None:
    """ Given the output path and a chain of connections to it,
        finds the original USD source that is not connected to anything
        and which is the source of the value for the given output.
        Returns the original source primitive.
    """
def usdFirstConnectedOriginatorSource(usd_input_or_output: UsdShade.Input | UsdShade.Output | None) -> UsdShade.Input | UsdShade.Output | None:
    """ Given the output path and a chain of connections to it,
        finds the original USD source that is not connected to anything
        and which is the source of the value for the given output.
        Returns the original source input or output.
    """
def usdFirstConnectedShader(usd_input_or_output: UsdShade.Input | UsdShade.Output | None) -> UsdShade.Shader | None:
    """ Returns the first shader connected to the given input/output,
        recursing into NodeGraphs if needed.
    """
def rampPartAttribName(ramp_name: str | None, part_name: str) -> str:
    """ Constructs a name for the ramp array attribute.
    """
def rampBasisAttribName(ramp_name: str | None) -> str:
    """ Returns a name for the ramp basis array attribute.
    """
def rampKeysAttribName(ramp_name: str | None) -> str:
    """ Returns a name for the ramp keys array attribute.
    """
def rampValuesAttribName(ramp_name: str | None) -> str:
    """ Returns a name for the ramp values array attribute.
    """
def rampColorspaceAttribName(ramp_name: str | None) -> str:
    """ Returns a name for the ramp color space array attribute.
    """
def rampNameFromAttribName(attrib_name: str) -> str | None:
    """ Returns a ramp root name given the USD input name
    """
