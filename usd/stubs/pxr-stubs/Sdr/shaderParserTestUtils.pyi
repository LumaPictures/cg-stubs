from pxr import Ndr as Ndr, Sdr as Sdr, Tf as Tf

def IsNodeOSL(node):
    """
    Determines if the given node has an OSL source type.
    """
def GetType(property):
    """
    Given a property (SdrShaderProperty), return the SdfValueTypeName type.
    """
def TestBasicProperties(node) -> None:
    """
    Test the correctness of the properties on the specified node (only the
    non-shading-specific aspects).
    """
def TestShadingProperties(node) -> None:
    """
    Test the correctness of the properties on the specified node (only the
    shading-specific aspects).
    """
def TestBasicNode(node, nodeSourceType, nodeDefinitionURI, nodeImplementationURI) -> None:
    """
    Test basic, non-shader-specific correctness on the specified node.
    """
def TestShaderSpecificNode(node) -> None:
    """
    Test shader-specific correctness on the specified node.
    """
def TestShaderPropertiesNode(node) -> None:
    """
    Tests property correctness on the specified shader node, which must be
    one of the following pre-defined nodes:
    * 'TestShaderPropertiesNodeOSL'
    * 'TestShaderPropertiesNodeARGS'
    * 'TestShaderPropertiesNodeUSD'
    These pre-defined nodes have a property of every type that Sdr supports.

    Property correctness is defined as:
    * The shader property has the expected SdrPropertyType
    * The shader property has the expected SdfValueTypeName
    * If the shader property has a default value, the default value's type
      matches the shader property's type
    """
