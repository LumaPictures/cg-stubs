# mypy: disable-error-code="misc, override, no-redef"

import pxr.Ndr as Ndr
import pxr.Sdr as Sdr
import pxr.Tf as Tf
from pxr.Sdf import SdfTypes as SdfTypes

def GetType(property):
    """
    Given a property (SdrShaderProperty), return the SdfValueTypeName type.
    """
def IsNodeOSL(node):
    """
    Determines if the given node has an OSL source type.
    """
def TestBasicNode(node, nodeSourceType, nodeDefinitionURI, nodeImplementationURI):
    """
    Test basic, non-shader-specific correctness on the specified node.
    """
def TestBasicProperties(node):
    """
    Test the correctness of the properties on the specified node (only the
    non-shading-specific aspects).
    """
def TestShaderPropertiesNode(node):
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
def TestShaderSpecificNode(node):
    """
    Test shader-specific correctness on the specified node.
    """
def TestShadingProperties(node):
    """
    Test the correctness of the properties on the specified node (only the
    shading-specific aspects).
    """
