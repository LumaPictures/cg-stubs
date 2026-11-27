import hou
from . import shaderutils as shaderutils
from collections.abc import Collection, Iterable, Mapping
from pxr import Sdf, Tf as Tf, Usd, UsdLux, UsdShade

from typing import TypeAlias
from typing import TypeAlias
_UsdShaderSchema: TypeAlias = UsdShade.Shader | UsdShade.NodeGraph | UsdLux.LightFilter
_UsdConnectable: TypeAlias = UsdShade.ConnectableAPI | UsdShade.Shader | UsdShade.NodeGraph | UsdLux.LightFilter
_ParmTupleValue: TypeAlias = tuple[int, ...] | tuple[float, ...] | tuple[str, ...] | tuple[hou.Ramp, ...]
_ParmDefaultValue: TypeAlias = tuple[int, ...] | tuple[float, ...] | tuple[str, ...] | int | bool
_MultiParmElement: TypeAlias = int | float | str | hou.Ramp | _ParmTupleValue
VisualizerShaderContext: str
RenderContextFromRenderMask: dict[str, str]

def findOutputNode(item: hou.NetworkMovableItem | None) -> hou.Node | None:
    """ Returns an output node, traversing thru the dots if needed.
    """
def renderContextName(shader_node: hou.VopNode, shader_node_output_name: str, curr_translator_id: int) -> str:
    """ Returns the USD render context name for the given node and output.
    """

class ShaderCache:
    """ A class that implements a look-aside cache for previously translated
        shader. The VOP shader nodes are not expected to change during
        a translation of a single materials, and therfore we can reuse
        an already translated USD shader primitive. This cache is meant
        to store the mapping from VOP to USD prim for such reuse.
    """
    myShaders: dict[hou.VopNode, _UsdShaderSchema]
    def __init__(self) -> None: ...
    def clear(self) -> None:
        """ Clears the cached shader entries.
        """
    def lookupShader(self, shader_node: hou.VopNode) -> _UsdShaderSchema | None:
        """ Returns a USD shader (schema) for the given shader node (VOP),
            if it exists in this cache. Otherwise, returns 'None'.
        """
    def cacheShader(self, shader_node: hou.VopNode, usd_shader: _UsdShaderSchema) -> None:
        """ Adds the given USD shader (schema) to this cache.
        """

theShaderCache: ShaderCache

class ParmTranslator:
    """ A class that implements the logic of encoding VOP node parameters
        as attributes on a USD primitive.
    """
    myParmTuple: hou.ParmTuple
    def __init__(self, parm_tuple: hou.ParmTuple) -> None: ...
    def parmTuple(self) -> hou.ParmTuple:
        """ Returns the parameter to be translated to a USD attribute.
        """
    def adjustedTimeCode(self, usd_time_code: Usd.TimeCode, force_time_dependent: bool = False) -> Usd.TimeCode:
        """ Returns an adjusted time code based on the given `usd_time_code`,
            checking whether the parameter is animatable, etc.
        """
    def adjustedParmValue(self, parm_value: _ParmTupleValue, usd_time_code: Usd.TimeCode) -> tuple[_ParmTupleValue, bool]:
        ''' Returns a tuple (new_parm_value, is_time_dependent)
            The new parm value is based on the given `parm_value`,
            checking whether the value should be further modified or tweaked
            based on some external factors (eg, node time dependency).
            It is used for string path values of the form "op:/path/to/cop"
            to insert a frame number if the cop node is time dependent, eg
            resulting in "op:/path/to/cop[42]" to indicate frame 42.
        '''
    def createAttrib(self, usd_shader: _UsdShaderSchema) -> Usd.Attribute | None:
        """ Creates and returns an attribute.
        """
    def setAttrib(self, usd_attrib: Usd.Attribute, usd_time_code: Usd.TimeCode, metadata_infos: Iterable['MetadataInfo'] = ...) -> None:
        """ Sets the given USD attribute according to the member node parameter
            at the specified time code
            Also authors attribute metadata, if available.
        """
    def findOrCreateAttrib(self, usd_shader: _UsdShaderSchema) -> Usd.Attribute | None:
        """ Returns an existing attribute if found, or newly created one if not.
        """
    def createAndSetAttrib(self, usd_shader: _UsdShaderSchema, usd_time_code: Usd.TimeCode, metadata_infos: Iterable['MetadataInfo'] = ...) -> None:
        """ Creates an input attribute on the given USD shader schema, and 
            sets its value according to the member node parameter, 
            at the specified time code.
            Also authors attribute metadata, if available.
        """
    def attribName(self) -> str:
        """ Returns the name of the attribute to create for this parameter.
        """
    def valueFromParm(self, parm_tuple: hou.ParmTuple, usd_time_code: Usd.TimeCode) -> _ParmTupleValue:
        """ Evaluates node's parameter and returns the value tuple.
        """
    def defaultValueFromParm(self, parm_tuple: hou.ParmTuple) -> _ParmDefaultValue:
        """ Obtains node's aprameter default value.
        """
    def isParmChanged(self, parm_names: Collection[str]) -> bool:
        """ Returns true if parameter is considered to have changed
            The 'parm_names' is the list of parameters that have changed;
            if empty, it means that any parm may have changed; else it
            contains parms that have changed.
        """
    def parmFromAttribMap(self) -> dict[str, str]:
        """ Returns a map that maps a USD primtive atrib name to node parm name.
        """

