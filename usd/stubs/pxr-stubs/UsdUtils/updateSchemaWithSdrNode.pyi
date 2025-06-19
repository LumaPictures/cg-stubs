# mypy: disable-error-code="misc, override, no-redef"

import pxr.Sdf as Sdf
import pxr.Sdr as Sdr
import pxr.Tf as Tf
import pxr.Usd as Usd
import pxr.UsdShade as UsdShade
import pxr.UsdUtils.constantsGroup
import pxr.Vt as Vt
from pxr.UsdUtils.constantsGroup import ConstantsGroup as ConstantsGroup
from typing import ClassVar

class PropertyDefiningKeys(pxr.UsdUtils.constantsGroup.ConstantsGroup):
    CONNECTABILITY: ClassVar[str] = ...
    INTERNAL_DISPLAY_GROUP: ClassVar[str] = ...
    NULL_VALUE: ClassVar[str] = ...
    PROPERTY_NS_PREFIX_OVERRIDE: ClassVar[str] = ...
    SDF_VARIABILITY_UNIFORM_STRING: ClassVar[str] = ...
    SHADER_ID: ClassVar[str] = ...
    USD_SUPPRESS_PROPERTY: ClassVar[str] = ...
    USD_VARIABILITY: ClassVar[str] = ...
    WIDGET: ClassVar[str] = ...
    _all: ClassVar[tuple] = ...

class SchemaDefiningKeys(pxr.UsdUtils.constantsGroup.ConstantsGroup):
    API_SCHEMAS_FOR_ATTR_PRUNING: ClassVar[str] = ...
    API_SCHEMA_AUTO_APPLY_TO: ClassVar[str] = ...
    API_SCHEMA_CAN_ONLY_APPLY_TO: ClassVar[str] = ...
    IS_USD_SHADE_CONTAINER: ClassVar[str] = ...
    PROVIDES_USD_SHADE_CONNECTABLE_API_BEHAVIOR: ClassVar[str] = ...
    REQUIRES_USD_SHADE_ENCAPSULATION: ClassVar[str] = ...
    SCHEMA_BASE: ClassVar[str] = ...
    SCHEMA_KIND: ClassVar[str] = ...
    SCHEMA_NAME: ClassVar[str] = ...
    SCHEMA_PROPERTY_NS_PREFIX_OVERRIDE: ClassVar[str] = ...
    TF_TYPENAME_SUFFIX: ClassVar[str] = ...
    TYPED_SCHEMA_FOR_ATTR_PRUNING: ClassVar[str] = ...
    _all: ClassVar[tuple] = ...

class SchemaDefiningMiscConstants(pxr.UsdUtils.constantsGroup.ConstantsGroup):
    API_SCHEMA_BASE: ClassVar[str] = ...
    API_STRING: ClassVar[str] = ...
    NodeDefAPI: ClassVar[str] = ...
    SINGLE_APPLY_SCHEMA: ClassVar[str] = ...
    TYPED_SCHEMA: ClassVar[str] = ...
    USD_SOURCE_TYPE: ClassVar[str] = ...
    _all: ClassVar[tuple] = ...

