# mypy: disable-error-code="misc, override, no-redef"

import Boost.Python
import pxr.Sdf
import pxr.Tf
import pxr.Usd
from typing import Any, ClassVar, overload

__MFB_FULL_PACKAGE_NAME: str

class DenoisePass(pxr.Usd.Typed):
    """
    A RenderDenoisePass generates renders via a denoising process.


    This may be the same renderer that a pipeline uses for UsdRender, or
    may be a separate one. Notably, a RenderDenoisePass requires another
    Pass to be present for it to operate. The denoising process itself is
    not generative, and requires images inputs to operate.

    As denoising integration varies so widely across pipelines, all
    implementation details are left to pipeline-specific prims that
    inherit from RenderDenoisePass.
    """
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None:
        """
        Construct a UsdRenderDenoisePass on UsdPrim C{prim}.


        Equivalent to UsdRenderDenoisePass::Get (prim.GetStage(),
        prim.GetPath()) for a *valid* C{prim}, but will not immediately throw
        an error for an invalid C{prim}
        """
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None:
        """
        Construct a UsdRenderDenoisePass on the prim held by C{schemaObj}.


        Should be preferred over UsdRenderDenoisePass (schemaObj.GetPrim()),
        as it preserves SchemaBase state.
        """
    @staticmethod
    def Define(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> DenoisePass:
        """
        Attempt to ensure a *UsdPrim* adhering to this schema at C{path} is
        defined (according to UsdPrim::IsDefined() ) on this stage.


        If a prim adhering to this schema at C{path} is already defined on
        this stage, return that prim. Otherwise author an *SdfPrimSpec* with
        *specifier* == *SdfSpecifierDef* and this schema's prim type name for
        the prim at C{path} at the current EditTarget. Author *SdfPrimSpec* s
        with C{specifier} == *SdfSpecifierDef* and empty typeName at the
        current EditTarget for any nonexistent, or existing but not *Defined*
        ancestors.

        The given *path* must be an absolute prim path that does not contain
        any variant selections.

        If it is impossible to author any of the necessary PrimSpecs, (for
        example, in case *path* cannot map to the current UsdEditTarget 's
        namespace) issue an error and return an invalid *UsdPrim*.

        Note that this method may return a defined prim whose typeName does
        not specify this schema class, in case a stronger typeName opinion
        overrides the opinion at the current EditTarget.
        """
    @staticmethod
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> DenoisePass:
        """
        Return a UsdRenderDenoisePass holding the prim adhering to this schema
        at C{path} on C{stage}.


        If no prim exists at C{path} on C{stage}, or if the prim at that path
        does not adhere to this schema, return an invalid schema object. This
        is shorthand for the following: ::

          UsdRenderDenoisePass(stage->GetPrimAtPath(path));

        """
    @staticmethod
    def GetSchemaAttributeNames(includeInherited: bool = ...) -> list[str]:
        """
        Return a vector of names of all pre-declared attributes for this
        schema class and all its ancestor classes.


        Does not include attributes that may be authored by custom/extended
        methods of the schemas involved.
        """
    @staticmethod
    def _GetStaticTfType() -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...

class Pass(pxr.Usd.Typed):
    '''
    A RenderPass prim encapsulates the necessary information to generate
    multipass renders.


    It houses properties for generating dependencies and the necessary
    commands to run to generate renders, as well as visibility controls
    for the scene. While RenderSettings describes the information needed
    to generate images from a single invocation of a renderer, RenderPass
    describes the additional information needed to generate a time varying
    set of images.

    There are two consumers of RenderPass prims - a runtime executable
    that generates images from usdRender prims, and pipeline specific code
    that translates between usdRender prims and the pipeline\'s resource
    scheduling software. We\'ll refer to the latter as\'job submission
    code\'.

    The objects that are relevant to the render is specified via the
    renderVisibility collection (UsdCollectionAPI) and can be accessed via
    GetRenderVisibilityCollectionAPI() . This collection has includeRoot
    set to true so that all objects participate in the render by default.
    To render only a specific set of objects, there are two options. One
    is to modify the collection paths to explicitly exclude objects that
    don\'t participate in the render, assuming it is known; the other
    option is to set includeRoot to false and explicitly include the
    desired objects. These are complementary approaches that may each be
    preferable depending on the scenario.

    The name of the prim is used as the pass\'s name.

    For any described attribute *Fallback* *Value* or *Allowed* *Values*
    below that are text/tokens, the actual token is published and defined
    in UsdRenderTokens. So to set an attribute to the value"rightHanded",
    use UsdRenderTokens->rightHanded as the value.
    '''
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None:
        """
        Construct a UsdRenderPass on UsdPrim C{prim}.


        Equivalent to UsdRenderPass::Get (prim.GetStage(), prim.GetPath()) for
        a *valid* C{prim}, but will not immediately throw an error for an
        invalid C{prim}
        """
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None:
        """
        Construct a UsdRenderPass on the prim held by C{schemaObj}.


        Should be preferred over UsdRenderPass (schemaObj.GetPrim()), as it
        preserves SchemaBase state.
        """
    def CreateCommandAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetCommandAttr() , and also Create vs Get Property Methods for
        when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateDenoiseEnableAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetDenoiseEnableAttr() , and also Create vs Get Property Methods
        for when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateDenoisePassRel(self) -> pxr.Usd.Relationship:
        """
        See GetDenoisePassRel() , and also Create vs Get Property Methods for
        when to use Get vs Create.
        """
    def CreateFileNameAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetFileNameAttr() , and also Create vs Get Property Methods for
        when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateInputPassesRel(self) -> pxr.Usd.Relationship:
        """
        See GetInputPassesRel() , and also Create vs Get Property Methods for
        when to use Get vs Create.
        """
    def CreatePassTypeAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetPassTypeAttr() , and also Create vs Get Property Methods for
        when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateRenderSourceRel(self) -> pxr.Usd.Relationship:
        """
        See GetRenderSourceRel() , and also Create vs Get Property Methods for
        when to use Get vs Create.
        """
    @staticmethod
    def Define(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> Pass:
        """
        Attempt to ensure a *UsdPrim* adhering to this schema at C{path} is
        defined (according to UsdPrim::IsDefined() ) on this stage.


        If a prim adhering to this schema at C{path} is already defined on
        this stage, return that prim. Otherwise author an *SdfPrimSpec* with
        *specifier* == *SdfSpecifierDef* and this schema's prim type name for
        the prim at C{path} at the current EditTarget. Author *SdfPrimSpec* s
        with C{specifier} == *SdfSpecifierDef* and empty typeName at the
        current EditTarget for any nonexistent, or existing but not *Defined*
        ancestors.

        The given *path* must be an absolute prim path that does not contain
        any variant selections.

        If it is impossible to author any of the necessary PrimSpecs, (for
        example, in case *path* cannot map to the current UsdEditTarget 's
        namespace) issue an error and return an invalid *UsdPrim*.

        Note that this method may return a defined prim whose typeName does
        not specify this schema class, in case a stronger typeName opinion
        overrides the opinion at the current EditTarget.
        """
    @staticmethod
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> Pass:
        """
        Return a UsdRenderPass holding the prim adhering to this schema at
        C{path} on C{stage}.


        If no prim exists at C{path} on C{stage}, or if the prim at that path
        does not adhere to this schema, return an invalid schema object. This
        is shorthand for the following: ::

          UsdRenderPass(stage->GetPrimAtPath(path));

        """
    def GetCommandAttr(self) -> pxr.Usd.Attribute:
        '''
        The command to run in order to generate renders for this pass.


        The job submission code can use this to properly send tasks to the job
        scheduling software that will generate products.

        The command can contain variables that will be substituted
        appropriately during submission, as seen in the example below with
        {fileName}.

        For example: command[0] ="prman"command[1] ="-progress"command[2]
        ="-pixelvariance"command[3] ="-0.15"command[4] ="{fileName}"# the
        fileName property will be substituted

        Declaration

        C{uniform string[] command}

        C++ Type

        VtArray<std::string>

        Usd Type

        SdfValueTypeNames->StringArray

        Variability

        SdfVariabilityUniform
        '''
    def GetDenoiseEnableAttr(self) -> pxr.Usd.Attribute:
        """
        When True, this Pass pass should be denoised.



        Declaration

        C{uniform bool denoise:enable = 0}

        C++ Type

        bool

        Usd Type

        SdfValueTypeNames->Bool

        Variability

        SdfVariabilityUniform
        """
    def GetDenoisePassRel(self) -> pxr.Usd.Relationship:
        """
        The The UsdRenderDenoisePass prim from which to source denoise
        settings.
        """
    def GetFileNameAttr(self) -> pxr.Usd.Attribute:
        """
        The asset that contains the rendering prims or other information
        needed to render this pass.



        Declaration

        C{uniform asset fileName}

        C++ Type

        SdfAssetPath

        Usd Type

        SdfValueTypeNames->Asset

        Variability

        SdfVariabilityUniform
        """
    def GetInputPassesRel(self) -> pxr.Usd.Relationship:
        """
        The set of other Passes that this Pass depends on in order to be
        constructed properly.


        For example, a Pass A may generate a texture, which is then used as an
        input to Pass B.

        By default, usdRender makes some assumptions about the relationship
        between this prim and the prims listed in inputPasses. Namely, when
        per-frame tasks are generated from these pass prims, usdRender will
        assume a one-to-one relationship between tasks that share their frame
        number. Consider a pass named'composite'whose *inputPasses* targets a
        Pass prim named'beauty.  By default, each frame for'composite  will
        depend on the same frame from'beauty': beauty.1 ->composite.1 beauty.2
        ->composite.2 etc

        The consumer of this RenderPass graph of inputs will need to resolve
        the transitive dependencies.
        """
    def GetPassTypeAttr(self) -> pxr.Usd.Attribute:
        """
        A string used to categorize differently structured or executed types
        of passes within a customized pipeline.


        For example, when multiple DCC's (e.g. Houdini, Katana, Nuke) each
        compute and contribute different Products to a final result, it may be
        clearest and most flexible to create a separate RenderPass for each.

        Declaration

        C{uniform token passType}

        C++ Type

        TfToken

        Usd Type

        SdfValueTypeNames->Token

        Variability

        SdfVariabilityUniform
        """
    def GetRenderSourceRel(self) -> pxr.Usd.Relationship:
        """
        The source prim to render from.


        If *fileName* is not present, the source is assumed to be a
        RenderSettings prim present in the current Usd stage. If fileName is
        present, the source should be found in the file there. This
        relationship might target a string attribute on this or another prim
        that identifies the appropriate object in the external container.

        For example, for a Usd-backed pass, this would point to a
        RenderSettings prim. Houdini passes would point to a Rop. Nuke passes
        would point to a write node.
        """
    def GetRenderVisibilityCollectionAPI(self) -> pxr.Usd.CollectionAPI:
        """
        Return the UsdCollectionAPI interface used for examining and modifying
        the render visibility of this prim.
        """
    @staticmethod
    def GetSchemaAttributeNames(includeInherited: bool = ...) -> list[str]:
        """
        Return a vector of names of all pre-declared attributes for this
        schema class and all its ancestor classes.


        Does not include attributes that may be authored by custom/extended
        methods of the schemas involved.
        """
    @staticmethod
    def _GetStaticTfType() -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...

class Product(SettingsBase):
    '''
    A UsdRenderProduct describes an image or other file-like artifact
    produced by a render.


    A RenderProduct combines one or more RenderVars into a file or
    interactive buffer. It also provides all the controls established in
    UsdRenderSettingsBase as optional overrides to whatever the owning
    UsdRenderSettings prim dictates.

    Specific renderers may support additional settings, such as a way to
    configure compression settings, filetype metadata, and so forth. Such
    settings can be encoded using renderer-specific API schemas applied to
    the product prim.

    For any described attribute *Fallback* *Value* or *Allowed* *Values*
    below that are text/tokens, the actual token is published and defined
    in UsdRenderTokens. So to set an attribute to the value"rightHanded",
    use UsdRenderTokens->rightHanded as the value.
    '''
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None:
        """
        Construct a UsdRenderProduct on UsdPrim C{prim}.


        Equivalent to UsdRenderProduct::Get (prim.GetStage(), prim.GetPath())
        for a *valid* C{prim}, but will not immediately throw an error for an
        invalid C{prim}
        """
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None:
        """
        Construct a UsdRenderProduct on the prim held by C{schemaObj}.


        Should be preferred over UsdRenderProduct (schemaObj.GetPrim()), as it
        preserves SchemaBase state.
        """
    def CreateOrderedVarsRel(self) -> pxr.Usd.Relationship:
        """
        See GetOrderedVarsRel() , and also Create vs Get Property Methods for
        when to use Get vs Create.
        """
    def CreateProductNameAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetProductNameAttr() , and also Create vs Get Property Methods for
        when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateProductTypeAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetProductTypeAttr() , and also Create vs Get Property Methods for
        when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    @staticmethod
    def Define(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> Product:
        """
        Attempt to ensure a *UsdPrim* adhering to this schema at C{path} is
        defined (according to UsdPrim::IsDefined() ) on this stage.


        If a prim adhering to this schema at C{path} is already defined on
        this stage, return that prim. Otherwise author an *SdfPrimSpec* with
        *specifier* == *SdfSpecifierDef* and this schema's prim type name for
        the prim at C{path} at the current EditTarget. Author *SdfPrimSpec* s
        with C{specifier} == *SdfSpecifierDef* and empty typeName at the
        current EditTarget for any nonexistent, or existing but not *Defined*
        ancestors.

        The given *path* must be an absolute prim path that does not contain
        any variant selections.

        If it is impossible to author any of the necessary PrimSpecs, (for
        example, in case *path* cannot map to the current UsdEditTarget 's
        namespace) issue an error and return an invalid *UsdPrim*.

        Note that this method may return a defined prim whose typeName does
        not specify this schema class, in case a stronger typeName opinion
        overrides the opinion at the current EditTarget.
        """
    @staticmethod
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> Product:
        """
        Return a UsdRenderProduct holding the prim adhering to this schema at
        C{path} on C{stage}.


        If no prim exists at C{path} on C{stage}, or if the prim at that path
        does not adhere to this schema, return an invalid schema object. This
        is shorthand for the following: ::

          UsdRenderProduct(stage->GetPrimAtPath(path));

        """
    def GetOrderedVarsRel(self) -> pxr.Usd.Relationship:
        """
        Specifies the RenderVars that should be consumed and combined into the
        final product.


        If ordering is relevant to the output driver, then the ordering of
        targets in this relationship provides the order to use.
        """
    def GetProductNameAttr(self) -> pxr.Usd.Attribute:
        '''
        Specifies the name that the output/display driver should give the
        product.


        This is provided as-authored to the driver, whose responsibility it is
        to situate the product on a filesystem or other storage, in the
        desired location.

        Declaration

        C{token productName =""}

        C++ Type

        TfToken

        Usd Type

        SdfValueTypeNames->Token
        '''
    def GetProductTypeAttr(self) -> pxr.Usd.Attribute:
        '''
        The type of output to produce.


        The default,"raster", indicates a 2D image.

        In the future, UsdRender may define additional product types.

        Declaration

        C{uniform token productType ="raster"}

        C++ Type

        TfToken

        Usd Type

        SdfValueTypeNames->Token

        Variability

        SdfVariabilityUniform
        '''
    @staticmethod
    def GetSchemaAttributeNames(includeInherited: bool = ...) -> list[str]:
        """
        Return a vector of names of all pre-declared attributes for this
        schema class and all its ancestor classes.


        Does not include attributes that may be authored by custom/extended
        methods of the schemas involved.
        """
    @staticmethod
    def _GetStaticTfType() -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...

class Settings(SettingsBase):
    '''
    A UsdRenderSettings prim specifies global settings for a render
    process, including an enumeration of the RenderProducts that should
    result, and the UsdGeomImageable purposes that should be rendered.


    How settings affect rendering

    For any described attribute *Fallback* *Value* or *Allowed* *Values*
    below that are text/tokens, the actual token is published and defined
    in UsdRenderTokens. So to set an attribute to the value"rightHanded",
    use UsdRenderTokens->rightHanded as the value.
    '''
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None:
        """
        Construct a UsdRenderSettings on UsdPrim C{prim}.


        Equivalent to UsdRenderSettings::Get (prim.GetStage(), prim.GetPath())
        for a *valid* C{prim}, but will not immediately throw an error for an
        invalid C{prim}
        """
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None:
        """
        Construct a UsdRenderSettings on the prim held by C{schemaObj}.


        Should be preferred over UsdRenderSettings (schemaObj.GetPrim()), as
        it preserves SchemaBase state.
        """
    def CreateIncludedPurposesAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetIncludedPurposesAttr() , and also Create vs Get Property
        Methods for when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateMaterialBindingPurposesAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetMaterialBindingPurposesAttr() , and also Create vs Get Property
        Methods for when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateProductsRel(self) -> pxr.Usd.Relationship:
        """
        See GetProductsRel() , and also Create vs Get Property Methods for
        when to use Get vs Create.
        """
    def CreateRenderingColorSpaceAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetRenderingColorSpaceAttr() , and also Create vs Get Property
        Methods for when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    @staticmethod
    def Define(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> Settings:
        """
        Attempt to ensure a *UsdPrim* adhering to this schema at C{path} is
        defined (according to UsdPrim::IsDefined() ) on this stage.


        If a prim adhering to this schema at C{path} is already defined on
        this stage, return that prim. Otherwise author an *SdfPrimSpec* with
        *specifier* == *SdfSpecifierDef* and this schema's prim type name for
        the prim at C{path} at the current EditTarget. Author *SdfPrimSpec* s
        with C{specifier} == *SdfSpecifierDef* and empty typeName at the
        current EditTarget for any nonexistent, or existing but not *Defined*
        ancestors.

        The given *path* must be an absolute prim path that does not contain
        any variant selections.

        If it is impossible to author any of the necessary PrimSpecs, (for
        example, in case *path* cannot map to the current UsdEditTarget 's
        namespace) issue an error and return an invalid *UsdPrim*.

        Note that this method may return a defined prim whose typeName does
        not specify this schema class, in case a stronger typeName opinion
        overrides the opinion at the current EditTarget.
        """
    @staticmethod
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> Settings:
        """
        Return a UsdRenderSettings holding the prim adhering to this schema at
        C{path} on C{stage}.


        If no prim exists at C{path} on C{stage}, or if the prim at that path
        does not adhere to this schema, return an invalid schema object. This
        is shorthand for the following: ::

          UsdRenderSettings(stage->GetPrimAtPath(path));

        """
    def GetIncludedPurposesAttr(self) -> pxr.Usd.Attribute:
        '''
        The list of UsdGeomImageable *purpose* values that should be included
        in the render.


        Note this cannot be specified per-RenderProduct because it is a
        statement of which geometry is present.

        Declaration

        C{uniform token[] includedPurposes = ["default","render"]}

        C++ Type

        VtArray<TfToken>

        Usd Type

        SdfValueTypeNames->TokenArray

        Variability

        SdfVariabilityUniform
        '''
    def GetMaterialBindingPurposesAttr(self) -> pxr.Usd.Attribute:
        '''
        Ordered list of material purposes to consider when resolving material
        bindings in the scene.


        The empty string indicates the"allPurpose"binding.

        Declaration

        C{uniform token[] materialBindingPurposes = ["full",""]}

        C++ Type

        VtArray<TfToken>

        Usd Type

        SdfValueTypeNames->TokenArray

        Variability

        SdfVariabilityUniform

        Allowed Values

        full, preview,""
        '''
    def GetProductsRel(self) -> pxr.Usd.Relationship:
        """
        The set of RenderProducts the render should produce.


        This relationship should target UsdRenderProduct prims. If no
        *products* are specified, an application should produce an rgb image
        according to the RenderSettings configuration, to a default display or
        image name.
        """
    def GetRenderingColorSpaceAttr(self) -> pxr.Usd.Attribute:
        """
        Describes a renderer's working (linear) colorSpace where all the
        renderer/shader math is expected to happen.


        When no renderingColorSpace is provided, renderer should use its own
        default.

        Declaration

        C{uniform token renderingColorSpace}

        C++ Type

        TfToken

        Usd Type

        SdfValueTypeNames->Token

        Variability

        SdfVariabilityUniform
        """
    @staticmethod
    def GetSchemaAttributeNames(includeInherited: bool = ...) -> list[str]:
        """
        Return a vector of names of all pre-declared attributes for this
        schema class and all its ancestor classes.


        Does not include attributes that may be authored by custom/extended
        methods of the schemas involved.
        """
    @staticmethod
    def GetStageRenderSettings(_stage: pxr.Usd.Stage, /) -> Settings:
        """
        Fetch and return C{stage} 's render settings, as indicated by root
        layer metadata.


        If unauthored, or the metadata does not refer to a valid
        UsdRenderSettings prim, this will return an invalid UsdRenderSettings
        prim.
        """
    @staticmethod
    def _GetStaticTfType() -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...

class SettingsBase(pxr.Usd.Typed):
    '''
    Abstract base class that defines render settings that can be specified
    on either a RenderSettings prim or a RenderProduct prim.


    For any described attribute *Fallback* *Value* or *Allowed* *Values*
    below that are text/tokens, the actual token is published and defined
    in UsdRenderTokens. So to set an attribute to the value"rightHanded",
    use UsdRenderTokens->rightHanded as the value.
    '''
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None:
        """
        Construct a UsdRenderSettingsBase on UsdPrim C{prim}.


        Equivalent to UsdRenderSettingsBase::Get (prim.GetStage(),
        prim.GetPath()) for a *valid* C{prim}, but will not immediately throw
        an error for an invalid C{prim}
        """
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None:
        """
        Construct a UsdRenderSettingsBase on the prim held by C{schemaObj}.


        Should be preferred over UsdRenderSettingsBase (schemaObj.GetPrim()),
        as it preserves SchemaBase state.
        """
    def CreateAspectRatioConformPolicyAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetAspectRatioConformPolicyAttr() , and also Create vs Get
        Property Methods for when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateCameraRel(self) -> pxr.Usd.Relationship:
        """
        See GetCameraRel() , and also Create vs Get Property Methods for when
        to use Get vs Create.
        """
    def CreateDataWindowNDCAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetDataWindowNDCAttr() , and also Create vs Get Property Methods
        for when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateDisableDepthOfFieldAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetDisableDepthOfFieldAttr() , and also Create vs Get Property
        Methods for when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateDisableMotionBlurAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetDisableMotionBlurAttr() , and also Create vs Get Property
        Methods for when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateInstantaneousShutterAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetInstantaneousShutterAttr() , and also Create vs Get Property
        Methods for when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreatePixelAspectRatioAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetPixelAspectRatioAttr() , and also Create vs Get Property
        Methods for when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateResolutionAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetResolutionAttr() , and also Create vs Get Property Methods for
        when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    @staticmethod
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> SettingsBase:
        """
        Return a UsdRenderSettingsBase holding the prim adhering to this
        schema at C{path} on C{stage}.


        If no prim exists at C{path} on C{stage}, or if the prim at that path
        does not adhere to this schema, return an invalid schema object. This
        is shorthand for the following: ::

          UsdRenderSettingsBase(stage->GetPrimAtPath(path));

        """
    def GetAspectRatioConformPolicyAttr(self) -> pxr.Usd.Attribute:
        '''
        Indicates the policy to use to resolve an aspect ratio mismatch
        between the camera aperture and image settings.


        This policy allows a standard render setting to do something
        reasonable given varying camera inputs.

        The camera aperture aspect ratio is determined by the aperture
        atributes on the UsdGeomCamera.

        The image aspect ratio is determined by the resolution and
        pixelAspectRatio attributes in the render settings.

           - "expandAperture": if necessary, expand the aperture to fit the
             image, exposing additional scene content

           - "cropAperture": if necessary, crop the aperture to fit the image,
             cropping scene content

           - "adjustApertureWidth": if necessary, adjust aperture width to
             make its aspect ratio match the image

           - "adjustApertureHeight": if necessary, adjust aperture height to
             make its aspect ratio match the image

           - "adjustPixelAspectRatio": compute pixelAspectRatio to make the
             image exactly cover the aperture; disregards existing attribute value
             of pixelAspectRatio

        Declaration

        C{uniform token aspectRatioConformPolicy ="expandAperture"}

        C++ Type

        TfToken

        Usd Type

        SdfValueTypeNames->Token

        Variability

        SdfVariabilityUniform

        Allowed Values

        expandAperture, cropAperture, adjustApertureWidth,
        adjustApertureHeight, adjustPixelAspectRatio
        '''
    def GetCameraRel(self) -> pxr.Usd.Relationship:
        """
        The *camera* relationship specifies the primary camera to use in a
        render.


        It must target a UsdGeomCamera.
        """
    def GetDataWindowNDCAttr(self) -> pxr.Usd.Attribute:
        """
        dataWindowNDC specifies the axis-aligned rectangular region in the
        adjusted aperture window within which the renderer should produce
        data.


        It is specified as (xmin, ymin, xmax, ymax) in normalized device
        coordinates, where the range 0 to 1 corresponds to the aperture. (0,0)
        corresponds to the bottom-left corner and (1,1) corresponds to the
        upper-right corner.

        Specifying a window outside the unit square will produce overscan
        data. Specifying a window that does not cover the unit square will
        produce a cropped render.

        A pixel is included in the rendered result if the pixel center is
        contained by the data window. This is consistent with standard rules
        used by polygon rasterization engines. UsdRenderRasterization

        The data window is expressed in NDC so that cropping and overscan may
        be resolution independent. In interactive workflows, incremental
        cropping and resolution adjustment may be intermixed to isolate and
        examine parts of the scene. In compositing workflows, overscan may be
        used to support image post-processing kernels, and reduced-resolution
        proxy renders may be used for faster iteration.

        The dataWindow:ndc coordinate system references the aperture after any
        adjustments required by aspectRatioConformPolicy.

        Declaration

        C{uniform float4 dataWindowNDC = (0, 0, 1, 1)}

        C++ Type

        GfVec4f

        Usd Type

        SdfValueTypeNames->Float4

        Variability

        SdfVariabilityUniform
        """
    def GetDisableDepthOfFieldAttr(self) -> pxr.Usd.Attribute:
        """
        Disable all depth of field by setting F-stop of the targeted camera to
        infinity.



        Declaration

        C{uniform bool disableDepthOfField = 0}

        C++ Type

        bool

        Usd Type

        SdfValueTypeNames->Bool

        Variability

        SdfVariabilityUniform
        """
    def GetDisableMotionBlurAttr(self) -> pxr.Usd.Attribute:
        """
        Disable all motion blur by setting the shutter interval of the
        targeted camera to [0,0] - that is, take only one sample, namely at
        the current time code.



        Declaration

        C{uniform bool disableMotionBlur = 0}

        C++ Type

        bool

        Usd Type

        SdfValueTypeNames->Bool

        Variability

        SdfVariabilityUniform
        """
    def GetInstantaneousShutterAttr(self) -> pxr.Usd.Attribute:
        """
        Deprecated - use disableMotionBlur instead.


        Override the targeted *camera* 's *shutterClose* to be equal to the
        value of its *shutterOpen*, to produce a zero-width shutter interval.
        This gives us a convenient way to disable motion blur.

        Declaration

        C{uniform bool instantaneousShutter = 0}

        C++ Type

        bool

        Usd Type

        SdfValueTypeNames->Bool

        Variability

        SdfVariabilityUniform
        """
    def GetPixelAspectRatioAttr(self) -> pxr.Usd.Attribute:
        """
        The aspect ratio (width/height) of image pixels.


        The default ratio 1.0 indicates square pixels.

        Declaration

        C{uniform float pixelAspectRatio = 1}

        C++ Type

        float

        Usd Type

        SdfValueTypeNames->Float

        Variability

        SdfVariabilityUniform
        """
    def GetResolutionAttr(self) -> pxr.Usd.Attribute:
        """
        The image pixel resolution, corresponding to the camera's screen
        window.



        Declaration

        C{uniform int2 resolution = (2048, 1080)}

        C++ Type

        GfVec2i

        Usd Type

        SdfValueTypeNames->Int2

        Variability

        SdfVariabilityUniform
        """
    @staticmethod
    def GetSchemaAttributeNames(includeInherited: bool = ...) -> list[str]:
        """
        Return a vector of names of all pre-declared attributes for this
        schema class and all its ancestor classes.


        Does not include attributes that may be authored by custom/extended
        methods of the schemas involved.
        """
    @staticmethod
    def _GetStaticTfType() -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...

class Tokens(Boost.Python.instance):
    RenderDenoisePass: ClassVar[str] = ...  # read-only
    RenderPass: ClassVar[str] = ...  # read-only
    RenderProduct: ClassVar[str] = ...  # read-only
    RenderSettings: ClassVar[str] = ...  # read-only
    RenderSettingsBase: ClassVar[str] = ...  # read-only
    RenderVar: ClassVar[str] = ...  # read-only
    adjustApertureHeight: ClassVar[str] = ...  # read-only
    adjustApertureWidth: ClassVar[str] = ...  # read-only
    adjustPixelAspectRatio: ClassVar[str] = ...  # read-only
    aspectRatioConformPolicy: ClassVar[str] = ...  # read-only
    camera: ClassVar[str] = ...  # read-only
    collectionRenderVisibilityIncludeRoot: ClassVar[str] = ...  # read-only
    color3f: ClassVar[str] = ...  # read-only
    command: ClassVar[str] = ...  # read-only
    cropAperture: ClassVar[str] = ...  # read-only
    dataType: ClassVar[str] = ...  # read-only
    dataWindowNDC: ClassVar[str] = ...  # read-only
    denoiseEnable: ClassVar[str] = ...  # read-only
    denoisePass: ClassVar[str] = ...  # read-only
    disableDepthOfField: ClassVar[str] = ...  # read-only
    disableMotionBlur: ClassVar[str] = ...  # read-only
    expandAperture: ClassVar[str] = ...  # read-only
    fileName: ClassVar[str] = ...  # read-only
    full: ClassVar[str] = ...  # read-only
    includedPurposes: ClassVar[str] = ...  # read-only
    inputPasses: ClassVar[str] = ...  # read-only
    instantaneousShutter: ClassVar[str] = ...  # read-only
    intrinsic: ClassVar[str] = ...  # read-only
    lpe: ClassVar[str] = ...  # read-only
    materialBindingPurposes: ClassVar[str] = ...  # read-only
    orderedVars: ClassVar[str] = ...  # read-only
    passType: ClassVar[str] = ...  # read-only
    pixelAspectRatio: ClassVar[str] = ...  # read-only
    preview: ClassVar[str] = ...  # read-only
    primvar: ClassVar[str] = ...  # read-only
    productName: ClassVar[str] = ...  # read-only
    productType: ClassVar[str] = ...  # read-only
    products: ClassVar[str] = ...  # read-only
    raster: ClassVar[str] = ...  # read-only
    raw: ClassVar[str] = ...  # read-only
    renderSettingsPrimPath: ClassVar[str] = ...  # read-only
    renderSource: ClassVar[str] = ...  # read-only
    renderVisibility: ClassVar[str] = ...  # read-only
    renderingColorSpace: ClassVar[str] = ...  # read-only
    resolution: ClassVar[str] = ...  # read-only
    sourceName: ClassVar[str] = ...  # read-only
    sourceType: ClassVar[str] = ...  # read-only
    def __init__(self, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """

class Var(pxr.Usd.Typed):
    '''
    A UsdRenderVar describes a custom data variable for a render to
    produce.


    The prim describes the source of the data, which can be a shader
    output or an LPE (Light Path Expression), and also allows encoding of
    (generally renderer-specific) parameters that configure the renderer
    for computing the variable.

    The name of the RenderVar prim drives the name of the data variable
    that the renderer will produce.

    In the future, UsdRender may standardize RenderVar representation for
    well-known variables under the sourceType C{intrinsic}, such as *r*,
    *g*, *b*, *a*, *z*, or *id*. For any described attribute *Fallback*
    *Value* or *Allowed* *Values* below that are text/tokens, the actual
    token is published and defined in UsdRenderTokens. So to set an
    attribute to the value"rightHanded", use UsdRenderTokens->rightHanded
    as the value.
    '''
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None:
        """
        Construct a UsdRenderVar on UsdPrim C{prim}.


        Equivalent to UsdRenderVar::Get (prim.GetStage(), prim.GetPath()) for
        a *valid* C{prim}, but will not immediately throw an error for an
        invalid C{prim}
        """
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None:
        """
        Construct a UsdRenderVar on the prim held by C{schemaObj}.


        Should be preferred over UsdRenderVar (schemaObj.GetPrim()), as it
        preserves SchemaBase state.
        """
    def CreateDataTypeAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetDataTypeAttr() , and also Create vs Get Property Methods for
        when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateSourceNameAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetSourceNameAttr() , and also Create vs Get Property Methods for
        when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    def CreateSourceTypeAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute:
        """
        See GetSourceTypeAttr() , and also Create vs Get Property Methods for
        when to use Get vs Create.


        If specified, author C{defaultValue} as the attribute's default,
        sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
        - the default for C{writeSparsely} is C{false}.
        """
    @staticmethod
    def Define(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> Var:
        """
        Attempt to ensure a *UsdPrim* adhering to this schema at C{path} is
        defined (according to UsdPrim::IsDefined() ) on this stage.


        If a prim adhering to this schema at C{path} is already defined on
        this stage, return that prim. Otherwise author an *SdfPrimSpec* with
        *specifier* == *SdfSpecifierDef* and this schema's prim type name for
        the prim at C{path} at the current EditTarget. Author *SdfPrimSpec* s
        with C{specifier} == *SdfSpecifierDef* and empty typeName at the
        current EditTarget for any nonexistent, or existing but not *Defined*
        ancestors.

        The given *path* must be an absolute prim path that does not contain
        any variant selections.

        If it is impossible to author any of the necessary PrimSpecs, (for
        example, in case *path* cannot map to the current UsdEditTarget 's
        namespace) issue an error and return an invalid *UsdPrim*.

        Note that this method may return a defined prim whose typeName does
        not specify this schema class, in case a stronger typeName opinion
        overrides the opinion at the current EditTarget.
        """
    @staticmethod
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> Var:
        """
        Return a UsdRenderVar holding the prim adhering to this schema at
        C{path} on C{stage}.


        If no prim exists at C{path} on C{stage}, or if the prim at that path
        does not adhere to this schema, return an invalid schema object. This
        is shorthand for the following: ::

          UsdRenderVar(stage->GetPrimAtPath(path));

        """
    def GetDataTypeAttr(self) -> pxr.Usd.Attribute:
        '''
        The type of this channel, as a USD attribute type.



        Declaration

        C{uniform token dataType ="color3f"}

        C++ Type

        TfToken

        Usd Type

        SdfValueTypeNames->Token

        Variability

        SdfVariabilityUniform
        '''
    @staticmethod
    def GetSchemaAttributeNames(includeInherited: bool = ...) -> list[str]:
        """
        Return a vector of names of all pre-declared attributes for this
        schema class and all its ancestor classes.


        Does not include attributes that may be authored by custom/extended
        methods of the schemas involved.
        """
    def GetSourceNameAttr(self) -> pxr.Usd.Attribute:
        '''
        The renderer should look for an output of this name as the computed
        value for the RenderVar.



        Declaration

        C{uniform string sourceName =""}

        C++ Type

        std::string

        Usd Type

        SdfValueTypeNames->String

        Variability

        SdfVariabilityUniform
        '''
    def GetSourceTypeAttr(self) -> pxr.Usd.Attribute:
        '''
        Indicates the type of the source.



           - "raw": The name should be passed directly to the renderer. This
             is the default behavior.

           - "primvar": This source represents the name of a primvar. Some
             renderers may use this to ensure that the primvar is provided; other
             renderers may require that a suitable material network be provided, in
             which case this is simply an advisory setting.

           - "lpe": Specifies a Light Path Expression in the OSL Light Path
             Expressions language as the source for this RenderVar. Some renderers
             may use extensions to that syntax, which will necessarily be non-
             portable.

           - "intrinsic": This setting is currently unimplemented, but
             represents a future namespace for UsdRender to provide portable
             baseline RenderVars, such as camera depth, that may have varying
             implementations for each renderer.

        Declaration

        C{uniform token sourceType ="raw"}

        C++ Type

        TfToken

        Usd Type

        SdfValueTypeNames->Token

        Variability

        SdfVariabilityUniform

        Allowed Values

        raw, primvar, lpe, intrinsic
        '''
    @staticmethod
    def _GetStaticTfType() -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...