class SimpleParmTranslator(ParmTranslator):
    """ A class that implements the logic of encoding a simple VOP node 
        parameter to an attribute on a USD primitive.
        Does not handle complex parameters such as ramps or multi-parms.
    """
    def __init__(self, parm_tuple: hou.ParmTuple) -> None: ...
    def createAndSetAttrib(self, usd_shader: _UsdShaderSchema, usd_time_code: Usd.TimeCode, metadata_infos: Iterable['MetadataInfo'] = ...) -> None:
        """ Creates an input attribute on the given USD shader schema, and 
            sets its value according to the member node parameter, 
            at the specified time code
            Also authors attribute metadata, if available.
        """
    def createAttrib(self, usd_shader: _UsdShaderSchema) -> Usd.Attribute:
        """ Creates an input attribute on the given USD shader schema,
            using the member node parameter to deduce its name and USD type.
        """
    def setAttrib(self, usd_attrib: Usd.Attribute, usd_time_code: Usd.TimeCode, metadata_infos: Iterable['MetadataInfo'] = ...) -> None:
        """ Sets the given USD attribute according to the member node parameter
            at the specified time code
            Also authors attribute metadata, if available.
        """
    def evalParm(self, usd_time_code: Usd.TimeCode) -> _ParmTupleValue:
        """ Evaluates member parameter.
        """
    def parmDefaultValue(self) -> _ParmDefaultValue:
        """ Evaluates the default value of the member parameter.
        """

class RampParmTranslator(ParmTranslator):
    """ A class that implements the logic of encoding a ramp VOP node parameter
        to an attribute on a USD shader primitive.
    """
    def __init__(self, parm_tuple: hou.ParmTuple) -> None: ...
    def createAndSetAttrib(self, usd_shader: _UsdShaderSchema, usd_time_code: Usd.TimeCode, metadata_infos: Iterable['MetadataInfo'] = ...) -> None:
        """ Creates an input attribute on the given USD shader schema, and 
            sets its value according to the member node parameter, 
            at the specified time code.
            Also authors attribute metadata, if available.
        """
    def setCustomDataOnAttrib(self, usd_attrib: Usd.Attribute) -> None:
        """ Sets custom data on every ramp-related parameter that ties it to
            all the other ramp parameters so that we can create the correct
            parameter interface for the ramp.
        """
    def evalParm(self, usd_time_code: Usd.TimeCode) -> hou.Ramp:
        """ Evaluates member ramp parameter.
        """
    def basisAttribName(self) -> str:
        """ Returns the name of the attribute for the ramp basis component.
        """
    def createBasisAttrib(self, usd_shader: _UsdShaderSchema) -> Usd.Attribute:
        """ Creates an input attribute (on the given USD shader schema)
            for the ramp basis component.
        """
    def setBasisAttrib(self, usd_attrib: Usd.Attribute, ramp_val: hou.Ramp, usd_time_code: Usd.TimeCode) -> None:
        """ Sets the ramp basis attribute, usd_attrib, to the basis
            of the ramp_val.
        """
    def createKeyCountAttrib(self, usd_shader: _UsdShaderSchema) -> Usd.Attribute:
        """ Creates an input attribute (on the given USD shader schema)
            for the ramp key count.
        """
    def setKeyCountAttrib(self, usd_attrib: Usd.Attribute, ramp_val: hou.Ramp, usd_time_code: Usd.TimeCode) -> None:
        """ Sets the ramp count attribute, usd_attrib, to the key count 
            of the ramp_val.
        """
    def keysAttribName(self) -> str:
        """ Returns the name of attribute for the ramp key positions component.
        """
    def createKeysAttrib(self, usd_shader: _UsdShaderSchema) -> Usd.Attribute:
        """ Creates an input attribute (on the given USD shader schema)
            for the ramp key positions component.
        """
    def setKeysAttrib(self, usd_attrib: Usd.Attribute, ramp_val: hou.Ramp, usd_time_code: Usd.TimeCode) -> None:
        """ Sets the ramp keys attribute, usd_attrib, to the keys (positions)
            of the ramp_val.
        """
    def valuesAttribName(self) -> str:
        """ Returns the name of attribute for the ramp control points values 
            component.
        """
    def createValuesAttrib(self, usd_shader: _UsdShaderSchema) -> Usd.Attribute:
        """ Creates an input attribute (on the given USD shader schema)
            for the ramp control points values component.
        """
    def setValuesAttrib(self, usd_attrib: Usd.Attribute, ramp_val: hou.Ramp, usd_time_code: Usd.TimeCode) -> None:
        """ Sets the ramp values attribute, usd_attrib, to the interpolation 
            values of the ramp_val.
        """
    def rampBasisMap(self) -> dict[hou.EnumValue[hou.rampBasis], str]:
        """ Returns a map from enumerated values of ramp interpolation
            to the string names of such interpolation.
        """
    def rampBasisValue(self, ramp_val: hou.Ramp) -> str:
        """ Returns the value of the ramp basis given the ramp.
        """
    def adjustedTimeCode(self, usd_time_code: Usd.TimeCode) -> Usd.TimeCode:
        """ Returns an adjusted time code based on the given `usd_time_code`,
            checking whether the parameter is animatable, etc.
        """
    def parmFromAttribMap(self) -> dict[str, str]:
        """ Returns a map that maps a primtive atrib name to node parm name.
        """

class MultiParmTranslator(ParmTranslator):
    """ A class that implements the logic of encoding a multi-parm VOP node 
        parameter as an attribute on a USD primitive.
    """
    def __init__(self, parm_tuple: hou.ParmTuple) -> None: ...
    def createAndSetAttrib(self, usd_shader: _UsdShaderSchema, usd_time_code: Usd.TimeCode, metadata_infos: Iterable['MetadataInfo'] = ...) -> None:
        """ Creates an input attribute on the given USD shader schema, and 
            sets its value according to the member node parameter, 
            at the specified time code.
            Also authors attribute metadata, if available.
        """
    def createAttrib(self, usd_shader: _UsdShaderSchema) -> Usd.Attribute | None:
        """ Creates an input attribute on the given USD shader schema,
            using the member multi-parm node parameter to deduce its name 
            and USD type, etc.
        """
    def evalParm(self, usd_time_code: Usd.TimeCode) -> list[_MultiParmElement]:
        """ Evaluates member multi-parm parameter as array.
        """
    def adjustedTimeCode(self, usd_time_code: Usd.TimeCode) -> Usd.TimeCode:
        """ Returns an adjusted time code based on the given `usd_time_code`,
            checking whether the parameter is animatable, etc.
        """