def UpdateSchemaWithSdrNode(schemaLayer, sdrNode, renderContext: str = ..., overrideIdentifier: str = ...):
    '''
    Updates the given schemaLayer with primSpec and propertySpecs from sdrNode
    metadata. 

    A renderContext can be provided which is used in determining the
    shaderId namespace, which follows the pattern: 
    "<renderContext>:<SdrShaderNodeContext>:shaderId". Note that we are using a
    node\'s context (SDR_NODE_CONTEXT_TOKENS) here to construct the shaderId
    namespace, so shader parsers should make sure to use appropriate
    SDR_NODE_CONTEXT_TOKENS in the node definitions.

    overrideIdentifier parameter is the identifier which should be used when 
    the identifier of the node being processed differs from the one Sdr will 
    discover at runtime, such as when this function is def a node constructed 
    from an explicit asset path. This should only be used when clients know the 
    identifier being passed is the true identifier which sdr Runtime will 
    provide when querying using GetShaderNodeByIdentifierAndType, etc.

    It consumes the following attributes (that manifest as Sdr 
    metadata) in addition to many of the standard Sdr metadata
    specified and parsed (via its parser plugin).

    Node Level Metadata:
        - "schemaName": Name of the new schema populated from the given sdrNode
          (Required)
        - "schemaKind": Specifies the UsdSchemaKind for the schema being
          populated from the sdrNode. (Note that this does not support
          multiple apply schema kinds).
        - "schemaBase": Base schema from which the new schema should inherit
          from. Note this defaults to "APISchemaBase" for an API schema or 
          "Typed" for a concrete scheme.
        - "apiSchemasForAttrPruning": A list of core API schemas which will be
          composed together and any shared shader property from this prim
          definition is pruned from the resultant schema. 
        - "typedSchemaForAttrPruning": A core typed schema which will be
          composed together with the apiSchemasForAttrPruning and any shared 
          shader property from this prim definition is pruned from the 
          resultant schema. If no typedSchemaForAttrPruning is provided then 
          only the apiSchemasForAttrPruning are composed to create a prim 
          definition. This will only be used when creating an APISchema.
        - "apiSchemaAutoApplyTo": The schemas to which the sdrNode populated 
          API schema will autoApply to.
        - "apiSchemaCanOnlyApplyTo": If specified, the API schema generated 
          from the sdrNode can only be validly applied to this set of schemas.
        - "providesUsdShadeConnectableAPIBehavior": Used to enable a 
          connectability behavior for an API schema.
        - "isUsdShadeContainer": Only used when
          providesUsdShadeConnectableAPIBehavior is set to true. Marks the
          connectable prim as a UsdShade container type.
        - "requiresUsdShadeEncapsulation": Only used when
          providesUsdShadeConnectableAPIBehavior is set to true. Configures the
          UsdShade encapsulation rules governing its connectableBehavior.
        - "tfTypeNameSuffix": Class name which will get registered with TfType 
          system. This gets appended to the domain name to register with TfType.
        - "schemaPropertyNSPrefixOverride": Node level metadata which can drive
          all node\'s properties namespace prefix. This can be useful for
          non connectable nodes which should not get UsdShade inputs and outputs
          namespace prefix.

    Property Level Metadata:
        - "usdVariability": Property level metadata which specifies a specific 
          sdrNodeProperty should have its USD variability set to Uniform or 
          Varying
        - "usdSuppressProperty": A property level metadata which determines if 
          the property should be suppressed from translation from args to 
          property spec.
        - "propertyNSPrefixOverride": Provides a way to override a property\'s
          namespace from the default (inputs:/outputs:) or from a node\'s
          schemaPropertyNSPrefixOverride metadata.

    Sdr Property Metadata to SdfPropertySpec Translations
        - A "null" value for Widget sdrProperty metadata translates to 
          SdfPropertySpec Hidden metadata.
        - SdrProperty\'s Help metadata (Label metadata if Help metadata not 
          provided) translates to SdfPropertySpec\'s Documentation string 
          metadata.
        - SdrProperty\'s Page metadata translates to SdfPropertySpec\'s
          DisplayGroup metadata.
        - SdrProperty\'s Label metadata translates to SdfPropertySpec\'s
          DisplayName metadata.
        - SdrProperty\'s Options translates to SdfPropertySpec\'s AllowedTokens.
        - SdrProperty\'s Default value translates to SdfPropertySpec\'s Default
          value.
        - Connectable input properties translates to InterfaceOnly
          SdfPropertySpec\'s CONNECTABILITY.
    '''
def _CreateAttrSpecFromNodeAttribute(primSpec, prop, primDefForAttrPruning, schemaPropertyNSPrefixOverride, isSdrInput: bool = ...): ...
def _IsNSPrefixConnectableAPICompliant(nsPrefix): ...