class MetadataInfo:
    """ A class the enapsulates information about one piece of metadata
        to author on a USD attribute. 
        The metadata value can come from a node parameter.
    """
    myKeyPath: str
    mySrcParmTuple: hou.ParmTuple | None
    def __init__(self, keypath: str, src_parm_tuple: hou.ParmTuple | None = None) -> None: ...
    def keyPath(self) -> str: ...
    def srcParmTuple(self) -> hou.ParmTuple | None: ...
    def createAttribMetadata(self, usd_attrib: Usd.Attribute, usd_time_code: Usd.TimeCode) -> None:
        """ Authors metadata on the given USD attribute, evaluating
            the source member parameter tuple at the given time if needed.
        """

def buildAttribMetadataInfosMap(shader_node: hou.VopNode) -> dict[str, list[MetadataInfo]]:
    """ Returns a map from a node parameter name to an array of MetadataInfos 
        for the USD attrib to which that node parameter translates to.
    """

class ShaderVisualizerInfo:
    """ Keeps information about visualizing (soloing) shaders.
    """
    myVisualizerNode: hou.VopNode | None
    myShaderNodeToVisualize: hou.VopNode | None
    myShaderNodeOutputNameToVisualize: str | None
    myUsdVisualizerOutputPath: Sdf.Path | None
    def __init__(self) -> None:
        """ Constructs the visualizer info object.
        """
    def visualizerNode(self) -> hou.VopNode | None: ...
    def shaderNodeToVisualize(self) -> hou.VopNode | None: ...
    def shaderNodeOutputNameToVisualize(self) -> str | None: ...
    def usdVisualizerOutputPath(self) -> Sdf.Path | None: ...
    def setUsdVisualizerOutputPath(self, path: Sdf.Path | None) -> None: ...
    def reset(self, visualizer_node: hou.VopNode | None = None) -> None:
        """ Resets the info to a given visualizer VOP node.
        """

theShaderVisualizerInfo: ShaderVisualizerInfo

class ShaderTranslatorHelper:
    """ This class implements the logic of translating Houdini shader VOP nodes 
        to USD shader primitives.
    """
    myID: int
    myUsdStage: Usd.Stage
    myUsdMaterialPath: str | None
    myUsdTimeCode: Usd.TimeCode
    myUsdMainConnectable: UsdShade.ConnectableAPI | None
    myUsdNodeGraph: UsdShade.NodeGraph | None
    myUsdMaterial: UsdShade.Material | None
    myShouldAuthorPreviewMetadata: bool
    def __init__(self, translator_id: int, usd_stage: Usd.Stage, usd_material_path: str | None, usd_time_code: Usd.TimeCode) -> None:
        """ Saves the common pieces of data as member variables.
        """
    def translatorID(self) -> int:
        """ Returns the ID number of this translator.
        """
    def usdStage(self) -> Usd.Stage:
        """ Returns the USD stage on which to define shader primitives.
        """
    def usdMainAncestorPath(self) -> str | None:
        """ Returns the path of the main USD material or node graph in which 
            to define primitives.
        """
    def usdMaterial(self) -> UsdShade.Material | None:
        """ Returns the USD material schema for the main material primitive 
            inside which to define shader primitives. 

            NOTE: This may be 'None' if the main parent is NodeGraph instead 
            of a Material primitive.
        """
    def usdNodeGraph(self) -> UsdShade.NodeGraph | None:
        """ Returns the USD Node Graph schema for the main primitive 
            (either a material on a node graph) inside which to define 
            shader primitives.

            Usually this is the Material primitive, unless the user
            chose to author a Node Graph primitive instead.

            NOTE: This may be 'None' for incremental re-translation of
            a specific existing shader primitive. But for full translation
            it is not 'None'.
        """
    def usdMainConnectable(self) -> UsdShade.ConnectableAPI | None:
        """ Returns the USD ConnectableAPI schema for the main primitive
            (either a material on a node graph) inside which to define 
            shader primitives. May be 'None'.

            Usually this is the Material primitive, unless the user
            chose to author a Node Graph primitive instead.
        """
    def setUsdMainConnectable(self, main_connectable: UsdShade.ConnectableAPI | None) -> None:
        """ Sets the main connectable.
            Should be called only from subclasses if needed.
        """
    def usdTimeCode(self) -> Usd.TimeCode:
        """ Returns the USD time code at which to set USD attribute values.
        """
    def houdiniFrame(self) -> float:
        """ Returns the Houdini playbar frame at which to evaluate node 
            parameters.
        """
    def initShaderVisualization(self, shader_node: hou.VopNode) -> None:
        """ Determines whether there is any shader node that may need 
            to be set up for visualizing the value of its output for debugging.
        """
    def updateShaderVisualization(self, usd_shader: _UsdShaderSchema) -> None:
        """ Creates the visualizer shader chain for the given shader.
            Returns a path to the output of newly created visualizing USD shader
            which can be connected to Material prim as a terminal shader output.
        """
    def finalizeShaderVisualization(self, mat_output_name: str, mat_output_type: Sdf.ValueTypeName) -> None:
        """ If needed, creates shader visualizer and connects 
            it as material terminal.
        """
    def createUsdVisualizerShader(self, usd_shader_output: UsdShade.Output, visualizer_node: hou.VopNode | None) -> Sdf.Path | None:
        """ Creates a USD shader primitive that visualizes the value 
            of a given output of another (pattern/utility) USD shader.
            Ie, the given output is usually a data such as a vector or a float.
            The visualizer node is provided for convenience to query any
            visualization settings (eg, ramp remapping), if needed.
            Returns a path to the output of newly created visualizing USD shader
            which can be connected to Material prim as a terminal shader output.
        """
    def createAndConnectUsdTerminalShader(self, shader_node: hou.VopNode, requested_shader_type: hou.EnumValue[hou.shaderType], shader_node_output_name: str) -> Sdf.Path | None:
        """ Creates and configures a USD shader primitive based on the
            given Houdini node, and links it to the USD material primitive 
            specified in the construcor (via USD primitive outputs).

            This is the main entry point API for translating a Houdini node
            (and its input nodes) to USD and connecting it to the USD material
            as one of its terminal shaders.

            Returns the path to the terminal output attribute of the material 
            primitive to which the terminal shader has been connected.
        """
    def createAndConnectUsdTerminalShaderToMainOutput(self, shader_node: hou.VopNode, requested_shader_type: hou.EnumValue[hou.shaderType], shader_node_output_name: str, usd_main_connectable: UsdShade.ConnectableAPI, usd_output_name: str, usd_output_type: Sdf.ValueTypeName) -> Sdf.Path | None:
        """ Creates and configures a USD shader primitive based on the
            given Houdini node, and links it to the given USD terminal output.

            Returns the path to the terminal output attribute of the material 
            primitive to which the terminal shader has been connected.
        """
    def createUsdTerminalShader(self, shader_node: hou.VopNode, shader_node_output_name: str, usd_parent_path: str, usd_shader_prim_name: str | None) -> Sdf.Path | str | None:
        """ Creates USD shader primitive given the Houdini `shader_node`.

            This is the main entry point API for translating a Houdini node
            (and its input nodes) to USD.
        """
    def createUsdShaderChain(self, shader_node: hou.VopNode, shader_node_output_name: str, usd_parent_connectable: _UsdConnectable, usd_shader_prim_name: str | None) -> Sdf.Path | str | None:
        """ Creates and configures a USD shader primitive (and its inputs)
            given the Houdini `shader_node` be translated into a USD. 

            The `usd_parent_connectable` is the USD Material or NodeGraph schema
            of the parent primitive directly in which to create shaders prims.

            Recursively tranverses the input nodes and repeats the translation 
            for each of them.

            Returns a path to the output of the translated USD shader primitive.
        """
    def postCreateUsdShaderChain(self, shader_node: hou.VopNode, shader_node_output_name: str, usd_shader_output: UsdShade.Output) -> None:
        """ This method is run after the shader chain has been authored
            based on the given shader VOP node for its given output.
        """
    def inputConnectionInfo(self, usd_shader: _UsdShaderSchema, shader_node: hou.VopNode, wire: hou.OpNodeConnection) -> tuple[_UsdShaderSchema | None, str | None, Sdf.ValueTypeName | None, hou.VopNode | None, str | None]:
        """ Returns a tuple describing how to continue the traversal
            of the input connection given by the wire.
            The returned info describes on which node
            to continue the recursive travarsal of the shader node chain
            and on which USD shader to author that connection.
        """
    def createAndConnectUsdGraphInput(self, usd_shader: _UsdShaderSchema, usd_shader_input_name: str, usd_shader_input_type: Sdf.ValueTypeName, usd_parent_connectable: _UsdConnectable, input_node: hou.VopNode, input_node_output_name: str) -> None:
        """ Creates and connect the shader input to the parent graph input.
        """
    def createAndConnectUsdMaterialInput(self, usd_shader: _UsdShaderSchema, usd_shader_input_name: str, usd_shader_input_type: Sdf.ValueTypeName, input_node: hou.VopNode, input_node_output_name: str) -> None:
        """ Creates and connects the shader input to the material input.
        """
    def createAndConnectPrimvarBinding(self, usd_shader: _UsdShaderSchema, usd_shader_input_name: str, usd_shader_input_type: Sdf.ValueTypeName, usd_parent_schema: _UsdConnectable, input_node: hou.VopNode) -> None:
        """ Creates a Primvar Reader primitive and connects its output
            to the shader's input (after creating it if necessary).
        """
    def createConstantValue(self, usd_shader: _UsdShaderSchema, usd_shader_input_name: str, usd_shader_input_type: Sdf.ValueTypeName, input_node: hou.VopNode, input_node_output_name: str) -> None:
        """ Authors a new value of an attribute on the shader primitive.
        """
    def createAndConnectUsdInputShader(self, usd_shader: _UsdShaderSchema, usd_shader_input_name: str, usd_shader_input_type: Sdf.ValueTypeName, usd_parent_schema: _UsdConnectable, input_node: hou.VopNode, input_node_output_name: str) -> None:
        """ Creates an input shader primitive, and connects its output 
            to the given shader's input, based on the input node information.
        """
    def connectUsdShaderRampInputToUsdShaderOutput(self, is_color_ramp: bool, usd_shader: _UsdShaderSchema, usd_shader_input_name: str, usd_input_shader_output_path: Sdf.Path | str) -> None:
        ''' Connects ramp input to the outupt of another shader.
            This expands the "virtual" connection of ramp into three
            arrays: basis, keys, and values.
        '''
    def createUsdShaderWithTranslator(self, shader_node: hou.VopNode, shader_node_output_name: str, usd_parent_schema: _UsdConnectable) -> Sdf.Path | str | None:
        """ Creates a USD shader using either this or another translator.
            Returns a path to the output of the translated USD shader primitive.
        """
    def createUsdShaderWithThisTranslator(self, shader_node: hou.VopNode, shader_node_output_name: str, usd_parent_schema: _UsdConnectable) -> Sdf.Path | str | None:
        """ Creates a USD shader (re-uses this translator object).
            Returns a path to the output of the translated USD shader primitive.
        """
    def createUsdShaderWithAnotherTranslator(self, shader_node: hou.VopNode, shader_node_output_name: str, usd_parent_schema: _UsdConnectable) -> str:
        """ Creates a USD shader (uses a new translator suited for the node).
            Returns a path to the output of the translated USD shader primitive.
        """
    def createUsdShaderOrGraph(self, shader_node: hou.VopNode, shader_node_output_name: str, usd_parent_schema: _UsdConnectable, usd_shader_prim_name: str | None) -> tuple[_UsdShaderSchema, list[str] | None]:
        """ Creates a USD primitive (shader or graph), given the shader node.
            Returns a tuple of the USD schema for the created primitive, 
            and the names of the shader node inputs to traverse and translate 
            to USD, to fully reflect (the portion of) the Houdini shader node 
            network originating from the given shader node.
        """
    def createUsdGraph(self, shader_node: hou.VopNode, shader_node_output_name: str, usd_parent_schema: _UsdConnectable, usd_shader_prim_name: str | None) -> _UsdShaderSchema:
        """ Creates and configures a USD graph primitive based on the given 
            Houdini shader node.
            Returns the USD graph schema for the created USD primitive.
        """
    def createUsdPrimvarReaderShader(self, shader_node: hou.VopNode, usd_parent_connectable: _UsdConnectable) -> Sdf.Path:
        """ Creates and configures the USD primvar reader shader primitive
            based on the given VOP node. 
            Returns a USD path to the output of the created USD primvar reader 
            shader primitive.
        """
    def createAndConnectUsdGraphChildShader(self, usd_graph: _UsdShaderSchema, usd_graph_output_name: str, usd_graph_output_type: Sdf.ValueTypeName, input_node: hou.VopNode, input_node_output_name: str) -> None:
        """ Creates a child USD shader inside the given USD parent graph, 
            and connects its output to graph's output.
        """
    def createAndConnectUsdGraphOutputToInput(self, usd_connectable: _UsdConnectable, usd_output_name: str, usd_output_type: Sdf.ValueTypeName, usd_src_connectable: _UsdConnectable, usd_src_input_name: str, usd_src_input_type: Sdf.ValueTypeName, input_node: hou.VopNode, input_node_output_name: str, ancestor_node: hou.VopNode | None) -> None:
        """ Creates an output on the USD connectable primitive and connects it 
            directly to an input of an ancestor connectable or its own input.
        """
    def createUsdGraphOutputConstantValue(self, usd_connectable: _UsdConnectable, usd_output_name: str, usd_output_type: Sdf.ValueTypeName, input_node: hou.VopNode, input_node_output_name: str) -> None:
        """ Authors a new value for the output attribute on the given USD 
            connectable parent schema (a Material or NodeGraph).
        """
    def createUsdShader(self, shader_node: hou.VopNode, shader_node_output_name: str, usd_parent_connectable: _UsdConnectable, usd_shader_prim_name: str | None = None) -> _UsdShaderSchema:
        """ Creates and configures a single USD shader primitive 
            based on the given Houdini shader node.
            Returns a USD shader schema for the created USD primitive.
        """
    def createUsdShaderAttributes(self, shader_node: hou.VopNode, usd_shader: _UsdShaderSchema) -> None:
        """ Creates and sets the shader input parameter attributes
            on the USD shader, given the Houdini shader node.
        """
    def updateUsdShaderAttributes(self, shader_node: hou.VopNode, shader_node_parameter_names: Collection[str], usd_shader_path: str | Sdf.Path) -> None:
        """ Re-translate the shader node parameters into USD shader attributes.

            This is the main entry point API for updating an existing
            USD shader primitive when only a small subset of Houdini node
            parameters have changed (and nothing else has changed).

            Does not create any new USD shader primitives, and 
            does not recursively process any input nodes.

            Note, if `shader_node_parameter_names` is empty, then this function
            assumes that any of the node's parameters may have changed, 
            thus it re-translates all applicable node parameters.
            If it's not empty, then it assumes that only the listed parameters 
            have changed, thus it re-translates only the listed node parameters.
        """
    def isNodeParmChanged(self, parameter_name: str | None, shader_node: hou.VopNode, shader_node_parameter_names: Collection[str] | None) -> bool:
        """ Returns true if node parameter has changed and affects USD shader.
        """
    def isUsdShaderInputChanged(self, input_name: str, parm_from_input_map: Mapping[str, str], shader_node: hou.VopNode, shader_node_parameter_names: Collection[str] | None) -> bool:
        """ Returns true if USD shader input attribute is affected 
            by the node parameter change.
        """
    def parmFromInputMap(self, shader_node: hou.VopNode) -> dict[str, str]:
        """ Builds and returns a map from a USD primitive input name 
            to a corresponding Houdini node parameter name.
        """
    def defineUsdPrim(self, vop_node: hou.VopNode, usd_prim_path: Sdf.Path | str, default_prim_type: str) -> _UsdShaderSchema:
        """ Creates a USD shader primitive at the given path based on 
            the given shader node, but does not author attributes on it,
            nor does it recursively follow any node inputs.
        """
    def defineUsdShader(self, shader_node: hou.VopNode, usd_shader_path: Sdf.Path | str) -> _UsdShaderSchema:
        """ Creates a USD shader primitive at the given path based on 
            the given shader node, but does not author attributes on it,
            nor does it recursively follow any node inputs.
        """
    def defineUsdGraph(self, shader_node: hou.VopNode, usd_graph_path: Sdf.Path | str) -> _UsdShaderSchema:
        """ Defines and returns a USD graph primitive. The shader node 
            may override the USD primitive type to Material or Shader, though.
        """
    def addUsdBasePrim(self, usd_prim: Usd.Prim, shader_node: hou.VopNode) -> None:
        """ Adds a reference, inheritance, or specialization of an existing
            (base) USD primitive to the given USD primitive `usd_prim`,
            based on the given Houdini shader node representing it.
        """
    def setInstanceableIfNeeded(self, usd_prim: Usd.Prim, shader_node: hou.VopNode) -> None:
        """ Sets the instanceable metadata on a shader prim, if needed.
        """
    def authorNodeGraphUIAttribs(self, usd_prim: Usd.Prim, vop_node: hou.VopNode) -> None:
        """ Authors UI node graph attributes (position and color)
            on the given USD prim from the given VOP node.
        """
    def usdOutputOfRepresentedPrimitive(self, shader_node: hou.VopNode, prim_output_name: str, prim_output_type: Sdf.ValueTypeName) -> UsdShade.Output | None:
        """ Returns an output of a USD primitive, if the given shader node
            represents such an existing primitive on the stage.
        """
    def createUsdPluginID(self, usd_plugin_schema: _UsdShaderSchema, plugin_node: hou.VopNode) -> None:
        """ Creates and sets a plugin ID for plugin-based primitive schema,
            translated from the given node. 
            In USD plugin-based prims don't have a dedicated schemas defined,
            but instad, use generic schma that has an ID attribute to 
            indicate specific implementation of the primitive.  Eg, 
            UsdShade.Shader, UsdLux.PluginLight, UsdLux.PluginLightFilter, etc.
        """
    def createUsdShaderID(self, usd_shader: _UsdShaderSchema, shader_node: hou.VopNode) -> None:
        """ Creates and sets the shader ID attribute on the given 
            USD shader schema (`usd_shader`).
        """
    def createUsdLightFilterID(self, usd_light_filter: UsdLux.LightFilter, filter_node: hou.VopNode) -> None:
        """ Creates and set the light filter ID attribute.
        """
    def createUsdShaderInputAttributes(self, usd_shader: _UsdShaderSchema, shader_node: hou.VopNode, shader_node_parameter_names: Collection[str] | None = None) -> None:
        """ Creates and sets input attributes on the given USD shader, 
            given the Houdini node that corresponds to it.

            If `shader_node_parameter_names` are given, only these parameters 
            will be considered for authoring (though some of them 
            may not be actually authored if they are at default value, etc).
        """
    def setPreviewShaderMetadata(self, usd_shader: _UsdShaderSchema, shader_node: hou.VopNode) -> None:
        """ Authors metadata tags on shader prim's attributes, that are used
            for authoring of the standard USD preview shader.
        """
    def createUsdShaderInput(self, usd_shader: _UsdShaderSchema, usd_shader_input_name: str, usd_shader_input_type: Sdf.ValueTypeName) -> UsdShade.Input:
        """ Creates an input on the given USD shader schema based
            on the node input information.
        """
    def createUsdShaderOutput(self, usd_shader: _UsdShaderSchema, usd_shader_output_name: str, usd_shader_output_type: Sdf.ValueTypeName) -> UsdShade.Output:
        """ Creates an input on the given USD shader schema based
            on the node input information.
        """
    def createUsdGraphInput(self, usd_connectable: _UsdConnectable, usd_input_name: str, usd_input_type: Sdf.ValueTypeName) -> UsdShade.Input:
        """ Creates an input on the USD connectable parent 
            (eg, Material or NodeGraph).
        """
    def createUsdGraphOutput(self, usd_connectable: _UsdConnectable, usd_output_name: str, usd_output_type: Sdf.ValueTypeName) -> UsdShade.Output:
        """ Creates an output on the USD connectable parent 
            (eg, Material or NodeGraph).
        """
    def setupUsdGraphInput(self, usd_input: UsdShade.Input, input_node: hou.VopNode, input_node_output_name: str, ancestor_node: hou.VopNode | None) -> None:
        """ Sets the value and metadata on the given USD ancestor input.
        """
    def connectUsdShaderInputToUsdShaderOutput(self, usd_shader: _UsdShaderSchema, usd_shader_input_name: str, usd_shader_input_type: Sdf.ValueTypeName, usd_input_shader_output_path: Sdf.Path | str | None) -> None:
        """ Connects an input of the given USD shader (`usd_shader`) 
            to the given output of another shader.
        """
    def connectUsdShaderInputToUsdGraphInput(self, usd_shader: _UsdShaderSchema, usd_shader_input_name: str, usd_shader_input_type: Sdf.ValueTypeName, usd_parent_connectable: _UsdConnectable, input_node: hou.VopNode, input_node_output_name: str) -> None:
        """ Connect the shader input to the input of the ancestor graph 
            (a Material or NodeGraph).
        """
    def connectUsdShaderInputToUsdMaterialInput(self, usd_shader: _UsdShaderSchema, usd_shader_input_name: str, usd_shader_input_type: Sdf.ValueTypeName, input_node: hou.VopNode, input_node_output_name: str) -> None:
        """ Connects the USD shader input to the input of the main ancestor
            (a Material or a NodeGraph).
        """
    def connectUsdMaterialOutputToUsdShaderOutput(self, main_output_name: str, main_output_type: Sdf.ValueTypeName, usd_shader_src_output_path: Sdf.Path | str) -> None:
        """ Connects the output of the main USD ancestor (Material or NodeGraph)
            to the given output of some USD primitive (Shader, NodeGraph, etc).
        """
    def connectUsdGraphOutputToUsdShaderOutput(self, usd_connectable: _UsdConnectable, usd_output_name: str, usd_output_type: Sdf.ValueTypeName, usd_shader_src_output_path: Sdf.Path | str | None) -> None:
        """ Connects the output of the given USD connctable parent (Material 
            or NodeGraph) to the given output of some USD primitive 
            (Shader, NodeGraph, etc).
        """
    def connectUsdShaderInputToUsdAncestorInput(self, usd_shader: _UsdShaderSchema, usd_shader_input_name: str, usd_shader_input_type: Sdf.ValueTypeName, usd_ancestor: _UsdConnectable, usd_ancestor_input_name: str, usd_ancestor_input_type: Sdf.ValueTypeName, input_node: hou.VopNode, input_node_output_name: str, ancestor_node: hou.VopNode | None) -> None:
        """ Connects the USD shader input to material input
        """
    def setUsdAncestorInputValue(self, parm_tuple: hou.ParmTuple | None, input_node: hou.VopNode, ancestor_input: UsdShade.Input) -> None:
        """ Authors an attribute value on the given ancestor input.
        """
    def setUsdAncestorInputMetadata(self, parm_tuple: hou.ParmTuple | None, input_node: hou.VopNode, ancestor_input: UsdShade.Input) -> None:
        """ Authors attribute metadata on the given ancestor input.
        """
    def usdShaderPrimitiveName(self, shader_node: hou.VopNode, usd_shader_prim_name: str | None) -> str:
        """ Returns the name of the USD shader primitive, 
            given the corresponding shader node that translates to it.
        """
    def usdShaderPrimitivePath(self, shader_node: hou.VopNode, usd_parent_connectable: _UsdConnectable, usd_shader_prim_name: str | None) -> Sdf.Path | str:
        """ Returns the full path to the USD shader primitive, 
            given its USD parent (eg Material or NodeGraph), 
            and the Houdini node translating into that shader primitive.
        """
    def usdShaderInputName(self, shader_node: hou.VopNode, shader_node_input_name: str | None) -> str:
        """ Returns the name of an input attribute of the USD shader prim, 
            given the shader node and its input name.
        """
    def usdShaderOutputName(self, shader_node: hou.VopNode, shader_node_output_name: str | None) -> str:
        """ Returns the name of an output attribute on the USD shader prim,
            given the shader node and its output name.
        """
    def usdMaterialOutputName(self, shader_node: hou.VopNode, shader_node_output_name: str, requested_shader_type: hou.EnumValue[hou.shaderType]) -> str:
        """ Returns the name of an output of the main ancestor (a Material
            or NodeGraph), that links it to the output of a USD shader 
            for the given shader type (eg, surface, displacement, etc).
        """
    def usdMaterialOutputType(self, shader_node: hou.VopNode, shader_node_output_name: str) -> Sdf.ValueTypeName:
        """ Returns the type of the output on the USD material prim that links 
            it to the USD shader for a given render taget and shading purpose.
        """
    def usdRenderContextName(self, shader_node: hou.VopNode, shader_node_output_name: str) -> str:
        ''' Returns the name of the render context used in the USD material 
            output name. Eg, "ri" for RenderMan context or "kma" for Karma.
        '''
    def usdShaderTypeToken(self, shader_node: hou.VopNode, shader_node_output_name: str, requested_shader_type: hou.EnumValue[hou.shaderType]) -> str:
        """ Returns the standard USD token string for the given shader type,
            (eg 'surface', 'displacement').  It is used for the USD material 
            output when connecting it to the USD shader output.
        """
    def usdShaderTypeTokenFromVopTypeName(self, vop_type_name: str) -> str:
        """ Returns the standard USD token string for the shader type
            deduced from the VOP type name.
        """
    def isShaderVopTypeName(self, vop_type_name: str | None) -> bool:
        """ Returns true if the vop type name represents a shader (eg surface).
            Otherwise, returns false (i.e., it represents a data type, eg int).
        """
    def usdShaderSourceType(self, shader_node: hou.VopNode) -> str:
        """ Returns the name that identifies the type of a shader source 
            Eg, 'glsl', 'vex', 'osl' (effectively, the shader language).
        """
    def usdShaderAssetOrID(self, shader_node: hou.VopNode) -> str:
        """ Returns the USD asset name or shader ID for the given shader node.
        """
    def sdfTypeFromNodeInput(self, node: hou.VopNode, input_name: str) -> Sdf.ValueTypeName:
        """ Returns the USD type given the node input.
        """
    def sdfTypeFromNodeOutput(self, node: hou.VopNode, output_name: str) -> Sdf.ValueTypeName:
        """ Returns the USD type given the node output.
        """
    def usdShaderOutputRenderType(self, node: hou.VopNode, output_name: str) -> str | None:
        """ Returns the USD shader output render type metadata to author.
        """
    def sdfTypeFromParentSubnetOutput(self, child: hou.VopNode, child_node_output_name: str) -> Sdf.ValueTypeName:
        """ Returns the Sdf type of the parent subnet's output that corresponds
            to the output of the given child node.
        """
    def inputNodeFromWire(self, wire: hou.OpNodeConnection) -> tuple[hou.VopNode | None, str]:
        """ Returns a tuple of an Houdini input node and its output name,
            given the connection wire between two Houdini nodes.
        """
    def parameterTranslator(self, parm_tuple: hou.ParmTuple) -> SimpleParmTranslator | RampParmTranslator | MultiParmTranslator | None:
        """ Returns a translator that can create and set a USD attribute that 
            corresponds to the given Houdini node parameter (hou.ParmTuple).
        """
    def simpleParameterTranslator(self, parm_tuple: hou.ParmTuple) -> SimpleParmTranslator:
        """ Returns a translator for simple parameters.
        """
    def rampParameterTranslator(self, parm_tuple: hou.ParmTuple) -> RampParmTranslator:
        """ Returns a translator for ramp parameters.
        """
    def multiParameterTranslator(self, parm_tuple: hou.ParmTuple) -> MultiParmTranslator:
        """ Returns a translator for multi-parameters.
        """

class ShaderTranslator:
    """ Translates Houdini shader nodes into USD shader primitives.
    """
    myID: int
    def __init__(self) -> None:
        """ Initialize member data.
        """
    def setTranslatorID(self, translator_id: int) -> None:
        """ Sets the translator ID. 
            The registry calls it to let the translator know its ID.
        """
    def translatorID(self) -> int:
        """ Gets the translator ID. 
            Translator IDs are not strictly necessary, but some translators
            use IDs for optimization. Eg, to continue using themselves for the
            translation of the subsequent Houdini nodes in the input chain
            traversal, instead of calling into the HOM API functions.
        """
    def matchesRenderMask(self, render_mask: str) -> bool:
        """ Returns true if the given render mask matches the render target for 
            which this translator translates the shader nodes into USD prims.
            Otherwise, returns false.
        """
    def beginMaterialTranslation(self, usd_stage: Usd.Stage, usd_material_path: str) -> None:
        """ Prepares the translator for translating shaders to the
            given material.
            This method is called before this translator is asked to translate
            any shader. Ie, before a call to createMaterialShader() method.
        """
    def endMaterialTranslation(self, usd_stage: Usd.Stage, usd_material_path: str) -> None:
        """ Cleans up the translator after translating all the shader to
            the given material.
            This method is called after this translator was asked to translate
            all the shaders. Ie, after all calls to createMaterialShader() 
            method.
        """
    def createMaterialShader(self, usd_stage: Usd.Stage, usd_material_path: str, usd_time_code: Usd.TimeCode, shader_node: hou.VopNode, shader_type: hou.EnumValue[hou.shaderType], shader_node_output_name: str) -> None:
        """ Creates a USD shader primitive that is a terminal shader 
            of the given USD material.  Ie, the translator will connect 
            the created shader primitive to the parent material primitive
            (via output attributes).

            usd_stage - UsdStage object on which to create the shader.
            usd_material_path - Path to the Material or the NodeGraph 
                primitive in which to create the shader. 
            usd_time_code - time code (frame) at which to evaluate shader 
                parameters and at which to set the primitive attributes.
            shader_node - Houdini node representing a shader.
            shader_type - The requested shader type to use (ie, hou.shaderType)
                in case the shader node implements several shaders 
                (eg, is a material builder) and the node lacks outputs
                to deduce the shader type.
            shader_node_output_name - The particular output of Houdini node that
                was used to arrive at the shader node that represents the
                shader to translate (in case the node has several shaders).
                The output name can be an empty string, if node has no outputs.
        """
    def createShader(self, usd_stage: Usd.Stage, usd_material_path: str, usd_parent_path: str, usd_shader_prim_name: str, usd_time_code: Usd.TimeCode, shader_node: hou.VopNode, shader_node_output_name: str) -> Sdf.Path | str | None:
        """ Creates a USD shader primitive that is part of a shader network
            chain. Ie, the translator will create a shader primitive 
            that the caller can use to connect as an input to another shader.

            Returns the path to the USD shader output attribute on the newly
            created shader primitive, that corresponds to the given 
            `shader_node_output_name` connector on the `shader_node`.

            usd_stage - UsdStage object on which to create the shader
            usd_material_path - Path to the main Material or NodeGraph 
                primitive in which to create the shader.
            usd_parent_path - Path to the parent primitive 
                directly inside which to create the shader.
            usd_shader_prim_name - Name of the shader primitive to create.
                It may be an empty string, in which case use shader_node's name.
            usd_time_code - time code (frame) at which to evaluate shader 
                parameters and at which to set the primitive attributes.
            shader_node - Houdini node representing a shader.
            shader_node_output_name - the output name of the Houdini node that 
                needs to be translated into USD shader output. 
        """
    def renderContextName(self, shader_node: hou.VopNode, shader_node_output_name: str) -> str:
        ''' Returns the name of the render context used in the USD material 
            output name. Eg, "ri" for RenderMan or "kma" for Karma.

            shader_node - Houdini node representing a shader.
            outupt_name - the output name of the Houdini node that needs to be
                translated into USD shader output. 
        '''
    def updateShaderParameters(self, usd_stage: Usd.Stage, usd_shader_path: str, usd_time_code: Usd.TimeCode, shader_node: hou.VopNode, shader_node_parameter_names: Collection[str]) -> None:
        """ Re-translates the parameters for the given shader.
            It allows targeted updates of USD shader primitives when
            a corresponding Houdini shader node's parameters changed,
            without the need to re-create the whole USD shader graph.

            usd_shader_path - USD path to the shader primitive to update.
            shader_node - Houdini node representing a shader that changed.
            shader_node_parameter_names - the list of names of the parameters 
                that changed.
                If the list is empty, any of the node's parameter may have
                changed. But if the list is not empty, then only the listed
                parameters have changed.
        """
    def shaderTranslatorHelper(self, translator_id: int, usd_stage: Usd.Stage, usd_material_path: str | None, usd_time_code: Usd.TimeCode) -> ShaderTranslatorHelper:
        """ Returns a translator helper that implements the actual logic
            of translating Houdini nodes into USD shaders.

            This is a convenience method to make it easier to derive
            custom translators from this class, without the need to repeat 
            the main API entry point methods such as createMaterialShader(). 
            Ie, it should suffice to override only this method (and 
            matchesRenderMask() method too), and then 
            implement the custom logic in the custom helper class 
            (usually derived from ShaderTranslatorHelper).
        """
